# :rocket: Sysarmy Blog

El blog de Sysarmy fue migrado desde Wordpress hacia [Go Hugo](https://gohugo.io/).

# ¿Como contribuir?

Las contribuciones siempre son bienvenidas, la idea es que cuando mas contenido afin tengamos en el blog, mayor beneficio para la comunidad. El unico requisito es que el contenido este en español.

La forma mas práctica para contribuir cortita y al pie:

- Forkear el repo
- git clone
- git checkout new-post
- copiar content/posts/template-post.md a el nuevo post
- sacar todo los placeholders y escribir el post per se.
- commit a tu fork/new-post <- IMPORTANTE
- hacer pull request a blog/new-post <- IMPORTANTE
- algun admin del post va a revisar el pull request, quizas iterar con comentarios.
- finalmente el pull request se acepta.
- Probablemente se hagan ajustes finales.
- se mergea a master y se publica en internet

## Instalación y configuracion de Go Hugo
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
La metadata que se está cargando en los todos los posts es: Slug, Tags, Thumbnail, Title, Url, date y la imagen (mismo valor que Thumbnail)
Ejemplo: 
```md
---
Description: "Sysarmy - Comunidad de sistemas"
Keywords:
- sysadmin
- sistemas
- desarrollo
- developer
- administración de sistemas
- administrador de sistemas
- linux
- cloud
- docker
- kubernetes
Section:
Slug: vos-de-que-trabajabas
Tags:
- sysarmy
Thumbnail: /blog/assets/xkcd.png
Title: Vos, de qué trabajabas?
Topics:
- Development
- Leadership
- Systems
Url: 2015/03/15/vos-de-que-trabajabas
date: 2015-03-15
---

{{% img src="/blog/assets/xkcd.png" class="half right" %}}
```

Una vez finalizado el post, localmente se puede validar buildeando.

```bash
hugo
```
:exclamation: Atención: En este repo solo se debe subir el post porque se buildea automágicamente y luego se podrá ver en https://sysarmy.com/blog

## Links de utilidad
[Go Hugo - Quick start](https://gohugo.io/getting-started/quick-start/)
