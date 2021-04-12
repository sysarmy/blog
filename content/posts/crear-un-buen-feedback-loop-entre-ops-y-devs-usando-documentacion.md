---
Description: “Esto nunca debería suceder. Si es así, llame a los desarrolladores"
Keywords:
- devops 
- engineer
- sre
- documentacion
Section: 
- devops
Tags:
- devops 
- engineer
- sre
- documentacion
Thumbnail: assets/crear-un-buen-feedback-loop-entre-ops-y-devs.png
socialImage: assets/crear-un-buen-feedback-loop-entre-ops-y-devs.png
featuredImage: assets/crear-un-buen-feedback-loop-entre-ops-y-devs.png
Title: “Esto nunca debería suceder. Si es así, llame a los desarrolladores"
Topics:
- devops 
- engineer
- sre
- documentacion
markup: markdown
date: 2021-04-11
draft: false
---
Si hay algo que a quienes desarrollan les gusta menos que escribir documentación, es responder llamados de la guardia innecesarios.

NdE: Este es un [artículo original](https://stackoverflow.blog/2021/03/18/creating-a-good-feedback-loop-between-ops-and-devs-using-documentation/) de [Thomas A. Limoncelli](https://stackoverflow.blog/author/tom-limoncelli/).

<!--more-->

El funcionamiento de un sitio web exitoso requiere la cooperación de operaciones (ops) y desarrolladores (devs), de ahí el término “devops”. Cuando hay un conflicto, antagonismos o falta de armonía, el sitio web sufre. Simplemente decirle a la gente que se "lleve bien" no es efectivo. La cooperación auténtica es el resultado de proporcionar una estructura que permite y fomenta la cooperación.

A menudo, una de esas áreas de conflicto y falta de armonía implica escalaciones de guardia. El sistema de monitoreo alerta a la gente de operaciones que hay un problema o un problema creciente que podría provocar una interrupción. Quien esté "de guardia" de operaciones debe manejar el problema o escalar el problema a los desarrolladores, sin importar la hora del día o de la noche.

Ahí radica un potencial conflicto. Demasiadas escalaciones desgastan a los desarrolladores. La falta de armonía comienza con exclamaciones como “¡Acabo de arreglar algo fácil! ¿Por qué esa gente de operaciones no puede hacer su trabajo? "

Operaciones se pone a la defensiva. "¿Como se supone que iba a saberlo?" o, "¡Acabo de hacer una pregunta y ahora se están volviendo idiotas!"

La discordia también puede comenzar en operaciones. "¡Oh, genial! ¡Otra sorpresa de los desarrolladores! "

No se puede obligar a la gente a cooperar, pero se pueden establecer estructuras y senderos que creen un entorno para la cooperación.

Uno de esos paradigmas es el ciclo de retroalimentación dinámica del runbook.

# Bucles de retroalimentación de runbook dinámicos (Dynamic runbook feedback loops)

Un [runbook](https://es.wikipedia.org/wiki/Runbook) es un conjunto de procedimientos sobre cómo responder en situaciones tales como recibir una alerta del sistema de monitoreo. El objetivo del ciclo de retroalimentación es crear un mecanismo en el que los expertos en la materia creen runbooks, pero tanto quienes desarrollan como quienes operan tienen la capacidad de mejorarlos de manera que reduzcan el número de escalaciones y mejoren la cooperación.

El objetivo de este proceso es establecer el equilibrio adecuado entre **esfuerzo** y **valor** al elaborar la documentación. Es una pérdida de esfuerzo que alguien escriba un tratado de 100 páginas sobre un tema simple; pero un runbook que sea demasiado breve no es útil. Este paradigma conduce al equilibrio adecuado. Un runbook comienza en el tamaño que el autor original consideró apropiado dado el conocimiento disponible, pero evoluciona al tamaño correcto a medida que se ejercita. Los runbooks que rara vez o nunca se necesitan reciben menos esfuerzo y los runbooks de uso frecuente se actualizan, optimizan y posiblemente se convierten en respuestas automáticas.

Esto contrasta notablemente con las organizaciones en las que los runbooks son creados por "el alto nivel" sin la participación de personas con participación directa. A menudo, estos no se pueden cambiar o el cambio requiere un proceso pesado que impide cualquier mejora.

# Escribirlo

La forma más fácil de distribuir el conocimiento del equipo es tener una buena documentación, lo que permite que cualquier persona que se encuentre con un problema desconocido siga un proceso probado para resolverlo. Eso es lo que se supone que son los runbooks. 

Nuestro formato preferido es una lista con viñetas que las operaciones pueden usar para resolver alertas. Cuando llega una alerta, las operaciones siguen las instrucciones del runbook. Si llegamos al final de la lista de viñetas y el problema no se resuelve, las operaciones escalan a los desarrolladores. 

Los desarrolladores de una organización necesitan escribir los documentos, obviamente. Pero con demasiada frecuencia, a los documentos se les asigna una prioridad baja y se los deja en un segundo plano para enviar nuevos productos, actualizaciones de funciones y otros trabajos considerados de misión crítica. Nunca llegan a hacerlo. La administración debe incluir la creación de runbooks como parte del proyecto.

Los desarrolladores no siempre se sienten cómodos escribiendo. Mirar una página en blanco puede resultar intimidante. Para superar el síndrome de la página en blanco, dales una [plantilla](https://www.atlassian.com/software/confluence/templates/devops-runbook). Ni siquiera se sentirá como si les estuviera pidiendo que escribieran un documento; solo desea que llenen este formulario. Si hace que la plantilla sea una serie de viñetas, cada una de las cuales es el procedimiento para manejar una alerta específica, el documento se vuelve casi trivial de completar. La pieza básica de documentación aquí es cómo lidiar con cada alerta.

Para motivar a los desarrolladores, recuérdeles que cuanto más tiempo dediquen a escribir runbooks, es menos probable que los problemas les lleguen. Todas las empresas quieren reducir las escalaciones, especialmente los desarrolladores que tienen que atenderlas fuera de las horas de trabajo, y el camino para llegar allí es a través de la documentación. 

El otro lado de este proceso, las alertas, debería reforzar la idea de que cualquier alerta tiene un proceso correspondiente en los runbooks al incluir la URL del runbook en el texto de la alerta. Esto aumenta la probabilidad de que se cumplan los procedimientos.

# Canalizar la retroalimentación hacia mejores runbooks

Aquí es donde comienza el ciclo de retroalimentación. 

En algún momento, una persona de operaciones recibirá una alerta que no está suficientemente documentada y debe ser escalada a los desarrolladores. Una vez que haya realizado todos los pasos del runbook y haya agotado todas las ideas que tenga, es hora de _hablar_ con las personas que escribieron el código. 

Este es el primer punto de retroalimentación: operaciones lee el runbook e intenta implementar el proceso documentado en él. Desarrollo puede haber documentado todas las alertas, pero aquí es donde la cosa se pone en marcha; Si un runbook no soluciona un problema cuando dice que lo hace, la persona de operaciones debe corregirlo inmediatamente o al menos identificar el problema. Cuando la persona de operaciones se convierte en desarrollador, ese es el comienzo de un ciclo de retroalimentación. 

Si un problema se agrava, debería activar una actualización del documento. Ya sea que el ingeniero de operaciones agregue lo que no estaba seguro, notó el caso de uso que desencadenó la escalada o el desarrollador aumentó la lista de viñetas, el resultado final hace que las operaciones sean más autosuficientes y reduce las escalaciones futuras. Quizás su [hábil gente de operaciones](https://www.youtube.com/watch?v=Z1B9E85_Msk) escribió un shell script que agrupa diez bullets en un solo comando; edite el runbook e inclúyalo. 

Y, sin embargo, a veces te encuentras con problemas desconocidos o impredecibles. En una empresa anterior, obtuve un runbook que era solo un elemento con viñetas: **“Esto nunca debería suceder. Si es así, llame a los desarrolladores"** . Hablé con el desarrollador y, sin acusarlos de ser vagos, le pregunté si esta era la mejor entrada de runbook que podían hacer. ¡Resultó que sí! Estaban monitoreando una afirmación que nunca debería suceder, pero si alguna vez sucedió, querían saberlo. Era el tipo de situación en la que una solución solo podía determinarse después de la primera vez que sucedía. 

Es importante eliminar los topes de velocidad para reparar y actualizar los runbooks. La gerencia debe crear una cultura en la que se espere y se anime a todos a editar con frecuencia, en tiempo real, no al final de un proyecto. Recomiendo que los ingenieros de operaciones vayan un paso más allá. Cuando lea un runbook, hágalo en modo de edición. Elimina la tentación de postergar las actualizaciones. Puedes pensar: 'Estoy en medio de abordar un problema en la producción, volveré más tarde y editaré esto'. No, nunca volverás. Nunca hay un más tarde. Si está en modo de edición, puede arreglar esa coma rota, pegar un comando actualizado o al menos tomar nota de que algo necesita mejorar. 

Si un paso no funciona o no está seguro de qué es lo que funciona, aún así, realice la edición. Estos son documentos vivos, por lo que no todas las ediciones tienen que ser perfectas. Escriba una nota para sí mismo o para el desarrollador: "esa última afirmación es confusa" o "la viñeta tres no funcionó". Al menos la próxima persona que vea esto sabrá que debe tener cuidado cuando llegue al punto número tres. Identificar el problema es mejor que el silencio.

El ciclo de retroalimentación permite a los desarrolladores controlar la frecuencia con la que se escalan. Si los desarrolladores sienten que los están escalando demasiado, bueno, médico, cúrate a ti mismo. Los desarrolladores pueden reducir futuras escalaciones mejorando el documento. Agregue los procedimientos que hubieran evitado que los operadores interrumpan su cena o realice llamadas de escalada deliberadas. 

El ciclo de retroalimentación brinda a las operaciones la confianza para escalar sin sentir que están molestando o rindiéndose demasiado pronto. Las operaciones pueden dudar en escalar un problema por temor a crear una situación de "niño que lloraba como un lobo" o que se vean estúpidos por no saber cómo manejar una situación. En cambio, las operaciones pueden "mostrar su tarea" para justificar su escalada. Es difícil sentirse molesto porque su cena se interrumpió cuando la persona de operaciones que lo llamó puede mostrar claramente que siguió el procedimiento escrito y los resultados de cada paso.

El beneficio de este ciclo de retroalimentación es que le brinda tanta o tan poca documentación como el proceso necesita, y tantas escalaciones como sea necesario. Permite a los desarrolladores solucionar el problema de obtener demasiadas escalaciones.

# Comparta, no acumule

Todo el mundo debería querer crear una organización en la que se comparta la información y se recompense el compartir.

Una vez trabajé en una empresa en la que se celebraba a una persona porque era la que mejor sabía manejar todo tipo de situaciones de la guardia. En retrospectiva, esto fue una bandera roja. ¿Por qué una persona era mucho mejor que todas las demás? ¿Se nos permite tener un servicio de mierda las semanas que otras personas están de guardia? Aprendí de esa experiencia.  

Ahora prefiero celebrar a las personas que comparten sus conocimientos para que todos sean excelentes en el servicio de guardia. Debemos honrar a quienes tienen más experiencia, pero celebrar a las personas que comparten sus conocimientos de manera que empoderen a todos para ser mejores. Esto incluye todo, desde la enseñanza individualizada hasta la respuesta a preguntas sobre Stack Overflow y la escritura de runbooks. Las personas que hacen eso permiten la excelencia sin importar a quién le toque llevar el on-call.

Podemos replantear esto en términos de dinámica de poder. La forma de la vieja escuela de mantener el poder y la influencia en una empresa era acumular información. Recuerdo haber admirado a una persona de una empresa anterior por la información que tenía. ¿Necesita realizar una [insertar tarea técnica]? Son la única persona que sabe cómo hacerlo. Visite su oficina. Muestre su respeto. Postrados ante su mente superior. Si lo consideran digno, harán las tareas por usted. Si quieres una empresa que funcione sin problemas, tira esa actitud tóxica al basurero de la historia.

La nueva forma es al revés. __El poder proviene de cuánto regalas__. Admiramos a la persona que comparte sus conocimientos: la persona que enseña a las personas cómo hacer las cosas en lugar de hacer las cosas por ellos; que se documenta constantemente, no al final del proyecto; que sea generoso con su conocimiento en todo lo que hacen. Son poderosos porque todos los señalan y dicen: "¡esa es la persona que me hizo exitoso!"

# Conocimiento fácilmente transferible

Aquí en Stack Overflow, tenemos una colección en nuestra instancia de Teams que contiene todos nuestros runbooks y procedimientos relacionados. Instamos a todos nuestros desarrolladores a que utilicen este proceso de comentarios con los documentos. El formato (artículos y preguntas que cualquiera puede comentar o editar) facilita la retroalimentación. Los runbooks que se utilizan con más frecuencia se han modificado y perfeccionado en gran medida. Los runbooks editados menos recientemente son fáciles de identificar y actualizar. El nivel de esfuerzo refleja la necesidad.

Luego están los efectos colaterales, las eficiencias adicionales que provienen de tener conocimiento probado en el campo fácilmente disponible. Las tecnologías y habilidades mencionadas en los runbooks nos informan cuando escribimos el anuncio de trabajo para el nuevo personal operativo. Una vez contratados, los runbooks se pueden utilizar como herramienta de entrenamiento. Se puede guiar a las personas de operaciones recién contratadas a través de cada runbook o utilizar los runbooks como ayuda para el autoaprendizaje. Una vez que hayan revisado todos los runbooks, estarán listos para estar de guardia. 

La clave de todos estos ciclos de retroalimentación es la facilidad con la que todos (desarrolladores, SRE y nuevos empleados) pueden hacer preguntas, plantear problemas y ofrecer sugerencias para mejores soluciones. A veces, la ansiedad de ser visto como menos conocedor puede evitar que las personas intervengan y comenten. Puede aliviar eso proporcionando explícitamente un espacio para preguntas en cada runbook. Aún mejor, puede usar una plataforma como Stack Overflow para Teams que está diseñada para recopilar información crítica para el negocio a partir de preguntas y respuestas. 

Un buen circuito de retroalimentación no resolverá todos los problemas en el proceso de guardia. Pero lo hará más sencillo, desde la depuración de un problema que aparece en la producción hasta la contratación, la capacitación y la incorporación. Cuando se hace bien, es una forma muy eficaz de mejorar su organización a través de procesos pequeños y arraigados.

# El add-on de #polemicaenvar

Dejamos el episodio de on-call y el episodio de postmortem donde hablamos sobre estos temas también.

{{< youtube LKDIY85rd20 >}}

{{< youtube 6d-Fb9R1-k4 >}}

* Traducción, revisión y publicación @jedux

