---
Description: "Comandos Básicos con Docker - 2da Parte"
Keywords:
- containers 
- docker
- dockerhub
- linux
Section: 
Tags:
- sysarmy
- docker
- containers
- sistemas
Thumbnail: assets/docker-thumbnail.png
socialImage: assets/docker-thumbnail.png
featuredImage: assets/docker-thumbnail.png
Title: Comandos Básicos con Docker - 2da Parte
Topics:
- sysarmy
- docker
- containers
- linux
markup: markdown
date: 2020-07-02
---

Además de crear, ejecutar, detener y eliminar contenedores como explicamos en [nuestro post previo](posts/docker-comandos-basicos-primera-parte) hay muchas más operaciones que podemos realizar. Entre ellas se destacan el ver la configuración, darle almacenamiento persistente, e inspeccionar sus logs. En este artículo veremos ejemplos de cada una de estas acciones. Para poder ilustrarlas mejor, crearemos un nuevo contenedor con opciones adicionales.

## Comandos de administración

La salida de `docker help` devuelve dos secciones claramente separadas: **Management Commands** (agrupados por categoría) y la más genérica **Commands** (a secas). Ambos conjuntos nos permiten interactuar con Docker pero hasta este momento hemos utilizado los últimos exclusivamente. Sin embargo, es recomendable acostumbrarnos a utilizar los primeros por una cuestión de consistencia. Veamos la razón.

En el artículo anterior aprendimos a mostrar la lista de imágenes y contenedores de la siguiente manera:

    docker images
    docker ps -a

Si bien el primer ejemplo nos da una idea que se refiere a imágenes, no es muy claro qué acción va a realizar. Por otra parte, el último no nos da ninguna pista sobre lo que hace. Sin embargo, al emplear los comandos de administración equivalentes obtenemos el mismo resultado de una forma más fácil de recordar:

    docker image ls
    docker container ls -a

Estos últimos consisten de `docker` seguido del tipo de recurso (`image`, `container`, etc) y de `ls` para mostrar la lista. De ahora en adelante, utilizaremos estos comandos siempre que sea posible.

## Crear un contenedor con opciones adicionales

Para comenzar, vamos a poner en práctica los comandos de administración empleando la imagen **nginx** para crear un nuevo contenedor. Al mismo tiempo, agregamos dos opciones que van a ser útiles para poder acceder a este. 

    docker container run --name=sysarmy-nginx --publish 8080:80 --detach --mount source=sysarmy-webapp,target=/usr/share/nginx/html nginx

donde:

- `--publish` permite vincular un puerto del host con uno del contenedor. En este caso, con `--publish 8080:80` se indica que el acceso al puerto 80 de **sysarmy-nginx** se realizará a partir del 8080 en el host. Al poder mapear puertos públicos a otros internos, podemos ejecutar múltiples instancias de nuestra aplicación (o apps distintas) en el mismo host.

- `--detach` hace que el contenedor se ejecute en segundo plano para poder continuar utilizando la terminal.

- `--mount=sysarmy-webapp,target=/usr/share/nginx/html` crea un volumen llamado **sysarmy-webapp** en el equipo host y lo monta en **/usr/share/nginx/html** en el contenedor. 

> El [uso de volúmenes](https://docs.docker.com/storage/volumes/) es el método recomendado para implementar almacenamiento persistente ya que es manejado enteramente por Docker. No depende de la estructura de directorios del host.

Dicho de otra manera, el contenedor que acabamos de crear servirá el contenido del volumen **sysarmy-webapp**. Para saber dónde reside ese volumen con el fin de agregar archivos al mismo, podemos usar el comando cuya salida vemos en la imagen siguiente:

    docker volume inspect sysarmy-webapp

que indica claramente la acción que nos proponemos llevar a cabo.

![Inspeccionar volumen utilizado en el contenedor](assets/docker-volume-inspect-1.png)

Ahora que sabemos que el volumen está ubicado en **/var/lib/docker/volumes/sysarmy-webapp/_data**, vamos a insertar contenido en el mismo para que el contenedor lo muestre.

## Agregar archivos en el volumen

Como primer paso, añadamos un archivo **index.html** y una copia de la [licencia Apache 2.0](https://github.com/moby/moby/blob/master/LICENSE) al volumen:

![Agregar archivos a un volumen](assets/docker-agregar-archivos-volumen-1.png)

Como ejemplo, usamos el siguiente **index.html** básico:

```html
<body>
    <h1 style="color: green">Mi contenedor de nginx</h1>
    <p>Descargar una copia de la <a href="apache-2.0-license.txt" target="_blank">licencia Apache 2.0</a></p>
</body>
```

Si ahora abrimos un navegador web y apuntamos a la dirección IP o nombre del host, deberíamos ver la página servida por el contenedor **sysarmy-nginx**:

![Comprobar que el contenedor funciona correctamente](assets/docker-nginx-servir-archivos-1.png)

También podemos ver los logs del contenedor (la opción `-f` nos permite ver la actividad del log en tiempo real):

    docker container logs sysarmy-nginx -f

![Inspeccionar los logs del contenedor](assets/docker-container-logs.png)

En la imagen de arriba podemos ver que aparte de nosotros, alguien desde la IP 116.197.128.47 accedió a la raíz del sitio utilizando una versión muy antigua de Google Chrome (¡o quizás también falsearon ese dato, como probablemente lo hicieron con la dirección!). Para quedarnos tranquilos, podemos detener **sysarmy-nginx** por el momento con:

    docker container stop sysarmy-nginx

ya que no lo necesitaremos funcionando para la próxima sección.

## Ver la configuración del contenedor

El comando `docker container inspect`, seguido del nombre del contenedor, nos devuelve información muy detallada sobre el mismo en formato JSON. Para poder consumirla más cómodamente, podemos recurrir a la opción `--format` e indicar qué sección particular nos interesa. Por ejemplo:

    docker container inspect --format='{{json .State}}' sysarmy-nginx 
    docker container inspect --format='{{json .Mounts}}' sysarmy-nginx

Aunque la salida de los comandos anteriores no está formateada como acostumbramos ver un archivo **.json**, es más compacta que el resultado de ejecutar `docker container inspect` sobre el contenedor. Depende de nosotros cuál alternativa usaremos en un momento dado.

## Conclusión

En este artículo aprendimos a utilizar los comandos de administración de Docker para realizar las tareas que ya conocíamos y otras nuevas. Si nos acostumbramos a emplearlos, nos resultará más fácil identificar qué es lo que cada uno hace con tan solamente mirarlos.
