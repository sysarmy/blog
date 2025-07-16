---
Title: "50 herramientas y comandos CLI que no vas a poder dejar de usar"
Description: "Una recopilación imprescindible de 50 comandos y herramientas de línea de comandos que mejoran la productividad y hacen tu vida como developer mucho más fácil."
Keywords:
- cli
- terminal
- productividad
- herramientas para developers

Tags:
- sysarmy
- bash
- tooling
- productividad

Thumbnail: assets/50-cli-command-tools.png
socialImage: assets/50-cli-command-tools.png
featuredImage: assets/50-cli-command-tools.png

Topics:
- herramientas de desarrollo
- eficiencia en terminal
- productividad técnica

markup: markdown
date: 2025-07-16
draft: true
---

![logo](https://media2.dev.to/dynamic/image/width=1000,height=420,fit=cover,gravity=auto,format=auto/https%3A%2F%2Fi.ibb.co%2FF4THZ2T%2Fcli-tools-banner.png)
Como desarrolladores, pasamos gran parte de nuestro tiempo en el terminal. Hay un montón de herramientas útiles CLI, que pueden hacer su vida en la línea de comandos más fácil, más rápido y más divertido en general.

Este post describe mi top 50 de herramientas CLI imprescindibles, en las que he llegado a confiar. Si hay algo que me falta - hágamelo saber en los comentarios :)

Al final del artículo, he incluido algunas secuencias de comandos para ayudarle a automatizar la instalación y actualización de estas herramientas en varios sistemas / distros.


↕️ **Índice** (haz clic para expandir)  
- [Utils](#utils)
  - [`thefuck` - Autocorrección de comandos mal escritos](#thefuck---autocorrección-de-comandos-mal-escritos)
  - [`zoxide` - Fácil navegación _(mejor cd)_](#zoxide---fácil-navegación-mejor-cd)
  - [`tldr` - Documentos mantenidos por la comunidad _(mejor `man`)_](#tldr---documentos-mantenidos-por-la-comunidad-mejor-man)
  - [`scc` - Contar líneas de código _(mejor `cloc`)_](#scc---contar-líneas-de-código-mejor-cloc)
  - [`exa` - Archivos de listado _(mejor `ls`)_](#exa---archivos-de-listado-mejor-ls)
  - [`duf` - Uso del disco _(mejor `df`)_](#duf---uso-del-disco-mejor-df)
  - [`aria2` - Utilidad de descarga _(mejor `wget`)_](#aria2---utilidad-de-descarga-mejor-wget)
  - [`bat` - Lectura de archivos _(mejor `cat`)_](#bat---lectura-de-archivos-mejor-cat)
  - [`diff-so-fancy` - Comparación de archivos _(mejor `diff`)_](#diff-so-fancy---comparación-de-archivos-mejor-diff)
  - [`entr` - Esté atento a los cambios](#entr---esté-atento-a-los-cambios)
  - [`exiftool` - Lectura y escritura de metadatos](#exiftool---lectura-y-escritura-de-metadatos)
  - [`fdupes` - Buscador de archivos duplicados](#fdupes---buscador-de-archivos-duplicados)
  - [`fzf` - Buscador de archivos difuso _(mejor `find`)_](#fzf---buscador-de-archivos-difuso-mejor-find)
  - [`hyperfine` - Evaluación comparativa de mandos](#hyperfine---evaluación-comparativa-de-mandos)
  - [`just` - Corredor de comandos moderno _(mejor `make`)_](#just---corredor-de-comandos-moderno-mejor-make)
  - [`jq` - Procesador JSON](#jq---procesador-json)
  - [`most` - Localizador de desplazamiento multiventana _(mejor less)_](#most---localizador-de-desplazamiento-multiventana-mejor-less)
  - [`procs` - Visor de procesos _(mejor ps)_](#procs---visor-de-procesos-mejor-ps)
  - [`rip` - Herramienta de borrado _(mejor rm)_](#rip---herramienta-de-borrado-mejor-rm)
  - [`ripgrep` - Búsqueda dentro de archivos _(mejor `grep`)_](#ripgrep---búsqueda-dentro-de-archivos-mejor-grep)
  - [`rsync` - Transferencia rápida e incremental de archivos](#rsync---transferencia-rápida-e-incremental-de-archivos)
  - [`sd` - Buscar y reemplazar _(mejor `sed`)_](#sd---buscar-y-reemplazar-mejor-sed)
  - [`tre` - Jerarquía de directorios _(mejor `tree`)_](#tre---jerarquía-de-directorios-mejor-tree)
  - [`xsel` - Acceso al portapapeles](#xsel---acceso-al-portapapeles)
- [CLI - Aplicaciones de monitorización y rendimiento](#cli---aplicaciones-de-monitorización-y-rendimiento)
  - [`bandwhich` - Monitor de utilización de ancho de banda](#bandwhich---monitor-de-utilización-de-ancho-de-banda)
  - [`ctop` - Métricas y monitoreo de contenedores](#ctop---métricas-y-monitoreo-de-contenedores)
  - [`bpytop` - Monitoreo de recursos _(mejor `htop`)_](#bpytop---monitoreo-de-recursos-mejor-htop)
  - [`glances` - Monitor de recursos + web y API](#glances---monitor-de-recursos--web-y-api)
  - [`gping` - Herramienta de ping interactiva _(mejor `ping`)_](#gping---herramienta-de-ping-interactiva-mejor-ping)
  - [`dua-cli` - Analizador y monitor de uso de disco _(mejor `du`)_](#dua-cli---analizador-y-monitor-de-uso-de-disco-mejor-du)
  - [`speedtest-cli` - Utilidad de prueba de velocidad en línea de comandos](#speedtest-cli---utilidad-de-prueba-de-velocidad-en-línea-de-comandos)
  - [`dog` - Cliente de búsqueda DNS _(mejor `dig`)_](#dog---cliente-de-búsqueda-dns-mejor-dig)
- [CLI Productividad](#cli-productividad)
  - [`browsh` - Navegador web CLI](#browsh---navegador-web-cli)
  - [`buku` - Gestor de marcadores](#buku---gestor-de-marcadores)
  - [`cmus` - Reproductor / navegador de música](#cmus---reproductor--navegador-de-música)
  - [`cointop` - Seguimiento de precios cripto](#cointop---seguimiento-de-precios-cripto)
  - [`ddgr` - Buscar en la web desde terminal](#ddgr---buscar-en-la-web-desde-terminal)
  - [`micro` - Editor de código _(mejor `nano`)_](#micro---editor-de-código-mejor-nano)
  - [`khal` - Cliente de Calendario](#khal---cliente-de-calendario)
  - [`mutt` - Cliente de Email](#mutt---cliente-de-email)
  - [`newsboat` - Lector de noticias RSS / ATOM](#newsboat---lector-de-noticias-rss--atom)
  - [`rclone` - Gestionar el almacenamiento en la nube](#rclone---gestionar-el-almacenamiento-en-la-nube)
  - [`taskwarrior` - Todo + gestión de tareas](#taskwarrior---todo--gestión-de-tareas)
  - [`tuir` - Terminal UI para Reddit](#tuir---terminal-ui-para-reddit)
- [CLI Dev Suits](#cli-dev-suits)
  - [`httpie` - Cliente de pruebas HTTP / API](#httpie---cliente-de-pruebas-http--api)
  - [`lazydocker` - Aplicación completa de gestión de Docker](#lazydocker---aplicación-completa-de-gestión-de-docker)
  - [`lazygit` - Aplicación completa de gestión Git](#lazygit---aplicación-completa-de-gestión-git)
  - [`kdash` - Aplicación del panel de control de Kubernetes](#kdash---aplicación-del-panel-de-control-de-kubernetes)
  - [`gdp-dashboard` - Depurador de Visual GDP](#gdp-dashboard---depurador-de-visual-gdp)
- [CLI Servicios Externos](#cli-servicios-externos)
  - [`ngrok` - Proxy inverso para compartir localhost](#ngrok---proxy-inverso-para-compartir-localhost)
  - [`tmate` - Compartir una sesión de terminal a través de Internet](#tmate---compartir-una-sesión-de-terminal-a-través-de-internet)
  - [`asciinema` - Grabar y compartir sesiones de terminal](#asciinema---grabar-y-compartir-sesiones-de-terminal)
  - [`navi` - Hoja de trucos interactiva](#navi---hoja-de-trucos-interactiva)
  - [`transfer.sh` - Intercambio rápido de archivos](#transfersh---intercambio-rápido-de-archivos)
  - [`surge` - Despliegue un sitio en segundos](#surge---despliegue-un-sitio-en-segundos)
  - [`wttr.in` - Compruebe el tiempo](#wttrin---compruebe-el-tiempo)
- [CLI Divertidos](#cli-divertidos)
  - [`cowsay` - Haz que una vaca ASCII diga tu mensaje](#cowsay---haz-que-una-vaca-ascii-diga-tu-mensaje)
  - [`figlet` - Texto de salida como texto de arte ASCII grande](#figlet---texto-de-salida-como-texto-de-arte-ascii-grande)
  - [`lolcat` - Haz que la salida de la consola tenga los colores del arco iris](#lolcat---haz-que-la-salida-de-la-consola-tenga-los-colores-del-arco-iris)
  - [`neofetch` - Mostrar datos del sistema e información de la distribución](#neofetch---mostrar-datos-del-sistema-e-información-de-la-distribución)
- [Instalación y Gestión](#instalación-y-gestión)
- [Conclusión](#conclusión)
  - [Información adicional](#información-adicional)
    - [Qué no se incluyó](#qué-no-se-incluyó)
    - [Créditos](#créditos)
    - [Comentarios](#comentarios)
    - [Insignias](#insignias)
- [Acerca de](#acerca-de)
- [Implementación](#implementación)
- [Informar de un problema](#informar-de-un-problema)
    - [Más información](#más-información)

## [](https://dev.to/lissy93/cli-tools-you-cant-live-without-57f6#utils)Utils

### [](https://dev.to/lissy93/cli-tools-you-cant-live-without-57f6#-raw-thefuck-endraw-autocorrect-misstyped-commands)[`thefuck`](https://github.com/nvbn/thefuck) - Autocorrección de comandos mal escritos

> `thefuck` es una de esas utilidades sin las que no podrás vivir una vez que la hayas probado. Siempre que escribas mal un comando y obtengas un error, simplemente ejecuta `fuck` y lo autocorregirá. Usa arriba/abajo para elegir una corrección, o simplemente ejecuta `fuck --yeah` para ejecutar inmediatamente la más probable.

[![the-fuck-example-usage](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Farticles%2Fsd34cab0xeybo4lu2wkf.gif)](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Farticles%2Fsd34cab0xeybo4lu2wkf.gif)

[![Ver thefuck en Github](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fimg.shields.io%2Fgithub%2Fstars%2Fnvbn%2Fthefuck%3Fcolor%3D232323%26label%3Dthefuck%26logo%3Dgithub%26labelColor%3D232323)](https://github.com/nvbn/thefuck) [![Autor nvbn](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fimg.shields.io%2Fbadge%2Fnvbn-b820f9%3FlabelColor%3Db820f9%26logo%3Dgithubsponsors%26logoColor%3Dfff)](https://github.com/nvbn) [![Escrito en Python](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fimg.shields.io%2Fstatic%2Fv1%3Flabel%3D%26message%3DPython%26color%3D3C78A9%26logo%3Dpython%26logoColor%3DFFFFFF)](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fimg.shields.io%2Fstatic%2Fv1%3Flabel%3D%26message%3DPython%26color%3D3C78A9%26logo%3Dpython%26logoColor%3DFFFFFF)

Instalacion

```


# MacOS (via Homebrew)
brew Instalacion thefuck

# Arch Linux
sudo pacman -S thefuck

# FreeBSD
pkg Instalacion thefuck


```

___

### [](https://dev.to/lissy93/cli-tools-you-cant-live-without-57f6#-raw-zoxide-endraw-easy-navigation-better-cd)[`zoxide`](https://github.com/ajeetdsouza/zoxide) - Fácil navegación _(mejor cd)_

> `z` te permite saltar a cualquier directorio sin necesidad de recordar o especificar su ruta completa. Recuerda los directorios que has visitado, para que puedas saltar rápidamente; ni siquiera necesitas escribir el nombre completo de la carpeta. También dispone de una opción de selección interactiva, mediante `fzf`, que permite filtrar los resultados de los directorios en tiempo real.

[![zoxide-example-usage](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Farticles%2F1gvi17q5n2607trw6bnb.gif)](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Farticles%2F1gvi17q5n2607trw6bnb.gif)

[![Ver zoxide en Github](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fimg.shields.io%2Fgithub%2Fstars%2Fajeetdsouza%2Fzoxide%3Fcolor%3D232323%26label%3Dzoxide%26logo%3Dgithub%26labelColor%3D232323)](https://github.com/ajeetdsouza/zoxide) [![Autor ajeetdsouza](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fimg.shields.io%2Fbadge%2Fajeetdsouza-b820f9%3FlabelColor%3Db820f9%26logo%3Dgithubsponsors%26logoColor%3Dfff)](https://github.com/ajeetdsouza) [![Escrito en Rust](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fimg.shields.io%2Fstatic%2Fv1%3Flabel%3D%26message%3DRust%26color%3De86243%26logo%3Drust%26logoColor%3DFFFFFF)](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fimg.shields.io%2Fstatic%2Fv1%3Flabel%3D%26message%3DRust%26color%3De86243%26logo%3Drust%26logoColor%3DFFFFFF)

Instalacion

```


# MacOS (via Homebrew)
brew Instalacion zoxide

# Arch Linux
sudo pacman -S zoxide

# Debian / Ubuntu
sudo apt Instalacion zoxide

# FreeBSD
pkg Instalacion zoxide

# Other (via Rust Creates)
cargo Instalacion zoxide --locked


```

___

### [](https://dev.to/lissy93/cli-tools-you-cant-live-without-57f6#-raw-tldr-endraw-communitymaintained-docs-better-raw-man-endraw-)[`tldr`](https://github.com/tldr-pages/tldr) - Documentos mantenidos por la comunidad _(mejor `man`)_

> `tldr` es una enorme colección de páginas de manual mantenidas por la comunidad. A diferencia de las páginas de manual tradicionales, están resumidas, contienen ejemplos de uso útiles y están coloreadas para facilitar la lectura.

[![tldr-example-usage](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Farticles%2F9vbps7vlm9r42qfk69w8.gif)](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Farticles%2F9vbps7vlm9r42qfk69w8.gif)

[![Ver tldr en Github](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fimg.shields.io%2Fgithub%2Fstars%2Ftldr-pages%2Ftldr%3Fcolor%3D232323%26label%3Dtldr%26logo%3Dgithub%26labelColor%3D232323)](https://github.com/tldr-pages/tldr) [![Autor tldr-pages](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fimg.shields.io%2Fbadge%2Ftldr-pages-b820f9%3FlabelColor%3Db820f9%26logo%3Dgithubsponsors%26logoColor%3Dfff)](https://github.com/tldr-pages)

Instalacion

```


# MacOS (via Homebrew)
brew Instalacion tldr

# Other (via NPM)
npm Instalacion -g tldr


```

___

### [](https://dev.to/lissy93/cli-tools-you-cant-live-without-57f6#-raw-scc-endraw-count-lines-of-code-better-raw-cloc-endraw-)[`scc`](https://github.com/boyter/scc) - Contar líneas de código _(mejor `cloc`)_

> `scc` te da un desglose del número de líneas de código Escrito en cada lenguaje para un directorio específico. También muestra algunas estadísticas divertidas, como el coste estimado de desarrollo e información sobre la complejidad. Es increíblemente rápido, muy preciso y tiene soporte para una amplia gama de lenguajes.

[![scc-example-usage](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Farticles%2Fewcq7bbenleoyy4pztrm.png)](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Farticles%2Fewcq7bbenleoyy4pztrm.png)

[![Ver scc en Github](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fimg.shields.io%2Fgithub%2Fstars%2Fboyter%2Fscc%3Fcolor%3D232323%26label%3Dscc%26logo%3Dgithub%26labelColor%3D232323)](https://github.com/boyter/scc) [![Autor boyter](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fimg.shields.io%2Fbadge%2Fboyter-b820f9%3FlabelColor%3Db820f9%26logo%3Dgithubsponsors%26logoColor%3Dfff)](https://github.com/boyter) [![Escrito en Go](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fimg.shields.io%2Fstatic%2Fv1%3Flabel%3D%26message%3DGo%2520Lang%26color%3D00ADD8%26logo%3Dgo%26logoColor%3DFFFFFF)](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fimg.shields.io%2Fstatic%2Fv1%3Flabel%3D%26message%3DGo%2520Lang%26color%3D00ADD8%26logo%3Dgo%26logoColor%3DFFFFFF)

Instalacion

```


# MacOS (via Homebrew)
brew Instalacion scc

# Other (via go)
go Instalacion github.com/boyter/scc/v3@latest


```

___

### [](https://dev.to/lissy93/cli-tools-you-cant-live-without-57f6#-raw-exa-endraw-listing-files-better-raw-ls-endraw-)[`exa`](https://github.com/ogham/exa) - Archivos de listado _(mejor `ls`)_

> `exa` es un reemplazo moderno basado en Rust para el comando `ls`, para listar archivos. Puede mostrar iconos de tipo de archivo, colores, información de archivo/carpeta y tiene varios formatos de salida - árbol, cuadrícula o lista.

[![exa-example-usage](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Farticles%2F3tkddmk9z6vpejnpw5we.png)](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Farticles%2F3tkddmk9z6vpejnpw5we.png)

[![Ver exa en Github](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fimg.shields.io%2Fgithub%2Fstars%2Fogham%2Fexa%3Fcolor%3D232323%26label%3Dexa%26logo%3Dgithub%26labelColor%3D232323)](https://github.com/ogham/exa) [![Autor ogham](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fimg.shields.io%2Fbadge%2Fogham-b820f9%3FlabelColor%3Db820f9%26logo%3Dgithubsponsors%26logoColor%3Dfff)](https://github.com/ogham) [![Escrito en Rust](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fimg.shields.io%2Fstatic%2Fv1%3Flabel%3D%26message%3DRust%26color%3De86243%26logo%3Drust%26logoColor%3DFFFFFF)](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fimg.shields.io%2Fstatic%2Fv1%3Flabel%3D%26message%3DRust%26color%3De86243%26logo%3Drust%26logoColor%3DFFFFFF)

Instalacion

```


# MacOS (via Homebrew)
brew Instalacion exa

# Arch Linux
sudo pacman -S exa

# Debian / Ubuntu
sudo apt Instalacion exa


```

___

### [](https://dev.to/lissy93/cli-tools-you-cant-live-without-57f6#-raw-duf-endraw-disk-usage-better-raw-df-endraw-)[`duf`](https://github.com/muesli/duf) - Uso del disco _(mejor `df`)_

> `duf` es genial para mostrar información sobre discos montados y comprobar el espacio libre. Produce una salida clara y colorida, e incluye opciones para ordenar y personalizar los resultados.

[![duf-example-usage](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Farticles%2Feaf6xpek2h2nevhmepaa.png)](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Farticles%2Feaf6xpek2h2nevhmepaa.png)

[![Ver duf en Github](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fimg.shields.io%2Fgithub%2Fstars%2Fmuesli%2Fduf%3Fcolor%3D232323%26label%3Dduf%26logo%3Dgithub%26labelColor%3D232323)](https://github.com/muesli/duf) [![Autor muesli](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fimg.shields.io%2Fbadge%2Fmuesli-b820f9%3FlabelColor%3Db820f9%26logo%3Dgithubsponsors%26logoColor%3Dfff)](https://github.com/muesli) [![Escrito en Go](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fimg.shields.io%2Fstatic%2Fv1%3Flabel%3D%26message%3DGo%2520Lang%26color%3D00ADD8%26logo%3Dgo%26logoColor%3DFFFFFF)](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fimg.shields.io%2Fstatic%2Fv1%3Flabel%3D%26message%3DGo%2520Lang%26color%3D00ADD8%26logo%3Dgo%26logoColor%3DFFFFFF)

Instalacion

```


# MacOS (via Homebrew)
brew Instalacion duf

# Arch Linux
sudo pacman -S duf

# Debian / Ubuntu
sudo apt Instalacion duf

# FreeBSD
pkg Instalacion duf


```

___

### [](https://dev.to/lissy93/cli-tools-you-cant-live-without-57f6#-raw-aria2-endraw-download-utility-better-raw-wget-endraw-)[`aria2`](https://github.com/aria2/aria2) - Utilidad de descarga _(mejor `wget`)_

> `aria2` es una utilidad ligera, multiprotocolo, de reanudación de descargas para HTTP/HTTPS, FTP, SFTP, BitTorrent y Metalink, con soporte para control a través de una interfaz RPC. Es increíblemente [rico en funciones](https://aria2.github.io/manual/en/html/README.html), y tiene toneladas de [opciones](https://aria2.github.io/manual/en/html/aria2c.html). También existe [ziahamza/webui-aria2](https://github.com/ziahamza/webui-aria2) - un buen compañero de interfaz web.

[![aria2c-example-usage](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Farticles%2Ffwgy2nq04kxwbrqdlvgc.png)](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Farticles%2Ffwgy2nq04kxwbrqdlvgc.png)

[![Ver aria2 en Github](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fimg.shields.io%2Fgithub%2Fstars%2Faria2%2Faria2%3Fcolor%3D232323%26label%3Daria2%26logo%3Dgithub%26labelColor%3D232323)](https://github.com/aria2/aria2) [![Autor aria2](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fimg.shields.io%2Fbadge%2Faria2-b820f9%3FlabelColor%3Db820f9%26logo%3Dgithubsponsors%26logoColor%3Dfff)](https://github.com/aria2) [![Escrito en C++](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fimg.shields.io%2Fstatic%2Fv1%3Flabel%3D%26message%3DC%2B%2B%26color%3D00599C%26logo%3Dcplusplus%26logoColor%3DFFFFFF)](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fimg.shields.io%2Fstatic%2Fv1%3Flabel%3D%26message%3DC%2B%2B%26color%3D00599C%26logo%3Dcplusplus%26logoColor%3DFFFFFF)

Instalacion

```


# MacOS (via Homebrew)
brew Instalacion aria2

# Arch Linux
sudo pacman -S aria2

# Debian / Ubuntu
sudo apt Instalacion aria2


```

___

### [](https://dev.to/lissy93/cli-tools-you-cant-live-without-57f6#-raw-bat-endraw-reading-files-better-raw-cat-endraw-)[`bat`](https://github.com/sharkdp/bat) - Lectura de archivos _(mejor `cat`)_

> `bat` es un clon de `cat` con resaltado de sintaxis e integración con git. Escrito en Rust, es muy performante, y tiene varias opciones para personalizar la salida y la tematización. Hay soporte para tuberías automáticas y concatenación de archivos.

[![bat-example-usage](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Farticles%2Fkmu0xst70282uodok8ar.png)](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Farticles%2Fkmu0xst70282uodok8ar.png)

[![Ver bat en Github](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fimg.shields.io%2Fgithub%2Fstars%2Fsharkdp%2Fbat%3Fcolor%3D232323%26label%3Dbat%26logo%3Dgithub%26labelColor%3D232323)](https://github.com/sharkdp/bat) [![Autor sharkdp](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fimg.shields.io%2Fbadge%2Fsharkdp-b820f9%3FlabelColor%3Db820f9%26logo%3Dgithubsponsors%26logoColor%3Dfff)](https://github.com/sharkdp) [![Escrito en Rust](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fimg.shields.io%2Fstatic%2Fv1%3Flabel%3D%26message%3DRust%26color%3De86243%26logo%3Drust%26logoColor%3DFFFFFF)](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fimg.shields.io%2Fstatic%2Fv1%3Flabel%3D%26message%3DRust%26color%3De86243%26logo%3Drust%26logoColor%3DFFFFFF)

Instalacion

```


# MacOS (via Homebrew)
brew Instalacion bat

# Arch Linux
sudo pacman -S bat

# Debian / Ubuntu
sudo apt Instalacion bat


```

___

### [](https://dev.to/lissy93/cli-tools-you-cant-live-without-57f6#-raw-diffsofancy-endraw-file-comparisons-better-raw-diff-endraw-)[`diff-so-fancy`](https://github.com/so-fancy/diff-so-fancy) - Comparación de archivos _(mejor `diff`)_

> `diff-so-fancy` le da un mejor aspecto a los diffs para comparar cadenas, archivos, directorios y cambios git. El resaltado de cambios hace que detectar los cambios sea mucho más fácil, y puedes personalizar el diseño y los colores de la salida.

[![diff-so-fancy-example-usage](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Farticles%2F77uu6c0pqoa8j8ft50u9.png)](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Farticles%2F77uu6c0pqoa8j8ft50u9.png)

[![Ver diff-so-fancy en Github](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fimg.shields.io%2Fgithub%2Fstars%2Fso-fancy%2Fdiff-so-fancy%3Fcolor%3D232323%26label%3Ddiff-so-fancy%26logo%3Dgithub%26labelColor%3D232323)](https://github.com/so-fancy/diff-so-fancy) [![Autor so-fancy](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fimg.shields.io%2Fbadge%2Fso-fancy-b820f9%3FlabelColor%3Db820f9%26logo%3Dgithubsponsors%26logoColor%3Dfff)](https://github.com/so-fancy) [![Escrito en Perl](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fimg.shields.io%2Fstatic%2Fv1%3Flabel%3D%26message%3DPerl%26color%3D39457E%26logo%3Dperl%26logoColor%3DFFFFFF)](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fimg.shields.io%2Fstatic%2Fv1%3Flabel%3D%26message%3DPerl%26color%3D39457E%26logo%3Dperl%26logoColor%3DFFFFFF)

Instalacion

```


# MacOS (via Homebrew)
brew Instalacion diff-so-fancy

# Arch Linux
sudo pacman -S diff-so-fancy

# Debian / Ubuntu
sudo apt Instalacion diff-so-fancy


```

___

### [](https://dev.to/lissy93/cli-tools-you-cant-live-without-57f6#-raw-entr-endraw-watch-for-changes)[`entr`](https://github.com/eradman/entr) - Esté atento a los cambios

> `entr` le permite ejecutar un comando arbitrario cada vez que un archivo cambia. Puedes pasar un archivo, directorio, enlace simbólico o regex para especificar qué archivos debe vigilar. Es realmente útil para reconstruir proyectos automáticamente, reaccionar a logs, pruebas automatizadas, etc. A diferencia de otros proyectos similares, utiliza kqueue(2) o inotify(7) para evitar el sondeo y mejorar el rendimiento.

[![entr-example-usage](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Farticles%2F414s8q5lrqtpm9lhpwd4.png)](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Farticles%2F414s8q5lrqtpm9lhpwd4.png)

[![Ver entr en Github](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fimg.shields.io%2Fgithub%2Fstars%2Feradman%2Fentr%3Fcolor%3D232323%26label%3Dentr%26logo%3Dgithub%26labelColor%3D232323)](https://github.com/eradman/entr) [![Autor eradman](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fimg.shields.io%2Fbadge%2Feradman-b820f9%3FlabelColor%3Db820f9%26logo%3Dgithubsponsors%26logoColor%3Dfff)](https://github.com/eradman) [![Escrito en C](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fimg.shields.io%2Fstatic%2Fv1%3Flabel%3D%26message%3DC%26color%3DA8B9CC%26logo%3Dc%26logoColor%3DFFFFFF)](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fimg.shields.io%2Fstatic%2Fv1%3Flabel%3D%26message%3DC%26color%3DA8B9CC%26logo%3Dc%26logoColor%3DFFFFFF)

Instalacion

```


# MacOS (via Homebrew)
brew Instalacion entr

# Arch Linux
sudo pacman -S entr

# Debian / Ubuntu
sudo apt Instalacion entr


```

___

### [](https://dev.to/lissy93/cli-tools-you-cant-live-without-57f6#-raw-exiftool-endraw-reading-writing-metadata)[`exiftool`](https://github.com/exiftool/exiftool) - Lectura y escritura de metadatos

> ExifTool es una práctica utilidad para leer, escribir, eliminar y crear metainformación para una amplia variedad de tipos de archivos. No vuelva a filtrar accidentalmente su ubicación al compartir una foto.

[![exiftool-example-usage](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Farticles%2Fthmzq7zswauycd3rr9ki.png)](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Farticles%2Fthmzq7zswauycd3rr9ki.png)

[![Ver exiftool en Github](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fimg.shields.io%2Fgithub%2Fstars%2Fexiftool%2Fexiftool%3Fcolor%3D232323%26label%3Dexiftool%26logo%3Dgithub%26labelColor%3D232323)](https://github.com/exiftool/exiftool) [![Autor exiftool](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fimg.shields.io%2Fbadge%2Fexiftool-b820f9%3FlabelColor%3Db820f9%26logo%3Dgithubsponsors%26logoColor%3Dfff)](https://github.com/exiftool) [![Escrito en Perl](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fimg.shields.io%2Fstatic%2Fv1%3Flabel%3D%26message%3DPerl%26color%3D39457E%26logo%3Dperl%26logoColor%3DFFFFFF)](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fimg.shields.io%2Fstatic%2Fv1%3Flabel%3D%26message%3DPerl%26color%3D39457E%26logo%3Dperl%26logoColor%3DFFFFFF)

___

### [](https://dev.to/lissy93/cli-tools-you-cant-live-without-57f6#-raw-fdupes-endraw-duplicate-file-finder)[`fdupes`](https://github.com/jbruchon/jdupes) - Buscador de archivos duplicados

> `jdupes` se utiliza para identificar y/o eliminar archivos duplicados dentro de directorios especificados. Es útil para liberar espacio en disco cuando tiene dos o más archivos idénticos.

[![fdupes-example-usage](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Farticles%2Fy2w432abh09dpel0olro.png)](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Farticles%2Fy2w432abh09dpel0olro.png)

[![Ver jdupes en Github](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fimg.shields.io%2Fgithub%2Fstars%2Fjbruchon%2Fjdupes%3Fcolor%3D232323%26label%3Djdupes%26logo%3Dgithub%26labelColor%3D232323)](https://github.com/jbruchon/jdupes) [![Autor jbruchon](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fimg.shields.io%2Fbadge%2Fjbruchon-b820f9%3FlabelColor%3Db820f9%26logo%3Dgithubsponsors%26logoColor%3Dfff)](https://github.com/jbruchon) [![Escrito en C](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fimg.shields.io%2Fstatic%2Fv1%3Flabel%3D%26message%3DC%26color%3DA8B9CC%26logo%3Dc%26logoColor%3DFFFFFF)](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fimg.shields.io%2Fstatic%2Fv1%3Flabel%3D%26message%3DC%26color%3DA8B9CC%26logo%3Dc%26logoColor%3DFFFFFF)

___

### [](https://dev.to/lissy93/cli-tools-you-cant-live-without-57f6#-raw-fzf-endraw-fuzzy-file-finder-better-raw-find-endraw-)[`fzf`](https://github.com/junegunn/fzf) - Buscador de archivos difuso _(mejor `find`)_

> `fzf` es un buscador de archivos difusos y una herramienta de filtrado extremadamente potente y fácil de usar. También tiene [plugins](https://github.com/junegunn/fzf/wiki/Related-projects) disponibles para la mayoría de los shells e IDEs, para mostrar resultados instantáneos durante la búsqueda. Este [post](https://www.freecodecamp.org/news/fzf-a-command-line-fuzzy-finder-missing-demo-a7de312403ff/) de Alexey Samoshkin destaca algunos de sus casos de uso.

[![fzf-example-usage](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Farticles%2Fe3mmtc4oero27c4nfwes.gif)](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Farticles%2Fe3mmtc4oero27c4nfwes.gif)

[![Ver fzf en Github](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fimg.shields.io%2Fgithub%2Fstars%2Fjunegunn%2Ffzf%3Fcolor%3D232323%26label%3Dfzf%26logo%3Dgithub%26labelColor%3D232323)](https://github.com/junegunn/fzf) [![Autor junegunn](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fimg.shields.io%2Fbadge%2Fjunegunn-b820f9%3FlabelColor%3Db820f9%26logo%3Dgithubsponsors%26logoColor%3Dfff)](https://github.com/junegunn) [![Escrito en Go](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fimg.shields.io%2Fstatic%2Fv1%3Flabel%3D%26message%3DGo%2520Lang%26color%3D00ADD8%26logo%3Dgo%26logoColor%3DFFFFFF)](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fimg.shields.io%2Fstatic%2Fv1%3Flabel%3D%26message%3DGo%2520Lang%26color%3D00ADD8%26logo%3Dgo%26logoColor%3DFFFFFF)

Instalacion

```


# MacOS (via Homebrew)
brew Instalacion fzf

# Arch Linux
sudo pacman -S fzf

# Debian / Ubuntu
sudo apt Instalacion fzf


```

___

### [](https://dev.to/lissy93/cli-tools-you-cant-live-without-57f6#-raw-hyperfine-endraw-command-benchmarking)[`hyperfine`](https://github.com/sharkdp/hyperfine) - Evaluación comparativa de mandos

>`hyperfine` facilita la evaluación comparativa precisa de comandos o scripts arbitrarios. Se encarga de las ejecuciones de calentamiento, de limpiar la caché para obtener resultados precisos y de evitar interferencias de otros programas. También puede exportar los resultados como datos sin procesar y generar gráficos.

[![hyperfine-example-usage](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Farticles%2Fo7ttudho3xuwtb9v9v6h.png)](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Farticles%2Fo7ttudho3xuwtb9v9v6h.png)

[![Ver hyperfine en Github](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fimg.shields.io%2Fgithub%2Fstars%2Fsharkdp%2Fhyperfine%3Fcolor%3D232323%26label%3Dhyperfine%26logo%3Dgithub%26labelColor%3D232323)](https://github.com/sharkdp/hyperfine) [![Autor sharkdp](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fimg.shields.io%2Fbadge%2Fsharkdp-b820f9%3FlabelColor%3Db820f9%26logo%3Dgithubsponsors%26logoColor%3Dfff)](https://github.com/sharkdp) [![Escrito en Rust](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fimg.shields.io%2Fstatic%2Fv1%3Flabel%3D%26message%3DRust%26color%3De86243%26logo%3Drust%26logoColor%3DFFFFFF)](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fimg.shields.io%2Fstatic%2Fv1%3Flabel%3D%26message%3DRust%26color%3De86243%26logo%3Drust%26logoColor%3DFFFFFF)

Instalacion

```


# MacOS (via Homebrew)
brew Instalacion hyperfine

# Arch Linux
sudo pacman -S hyperfine

# Debian / Ubuntu
sudo apt Instalacion hyperfine


```

___

### [](https://dev.to/lissy93/cli-tools-you-cant-live-without-57f6#-raw-just-endraw-modern-command-runner-better-raw-make-endraw-)[`just`](https://github.com/casey/just) - Corredor de comandos moderno _(mejor `make`)_

> `just` es similar a `make` pero con algunas buenas adiciones. Te permite agrupar los comandos de tus proyectos en recopilaciones, que pueden ser fácilmente listadas y ejecutadas. Soporta alias, argumentos posicionales, diferentes shells, integración dot env, interprulación de cadenas, y casi todo lo que puedas necesitar.

[![Ver just en Github](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fimg.shields.io%2Fgithub%2Fstars%2Fcasey%2Fjust%3Fcolor%3D232323%26label%3Djust%26logo%3Dgithub%26labelColor%3D232323)](https://github.com/casey/just) [![Autor casey](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fimg.shields.io%2Fbadge%2Fcasey-b820f9%3FlabelColor%3Db820f9%26logo%3Dgithubsponsors%26logoColor%3Dfff)](https://github.com/casey) [![Escrito en Rust](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fimg.shields.io%2Fstatic%2Fv1%3Flabel%3D%26message%3DRust%26color%3De86243%26logo%3Drust%26logoColor%3DFFFFFF)](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fimg.shields.io%2Fstatic%2Fv1%3Flabel%3D%26message%3DRust%26color%3De86243%26logo%3Drust%26logoColor%3DFFFFFF)

Instalacion

```


# MacOS (via Homebrew)
brew Instalacion just

# Arch Linux
sudo pacman -S just

# Debian / Ubuntu
sudo apt Instalacion just


```

___

### [](https://dev.to/lissy93/cli-tools-you-cant-live-without-57f6#-raw-jq-endraw-json-processor)[`jq`](https://github.com/stedolan/jq) - Procesador JSON

> `jq` es como `sed`, pero para JSON - puedes usarlo para cortar y filtrar y mapear y transformar datos estructurados con facilidad. Se puede utilizar para escribir consultas complejas para extraer o manipular datos JSON. También hay un [jq playground](https://jqplay.org/) que puedes usar para probarlo, o formular consultas con información en tiempo real.

[![Ver jq en Github](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fimg.shields.io%2Fgithub%2Fstars%2Fstedolan%2Fjq%3Fcolor%3D232323%26label%3Djq%26logo%3Dgithub%26labelColor%3D232323)](https://github.com/stedolan/jq) [![Autor stedolan](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fimg.shields.io%2Fbadge%2Fstedolan-b820f9%3FlabelColor%3Db820f9%26logo%3Dgithubsponsors%26logoColor%3Dfff)](https://github.com/stedolan) [![Escrito en C](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fimg.shields.io%2Fstatic%2Fv1%3Flabel%3D%26message%3DC%26color%3DA8B9CC%26logo%3Dc%26logoColor%3DFFFFFF)](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fimg.shields.io%2Fstatic%2Fv1%3Flabel%3D%26message%3DC%26color%3DA8B9CC%26logo%3Dc%26logoColor%3DFFFFFF)

___

### [](https://dev.to/lissy93/cli-tools-you-cant-live-without-57f6#-raw-most-endraw-multiwindow-scroll-pager-better-less)[`most`](https://www.jedsoft.org/most/) - Localizador de desplazamiento multiventana _(mejor less)_

> `most` es un paginador, para leer archivos largos o salidas de comandos. `most` soporta multi-ventanas y tiene la opción de no ajustar el texto.

[![Autor Jed](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fimg.shields.io%2Fbadge%2Fjed-b820f9%3FlabelColor%3Db820f9%26logo%3Dgithubsponsors%26logoColor%3Dfff)](https://www.jedsoft.org/aboutme.html) [![Escrito en S-Lang](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fimg.shields.io%2Fstatic%2Fv1%3Flabel%3D%26message%3DS_Lang%26color%3D000000%26logo%3Dsimkl%26logoColor%3DFFFFFF)](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fimg.shields.io%2Fstatic%2Fv1%3Flabel%3D%26message%3DS_Lang%26color%3D000000%26logo%3Dsimkl%26logoColor%3DFFFFFF)

___

### [](https://dev.to/lissy93/cli-tools-you-cant-live-without-57f6#-raw-procs-endraw-process-viewer-better-ps)[`procs`](https://github.com/dalance/procs) - Visor de procesos _(mejor ps)_

> `procs` es un visor de procesos fácil de navegar, tiene resaltado de color, facilita la clasificación y búsqueda de procesos, tiene árbol Ver y se actualiza en tiempo real.

![procs-example-usage](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Farticles%2F66aux8de5ayqzdjxeu7b.gif)

[![Ver procs en Github](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fimg.shields.io%2Fgithub%2Fstars%2Fdalance%2Fprocs%3Fcolor%3D232323%26label%3Dprocs%26logo%3Dgithub%26labelColor%3D232323)](https://github.com/dalance/procs) [![Autor dalance](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fimg.shields.io%2Fbadge%2Fdalance-b820f9%3FlabelColor%3Db820f9%26logo%3Dgithubsponsors%26logoColor%3Dfff)](https://github.com/dalance) [![Escrito en Rust](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fimg.shields.io%2Fstatic%2Fv1%3Flabel%3D%26message%3DRust%26color%3De86243%26logo%3Drust%26logoColor%3DFFFFFF)](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fimg.shields.io%2Fstatic%2Fv1%3Flabel%3D%26message%3DRust%26color%3De86243%26logo%3Drust%26logoColor%3DFFFFFF)

___

### [](https://dev.to/lissy93/cli-tools-you-cant-live-without-57f6#-raw-rip-endraw-deletion-tool-better-rm)[`rip`](https://github.com/nivekuil/rip) - Herramienta de borrado _(mejor rm)_

> `rip` es una herramienta de borrado segura, ergonómica y eficaz. Le permite eliminar archivos y directorios de forma intuitiva y restaurar fácilmente los archivos eliminados.

[![rip-example-usage](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fi.ibb.co%2F10DTvT2%2Frip.gif)](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fi.ibb.co%2F10DTvT2%2Frip.gif)

[![Ver rip en Github](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fimg.shields.io%2Fgithub%2Fstars%2Fnivekuil%2Frip%3Fcolor%3D232323%26label%3Drip%26logo%3Dgithub%26labelColor%3D232323)](https://github.com/nivekuil/rip) [![Autor nivekuil](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fimg.shields.io%2Fbadge%2Fnivekuil-b820f9%3FlabelColor%3Db820f9%26logo%3Dgithubsponsors%26logoColor%3Dfff)](https://github.com/nivekuil) [![Escrito en Rust](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fimg.shields.io%2Fstatic%2Fv1%3Flabel%3D%26message%3DRust%26color%3De86243%26logo%3Drust%26logoColor%3DFFFFFF)](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fimg.shields.io%2Fstatic%2Fv1%3Flabel%3D%26message%3DRust%26color%3De86243%26logo%3Drust%26logoColor%3DFFFFFF)

___

### [](https://dev.to/lissy93/cli-tools-you-cant-live-without-57f6#-raw-ripgrep-endraw-search-within-files-better-raw-grep-endraw-)[`ripgrep`](https://github.com/BurntSushi/ripgrep) - Búsqueda dentro de archivos _(mejor `grep`)_

> `ripgrep` es una herramienta de búsqueda orientada a líneas que busca recursivamente un patrón regex en el directorio actual. Puede ignorar el contenido de `.gitignore` y omitir archivos binarios. Es capaz de buscar dentro de archivos comprimidos, o sólo buscar en una extensión específica, y entiende los archivos que utilizan varios métodos de codificación

[![ripgrep-example-usage](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Farticles%2Fxbmr38l5sfeynfy4yu1l.png)](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Farticles%2Fxbmr38l5sfeynfy4yu1l.png)

[![Ver ripgrep en Github](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fimg.shields.io%2Fgithub%2Fstars%2FBurntSushi%2Fripgrep%3Fcolor%3D232323%26label%3Dripgrep%26logo%3Dgithub%26labelColor%3D232323)](https://github.com/BurntSushi/ripgrep) [![Autor BurntSushi](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fimg.shields.io%2Fbadge%2FBurntSushi-b820f9%3FlabelColor%3Db820f9%26logo%3Dgithubsponsors%26logoColor%3Dfff)](https://github.com/BurntSushi) [![Escrito en Rust](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fimg.shields.io%2Fstatic%2Fv1%3Flabel%3D%26message%3DRust%26color%3De86243%26logo%3Drust%26logoColor%3DFFFFFF)](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fimg.shields.io%2Fstatic%2Fv1%3Flabel%3D%26message%3DRust%26color%3De86243%26logo%3Drust%26logoColor%3DFFFFFF)

___

### [](https://dev.to/lissy93/cli-tools-you-cant-live-without-57f6#-raw-rsync-endraw-fast-incremental-file-transfer)[`rsync`](https://rsync.samba.org/) - Transferencia rápida e incremental de archivos

> `rsync` te permite copiar archivos grandes localmente o desde o hacia hosts remotos o unidades externas. Puede utilizarse para mantener sincronizados archivos de varias ubicaciones y es perfecto para crear, actualizar y restaurar copias de seguridad.

[![Ver rsync en Github](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fimg.shields.io%2Fgithub%2Fstars%2FWayneD%2Frsync%3Fcolor%3D232323%26label%3Drsync%26logo%3Dgithub%26labelColor%3D232323)](https://github.com/WayneD/rsync) [![Autor WayneD](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fimg.shields.io%2Fbadge%2FWayneD-b820f9%3FlabelColor%3Db820f9%26logo%3Dgithubsponsors%26logoColor%3Dfff)](https://github.com/WayneD) [![Escrito en C](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fimg.shields.io%2Fstatic%2Fv1%3Flabel%3D%26message%3DC%26color%3DA8B9CC%26logo%3Dc%26logoColor%3DFFFFFF)](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fimg.shields.io%2Fstatic%2Fv1%3Flabel%3D%26message%3DC%26color%3DA8B9CC%26logo%3Dc%26logoColor%3DFFFFFF)

___

### [](https://dev.to/lissy93/cli-tools-you-cant-live-without-57f6#-raw-sd-endraw-find-and-replace-better-raw-sed-endraw-)[`sd`](https://github.com/chmln/sd) - Buscar y reemplazar _(mejor `sed`)_
> `sd` es una herramienta de búsqueda y reemplazo fácil, rápida e intuitiva, basada en literales de cadena. Puede ejecutarse sobre un fichero, un directorio entero o cualquier texto canalizado.

[![sd-example-usage](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Farticles%2Fu1nd67tliy5l7b34r21r.png)](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Farticles%2Fu1nd67tliy5l7b34r21r.png)

[![Ver sd en Github](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fimg.shields.io%2Fgithub%2Fstars%2Fchmln%2Fsd%3Fcolor%3D232323%26label%3Dsd%26logo%3Dgithub%26labelColor%3D232323)](https://github.com/chmln/sd) [![Autor chmln](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fimg.shields.io%2Fbadge%2Fchmln-b820f9%3FlabelColor%3Db820f9%26logo%3Dgithubsponsors%26logoColor%3Dfff)](https://github.com/chmln) [![Escrito en Rust](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fimg.shields.io%2Fstatic%2Fv1%3Flabel%3D%26message%3DRust%26color%3De86243%26logo%3Drust%26logoColor%3DFFFFFF)](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fimg.shields.io%2Fstatic%2Fv1%3Flabel%3D%26message%3DRust%26color%3De86243%26logo%3Drust%26logoColor%3DFFFFFF)

___

### [](https://dev.to/lissy93/cli-tools-you-cant-live-without-57f6#-raw-tre-endraw-directory-hierarchy-better-raw-tree-endraw-)[`tre`](https://github.com/dduan/tre) - Jerarquía de directorios _(mejor `tree`)_

> `tre` muestra una lista de archivos en forma de árbol para tu directorio actual o uno especificado, con colores. Al ejecutarlo con la opción `-e`, numera cada elemento y crea un alias temporal que puedes usar para saltar rápidamente a esa ubicación

[![tre-example-usage](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Farticles%2F5dl6kxdum67xexkztr8d.png)](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Farticles%2F5dl6kxdum67xexkztr8d.png)

[![Ver tre en Github](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fimg.shields.io%2Fgithub%2Fstars%2Fdduan%2Ftre%3Fcolor%3D232323%26label%3Dtre%26logo%3Dgithub%26labelColor%3D232323)](https://github.com/dduan/tre) [![Autor dduan](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fimg.shields.io%2Fbadge%2Fdduan-b820f9%3FlabelColor%3Db820f9%26logo%3Dgithubsponsors%26logoColor%3Dfff)](https://github.com/dduan) [![Escrito en Rust](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fimg.shields.io%2Fstatic%2Fv1%3Flabel%3D%26message%3DRust%26color%3De86243%26logo%3Drust%26logoColor%3DFFFFFF)](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fimg.shields.io%2Fstatic%2Fv1%3Flabel%3D%26message%3DRust%26color%3De86243%26logo%3Drust%26logoColor%3DFFFFFF)

___

### [](https://dev.to/lissy93/cli-tools-you-cant-live-without-57f6#-raw-xsel-endraw-access-the-clipboard)[`xsel`](https://github.com/kfish/xsel) - Acceso al portapapeles

> `xsel` te permite leer y escribir en el portapapeles de selección X desde la línea de comandos. Es útil para enviar la salida de un comando al portapapeles o para pegar datos copiados en un comando.

[![Ver xsel en Github](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fimg.shields.io%2Fgithub%2Fstars%2Fkfish%2Fxsel%3Fcolor%3D232323%26label%3Dxsel%26logo%3Dgithub%26labelColor%3D232323)](https://github.com/kfish/xsel) [![Autor kfish](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fimg.shields.io%2Fbadge%2Fkfish-b820f9%3FlabelColor%3Db820f9%26logo%3Dgithubsponsors%26logoColor%3Dfff)](https://github.com/kfish) [![Escrito en C](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fimg.shields.io%2Fstatic%2Fv1%3Flabel%3D%26message%3DC%26color%3DA8B9CC%26logo%3Dc%26logoColor%3DFFFFFF)](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fimg.shields.io%2Fstatic%2Fv1%3Flabel%3D%26message%3DC%26color%3DA8B9CC%26logo%3Dc%26logoColor%3DFFFFFF)

___

## [](https://dev.to/lissy93/cli-tools-you-cant-live-without-57f6#cli-monitoring-and-performance-apps)CLI - Aplicaciones de monitorización y rendimiento 

### [](https://dev.to/lissy93/cli-tools-you-cant-live-without-57f6#-raw-bandwhich-endraw-bandwidth-utilization-monitor)[`bandwhich`](https://github.com/imsnif/bandwhich) - Monitor de utilización de ancho de banda

> Muestra el uso de ancho de banda, información de conexión, hosts salientes y consultas DNS en tiempo real

[![bandwhich-example-usage](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Farticles%2Fps64sac0bije443ql4ba.png)](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Farticles%2Fps64sac0bije443ql4ba.png)

[![Ver bandwhich en Github](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fimg.shields.io%2Fgithub%2Fstars%2Fimsnif%2Fbandwhich%3Fcolor%3D232323%26label%3Dbandwhich%26logo%3Dgithub%26labelColor%3D232323)](https://github.com/imsnif/bandwhich) [![Autor imsnif](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fimg.shields.io%2Fbadge%2Fimsnif-b820f9%3FlabelColor%3Db820f9%26logo%3Dgithubsponsors%26logoColor%3Dfff)](https://github.com/imsnif) [![Escrito en Rust](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fimg.shields.io%2Fstatic%2Fv1%3Flabel%3D%26message%3DRust%26color%3De86243%26logo%3Drust%26logoColor%3DFFFFFF)](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fimg.shields.io%2Fstatic%2Fv1%3Flabel%3D%26message%3DRust%26color%3De86243%26logo%3Drust%26logoColor%3DFFFFFF)

___

### [](https://dev.to/lissy93/cli-tools-you-cant-live-without-57f6#-raw-ctop-endraw-container-metrics-and-monitoring)[`ctop`](https://github.com/bcicen/ctop) - Métricas y monitoreo de contenedores

> Como `top`, pero para monitorear el uso de recursos de contenedores en ejecución (Docker y runC). Muestra CPU, memoria y ancho de banda de red en tiempo real, así como el nombre, estado e ID de cada contenedor. También incluye un visor de logs integrado y opciones para gestionar (detener, iniciar, ejecutar, etc.) contenedores.

[![ctop-example-usage](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Farticles%2Foq52gq649s5tfe6u2snx.gif)](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Farticles%2Foq52gq649s5tfe6u2snx.gif)

[![Ver ctop en Github](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fimg.shields.io%2Fgithub%2Fstars%2Fbcicen%2Fctop%3Fcolor%3D232323%26label%3Dctop%26logo%3Dgithub%26labelColor%3D232323)](https://github.com/bcicen/ctop) [![Autor bcicen](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fimg.shields.io%2Fbadge%2Fbcicen-b820f9%3FlabelColor%3Db820f9%26logo%3Dgithubsponsors%26logoColor%3Dfff)](https://github.com/bcicen) [![Escrito en Go](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fimg.shields.io%2Fstatic%2Fv1%3Flabel%3D%26message%3DGo%2520Lang%26color%3D00ADD8%26logo%3Dgo%26logoColor%3DFFFFFF)](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fimg.shields.io%2Fstatic%2Fv1%3Flabel%3D%26message%3DGo%2520Lang%26color%3D00ADD8%26logo%3Dgo%26logoColor%3DFFFFFF)

___

### [](https://dev.to/lissy93/cli-tools-you-cant-live-without-57f6#-raw-bpytop-endraw-resource-monitoring-better-raw-htop-endraw-)[`bpytop`](https://github.com/aristocratos/bpytop) - Monitoreo de recursos _(mejor `htop`)_

> `bpytop` es un monitor de recursos rápido, interactivo y visual. Muestra los procesos principales en ejecución, el historial reciente de CPU, memoria, disco y red. Desde la interfaz puedes navegar, ordenar y buscar; también hay soporte para temas de color personalizados.

[![bpytop-example-usage](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Farticles%2Fdp97y4vlwmqstfr0yyg3.gif)](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Farticles%2Fdp97y4vlwmqstfr0yyg3.gif)

[![Ver bpytop en Github](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fimg.shields.io%2Fgithub%2Fstars%2Faristocratos%2Fbpytop%3Fcolor%3D232323%26label%3Dbpytop%26logo%3Dgithub%26labelColor%3D232323)](https://github.com/aristocratos/bpytop) [![Autor aristocratos](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fimg.shields.io%2Fbadge%2Faristocratos-b820f9%3FlabelColor%3Db820f9%26logo%3Dgithubsponsors%26logoColor%3Dfff)](https://github.com/aristocratos) [![Escrito en Python](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fimg.shields.io%2Fstatic%2Fv1%3Flabel%3D%26message%3DPython%26color%3D3C78A9%26logo%3Dpython%26logoColor%3DFFFFFF)](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fimg.shields.io%2Fstatic%2Fv1%3Flabel%3D%26message%3DPython%26color%3D3C78A9%26logo%3Dpython%26logoColor%3DFFFFFF)

___

### [](https://dev.to/lissy93/cli-tools-you-cant-live-without-57f6#-raw-glances-endraw-resource-monitor-web-and-api)[`glances`](https://github.com/nicolargo/glances) - Monitor de recursos + web y API

> `glances` es otro monitor de recursos, pero con un conjunto de características diferente. Incluye una vista web totalmente responsiva, una API REST y monitoreo histórico. Es fácilmente extensible y puede integrarse con otros servicios.

[![glances-example-usage](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Farticles%2F77lyqbdf6pcjolhjk0oi.gif)](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Farticles%2F77lyqbdf6pcjolhjk0oi.gif)

[![Ver glances en Github](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fimg.shields.io%2Fgithub%2Fstars%2Fnicolargo%2Fglances%3Fcolor%3D232323%26label%3Dglances%26logo%3Dgithub%26labelColor%3D232323)](https://github.com/nicolargo/glances) [![Autor nicolargo](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fimg.shields.io%2Fbadge%2Fnicolargo-b820f9%3FlabelColor%3Db820f9%26logo%3Dgithubsponsors%26logoColor%3Dfff)](https://github.com/nicolargo) [![Escrito en Python](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fimg.shields.io%2Fstatic%2Fv1%3Flabel%3D%26message%3DPython%26color%3D3C78A9%26logo%3Dpython%26logoColor%3DFFFFFF)](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fimg.shields.io%2Fstatic%2Fv1%3Flabel%3D%26message%3DPython%26color%3D3C78A9%26logo%3Dpython%26logoColor%3DFFFFFF)

___

### [](https://dev.to/lissy93/cli-tools-you-cant-live-without-57f6#-raw-gping-endraw-interactive-ping-tool-better-raw-ping-endraw-)[`gping`](https://github.com/orf/gping) - Herramienta de ping interactiva _(mejor `ping`)_

> `gping` puede ejecutar pruebas de ping en varios hosts, mostrando los resultados en un gráfico en tiempo real. También puede usarse para monitorear el tiempo de ejecución, cuando se usa con la opción `--cmd`.

[![gping-example-usage](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Farticles%2Fnpgzre8kagt1j6yzy4uc.gif)](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Farticles%2Fnpgzre8kagt1j6yzy4uc.gif)

[![Ver gping en Github](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fimg.shields.io%2Fgithub%2Fstars%2Forf%2Fgping%3Fcolor%3D232323%26label%3Dgping%26logo%3Dgithub%26labelColor%3D232323)](https://github.com/orf/gping) [![Autor orf](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fimg.shields.io%2Fbadge%2Forf-b820f9%3FlabelColor%3Db820f9%26logo%3Dgithubsponsors%26logoColor%3Dfff)](https://github.com/orf) [![Escrito en Rust](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fimg.shields.io%2Fstatic%2Fv1%3Flabel%3D%26message%3DRust%26color%3De86243%26logo%3Drust%26logoColor%3DFFFFFF)](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fimg.shields.io%2Fstatic%2Fv1%3Flabel%3D%26message%3DRust%26color%3De86243%26logo%3Drust%26logoColor%3DFFFFFF)

___

### [](https://dev.to/lissy93/cli-tools-you-cant-live-without-57f6#-raw-duacli-endraw-disk-usage-analyzer-and-monitor-better-raw-du-endraw-)[`dua-cli`](https://github.com/Byron/dua-cli) - Analizador y monitor de uso de disco _(mejor `du`)_

> `dua-cli` te permite ver de forma interactiva el espacio usado y disponible en cada unidad montada, y facilita liberar almacenamiento.

[![dua-cli-usage-example](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Farticles%2F3c46q1bh8qdfvy5s1sm6.gif)](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Farticles%2F3c46q1bh8qdfvy5s1sm6.gif)

[![Ver dua-cli en Github](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fimg.shields.io%2Fgithub%2Fstars%2FByron%2Fdua-cli%3Fcolor%3D232323%26label%3Ddua-cli%26logo%3Dgithub%26labelColor%3D232323)](https://github.com/Byron/dua-cli) [![Autor Byron](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fimg.shields.io%2Fbadge%2FByron-b820f9%3FlabelColor%3Db820f9%26logo%3Dgithubsponsors%26logoColor%3Dfff)](https://github.com/Byron) [![Escrito en Rust](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fimg.shields.io%2Fstatic%2Fv1%3Flabel%3D%26message%3DRust%26color%3De86243%26logo%3Drust%26logoColor%3DFFFFFF)](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fimg.shields.io%2Fstatic%2Fv1%3Flabel%3D%26message%3DRust%26color%3De86243%26logo%3Drust%26logoColor%3DFFFFFF)

___

### [](https://dev.to/lissy93/cli-tools-you-cant-live-without-57f6#-raw-speedtestcli-endraw-command-line-speed-test-utility)[`speedtest-cli`](https://github.com/sivel/speedtest-cli) - Utilidad de prueba de velocidad en línea de comandos

> `speedtest-cli` simplemente ejecuta una prueba de velocidad de internet, usando speedtest.net, pero directamente desde la terminal :)

[![speedtest-cli-example-usage](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Farticles%2Femb2z6s2wovmtywb3lcz.gif)](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Farticles%2Femb2z6s2wovmtywb3lcz.gif)

[![Ver speedtest-cli en Github](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fimg.shields.io%2Fgithub%2Fstars%2Fsivel%2Fspeedtest-cli%3Fcolor%3D232323%26label%3Dspeedtest-cli%26logo%3Dgithub%26labelColor%3D232323)](https://github.com/sivel/speedtest-cli) [![Autor sivel](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fimg.shields.io%2Fbadge%2Fsivel-b820f9%3FlabelColor%3Db820f9%26logo%3Dgithubsponsors%26logoColor%3Dfff)](https://github.com/sivel) [![Escrito en Python](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fimg.shields.io%2Fstatic%2Fv1%3Flabel%3D%26message%3DPython%26color%3D3C78A9%26logo%3Dpython%26logoColor%3DFFFFFF)](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fimg.shields.io%2Fstatic%2Fv1%3Flabel%3D%26message%3DPython%26color%3D3C78A9%26logo%3Dpython%26logoColor%3DFFFFFF)

___

### [](https://dev.to/lissy93/cli-tools-you-cant-live-without-57f6#-raw-dog-endraw-dns-lookup-client-better-raw-dig-endraw-)[`dog`](https://github.com/ogham/dog) - Cliente de búsqueda DNS _(mejor `dig`)_

> `dog` es un cliente de búsqueda DNS fácil de usar, con soporte para DoT y DoH, salidas coloridas y la opción de emitir JSON.

[![dog-example-usage](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Farticles%2Fpym49mhc8gsbgx0u89da.png)](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Farticles%2Fpym49mhc8gsbgx0u89da.png)

[![Ver dog en Github](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fimg.shields.io%2Fgithub%2Fstars%2Fogham%2Fdog%3Fcolor%3D232323%26label%3Ddog%26logo%3Dgithub%26labelColor%3D232323)](https://github.com/ogham/dog) [![Autor ogham](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fimg.shields.io%2Fbadge%2Fogham-b820f9%3FlabelColor%3Db820f9%26logo%3Dgithubsponsors%26logoColor%3Dfff)](https://github.com/ogham) [![Escrito en Rust](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fimg.shields.io%2Fstatic%2Fv1%3Flabel%3D%26message%3DRust%26color%3De86243%26logo%3Drust%26logoColor%3DFFFFFF)](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fimg.shields.io%2Fstatic%2Fv1%3Flabel%3D%26message%3DRust%26color%3De86243%26logo%3Drust%26logoColor%3DFFFFFF)

___

## [](https://dev.to/lissy93/cli-tools-you-cant-live-without-57f6#productividad-cli)CLI Productividad

> Navega por la web, escucha música, revisa correos, gestiona calendarios, lee noticias y más, ¡todo sin salir de la terminal!

### [](https://dev.to/lissy93/cli-tools-you-cant-live-without-57f6#browsh---navegador-web-cli)[`browsh`](https://github.com/browsh-org/browsh) - Navegador web CLI

> `browsh` es un navegador de texto moderno, interactivo y en tiempo real, renderizado para TTYs y navegadores. Soporta navegación tanto con ratón como con teclado, y tiene muchas más funciones de lo que esperarías para una aplicación puramente de terminal. Además, ayuda a reducir el consumo de batería que afecta a los navegadores modernos y, con soporte para MoSH, puedes experimentar tiempos de carga más rápidos gracias al menor uso de ancho de banda.

![browsh-example-usage](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Farticles%2F8wk8p8i33telyx5li3t4.gif)

[![Ver browsh en Github](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fimg.shields.io%2Fgithub%2Fstars%2Fbrowsh-org%2Fbrowsh%3Fcolor%3D232323%26label%3Dbrowsh%26logo%3Dgithub%26labelColor%3D232323)](https://github.com/browsh-org/browsh) [![Autor browsh-org](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fimg.shields.io%2Fbadge%2Fbrowsh-org-b820f9%3FlabelColor%3Db820f9%26logo%3Dgithubsponsors%26logoColor%3Dfff)](https://github.com/browsh-org) [![Escrito en JavaScript](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fimg.shields.io%2Fstatic%2Fv1%3Flabel%3D%26message%3DJavaScript%26color%3DF7DF1E%26logo%3Djavascript%26logoColor%3DFFFFFF)](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fimg.shields.io%2Fstatic%2Fv1%3Flabel%3D%26message%3DJavaScript%26color%3DF7DF1E%26logo%3Djavascript%26logoColor%3DFFFFFF)

___

### [](https://dev.to/lissy93/cli-tools-you-cant-live-without-57f6#buku---gestor-de-marcadores)[`buku`](https://github.com/jarun/buku) - Gestor de marcadores

> `buku` es un gestor de marcadores para terminal, con muchas opciones de configuración, almacenamiento y uso. También dispone de una [interfaz web opcional](https://github.com/jarun/buku/tree/master/bukuserver#screenshots) y un [plugin para navegador](https://github.com/samhh/bukubrow-webext#installation) para acceder a tus marcadores fuera de la terminal.

[![buku-example-usage](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Farticles%2Fi3sdudxkh620u0e19bu3.png)](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Farticles%2Fi3sdudxkh620u0e19bu3.png)

[![Ver buku en Github](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fimg.shields.io%2Fgithub%2Fstars%2Fjarun%2Fbuku%3Fcolor%3D232323%26label%3Dbuku%26logo%3Dgithub%26labelColor%3D232323)](https://github.com/jarun/buku) [![Autor jarun](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fimg.shields.io%2Fbadge%2Fjarun-b820f9%3FlabelColor%3Db820f9%26logo%3Dgithubsponsors%26logoColor%3Dfff)](https://github.com/jarun) [![Escrito en Python](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fimg.shields.io%2Fstatic%2Fv1%3Flabel%3D%26message%3DPython%26color%3D3C78A9%26logo%3Dpython%26logoColor%3DFFFFFF)](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fimg.shields.io%2Fstatic%2Fv1%3Flabel%3D%26message%3DPython%26color%3D3C78A9%26logo%3Dpython%26logoColor%3DFFFFFF)

___

### [](https://dev.to/lissy93/cli-tools-you-cant-live-without-57f6#cmus---reproductor--navegador-de-musica)[`cmus`](https://github.com/cmus/cmus) - Reproductor / navegador de música

> `cmus` es un reproductor de música para terminal, controlado con atajos de teclado. Soporta una amplia gama de formatos y códecs de audio, y permite organizar pistas en listas de reproducción y aplicar configuraciones de reproducción.

[![cmus-example-usage](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Farticles%2F3x53mxo9ynnflesyk6xr.png)](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Farticles%2F3x53mxo9ynnflesyk6xr.png)

[![Ver cmus en Github](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fimg.shields.io%2Fgithub%2Fstars%2Fcmus%2Fcmus%3Fcolor%3D232323%26label%3Dcmus%26logo%3Dgithub%26labelColor%3D232323)](https://github.com/cmus/cmus) [![Autor cmus](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fimg.shields.io%2Fbadge%2Fcmus-b820f9%3FlabelColor%3Db820f9%26logo%3Dgithubsponsors%26logoColor%3Dfff)](https://github.com/cmus) [![Escrito en C](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fimg.shields.io%2Fstatic%2Fv1%3Flabel%3D%26message%3DC%26color%3DA8B9CC%26logo%3Dc%26logoColor%3DFFFFFF)](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fimg.shields.io%2Fstatic%2Fv1%3Flabel%3D%26message%3DC%26color%3DA8B9CC%26logo%3Dc%26logoColor%3DFFFFFF)

___

### [](https://dev.to/lissy93/cli-tools-you-cant-live-without-57f6#cointop---seguimiento-de-precios-cripto)[`cointop`](https://github.com/cointop-sh/cointop) - Seguimiento de precios cripto

> `cointop` muestra los precios actuales de criptomonedas y el historial de precios de tu portafolio. Soporta alertas de precio, gráficos históricos, conversión de divisas, búsqueda difusa y mucho más. Puedes probar la demo en la web [cointop.sh](https://cointop.sh/) o ejecutando `ssh cointop.sh`.

[![cointop-example-usage](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Farticles%2Fo58mhjhmw0hzglbsy4tg.png)](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Farticles%2Fo58mhjhmw0hzglbsy4tg.png)

[![Ver cointop en Github](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fimg.shields.io%2Fgithub%2Fstars%2Fcointop-sh%2Fcointop%3Fcolor%3D232323%26label%3Dcointop%26logo%3Dgithub%26labelColor%3D232323)](https://github.com/cointop-sh/cointop) [![Autor cointop-sh](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fimg.shields.io%2Fbadge%2Fcointop-sh-b820f9%3FlabelColor%3Db820f9%26logo%3Dgithubsponsors%26logoColor%3Dfff)](https://github.com/cointop-sh) [![Escrito en Go](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fimg.shields.io%2Fstatic%2Fv1%3Flabel%3D%26message%3DGo%2520Lang%26color%3D00ADD8%26logo%3Dgo%26logoColor%3DFFFFFF)](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fimg.shields.io%2Fstatic%2Fv1%3Flabel%3D%26message%3DGo%2520Lang%26color%3D00ADD8%26logo%3Dgo%26logoColor%3DFFFFFF)

___

### [](https://dev.to/lissy93/cli-tools-you-cant-live-without-57f6#ddgr---buscar-en-la-web-desde-terminal)[`ddgr`](https://github.com/jarun/ddgr) - Buscar en la web desde terminal

> `ddgr` es como [googler](https://github.com/jarun/googler), pero para DuckDuckGo. Es rápido, limpio y fácil, con soporte para respuestas instantáneas, autocompletado, bangs de búsqueda y búsqueda avanzada. Respeta tu privacidad por defecto, también tiene soporte para proxy HTTPS y funciona con Tor.

[![dggr-example-usage](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Farticles%2Fc25z80hclk61z2vrm5sp.png)](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Farticles%2Fc25z80hclk61z2vrm5sp.png)

[![Ver ddgr en Github](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fimg.shields.io%2Fgithub%2Fstars%2Fjarun%2Fddgr%3Fcolor%3D232323%26label%3Dddgr%26logo%3Dgithub%26labelColor%3D232323)](https://github.com/jarun/ddgr) [![Autor jarun](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fimg.shields.io%2Fbadge%2Fjarun-b820f9%3FlabelColor%3Db820f9%26logo%3Dgithubsponsors%26logoColor%3Dfff)](https://github.com/jarun) [![Escrito en Python](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fimg.shields.io%2Fstatic%2Fv1%3Flabel%3D%26message%3DPython%26color%3D3C78A9%26logo%3Dpython%26logoColor%3DFFFFFF)](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fimg.shields.io%2Fstatic%2Fv1%3Flabel%3D%26message%3DPython%26color%3D3C78A9%26logo%3Dpython%26logoColor%3DFFFFFF)

___


### [](https://dev.to/lissy93/cli-tools-you-cant-live-without-57f6#-raw-micro-endraw-code-editor-better-raw-nano-endraw-)[`micro`](https://github.com/zyedidia/micro) - Editor de código _(mejor `nano`)_

> `micro` es un editor de código fácil de usar, rápido y extensible, con soporte para ratón. Como viene en un solo binario, la instalación es tan simple como `curl https://getmic.ro | bash`.

[![micro-screenshot](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Farticles%2F5mqf1nz04pqx9wnr8ivj.png)](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Farticles%2F5mqf1nz04pqx9wnr8ivj.png)

[![Ver micro en Github](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fimg.shields.io%2Fgithub%2Fstars%2Fzyedidia%2Fmicro%3Fcolor%3D232323%26label%3Dmicro%26logo%3Dgithub%26labelColor%3D232323)](https://github.com/zyedidia/micro) [![Autor zyedidia](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fimg.shields.io%2Fbadge%2Fzyedidia-b820f9%3FlabelColor%3Db820f9%26logo%3Dgithubsponsors%26logoColor%3Dfff)](https://github.com/zyedidia) [![Escrito en Go](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fimg.shields.io%2Fstatic%2Fv1%3Flabel%3D%26message%3DGo%2520Lang%26color%3D00ADD8%26logo%3Dgo%26logoColor%3DFFFFFF)](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fimg.shields.io%2Fstatic%2Fv1%3Flabel%3D%26message%3DGo%2520Lang%26color%3D00ADD8%26logo%3Dgo%26logoColor%3DFFFFFF)

___

### [](https://dev.to/lissy93/cli-tools-you-cant-live-without-57f6#-raw-khal-endraw-calendar-client)[`khal`](https://github.com/pimutils/khal) - Cliente de Calendario

> `khal` es una aplicación de calendario para terminales, que muestra los próximos eventos, vistas del mes y de la agenda. Puedes sincronizarlo con cualquier calendario CalDAV, y añadir, editar y eliminar eventos directamente.

[![khal-example-usage](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Farticles%2Fh9rvj3xn074gt3r7wvct.png)](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Farticles%2Fh9rvj3xn074gt3r7wvct.png)

[![Ver khal en Github](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fimg.shields.io%2Fgithub%2Fstars%2Fpimutils%2Fkhal%3Fcolor%3D232323%26label%3Dkhal%26logo%3Dgithub%26labelColor%3D232323)](https://github.com/pimutils/khal) [![Autor pimutils](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fimg.shields.io%2Fbadge%2Fpimutils-b820f9%3FlabelColor%3Db820f9%26logo%3Dgithubsponsors%26logoColor%3Dfff)](https://github.com/pimutils) [![Escrito en Python](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fimg.shields.io%2Fstatic%2Fv1%3Flabel%3D%26message%3DPython%26color%3D3C78A9%26logo%3Dpython%26logoColor%3DFFFFFF)](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fimg.shields.io%2Fstatic%2Fv1%3Flabel%3D%26message%3DPython%26color%3D3C78A9%26logo%3Dpython%26logoColor%3DFFFFFF)

___

### [](https://dev.to/lissy93/cli-tools-you-cant-live-without-57f6#-raw-mutt-endraw-email-client)[`mutt`](https://gitlab.com/muttmua/mutt) - Cliente de Email

> `mut` es un cliente de correo clásico, basado en terminal, para enviar, leer y gestionar correos electrónicos. Soporta todos los principales protocolos de correo electrónico y formatos de buzón, permite archivos adjuntos, CCO/CC, hilos, listas de correo y notificaciones de estado de entrega.

[![mutt-example-usage](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fi.ibb.co%2FzVVsG3s%2Fmutt.webp)](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fi.ibb.co%2FzVVsG3s%2Fmutt.webp)

[![Ver mutt en Github](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fimg.shields.io%2Fgithub%2Fstars%2Fmuttmua%2Fmutt%3Fcolor%3D232323%26label%3Dmutt%26logo%3Dgithub%26labelColor%3D232323)](https://gitlab.com/muttmua/mutt) [![Autor muttmua](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fimg.shields.io%2Fbadge%2Fmuttmua-b820f9%3FlabelColor%3Db820f9%26logo%3Dgithubsponsors%26logoColor%3Dfff)](https://github.com/muttmua) [![Escrito en C](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fimg.shields.io%2Fstatic%2Fv1%3Flabel%3D%26message%3DC%26color%3DA8B9CC%26logo%3Dc%26logoColor%3DFFFFFF)](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fimg.shields.io%2Fstatic%2Fv1%3Flabel%3D%26message%3DC%26color%3DA8B9CC%26logo%3Dc%26logoColor%3DFFFFFF)

___

### [](https://dev.to/lissy93/cli-tools-you-cant-live-without-57f6#-raw-newsboat-endraw-rss-atom-news-reader)[`newsboat`](https://github.com/newsboat/newsboat) - Lector de noticias RSS / ATOM

> `newsboat` es un lector y agregador de feeds RSS, para leer las noticias, blogs y seguir las actualizaciones directamente desde el terminal.

[![newsboat-example-usage](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Farticles%2Fcdx7nffucs0vgubg1q4p.png)](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Farticles%2Fcdx7nffucs0vgubg1q4p.png)

[![Ver newsboat en Github](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fimg.shields.io%2Fgithub%2Fstars%2Fnewsboat%2Fnewsboat%3Fcolor%3D232323%26label%3Dnewsboat%26logo%3Dgithub%26labelColor%3D232323)](https://github.com/newsboat/newsboat) [![Autor newsboat](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fimg.shields.io%2Fbadge%2Fnewsboat-b820f9%3FlabelColor%3Db820f9%26logo%3Dgithubsponsors%26logoColor%3Dfff)](https://github.com/newsboat) [![Escrito en C++](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fimg.shields.io%2Fstatic%2Fv1%3Flabel%3D%26message%3DC%2B%2B%26color%3D00599C%26logo%3Dcplusplus%26logoColor%3DFFFFFF)](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fimg.shields.io%2Fstatic%2Fv1%3Flabel%3D%26message%3DC%2B%2B%26color%3D00599C%26logo%3Dcplusplus%26logoColor%3DFFFFFF)

___

### [](https://dev.to/lissy93/cli-tools-you-cant-live-without-57f6#-raw-rclone-endraw-manage-cloud-storage)[`rclone`](https://github.com/rclone/rclone) - Gestionar el almacenamiento en la nube

> `rclone` es una práctica utilidad para sincronizar archivos y carpetas con varios proveedores de almacenamiento en la nube. Puede invocarse directamente desde la línea de comandos o integrarse fácilmente en un script como sustituto de las pesadas aplicaciones de sincronización de escritorio.

[![Ver rclone en Github](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fimg.shields.io%2Fgithub%2Fstars%2Frclone%2Frclone%3Fcolor%3D232323%26label%3Drclone%26logo%3Dgithub%26labelColor%3D232323)](https://github.com/rclone/rclone) [![Autor rclone](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fimg.shields.io%2Fbadge%2Frclone-b820f9%3FlabelColor%3Db820f9%26logo%3Dgithubsponsors%26logoColor%3Dfff)](https://github.com/rclone) [![Escrito en Go](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fimg.shields.io%2Fstatic%2Fv1%3Flabel%3D%26message%3DGo%2520Lang%26color%3D00ADD8%26logo%3Dgo%26logoColor%3DFFFFFF)](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fimg.shields.io%2Fstatic%2Fv1%3Flabel%3D%26message%3DGo%2520Lang%26color%3D00ADD8%26logo%3Dgo%26logoColor%3DFFFFFF)

___

### [](https://dev.to/lissy93/cli-tools-you-cant-live-without-57f6#-raw-taskwarrior-endraw-todo-task-management)[`taskwarrior`](https://github.com/GothenburgBitFactory/taskwarrior) - Todo + gestión de tareas

> `task` es una aplicación CLI de gestión de tareas/todo. Es simple y discreta, pero también increíblemente potente y escalable, con funciones avanzadas de organización y consulta. También hay un montón (¡más de 700!) de [plugins] adicionales (https://taskwarrior.org/tools/) para ampliar su funcionalidad e integrarse con servicios de terceros.

[![task-warrior-example-usage](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Farticles%2Fa19870j5shovm8wa0540.jpg)](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Farticles%2Fa19870j5shovm8wa0540.jpg)

[![Ver taskwarrior en Github](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fimg.shields.io%2Fgithub%2Fstars%2FGothenburgBitFactory%2Ftaskwarrior%3Fcolor%3D232323%26label%3Dtaskwarrior%26logo%3Dgithub%26labelColor%3D232323)](https://github.com/GothenburgBitFactory/taskwarrior) [![Autor GothenburgBitFactory](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fimg.shields.io%2Fbadge%2FGothenburgBitFactory-b820f9%3FlabelColor%3Db820f9%26logo%3Dgithubsponsors%26logoColor%3Dfff)](https://github.com/GothenburgBitFactory) [![Escrito en C++](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fimg.shields.io%2Fstatic%2Fv1%3Flabel%3D%26message%3DC%2B%2B%26color%3D00599C%26logo%3Dcplusplus%26logoColor%3DFFFFFF)](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fimg.shields.io%2Fstatic%2Fv1%3Flabel%3D%26message%3DC%2B%2B%26color%3D00599C%26logo%3Dcplusplus%26logoColor%3DFFFFFF)

___

### [](https://dev.to/lissy93/cli-tools-you-cant-live-without-57f6#-raw-tuir-endraw-terminal-ui-for-reddit)[`tuir`](https://gitlab.com/ajak/tuir) - Terminal UI para Reddit

> `tuir` es genial si quieres parecer que estás trabajando, ¡mientras en realidad navegas por Reddit! Tiene combinaciones de teclas intuitivas, temas personalizados, y también puede renderizar imágenes y contenido multimedia. También está [haxor](https://github.com/donnemartin/haxor-news) para noticias de hackers.

[![tuir-example-usage](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Farticles%2Fynv7v3iubo16pywpz008.png)](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Farticles%2Fynv7v3iubo16pywpz008.png)

[![Ver tuir on GitLab](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fimg.shields.io%2Fgitlab%2Fstars%2Fajak%2Ftuir%3Fcolor%3Dfc6d26%26label%3Dtuir%26logo%3Dgitlab%26labelColor%3D232323)](https://gitlab.com/ajak/tuir) [![Autor ajak](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fimg.shields.io%2Fbadge%2Fajak-b820f9%3FlabelColor%3Db820f9%26logo%3Dgithubsponsors%26logoColor%3Dfff)](https://github.com/ajak) [![Escrito en Python](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fimg.shields.io%2Fstatic%2Fv1%3Flabel%3D%26message%3DPython%26color%3D3C78A9%26logo%3Dpython%26logoColor%3DFFFFFF)](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fimg.shields.io%2Fstatic%2Fv1%3Flabel%3D%26message%3DPython%26color%3D3C78A9%26logo%3Dpython%26logoColor%3DFFFFFF)

___

## [](https://dev.to/lissy93/cli-tools-you-cant-live-without-57f6#cli-dev-suits)CLI Dev Suits

### [](https://dev.to/lissy93/cli-tools-you-cant-live-without-57f6#-raw-httpie-endraw-http-api-testing-testing-client)[`httpie`](https://github.com/httpie/httpie) - Cliente de pruebas HTTP / API

> `httpie` es un cliente HTTP, para pruebas, depuración y uso de APIs. Soporta todo lo que se puede esperar - HTTPS, proxies, autenticación, cabeceras personalizadas, sesiones persistentes, análisis JSON. El uso es simple con una sintaxis expresiva y salida coloreada. Al igual que otros clientes HTTP (Postman, Hopscotch, Insomnia, etc) HTTPie también incluye una interfaz web.

[![httpie-example-usage](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Farticles%2Fgf1gdlvo5czinlxl2k8z.png)](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Farticles%2Fgf1gdlvo5czinlxl2k8z.png)

[![Ver httpie en Github](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fimg.shields.io%2Fgithub%2Fstars%2Fhttpie%2Fhttpie%3Fcolor%3D232323%26label%3Dhttpie%26logo%3Dgithub%26labelColor%3D232323)](https://github.com/httpie/httpie) [![Autor httpie](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fimg.shields.io%2Fbadge%2Fhttpie-b820f9%3FlabelColor%3Db820f9%26logo%3Dgithubsponsors%26logoColor%3Dfff)](https://github.com/httpie) [![Escrito en Python](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fimg.shields.io%2Fstatic%2Fv1%3Flabel%3D%26message%3DPython%26color%3D3C78A9%26logo%3Dpython%26logoColor%3DFFFFFF)](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fimg.shields.io%2Fstatic%2Fv1%3Flabel%3D%26message%3DPython%26color%3D3C78A9%26logo%3Dpython%26logoColor%3DFFFFFF)

___

### [](https://dev.to/lissy93/cli-tools-you-cant-live-without-57f6#-raw-lazydocker-endraw-full-docker-management-app)[`lazydocker`](https://github.com/jesseduffield/lazydocker) - Aplicación completa de gestión de Docker

> `lazydocker` es una aplicación de gestión de Docker, que te permite Ver todos los contenedores e imágenes, gestionar su estado, leer registros, comprobar el uso de recursos, reiniciar/reconstruir, analizar capas, podar contenedores, imágenes y volúmenes no utilizados, y mucho más. Te ahorra la necesidad de recordar, escribir y encadenar múltiples comandos Docker.

[![lazy-docker-example-usage](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Farticles%2Fcp3b6fc4kzuoj746hmb6.png)](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Farticles%2Fcp3b6fc4kzuoj746hmb6.png)

[![Ver lazydocker en Github](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fimg.shields.io%2Fgithub%2Fstars%2Fjesseduffield%2Flazydocker%3Fcolor%3D232323%26label%3Dlazydocker%26logo%3Dgithub%26labelColor%3D232323)](https://github.com/jesseduffield/lazydocker) [![Autor jesseduffield](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fimg.shields.io%2Fbadge%2Fjesseduffield-b820f9%3FlabelColor%3Db820f9%26logo%3Dgithubsponsors%26logoColor%3Dfff)](https://github.com/jesseduffield) [![Escrito en Go](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fimg.shields.io%2Fstatic%2Fv1%3Flabel%3D%26message%3DGo%2520Lang%26color%3D00ADD8%26logo%3Dgo%26logoColor%3DFFFFFF)](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fimg.shields.io%2Fstatic%2Fv1%3Flabel%3D%26message%3DGo%2520Lang%26color%3D00ADD8%26logo%3Dgo%26logoColor%3DFFFFFF)

___

### [](https://dev.to/lissy93/cli-tools-you-cant-live-without-57f6#-raw-lazygit-endraw-full-git-management-app)[`lazygit`](https://github.com/jesseduffield/lazygit) - Aplicación completa de gestión Git

> `lazygit` es un cliente git visual, en la línea de comandos. Fácilmente añadir, confirmar y puch archivos, resolver conflictos, comparar diffs, gestión de registros, y hacer operaciones complejas como aplasta y rebobina. Hay combinaciones de teclas para todo, colores, y es fácilmente configurable y ampliable.

[![lazy-git-example-usage](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Farticles%2Fhijyjh8rytgwxcqra8n2.png)](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Farticles%2Fhijyjh8rytgwxcqra8n2.png)

[![Ver lazygit en Github](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fimg.shields.io%2Fgithub%2Fstars%2Fjesseduffield%2Flazygit%3Fcolor%3D232323%26label%3Dlazygit%26logo%3Dgithub%26labelColor%3D232323)](https://github.com/jesseduffield/lazygit) [![Autor jesseduffield](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fimg.shields.io%2Fbadge%2Fjesseduffield-b820f9%3FlabelColor%3Db820f9%26logo%3Dgithubsponsors%26logoColor%3Dfff)](https://github.com/jesseduffield) [![Escrito en Go](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fimg.shields.io%2Fstatic%2Fv1%3Flabel%3D%26message%3DGo%2520Lang%26color%3D00ADD8%26logo%3Dgo%26logoColor%3DFFFFFF)](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fimg.shields.io%2Fstatic%2Fv1%3Flabel%3D%26message%3DGo%2520Lang%26color%3D00ADD8%26logo%3Dgo%26logoColor%3DFFFFFF)

___

### [](https://dev.to/lissy93/cli-tools-you-cant-live-without-57f6#-raw-kdash-endraw-kubernetes-dashboard-app)[`kdash`](https://github.com/kdash-rs/kdash/) - Aplicación del panel de control de Kubernetes

> `kdash` es una herramienta de gestión de Kubernetes todo en uno. Ver métricas de nodo, ver recursos, transmitir registros de contenedor, analizar contextos y gestionar nodos, pods y espacios de nombres.

[![Ver kdash en Github](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fimg.shields.io%2Fgithub%2Fstars%2Fkdash-rs%2Fkdash%3Fcolor%3D232323%26label%3Dkdash%26logo%3Dgithub%26labelColor%3D232323)](https://github.com/kdash-rs/kdash/) [![Autor kdash-rs](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fimg.shields.io%2Fbadge%2Fkdash-rs-b820f9%3FlabelColor%3Db820f9%26logo%3Dgithubsponsors%26logoColor%3Dfff)](https://github.com/kdash-rs) [![Escrito en Rust](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fimg.shields.io%2Fstatic%2Fv1%3Flabel%3D%26message%3DRust%26color%3De86243%26logo%3Drust%26logoColor%3DFFFFFF)](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fimg.shields.io%2Fstatic%2Fv1%3Flabel%3D%26message%3DRust%26color%3De86243%26logo%3Drust%26logoColor%3DFFFFFF)

___

### [](https://dev.to/lissy93/cli-tools-you-cant-live-without-57f6#-raw-gdpdashboard-endraw-visual-gdp-debugger)[`gdp-dashboard`](https://github.com/cyrus-and/gdb-dashboard) - Depurador de Visual GDP

> `gdp-dashboard` añade un elemento visual al depurador de GNU, para depurar programas C y C++. Analiza fácilmente la memoria, pasa por puntos de interrupción y registros Ver.

[![gdp-dashboard-example-usage](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Farticles%2Fumijepka2llahumhpub7.png)](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Farticles%2Fumijepka2llahumhpub7.png)

[![Ver gdb-dashboard en Github](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fimg.shields.io%2Fgithub%2Fstars%2Fcyrus-and%2Fgdb-dashboard%3Fcolor%3D232323%26label%3Dgdb-dashboard%26logo%3Dgithub%26labelColor%3D232323)](https://github.com/cyrus-and/gdb-dashboard) [![Autor cyrus-and](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fimg.shields.io%2Fbadge%2Fcyrus-and-b820f9%3FlabelColor%3Db820f9%26logo%3Dgithubsponsors%26logoColor%3Dfff)](https://github.com/cyrus-and) [![Escrito en Python](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fimg.shields.io%2Fstatic%2Fv1%3Flabel%3D%26message%3DPython%26color%3D3C78A9%26logo%3Dpython%26logoColor%3DFFFFFF)](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fimg.shields.io%2Fstatic%2Fv1%3Flabel%3D%26message%3DPython%26color%3D3C78A9%26logo%3Dpython%26logoColor%3DFFFFFF)

___


## [](https://dev.to/lissy93/cli-tools-you-cant-live-without-57f6#cli-external-sercvices)CLI Servicios Externos

### [](https://dev.to/lissy93/cli-tools-you-cant-live-without-57f6#-raw-ngrok-endraw-reverse-proxy-for-sharing-localhost)[`ngrok`](https://ngrok.com/) - Proxy inverso para compartir localhost

> `ngrok` de forma segura* expone tu localhost a internet detrás de una URL única. Esto te permite compartir lo que estás trabajando con tus colegas remotos, en tiempo real. El uso es [muy simple](https://notes.aliciasykes.com/p/RUi22QSyWe), pero también tiene un montón de características avanzadas para cosas como la autenticación, webhooks, cortafuegos, inspección de tráfico, dominios personalizados / comodín y mucho más.

[![ngrok-example-usage](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Farticles%2Fr9pomjvv8v7lf6gapw4r.png)](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Farticles%2Fr9pomjvv8v7lf6gapw4r.png)

[![Ver ngrok en Github](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fimg.shields.io%2Fgithub%2Fstars%2Finconshreveable%2Fngrok%3Fcolor%3D232323%26label%3Dngrok%26logo%3Dgithub%26labelColor%3D232323)](https://github.com/inconshreveable/ngrok) [![Autor inconshreveable](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fimg.shields.io%2Fbadge%2Finconshreveable-b820f9%3FlabelColor%3Db820f9%26logo%3Dgithubsponsors%26logoColor%3Dfff)](https://github.com/inconshreveable) [![Escrito en Go](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fimg.shields.io%2Fstatic%2Fv1%3Flabel%3D%26message%3DGo%2520Lang%26color%3D00ADD8%26logo%3Dgo%26logoColor%3DFFFFFF)](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fimg.shields.io%2Fstatic%2Fv1%3Flabel%3D%26message%3DGo%2520Lang%26color%3D00ADD8%26logo%3Dgo%26logoColor%3DFFFFFF)

___

### [](https://dev.to/lissy93/cli-tools-you-cant-live-without-57f6#-raw-tmate-endraw-share-a-terminal-session-via-internet)[`tmate`](https://tmate.io/) - Compartir una sesión de terminal a través de Internet
> `tmate` te permite compartir instantáneamente una sesión de terminal en vivo con alguien en otra parte del mundo. Funciona a través de diferentes sistemas, soporta control de acceso / auth, puede ser auto-alojado, y tiene todas las características de Tmux
[![Ver tmate en Github](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fimg.shields.io%2Fgithub%2Fstars%2Ftmate-io%2Ftmate%3Fcolor%3D232323%26label%3Dtmate%26logo%3Dgithub%26labelColor%3D232323)](https://github.com/tmate-io/tmate) [![Autor tmate-io](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fimg.shields.io%2Fbadge%2Ftmate-io-b820f9%3FlabelColor%3Db820f9%26logo%3Dgithubsponsors%26logoColor%3Dfff)](https://github.com/tmate-io) [![Escrito en C](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fimg.shields.io%2Fstatic%2Fv1%3Flabel%3D%26message%3DC%26color%3DA8B9CC%26logo%3Dc%26logoColor%3DFFFFFF)](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fimg.shields.io%2Fstatic%2Fv1%3Flabel%3D%26message%3DC%26color%3DA8B9CC%26logo%3Dc%26logoColor%3DFFFFFF)

___

### [](https://dev.to/lissy93/cli-tools-you-cant-live-without-57f6#-raw-asciinema-endraw-recording-sharing-terminal-sessions)[`asciinema`](https://asciinema.org/) - Grabar y compartir sesiones de terminal
> `asciinema` es muy útil para grabar, compartir e incrustar fácilmente una sesión de terminal. Ideal para mostrar algo que has construido, o para mostrar los pasos de línea de comandos para un tutorial. A diferencia de los vídeos de grabación de pantalla, el usuario puede copiar y pegar el contenido, cambiar el tema sobre la marcha y controlar la reproducción.

[![Ver asciinema en Github](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fimg.shields.io%2Fgithub%2Fstars%2Fasciinema%2Fasciinema%3Fcolor%3D232323%26label%3Dasciinema%26logo%3Dgithub%26labelColor%3D232323)](https://github.com/asciinema/asciinema) [![Autor asciinema](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fimg.shields.io%2Fbadge%2Fasciinema-b820f9%3FlabelColor%3Db820f9%26logo%3Dgithubsponsors%26logoColor%3Dfff)](https://github.com/asciinema) [![Escrito en Python](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fimg.shields.io%2Fstatic%2Fv1%3Flabel%3D%26message%3DPython%26color%3D3C78A9%26logo%3Dpython%26logoColor%3DFFFFFF)](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fimg.shields.io%2Fstatic%2Fv1%3Flabel%3D%26message%3DPython%26color%3D3C78A9%26logo%3Dpython%26logoColor%3DFFFFFF)

___

### [](https://dev.to/lissy93/cli-tools-you-cant-live-without-57f6#-raw-navi-endraw-interactive-cheat-sheet)[`navi`](https://github.com/denisidoro/navi) - Hoja de trucos interactiva

> `navi` permite navegar por las hojas de trucos y ejecutar comandos. Los valores sugeridos para los argumentos se muestran dinámicamente en una lista. Escribe menos, reduce los errores y ahórrate tener que memorizar miles de comandos. Se integra con [tldr](https://github.com/tldr-pages/tldr) y [cheat.sh](https://github.com/chubin/cheat.sh) para obtener contenido, pero también puedes importar otras cheatsheets, o incluso escribir las tuyas propias.

[![Ver navi en Github](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fimg.shields.io%2Fgithub%2Fstars%2Fdenisidoro%2Fnavi%3Fcolor%3D232323%26label%3Dnavi%26logo%3Dgithub%26labelColor%3D232323)](https://github.com/denisidoro/navi) [![Autor denisidoro](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fimg.shields.io%2Fbadge%2Fdenisidoro-b820f9%3FlabelColor%3Db820f9%26logo%3Dgithubsponsors%26logoColor%3Dfff)](https://github.com/denisidoro) [![Escrito en Rust](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fimg.shields.io%2Fstatic%2Fv1%3Flabel%3D%26message%3DRust%26color%3De86243%26logo%3Drust%26logoColor%3DFFFFFF)](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fimg.shields.io%2Fstatic%2Fv1%3Flabel%3D%26message%3DRust%26color%3De86243%26logo%3Drust%26logoColor%3DFFFFFF)

___

### [](https://dev.to/lissy93/cli-tools-you-cant-live-without-57f6#-raw-transfersh-endraw-fast-file-sharing)[`transfer.sh`](https://github.com/dutchcoders/transfer.sh/) - Intercambio rápido de archivos

> `transfer` hace que subir y compartir archivos sea realmente fácil, directamente desde la línea de comandos. Es gratis, soporta encriptación, te da una URL única, y también puede ser auto-alojado.  
> He escrito una función de ayuda Bash para hacer el uso un poco más fácil, puedes [encontrarla aquí](https://github.com/Lissy93/dotfiles/blob/master/utils/transfer.sh) o probarla ejecutando `bash <(curl -L -s https://alicia.url.lol/transfer)`.

[![transfer-sh-example-usage](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Farticles%2F2vl1k2i4tgvww87khlz1.png)](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Farticles%2F2vl1k2i4tgvww87khlz1.png)

[![Ver transfer.sh en Github](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fimg.shields.io%2Fgithub%2Fstars%2Fdutchcoders%2Ftransfer.sh%3Fcolor%3D232323%26label%3Dtransfer.sh%26logo%3Dgithub%26labelColor%3D232323)](https://github.com/dutchcoders/transfer.sh) [![Autor dutchcoders](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fimg.shields.io%2Fbadge%2Fdutchcoders-b820f9%3FlabelColor%3Db820f9%26logo%3Dgithubsponsors%26logoColor%3Dfff)](https://github.com/dutchcoders) [![Escrito en Go](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fimg.shields.io%2Fstatic%2Fv1%3Flabel%3D%26message%3DGo%2520Lang%26color%3D00ADD8%26logo%3Dgo%26logoColor%3DFFFFFF)](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fimg.shields.io%2Fstatic%2Fv1%3Flabel%3D%26message%3DGo%2520Lang%26color%3D00ADD8%26logo%3Dgo%26logoColor%3DFFFFFF)

___

### [](https://dev.to/lissy93/cli-tools-you-cant-live-without-57f6#-raw-surge-endraw-deploy-a-site-in-seconds)[`surge`](https://surge.sh/) - Despliegue un sitio en segundos

> `surge` es un proveedor de alojamiento estático gratuito, que puedes desplegar directamente desde el terminal en un solo comando, ¡sólo ejecuta `surge` desde dentro de tu directorio `dist`! Soporta dominios personalizados, certificados SSL automáticos, soporte pushState, soporte de recursos cross-origin - ¡y es gratis!

[![surge-sh-example-usage](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Farticles%2Fkwmm4qte24btl41amyol.png)](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Farticles%2Fkwmm4qte24btl41amyol.png)

___

### [](https://dev.to/lissy93/cli-tools-you-cant-live-without-57f6#-raw-wttrin-endraw-check-the-weather)[`wttr.in`](https://github.com/chubin/wttr.in) - Compruebe el tiempo

> `wttr.in` es un servicio que muestra el tiempo en un formato digerible en la línea de comandos. Sólo tienes que ejecutar `curl wttr.in` o `curl wttr.in/London` para probarlo. Hay parámetros de URL para personalizar los datos devueltos, así como el formato.

[![wrrt-in-example-usage](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Farticles%2F0xm7lb85oat23vtsj20i.png)](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Farticles%2F0xm7lb85oat23vtsj20i.png)

[![Ver wttr.in en Github](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fimg.shields.io%2Fgithub%2Fstars%2Fchubin%2Fwttr.in%3Fcolor%3D232323%26label%3Dwttr.in%26logo%3Dgithub%26labelColor%3D232323)](https://github.com/chubin/wttr.in) [![Autor chubin](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fimg.shields.io%2Fbadge%2Fchubin-b820f9%3FlabelColor%3Db820f9%26logo%3Dgithubsponsors%26logoColor%3Dfff)](https://github.com/chubin) [![Escrito en Python](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fimg.shields.io%2Fstatic%2Fv1%3Flabel%3D%26message%3DPython%26color%3D3C78A9%26logo%3Dpython%26logoColor%3DFFFFFF)](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fimg.shields.io%2Fstatic%2Fv1%3Flabel%3D%26message%3DPython%26color%3D3C78A9%26logo%3Dpython%26logoColor%3DFFFFFF)

___

## [](https://dev.to/lissy93/cli-tools-you-cant-live-without-57f6#cli-fun)CLI Divertidos

### [](https://dev.to/lissy93/cli-tools-you-cant-live-without-57f6#-raw-cowsay-endraw-have-an-ascii-cow-say-your-message)[`cowsay`](https://en.wikipedia.org/wiki/Cowsay) - Haz que una vaca ASCII diga tu mensaje

> `cowsay` es una vaca parlante configurable. Está basado en el [original](https://github.com/tnalpgge/rank-amateur-cowsay) de Tony Monroe

[![cowsay-example-usage](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Farticles%2Fazoieebcf11io8mhkc45.png)](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Farticles%2Fazoieebcf11io8mhkc45.png)

[![Ver cowsay en Github](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fimg.shields.io%2Fgithub%2Fstars%2Fpiuccio%2Fcowsay%3Fcolor%3D232323%26label%3Dcowsay%26logo%3Dgithub%26labelColor%3D232323)](https://github.com/piuccio/cowsay) [![Autor piuccio](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fimg.shields.io%2Fbadge%2Fpiuccio-b820f9%3FlabelColor%3Db820f9%26logo%3Dgithubsponsors%26logoColor%3Dfff)](https://github.com/piuccio) [![Escrito en JavaScript](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fimg.shields.io%2Fstatic%2Fv1%3Flabel%3D%26message%3DJavaScript%26color%3DF7DF1E%26logo%3Djavascript%26logoColor%3DFFFFFF)](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fimg.shields.io%2Fstatic%2Fv1%3Flabel%3D%26message%3DJavaScript%26color%3DF7DF1E%26logo%3Djavascript%26logoColor%3DFFFFFF)

___

### [](https://dev.to/lissy93/cli-tools-you-cant-live-without-57f6#-raw-figlet-endraw-output-text-as-big-ascii-art-text)[`figlet`](http://www.figlet.org/) - Texto de salida como texto de arte ASCII grande

> `figlet` muestra el texto como arte ASCII

[![figlet-example-usage](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Farticles%2Fxpaq8ufvoru1ijm8oj2c.png)](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Farticles%2Fxpaq8ufvoru1ijm8oj2c.png)

[![Ver figlet en Github](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fimg.shields.io%2Fgithub%2Fstars%2Fcmatsuoka%2Ffiglet%3Fcolor%3D232323%26label%3Dfiglet%26logo%3Dgithub%26labelColor%3D232323)](https://github.com/cmatsuoka/figlet) [![Autor cmatsuoka](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fimg.shields.io%2Fbadge%2Fcmatsuoka-b820f9%3FlabelColor%3Db820f9%26logo%3Dgithubsponsors%26logoColor%3Dfff)](https://github.com/cmatsuoka) [![Escrito en C](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fimg.shields.io%2Fstatic%2Fv1%3Flabel%3D%26message%3DC%26color%3DA8B9CC%26logo%3Dc%26logoColor%3DFFFFFF)](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fimg.shields.io%2Fstatic%2Fv1%3Flabel%3D%26message%3DC%26color%3DA8B9CC%26logo%3Dc%26logoColor%3DFFFFFF)

___

### [](https://dev.to/lissy93/cli-tools-you-cant-live-without-57f6#-raw-lolcat-endraw-make-console-output-raibow-colored)[`lolcat`](https://github.com/busyloop/lolcat) - Haz que la salida de la consola tenga los colores del arco iris

> `lolcat` colorea de arco iris cualquier texto que se le pase

[![lolcat-example-usage](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Farticles%2Fsp719mxeffx3zfecm2hs.png)](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Farticles%2Fsp719mxeffx3zfecm2hs.png)

[![Ver lolcat en Github](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fimg.shields.io%2Fgithub%2Fstars%2Fbusyloop%2Flolcat%3Fcolor%3D232323%26label%3Dlolcat%26logo%3Dgithub%26labelColor%3D232323)](https://github.com/busyloop/lolcat) [![Autor busyloop](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fimg.shields.io%2Fbadge%2Fbusyloop-b820f9%3FlabelColor%3Db820f9%26logo%3Dgithubsponsors%26logoColor%3Dfff)](https://github.com/busyloop) [![Escrito en Ruby](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fimg.shields.io%2Fstatic%2Fv1%3Flabel%3D%26message%3DRuby%26color%3DCC342D%26logo%3Druby%26logoColor%3DFFFFFF)](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fimg.shields.io%2Fstatic%2Fv1%3Flabel%3D%26message%3DRuby%26color%3DCC342D%26logo%3Druby%26logoColor%3DFFFFFF)

___

### [](https://dev.to/lissy93/cli-tools-you-cant-live-without-57f6#-raw-neofetch-endraw-show-system-data-and-ditstro-info)[`neofetch`](https://github.com/dylanaraps/neofetch) - Mostrar datos del sistema e información de la distribución

> `neofetch` imprime información de la distro y del sistema (para que puedas flexionar que usas Arch btw en r/unixporn)

[![neofetch-example-usage](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Farticles%2Fu2jus0pzbtrz4nc624u0.png)](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Farticles%2Fu2jus0pzbtrz4nc624u0.png)

[![Ver neofetch en Github](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fimg.shields.io%2Fgithub%2Fstars%2Fdylanaraps%2Fneofetch%3Fcolor%3D232323%26label%3Dneofetch%26logo%3Dgithub%26labelColor%3D232323)](https://github.com/dylanaraps/neofetch) [![Autor dylanaraps](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fimg.shields.io%2Fbadge%2Fdylanaraps-b820f9%3FlabelColor%3Db820f9%26logo%3Dgithubsponsors%26logoColor%3Dfff)](https://github.com/dylanaraps) [![Escrito en Bash](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fimg.shields.io%2Fstatic%2Fv1%3Flabel%3D%26message%3DBash%26color%3Dgreen%26logo%3Dgnubash%26logoColor%3DFFFFFF)](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fimg.shields.io%2Fstatic%2Fv1%3Flabel%3D%26message%3DBash%26color%3Dgreen%26logo%3Dgnubash%26logoColor%3DFFFFFF)

Como ejemplo, estoy usando `cowsay`, `figlet`, `lolcat` y `neofetch` para crear un MOTD personalizado basado en el tiempo que se muestra al usuario cuando se conecta por primera vez. Les saluda por su nombre, muestra información del servidor y la hora, fecha, tiempo e IP. [Aquí está el código fuente](https://github.com/Lissy93/dotfiles/blob/master/utils/welcome-banner.sh).

[![welcome](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Farticles%2Fobdjwjl5on1mdst6lvkh.png)](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Farticles%2Fobdjwjl5on1mdst6lvkh.png)
___

## [](https://dev.to/lissy93/cli-tools-you-cant-live-without-57f6#instalacion-y-gestion)Instalación y Gestión

La mayoría de nosotros tenemos un conjunto básico de aplicaciones y utilidades CLI en las que confiamos. Configurar una nueva máquina e instalar cada programa individualmente sería muy tedioso. Por eso, la tarea de instalar y actualizar tus apps de terminal es perfecta para automatizar. [Aquí](https://github.com/Lissy93/dotfiles/tree/master/scripts/installs) tienes algunos scripts de ejemplo que he escrito, que puedes añadir fácilmente a tus dotfiles o ejecutar de forma independiente para asegurarte de que nunca te falte una app.

Para usuarios de MacOS, el método más sencillo es usar [Homebrew](https://brew.sh/). Solo tienes que crear un Brewfile (con `touch ~/.Brewfile`), luego listar cada una de tus apps y ejecutar `brew bundle`. Puedes mantener tu lista de paquetes respaldada poniéndola en un repositorio Git. Aquí tienes un ejemplo para empezar: [https://github.com/Lissy93/Brewfile](https://github.com/Lissy93/Brewfile)

En Linux, normalmente querrás usar el gestor de paquetes nativo (por ejemplo, `pacman`, `apt`). Por ejemplo, [aquí tienes un script](https://github.com/Lissy93/dotfiles/blob/master/scripts/installs/arch-pacman.sh) para instalar las apps anteriores en sistemas Arch Linux.

Las aplicaciones de escritorio en Linux pueden gestionarse de forma similar, usando Flatpak. De nuevo, [aquí tienes un script de ejemplo](https://github.com/Lissy93/dotfiles/blob/master/scripts/installs/flatpak.sh) :)

___

## [](https://dev.to/lissy93/cli-tools-you-cant-live-without-57f6#conclusion)Conclusión

... Y eso es todo: una lista de útiles aplicaciones CLI y un método para instalarlas y mantenerlas actualizadas en todos tus sistemas.

Espero que algunas de estas te sean útiles :)

¡Me encantaría saber cuáles son tus aplicaciones CLI favoritas! Déjalo en los comentarios abajo.

### [](https://dev.to/lissy93/cli-tools-you-cant-live-without-57f6#informacion-adicional)Información adicional

#### [](https://dev.to/lissy93/cli-tools-you-cant-live-without-57f6#que-no-se-incluyo)Qué no se incluyó

-   Esta lista no incluye lo básico, como Vim, Tmux, Ranger, ZSH, Git, etc., que probablemente ya usas
-   Tampoco he incluido nada demasiado específico o solo relevante para pocos usuarios
-   No se incluye nada específico de un sistema o que no sea multiplataforma (Linux/Unix, MacOS)
-   Tampoco apps relacionadas con la terminal pero que no sean CLI (como emuladores de terminal)
-   Para la mayoría de los proyectos listados, hay muchas alternativas que logran cosas similares; por brevedad, esas tampoco se incluyeron

#### [](https://dev.to/lissy93/cli-tools-you-cant-live-without-57f6#creditos)Créditos

Un gran reconocimiento a los autores y comunidades detrás de cada una de estas apps. Sin ellos y su trabajo, nuestra vida en la línea de comandos sería mucho menos genial. Donde ha sido posible, he intentado dar crédito a los autores, pero si me he olvidado de alguno, avísame abajo y haré una actualización.

#### [](https://dev.to/lissy93/cli-tools-you-cant-live-without-57f6#comentarios)Comentarios

¿Qué me he perdido? Me encantaría conocer tus aplicaciones CLI favoritas, ¡especialmente si hay alguna increíble que no he incluido!

También me gustaría conocer tus opiniones y sugerencias; siempre busco mejorar :)

#### [](https://dev.to/lissy93/cli-tools-you-cant-live-without-57f6#insignias)Insignias

A continuación el script que hice para generar las insignias de Autor, lenguaje y estrellas de GitHub:

## Acerca de

He creado esto para generar rápidamente los enlaces del proyecto, para esta publicación: [Herramientas CLI sin las que no podrás vivir 🔧](https://dev.to/lissy93/cli-tools-you-cant-live-without-57f6)

Es solo un script sencillo para generar rápidamente insignias Markdown incrustables que muestran información del repositorio.  
Los datos se obtienen de la API de GitHub y las insignias se sirven utilizando la API de [Shields.io](https://shields.io/).  
Incluye una insignia para + enlace a: el autor, el repositorio + recuento de estrellas y el lenguaje utilizado.  
Pega la URL de un repositorio, pulsa «Generar» y los resultados se copiarán en tu portapapeles.

## Implementación

Es solo una página HTML estática, así que puedes servirla con cualquier servidor web, CDN o host estático.  
Hay una demo alojada en GH Pages, en: [lissy93.github.io/repo-badge-maker](https://lissy93.github.io/repo-badge-maker/)

## Informar de un problema

¿Has encontrado algo que no funciona? [Abre un problema](https://github.com/Lissy93/repo-badge-maker/issues/new/choose) y describe el problema, los pasos para reproducirlo junto con...

[Ver en Github](https://github.com/Lissy93/repo-badge-maker)


#### [](https://dev.to/lissy93/cli-tools-you-cant-live-without-57f6#find-more)Más información

Si te ha gustado esto, te recomiendo que eches un vistazo también a:

-   **[terminals-are-sexy](https://github.com/k4m4/terminals-are-sexy)** por Nikolaos Kamarinakis
-   **[awesome-shell](https://github.com/alebcay/awesome-shell)** por Caleb Xu
-   **[awesome-cli-apps](https://github.com/agarrharr/awesome-cli-apps)** por Adam Garrett-Harris

Si eres nuevo en la línea de comandos, **[The Art of Command Line](https://github.com/jlevy/the-art-of-command-line)**, de Joshua Levy, es un recurso excelente, al igual que **[Bash Guide](https://github.com/Idnan/bash-guide)**, de Adnan Ahmed.

Y si buscas inspiración, te encantará **[r/unixporn](https://www.reddit.com/r/unixporn/)** ⚡

___

* La versión original de este artículo se puede encontrar en [dev.to/lissy93](https://dev.to/lissy93/cli-tools-you-cant-live-without-57f6) (inglés).


* Autoría por [Alicia Sykes](https://www.aliciasykes.com/), traducción por [@elflacodeit](https://www.instagram.com/elflacodeit/)