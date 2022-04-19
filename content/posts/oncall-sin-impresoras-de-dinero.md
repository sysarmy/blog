---
Title: "Guardias para empresas sin impresoras de dinero"
date: 2022-04-19
draft: false
Description: "En este post te compartimos algunos tips para rotaciones de guardia en empresas sin el presupuesto de Google. Lo importante es [siempre usar antitranspirante](https://sysarmy.com/sudo/)."
markup: markdown

Keywords:
  - oncall
  - guardias
  - sre
  - priorización
  - mejores-prácticas

Tags:
  - sysarmy
  - oncall
  - guardias
  - sre
  - priorización
  - mejores-prácticas

Topics:
  - oncall
  - guardias
  - sre
  - priorización
  - mejores-prácticas

Thumbnail: assets/empresas-sin-impresoras-de-dinero.jpg
socialImage: assets/empresas-sin-impresoras-de-dinero.jpg
featuredImage: assets/empresas-sin-impresoras-de-dinero.jpg
externalPermlink: "https://www.softwareatscale.dev/p/manageable-on-call-for-companies"
---

_La versión original de este post se puede encontrar en [Software at Scale](https://www.softwareatscale.dev/p/manageable-on-call-for-companies) (en inglés)._

El libro de [SRE de Google](https://sre.google/sre-book/table-of-contents/) se ha convertido en una biblia para las empresas de software que quieren aprender mejores prácticas en operaciones. Es un libro bien escrito e informativo sobre conceptos de los que no se solía hablar mucho en la industria del software. También está disponible gratis para leer en línea (en inglés) y no es parte de ninguna estrategia de marketing o de ventas con enlaces de afiliados turbios o una edición que tenés que pagar para actualizar o seguir leyendo.

Pero un capítulo en particular ([Estar de guardia](https://sre.google/sre-book/being-on-call/), en inglés) tiene consejos que parecerían aplicar solo a empresas utópicas con recursos y personal ilimitados. Así que quería bajar algunos de sus conceptos de una manera que sea útil para organizaciones más pequeñas, explorar algunos principios todavía más básicos en torno a los aspectos técnicos y organizativos de la gestión de rotaciones de guardia sostenibles para todo tipo de equipos de software y, con suerte, dar algunos consejos prácticos.

## Responsabilidades en las guardias

En primer lugar, la responsabilidad de una buena rotación de guardia recae directamente en el/la gerente de ingeniería del equipo. El equipo técnico por sí solo no puede resolver el problema de la carga de guardia insostenible sin la ayuda y el apoyo de la gerencia, ya que la sustentabilidad de la rotación de guardia involucra piezas tanto técnicas como organizativas. Por ejemplo, una rotación puede estar sobrecargada debido a razones técnicas, como software o alarmas poco confiables, pero un equipo muy pequeño o el bajo rendimiento de los miembros del equipo pueden también ser parte del problema. Si el equipo tiene una rotación de guardia insostenible, el equipo técnico debe sugerir soluciones técnicas y a su vez escalar los problemas a la gerencia. Si la gerencia parece no querer o no poder resolver el problema en un tiempo razonable, ya sea priorizando la inversión en calidad u otros medios, el equipo técnico debe sentirse cómodo [votando con los pies](https://es.wikipedia.org/wiki/Votar_con_los_pies).

Un refrán común es que _irse de un equipo por malas guardias va a hacer que la experiencia sea peor para el resto de las personas del equipo_ y, personalmente, me he quedado en equipos más tiempo del que debería por este motivo. Empezar a reconocer que lidiar con el desgaste y las renuncias, por cualquier motivo, es en última instancia responsabilidad de la gerencia y que, como equipo técnico, sólo se puede llegar hasta cierto punto, debería ayudar a aliviar esta preocupación. Tu empresa no dudaría en despedirte si no cumplís con las responsabilidades de tu trabajo, así que tenés derecho a hacer lo mismo con tu equipo.

## ¿Es necesario estar de guardia 24/7?

Una suposición general es que los equipos tienen alertas que podrían activarse las 24 horas del día, los 7 días de la semana. Esto suele ser cierto en la escala de Google, pero cada equipo debería decidir si les aplica según diferentes postulados, antes de asumir que cuanto más guardia, mejor. Se puede comenzar preguntando si en el caso que el producto del equipo tenga una interrupción total fuera del horario laboral causaría una gran pérdida de funcionalidad para un gran conjunto de clientes, una pérdida grave de ingresos o un daño reputacional. Esto suena simple, pero automáticamente implica que la mayoría de los equipos que administran herramientas internas y los equipos con productos limitados no necesitan estar de guardia 24/7. Por ejemplo, un equipo que administra un pipeline interno de datos críticos que no generan ingresos, el clúster de Jenkins, o un equipo que gestiona una función no crítica en la página de inicio de la aplicación, no deberían tener guardias 24/7 de forma predeterminada (siempre y cuando el resto de la aplicación pueda manejar las fallas de manera limpia).

Para ser claros, cada equipo podría optar por tener una rotación de guardia 24/7, incluso si no cumple con estas restricciones. Este compromiso entre el valor del cliente y la sostenibilidad de las guardias debería ser explícito y podría tener sentido en algunos casos (por ejemplo, una rotación grande -muchas personas en el equipo- y tranquila -pocos incidentes-).

## Establecimiento de un SLA y un SLO

Los productos deberían tener métricas de calidad para establecer qué es importante para los clientes, e impulsar las inversiones en alertas y mejoras de infraestructura. Estos pueden tomar la forma de SLOs (objetivos de nivel de servicio, por las siglas en inglés de _service level objectives_) y SLAs externos (acuerdos de nivel de servicio, por las siglas en inglés de _service level agreements_). Un SLA es el número más bajo posible con el que vos y tus clientes van a estar de acuerdo, no un número aspiracional que hayas escuchado que usa Amazon. Muchas empresas de SaaS de miles de millones de dólares se han construido sobre la base de dos nueves de disponibilidad (podés leer más [acá](https://upperedge.com/workday/what-you-need-to-know-about-workdays-standard-sla-and-service-credits/), en inglés). Incluso a empresas de renombre con una fuerte presencia sobre el consumidor les va bien con tres nueves (podés leer más [acá](https://dropbox.tech/infrastructure/lessons-learned-in-incident-management), en inglés). Idealmente, es un valor que sólo debería cambiar en función de las necesidades del cliente, por ejemplo, si el equipo de ventas lo menciona como un problema durante las conversaciones con un cliente potencial. Tu SLA externo tiene que ser un poco más bajo que el SLO. Por ejemplo, si tu SLA es del 99,8% de disponibilidad mensual, el SLO debería ser del 99,9% para no volar demasiado cerca del sol. Este SLO va a ayudar a impulsar otros factores de la rotación de guardia.

## Tiempos de respuesta

La expectativa general debe ser que una vez que un miembro del equipo haya respondido una alerta, se ponga a _debugguear_ e investigar el problema, o que llame a otra persona para que lo/la ayude. Por otro lado, si la persona no puede resolver el problema en ese momento, no debe responder la alerta para que pueda escalar a una guardia secundaria, o ascender hacia puestos gerenciales.

Es importante calcular el tiempo de respuesta de alertas tanto para las guardias en horas laborales como no laborales. Si tu equipo está cómodo estableciendo tiempos de respuesta de treinta minutos o más, no se necesita pensar mucho más. Cualquier cosa por debajo de ese tiempo requiere cierta diligencia para justificar el sentido de inversión hacia el servicio de alertas; de lo contrario, se quita la capacidad del equipo para hacer cosas básicas de la vida como salir a caminar sin su computadora, algo que no debería tomarse demasiado a la ligera.

Para establecer tiempos de respuesta de alertas, primero hay que pasar por el proceso de establecer un SLO. Con este SLO, se puede calcular una duración máxima de interrupción mensual: cuánto tiempo el producto puede estar caído sin romper el SLO. Después, se debería calcular la duración promedio de las tareas que tu equipo necesitaría para resolver una interrupción en el servicio. Por ejemplo, si suponés que tu equipo va a tardar diez minutos en tener una estimación razonable de un problema, la mitigación más común es realizar un _rollback_ a una versión anterior, y lleva veinte minutos en promedio hacer un _rollback_, el tiempo para la mitigación es de al menos treinta minutos. Si esperás dos caídas de este tipo al mes, el producto generalmente estaría caído durante una hora al mes. Si el SLO te permite estar caído durante 120 minutos al mes y querés un margen de 30 minutos, entonces tenés que contabilizar 90 minutos de interrupciones. Para garantizar solo 90 minutos sin servicio con dos incidentes esperados por mes, el tiempo de respuesta del sistema de alertas (_pager_) no puede ser inferior a quince minutos. Obviamente, esto también podría implicar que el producto tarda demasiado en hacer el _rollback_, y podría ayudar a guiar una decisión para invertir en mejorar esos tiempos.

En la práctica, estos cálculos implican que un SLO de tres nueves o más (99,9%+), seguramente van a requerir un tiempo de respuesta de alertas de cinco minutos, así que hay que tener mucho cuidado con los SLOs agresivos.

## Guardia secundaria y escalamiento

En general, si tu equipo tiene guardias 24/7, es sumamente necesario que haya una guardia secundaria. Por defecto, la cadena de escalamiento de alertas también debe ascender hacia los puestos gerenciales. Luego, la jerarquía de dirección será informada y tendrá que lidiar con los incidentes que se presenten para que puedan detectar signos de problemas en sus equipos con anticipación, y se debería incentivar a la gerencia para mejorar la calidad y reducir las alertas.

Si tu equipo no tiene guardias 24/7, no es necesario tener una guardia secundaria. Dependiendo de la carga de trabajo esperada, los procesos de planificación deberían asignar menos trabajo a el/la ingeniero/a de guardia, y se espera que el trabajo de guardia sea una prioridad para ellos/as.

## Tamaño del equipo

Si el tiempo de respuesta de alertas es de quince minutos o menos, entonces las rotaciones de guardia deben ser grandes, y las semanas de guardia generalmente deben transcurrir sin incidentes para que sigan siendo sostenibles. De lo contrario, los equipos podrían entrar en una espiral de muerte cuando haya eventualidades como el renuncias. Por ejemplo, una rotación puede parecer sostenible durante varios meses, pero se volvería inmediatamente insostenible si uno o dos miembros del equipo renuncian después de el pago de los bonos o los ciclos de adjudicación, y más miembros del equipo comenzarían a buscar otro empleo.

El libro de SRE de Google recomienda tamaños mínimos de equipo de al menos ocho personas, a no ser que las rotaciones se puedan dividir entre varios miembros del equipo en dos o más zonas horarias. En la práctica, mantener esto puede ser un desafío para los equipos. El número de personas disponibles suele ser escaso y las personas responsables de la toma de decisiones tienen diferentes prioridades a la hora de asignar las personas del equipo de guardia. Además, la mayoría de las empresas no tienen oficinas de ingeniería en varias zonas horarias. Si es difícil ampliar el equipo, lo mejor que se puede hacer es hacer que la rotación sea extremadamente tranquila a través de inversiones técnicas. Para mí, una rotación de guardia tranquila es con menos de cuatro alertas por semana y cero alertas fuera del horario laboral. Si una rotación de guardia puede mantener esto consistentemente, entonces una rotación más pequeña (no menos de seis personas) es aceptable. Sigue siendo disruptivo estar de guardia, pero al menos se elimina el estrés de la rotación.

## Traspasos

Con una frecuencia fija (generalmente semanal), los miembros de la rotación deben reunirse para analizar las alertas, pasar la guardia al siguiente miembro del equipo y proponer acciones. Cada acción debería tener propuesta una prioridad y un tamaño (más comúnmente en puntos de historia). El/la líder técnico/a del equipo (o alguien delegado por él/ella) debe ordenar globalmente todas las acciones para la próxima ronda de planificación, con aportes del resto del equipo si es necesario. El/la gerente de ingeniería se tiene que asegurar que al menos X puntos de historia del trabajo de guardia se asignen en cada ciclo de planificación, y de asignar el trabajo para que las acciones se distribuyan uniformemente en todo el equipo. Este proceso garantiza un impulso constante de mejora de la rotación sin sobrecargar a algunos miembros del equipo con el trabajo de las acciones.

Las acciones deberían crearse cada vez que una alerta se active más de una vez. Estoy explícitamente en contra de las alertas de baja prioridad, siempre que sea posible (podés leer más sobre esto [acá](https://utsavshah.com/2020/10/12/case-against-low-priority-alerts/), en inglés).

## Conclusión

Estas fueron algunas ideas para gestionar de manera sostenible las rotaciones de guardia. Cada una de estas ideas tiene muchos niveles de complejidad y los problemas correspondientes podrían abordarse de múltiples maneras. Por ejemplo, dado que la gerencia es responsable en última instancia de la sostenibilidad de la guardia, es posible que haya algunos gerentes que quieran estar en la rotación (podés leer más sobre esto [acá](https://awspyker.medium.com/why-as-a-netflix-infrastructure-manager-am-i-on-call-bdc551ac01fe), en inglés). Con suerte, esta publicación te fue útil y te dio algo en qué pensar. 

- La versión original de este post se puede encontrar en [Software at Scale](https://www.softwareatscale.dev/p/manageable-on-call-for-companies) (en inglés).
- Traducción por [@nachichuri](https://twitter.com/Nachichuri), revisión por [@jedux](https://twitter.com/jedux).
