---
Title: "¿Estás list@ para Vim? Una guía para principiantes"
date: 2022-02-01
draft: false
Description: "Después de leer esta guia definitiva, vas a querer usar [esta remera](https://tienda.sysarmy.com/productos/wq/) y [esta birome](https://tienda.sysarmy.com/productos/vi-rome/) todos los días."
markup: markdown

Keywords:
  - vim
  - herramientas
  - editor
  - sistemas
Tags:
  - sysarmy
  - vim
  - herramientas
  - editor
  - sistemas
  - wq!
Topics:
  - vim
  - herramientas
  - editor
  - sistemas

Thumbnail: assets/vim-beginner-guide-thumbnail.webp
socialImage: assets/vim-beginner-guide-thumbnail.webp
featuredImage: assets/vim-beginner-guide-thumbnail.webp
externalPermlink: "https://thevaluable.dev/vim-commands-beginner/"
---
_La versión original de este post se puede encontrar en [The Valuable Dev](https://thevaluable.dev/vim-commands-beginner/) (inglés)._

_"¡Vim no es para mí!"_ gritó David, mi compañero desarrollador.

No es la primera vez que escucho esta frase. ¿El resultado? Yo, explicándole a David y a otras personas reunidas alrededor de mi escritorio que aprender los conceptos básicos de Vim puede ser beneficioso para cualquiera:

- Muchas [interfaces de línea de comandos](https://es.wikipedia.org/wiki/Interfaz_de_l%C3%ADnea_de_comandos) usan atajos de teclado similares a Vim, como [less](https://es.wikipedia.org/wiki/Less), por ejemplo.
- Se pueden editar fácilmente archivos en sistemas remotos o en contenedores de docker cuando solo Vi (el antepasado de Vim) o Vim están disponibles.
- Tiene muchas posibilidades de personalización, para que coincida con tus necesidades y preferencias personales.
- Se puede ejecutar Vim donde quieras.
- Vim puede editar archivos de texto muy grandes sin tildarse, como archivos de registro grandes, por ejemplo.
- Se puede aprender una forma nueva y divertida de crear y editar contenido.

Para mí, Vim es la **gamificación de la programación**.

Aún así, algunos desarrolladores no intentan entender de qué se trata Vim. Al mismo tiempo, tienen una opinión tajante al respecto. ¿Cómo puede alguien juzgar algo sin realmente probarlo?

No puedo culparlos: yo tenía exactamente el mismo sesgo hace años. Pero cuando traté de aprender a usar Vim, cuando traté de entender cómo funciona, no solo aprender dos atajos al azar, me enamoré.

Es por eso que hoy me gustaría compartir con ustedes cómo aprendí los conceptos básicos de Vim. Más específicamente, en este artículo veremos:

- Cómo aprender rápidamente buenas técnicas de tipeo. Son esenciales si querés liberar el poder latente de Vim. Incluso si no usas Vim, estas técnicas tienen muchos beneficios para cualquier desarrollador.
- Los diferentes modos de Vim. Esta es una de las principales razones por las que Vim es una locura.
- Los atajos básicos de Vim (combinaciones de teclas) para que seas eficiente lo más rápido posible, con algunos consejos para recordarlos fácilmente.
- Cómo hablar el Idioma de Vim.
- Cuáles son las opciones de Vim y cómo manipularlas.

Después de esto, vas a hablar de Vim con experiencia y confianza, aunque sea para decir: “¡naaaah, Vim no es para mí!”.

El objetivo de este artículo no es reemplazar tu IDE por Vim de un día para otro. Recomendaría tomar un enfoque paso a paso.

Al principio, podés intentar usar Vim para editar alguna configuración u otros archivos de texto. Practicar lo que vas a aprender en este artículo es la clave para comprender realmente cómo funciona Vim y por qué es tan popular, incluso décadas después de su creación.

No creas que Vim es difícil de aprender. Es fácil aprender a editar cualquier archivo, pero es difícil de dominar. Los gurús de Vim, programando en el Himalaya durante cientos de años, ni siquiera pueden pretender saber todo sobre Vim. Eso es genial, porque significa que las posibilidades de este editor son infinitas.

¿Tenés dudas? Seguime. Sumerjámonos en el maravilloso mundo de Vim.

# Prerrequisitos: el poder está en tus dedos

Cuando decidí aprender Vim, quería hacerlo bien. Vim te permite olvidarte de tus manos y te permite concentrarte realmente en lo más importante: lo que estás escribiendo.

## El mouse: tu falso mejor amigo

Una de las ventajas de Vim es dejar tus manos sobre el teclado, sin la necesidad constante de agarrar el mouse.

Veo que tenés miedo: ¡tu mouse es como tu tercera mano! ¡Es tan útil y fácil! ¿Por qué no lo usarías?

Tu mouse es un poco como un implante que un médico te puso en el cuerpo a una edad muy temprana, diciéndole a tus padres que es el mejor dispositivo para hacer algo en una computadora. Te gusta porque es una costumbre, hace ya mucho tiempo.

Preguntate: ¿por qué, si el mouse es tan perfecto, tu IDE favorito tiene 341.324 _atajos de teclado_? ¿Quizás porque usar el teclado es más rápido? ¿Más fácil? ¿Más eficiente? ¿Más _cómodo_?

El mouse no es tu mejor amigo. Es solo un amigo. Con ese criterio, entonces el teclado es tu medio hermano. El poder proviene de él, y Vim es perfecto para que aproveches y liberes este poder.

Es por eso que creo profundamente que antes de aprender Vim, es necesario aprender técnicas básicas de escritura y mecanografía en el teclado. Los beneficios son enormes:

- Vas a escribir más rápido y con mayor precisión.
- Vas a poder aumentar tu velocidad y precisión con el tiempo.
- Ya no te vas a concentrar en tu teclado. Ni siquiera un poco.

Si ya usas estas técnicas, ¡genial! Podés pasar directamente al siguiente capítulo.

## Escritura eficiente: las dos reglas

Todos estamos de acuerdo en que para un desarrollador es más importante saber pensar que saber escribir. Dicho esto, sigue siendo agradable sentirse en control de tus herramientas. Como desarrollador, ¡el teclado es una de las más importantes!

Es muy gratificante ver cómo mejora tu escritura día tras día, mes tras mes, incluso año tras año. El espacio para mejorar es enorme, incluso si es bastante rápido y fácil aprender los conceptos básicos.

La primera regla que debes aprender es colocar las manos correctamente:

![](assets/vim-beginner-guide-keyboard.png)

Las teclas `a`,`s`,`d`,`f` y `j`,`k`,`l`,`ñ` se llaman _teclas de fila_. Son los puntos de partida para tus manos. A partir de ahí, podés apretar cualquier otra tecla fácilmente.

Vas a notar que hay pequeñas marcas en las teclas `f` y `j` de tu teclado: son indicadores para que sepas dónde poner tus dedos índices. Cuando estén en la posición correcta, simplemente apoyá los otros dedos en las otras teclas de fila.

La segunda regla que tenés que seguir: tratá de no mirar el teclado mientras escribís. Si no te acordás dónde está una tecla, primero intentá apretarla sin mirar, incluso si parece aleatorio.

Estuve escribiendo sólo con dos dedos durante años. Se sentía totalmente raro tratar de seguir estas reglas al principio. Ahora, no podría escribir de otra manera, principalmente porque es más cómodo.

Me tomó solo una o dos semanas aprender esta nueva forma de escribir. No es porque sea un genio (definitivamente no), sino porque es fácil.

### La primera semana

Cuando decidas usar las dos reglas que describí anteriormente, tenés que tratar de seguirlas _todo el tiempo_. Es necesario un compromiso del 100%. Cuando te sorprendas usando tus viejas (y malas) técnicas nuevamente, tené paciencia, no lo veas como un fracaso y volvé a las buenas. Esta es la parte obligatoria del proceso de aprendizaje.

Los tres primeros días son los más difíciles. Vas a alternar entre buena y mala técnica sin siquiera darte cuenta. Van a haber errores y va a ser lento.

Afortunadamente, al final de la semana, la cantidad de errores va a disminuir y vas a tener cada vez menos necesidad de mirar las teclas.

### La segunda semana

Vas a notar que durante la segunda semana la cantidad de errores va a disminuir aún más, y tu necesidad de mirar al teclado va a desaparecer.

Al final de la semana, vas a ver que tu velocidad de escritura ya está mejorando. Los sentimientos de recompensa van a empezar a complacer a tu cerebro.

### Velocidad y precisión

Durante tus dos semanas de entrenamiento inicial, no te tenés que concentrar en la velocidad o la precisión. Solamente escribí, tanto como puedas, y no te preocupes por nada más todavía, ni siquiera por los errores que cometas.

Después de eso, podés empezar a concentrarte en la velocidad y la precisión: qué tan rápido podés escribir tratando de cometer la menor cantidad de errores posible.

Para entrenar estas buenas técnicas de mecanografía, desde el comienzo de tu experiencia de aprendizaje hasta el final de tu vida, podés usar un software de mecanografía que puede ayudar drásticamente.

Acá hay una lista de mis favoritos:

- [Ratatype](https://www.ratatype.es/typing-test/)
- [Keyhero](https://www.keyhero.com/prueba-mecanografia/test-gratuito/)
- [Type Racer](https://play.typeracer.com/?universe=lang_es)

# Vim o Neovim?

![](assets/vim-beginner-guide-hate.webp)

Con los temas fundamentales fuera del camino, instalemos Neovim.

¿Neovim? ¿Qué es esta nueva cosa rara, podrías preguntar, y con razón?

Neovim es una [refactorización](https://es.wikipedia.org/wiki/Refactorizaci%C3%B3n) de Vim. Es compatible con todo lo que vamos a ver de Vim. Definitivamente recomendaría usarlo, en lugar del Vim normal, ya que está optimizado de fábrica.

Acá están los enlaces oficiales para ambos programas:

- [Neovim](https://neovim.io/)
- [Vim](https://www.vim.org/)

Debido a que Neovim y Vim son _casi_ idénticos (con una filosofía diferente), continuaré llamando a estos dos programas usando el término genérico _Vim_ en este artículo.

# Configuración de Vim

En Vim, casi todo es configurable. Es una locura, en serio. Podés customizar tu editor de acuerdo con tus necesidades específicas y deseos megalómanos.

Dependiendo de si instalaste Vim o Neovim, el archivo de configuración debería estar en la siguiente ruta por defecto:

- Para Vim: `~/.vimrc`.
- Para Neovim: `~/.config/nvim/init.vim` o `~/nvim/init.vim` (dependiendo del valor de la variable de entorno `$XDG_CONFIG_HOME`).

Este archivo de configuración se llama _vimrc_.

Vamos a abrir vimrc con tu editor favorito (¡que pronto podría ser reemplazado por Vim!) y agreguemos algunas cosas básicas. Voy a explicar más adelante el propósito de cada una:

```
noremap <Up> <Nop>
noremap <Down> <Nop>
noremap <Left> <Nop>
noremap <Right> <Nop>
```

y también

```
set clipboard+=unnamedplus
```

El contenido de vimrc y los diferentes complementos para Vim a menudo están escritos en Vimscript, un lenguaje de programación creado específicamente para el editor. Sin embargo, no te recomendaría que aprendas este lenguaje, excepto los conceptos básicos para configurar Vim. Es bastante doloroso de usar. Es por eso que Neovim quiere reemplazarlo con [Lua](https://es.wikipedia.org/wiki/Lua), lo cual es una muy buena idea.

Ahora, iniciemos Vim y, sin tratar de hacer nada más, veamos los conceptos básicos que se necesitan para empezar.

# Los modos de Vim

![](assets/vim-beginner-guide-modes.webp)

> ---
>
> **Aclaración**
>
> Por defecto, siempre que veas una referencia a una tecla o a un atajo, como por ejemplo: `i`, `CTRL+r`, corresponde a una pulsación de la tecla **en minúscula**. En el caso de que la letra que haya que apretar sea en mayúscula, se va a aclarar al lado de la combinación (los atajos de Vim cambian entre letras mayúsculas y minúsculas).
>
> ---

Después de iniciar Vim, vas a ver una pantalla de bienvenida que muestra los comandos básicos que se pueden usar. Esta pantalla va a desaparecer ni bien empieces a escribir contenido.

Vim no es como tu editor común donde simplemente podés escribir en tu teclado y el contenido aparece mágicamente en la pantalla. Intentá escribir `x`, por ejemplo: parece que no pasara nada.

Esto se debe a que Vim tiene _modos_, y podés hacer diferentes cosas según el modo en el que te encuentres. Para identificar fácilmente los diferentes modos de los que hablo en este artículo, siempre los voy a escribir en mayúsculas (por ejemplo, modo NORMAL).

## Modo normal

Normalmente, cuando abrís un editor, podés escribir directamente contenido. En Vim no. Su modo predeterminado es el modo NORMAL, donde podés _editar_ contenido existente.

Podés usar teclas para moverte a donde quieras y editar lo que quieras: insertar, cambiar o eliminar palabras, oraciones o incluso párrafos. ¡Sin usar el mouse ni una vez!

Pensalo como un sistema de accesos directos que permite apuntar exactamente a lo que querés editar. La diferencia entre tu editor predeterminado con interfaz gráfica y Vim cuando hablamos de accesos directos (o combinaciones de teclas) es significativa: tienen sentido en Vim, la mayor parte del tiempo. Siguen una cierta lógica y son _combinables_. Es por esto que Vim es fácil de aprender.

Por ejemplo, el atajo `CTRL+shift+n` para encontrar un archivo en tu editor con interfaz gráfica favorito es difícil de recordar porque es difícil vincular lo que sabés (abrir un archivo) y lo que querés aprender (la combinación de teclas).

Volveremos al modo NORMAL más tarde, cuando aprendamos las combinaciones de teclas principales de Vim.

## Modo insertar

Mirá tu cursor en Vim: normalmente debería ser un cuadrado. Ahora, presionemos nuestro primer atajo en modo NORMAL: `i`, para `i`nsertar.

¿Qué es esta magia oscura? ¡Tu cursor se convirtió en un palito! ¡En la esquina inferior izquierda, apareció el indicador `--INSERT--`! ¡Qué impresionante! ¡Qué maravilloso! ¿Crees que estoy exagerando? ¡Sí!

Bienvenido al modo INSERTAR.

Finalmente podés escribir tu contenido en este modo: dale, escribí lo que quieras. Para volver al modo NORMAL y dejar de insertar, simplemente apretá `ESC` o `CTRL-c`. El cursor vuelve a convertirse en un cuadrado y el indicador `--INSERT--` desaparece. No te pongas triste, ya va a volver.

Así es como se trabaja con Vim: haciendo malabarismo entre el modo NORMAL para editar contenido _existente_ y el modo INSERTAR para insertar contenido _nuevo_.

## Modo visual

Hay un tercer modo importante en Vim que vas a usar con frecuencia: el modo VISUAL. ¿Su objetivo? Seleccionar contenido. Desde ahí, se puede modificar, editar o copiar la selección.

Para ingresar al modo VISUAL, es posible que ya lo hayas adivinado, hay que escribir `v` en el modo NORMAL. Vas a ver el indicador `--VISUAL--` que aparece en la esquina inferior izquierda de tu instancia de Vim. Nuevamente, para volver a nuestro modo predeterminado, el modo NORMAL, apretá `ESC` o `CTRL-c`.

También podés seleccionar líneas completas si iniciás el modo visual por líneas con la combinación de teclas `SHIFT+v`. Eso no es todo: se puede iniciar el modo visual en bloque, usando la combinación de teclas `CTRL+v`. Es bastante útil cuando tenés que lidiar con tablas o listas, por ejemplo.

## Modo de línea de comandos

El modo LÍNEA DE COMANDOS se puede comparar con el menú de una interfaz gráfica. Un menú extenso y poderoso.

Si escribís `:` en modo NORMAL, tu cursor se va a mover automáticamente a la parte inferior de Vim. Desde ahí, podés escribir cualquier comando que desees. Estos comandos también se denominan _comandos Ex_.

Estos son los más básicos:

- `:help` para abrir la ayuda de Vim. Posiblemente el comando más útil. Esta ayuda es muy completa. Si [no te acordás cómo salir de Vim](https://tienda.sysarmy.com/productos/wq/), por ejemplo, podés escribir: `:help quit`.
- `:q` para salir (de `q`uit en inglés) de la ventana actual. Si solo hay una ventana (es la opción predeterminada), por fin vas a salir Vim.
- `:q!` salir sin guardar. ¡Es como gritarle a tu editor que querés salir, sean cuales sean las consecuencias!
- `:w` para guardar (de `w`rite en inglés), guarda el archivo actual abierto.
- Incluso se puede combinar algún comando ex: `:wq` para guardar y salir. O simplemente en este caso podés usar `:x`.
- `:e <ruta>` para editar un archivo. La ruta puede ser absoluta o relativa.

Ahora que sabés cómo acceder a la ayuda de Vim, voy a empezar a dejar al final de cada sección los comandos de ayuda que podés usar para profundizar. Por ejemplo, estos son los de esta sección:

> **Ayuda en Vim**
>
> - `:help helphelp` (Ayuda para las páginas de ayuda)
> - `:help vim-modes` (Modos de vim)
> - `:help insert.txt` (Modo insertar)
> - `:help visual.txt` (Modo visual)
> - `:help cmdline.txt` (Modo línea de comandos)
> - `:help write-quit` (Guardar y salir de Vim)
> - `:help ex-cmd-index` (Índice de comandos Ex)

No te preocupes si no entendés lo que está escrito en la ayuda o si es demasiado abrumador. Teneme paciencia en este artículo, y más tarde, cuando tengas más comodidad con Vim, podés volver a esta ayuda encantadora.

# Atajos generales de Vim

Ahora que entendemos el concepto general de Vim y sus modos, veamos los atajos más importantes en el modo NORMAL que hay que tener en cuenta. Te invito a probarlos en Vim mientras lees.

## Escribí tu propio [machete](https://es.wikipedia.org/wiki/Apunte_escondido)

Podés encontrar miles de machetes (cheatsheets) en Internet que te van a mostrar tantos atajos de teclado como quieras. Cuando yo estaba aprendiendo a usar Vim, usaba uno.

Pero al mismo tiempo, iba escribiendo _mi propio machete_.

¿Por qué? Personalmente, me ayudó mucho a memorizar las teclas que tenía que apretar. Escribir es una forma poderosa de apropiar la información.

Organizá tu machete como quieras, y usa lo que quieras (papel, evernote, mindmaps…). Para el mío, estoy usando [Joplin](https://joplinapp.org/), un sistema de toma de notas gratuito y de código abierto.

¡Puntos extra si escribís tu machete... en Vim!

El resto del artículo te va a mostrar los atajos básicos necesarios al principio. Tené en cuenta que Vim está lleno de sutilezas que le otorgan poder y eficiencia, según el contexto. ¡Es un proceso de aprendizaje interminable que hace que este editor sea tan interesante, tan divertido de usar y tan gratificante!

## Búsqueda

Escribí un [artículo completo sobre la búsqueda en Vim](https://thevaluable.dev/vim-search-find-replace/) (en inglés), pero, por ahora, la tecla `/` debería ser suficiente. Al presionarla, el cursor se va a mover a la parte inferior de la pantalla. Desde ahí, escribí tu búsqueda y presioná `ENTER`.

Podés ir a la siguiente ocurrencia encontrada escribiendo `n`. Para ir a la anterior, usá `N` (mayúscula).

También podés usar estas dos teclas en modo NORMAL para buscar la palabra seleccionada bajo el cursor:

- `*` - Buscar hacia adelante.
- `#` - Buscar hacia atrás.

## Deshacer y rehacer

¿Qué haríamos sin los esenciales deshacer y rehacer?

- `u` deshace tu última edición.
- `CTRL-r` rehace. Podés pensarlo como que estás en control (`CTRL`) de tu contenido.

## Modo insertar

Vimos anteriormente que una sola tecla transportó tu alma al mundo tranquilizador del modo INSERTAR.

Hay otros atajos de teclado útiles para hacerlo, que introducen algunas sutilezas:

- `i` - inserta contenido antes del carácter actual.
- `a` - inserta contenido después del carácter actual (de `a`fter en inglés).
- `A` (mayúscula) - inserta contenido después de todo. Mueve el cursor hasta el final de la línea e ingresará al modo INSERTAR.
- `o` - crea una nueva línea, debajo de la actual, y permite insertar contenido (de `o`pen en inglés).
- `O` (mayúscula) - crea una nueva línea encima de la actual.
- `esc` o `CTRL-c` o `CTRL-[`: regresa al modo NORMAL si estás en el modo INSERTAR.

> **Ayuda en Vim**
>
> - `:help search-commands` (Patrones de búsqueda)
> - `:help undo-redo` (Ayuda para comandos Deshacer y Rehacer)

# Movimientos de Vim

Los movimientos en Vim permiten mover el cursor horizontalmente (en una línea) o verticalmente.

Tené en cuenta que se puede combinar movimientos con un número: si querés hacer un movimiento 6 veces, por ejemplo, podés hacer `6<movimiento>`. Reemplazá `<movimiento>` con el movimiento que quieras.

Podés usar movimientos en modo NORMAL y modo VISUAL.

## Olvidate de las flechas

Para ser completamente honesto, esta fue la parte más difícil para mí: no usar las flechas para mover el cursor.

Como dije en la primera parte del artículo, tus dedos tienen que estar en las _teclas de fila_. Primero, para que mejore tu mecanografía, y segundo porque las teclas de Vim que se pueden usar en modo NORMAL están alrededor de las teclas de fila. Tus manos no deberían moverse demasiado; solo tus dedos deberían hacerlo.

Ahora, intentá apretar las flechas desde las teclas de fila: ¡sí, es necesario mover la mano! Esto definitivamente no es lo que queremos.

Por eso, en lugar de usar las flechas, debemos usar las teclas `h`, `j`, `k` y `l` para movernos respectivamente hacia la izquierda, hacia abajo, hacia arriba y hacia la derecha.

Es difícil al principio: vas a intentar usar las flechas para mover el cursor, y más de una vez. ¡Es por eso que previamente las deshabilitamos en la configuración!

¿Cómo recordar qué significan `h`, `j`, `k` y `l`?

- `h` mueve el cursor hacia la izquierda y `l` lo mueve hacia la derecha. Tiene sentido, ya que `h` está a la izquierda de la secuencia `hjkl` y `l` está a la derecha.
- `j` mueve el cursor hacia abajo. Podés recordarlo ya que `j` parece una flecha que apunta hacia abajo (con un poco de imaginación). Otro método mnemotécnico: la tecla `j` tiene una pequeña marca en la parte inferior de la tecla, lo que significa que el cursor va a bajar.
- `k` es la única letra que queda, por lo que tiene que subir. ¡Siempre me imagino a una Tortuga Ninja _saltando para arriba_ y diciendo “Kowabunga”! Ni siquiera está bien escrito (sería “Cowabunga”) pero me funciona. No me juzgues, porfa.

Veo tu mente llena de preguntas. ¡No temas, padawan! Te voy a ayudar, con un [revolucionario juego AAA del que todo el mundo hablará dentro de veinte años](https://themouseless.dev/snake/). Para jugarlo, hay que usar usar `hjkl`.

Si preferís los rompecabezas, probá este maravilloso [sokoban](https://themouseless.dev/sokoban/). Esta vez se puede usar `hjkl` o las flechas, pero intentá usar solo `hjkl`.

## Moverse horizontalmente

Acá hay algunos atajos de teclado básicos para moverse rápidamente en una línea en modo NORMAL:

- `w` - avanzar a la siguiente palabra. Una palabra, por defecto, es una secuencia que contiene letras, dígitos o guiones bajos.
- `b` - mueve el cursor hacia la palabra anterior.
- `0` - mueve el cursor al principio de la línea actual.
- `ˆ` - mueve el cursor al primer carácter que no esté en blanco en la línea actual.
- `$` - mueve el cursor al final de la línea actual.
- `%` - mueve el cursor al corchete correspondiente cuando el cursor esté parado en un corchete.

También podés moverte a un carácter específico de la línea usando:

- `f` + `<carácter>` - encuentra el carácter después del cursor.
- `F` (mayúscula) + `<carácter>` - encuentra el carácter antes del cursor.
- `t` + `<carácter>` - se mueve a un carácter después del cursor.
- `T` (mayúscula) + `<carácter>` - se mueve a un carácter antes del cursor.

Después de usar una de las últimas cuatro combinaciones de teclas, podés moverte en el carácter elegido con `;` para ir hacia adelante, y `,` para ir hacia atrás. ¡Una forma muy poderosa de moverse horizontalmente!

## Moverse verticalmente

Podés moverte verticalmente simplemente buscando la palabra a la que querés saltar (ver arriba para aprender cómo buscar). También hay otras formas de moverse verticalmente:

- `<nro_de_línea>` + `G` (mayúscula) - mueve el cursor al principio de la línea elegida. Por ejemplo, `10G` mueve el cursor a la línea 10.
- `G` (mayúscula) - mueve el cursor a la última línea del archivo.
- `1G` (mayúscula) o `gg` - mueve el cursor a la primera línea del archivo.

También se pueden usar diferentes atajos para desplazarse. Estos son los más básicos:

- `CTRL-e` - desplaza la ventana hacia abajo.
- `CTRL-u` - mueve el cursor hacia arriba media pantalla.
- `CTRL-d` - mueve el cursor hacia abajo media pantalla.

> **Ayuda en Vim**
>
> - `:help cursor-motions` (Movimientos del cursor)
> - `:help left-right-motions` (Movimientos horizontales)
> - `:help up-down-motions` (Movimientos verticales)
> - `:help scrolling` (Scrollear el documento)

# El idioma de Vim

![](assets/vim-beginner-guide-language.webp)

En Vim, los atajos de teclado se pueden pensar como "frases", que describen una acción. Eso es lo que quise decir cuando dije que los atajos son _combinables_. Ya sé, suena raro, pero es genial.

Estas "frases" son tan comunes que vas a asociar fácilmente lo que ya sabes (la oración) con lo que necesitas aprender (los atajos de teclado).

Mejor aún: saber que Vim tiene un "lenguaje de atajos de teclado" te va llevar a combinarlos instintivamente para hacer lo que necesitás hacer y, en muchos casos, ¡va funcionar!

## Operadores

Los operadores son los verbos del idioma de Vim. Necesitan combinarse con movimientos u objetos de texto para que funcionen. Estos son algunos operadores importantes:

- `d` para borrar (de `d`elete en inglés)
- `c` para cambiar (de `c`hange en inglés)
- `y` para copiar (de `y`ank en inglés)

Cuando se usa el operador `y`, se puede pegar lo que se haya copiado usando la tecla `p` o `p` (mayúscula).

Se pueden combinar operadores y movimientos de la siguiente manera:

- `d$` - elimina desde el cursor hasta el final de la línea. También se puede utilizar el alias `D` (mayúscula).
- `dgg` - elimina todo, desde el cursor hasta el principio del archivo.
- **ggdG** - ¡borra todo en el archivo!

## Objetos de texto

Si los operadores son los verbos, los objetos de texto son los sustantivos. En pocas palabras, un objeto de texto es un conjunto de caracteres. En Vim, una `palabra` es un objeto de texto, así como una `oración` o un `párrafo`.

Por ejemplo, se pueden usar operadores y objetos de texto de la siguiente manera:

- `diw` - elimina la palabra actual debajo del cursor (de `d`elete `i`nside the `w`ord en inglés).
- `ciw` - elimina la palabra actual debajo del cursor y cambia al modo INSERTAR. En resumen, ¡cambia la palabra! (de `c`hange `i`nside the `w`ord en inglés).
- `dip` - elimina el párrafo (de `d`elete `i`nside the `p`aragraph en inglés).

Podés intentar _cambiar una palabra_ o _eliminar una palabra_, también funciona e introduce algunas sutilezas. ¡Te dejo encontrar cuáles podrían ser los atajos de teclado para hacerlo!

> **Ayuda en Vim**
>
> - `:help operator` (Ayuda sobre operadores)
> - `:help text-objects` (Ayuda sobre objetos de texto)

# Opciones de Vim

Se puede modificar el comportamiento de Vim modificando las opciones.

Podés pensar en una opción como una variable. Puede ser un valor booleano (que se puede activar y desactivar), una cadena de caracteres o un número. Se pueden visualizar o modificar los valores utilizando el modo LÍNEA DE COMANDOS.

Si lo que querés es modificar permanentemente alguna opción, se pueden asignar los nuevos valores directamente en tu vimrc, como hicimos con la opción `clipboard` al principio de este artículo.

Estos son los comandos que se pueden utilizar:

- `:set no<opción>` - desactiva la opción.
- `:set <opción>!` - activa la opción.
- `:set <opción>?` - muestra el valor de la opción.
- `:set <opción>=<valor>` - establece el valor `<valor>` (cadena de caracteres o número).
- `:set <opción>+=<valor>` - agrega el valor `<valor>` a la opción ya establecida.
- `:set <opción>-=<valor>` - elimina el valor `<valor>` de las opciones ya establecidas.
- `:set <opción>&` - restablece la opción a su valor predeterminado.

Por ejemplo, si querés mostrar el tipo de archivo del archivo que se encuentra abierto, podés ejecutar:

    :set filetype?

Sacale el prefijo `:` si querés agregar estas opciones en tu vimrc.

> **Ayuda en Vim**
>
> - `:help options` (Ayuda sobre las opciones)
> - `:help option-list` (Listado de opciones)

# El comienzo del viaje de Vim

¡Felicidades! Te iniciaste en el oscuro entendimiento de Vim. Resumamos lo que aprendimos en este artículo:

- Tener técnicas de escritura y mecanografía adecuadas va a hacer el proceso más rápido, más preciso y te va a permitir concentrarte únicamente en el contenido que tengas que escribir, no en el teclado o en tus manos. También te vas a sentir más en control (una buena manera de [reducir el estrés](https://sysarmy.com/blog/posts/encuesta-de-burnout/)).
- Escribí tu propio machete a medida que aprendas nuevas combinaciones de teclas e intentá encontrar tus propios mnemotécnicos para retenerlas. Va a acelerar tu proceso de aprendizaje. Para recordar fácilmente, tratá de asociar lo que ya sabes con lo que querés aprender.
- Podés usar una combinación de operadores, movimientos y objetos de texto para editar tu texto en modo NORMAL.
- ¡Necesitás usar las teclas de fila `h`, `j`, `k` y `l` para navegar en Vim, para apreciar realmente su comodidad, su potencia y su diversión!
- Probá por tu cuenta las combinaciones de teclas explicadas en este artículo, para que las memorices usando memoria muscular.
- Las opciones de Vim se pueden activar, desactivar, alternar o desactivar (para valores booleanos). También se pueden modificar los valores (para cadenas de caracteres y números). Siempre es interesante mostrar los valores para asegurarse de que Vim se comporte como se espera.

Incluso si todavía no te gusta usar Vim, al menos lo intentaste. Vas a poder usarlo cuando te pierdas en un servidor remoto lejano y, lo más importante, ¡ahora podés afirmar, legítimamente, que no te gusta Vim!

¿Qué sigue en este viaje de aprendizaje de Vim?

- Podés leer la segunda parte de esta serie de artículos, [Vim for intermediate users](https://thevaluable.dev/vim-intermediate/) (en inglés).
- Deberías probar `vimtutor`. Si usás Neovim, solamente tenés que ejecutar el comando ex `:Tuto`. Si usas Vim, escribí el comando `vimtutor` en tu terminal.
- Si sabés inglés, te recomiendo leer el libro _Practical Vim_, de Drew Neil. Vas a aprender un montón.
- Vim es un juego: el objetivo es usar la menor cantidad posible de combinaciones de teclas para lograr lo que querés hacer. Con ese espíritu, [Vim Golf](https://www.vimgolf.com/) (en inglés) puede ser muy divertido.

Si no te convertiste en un _Vim Hater_, ahora estás en el camino para convertirte en un _Vim Master_.

- La versión original de este post se puede encontrar en [The Valuable Dev](https://thevaluable.dev/vim-commands-beginner/) (inglés).
- Traducción por [@nachichuri](https://twitter.com/Nachichuri), revisión por [@jedux](https://twitter.com/jedux).
