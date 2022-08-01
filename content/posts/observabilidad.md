---
Title: "Qué es realmente la observabilidad y por qué es importante"
date: 2022-06-01
draft: false
Description: "Nuestra industria no tiene la definición correcta de _observabilidad_ y va a costar enormes cantidades de dinero y a causar caídas constantes de servicio hasta que esto cambie."
markup: markdown

Keywords:
  - sysarmy
  - observabilidad
  - monitoreo
  - herramientas
  - arquitectura
Tags:
  - sysarmy
  - observabilidad
  - monitoreo
  - herramientas
  - arquitectura
Topics:
  - sysarmy
  - observabilidad
  - monitoreo
  - herramientas
  - arquitectura

Thumbnail: assets/observability_cover.png
socialImage: assets/observability_cover.png
featuredImage: assets/observability_cover.png
externalPermlink: "https://medium.com/@MarkDennehy/observability-72891a0c3866"
---
_La versión original de este post se puede encontrar en [Medium](https://medium.com/@MarkDennehy/observability-72891a0c3866) (inglés)._

> [TL;DR](https://es.wikipedia.org/wiki/TL;DR): Nuestra industria no tiene la definición correcta de observabilidad y va a costar enormes cantidades de dinero y a causar caídas constantes de servicio hasta que esto cambie.

Me he sentido cada vez más frustrado con algo durante estos últimos 1-4 años. La mayor parte del tiempo, es algo que se descarta porque es difícil de monetizar, aunque en realidad no es difícil de entender o implementar. Los equipos de ingeniería la tienen tan cerca que rara vez la tienen en cuenta y los proveedores piensan que no es rentable, entonces termina en una situación que se presta para ser ignorada deliberadamente. Específicamente, estoy hablando de la gran brecha entre lo que nuestra industria llama *observabilidad* y lo que la *observabilidad* **realmente es**.

Y esta brecha no es una trivialidad académica: significa que hay una **gran** falencia en las herramientas que usamos, que se traduce directamente en la pérdida de ingresos, además de mucho dolor y trabajo innecesario para los equipos de ingeniería.

Hoy en día, ninguna de las herramientas de observabilidad, de ningún proveedor, son adecuadas para cumplir su función. No es suficiente tener interfaces de usuario lindas y poder ir haciendo clic desde una métrica hasta un _log_ y una traza. Son extras que está bueno tener. Lo que realmente **necesitamos** tener es soporte en nuestras herramientas para permitir que los equipos de ingeniería [codifiquen](https://es.wikipedia.org/wiki/Codificaci%C3%B3n_(memoria)) fácilmente sus propios modelos mentales de cómo funciona cada servicio, para que el resto de las personas puedan ver lo que está pasando, sin necesidad de todo el contexto y la experiencia que los equipos de ingeniería necesitaron originalmente para armar esos modelos mentales.

La detección de problemas complejos en nuestros sistemas, y poder dar respuestas correctas a preguntas difíciles como _"¿cuánto va a afectar la degradación de la API de AWS a la latencia de nuestra aplicación?"_ o _"¿cuánto va a costar correr este servicio en dos años a esta tasa de crecimiento?"_ le da dolores de cabeza a casi todas las empresas en todas las escalas por encima de _“solo tenemos un/a ingeniero/a y el/ella sabe cómo funciona todo”_. Responder correctamente a estas preguntas mientras los modelos mentales de los equipos de ingeniería todavía están dentro de sus cabezas, suele ser difícil o incluso imposible, porque las respuestas se arman combinando el conocimiento de varias personas, y no todo entra en una sola cabeza. Necesitamos poder codificar modelos porque permite que otras personas los usen con sus datos para responder estas preguntas, o inclusive automatizar la respuesta.

Pero hoy en día no hay forma de hacer esto de manera fácil, porque en la industria de la monitorización en los últimos años, el término “Observabilidad” se ha utilizado exclusivamente como término de marketing; al principio por unos pocos proveedores, y después cada vez más, pero todos lo han usado para referirse, en esencia, a _“nuestro producto”_. Ninguno ha utilizado la definición real del término ni nada parecido, por lo que nadie ha estado trabajando en las herramientas que necesitamos para lograr observabilidad.

La diferencia entre lo que realmente significa el término y para lo que se ha estado usando, es el motivo por el cual adoptar lo que cualquier proveedor describe como "herramientas de observabilidad" no es una solución para los problemas de los equipos de monitoreo. La observabilidad en realidad es un concepto muy fundamental y, como la mayoría de los fundamentos, se puede establecer de una manera muy sencilla y fácil de entender. En cinco pasos, es así:

![Imagen con un gráfico que indica de qué manera un sistema de monitoreo debe capturar los outputs del estado de los sistemas para generar un ecosistema observable.](assets/observability_draw.png)

1. **Tenemos un sistema.** Este sistema puede ser _cualquier cosa_, ya sea la aplicación de tu empresa, un servicio en particular, un host en particular o cualquier otra cosa, **no importa**.

2. **Tenemos un modelo de este sistema que tiene cierto número de estados internos.** **No importa** si son dos estados (_"Funcionando"_ y _"Roto"_) o dos millones de estados.

3. **Tenemos algunas salidas del sistema.** **No importa** si se trata de métricas, _logs_, trazas o cualquier otra cosa.

4. **Si podemos saber en qué estado interno se encuentra el sistema simplemente observando sus salidas, entonces ese sistema es Observable.** Si hay estados en los que el sistema puede estar, pero no podemos darnos cuenta que está en ese estado al observar las salidas, entonces ese sistema es solo parcialmente observable.

5. **La Observabilidad del sistema es una medida de en cuántos estados nos podemos dar cuenta que nos encontramos, en comparación con la cantidad total de estados en nuestro modelo.**

Sí, ya sé que la [definición de Wikipedia](https://es.wikipedia.org/wiki/Observabilidad) es más complicada. Y si en algún momento estudiaste modelado de espacio de estados o hiciste algún curso sobre la teoría del control, la definición de Wikipedia es mejor. Si también viste algo de la historia de los métodos formales en informática, seguro sabés por qué esto no es tan importante; y si no, la versión simplificada es que nosotros como industria realmente no podemos crear modelos formales para nuestros sistemas porque no los entendemos lo suficientemente bien, y no enseñamos las matemáticas necesarias para entenderlo a suficientes ingenieros e ingenieras, así que todo lo que podemos usar por ahora es una vista simplificada de la _observabilidad_. Pero es suficiente para poder empezar a trabajar.

En su mayoría, la industria ha analizado la definición de _observabilidad_, cuando la ha analizado, desde el punto de vista de las salidas, y ha hecho que éstas sean más legibles y que sea más fácil crear nuevos resultados de salida. De ahí es de donde sacamos el meme inútil de los _"tres pilares de la observabilidad"_. Pero para nosotros como equipos de ingeniería y para las empresas en general, la parte mucho más importante hoy en día es el _otro_ componente crítico del que habla la definición: **requiere que tengamos un modelo del sistema**. El monitoreo es necesario, pero no suficiente, para darnos _observabilidad_.

En la actualidad, podemos elegir cualquier proveedor, construir la plataforma de datos definitiva, enviar todas las métricas, _logs_, trazas y cualquier otro dato que podamos pensar para que podamos verlo en cualquier resolución, en cualquier frecuencia de actualizaciones, en cualquier combinación, usando cualquier interfaz gráfica y _todavía_ no vamos a saber qué está pasando si no tenemos un modelo. Podemos construir el mejor sistema de monitoreo del mundo, y no vamos a saber qué está pasando.

Hoy en día, ese modelo solo existe en las mentes de los equipos de ingeniería (especialmente los que hacemos turnos de guardia). Podemos leer algunas métricas o logs específicos, y en seguida decirte que un servicio en particular está roto y cuán roto, por qué, y qué hacer para solucionarlo. Y si alguien del equipo se tira abajo de un colectivo mañana (o, también, se contagia de Covid-19), o lo roba otra empresa, o se jubila; bueno, ese modelo se pierde por el tiempo que le tome a alguien más del equipo de ingeniería volver a aprenderlo, si es que puede. También significa que la formación de nuevos/as empleados/as lleva más tiempo del necesario y que nuestros sistemas son más opacos para el resto de la empresa.

¿No me crees? Sentá a un/a ejecutivo/a de nivel C (CEO, CFO, CTO) o a un/a nuevo/a empleado/a frente a un tablero sin mucho formato y preguntales qué está haciendo el sistema. No van a tener el contexto, así que no lo van a saber. Si no se dan por vencidos de inmediato o piensan que es un chiste, seguramente van a mirar el tablero y van a intentar construir un modelo desde cero usando los metadatos que puedan encontrar, como los títulos de los gráficos o las unidades en los ejes, o usando datos anteriores en el gráfico para ver si la última hora se ve diferente a la semana pasada. Probablemente hayas visto a nuevos/as empleados/as haciendo esto durante su formación si alguna vez los/as supervisaste, capacitaste o asesoraste.

Esta es la mayor debilidad en las ofertas del mercado de la industria de monitoreo en la actualidad. La industria está completamente enfocada en extraer resultados de los sistemas de diferentes formas y presentarlos a los equipos de ingeniería de varias maneras, o brindarles herramientas para que lo hagan ellos mismos. La competencia se ha centrado en cuántos puntos de datos puede ingestar un proveedor, en sus modelos de precios, en evaluaciones comparativas de sus interfaces de usuario y varias otras cosas de poco mérito fundamental. Se ha prestado muy poca atención al desarrollo de herramientas que nos permitan extraer el modelo de la mente de los equipos de ingeniería y codificarlo para que las personas sin su conocimiento institucional puedan entender lo que está pasando.

Sí. Todos hemos oído hablar de las maravillosas praderas iluminadas por el sol explicadas con términos de marketing como _MLOps_ y _AIOps_, y hay muchas cosas que se podrían decir al respecto, usando una historia que se remonta a Machine Learning, Inteligencia Artificial, Big Data, Heurística, Inteligencia Artificial de nuevo, Sistemas Expertos e incluso más atrás dependiendo de cuánto tiempo hayas estado en esta industria, pero basta con decir que estos sistemas no pueden hacer este trabajo, porque no tienen un contexto más profundo y solo intentan encontrar patrones en los datos sin entenderlos. Cuando el líder del programa _ML-for-SRE_ (Machine Learning para Site Reliability Engineering) de Google [dice esto mismo abiertamente en una conferencia](https://www.youtube.com/watch?v=Nl6AmAL3i08) (en inglés), tal vez haya llegado el momento de que la industria acepte que tirarle datos a una caja negra y esperar que haga magia simplemente no es un plan viable en este contexto.

Peor aún, la tendencia actual es hablar sobre cómo la observabilidad resuelve el problema de las _"incógnitas desconocidas"_, es decir, recuperar el sistema cuando está en un estado desconocido. Este es un error categórico. La observabilidad es básicamente el ratio entre la cantidad de estados en los que podés darte cuenta que un sistema está, y la cantidad de estados totales en su modelo; si el sistema se encuentra en un estado desconocido, entonces el modelo estaba incompleto y ¿cómo se puede usar la observabilidad para arreglar el modelo? La idea no tiene sentido.

La realidad es que si el sistema está en un estado desconocido, no sabés lo que está pasando, por definición literal. Entonces es necesario construir un nuevo modelo o ampliar uno viejo para hacerle frente a esa situación. Esto te lleva a la categoría de _diagnóstico de fallas_, no de monitoreo. Hay que abrir la caja negra del sistema y mirar en detalle para descubrir qué pasó, lo cual te saca del marco matemático completo de la observabilidad. En ese escenario, la observabilidad es el _objetivo final_, no el medio. Y van a hacer falta diferentes herramientas, para lo cual tampoco hay mucho.

La pregunta obvia en este punto es: _“¿Y qué? ¿Por qué importa esto? ¿De qué manera no hacer esto nos termina costando dinero?”_. Bien, hablemos de dinero.

Los proveedores de monitoreo SaaS tienen varios modelos de facturación diferentes, pero de una manera u otra, todos se reducen a esto: pagás de acuerdo a la cantidad de puntos de datos que generás. Generás más puntos de datos, pagás más dinero. Esto es menos pronunciado para las soluciones locales, pero los requisitos de recursos significan que existe el mismo efecto, solo que la medición es menos lineal y es más difícil de planificar. Esto crea una tensión entre los equipos de ingeniería que quieren enviar todas las métricas que puedan con una frecuencia muy alta; y equipos de finanzas que quieren reducir la factura final que genera. Y una de las retóricas más antiguas es cuando Finanzas pregunta _"¿necesitan todas estas métricas?"_ e Ingeniería responde _"no sé lo que necesito saber hasta que necesito saberlo"_. Esta respuesta al estilo de Sir Humphrey se debe a que no se tiene un modelo adecuado del sistema. Los equipos que sí tienen un modelo, incluso de manera informal en sus cabezas, saben lo que necesitan ver como salidas y con qué frecuencia. Les permite generar puntos de datos que muestran lo que necesitan saber y no preocuparse por lo que no les importa. Reduce sus costos. Cuanto más codifican estos modelos, menor es el costo final.

Cuando algo _sale mal_, tener un modelo del sistema que no está en la cabeza de alguien del equipo de ingeniería hace posible la detección automática de fallas y abre la puerta a la posibilidad de una reparación automatizada o asistida (esto se apoya en la próxima palabra de moda que la industria de monitoreo está usando para cooptar, _controlabilidad_), todo lo cual reduce el tiempo para restaurar un servicio y permite a las empresas cumplir con los SLA, tener SLA más estrictos, reduce los pagos de multas y facilita las ventas a medida que aumenta la reputación de confiabilidad.

Más allá de la inmediatez de los requisitos operativos, cuando tenés un modelo de un sistema, podés hacer mejores predicciones sobre cómo se va a comportar a largo plazo. Esto significa predecir los costos de satisfacer las necesidades de los equipos y los clientes. Significa la capacidad de invertir cuando es necesario y no hasta que es realmente necesario, y te permite comprender la cantidad correcta a invertir.

En otras palabras, si como industria queremos mejorar la confiabilidad, reducir los gastos operativos, optimizar los gastos de capital y saber qué sucede realmente con nuestros sistemas a medida que sucede, entonces nuestro verdadero objetivo es construir un sistema observable y eso requiere dos cosas: monitoreo **y** modelado.

Hoy, tenemos monitoreo y vamos a seguir mejorándolo. **No** tenemos modelos y ningún proveedor parece interesado en proporcionarlos en este momento. En cambio, nos encontramos presenciando una reversión de la guerra de frecuencias entre Intel y AMD en un nuevo espacio, ya que los proveedores afirman que pueden ingestar más puntos de datos por segundo que sus competidores (y, como sucedió en la guerra de frecuencias, buscan pasar a un nueva métrica como la cardinalidad cuando alcanzan límites fundamentales), como si eso fuera realmente necesario. O los vemos inventar una nueva definición de lo que es la observabilidad y tratar de aprovecharse de eso, como si pudiera ayudar en algo.

Como parte de equipos de ingeniería que tienen carbón en la cara, sería más feliz si en su lugar solo construyeran las herramientas que necesitamos desesperadamente.

- La versión original de este post se puede encontrar en [Medium](https://medium.com/@MarkDennehy/observability-72891a0c3866) (inglés).
- Autoría de [Mark Dennehy](https://medium.com/@MarkDennehy), traducción por [@nachichuri](https://twitter.com/Nachichuri), revisión por [@jedux](https://twitter.com/jedux).