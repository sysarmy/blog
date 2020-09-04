# :rocket: Sysarmy Blog

El blog de Sysarmy fue migrado desde Wordpress hacia [Go Hugo](https://gohugo.io/).

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

Una vez finalizado el post, queda buildear y pushear el directorio creado al /blog del repo sysarmy.github.io.
```bash
hugo
```
## Links de utilidad
[Go Hugo - Quick start](https://gohugo.io/getting-started/quick-start/)
