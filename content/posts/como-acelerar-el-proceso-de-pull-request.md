---
title: "Como Acelerar El Proceso De Aprobación de los Pull Request"
date: 2021-05-02T21:20:38-03:00
description: "A la hora de agregar nuevo código, GitHub introdujo el concepto de Pull Request (PR), donde uno o mas humanos(Requester), le avisa a otros humanos (Reviewer), que estan tratando de incorporar nuevos cambios al repositorio. La idea es que el Reviewer revise esos cambios, y devuelva en forma de feedback. Esta feature es sumamente útil a la hora de hacer code review, pero por razones de la vida a veces este proceso se hace muy largo."
draft: true

keywords:
    - code review
    - pull request
    - git
tags:
    - code review
    - pull request
    - git
topics:
    - code review
    - pull request
    - git
thumbnail: assets/como-acelerar-el-proceso-de-pull-request.png
socialImage: assets/como-acelerar-el-proceso-de-pull-request.png
featuredImage: assets/como-acelerar-el-proceso-de-pull-request.png
externalPermlink: "https://medium.com/@m_vicent/como-acelerar-el-proceso-de-aprobaci%C3%B3n-en-los-pull-request-5eb6303cf761"
---

# Code review mas rápidos

[Git](https://git-scm.com/) y [GitHub](https://github.com/) tomaron la delantera en versionado de código, hoy prácticamente todas las empresas medianas/chicas/grandes lo usan para mantener y versionar su código.
A la hora de agregar nuevo código, GitHub introdujo el concepto de [Pull Request (PR)](https://docs.github.com/es/github/collaborating-with-issues-and-pull-requests/about-pull-requests), donde uno o mas humanos(Requester), le avisa a otros humanos (Reviewer), que están tratando de incorporar nuevos cambios al repositorio. La idea es que el Reviewer revise esos cambios, y devuelva en forma de feedback. Esta funcionalidad es sumamente útil a la hora de hacer code review, pero por razones de la vida a veces este proceso se hace muy largo.
Estos son algunos consejos y trucos que aprendí y encontré por ahí y que podes agregar a tu flow de trabajo para acelerar el proceso desde que mandás un PR hasta que se aprueba/mergea.

## Disclaimer:
Esto no es una guía de cómo hacer code review. Para eso existen [libros y papers enteros sobre eso.](https://github.com/joho/awesome-code-review)
Esto más bien son consideraciones para reducir el trabajo entre ambas partes, centrado en el flow de github y solo pensando para enviar y recibir pull requests.

# Consejos para cualquiera de las partes

## Configurar las notificaciones. 🔔

Parece un poco obvio, pero asegurarse de tener prendidas las notificaciones por el medio que mas te guste, es algo que debemos hacer para enterarnos que tenemos que hacer algo con un pull request.

La notificaciones pueden ser por email, por web, por push notifications o incluso hay unos plugins re piolas para Slack etc. La casa recomienda fuerte: [pullreminders](https://pullreminders.com)

Si no querés mirar las notificaciones, al menos entra un par de veces al día al [menú](https://github.com/pulls/review-requested) de GitHub. Ahí esta toda la información sobre los pull request que requieren una acción tuya.

## Guarda un poco de tiempo en tu agenda/dia a dia. 📅

Un reminder en el calendar, mientras tomas el café de la mañana, o terminaste con la maratónica meeting party, pero que ese tiempo este y este bloqueado, para que te puedas concentrar en eso.

## Involucrar al equipo. 👨‍👩‍👧‍👧👩‍👩‍👧‍👧

Una sola persona no puede estar haciendo las reviews. Esto a veces es complicado porque muchas veces los reviews recaen sobre la misma persona, hay que evitar que eso pase, sino el conocimiento no se comparte. Una buena práctica podría ser, no tener más de X cosas en status “review”.

## Darse por vencido.

Si ya paso mucho tiempo, y no tomaste ninguna acción, fíjate si alguien te puede ayudar con eso, y si sigue siendo valido el PR.

Podes considerar bloquear el ticket relacionado como para especificar que hasta que no hagan el review, el ticket se encuentra bloqueado porque necesitas eso para seguir.

## Evita discusiones largas (o chat). 💬

Especialmente las que no tienen una relación con lo que representa ese PR, Si la discusión se empieza a ir fuera del scope del pr, ticket etc, Quizás sea momento de hacer una llamada, poner una reunión o hablarlo con el equipo.

## Asegurarse que el PR, Tiene los reviewers correctos,(o tiene reviewers).

También, un poco obvia, pero es la mejor manera de notificar que “tienes un pr para revisar” es agregar el reviewer en la sección correspondiente. _(Solapita de la derecha)_.Puede ser una persona o un team

## Usar GitHub teams.

Esta feature esta hace rato, pero básicamente son groups de personas que cuentan como si fuera 1 reviewer, cualquiera de ese grupo que deje un review, cuenta como reviewer.
Se puede configurar de mil maneras, Incluso se puede setupear que un mínimo de 2 reviewers por team, haciendo round robin para no enganchar a las mismas 2 personas.

## Algunas cosas no requieren aprobación de PR.
Esto no quiere decir que no se haga, el PR, pero tal vez no hace falta que se firme o que lo revise alguien. Puede ser una emergencia o hot fix, o simplemente es tan trivial que no vale la pena molestar a otra persona.

## Considerar donde esta el cierre
Medir niveles de urgencia, entender que se esta tratando de cumplir, y considerar que algunas cosas , algunos cambios se puede seguir en otro PR. No hace falta que se entregue algo prístino en el primer intento.
La idea de hacer PRs, es que el código lo mire mas de una persona, algunos autores recomiendan que si hacemos algo así como pair programming, podemos hacer un PR y mergearlo, no necesitamos approve. (Hay unos [plugins](https://github.com/kejadlen/git-together) de git re copados para eso).

# Consejos para Requesters.
## Auto review
Primero que nada. Limpia toda la mugre que haya quedado o que no sea consistente con lo que tenes que enviar.

Deja comentarios propios, si algo no queda claro, contar un poco porque lo resolviste de esa forma, o explica un poco mejor que estas haciendo. Si lo amerita dejar comentarios en el código también.

Recordar que, si bien github es bueno para mostrar lo que se ve, también es muy bueno para ocultar otras que no se vean.

## Escribir una buena descripcion en el pr:
La explicación en la portada de del ticket es clave. Screenshots, gifs, bulletpoints, memes, cualquier cosa que ayude a entender el concepto que estamos armando y por que necesitamos ese cambio.

## Clasificar tus PR.
Comprimilos en pequeños unidades de información. De la misma manera que haces commits atómicos, trata de enviar pull request atómicos.
Esto genera que el reviewer tenga menos trabajo y tiempo de review donde se vea claro el objetivo. La idea seria que cambios mas chicos, menos esfuerzo cognitivo al reviewver y por lo tanto son mas fáciles de revisar / aprobar.
Hay una [guía mas detallada](https://sergeyzhuk.me/2018/12/29/code_review) de esto.

## Encadena tus Prs

Si tenes dependencias entre PRs, uni las referencias, para que queden encadenadas. ej: abro branch de develop a my-feature-part-1 y luego abro un my-feature-part2 que sale de my-feature-part-1.

## Se perseverante
Quizás mas de X días sea buen momento para pinguear a los reviewvers, pregunta porque nadie lo reviso, empuja para que salga adelante. Los prs (A diferencia del Whisky) no mejoran con el tiempo.

## Las tareas no son siempre son 1 pr : 1ticket.
Considera que 1 ticket puede ser N pull request, salvo regla explicita, no es necesario resolver todo un ticket en 1 PR. podes hacer mas de 1 para la misma tarea. Vas a tener mas tiempo de review, pero vas a tener fragmentos mas consistentes a la hora de mandar un cambio.

## Mandar un early preview del PR,
Puede ayudar a ejemplificar el angulo que tomaste, no te olvides de poner un `wip`, Hay que tener en cuenta que esto también puede agregar ruido a la hora de “revisar” cosas.
Esto es mas bien para validar diseños, ángulos y tener una visibilidad de progreso.
Actualmente github tiene una función “draft” para tener una early version.

# Consejos para Reviewers.
## Mantené los comentarios sobre el código que se esta discutiendo en el momento.
Deja el estilo y la forma para los linters, las herramientas, o impulsa por tener y mantener una convención.
Si ves cosas mal hechas, que ya estaban, no esta mal arreglarlas solo que quizás no en ese contexto.

## Prioridades
El código en PR, es el más cercano a prod, por lo tanto trata de darle prioridad, que el que no se escribió o esta por escribir.

## Decidí
Si no ves nada malo o raro, no dudes en aprobar, no procrastines o dejes “para mas tarde”. Si no estas seguro, llama a otro reviewer que te ayude a revisar.
Quizás hay cosas que no entendés o sabes de alguien mas interesado en revisar eso.

## TL;DR
Si es muy largo, deja una nota hasta donde revisaste, y que es lo que entendiste, si bien no completaste el objetivo, mínimamente hiciste un repaso, y eso le va a dar una pauta al próximo reviewer por donde seguir.

## De atrás para adelante
Una buena forma de empezar es mirar los tests que se esta agregando. Eso puede dar una buena pista de que funcionalidad se trata de testear.

## Usa los ☑️ de los files.
los checks de los files de arriba a la derecha, dan 3 ventajas:
- Esconden código que ya revisaste.
- Esconden files que “no te interesan” ej: yarn.lock.
-Se te avisa cuando el Requester mando nuevos cambios desde que vos revisaste, re abriendo esos files. Usalos.

## Sugeri codigo
Dan mucha velocidad al requester. (Cuidado con el identado o dependencias).

## Identifica y clasifica tu feedback
* Comment & Approve: Viste algo que es menor, no es bloquearte o no podría generar nuevos errores. ✅ . Es valido dejar coments por: cambios chicos, cosas que podrian hacerse mejor, pero no son bloqueantes.
* Request changes: Viste algo que no debería llegar a prod, hay algo que no te cierra como esta hecho, viste algo que rompe retrocompatiblidad. ❌
También se puede usar una [convención de tipos de mensajes](https://conventionalcomments.org).

## Dar un veredicto
En general hacer una revisión y dejar feedback en un PR es correcto, pero también se busca una conclusión, y/o dictamen de parte del Requester.
Esto a veces no se da si hay muchas dudas o falta de conocimiento/contexto, respecto al cambio que se esta aplicando. Esto puede ser un buen indicador para dejar este mismo feedback en la review, y pedir por otro reviewer, con mayor conocimiento.
No concluir y dejar pendiente el PR , deja en un limbo los cambios.

# Conclusión
Los Prs, son solo una parte del proceso de code review. El code review es lo que aporta valor, el PR, es una forma fancy de poder hacer code review.
No hay soluciones mágicas. Y todo se reduce a personas cooperando con buena voluntad.

[Artículo original](https://medium.com/@m_vicent/como-acelerar-el-proceso-de-aprobaci%C3%B3n-en-los-pull-request-5eb6303cf761 de), revisó @jedux.

# Links y Referencias.

- https://sergeyzhuk.me/2018/12/29/code_review
- https://dev.to/ph1/6-practices-for-effective-pull-requests-129d
- https://blog.codinghorror.com/pair-programming-vs-code-reviews/
- https://github.com/kejadlen/git-together / https://github.com/pivotal-legacy/git_scripts / https://github.com/git-duet/git-duet
- https://github.com/palantir/bulldozer
- https://github.com/joho/awesome-code-review
- https://pullreminders.com
- https://conventionalcomments.org
