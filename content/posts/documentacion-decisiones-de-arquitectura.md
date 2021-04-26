---
draft: true
title: "Documentación De Decisiones De Arquitectura"
date: 2021-04-25

keywords:
    - arquitectura
    - documentación
tags:
    - arquitectura
    - documentación
topics:
    - arquitectura
    - documentación
thumbnail: assets/documentacion-decisiones-de-arquitectura.jpg
socialImage: assets/documentacion-decisiones-de-arquitectura.jpg
featuredImage: assets/documentacion-decisiones-de-arquitectura.jpg
externalPermlink: "https://cognitect.com/blog/2011/11/15/documenting-architecture-decisions"
---
# CONTEXTO

La arquitectura de los proyectos ágiles debe describirse y definirse de forma diferente. No todas las decisiones se tomarán a la vez, ni tampoco se tomarán todas al comenzar el proyecto.

<!--more-->

Un {{< canonical href="https://cognitect.com/blog/2011/11/15/documenting-architecture-decisions" text="artículo" >}} de [
Michael Nygard](https://twitter.com/Ruurtjan)

Los métodos ágiles no se oponen a la documentación, **sólo a la documentación sin valor**. Los documentos que ayudan al equipo pueden tener valor, pero sólo si se mantienen actualizados. Los documentos grandes **nunca** se mantienen actualizados. Los documentos pequeños y modulares tienen al menos **una** oportunidad de ser actualizados.

Además, nadie lee nunca los documentos grandes. La mayoría de los desarrolladores han estado en al menos un proyecto en el que el documento de especificaciones era más grande (en bytes) que el tamaño total del código fuente. Esos documentos son demasiado grandes para abrirlos, leerlos o actualizarlos. En partes pequeñas son más fáciles de consumir para todas las partes interesadas.

**Una de las cosas más difíciles de seguir durante la vida de un proyecto es la motivación que hay detrás de ciertas decisiones**. Una persona nueva que llega a un proyecto puede estar perpleja, desconcertada, encantada o enfurecida por alguna decisión anterior. Sin entender los motivos ni las consecuencias, esta persona sólo tiene dos opciones:

1. **Aceptar ciegamente la decisión.**

    Esta respuesta puede estar bien, si la decisión sigue siendo válida. Sin embargo, puede no ser buena si el contexto ha cambiado y la decisión debería ser realmente revisada. Si el proyecto acumula demasiadas decisiones aceptadas sin comprensión, entonces el equipo de desarrollo tiene miedo de cambiar algo y el proyecto se derrumba por su propio peso.

2. **Cambiar a ciegas.**

    De nuevo, esto puede estar bien si la decisión necesita ser revertida. Por otro lado, cambiar la decisión sin entender su motivación o sus consecuencias podría significar dañar el valor global del proyecto sin darse cuenta. (Por ejemplo, la decisión apoyaba un requisito no funcional que aún no se ha probado).

Es mejor evitar tanto la aceptación ciega como la revocación ciega.

# DECISIÓN

Mantendremos una colección de registros para las decisiones "arquitectónicamente significativas": las que afectan a la estructura, los requerimientos no funcionales, las dependencias, las interfaces o las técnicas de construcción.

Un registro de decisiones de arquitectura (ADR) es un breve archivo de texto en un formato similar a un patrón [alejandrino](https://es.wikipedia.org/wiki/Alejandrino). (Aunque las decisiones en sí mismas no son necesariamente patrones, comparten el equilibrio de fuerzas característico). Cada registro describe un conjunto de fuerzas y una única decisión en respuesta a esas fuerzas. Tenga en cuenta que la decisión es la pieza central aquí, por lo que las fuerzas específicas pueden aparecer en múltiples ADR`[^1].

Mantendremos los ADR en el repositorio del proyecto bajo `doc/arch/adr-NNN.md`

Deberemos utilizar un lenguaje de formato de texto ligero como [Markdown](https://www.markdownguide.org/) o Textile.

Los ADRs se numerarán de forma secuencial y monótona. Los números no se reutilizarán.

Si se revoca una decisión, mantendremos la antigua, pero la marcaremos como superada. (Sigue siendo relevante saber que era la decisión, pero ya no lo es).

Utilizaremos un formato con pocas partes, para que cada documento sea fácil de digerir. El formato tiene sólo unas pocas partes.

**Título** Estos documentos tienen nombres que son frases sustantivas cortas. Por ejemplo, _"ADR 1: Deployment on Ruby on Rails 3.0.10"_ o _"ADR 9: LDAP for Multitenant Integration"._

**Contexto** Esta sección describe las fuerzas en juego, incluyendo las tecnológicas, políticas, sociales y locales del proyecto. Estas fuerzas están probablemente en tensión, y deben ser señaladas como tales. El lenguaje de esta sección es neutral en cuanto a valores. Simplemente se describen los hechos.

**Decisión** Esta sección describe nuestra respuesta a estas fuerzas. Se expresa en frases completas, con voz activa. "Vamos a..."

**Estado** Una decisión puede ser "propuesta" si las partes interesadas del proyecto aún no están de acuerdo con ella, o "aceptada" una vez que se ha acordado. Si una ADR posterior modifica o revoca una decisión, puede marcarse como "obsoleta" o "superada" con una referencia a su sustitución.

**Consecuencias** Esta sección describe el contexto resultante, tras aplicar la decisión. Aquí deben enumerarse todas las consecuencias, no sólo las "positivas". Una decisión concreta puede tener consecuencias positivas, negativas y neutras, pero todas ellas afectan al equipo y al proyecto en el futuro.

El documento completo debe tener una o dos páginas. Redactaremos cada ADR como si fuera una conversación con un futuro desarrollador. Esto requiere un buen estilo de redacción, con frases completas organizadas en párrafos. Las viñetas son aceptables sólo por estilo visual, no como excusa para escribir fragmentos de frases. (Bullets kill people, even PowerPoint bullets.) NdE: esta frase quedo en inglés para que no pierda la sutileza.

# ESTADO

Aceptado.

# CONSECUENCIAS

Una ADR describe una decisión significativa para un proyecto concreto. Debe ser algo que repercuta en el desarrollo del resto del proyecto.

Es muy probable que las consecuencias de una ADR se conviertan en el contexto de las siguientes ADR. Esto también es similar a la idea de Alexander de un lenguaje de patrones: las respuestas a gran escala crean espacios en los que las de escala mas pequeña encajan.

Los desarrolladores y las partes interesadas del proyecto pueden ver las ADR, incluso cuando la composición del equipo cambia con el tiempo.

La motivación de las decisiones anteriores es visible para todos, presentes y futuros. Nadie se queda rascándose la cabeza para entender **"¿en qué estaban pensando?"** y el momento de cambiar las antiguas decisiones estará claro a partir de los cambios en el contexto del proyecto.

-----

# INFORME DE EXPERIENCIAS

Habrás notado que este post tiene el formato de un ADR propiamente dicho. Llevamos utilizando este formato en algunos de nuestros proyectos desde principios de agosto. No es mucho tiempo en el sentido global, pero los primeros comentarios, tanto de clientes como de promotores, han sido bastante positivos. En ese tiempo, hemos tenido entre seis y diez promotores que han rotado por los proyectos utilizando las ADR. Todos ellos han declarado que aprecian el grado de contexto que recibieron al leerlos.

Las ADR han sido especialmente útiles para **captar las intenciones a largo plazo.** Tenemos varios clientes que están estabilizando sus sistemas actuales, pero que están pensando en una reestructuración mayor en un futuro no muy lejano. Al anotar estas intenciones, no dificultamos inadvertidamente esos cambios futuros.

Una posible objeción es que mantenerlas en el control de versiones con el código las hace menos accesibles para los gestores de proyectos, las partes interesadas del cliente y otras personas que no viven en el control de versiones como lo hace el equipo de desarrollo. En la práctica, casi todos nuestros proyectos viven en repositorios privados de GitHub, por lo que podemos intercambiar enlaces a la última versión en `master. Como GitHub procesa el markdown automáticamente, su aspecto es tan amigable como el de cualquier página wiki.

Hasta ahora, los ADRs están demostrando ser una herramienta útil, así que seguiremos utilizándolos.

# MÁS LECTURA

Gracias a Philipe Kruchten por hablar de la importancia de las decisiones de arquitectura. Me han dicho que hay más sobre ellas en [Documenting Software Architectures](https://resources.sei.cmu.edu/library/asset-view.cfm?assetID=30386), que está cerca de la parte superior de mi cola de lectura.

-----

# MÁS Links

- [Architectural decision](https://en.wikipedia.org/wiki/Architectural_decision)
- [ADR in Github](https://adr.github.io/)
- [Sustainable Architectural Design Decisions](https://www.infoq.com/articles/sustainable-architectural-design-decisions/)
- [A Definition of Done for Architectural Decision Making](https://www.ozimmer.ch/practices/2020/05/22/ADDefinitionOfDone.html)

[^1]: ADR, architecture decision record.