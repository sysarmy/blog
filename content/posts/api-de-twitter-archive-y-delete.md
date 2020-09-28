---
Description: "Probando la API de Twitter: tweet archive y delete"
Keywords:
- sysadmin 
- twitter
- api
- python
Section: 
Tags:
- sysadmin 
- twitter
- api
- python
Thumbnail: https://miro.medium.com/max/1400/1*Y5r4YuCqCLqIWlCy_ccPqQ.jpeg
socialImage: https://miro.medium.com/max/1400/1*Y5r4YuCqCLqIWlCy_ccPqQ.jpeg
featuredImage: https://miro.medium.com/max/1400/1*Y5r4YuCqCLqIWlCy_ccPqQ.jpeg
Title: "Probando la API de Twitter: tweet archive y delete"
Topics:
- sysadmin 
- sistemas
- consejos
- kubernetes
- argo
- continous
markup: markdown
date: 2020-09-28
draft: false

---

Hace mucho tiempo que no me ponía a hacer algo con la API de Twitter, y se que hubo muchos cambios en los últimos meses / años en cuanto a funcionalidades, permisos y limitaciones.

Para este caso en particular necesitaba hacer un cleanup masivo de algunas cuentas de Twitter con decenas de miles de tweets. He aquí algunas cuestiones interesantes, y lecciones aprendidas por pasos para principiantes.

<!--more-->

# Paso 1: Cuenta Dev de Twitter, permisos y autenticación

Más allá de los pasos para crear la cuenta de Developer de Twitter (y todas las justificaciones necesarias), quiero recalcar un par de tips y problemas que tuve que les pueden llegar a pasar:

1. Luego de enviar su request para una cuenta de developer les puede llegar a pasar, como a mí, que en unas pocas horas o días ya van a poder crear su app en el dashboard de Twitter.

![](https://miro.medium.com/max/1400/1*Y5r4YuCqCLqIWlCy_ccPqQ.jpeg)
*Vista principal del dashboard de Twitter Dev*

Cuidado, esto es verídico, y por más que creé la app no me funcionaba por problemas de autenticación de tokens (por más que hagan todo bien). Recién un mes después de que me llegó este mail de confirmación pude hacer andar todo. **Clave:** asegurarse de tener la confirmación por mail de Twitter antes de probar porque **no van a poder autenticar**.

![](https://miro.medium.com/max/1400/1*JytexSnThIcgvwjzSUWQ7w.jpeg)

*Ejemplo de mail de confirmación*

2. Una vez creada la app, asegúrense de:

  - crear un dev environment, agregar la app, y agregar el dev environment a las funcionalidades de la app:
  ![](https://miro.medium.com/max/1400/1*YL4be7SqpYL7t_jXNOFmfA.jpeg)
  - darle los permisos:
  ![](https://miro.medium.com/max/1400/1*7Oj-OPc4a3oCgISwi7WkSg.jpeg)
  - generar y copiar los tokens:
  ![](https://miro.medium.com/max/1400/1*tL8LxVcFxsnjQ1JlPDlzrA.jpeg)
  - suscribir su app a los Labs de Twitter.

Yo porque soy medio bruto le doy todos los permisos a mi app (por las dudas) pero haciendo esto no tendrían que tener ningun problema. En caso de necesitar troubleshooting de autenticación para los tokens vayan a [este link](https://developer.twitter.com/en/docs/labs/tweets-and-users/quick-start/get-tweets).

# Paso 2: Script para borrar TODOS los tuits de una cuenta

Lamentablemente no hay forma fácil de borrar masivamente tus tuits, y de las herramientas que hay online, una o dos son confiables, pero tenés que pagar. Lo intenté! Pero oh!, el pago es con tarjeta de crédito a través de PayPal, que está bloqueado en el país.

Lo que hice con este script está basado 90% [en este código](https://github.com/ngeor/delete-old-tweets) en Python que encontré en GitHub. Está muy bueno y anda perfecto, gran aporte.

*Requerimientos: Python, librería [Tweepy](https://www.tweepy.org/) 3.7.0*

1. La autenticación se hace en las primeras líneas sólo con sus Tokens. Es lo único que se usa y no hace falta agregar nada más.

![](https://miro.medium.com/max/1214/1*yT_gKrhbYt-E35XmKMrUvA.png)

2. Lo único que tienen que hacer es cambiar el max_id con el ID de el tuit que quieren poner como límite y lo que hace el script es borrar todos los tuits empezando por el más viejo. Fácil y simple.

3. Está limitado a 200 API calls por una cuestión obvia. Borra bastante rápido, a un ritmo de medio segundo por tweet, y no te jode con ninguna limitación o threshold de la cuenta de dev.
Ahora... si están buscando borrar tweets de hasta hace un año, no van a tener problemas. El inconveniente es que cuando hacen el get de los tweets, la API te va a limitar el get tweets hasta un año, siempre. Lamentablemente esta es una limitación a la que no le pudimos encontrar la vuelta.

# Paso 3: Tweet Archive y lista de IDs de Tweets

La API nos puede limitar, pero una de las cosas que podemos hacer es — desde los settings de la cuenta — bajar un archive completo de toda tu data de Twitter. Esto te baja absolutamente todo: fotos, actividad, etc. Depende de actividad de la cuenta puede pesar hasta mas de 2 GB:

![](https://miro.medium.com/max/1400/1*yzuRuTcX9xhXoQH4rcExtw.png)

1. Una vez bajado el archivo, ir a la carpeta data y editar el archivo tweet.js (va a ser el más pesado de todos). Es un json que se ve así:

![](https://miro.medium.com/max/1400/1*Nqkw_1O5MH2rAa1y_rPp-g.png)

Va a tener posiblemente miles de lineas y no está ordenado cronológicamente (no pregunten por qué).

2. Ahora lo que tenemos que hacer es traernos los IDs de los tweets. Si tienen alguna herramienta para parsear json, bárbaro. Sino lo que pueden hacer es una búsqueda con regex usando notepad++ del campo “id_str”. Este [cheatsheet](https://www.launch2success.com/guide/advanced-find-and-replace-in-notepad/) está bastante simplificado para lo que necesitamos. Una búsqueda así sirve ( **¡cuidado!** algunos IDs tienen 18 dígitos, y otros 19)

![](https://miro.medium.com/max/1142/1*F3ambA2C_g0A4b7gIjwYuw.png)

Muchos IDs les van a aparecer duplicados, pero lo bueno es que los IDs sí están ordenados numéricamente: ID más bajo es el tweet más viejo y ID más alto es el tweet más nuevo. Removemos duplicados y ordenamos hasta tener una lista en un txt así:

![](https://miro.medium.com/max/744/1*-f816Y4PcizjYjPTeLD4xg.png)

3. Una vez que tienen el txt listo: ponen el path en el código (línea 100) y va a buscar los IDs y los va a borrar. Si el ID es viejo de un tuit que ya borraron o no existe, lo omite.
En max_id hay que poner el límite del último tweet que quieren borrar.

![](https://miro.medium.com/max/1400/1*BBuNwURXWEhS-oSWkeu9gg.png)

Y listo! Si alguien quiere mejorarlo, adelante :) [Acá está el código listo para usar](https://github.com/sysarmy/disneyland/blob/master/misc/api-de-twitter-archive-and-delete/deleteTxt.py)

*Créditos a Pablo Pietro, [Edu](https://twitter.com/jedux) y [Godlike](https://twitter.com/godlike64) que me dieron una mano pensando e investigando*

#### Autor

[Mariano Aragunde](https://medium.com/@aragunde) Periodista, comunicador, IBMer, ultramaratonista, triatleta, músico, hincha de Racing, del Oeste (con eso creo que alcanza). Mis opiniones son personales
