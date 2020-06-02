---
Description: "Proyecto con Docker - Parte 1 (Mejorar el Dockerfile)"
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
Title: Proyecto con Docker - Parte 1 (Mejorar el Dockerfile)
Topics:
- sysarmy
- docker
- containers
- linux
markup: markdown
date: 2020-06-02
---

En [el artículo anterior](posts/docker-mi-primera-imagen) abordamos el tema de la creación de una imagen sencilla desde cero a partir de un Dockerfile. En base a los principios que explicamos previamente en esta serie, en este post comenzaremos a construir un ejemplo más robusto. Durante el proceso aprovecharemos para introducir nuevos conceptos y algunas buenas prácticas para la escritura de un Dockerfile partiendo de un proyecto existente en Github.

## Clonar un proyecto desde Github

En esta oportunidad, el primer paso consistirá en clonar un repositorio desde la cuenta de Docker Samples en Github:

```bash
git clone https://github.com/dockersamples/node-bulletin-board.git
```

Una vez finalizado el paso anterior, encontraremos el Dockerfile en el directorio node-bulletin-board/bulletin-board-app:

```bash
cd node-bulletin-board/bulletin-board-app
cat Dockerfile
```

donde veremos el siguiente contenido:

```
FROM node:current-slim

WORKDIR /usr/src/app
COPY package.json .
RUN npm install

EXPOSE 8080
CMD [ "npm", "start" ]

COPY . .
```

Algunas de las directivas nos resultarán familiares de nuestro post anterior:

- `FROM node:current-slim` nos dice que se usaremos la imagen **node** con la etiqueta **current-slim** como base. Por lo general, las imágenes que llevan la palabra _slim_ en su etiqueta incluyen lo justo y lo necesario para correr node - nada más y nada menos. Esta es una buena práctica para lograr que la imagen final sea lo más pequeña posible y resulta tanto en menor espacio ocupado en disco como en una mayor rapidez en el proceso de generación. Sin embargo, es importante destacar que esta alternativa puede no resultar la más apropiada si vamos a necesitar otros módulos. En ese caso, podemos optar por `node:current` o `node:current-alpine`.

- Con `WORKDIR /usr/src/app` cambiamos el directorio actual de trabajo en la imagen a /usr/src/app para luego copiar el archivo package.json (el manifiesto de la aplicación) desde nuestro equipo local a ese lugar (simbolizado por el punto).

Mientras que otras son nuevas o toman un formato distinto que las que habíamos visto previamente:

- `RUN npm install` ejecuta el comando en cuestión en una shell (`/bin/sh -c` en Linux o `cmd /S /C` en Windows). Una forma alternativa para obtener el mismo resultado sería `RUN [ "npm", "install" ]``. Por lo general, se emplea la primera cuando se necesita una expansión de la shell y la segunda cuando el comando a correr espera opciones o más parámetros. Cuando ninguno de los dos casos aplica directamente, se puede emplear cualquiera de las dos alternativas.

- `EXPOSE 8080` abre el puerto especificado e indica que el contenedor estará escuchando en el mismo. Si no es especifica un protocolo, se asume TCP, aunque también puede escribirse explícitamente como 8080/tcp. Es importante recordar que más adelante tendremos que mapear un puerto de host disponible al que acabamos de exponer en el contenedor.

- `CMD [ "npm", "start" ]` es el comando que se debe correr cuando se inicie el contenedor (`npm start`). Solamente puede haber una directiva `CMD` por Dockerfile. Si se encuentra más que una, solamente la última se tendrá en cuenta.

- Finalmente, `COPY . .` copia todo el contenido de nuestra ubicación actual en el host (representado por el primer punto) al directorio de trabajo de la imagen (que establecimos antes mediante `WORKDIR`).

> La instrucción `RUN` difiere de `CMD` en que se utiliza durante el proceso de creación de la imagen, mientras que esta última indica la acción inicial del contenedor.

Más adelante volveremos sobre un par de estas directivas para hacerlas más eficaces, pero por el momento podemos usar el Dockerfile tal como está para generar la imagen y levantar el contenedor.

## Crear la imagen y el contenedor

Desde el mismo directorio donde se encuentra el Dockerfile, ejecutaremos el siguiente comando para generar la imagen y aplicarle la etiqueta 1.0:

```bash
docker image build -t sysarmy-bulletin-board:1.0 .
```

A continuación, levantaremos un contenedor basado en la imagen que acabamos de crear. La opción `--rm` hará que Docker elimine el contenedor cuando finalice su ejecución. Recordemos que con la opción `--publish` indicamos primero el puerto del host y a continuación el del contenedor. En este caso son iguales, pero no necesariamente siempre van a serlo.

```bash
docker container run --rm --name=bulletin-board --publish 8080:8080 sysarmy-bulletin-board:1.0
```

Finalmente, podemos ver la aplicación funcionando apuntando a la IP del host usando el puerto 8080:

![La aplicación node en funcionamiento](assets/docker-node-app.png)

Por lo que podemos ver, la aplicación está funcionando aunque testear está fuera del propósito de este artículo. La pregunta que en realidad nos interesa es: ¿habrá algo en el Dockerfile que podamos retocar para generar la imagen de forma más eficiente?

## Mejorar el Dockerfile

Antes de editar el archivo, veamos el tamaño en bytes de la imagen que creamos previamente. La imagen de abajo muestra 181538292 bytes (182 MB aproximadamente):

```bash
docker image inspect sysarmy-bulletin-board:1.0 --format='{{.Size}}'
```

![Tamaño de una imagen](assets/docker-image-size.png)

La primera modificación que vamos a introducir en el Dockerfile es en la línea `COPY . .` (última directiva) para que solamente copie los contenidos necesarios a la imagen y nada más. Si examinamos el contenido de nuestra ubicación actual veremos que hay archivos que no serán necesarios en la imagen y mucho menos en el contenedor. En particular, no tiene sentido copiar en la imagen el mismo Dockerfile, el archivo de licencia, el manifiesto y el readme.md porque esos recursos no son necesarios para el contenedor. Para implementar este cambio, reemplazaremos la línea

```
COPY . .
```

por

```
COPY [ "backend", "backend/" ]
COPY [ "app.js", "fonts", "index.html", "server.js", "site.css", "./" ]
```

donde vemos que cada recurso de origen es nombrado específicamente y el destino (**backend/** primero y **./** luego) tiene que indicarse con una barra al final. Como **backend** es un directorio, tenemos que incluirlo en su propia línea debido a que la directiva no copia el directorio mismo sino solamente sus contenidos. La razón por la que hacemos la copia en este orden es para poder aprovechar la caché en el futuro, ya que es más probable que cambie la última línea (contenidos de la raíz) que el módulo **backend**. Recordemos que cualquier cambio en una línea del Dockerfile invalida la caché de ese paso y de todos los siguientes.

Por último, vamos a colocar estas directivas antes que `CMD [ "npm", "start" ]` que dejaremos para el final como es costumbre. A este punto, el Dockerfile quedó de la siguiente forma:

```
FROM node:current-slim

WORKDIR /usr/src/app
COPY package.json .
RUN npm install

EXPOSE 8080
COPY [ "backend", "backend/" ]
COPY [ "app.js", "fonts", "index.html", "server.js", "site.css", "./" ]
CMD [ "npm", "start" ]
```

Al generar la imagen con la etiqueta 1.1 vemos que se utilizaron varios pasos desde la caché (resaltados en verde) debido a que las líneas en cuestión no cambiaron:

![Generación de la nueva imagen](assets/docker-build-image.png)

Ahora veamos el tamaño de la imagen resultante comparada a la anterior:

![Comparación en el tamaño de las imágenes](assets/docker-image-size-2.png)

Como podemos ver arriba, nos ahorramos poco menos que 3 KB. Si bien ese espacio es prácticamente insignificante, la práctica de copiar a la imagen el contenido que se necesite (y nada más) puede reducir el tamaño de una forma apreciable en otros casos. Además, nos aseguramos de que el contenedor tendrá los recursos justos sin otros agregados.

## Conclusión

En este post explicamos dos cuestiones importantes a tener en cuenta a la hora de escribir un Dockerfile (no incluir en la imagen contenidos innecesarios y aprovechar la caché). En la medida que nuestros proyectos se vuelvan más robustos podremos sacarle mayor provecho a lo que aprendimos en esta oportunidad. En el último post de esta serie aprovecharemos todos los contenidos que hemos desarrollado hasta ahora para darle algunos toques finales al proyecto y mostraremos la manera de publicar nuestra imagen en el [Hub](https://hub.docker.com/). ¡No se lo pierdan!