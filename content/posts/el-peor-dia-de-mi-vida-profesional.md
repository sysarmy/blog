---
Title: "El peor día de mi vida (profesional)"
date: 2022-09-28
draft: false
Description: "Todos tuvimos un día malo en el trabajo, no importa a que te dediques. En este post, Javier V M Bruno te cuenta el suyo y nos deja una valiosa enseñanza."
markup: markdown

Keywords:
  - sysarmy
  - sistemas
  - backups
Tags:
  - sysarmy
  - sistemas
  - backups
Topics:
  - sysarmy
  - sistemas
  - backups

Thumbnail: assets/epddmvp-cover.jpg
socialImage: assets/epddmvp-cover.jpg
featuredImage: assets/epddmvp-cover.jpg
externalPermlink: "https://medium.com/@jvmbruno-es/el-peor-d%C3%ADa-de-mi-vida-profesional-6c2d962823af"
---

_Autoría de [Javier V M Bruno](https://medium.com/@jvmbruno-es), publicado originalmente en [Medium](https://medium.com/@jvmbruno-es/el-peor-d%C3%ADa-de-mi-vida-profesional-6c2d962823af)._

## La historia

Imagino todos tuvimos un día malo en el trabajo, no importa a que te dediques. El mío fue un Lunes (Yup!) 27 de Agosto, 2012. Cómo es que me acuerdo de la fecha exacta? 4 días después tenía fecha para casarme por civil.

Ese día llegué temprano a la oficina, estaba yo solo. Cuando entrabas a la oficina lo primero que veías era el rack de servers. Si. Nuestros escritorios estaban alado de los servers.

Note que uno de los discos de nuestro server principal tenia el led titilando en rojo. Algo bastante común, que los discos “murieran” ya que varias veces el aire acondicionado de la oficina falló así que ya todos los discos tuvieron su cuota de calor, destruyendo su vida útil. Medio dormido, aun con la campera puesta, saque un disco de un cajón de los “discos usados que no están tan mal”. Saque el que estaba fallando y puse el otro.

Esto lo hice ya varias veces en el pasado. Al poner el disco nuevo la controladora comienza el rebuild y eventualmente todo vuelve a la normalidad.

Ese día no fue así. De alguna manera, ese día, la controladora dijo, “hey! este disco nuevo que insertarte, lo voy a tomar como que es parte del actual raid”.

Mientras yo me preparaba el primer café del día vi como servers comenzaban a caerse. Cosas dejaban de andar. El terror comenzó. Mi propio Chernobyl. “Una seguidilla de hechos bochornosos…” como solían decir Pablo y pachu en [Showmatch](https://www.youtube.com/watch?v=eIk6T4691OM). Los planetas se alinearon (esta ves no para el bien) y todo lo que debía fallar para la catástrofe, falló. En su perfecto orden.

La controladora al haber adoptado el disco como valido, comenzó a usar los sectores de ese disco y replicarlos en los otros discos (raid 5), destruyendo todo. Y de a una las virtuales que corrían en esa maquina fueron “crasheando” y finalmente el main server (que era el Controlador de Dominio) también cayó.

“No hay problema, tenemos copia de seguridad” le explicaba a mi jefe, el gerente general de sistemas. La información estaba, lo que no estaban eran los servers encargados de mostrarla.

Normalmente si no esta disponible el Controlador de Dominio (o su secundario) uno aun puede logearse en su computadora, despues de darle aceptar al mensaje de error de que no hay server disponible que se van a usar las credenciales “cacheadas”. Obviamente no fue nuestro caso, la mitad de la red no podia logearse. Los chicos de soporte corriendo por todos los edificios sacando las maquinas del dominio para que el personal pudiera trabajar.

Mi compañero y yo tratando de recuperar los servers uno por uno desde backups y aplicando luego los últimos cambios.

Para dar una correcta imagen, esta infra eran 8 edificios, con mas de 600 dispositivos y una infinita lista de servicios hacia internet y nosotros eramos 2. En redes. Encargados de mantener todo eso a flote.

A pesar de la catástrofe toda la institución no se hizo mucho problema. ¿No hay correo? Mejor, así no tengo que leer correos. ¿Esta caída la pagina? que intenten mañana. Mientras pueda checkear mi facebook estamos bien. El lunes nos quedamos en la oficina hasta las 12 de la noche y al otro dia 6 am devuelta ahi. Pero todo iba en camino…. hasta que….

Por alguna razón el software de contabilidad, no le gusto el restore de la base de datos. Si bien se hizo correctamente, había cierto margen de que algún dato no quedo relacionado bien. Como era fin de mes, contabilidad estuvo cargando muchos datos sobre los pagos de los sueldos y tal ves la copia de seguridad no incluía todos. Pero les era mas difícil revisar todo, que el hecho de cargar todo el mes de cero. Lo cual nos pareció bien. Ahi fue cuando contabilidad envió un correo diciendo que por una excepción, este mes, cobraríamos nuestro sueldo 1 o 2 días mas tarde. Sino hay correo o toda la infra esta caída, ta bien, pero ¿cobrar el sueldo 1 día mas tarde? INACEPTABLE.

El martes a la noche mis amigos me tenían una fiesta de despedida de soltero sorpresa. Comimos asado y tomamos como si fuera el último día en este mundo. Y casi que lo fue.

Obviamente, en la despedida estaba la mayoría de la gente de sistemas, que me acompañaron en el ejercicio de tomar y mucho. Llegue a mi casa a las 6 am y a las 8 mi teléfono explotó. Mi jefe casi llorando al teléfono, de que vaya urgente a la oficina, que presidencia armo una reunion para que le explicáramos porque la gente iba a cobrar 1 día mas tarde. En fin. Reunion con presidencia, con resaca, y 2 horas de sueño. Lindos recuerdos. Intervención va, intervención viene, todos concordaron que cobrar 1 día mas tarde no era el fin del mundo, sobre todo mientras nos recuperábamos de terrible catástrofe. Pero como siempre había que hacer el revuelo para que todos se quedaran contentos de que se estaba haciendo todo lo posible.

## Lo técnico

Cuando uno vive estos feos momentos, uno los revive una y otra ves en la mente y busca entender que paso, y ver como se podría haber evitado. “Tal ves si ese día llegaba tarde…” jajajaja

Como conté, éramos 2, siempre corriendo tras lo urgente y dejando de lado lo importante. La controladora estaba en un server DELL, las herramientas de monitoreo y alarmas de DELL (si has estado en IT por mas de 5 minutos sabes….) son un asco. Recuerdo haber querido configurar las alertas por SMTP, pero el software no soportaba cifrado, o ni siquiera autenticación. “Otro día levanto un server SMTP que haga de relay con el que esta en producción”

En ese momento teníamos pocas herramientas de monitoreo. Pero que esto no te pase nunca, de verdad, no esta bueno. Hoy (obviamente) tenemos [Eventsentry](https://www.eventsentry.com/) configurado para monitorear todos los raids. Tanto sea a través del OpenManager de Dell, o SNMP. Desde mismo la página de información del Host (Demo [LINK](https://demo.eventsentry.com/hostinventory?id=1)) que podemos ver el estado del VD del raid:

| ![](assets/epddmvp1.png)   |
| :------------------------: |
| Estado del Volumen Virtual |

Así como las alertas por email (o SMS, telegram, como gustes que te avise) de cuando un disco es detectado por posible futuro fallo, o cuando los discos fallan:

| ![](assets/epddmvp2.png)                  |
| :---------------------------------------: |
| Alerta de un disco se desconectó del RAID |

También ahora recibo notificaciones cuando la reconstrucción del raid comienza y cuando termina. Pero no solo eso. También puedo predecir fallos en raid inclusive antes que la controladora lo sepa.

Por ejemplo cuando un disco o varios comienzan a fallar, leen o escriben mas lento o fallan en buscar un sector. Estos aun no son marcados como malos sino falla X cantidad de veces. Pero aun así, yo recibo una notificación que el performance del raid no es el normal, y puedo ir a revisar si todo esta bien.

| ![](assets/epddmvp3.png) |
| :----------------------: |
| Alerta de performance    |

No solo monitorear las posibles fallas físicas, sino también las lógicas, como el quedarte sin espacio en un disco donde corres una base de datos, o la laptop de las persona que carga la planilla de sueldos (la mas importante de toda la empresa!)

| ![](assets/epddmvp4.png) |
| :----------------------: |
| Listado de discos de toda la red, con capacidad, uso y predicción demo link [AQUI](https://demo.eventsentry.com/diskspacestatus?search.query=&search.logfile=0&search.revision=0&search.active=&search.dateRange=Current&search.group=&search.order=computer.name&search.sort=asc&search.refresh=&search.page=1&search.limit=25&search.type=detailed&pageDefault=true&report=1&PROFILE=English) |

En la urgencia de sacar rápido andando las computadoras, los chicos de soporte fueron máquina por maquina a sacarlas del dominio, o arreglar problemas globales (sobre todo porque el Controlador de Dominio ya no existía…). Ahora mirando hacia atrás se que muchas de las acciones que se hicieron en persona se pondrían haber hecho masivamente desde la red. Con tools como Admin Assistant (Enlace [AQUI](https://www.eventsentry.com/adminassistant)), que es completamente gratuita.
Como por ejemplo podríamos haber cambiado configuraciones de windows desde el registro, de todas las computadoras de la red, solo con un par de clicks

| ![](assets/epddmvp5.png)                                                                       |
| :--------------------------------------------------------------------------------------------: |
| Captura de pantalla de Admin Assistant, cambiando valores de registros de varias computadoras. |

## La reflexión

Si bien mi reflexión esta basada en largos, muy largos, años de experiencia, la reflexión es corta:

> ### **Que jamás lo urgente te quite de hacer lo importante.**

Así sea tu jefe quien te lo pide, o el CEO. Sabe que el día que un backup no funcione porque no tuviste el tiempo de revisar que se estaban haciendo bien, tu jefe no te va a decir “No hay problema, se que no te di tiempo de revisarlos” la responsabilidad igual va a caer en vos.

También en estos momentos se separan las aguas, entre los co-workers y los amigos de fierro. De los que se arremangaron y salieron a lucharla con vos, de los que desde la silla te dijeron que hiciste mal o como debiste haberlo hecho.

Y como siempre no hay nada como cerrar tu día sabiendo que si algo pasa, te vas a enterar rápido. MONITOREA!

## Cierre

Este articulo se lo dedico al sobrevaluado WD Velociraptor que nos marcó la vida a varios de sistemas aquél día. R.I.P.

| ![](assets/epddmvp6.png) |
| :----------------------: |
| In Loving Memory         |

- Autoría de [Javier V M Bruno](https://medium.com/@jvmbruno-es), publicado originalmente en [Medium](https://medium.com/@jvmbruno-es/el-peor-d%C3%ADa-de-mi-vida-profesional-6c2d962823af).