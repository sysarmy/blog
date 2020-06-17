---
Description: "Comandos Básicos con Docker - 1era Parte"
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
Title: Comandos Básicos con Docker - 1era Parte
Topics:
- sysarmy
- docker
- containers
- linux
markup: markdown
date: 2020-04-14
---

Después de haber aprendido qué es Docker y qué soluciones brinda en [el post anterior](posts/que-es-docker), ahora es momento de comenzar a aprender los comandos necesarios para sacar provecho de esta tecnología. Asumimos el uso de sudo o de un grupo que tenga los permisos para ejecutar estos comandos (otorgados a través de **/etc/sudoers**).

Si bien en el artículo anterior vimos cómo descargar una imagen y ejecutar un contenedor basado en esta, eso es solamente el principio. En esta oportunidad explicaremos otras formas de crear, así como de ejecutar, detener y eliminar contenedores. 

## Más sobre la creación de contenedores

Recordemos que docker run, seguido del nombre de una imagen, creará y ejecutará un contenedor basado en esta. Si dicha imagen no existe en el equipo host, Docker primero la obtendrá desde el [Hub](https://hub.docker.com/), mientras que en sucesivas ocasiones la utilizará sin necesidad de descargarla nuevamente.

> Si no queremos despegarnos de la línea de comandos, también podemos buscar imágenes utilizando `docker search` seguido por un criterio de búsqueda.

Otra alternativa que tenemos es descargar la imagen primero, almacenarla localmente, y luego crear el contenedor cuando lo deseemos. En primer lugar, descarguemos la imagen oficial de Debian:

    docker pull debian

A este punto podemos ver la lista de imágenes y de contenedores disponibles en el sistema:

    docker images
    docker ps -a

donde la opción `-a` en el último comando hace posible que veamos aquellos que están en ejecución como los que no:

![Ver lista de imágenes y contenedores](assets/docker-imagenes-contenedores.png)

Como podemos apreciar arriba, entre las propiedades de imágenes y contenedores se pueden mencionar sus nombres (debajo de **REPOSITORY** y **NAMES**) y sus respectivos identificadores. Por defecto, Docker asigna un nombre aleatorio para los nuevos contenedores, pero se puede especificar otro distinto al momento de crearlos (como por ejemplo, **sysarmy_docker**):

    docker run --name=sysarmy_docker debian

Luego de ejecutar el comando anterior, pareciera que nada sucede. Pero si ahora volvemos a ejecutar `docker ps -a` vemos que el contenedor se creó, corrió el comando `bash` y finalizó:

![Ejecución de un contenedor basado en la imagen Debian](assets/docker-run-1.png)

> Un contenedor está en ejecución mientras lo hacen los procesos en su interior. Una vez que estos finalizan, también lo hace el contenedor.

Si eliminamos el contenedor (utilizando su nombre o ID) y luego volvemos a crearlo agregando la opción combinada `-it`, veremos algo diferente: el prompt cambia al del contenedor. En este caso, `-i` hace que se pueda acceder a STDIN incluso si el contenedor se está ejecutando en segundo plano y `-t` crea una pseudoterminal para ese propósito:

![Acceder a la línea de comandos del contenedor](assets/docker-run-2.png)

Para salir del contenedor, escribimos el comando `exit` y volveremos al prompt del equipo host. En ese momento, finalizará su ejecución. Eso nos lleva a la pregunta obvia: ¿cómo podemos lograr que un contenedor continúe corriendo cuando salimos del mismo o cuando cerramos la terminal desde la que lo iniciamos?

## Ejecutar contenedores existentes

Tomemos como ejemplo a **sysarmy_docker** para ilustrar cómo iniciar un contenedor existente que está detenido:

    docker start sysarmy_docker

Es importante notar que el comando de arriba iniciará **sysarmy_docker** con la misma configuración que cuando lo creamos pero en segundo plano. Para conectarnos a la pseudoterminal disponible, debemos hacer

    docker attach sysarmy_docker

Como se trata de una línea de comandos de Linux, podemos ejecutar comandos en la misma:

    cat /etc/hosts

De todas maneras, si lo que nos interesaba era ejecutar un comando sobre el contenedor, bien podríamos haber utilizado el comando `docker exec` sin necesidad de ingresar al prompt de **sysarmy_docker**. En la imagen siguiente observamos esta acción llevada a cabo de las dos formas que acabamos de explicar:

![Ejecutar comandos en un contenedor existente](assets/docker-ejecutar-comandos-en-contenedor.png)

Si empezamos a experimentar con las imágenes disponibles en Docker Hub (hasta que aprendamos a crear las propias), en algún momento vamos a querer comenzar a limpiar el entorno para no mantener contenedores o imágenes que no necesitamos más.

## Detener y eliminar contenedores e imágenes

En primer lugar, para eliminar un contenedor primero tenemos que asegurarnos de que esté detenido. En el siguiente ejemplo utilizamos un contenedor cuyo nombre es **silly_tesla** para ilustrar la operación. Como se observa en la primera imagen de la sección anterior, **silly_tesla** es uno de los existentes en nuestro sistema a este punto.

    docker stop silly_tesla

Luego lo removemos con:

    docker rm silly_tesla

Como próximo paso vamos a hacer es deshacernos de **whalesay** ya que cumplió su fin. En el comando de abajo utilizamos **docker/whalesay** para referirnos a la imagen ya que con ese nombre la descargamos del Hub:

    docker rmi docker/whalesay

![Eliminar contenedores](assets/docker-rm.png)

Siempre podemos ver la lista de imágenes que tenemos descargadas empleando `docker images` para asegurarnos de que no estamos desperdiciando espacio en el sistema de archivos del host con archivos que no empleamos más.

En [el próximo post](posts/docker-comandos-basicos-segunda-parte) de esta serie aprenderemos otras alternativas para realizar las tareas que detallamos en esta oportunidad y otras nuevas. ¡Nos leemos ahí!