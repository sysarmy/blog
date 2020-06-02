---
Description: "Mi Primera Imagen con Docker"
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
Title: Mi Primera Imagen con Docker
Topics:
- sysarmy
- docker
- containers
- linux
markup: markdown
date: 2020-05-15
---

Como explicamos en [el primer artículo de esta serie](posts/que-es-docker), una imagen contiene los binarios de una aplicación, sus dependencias, metadatos e indicaciones para su ejecución. No incluye un sistema operativo completo ni un kernel, ya que esos recursos son provistos por el host mismo donde Docker está corriendo. También es importante aclarar que una imagen puede consistir de una sola aplicación o de un conjunto más robusto como un stack LAMP completo. Hasta este momento hemos utilizado imágenes descargadas del [Hub](https://hub.docker.com/), pero ahora aprenderemos cómo crear una propia de acuerdo a nuestras necesidades.

## El Dockerfile

Para crear nuestra primer imagen a medida, necesitamos introducir el concepto de Dockerfile. En pocas palabras, un Dockerfile es una receta que detalla los componentes y una serie de operaciones paso a paso para generar una imagen. A pesar de que guarda ciertas similitudes con un shell script, en realidad utiliza un lenguaje propio de Docker. Para ilustrar, agreguemos el siguiente contenido a un archivo llamado **Dockerfile** en nuestro directorio actual: 

```
FROM nginx:1.18.0-alpine
WORKDIR /usr/share/nginx/html
COPY index.html index.html
```

Cada una de estas líneas crea [una capa de sólo lectura](https://docs.docker.com/storage/storagedriver/#images-and-layers) en el proceso de creación de la imagen y cumple la siguiente función:

- `FROM nginx:1.18.0-alpine` indica que vamos a usar como base la imagen **nginx** que posea la etiqueta `1.18.0-alpine`. Hasta este momento no habíamos utilizado etiquetas para especificar una versión o alternativa determinada de una imagen. Es importante aclarar que cuando hicimos eso, tomamos latest por defecto. En el caso de **nginx**, podríamos haber utilizado cualquiera de los tags disponibles en la descripción de la imagen oficial:

![Etiquetas disponibles en la imagen nginx](assets/docker-imagen-nginx-etiquetas.png)

Los tags que aparecen en cada ítem de la imagen de arriba son sinónimos entre sí. En otras palabras, es lo mismo emplear `1.18.0-alpine` que `stable-alpine` o `1.18-alpine`. De la misma forma, las etiquetas `latest`, `1.17.10`, `mainline`, `1`, o `1.17` describen una misma imagen. 

- `WORKDIR /usr/share/nginx/html` cambia el directorio de trabajo a /usr/share/nginx/html dentro de la imagen. Si bien se podría utilizar `RUN cd /usr/share/nginx/html`, es conveniente emplear `WORKDIR` para que los comandos siguientes se ejecuten en ese directorio. La alternativa basada en `RUN` solamente nos posicionaría en el directorio mencionado mientras se procesa la línea actual del Dockerfile. Como precisamos copiar un archivo en este caso (veamos la próxima línea), nos inclinamos por `WORKDIR`.

- `COPY index.html index.html` copia un archivo llamado index.html desde nuestra ubicación actual al directorio raíz del servidor web (que especificamos con `WORKDIR /usr/share/nginx/html` en la línea anterior). Nuestro index.html de ejemplo tiene el siguiente contenido:

```html
<!DOCTYPE html>
<html>
    <head>
            <title>Docker con sysarmy</title>
        </head>
        <body>
            <h1 style="color: dodgerblue;">Construir una imagen desde cero</h1>
        </body>
</html>
```

Ahora que tenemos el Dockerfile y el HTML estamos en condición de utilizarlos para llevar a cabo la creación de la imagen. Aunque en este caso estamos utilizando un archivo individual, es lo mismo para una aplicación entera con más componentes.

## Nuestra primera imagen

A modo de práctica, veamos la lista de comandos disponibles para la administración de imágenes. Luego de escribir `docker image` y presionar Tab dos veces, veremos las siguientes posibilidades:

- `build`
- `import`
- `load`
- `prune`
- `push`
- `save`
- `history`
- `inspect`
- `ls`
- `pull`
- `rm`
- `tag`

Debido a que `build` parece ser lo que necesitamos, podemos agregar `--help` y ver una descripción:

![Descripción de docker build](assets/docker-build-help.png)

La sintaxis para generar la imagen es la siguiente:

```bash
docker image build -t mi-nginx-app:latest .
```

donde `mi-nginx-app:latest` será el nombre de la imagen y su etiqueta, mientras que el punto del final indica que el contexto de la imagen se tomará de nuestra ubicación actual en el host. Esto significa que Docker incluirá todo el contenido de nuestro directorio de trabajo en la creación de la imagen. Si nos descuidamos con esto, podemos llegar a obtener una imagen de mayor tamaño que la que queríamos. Como consecuencia, esto puede repercutir en el tiempo necesario para generar la imagen, para publicarla (enviarla al [Hub](https://hub.docker.com/), opcionalmente) y para su uso posterior.

![Generar la imagen basada en nginx](assets/docker-build-nginx.png)

En la imagen de arriba podemos observar lo siguiente:

- Cada línea en el Dockerfile representa un paso en la generación de la imagen (señalados con las flechas).

- Resaltados en celeste aparecen los hashes que Docker guarda para identificar el resultado de cada paso. Esto sirve para agilizar la generación de imágenes basadas en el mismo Dockerfile que hagamos en el futuro. Si cambiáramos algo en el paso 2, esto haría que Docker vuelva a procesar la línea en cuestión y todas las siguientes.

- En verde aparece el ID de la imagen resultante, la cual coincide con el que vemos en el resultado de `docker image ls`. En este mismo comando vemos que el proceso de generación de la imagen incluyó la descarga de la imagen `1.18.0-alpine`. Debido a que `nginx:1.18.0-alpine` y `mi-nginx-app:latest` difieren en un solo archivo (index.html), el tamaño que apreciamos en la última columna -expresado en MB- es idéntico.

El último paso consistirá en crear un contenedor basado en nuestra nueva imagen para comprobar el resultado.

## Creación del contenedor

Para finalizar, vamos a instanciar un contenedor utilizando mi-nginx-app. Para poder acceder al mismo, expondremos el puerto 8080 del host y lo asociaremos al puerto 80 del contenedor:

```bash
docker container run --name=mi-contenedor --publish 8080:80 mi-nginx-app
```

![Creación y prueba del contenedor basado en la imagen nginx](assets/docker-nginx-contenedor-propio.png)

Al navegar al puerto 8080 del host veremos el archivo index.html que incluimos en la imagen, mientras que en la consola observaremos los registros de acceso.

## Conclusión

En este artículo aprendimos a crear una nueva imagen partiendo de un Dockerfile y creamos un contenedor basado en la misma. Este ejercicio es la base para crear imágenes y contenedores más robustos, tema que abordaremos en [nuestro próximo post](posts/docker-proyecto-primera-parte). ¡Hasta la próxima! 