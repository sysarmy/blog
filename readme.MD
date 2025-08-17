# :rocket: Sysarmy Blog

En nuestro blog publicamos novedades y artículos relacionados a nuestra comunidad y tecnología en general.

El blog de Sysarmy está hecho con [Go Hugo](https://gohugo.io/).

## ¿Cómo contribuir?

¡Las contribuciones siempre son bienvenidas! La idea es que, cuanto más contenido afín tengamos en el blog, mayor será el beneficio para la comunidad. El único requisito es que el contenido esté en español.

La forma más directa y fácil de contribuir es escribiendo tu post en un Documento de Google y [compartiéndolo con la comunidad](#ayuda-de-la-comunidad) para que alguien lo pueda revisar y publicar por vos.

Si querés darle el formato vos, en [este artículo](https://github.com/firstcontributions/first-contributions/blob/master/translations/README.es.md) podés ver una guía paso a paso para realizar tu primera contribución a un repositorio en GitHub, y acá te dejamos una lista cortita y al pie para mandar tu contribución:

1. Forkear el repo. [911 que es git?](https://teloexplicocongatitos.com/poster/tlecg04)
2. [Clonar](https://github.com/firstcontributions/first-contributions/blob/master/translations/README.es.md#clona-clone-el-repositorio) el fork a tu PC con `git clone`.
3. Crear una nueva rama, por ejemplo _new-post_ usando `git checkout -b new-post`.
4. En el directorio `content/posts/` vas a encontrar el archivo **template-post.md**, que es una plantilla. Copiarlo, y ponerle el nombre del post.
5. Editar los valores por defecto (description, tags, etc) y escribir el post per se. El post se formatea por defecto usando Markdown, así que te dejamos [una guía rápida](https://docs.github.com/es/get-started/writing-on-github/getting-started-with-writing-and-formatting-on-github/basic-writing-and-formatting-syntax) para poder darle formato a tu post. Todas las imágenes que uses en tu post las tenés que dejar en el directorio `static/assets/`, y las podés insertar en el cuerpo del post usando Markdown, por ejemplo `![](assets/mi-imagen.png)`.
6. :exclamation: Hacer el commit y push a tu fork/new-post. Este paso es importante, siempre hacer el push a tu fork.
7. :exclamation: Hacer [pull request](https://github.com/firstcontributions/first-contributions/blob/master/translations/README.es.md#env%C3%ADa-submit-tus-cambios-para-ser-revisados) a `blog/master`.
8. Algún admin del blog va a revisar el pull request, quizás iterar con comentarios.
9. Finalmente el pull request se acepta.
10. Probablemente se hagan ajustes finales.
11. Se mergea a master y se publica en :sparkles:Internet:sparkles:.

## Instalación y configuración de Go Hugo

[En este link](https://gohugo.io/getting-started/installing/) podés encontrar la documentación oficial para instalar Go Hugo (en inglés). De todas maneras te dejamos algunas alternativas de instalación:

<details>
  <summary><h3>En Windows</h3></summary>
  Si estás en una PC con Windows y usas <a href='https://chocolatey.org/'>Chocolatey</a> como gestor de paquetes, podés instalar Hugo con el siguiente comando: 
  
  <div class="highlight highlight-source-shell position-relative overflow-auto">
    <pre>choco install hugo -confirm</pre>
  </div>
  
  Y después iniciarlo es tan simple como ejecutar:
  
  <div class="highlight highlight-source-shell position-relative overflow-auto">
    <pre>hugo server -D</pre>
  </div>
  Por defecto vas a poder acceder al blog entrando a <a href='http://localhost:1313/blog/'>http://localhost:1313/blog/</a>.
</details>

<details>
  <summary><h3>En MacOS</h3></summary>
  
  Utilizando [brew](https://brew.sh/index_es) se debe correr el siguiente comando:
  
  <div class="highlight highlight-source-shell position-relative overflow-auto">
    <pre>brew install hugo</pre>
  </div>
 
  Verificar la versión instalada
  
  <div class="highlight highlight-source-shell position-relative overflow-auto">
    <pre>hugo version</pre>
  </div>

  En el archivo config.toml se encuentra atributo publishDir, este se utiliza para determinar el directorio destino cuando se buildea.
  Una vez clonado el repositorio y desde el directorio blog, iniciar Go Hugo en modo Develop (no genera los archivos estáticos):
  
  <div class="highlight highlight-source-shell position-relative overflow-auto">
    <pre>hugo server --renderToMemory</pre>
  </div>
  Por defecto vas a poder acceder al blog entrando a <a href='http://localhost:1313/blog/'>http://localhost:1313/blog/</a>.
</details>

<details>
  <summary><h3>En Linux</h3></summary>
  <ul>
    <li><h4>Paquete de Snap</h4></li>
    Para las <a href='https://snapcraft.io/docs/installing-snapd'>distribuciones que soporten Snap</a>, se puede instalar con:
    <div class="highlight highlight-source-shell position-relative overflow-auto">
      <pre lang="console">snap install hugo</pre>
    </div>
    <li><h4>Debian y Ubuntu</h4></li>
    <div class="highlight highlight-source-shell position-relative overflow-auto">
      <pre lang="console">sudo apt-get install hugo</pre>
    </div>
    La documentación de Hugo recomienda utilizar el paquete de Snap sobre esta opción ya que el .deb suele estar algunas versiones atrasado.
    <li><h4><a href='https://i.kym-cdn.com/photos/images/newsfeed/002/243/374/ae2.jpg'>Arch Linux</a></h4></li>
    Armaste el OS con tus propias manos, así que no debería ser necesario aclararlo, pero:
    <div class="highlight highlight-source-shell position-relative overflow-auto">
      <pre lang="console">sudo pacman -Syu hugo</pre>
    </div>
    <li><h4>Fedora</h4></li>
    <div class="highlight highlight-source-shell position-relative overflow-auto">
      <pre lang="console">sudo dnf install hugo</pre>
    </div>
  </ul>
  
  Una vez instalado Hugo, independientemente de tu distribución, y desde el directorio clonado del repositorio, podés iniciar Hugo con el siguiente comando:
  <div class="highlight highlight-source-shell position-relative overflow-auto">
    <pre lang="console">hugo server -D</pre>
  </div>
  Por defecto vas a poder acceder al blog entrando a <a href='http://localhost:1313/blog/'>http://localhost:1313/blog/</a>.
</details>

<details>
  <summary><h3>Con Docker</h3></summary>
  El equipo de Hugo no ofrece imágenes oficiales de Docker, pero recomienda la siguiente: <a href='https://hub.docker.com/r/klakegg/hugo/'>https://hub.docker.com/r/klakegg/hugo/</a>
  
  Para utilizarla, desde el directorio del repositorio clonado, solo hay que ejecutar:
  <div class="highlight highlight-text-shell-session position-relative overflow-auto">
    <pre lang="console">docker run --rm -it \
      -v $(pwd):/src \
      -p 1313:1313 \
      klakegg/hugo \
      server</pre>
  </div>
  
  O también se puede usar con docker-compose:
  <div class="highlight highlight-text-shell-session position-relative overflow-auto">
    <pre lang="yaml">server:
    image: klakegg/hugo
    command: server
    volumes:
      - ".:/src"
    ports:
      - "1313:1313"</pre>
  </div>
  Por defecto vas a poder acceder al blog entrando a <a href='http://localhost:1313/blog/'>http://localhost:1313/blog/</a>.  
</details>

## Información importante sobre los posts
Además de hacer una copia del template, también se puede utilizar el siguiente comando para generar un post nuevo. El archivo se encontrará dentro del directorio `content/posts/`:
```console
hugo new posts/nombre-del-post.md
```
La metadata que se está cargando en todos los posts es:

- **Title**: el título del post.
- **Description**: descripción del contenido del post.
- **Keywords**: palabras clave relacionadas con el contenido del post.
- **Tags**: similar a keywords, etiquetas que permitan filtrar el post.
- **Thumbnail/socialImage/featuredImage** (los 3 tienen el mismo valor): imagen principal del artículo.
- **Topics**: similar a tags, temas que aborda el post.
- **markup**: markdown o html según corresponda.
- **date**: fecha de publicación.

Ejemplo: 
```md
---
Description: "10 proyectos de portfolio para aspirantes a automation engineer"
Keywords:
- devops 
- engineer
- ...
Section: 
Tags:
- sysarmy
- devops
- ...
Thumbnail: assets/202103-iniciarse-en-devops.png
socialImage: assets/202103-iniciarse-en-devops.png
featuredImage: assets/202103-iniciarse-en-devops.png
Title: "Como entrar a DevOps, un hilo robado"
Topics:
- devops 
- engineer
- ...
markup: markdown
date: 2021-03-02
draft: false
---
```

Una vez finalizado el post, localmente se puede validar buildeando.

```bash
hugo
```
:exclamation: Atención: En este repo solo se debe subir el post porque se buildea automágicamente y luego se podrá ver en https://sysarmy.com/blog

## Ayuda de la comunidad

¿Dudas, consultas o inquietudes? Podés sumarte a [Discord <img width="16px" src="https://cdn.jsdelivr.net/npm/simple-icons@v/icons/discord.svg" />](https://sysar.my/discord) o [Slack <img width="16px" src="https://cdn.jsdelivr.net/npm/simple-icons@v3/icons/slack.svg" />](https://sysar.my/slack), en ambos hay un canal `#disneyland` (que esta bridgeado entre ambas plataformas). Si dejas un mensaje 🛎️ ahí alguien te va a responder (aunque pueda tardar un poco).

## Links de utilidad
- [Primeras contribuciones](https://github.com/firstcontributions/first-contributions/blob/master/translations/README.es.md)
- [Go Hugo - Install Hugo](https://gohugo.io/getting-started/installing/)
- [Go Hugo - Quick start](https://gohugo.io/getting-started/quick-start/)


