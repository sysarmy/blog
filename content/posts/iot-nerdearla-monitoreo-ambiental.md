---
Title: "Sistema IoT para monitoreo ambiental en Nerdearla: arquitectura, hardware y aprendizajes"
Description: "Del home lab a Nerdearla: cómo construí un sistema IoT de calidad del aire que funcionó en un evento con miles de personas — y una red de gente que me sostuvo."
date: 2026-10-06
draft: false
markup: markdown

Keywords:
  - iot
  - distributed-architecture
  - monitoring
  - amazon-ec2
  - infrastructure-as-code
Tags:
  - iot
  - distributed-architecture
  - monitoring
  - amazon-ec2
  - infrastructure-as-code
Topics:
  - iot
  - monitoring
  - cloud
  - nerdearla

Thumbnail: assets/nerdearla-iot-portada.webp
socialImage: assets/nerdearla-iot-portada.webp
featuredImage: assets/nerdearla-iot-portada.webp
---

Estoy muy contenta de poder compartir finalmente parte del trabajo que estuve haciendo durante el último mes para **Nerdearla**, junto con el equipo de Nerdearla — Eduardo Casarero, Emilio Nagy (Nachi) y Lole.

<!--more-->

Mi intención al escribirlo es también que esta experiencia sirva para alentar a más chicas y mujeres a animarse a desafíos técnicos como este.

Mi profesión principal es DevOps. En mi día a día trabajo sobre todo alrededor de infraestructura, automatización, observabilidad y sistemas distribuidos.

IoT es algo diferente, y me gusta porque me obliga a cruzar mundos que normalmente aparecen separados: software, infraestructura, electrónica, hardware y, sobre todo, problemas del mundo físico.

Desde chica me interesó la ecología y la idea de entender mejor nuestro entorno. Hoy me interesa especialmente pensar cómo podemos usar la tecnología para construir un mundo un poco mejor: más accesible, más consciente de su entorno y también más amable con las personas que tienen sensibilidades sensoriales y neurodivergencias.

Hace aproximadamente un mes me invitaron a desarrollar un sistema IoT para medir distintas condiciones ambientales durante Nerdearla de este año, y luego a compartir en una entrevista en vivo cómo armar una estación de medición de calidad del aire de forma sencilla y accesible.

La verdad es que me quedé bastante sorprendida cuando me escribieron. Venía trabajando con IoT como parte de mi tesis de Licenciatura, pero no esperaba que apareciera una oportunidad así.

Así que dije que sí.

Inmediatamente recurrí a mis compañeras de AWS Women in Cloud (WiC), con quienes había estado estudiando Infraestructura en la Universidad de la Marina Mercante. Me alentaron muchísimo y me ayudaron a encontrar el coraje para meterme de lleno en el proyecto.

Mientras empezaba a contarle a la gente lo que estábamos haciendo, empecé a escuchar motivos muy personales por los que este tipo de mediciones puede importar. Alguien me contó que a su papá le encantaría saber la humedad porque le afecta a las articulaciones. Otra persona me dijo que tiene asma y que le gustaría poder acceder a esta información.

Eso hizo que el proyecto se sintiera mucho más real.

## Del home lab al evento

Mi interés por IoT empezó hace mucho. El año pasado estuve trabajando con una maestra de primaria amiga para desarrollar ideas sobre robótica para sus sobrinas. Este interés se agudizó este año con un curso de IoT con Agustín Candia en la UNLP que tomé como optativa. Me gustó tanto que empecé a conversar con Agustín y Laura Fava sobre hacer mi tesis con ellos en el LINTI (Laboratorio de Investigación en Nuevas Tecnologías Informáticas de la UNLP).

Originalmente estaba pensando en trabajar con caudalímetros de agua para un municipio —un problema muy concreto y actual— cuando apareció la posibilidad de Nerdearla.

Le pregunté a Agustín y Laura si el proyecto de Nerdearla podía funcionar como una pre-tesis. Me contaron que en el LINTI también estaban trabajando con proyectos de calidad del aire, y eso abrió una conversación sobre participar en los proyectos existentes de mediciones ambientales, y que esto podría servir como experiencia previa.

Lo que nos interesa en común es cómo podemos construir sistemas de medición ambiental que sean accesibles, abiertos y económicos para comunidades y cooperativas locales, y que eventualmente puedan escalar.

También quedaron algunas ideas afuera de este proyecto. Por ejemplo, me interesa especialmente la firma inmutable de las mediciones, algo que había explorado en el trabajo final de IoT y que me gustaría seguir investigando.

## Construir para un entorno real

Nerdearla planteaba desafíos muy distintos de los experimentos que había hecho en casa.

Importaba la escala del lugar. También el hecho de que teníamos poco tiempo, hardware limitado y muy poca información previa sobre cómo se iban a comportar la red y el entorno físico una vez que decenas de miles de personas estuvieran circulando por el edificio.

En mis experimentos había encontrado que los picos de transmisión de Wi-Fi al enviar mensajes MQTT podían provocar ocasionalmente *brownouts* en algunas placas ESP32. Un brownout es una caída momentánea de tensión: la radio pide un pico de corriente que la fuente no llega a entregar, y la placa se reinicia.

Dado el poco tiempo disponible, decidí no dedicar esfuerzos a resolver el funcionamiento con baterías, ya que por experiencia previa esto también requiere hacer configuraciones finas sobre el uso de recursos para lo cual no había tiempo. En cambio, me concentré en tener fuentes de alimentación confiables y en resolver los problemas de conectividad y almacenamiento con memoria flash y otras estrategias de caché.

También teníamos distintas placas ESP32, incluyendo algunas más económicas con Wi-Fi de menor rango. Todas contaban con Wi-Fi de 2,4 GHz y Bluetooth. Inclusive si hubiéramos tenido placas más nuevas con Wi-Fi de 5 GHz, lo cual tiene otras posibilidades, también requiere más electricidad. No estaba convencida de que invertir en eso resolvería el problema de conectividad en un evento con tanta gente.

Agustín sugirió que primero nos aseguráramos de tener fuentes de alimentación robustas y después trabajáramos sobre las soluciones de software.

Fue una decisión importante.

## Infraestructura

{{< figure src="assets/nerdearla-iot-arquitectura.webp" alt="Diagrama de flujo de la arquitectura de código" caption="Diagrama de flujo de la arquitectura de código" position="center" captionPosition="center" >}}
El equipo de Nerdearla quería tener un host virtual centralizado, saliendo del setup en LAN para mayor autonomía durante las pruebas previas.

Consideramos usar una VM en su servidor privado con acceso mediante un túnel, pero como el esquema con MQTT/Mosquitto usa TCP directamente y no HTTP, para esta arquitectura tenía más sentido una VM accesible desde Internet.

Propuse una instancia pequeña de **AWS (EC2)** con IP pública, suficiente para ejecutar el backend de los nodos, la observabilidad y un pequeño sitio web estático donde los asistentes pudieran consultar qué salas estaban más frescas, con mejor aire o más silenciosas.

El backend es un **Docker Compose** sencillo. El flujo de datos es una sola línea:

```
Nodos ESP32  --MQTT/TLS:443-->  Mosquitto  --Telegraf-->  InfluxDB  --Grafana-->  dashboards
```

Un detalle que condicionó todo el diseño: en la red del venue el único puerto de salida confiable era el 443. Entonces publiqué el broker MQTT **sobre TLS directamente en el 443**, no sobre HTTP. Esto es MQTT crudo cifrado, no WebSockets:

```ini
# mosquitto.conf
allow_anonymous false
password_file /mosquitto/config/passwd

# Listener interno (solo red de Docker, para Telegraf)
listener 1883 0.0.0.0

# Listener público: MQTT over TLS en el 443 (el único puerto que el venue deja salir)
listener 443 0.0.0.0
certfile /mosquitto/config/certs/fullchain.pem
keyfile  /mosquitto/config/certs/privkey.pem
```

El certificado es de Let's Encrypt. En el firmware de cada nodo embebo la raíz pública (ISRG Root X1) para validar la cadena del broker, así la conexión es cifrada de punta a punta sin depender de un proxy intermedio.

Elegí **Telegraf** en lugar de Node-RED porque los requerimientos eran relativamente simples y, para este caso, un enfoque basado en archivos de configuración se adaptaba mejor. Cada nodo publica un JSON a un topic con la forma `iot/<type>/<device>/telemetry`; Telegraf lo consume, convierte `type` y `device` en tags, y usa el `ts` del payload como timestamp de InfluxDB:

```toml
# telegraf.conf
[[inputs.mqtt_consumer]]
  servers   = ["tcp://mosquitto:1883"]
  topics    = ["iot/+/+/telemetry"]
  data_format    = "json"
  tag_keys       = ["type", "device"]
  json_time_key  = "ts"         
  json_time_format = "unix"
  name_override  = "telemetry"

[[outputs.influxdb]]
  urls     = ["http://influxdb:8086"]
  database = "iot"
```

Que el timestamp lo ponga el nodo (y no el servidor) es clave: una lectura atrasada por una caída de Wi-Fi se inserta en InfluxDB en el momento en que realmente ocurrió, no cuando llegó. Más abajo explico cómo el firmware aprovecha esto.

La observabilidad es **Grafana**, expuesta solo en `localhost` y publicada hacia afuera por un túnel, nunca abriendo un puerto de más. El sitio estático lo sirve un `nginx:alpine`, y un pequeño script de Python consulta InfluxDB cada 10 segundos y escribe un `latest.json` que la página lee *same-origin*.

También tuve un pequeño momento creativo: le puse un nombre poético al sitio con influencia andina, y diseñé un logo inspirado en ideas de conciencia ambiental, y trabajé el diseño de la página con un amigo que me ayudó para aliviar la carga de trabajo.

El backend se provisiona con **Ansible**. El playbook también incluye medidas básicas de *hardening*: SSH solo por clave, sin root, y `fail2ban`.

```yaml
# ansible/roles/hardening/tasks/main.yml
- name: Endurecer sshd_config (solo key, sin root)
  ansible.builtin.lineinfile:
    path: /etc/ssh/sshd_config
    regexp: '^#?\s*{{ item.key }}\s+'
    line:   '{{ item.key }} {{ item.value }}'
    validate: /usr/sbin/sshd -t -f %s
  loop:
    - { key: PasswordAuthentication, value: 'no' }
    - { key: PermitRootLogin,        value: 'no' }
  notify: restart sshd

- name: Instalar fail2ban
  ansible.builtin.apt: { name: fail2ban, state: present, update_cache: true }
```

Los secretos viven cifrados con **SOPS** y se inyectan al `.env` en tiempo de provisión, nunca en el repo.

## El firmware: una sola base, varias placas

Después vino la parte física.

Teníamos que conseguir cajas para los nodos. Algunas las compramos en una tienda online y otras fueron impresas en 3D por un voluntario.

Coordinamos qué componentes comprar a partir de las mediciones que el equipo quería obtener. Terminamos usando sensores **SCD40/SCD41** (CO₂, temperatura y humedad) y **micrófonos MEMS INMP441** (nivel de ruido por I2S).

Me enviaron todo a casa y empecé a soldar y cablear.

Los micrófonos eran particularmente difíciles de soldar. El primero lo soldé al revés para poder ver las etiquetas más fácilmente.

Funcionaba igual.

Después le agarré la mano y pude terminar todos los nodos a tiempo y al derecho ya conociendo las etiquetas.

También tuve momentos bastante frustrantes con algunas de las placas más económicas. Agregué una placa propia y compré algunas **ESP32-C3** para reemplazar otras. El problema es que cada variante de ESP32 (C3, S3, NodeMCU clásico) tiene pines distintos y hasta periféricos I2S distintos. En lugar de mantener tres firmwares, mantengo **uno solo** y selecciono la placa con un `#define` antes de flashear:

```c
#define BOARD_S3       1
#define BOARD_NODEMCU  2
#define BOARD_C3       3

#define BOARD BOARD_C3   // <-- se cambia por placa

#if   BOARD == BOARD_S3
  #define SCD_SDA 8
  #define SCD_SCL 9
  #define I2S_BCK 5
  #define I2S_WS  4
  #define I2S_DIN 6
#elif BOARD == BOARD_NODEMCU
  #define SCD_SDA 21
  #define SCD_SCL 22
  #define I2S_BCK 26
  #define I2S_WS  25
  #define I2S_DIN 33
#elif BOARD == BOARD_C3
  #define SCD_SDA 4     // evita strapping / flash / USB del C3
  #define SCD_SCL 5
  #define I2S_BCK 6
  #define I2S_WS  7
  #define I2S_DIN 10
#else
  #error "Definí BOARD = BOARD_S3 / BOARD_NODEMCU / BOARD_C3"
#endif
```

Aparecieron detalles que no esperaba. El mismo micrófono INMP441 leído por el periférico I2S de cada chip deja la muestra de 24 bits en distinta posición dentro de la palabra de 32 bits, así que el mismo desplazamiento de bits da un nivel distinto por placa. Por eso a cada variante le agregué un `MIC_DB_OFFSET`, que calibré en vivo contra una app de sonómetro en el celular.

En una próxima iteración me gustaría poder contar con sonómetro profesional en el mismo lugar de instalación.

## Sobrevivir a los brownouts: store-and-forward en el nodo

El riesgo real del evento era perder datos cuando el Wi-Fi se pusiera intermitente o cuando un pico de radio reiniciara una placa. Lo resolví en el propio nodo, con un patrón **store-and-forward** parecido al snapshot de una base de datos: una cola en RAM que drena a MQTT, y cada 5 minutos, si cambió, un volcado a la memoria flash (LittleFS) para sobrevivir un reboot.

Dos decisiones hacen que funcione.

Primero, drenar **de a poco, nunca en ráfaga**. Una ráfaga de Wi-Fi es justo lo que vuelve a disparar el brownout en una fuente marginal, así que mando como mucho 2 mensajes cada 500 ms:

```c
// Drena de a poco: una ráfaga de WiFi puede re-disparar el brownout.
// Hasta 2 mensajes cada 500ms = ~4/s.
void bufDrain() {
  static uint32_t lastDrain = 0;
  if (bufCount == 0 || !mqtt.connected() || millis() - lastDrain < 500) return;
  lastDrain = millis();
  for (int k = 0; k < 2 && bufCount > 0 && mqtt.connected(); k++) {
    char payload[320];
    buildPayload(payload, sizeof(payload), ring[bufHead]);
    if (!mqtt.publish(TOPIC, payload)) break;  // sin ACK: reintenta después
    bufHead = (bufHead + 1) % BUF_CAP;
    bufCount--;
  }
}
```

Segundo, cada lectura viaja con **su propio timestamp**. Una medición que quedó demorada en la cola llega tarde, pero entra en InfluxDB en el momento en que realmente ocurrió, así que la serie temporal no tiene huecos ni corrimientos. La cola guarda hasta ~12 horas de datos en RAM; si se llena, pisa la más vieja; y el `seq` monótono permite detectar si se perdió algún mensaje.

Mientras tanto, los días seguían pasando. El sistema todavía no estaba terminado.

Pude probar el sistema distribuido con la ayuda de algunos amigos, lo que me dio la confianza necesaria para llevarlo al evento.

## Y finalmente llegó el momento

Por responsabilidad hacia clientes no podía pedir el día libre en el trabajo para estar durante todo el *setup*, así que estuve enviando algunas instrucciones de manera remota.

Al principio, los nodos no estaban enviando nada.

El problema resultó ser un carácter acentuado en el nombre de la red Wi-Fi.

Lo cambiaron.

Y, de repente, todos los nodos aparecieron online.

Fue increíble.

{{< figure src="assets/nerdearla-iot-sitio-ui.webp" alt="El sitio en vivo, consultado desde el navegador" caption="El sitio en vivo, consultado desde el navegador" position="center" captionPosition="center" >}}
{{< figure src="assets/nerdearla-iot-sitio.webp" alt="El sitio estático sirviendo en un display del evento" caption="El sitio estático sirviendo en un display del evento" position="center" captionPosition="center" >}}
{{< figure src="assets/nerdearla-iot-grafana.webp" alt="Mediciones en Grafana para personal (backroom del evento)" caption="Mediciones en Grafana para personal (backroom del evento)" position="center" captionPosition="center" >}}
Cuando empezó a entrar la gente, el Wi-Fi empezó a funcionar de manera intermitente para algunos nodos. Pero aun así pudimos obtener suficientes métricas como para comparar los distintos espacios. Acá es donde el buffer en el nodo hizo su trabajo: lo que no se podía enviar en el momento quedaba guardado y entraba después, en su tiempo correcto.

Fue fascinante ver cómo las mediciones cambiaban momento a momento a medida que el edificio se llenaba. Esto permitió que el personal de Nerdearla pudiera tomar medidas para prevenir la sobre-ocupación y refrescar las salas entre sesiones.

También hubo un par de anécdotas que me quedaron grabadas.

En un momento entré a Nerdearla con algunos nodos extra y terminé conversando con un asistente muy aficionado a la electrónica y que trabaja con electronica armando escape rooms. Miró los nodos y empezó a identificar los componentes, incluso los modelos de las placas. Reconoció hasta el micrófono que yo había soldado al revés, y nos reímos un rato.

Fuimos a instalar un nodo extra en el coworking silencioso y uno de los speakers principales del evento —a quien, para mi vergüenza, no reconocí en ese momento— me cedió su lugar y su alargue para que pudiéramos instalarlo.

Me dijo “I think it’s important to measure the CO₂, and I really need to get some sunlight.”. Solo cuando fui a ver su panel me dí cuenta de su importancia.

Me sentí comprendida, aunque cada uno por motivos distintos.

Yo estaba agotada —llevaba días durmiendo muy poco— y al principio ni siquiera tenía una noción clara de qué estaba pasando. Pero a medida que empezó a llegar feedback, para el viernes al mediodía finalmente sentí que todo estaba funcionando de manera bastante fluida.

También había diseñado un nodo para medir consumo eléctrico, con una pinza amperométrica SCT-013 y un ADC ADS1115. Pudimos ponerlo a funcionar durante el segundo día, una vez que encontramos un lugar adecuado para instalarlo, y aunque su posicionamiento en el lugar (con muchas columnas y rodeado de gente que iba y venía), generó varios problemas de conectividad, conseguimos algunas mediciones.

En un momento tuve que pedir un lápiz soldador para arreglar un componente, y me guiaron hasta un espacio tranquilo donde conversé con trabajadoras del lugar fascinadas con el proceso.

{{< figure src="assets/nerdearla-iot-soldando.webp" alt="Soldando el nodo de medición de corriente" caption="Soldando el nodo de medición de corriente" position="center" captionPosition="center" >}}
Ver todo el sistema funcionando en un lugar lleno de gente fue increíblemente emocionante.

Lo que había empezado como pequeños experimentos en mi home lab terminó convirtiéndose en un sistema IoT distribuido funcionando en un entorno real, con restricciones reales y personas usando los resultados.

Y aprendí muchísimo en el proceso.

## Agradecimientos

Y nada de esto habría sido posible sin el apoyo incondicional de **Javier Perales**, que me ayudó con el diseño de la página web, vino a acompañarme durante los primeros dos días y después fue a mi casa a cuidar a mi gatita, que se había quedado sola. También estuvo **Federico Meza**, un amigo electricista que nos dio una mano logística con la medición eléctrica y su instalación.

Gracias a **Eduardo, Nachi y Lole** de Nerdearla; a **Agustín y Laura** en el LINTI; a los voluntarios que ayudaron con el hardware; a mis amigos que me ayudaron a probar el sistema; y a todas las personas que me alentaron a decir que sí a este proyecto.

También quiero agradecer a mis compañeras de **AWS Women in Cloud**, que estuvieron en Nerdearla como *community partners*. En medio del ritmo intenso, que varias de ellas —especialmente **Silvina Belén Aponte Díaz**— se acercaran a buscarme para darme apoyo fue algo que me sostuvo mucho. Quiero agradecer de corazón a **Guadalupe Tulín**, que me acompañó en la parte logística, además del apoyo criterioso de diseño y difusión; y una mención especial a **Dai Rodríguez, Alejandra Leuno y Laura Bolaños**, que me sostuvieron y apoyaron durante y después. **Delia Alomo** me compartió su experiencia y me alentó a publicar en la comunidad.

Y quiero agradecer especialmente a mi equipo de trabajo, que me hizo el aguante mientras fui a hacer la instalación y para que pudiera estar presente durante el armado.

Tener ese tipo de apoyo hizo una diferencia enorme: me permitió tomar algo que venía experimentando como parte de mis estudios y llevarlo a un entorno real.

Ojalá más chicas y mujeres se animen a estos desafíos. Yo empecé con dudas y miedos, pero terminé con un sistema funcionando en un evento real. Si yo pude, muchas más pueden.

Estoy muy agradecida con todas las personas que hicieron posible que esto sucediera.
