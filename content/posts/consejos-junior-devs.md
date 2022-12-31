---
Title: "Consejos para desarrolladores junior"
Description: "Este artículo menciona y vincula muchos conceptos muy valiosos para quienes estén arrancando a programar."
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

Thumbnail: assets/consejos-junior-devs.jpg
socialImage: assets/consejos-junior-devs.jpg
featuredImage: assets/consejos-junior-devs.jpg

Topics:
- dev
- desarrollo
- software
- mejores-practicas


markup: markdown
date: 2022-12-31
draft: false
---

_La versión original de este post se puede encontrar en [DEV Community](https://dev.to/jeroendedauw/advice-for-junior-developers-30am) (inglés)._

Esta publicación menciona y vincula con muchos conceptos valiosos que podés explorar en mayor detalle según creas necesario. Tiene tres secciones:

+ Consejos Generales – Contexto y motivación importante para los consejos técnicos
+ Consejos Técnicos – La parte principal
+ Lecturas Recomendadas – Vínculos a libros de buena calidad y blogs que son geniales para arrancar

## Consejos Generales para Juniors

### 1. El código no es lo importante

Como desarrolladores, nos gusta escribir código. A la mayoría nos gusta que nos den una tarea precisa. Un desafío técnico divertido para resolver sin prestarle atención al resto del mundo.

Tomate el trabajo de asegurarte de que estás resolviendo el problema correcto. Citando a Peter Drucker: [No hay nada tan inútil como hacer eficientemente aquello que no debería ser hecho en absoluto](https://medium.com/swlh/there-is-nothing-so-useless-as-doing-efficiently-something-that-should-not-have-been-done-at-all-8c5d2282319d). Juntá información temprano y seguido, típicamente con entrega continua a usuarios reales. [Sé Ágil](https://agilemanifesto.org/principles.html).

El desarrollo de software es caro, con la mayor parte del esfuerzo de los proyectos del mundo real típicamente dirigidos al mantenimiento. Combiná esto con que el objetivo es que el usuario/negocio obtenga resultados, [el mejor código a veces no es código](https://blog.codinghorror.com/the-best-code-is-no-code-at-all/). Citando a Bill Gates: “Medir el progreso de un trabajo de programación en cantidad de líneas de código es como medir el progreso de construcción de un avión por peso.”

Ver también: [YAGNI](https://es.wikipedia.org/wiki/YAGNI), [KISS](https://es.wikipedia.org/wiki/Principio_KISS), [The Last Responsible Moment](https://blog.codinghorror.com/the-last-responsible-moment/) (en inglés).

### 2. El diseño de software importa

Durante los 5 años de mi carrera en desarrollo de software, pensé que el diseño de software era para los arquitectos de software u otra gente con roles especiales. Estaba enfocado en “hacer las cosas”, y veía el diseño de software y prácticas cómo escribir pruebas, como una distracción en el mejor de los casos. Mi código funcionaba, estaba terminando un montón de cosas. O al menos eso creía.

Después leí [Clean Code](https://www.goodreads.com/book/show/3735293-clean-code), de [Robert C. Martin](https://cleancoders.com/). Este libro te motiva a que te interese el diseño de software y contiene ejemplos y mucha heurística técnica. La conclusión más conceptual es el dicho “**la única manera de hacerlo rápido es hacerlo bien**”. En otras palabras, [si haces una chanchada, te va a demorar](https://martinfowler.com/articles/is-quality-worth-cost.html). Ver también: [TradableQualityHypothesis](https://martinfowler.com/bliki/TradableQualityHypothesis.html), [DesignStaminaHypothesis](https://martinfowler.com/bliki/DesignStaminaHypothesis.html) (en inglés).

Aprender cómo escribir código limpio y bien diseñado lleva tiempo y esfuerzo, por supuesto. Y cuando empieces, vas a ser lento y cometer errores. [Simple no es Fácil](https://www.entropywins.wtf/blog/2017/01/02/simple-is-not-easy/).

### 3. Usá MEJORES prácticas

Escribir pruebas tiende a ser beneficioso. Hay algunas excepciones, pero la mayoría de las veces, tiene mucho sentido escribir pruebas automáticas. Escribir pruebas es un ejemplo de una buena práctica.

Si sos nuevo escribiendo pruebas, simplemente seguí las mejores prácticas y escribí pruebas para todo. **Cuando estás arrancando, seguir ciegamente las mejores prácticas va a ser mejor que seguir tu propio juicio subdesarrollado.** Con el tiempo aprenderás cómo escribir pruebas efectivamente, y darte cuenta de la diferencia de meter la pata, y situaciones en las que escribir una prueba no vale la pena. También empezarás a entender el valor que traen las pruebas a un nivel más visceral, experimentando la disminución de las sesiones de búsqueda de errores en el código y la posibilidad de rehacer tu código sin preocupaciones que te permiten tus pruebas. **Después de desarrollar tu juicio, podrás trascender las mejores prácticas.**

Este consejo aplica para mejores prácticas de cualquier área en la que estés arrancando. Las pruebas automáticas son solo un ejemplo.

Un gran problema es que no es fácil diferenciar entre una prueba sensata o algo insensato o incluso contraproductivo. Esto se complica aún más con el lío que es la mayoría del código existente, y por el hecho de que la mayoría de los desarrolladores, incluyendo los “experimentados” y “senior”, no saben lo básico del diseño de software. Esto hace que tener un buen mentor sea algo extremadamente valioso. Dejando eso de lado, un consejo basado en mi propia experiencia es tener cuidado con las mejores prácticas específicas a la comunidad de tu lenguaje de programación o framework. Buscá consejos perennes que han estado dando vueltas por décadas.

## Consejos Técnicos para Principiantes

Nuestro enfoque será en tópicos técnicos. Muchas otras áreas son importantes, como la salud, la felicidad, la carrera, las habilidades blandas. Saber cómo esquivar una caída técnica no te va a ayudar si estás sin dormir y trabajando en el problema incorrecto para un jefe tóxico que te paga mal.

### 4. Escribí pruebas

Escribí pruebas automatizadas. Tal vez escribi pruebas antes de escribir código, como en el [Desarrollo Guiado por Pruebas](https://es.wikipedia.org/wiki/Desarrollo_guiado_por_pruebas). Esto simplifica la tarea de verificar si tu código es correcto en una manera repetible, salvándote de de muchas pruebas manuales y de sesiones de búsqueda de errores.

>¿Pensás que probar antes es difícil? Tratá de encontrar errores después.

Algo que es tal vez más importante, las pruebas te dan una red de seguridad para refactorizar tu código. Una refactorización continua es necesaria para mantener tu código limpio. Sin un conjunto de pruebas confiables, es más probable que tu código se pudra.

Escribir pruebas es difícil si el diseño de tu código es pobre, como cuando usas código reutilizado heredado, o cuando usas funciones estáticas. Si, por otro lado, tenés clases [SOLID](https://es.wikipedia.org/wiki/SOLID), sin dependencias globales, entonces escribir buenas pruebas no es tan difícil.

El diseño de pruebas importa porque las pruebas mal escritas te van a retrasar.  Evitá vincular tus pruebas a detalles de implementación del código que todavía están a prueba o a la estructura del sistema. Evitá sobreutilizar Mocks y [escribí mejores Dobles de Prueba](https://www.entropywins.wtf/blog/2016/05/13/5-ways-to-write-better-mocks/).

### 5. No uses herencia para reutilización de código

Esta es una de las mejores buenas prácticas que la sección “Uso de mejores prácticas” trae a colación. Mi recomendación: no uses herencia para reutilización de código en lo absoluto cuando estás arrancando. Rara vez es la opción correcta y puede ocasionar muchos problemas. [Favorecé la composición por sobre la herencia](https://en.wikipedia.org/wiki/Composition_over_inheritance).

### 6. Escribí código orientado a objetos

Escribí código [SOLID](https://es.wikipedia.org/wiki/SOLID) que no sea [STUPID](https://williamdurand.fr/2013/07/30/from-stupid-to-solid-code/). Hay muchísimo valor en entender estos principios y antipatrones.

Creá objetos. Las clases con solo métodos estáticos no son orientadas a objetos. Tratá de evitar usar código estático.

Ver también: [mi defensa de SOLID](https://www.entropywins.wtf/blog/2017/02/17/why-every-single-argument-of-dan-north-is-wrong/) (en inglés).

### 7. Escribí código funcional

([Programación funcional](https://es.wikipedia.org/wiki/Programaci%C3%B3n_funcional) no debe ser confundida con [programación estructurada](https://es.wikipedia.org/wiki/Programaci%C3%B3n_estructurada) [imperativa](https://es.wikipedia.org/wiki/Programaci%C3%B3n_imperativa).)

Este ítem no es para que te cambies a un lenguaje funcional. Podés aprovechar los beneficios de usar estilo funcional en tu lenguaje orientado a objetos. [Minimizá los estados](https://www.entropywins.wtf/blog/2018/10/24/readable-functions-minimize-state/), especialmente los estados mutables, y [hacé una sola cosa en tus funciones](https://www.entropywins.wtf/blog/2018/10/30/readable-functions-do-one-thing/). Ver también: [núcleo funcional, caparazón imperativo](https://www.destroyallsoftware.com/screencasts/catalog/functional-core-imperative-shell) (en inglés).

### 8. Usa duplicación basada en información

Copiar y pegar grandes pedazos de código a múltiples lugares es casi siempre imprudente. Cualquier desarrollador que se respeta a sí mismo rápidamente aprende esto y empieza a seguir cierta forma de [No te repitas](https://es.wikipedia.org/wiki/No_te_repitas). Desafortunadamente, el objetivo bien intencionado de DRY (No te repitas, por su sigla en inglés) usualmente lleva a la sobreingeniería y complejidad accidental. Acá es donde la contraparte de DRY entra: Escribí Todo Dos Veces (WET, por su sigla en inglés). La idea detrás de WET es de deduplicar en la tercera ocurrencia de una duplicación.

Para un análisis más en detalle de los costos y beneficios de la deduplicación, ver [The Fallacy of DRY](https://www.entropywins.wtf/blog/2017/09/06/the-fallacy-of-dry/) (en inglés).

### 9. Tipos, Nombres y Comentarios

Tratá de escribir código autodocumentado y evitá los comentarios.

>Cada vez que escribas un comentario, deberías hacer una mueca y sentir el fracaso de tu habilidad de expresión.
>
>– Robert C. Martin

Los comentarios son peligrosos porque pueden mentir. El código puede cambiar sin que el comentario sea actualizado. Código nuevo puede ser agregado directamente debajo del comentario. El comentario puede haber estado mal o impreciso en un primer lugar. Cuando esto pasa, el comentario no solo se convierte en inútil, se convierte en engañoso.

Para escribir código autodocumentado:

+ [Hacé una sola cosa en tus funciones](https://www.entropywins.wtf/blog/2018/10/30/readable-functions-do-one-thing/).
  - Haciendo una sola cosa en una función, le podés dar un nombre claro.
  - ¿Sentís la necesidad de explicar qué hacen las diferentes secciones de tu función agregando comentarios? En lugar de eso, extraé cada sección a su propia función claramente nomenclada.
  - [“Extraé hasta el hartazgo”](https://verraes.net/2013/09/extract-till-you-drop/): Si podés extraer una función, entonces deberías. No le tengas miedo a las funciones chiquitas.
  - [Separación de comandos y consultas, CommandQuerySeparation](https://martinfowler.com/bliki/CommandQuerySeparation.html).
  - Similar al [Principio de responsabilidad única](https://es.wikipedia.org/wiki/Principio_de_responsabilidad_%C3%BAnica) para las clases (La S en SOLID).
+ **[Minimizá los estados](https://www.entropywins.wtf/blog/2018/10/24/readable-functions-minimize-state/).**
+ **Usá tipos.** Junto con el conjunto de pruebas que ejecutan el código, podés confiar en los tipos para decirte la verdad.
+ **Evitá tipos mezclados.** Evitá parámetros o valores de retorno que pueden ser un entero, un valor binario, o una cadena de texto. Esto sucede naturalmente si escribís funciones enfocadas que hacen solo una tarea.
+ **Escribí pruebas:** Un buen conjunto de tareas bien escrito y comprensivo te muestra cómo puede ser utilizado el código de producción, y cómo se comporta.

[Clean Code](https://www.goodreads.com/book/show/3735293-clean-code) de Robert C. Martin tiene algunas buenas reglas sobre nomenclatura y comentarios.

## Lecturas Recomendadas para Juniors (en inglés)

### Libros

+ **[Clean Code](https://www.goodreads.com/book/show/3735293-clean-code), 2007 libro de  Robert C. Martin**
+ **[Apprenticeship Patterns: Guidance for the Aspiring Software Craftsman](https://www.goodreads.com/book/show/5608045-apprenticeship-patterns), 2009**
+ [Working Effectively with Legacy Code](https://www.goodreads.com/book/show/44919.Working_Effectively_with_Legacy_Code), 2004 libro de Michael Feathers
+ [Refactoring: Improving the Design of Existing Code](https://www.goodreads.com/book/show/44936.Refactoring), 1999
+ [The Software Craftsman](https://www.goodreads.com/book/show/23215733-the-software-craftsman), 2014

### Blogs

+ [MartinFowler.com](https://martinfowler.com/) - Muchísimos artículos de alta calidad sobre todo lo relacionado con el desarrollo de software
+ [EntropyWins.wtf](https://www.entropywins.wtf/) - Cláramente el mejor blog de internet :)

Ver también: [Recommended Reading for Developers](https://blog.codinghorror.com/recommended-reading-for-developers/) de Jeff Atwood

### Links Extra
+ [Tell Don't Ask](https://martinfowler.com/bliki/TellDontAsk.html) – Buena práctica de encapsulación.
+ [Law of Demeter](https://wiki.c2.com/?LawOfDemeter) – Buena práctica de acoplamiento.
+ [Diseño guiado por el dominio](https://es.wikipedia.org/wiki/Dise%C3%B1o_guiado_por_el_dominio) – Una gran herramienta. Más avanzada, conviene aprender primero lo más básico.
+ [Object Calisthenics](https://williamdurand.fr/2013/06/03/object-calisthenics/) – Reglas que limitan lo que podés hacer en programación. Bueno para aprender cómo poder hacer las cosas de otra manera.
+ [Programación en pareja](https://es.wikipedia.org/wiki/Programaci%C3%B3n_en_pareja) – Una muy buena manera de aprender de los otros.
+ [Code katas](https://codingdojo.org/kata/) – Programación simple, genial para practicar una técnica o habilidad específica como el Desarrollo Guiado por Pruebas (TDD).

### Sobre Jeroen

[Jeroen De Dauw](https://www.entropywins.wtf/) es el CEO de [Professional Wiki](https://professional.wiki/), que provee servicios de [hosting de wikis](https://www.pro.wiki/). Ocasionalmente escribe en su [blog de diseño de software](https://www.entropywins.wtf/blog/). Podés [seguir a Jeroen en Twitter](https://twitter.com/JeroenDeDauw).

* La versión original de este post se puede encontrar en [DEV Community](https://dev.to/jeroendedauw/advice-for-junior-developers-30am) (inglés).
* Autoría por [Jeroen De Dauw](https://twitter.com/JeroenDeDauw), traducción por [@jcasarini](https://twitter.com/jcasarini), revisión por [@nachichuri](https://twitter.com/nachichuri).
