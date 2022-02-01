# :rocket: Sysarmy Blog

El blog de Sysarmy fue migrado desde Wordpress hacia [Go Hugo](https://gohugo.io/).

# ¿Como contribuir?

Las contribuciones siempre son bienvenidas! La idea es que, cuanto más contenido afín tengamos en el blog, mayor será el beneficio para la comunidad. El único requisito es que el contenido esté en español.

La forma mas práctica para contribuir cortita y al pie:

- Forkear el repo. [911 que es git?](https://teloexplicocongatitos.com/poster/tlecg04)
- git clone
- git checkout new-post
- Copiar content/posts/template-post.md a el nuevo post
- Sacar todo los placeholders y escribir el post per se.
- commit a tu fork/new-post <- IMPORTANTE
- Hacer pull request a blog/new-post <- IMPORTANTE
- Algún admin del post va a revisar el pull request, quizás iterar con comentarios.
- Finalmente el pull request se acepta.
- Probablemente se hagan ajustes finales.
- Se mergea a master y se publica en internet.

## Instalación y configuración de Go Hugo
Utilizando brew se debe correr el siguiente comando
```bash
brew install hugo
```
Verificar la versión instalada
```bash
hugo version
```
Clonar este proyecto 
```bash
git clone https://github.com/sysarmy/blog.git
```
En el archivo config.toml se encuentra atributo publishDir, este se utiliza para determinar el directorio destino cuando se buildea.
Una vez en el directorio blog, iniciar Go Hugo en modo Develop (no genera los archivos estáticos).
```bash
hugo server -D
```

## Creación de un post
Se puede utilizar el siguiente comando para generarlo. El archivo se encontrará dentro del directorio contest/posts/
```bash
hugo new posts/nombre-del-post.md
```
La metadata que se está cargando en todos los posts es: Description, Keywords, Tags, Thumbnail/socialImage/featuredImage (los 3 tienen el mismo valor), Title, Topics, markup (markdown/html según corresponda) y date.
Ejemplo: 
```md
---
Description: "10 proyectos de portfolio para aspirantes a automation engineer"
Keywords:
- devops 
- engineer
- tools
- jr
- aprender
Section: 
Tags:
- sysarmy
- devops 
- engineer
- tools
- jr
- aprender
Thumbnail: assets/202103-iniciarse-en-devops.png
socialImage: assets/202103-iniciarse-en-devops.png
featuredImage: assets/202103-iniciarse-en-devops.png
Title: "Como entrar a DevOps, un hilo robado"
Topics:
- devops 
- engineer
- tools
- jr
- aprender
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



## Links de utilidad
[Go Hugo - Quick start](https://gohugo.io/getting-started/quick-start/)


