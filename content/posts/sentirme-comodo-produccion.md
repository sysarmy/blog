---
Title: "Cómo sentirme cómodo en producción"
Description: "Mi camino para sentirme cómodo en ambiente de producción"
Keywords:
- principiantes
- productidad
- novato
- aprendizaje
- mejores-practicas

Tags:
- sysarmy
- dev
- desarrolladores
- mejores-practicas

Thumbnail: assets/sentirme-comodo-produccion.jpg
socialImage: assets/sentirme-comodo-produccion.jpg
featuredImage: assets/sentirme-comodo-produccion.jpg

Topics:
- dev
- desarrollo
- software
- mejores-practicas

markup: markdown
date: 2023-11-02
draft: false
---

_La versión original de este post se puede encontrar en [Better Programming](https://betterprogramming.pub/the-path-of-getting-comfortable-in-production-c88456146f00) (inglés)._

Hace 4 años, era un desarrollador bastante decente, he estado haciendo desarrollo para PCs de escritorio por casi 6 años, incluso he tenido a cargo un pequeño equipo, pero nunca tuve la oportunidad de trabajar con sistemas distribuidos de alta disponibilidad que aprovechan ciclos de entrega cortos.

Hace 4 años hice el cambio, apostando todo en una compañía de [SaaS (Software as a Service)](https://es.wikipedia.org/wiki/Software_como_servicio) saliendo de mi zona de confort a nuevas tecnologías. Fue entonces que aprendí de esto llamado “producción” — lo que pasa después de la última entrada de código en el IDE, y lo que pasa después de que mi código es enviado a “la nube”, que era desconocido para mí hasta ese momento.

Mirando hacia atrás, puedo decir con confianza que **sentirse cómodo en producción es un viaje que toma tiempo**, requiere un conjunto de habilidades bastante diferentes a las de escribir código, y mucho trabajo colaborativo.

Así que si sos un desarrollador que nunca recibió una alerta de producción, o no entendés del todo qué pasa luego de que CI termina su parte — ¡este artículo es exáctamente para vos! No voy a explicar todo eso en detalles, PERO, voy a describir el camino que he tomado, y con suerte inspirarte y hacerte este viaje más fácil.


## Paso 1 — Hacete amigos en los equipos de Ops/SRE
Estás por NO entender un montón de cosas. ¡Vas a sentirte perdido un montón de veces! Vas a necesitar “alguien de dentro” con quien hablar.

Como muchos de los procesos, herramientas, y prácticas van a ser específicas e internas de la compañía — Google solo te va a ayudar un poco — vas a necesitar un mentor.


## Paso 2 — Revisá tu Definición de Terminado (DOD, Definition of Done)
Una función que anda es buena, una función probada es mejor, y una función probada automáticamente es increíble. No terminaste, sin embargo — ¿cómo te asegurás a largo plazo tu función anda en producción? ¿Cómo podés investigar errores en esa función de acá a 6 meses? ¿Cómo te asegurás de que la estabilidad general del sistema se mantiene intacta?

Tenés que cambiar tu forma de pensar — la estabilidad del software evoluciona y cambia según pasa el tiempo, por lo tanto tu trabajo se termina solo cuando todo lo del párrafo anterior está cubierto. Y eso incluye:

1. Monitoreo — El comportamiento de tu función es monitoreado, y no afecta el comportamiento general del sistema (las [4 métricas de oro](https://sre.google/sre-book/monitoring-distributed-systems/) son un buen comienzo).
2. Registros — asegurate de tener registros relevantes para saber qué sucede en el sistema, especialmente cuando algo falla. Asegurate de tener la excepción y la traza del sistema disponibles.
Podés empezar con registros verborrágicos cuando sacás a producción una función, y reducirlos y refinarlos con el tiempo.
3. ¿Tus intervalos y trazas están etiquetados correctamente para cubrir todos los flujos de interés?

Por último — entendé la diferencia entre monitoreo positivo y negativo, y asegurate de estar monitoreando positivamente tus cambios en la función.

Monitoreo positivo significa que estás activamente asegurándote de que tu función trabaja correctamente.
Monitoreo negativo (usualmente) significa que estás monitoreando pasivamente que nada se haya roto.


## Paso 3 — Entendé tu infraestructura
Tenés que entender qué es lo que pone el código en producción, cómo se construye, cómo se implementa — esto es tan importante como entender tu código ya que puede ocasionar problemas, o con la misma facilidad, solucionarlos.
Ser capaz de entender y controlar este proceso te puede dar superpoderes — podés crear imágenes personalizadas — interactuar con ambientes, ¡incluso crear los tuyos propios!

Entendé tu proceso de compilación y CI — idealmente — agregale alguna funcionalidad, asegurate de poder cambiarlo si surge la oportunidad. Aprendé y sentite cómodo con los procesos de implementación y de restauración.

Comprendé tu esquema de producción — dónde estan tus instancias, cuál es su runtime, cómo están configuradas y conectadas con el mundo, cómo se les entrega nuevo software, cómo podés enviar o desviar tráfico desde y hacia ellas.


## Paso 4 — Monitoreá, Monitoreá, Monitoreá
Usualmente arrancaba cada día laboral chequeando 3-4 paneles principales de sistemas bajo mi dominio. Estaba aprendiendo los patrones de tráfico — entendiendo cómo se veía lo “normal” (mirá [esta charla](https://youtu.be/Q4nniyAarbs?t=1775) que crea el término “_ingeniería intuitiva_”).

Así que, ¿qué es lo “normal”? ¿Qué estaba mirando?

Las métricas obvias eran Latencia, Transferencia, Tasa de Errores (sip, algunos sistemas tienen errores en el “estado normal”), pero me metí más a fondo — patrones comunes de utilización de CPU, red, memoria, distribución de latencias, distribución de tráfico de los clientes. Podías consultarme en cualquier momento del día, y te podía decir con altos niveles de confianza cuál era la tasa de transferencia de nuestro sistema, quiénes eran los clientes que generaban la mayor parte del volumen, y el número de réplicas en la flota. Conociendo lo “normal” — podía detectar “anomalías”.

En algun momento, este monitoreo constante y la experimentación con las métricas, registros y herramientas de observabilidad te conducirán a poder monitorear cualquier cosa con diferentes herramientas y desde diferentes ángulos, independizándote — he aprendido por las malas que las herramientas de observabilidad también pueden fallar durante las caídas de sistemas, y tener la posibilidad de monitorear sistemas con un nivel de redundancia es un alivio.

Por último, investigar las anomalías, incluso aquellas que no causaron alertas o impactos visibles. ¡Vas a aprender muchísimo de ellas! Podrías llegar a enterarte que algunos de tus clientes tiene picos de tráfico, o que tu sistema pasa por ciclos de limpieza en algunos momentos del día ([Postgres VACCUM](https://www.postgresql.org/docs/9.1/sql-vacuum.html) o GCs por ejemplo).

En un ejemplo interesante, me las arreglé para darme cuenta de que teníamos un caso de mala integración con un cliente investigando un patrón anormal de tráfico. El sistema mejoró.


## Paso 5 — Eliminá “no es mi responsabilidad” de tu vocabulario
Para aprender realmente y sentir el sistema, no podés estar limitado a los 4-5 servicios o componentes bajo tu control. Tenés que entender cómo funcionan otros sistemas también, qué los hace andar.

No tiene que ser un entendimiento profundo exhaustivo de 360 grados de cada bit y byte, pero un esquema general de las cosas puede ser muy informativo.

Cuando ya hayas estado monitoreando los sistemas de producción por el tiempo suficiente (paso 4) — “meterse” en otros sistemas, e incluso — entender los problemas de otros sistemas es mucho más simple. Podés entender cuando la base de datos devuelve errores viendo los registros incluso si no estás familiarizado con la base de datos o el servicio — y ya sos un experto en cómo aprovechar esos registros de errores.

Los códigos de errores de HTTP son los mismos, sin importar el servicio. Tal vez no comprendas del todo la causa o impacto — pero está en tus capacidades entender qué es lo que está pasando, y qué está fallando.

Con suerte — la mayoría de los sistemas son lo suficientemente estables, así que otros servicios son simplemente otra oportunidad para aprender. Es más —entender más sistemas te hace mucho más seguro y capaz de determinar el impacto en el negocio (esperá al paso 7).

## Paso 6 — Recolectá incidentes — investigá cada uno de ellos

Metete en las salas de situación de incidentes, sentate en el fondo. Simplemente mirá y escuchá. Aprendé, sentí la emoción (o el terror).
Revisá o presenciá postmortems. Entendé qué pasó — entendé cuáles son los SLIs afectados, y cómo monitorearlos. ¡Esos SLIs se traducen en impactos al negocio!

Vas a aprender muchísimo con solo estar ahí, viendo cómo operan los ingenieros. Cada incidente va a estar metido en tu ser profesional, y la próxima vez que pase algo así (o algo similar a eso, que va a suceder), vas a tener un poco más de contexto que el resto y vas a estar un paso adelante.

Vas a entender la diferencia entre impacto (lo que le pasa al negocio), los síntomas (lo que le pasa a tus sistemas), y la Causa Raíz (lo que empezó la debacle).

Eventualmente, te vas a sentir cómodo en incidentes de producción — es parte del trabajo, como lo es revisar código o hablar sobre tu diseño.

## Paso 7 —  Conocé tu negocio
¡El ingeniero promedio no entiende lo que “tener problemas de latencia en el ElasticSearch” significa para el cliente! Hay una barrera de dominios entre la implementación técnica del sistema y el valor que le genera al consumidor final.

Como parte del equipo de ingeniería, tenés que entender el valor que dan tus componentes y poder explicar el impacto de cualquier problema en el sistema, desde la perspectiva del usuario final.

Unos años atrás cuando trabajaba en una pequeña startup, en un famoso incidente, un ingeniero de guardia reportó que “había un cola de trabajos” en el negocio — quien obviamente no tenía idea de qué eran esos trabajos. Esto ocasionó muchas preguntas y causó mucho pánico innecesario.


## Paso 8 — Preguntás cómo se hace una vez y lo hacés vos solo la próxima

Tratá de ser lo mas independiente posible, aprendé a hacer algo dentro de los permisos y límites de tu rol:

* ¿Necesitás cambiar cómo es compilada tu imagen? ¡Buenísimo! Pedí ayuda, y después asegurate de que podés rehacerlo solo.
* ¿Necesitás ssh/kubectl en alguna instancia para verificar algo? ¡Genial! Sentate al lado de tu colega favorito y escribí lo que están haciendo, y luego asegurate de que podés rehacerlo solo.
* ¿Necesitás crear una métrica complicada en Prometheus o un panel de Kibana? ¡Buenísimo! Tomate de la mano de tus expertos en observabilidad y aprendé cómo lo hacen, dónde ponen su enfoque, y luego asegurate de que lo podés rehacer por vos mismo.
* ¿Necesitás encontrar un error en algo complejo en producción? Sentate con el líder de tu equipo y discutan cómo podría solucionarlo, y luego asegurate de poder hacerlo solo.

Luego de poder hacer todas esas cosas solo, podés empezar a tomar más responsabilidades dentro del equipo y entregar valor más rápido. Es más, vas a empezar a entender los dominios del DevOps y su jerga, y vas a poder comunicarte mucho mejor con el equipo de operaciones.


## Retrospectiva
Ahí lo tenés, este es el camino que he tomado. Es un viaje intensivo, que involucra docenas de servicios, montón de colegas, algunos mentores, y ocasionales caídas de sistema. Las habilidades obtenidas son impagables, y las posibilidades infinitas.

* La versión original de este post se puede encontrar en [Better Programming](https://betterprogramming.pub/the-path-of-getting-comfortable-in-production-c88456146f00) (inglés).
* Autoría por [Boris Cherkasky](https://twitter.com/cherkaskyb), traducción por [@jcasarini](https://twitter.com/jcasarini), revisión por [@nachichuri](https://twitter.com/nachichuri).
