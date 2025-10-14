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
- cli

Thumbnail: assets/50-cli-command-tools.png
socialImage: assets/50-cli-command-tools.png
featuredImage: assets/50-cli-command-tools.png

Topics:
- herramientas de desarrollo
- eficiencia en terminal
- productividad técnica

markup: markdown
date: 2025-10-14
draft: false
---

_La versión original de este post se puede encontrar en [dev.to/lissy93](https://dev.to/lissy93/cli-tools-you-cant-live-without-57f6) (inglés)._

Como desarrolladores, pasamos gran parte de nuestro tiempo en el terminal. Hay un montón de herramientas CLI útiles que pueden hacer tu vida en la línea de comandos más fácil, más rápida y más divertida.

Este post describe mi top 50 de herramientas CLI imprescindibles, en las que he llegado a confiar.

Al final del artículo, he incluido algunas secuencias de comandos para ayudarle a automatizar la instalación y actualización de estas herramientas en varios sistemas / distros.

↕️ **Índice**
- [Utilidades](/blog/posts/50-herramientas-cli-no-vas-a-poder-dejar-de-usar/#utilidades)
  - [`thefuck` - Autocorrección de comandos mal escritos](/blog/posts/50-herramientas-cli-no-vas-a-poder-dejar-de-usar/#thefuck---autocorrección-de-comandos-mal-escritos)
  - [`zoxide` - Fácil navegación _(mejor `cd`)_](/blog/posts/50-herramientas-cli-no-vas-a-poder-dejar-de-usar/#zoxide---fácil-navegación-mejor-cd)
  - [`tldr` - Documentos mantenidos por la comunidad _(mejor `man`)_](/blog/posts/50-herramientas-cli-no-vas-a-poder-dejar-de-usar/#tldr---documentos-mantenidos-por-la-comunidad-mejor)
  - [`scc` - Contar líneas de código _(mejor `cloc`)_](/blog/posts/50-herramientas-cli-no-vas-a-poder-dejar-de-usar/#scc---contar-líneas-de-código-mejor)
  - [`exa` - Archivos de listado _(mejor `ls`)_](/blog/posts/50-herramientas-cli-no-vas-a-poder-dejar-de-usar/#exa---archivos-de-listado-mejor)
  - [`duf` - Uso del disco _(mejor `df`)_](/blog/posts/50-herramientas-cli-no-vas-a-poder-dejar-de-usar/#duf---uso-del-disco-mejor)
  - [`aria2` - Utilidad de descarga _(mejor `wget`)_](/blog/posts/50-herramientas-cli-no-vas-a-poder-dejar-de-usar/#aria2---utilidad-de-descarga-mejor)
  - [`bat` - Lectura de archivos _(mejor `cat`)_](/blog/posts/50-herramientas-cli-no-vas-a-poder-dejar-de-usar/#bat---lectura-de-archivos-mejor)
  - [`diff-so-fancy` - Comparación de archivos _(mejor `diff`)_](/blog/posts/50-herramientas-cli-no-vas-a-poder-dejar-de-usar/#diff-so-fancy---comparación-de-archivos-mejor)
  - [`entr` - Esté atento a los cambios](/blog/posts/50-herramientas-cli-no-vas-a-poder-dejar-de-usar/#entr---esté-atento-a-los-cambios)
  - [`exiftool` - Lectura y escritura de metadatos](/blog/posts/50-herramientas-cli-no-vas-a-poder-dejar-de-usar/#exiftool---lectura-y-escritura-de-metadatos)
  - [`fdupes` - Buscador de archivos duplicados](/blog/posts/50-herramientas-cli-no-vas-a-poder-dejar-de-usar/#fdupes---buscador-de-archivos-duplicados)
  - [`fzf` - Buscador de archivos difuso _(mejor `find`)_](/blog/posts/50-herramientas-cli-no-vas-a-poder-dejar-de-usar/#fzf---buscador-de-archivos-difuso-mejor)
  - [`hyperfine` - Evaluación comparativa de mandos](/blog/posts/50-herramientas-cli-no-vas-a-poder-dejar-de-usar/#hyperfine---evaluación-comparativa-de-mandos)
  - [`just` - Corredor de comandos moderno _(mejor `make`)_](/blog/posts/50-herramientas-cli-no-vas-a-poder-dejar-de-usar/#just---corredor-de-comandos-moderno-mejor)
  - [`jq` - Procesador JSON](/blog/posts/50-herramientas-cli-no-vas-a-poder-dejar-de-usar/#jq---procesador-json)
  - [`most` - Localizador de desplazamiento multiventana _(mejor less)_](/blog/posts/50-herramientas-cli-no-vas-a-poder-dejar-de-usar/#most---localizador-de-desplazamiento-multiventana-mejor-less)
  - [`procs` - Visor de procesos _(mejor ps)_](/blog/posts/50-herramientas-cli-no-vas-a-poder-dejar-de-usar/#procs---visor-de-procesos-mejor-ps)
  - [`rip` - Herramienta de borrado _(mejor rm)_](/blog/posts/50-herramientas-cli-no-vas-a-poder-dejar-de-usar/#rip---herramienta-de-borrado-mejor-rm)
  - [`ripgrep` - Búsqueda dentro de archivos _(mejor `grep`)_](/blog/posts/50-herramientas-cli-no-vas-a-poder-dejar-de-usar/#ripgrep---búsqueda-dentro-de-archivos-mejor)
  - [`rsync` - Transferencia rápida e incremental de archivos](/blog/posts/50-herramientas-cli-no-vas-a-poder-dejar-de-usar/#rsync---transferencia-rápida-e-incremental-de-archivos)
  - [`sd` - Buscar y reemplazar _(mejor `sed`)_](/blog/posts/50-herramientas-cli-no-vas-a-poder-dejar-de-usar/#sd---buscar-y-reemplazar-mejor)
  - [`tre` - Jerarquía de directorios _(mejor `tree`)_](/blog/posts/50-herramientas-cli-no-vas-a-poder-dejar-de-usar/#tre---jerarquía-de-directorios-mejor)
  - [`xsel` - Acceso al portapapeles](/blog/posts/50-herramientas-cli-no-vas-a-poder-dejar-de-usar/#xsel---acceso-al-portapapeles)
- [Aplicaciones de monitorización y rendimiento](/blog/posts/50-herramientas-cli-no-vas-a-poder-dejar-de-usar/#aplicaciones-de-monitorización-y-rendimiento)
  - [`bandwhich` - Monitor de utilización de ancho de banda](/blog/posts/50-herramientas-cli-no-vas-a-poder-dejar-de-usar/#bandwhich---monitor-de-utilización-de-ancho-de-banda)
  - [`ctop` - Métricas y monitoreo de contenedores](/blog/posts/50-herramientas-cli-no-vas-a-poder-dejar-de-usar/#ctop---métricas-y-monitoreo-de-contenedores)
  - [`bpytop` - Monitoreo de recursos _(mejor `htop`)_](/blog/posts/50-herramientas-cli-no-vas-a-poder-dejar-de-usar/#bpytop---monitoreo-de-recursos-mejor)
  - [`glances` - Monitor de recursos + web y API](/blog/posts/50-herramientas-cli-no-vas-a-poder-dejar-de-usar/#glances---monitor-de-recursos--web-y-api)
  - [`gping` - Herramienta de ping interactiva _(mejor `ping`)_](/blog/posts/50-herramientas-cli-no-vas-a-poder-dejar-de-usar/#gping---herramienta-de-ping-interactiva-mejor)
  - [`dua-cli` - Analizador y monitor de uso de disco _(mejor `du`)_](/blog/posts/50-herramientas-cli-no-vas-a-poder-dejar-de-usar/#dua-cli---analizador-y-monitor-de-uso-de-disco-mejor)
  - [`speedtest-cli` - Utilidad de prueba de velocidad en línea de comandos](/blog/posts/50-herramientas-cli-no-vas-a-poder-dejar-de-usar/#speedtest-cli---utilidad-de-prueba-de-velocidad-en-línea-de-comandos)
  - [`dog` - Cliente de búsqueda DNS _(mejor `dig`)_](/blog/posts/50-herramientas-cli-no-vas-a-poder-dejar-de-usar/#dog---cliente-de-búsqueda-dns-mejor)
- [Productividad](/blog/posts/50-herramientas-cli-no-vas-a-poder-dejar-de-usar/#productividad)
  - [`browsh` - Navegador web CLI](/blog/posts/50-herramientas-cli-no-vas-a-poder-dejar-de-usar/#browsh---navegador-web-cli)
  - [`buku` - Gestor de marcadores](/blog/posts/50-herramientas-cli-no-vas-a-poder-dejar-de-usar/#buku---gestor-de-marcadores)
  - [`cmus` - Reproductor / navegador de música](/blog/posts/50-herramientas-cli-no-vas-a-poder-dejar-de-usar/#cmus---reproductor--navegador-de-música)
  - [`cointop` - Seguimiento de precios cripto](/blog/posts/50-herramientas-cli-no-vas-a-poder-dejar-de-usar/#cointop---seguimiento-de-precios-cripto)
  - [`ddgr` - Buscar en la web desde terminal](/blog/posts/50-herramientas-cli-no-vas-a-poder-dejar-de-usar/#ddgr---buscar-en-la-web-desde-terminal)
  - [`micro` - Editor de código _(mejor `nano`)_](/blog/posts/50-herramientas-cli-no-vas-a-poder-dejar-de-usar/#micro---editor-de-código-mejor)
  - [`khal` - Cliente de Calendario](/blog/posts/50-herramientas-cli-no-vas-a-poder-dejar-de-usar/#khal---cliente-de-calendario)
  - [`mutt` - Cliente de Email](/blog/posts/50-herramientas-cli-no-vas-a-poder-dejar-de-usar/#mutt---cliente-de-email)
  - [`newsboat` - Lector de noticias RSS / ATOM](/blog/posts/50-herramientas-cli-no-vas-a-poder-dejar-de-usar/#newsboat---lector-de-noticias-rss--atom)
  - [`rclone` - Gestionar el almacenamiento en la nube](/blog/posts/50-herramientas-cli-no-vas-a-poder-dejar-de-usar/#rclone---gestionar-el-almacenamiento-en-la-nube)
  - [`taskwarrior` - Todo + gestión de tareas](/blog/posts/50-herramientas-cli-no-vas-a-poder-dejar-de-usar/#taskwarrior---todo--gestión-de-tareas)
  - [`tuir` - Terminal UI para Reddit](/blog/posts/50-herramientas-cli-no-vas-a-poder-dejar-de-usar/#tuir---terminal-ui-para-reddit)
- [Dev Tools](/blog/posts/50-herramientas-cli-no-vas-a-poder-dejar-de-usar/#dev-tools)
  - [`httpie` - Cliente de pruebas HTTP / API](/blog/posts/50-herramientas-cli-no-vas-a-poder-dejar-de-usar/#httpie---cliente-de-pruebas-http--api)
  - [`lazydocker` - Aplicación completa de gestión de Docker](/blog/posts/50-herramientas-cli-no-vas-a-poder-dejar-de-usar/#lazydocker---aplicación-completa-de-gestión-de-docker)
  - [`lazygit` - Aplicación completa de gestión Git](/blog/posts/50-herramientas-cli-no-vas-a-poder-dejar-de-usar/#lazygit---aplicación-completa-de-gestión-git)
  - [`kdash` - Aplicación del panel de control de Kubernetes](/blog/posts/50-herramientas-cli-no-vas-a-poder-dejar-de-usar/#kdash---aplicación-del-panel-de-control-de-kubernetes)
  - [`gdb-dashboard` - Depurador de Visual GDP](/blog/posts/50-herramientas-cli-no-vas-a-poder-dejar-de-usar/#gdb-dashboard---depurador-visual-de-gdb)
- [Servicios Externos](/blog/posts/50-herramientas-cli-no-vas-a-poder-dejar-de-usar/#servicios-externos)
  - [`ngrok` - Proxy inverso para compartir localhost](/blog/posts/50-herramientas-cli-no-vas-a-poder-dejar-de-usar/#ngrok---proxy-inverso-para-compartir-localhost)
  - [`tmate` - Compartir una sesión de terminal a través de Internet](/blog/posts/50-herramientas-cli-no-vas-a-poder-dejar-de-usar/#tmate---compartir-una-sesión-de-terminal-a-través-de-internet)
  - [`asciinema` - Grabar y compartir sesiones de terminal](/blog/posts/50-herramientas-cli-no-vas-a-poder-dejar-de-usar/#asciinema---grabar-y-compartir-sesiones-de-terminal)
  - [`navi` - Hoja de trucos interactiva](/blog/posts/50-herramientas-cli-no-vas-a-poder-dejar-de-usar/#navi---hoja-de-trucos-interactiva)
  - [`transfer.sh` - Intercambio rápido de archivos](/blog/posts/50-herramientas-cli-no-vas-a-poder-dejar-de-usar/#transfersh---intercambio-rápido-de-archivos)
  - [`surge` - Despliegue un sitio en segundos](/blog/posts/50-herramientas-cli-no-vas-a-poder-dejar-de-usar/#surge---despliegue-un-sitio-en-segundos)
  - [`wttr.in` - Compruebe el tiempo](/blog/posts/50-herramientas-cli-no-vas-a-poder-dejar-de-usar/#wttrin---compruebe-el-tiempo)
- [Divertidos](/blog/posts/50-herramientas-cli-no-vas-a-poder-dejar-de-usar/#divertidos)
  - [`cowsay` - Haz que una vaca ASCII diga tu mensaje](/blog/posts/50-herramientas-cli-no-vas-a-poder-dejar-de-usar/#cowsay---haz-que-una-vaca-ascii-diga-tu-mensaje)
  - [`figlet` - Texto de salida como texto de arte ASCII grande](/blog/posts/50-herramientas-cli-no-vas-a-poder-dejar-de-usar/#figlet---texto-de-salida-como-texto-de-arte-ascii-grande)
  - [`lolcat` - Haz que la salida de la consola tenga los colores del arco iris](/blog/posts/50-herramientas-cli-no-vas-a-poder-dejar-de-usar/#lolcat---haz-que-la-salida-de-la-consola-tenga-los-colores-del-arco-iris)
  - [`neofetch` - Mostrar datos del sistema e información de la distribución](/blog/posts/50-herramientas-cli-no-vas-a-poder-dejar-de-usar/#neofetch---mostrar-datos-del-sistema-e-información-de-la-distribución)
- [Instalación y Gestión](/blog/posts/50-herramientas-cli-no-vas-a-poder-dejar-de-usar/#instalación-y-gestión)
- [Conclusión](/blog/posts/50-herramientas-cli-no-vas-a-poder-dejar-de-usar/#conclusión)
  - [Información adicional](/blog/posts/50-herramientas-cli-no-vas-a-poder-dejar-de-usar/#información-adicional)
    - [Qué no se incluyó](/blog/posts/50-herramientas-cli-no-vas-a-poder-dejar-de-usar/#qué-no-se-incluyó)
    - [Créditos](/blog/posts/50-herramientas-cli-no-vas-a-poder-dejar-de-usar/#créditos)
    - [Comentarios](/blog/posts/50-herramientas-cli-no-vas-a-poder-dejar-de-usar/#comentarios)
    - [Más información](/blog/posts/50-herramientas-cli-no-vas-a-poder-dejar-de-usar/#más-información)

## Utilidades

### [](#thefuck---autocorrección-de-comandos-mal-escritos)[`thefuck`](https://github.com/nvbn/thefuck) - Autocorrección de comandos mal escritos

> `thefuck` es una de esas utilidades sin las que no podrás vivir una vez que la hayas probado. Siempre que escribas mal un comando y obtengas un error, simplemente ejecuta `fuck` y lo autocorregirá. Usa arriba/abajo para elegir una corrección, o simplemente ejecuta `fuck --yeah` para ejecutar inmediatamente la más probable.

![the-fuck-example-usage](assets/50-thefuck.gif)

#### Instalación

```
# macOS (vía Homebrew)
brew install thefuck

# Arch Linux
sudo pacman -S thefuck

# FreeBSD
pkg install thefuck

```

| [Ver thefuck en GitHub](https://github.com/nvbn/thefuck) | [Autor nvbn](https://github.com/nvbn) | Escrito en Python |
| :-: | :-: | :-: |

___

### [](#zoxide---fácil-navegación-mejor-cd)[`zoxide`](https://github.com/ajeetdsouza/zoxide) - Fácil navegación _(mejor cd)_

> `zoxide` te permite saltar a cualquier directorio sin necesidad de recordar o especificar su ruta completa. Recuerda los directorios que has visitado, para que puedas saltar rápidamente; ni siquiera necesitas escribir el nombre completo de la carpeta. También dispone de una opción de selección interactiva, mediante `fzf`, que permite filtrar los resultados de los directorios en tiempo real.

![zoxide-example-usage](assets/50-zoxide.gif)

#### Instalación

```
# macOS (vía Homebrew)
brew install zoxide

# Arch Linux
sudo pacman -S zoxide

# Debian / Ubuntu
sudo apt install zoxide

# FreeBSD
pkg install zoxide

# Otros (vía Rust Creates)
cargo install zoxide --locked

```

| [Ver zoxide en GitHub](https://github.com/nvbn/ajeetdsouza/zoxide) | [Autor nvbn](https://github.com/ajeetdsouza) | Escrito en Rust |
| :-: | :-: | :-: |

___

### [](#tldr---documentos-mantenidos-por-la-comunidad-mejor-man)[`tldr`](https://github.com/tldr-pages/tldr) - Documentos mantenidos por la comunidad _(mejor `man`)_

> `tldr` es una enorme colección de páginas de manual mantenidas por la comunidad. A diferencia de las páginas de manual tradicionales, están resumidas, contienen ejemplos de uso útiles y están coloreadas para facilitar la lectura.


![tldr-example-usage](assets/50-tldr.gif)

#### Instalación

```
# macOS (vía Homebrew)
brew install tldr

# Otros (vía NPM)
npm install -g tldr

```

| [Ver tldr en GitHub](https://github.com/tldr-pages/tldr) | [Autor tldr-pages](https://github.com/tldr-pages) |
| :-: | :-: |

___

### [](#scc---contar-líneas-de-código-mejor-cloc)[`scc`](https://github.com/boyter/scc) - Contar líneas de código _(mejor `cloc`)_

> `scc` te da un desglose del número de líneas de código Escrito en cada lenguaje para un directorio específico. También muestra algunas estadísticas divertidas, como el coste estimado de desarrollo e información sobre la complejidad. Es increíblemente rápido, muy preciso y tiene soporte para una amplia gama de lenguajes.

![scc-example-usage](assets/50-scc.webp)

#### Instalación

```
# macOS (vía Homebrew)
brew install scc

# Otros (vía go)
go install github.com/boyter/scc/v3@latest

```

| [Ver scc en GitHub](https://github.com/boyter/scc) | [Autor boyter-pages](https://github.com/boyter) | Escrito en Go |
| :-: | :-: | :-: |

___

### [](#exa---archivos-de-listado-mejor-ls)[`exa`](https://github.com/ogham/exa) - Archivos de listado _(mejor `ls`)_

> `exa` es un reemplazo moderno basado en Rust para el comando `ls`, para listar archivos. Puede mostrar iconos de tipo de archivo, colores, información de archivo/carpeta y tiene varios formatos de salida - árbol, cuadrícula o lista.

![exa-example-usage](assets/50-exa.webp)

#### Instalación

```
# macOS (vía Homebrew)
brew install exa

# Arch Linux
sudo pacman -S exa

# Debian / Ubuntu
sudo apt install exa

```

| [Ver exa en GitHub](https://github.com/ogham/exa) | [Autor boyter-pages](https://github.com/ogham) | Escrito en Rust |
| :-: | :-: | :-: |

___

### [](#duf---uso-del-disco-mejor-df)[`duf`](https://github.com/muesli/duf) - Uso del disco _(mejor `df`)_

> `duf` es genial para mostrar información sobre discos montados y comprobar el espacio libre. Produce una salida clara y colorida, e incluye opciones para ordenar y personalizar los resultados.

![duf-example-usage](assets/50-duf.png)

#### Instalación

```
# macOS (vía Homebrew)
brew install duf

# Arch Linux
sudo pacman -S duf

# Debian / Ubuntu
sudo apt install duf

# FreeBSD
pkg install duf

```

| [Ver duf en GitHub](https://github.com/muesli/duf) | [Autor muesli](https://github.com/muesli) | Escrito en Go |
| :-: | :-: | :-: |

___

### [](#aria2---utilidad-de-descarga-mejor-wget)[`aria2`](https://github.com/aria2/aria2) - Utilidad de descarga _(mejor `wget`)_

> `aria2` es una utilidad ligera, multiprotocolo, de reanudación de descargas para HTTP/HTTPS, FTP, SFTP, BitTorrent y Metalink, con soporte para control a través de una interfaz RPC. Es increíblemente [rico en funciones](https://aria2.github.io/manual/en/html/README.html), y tiene toneladas de [opciones](https://aria2.github.io/manual/en/html/aria2c.html). También existe [ziahamza/webui-aria2](https://github.com/ziahamza/webui-aria2) - un buen compañero de interfaz web.

![aria2-example-usage](assets/50-aria2c.png)

#### Instalación

```
# macOS (vía Homebrew)
brew install aria2

# Arch Linux
sudo pacman -S aria2

# Debian / Ubuntu
sudo apt install aria2

```

| [Ver aria2 en GitHub](https://github.com/aria2/aria2) | [Autor aria2](https://github.com/aria2) | Escrito en C++ |
| :-: | :-: | :-: |

___

### [](#bat---lectura-de-archivos-mejor-cat)[`bat`](https://github.com/sharkdp/bat) - Lectura de archivos _(mejor `cat`)_

> `bat` es un clon de `cat` con resaltado de sintaxis e integración con git. Escrito en Rust, es muy performante, y tiene varias opciones para personalizar la salida y la tematización. Hay soporte para tuberías automáticas y concatenación de archivos.

![bat-example-usage](assets/50-bat.png)

#### Instalación

```
# macOS (vía Homebrew)
brew install bat

# Arch Linux
sudo pacman -S bat

# Debian / Ubuntu
sudo apt install bat

```

| [Ver bat en GitHub](https://github.com/sharkdp/bat) | [Autor sharkdp](https://github.com/sharkdp) | Escrito en Rust |
| :-: | :-: | :-: |

___

### [](#diff-so-fancy---comparación-de-archivos-mejor-diff)[`diff-so-fancy`](https://github.com/so-fancy/diff-so-fancy) - Comparación de archivos _(mejor `diff`)_

> `diff-so-fancy` le da un mejor aspecto a los diffs para comparar cadenas, archivos, directorios y cambios git. El resaltado de cambios hace que detectar los cambios sea mucho más fácil, y puedes personalizar el diseño y los colores de la salida.

![diff-so-fancy-example-usage](assets/50-diff.png)

#### Instalación

```
# macOS (vía Homebrew)
brew install diff-so-fancy

# Arch Linux
sudo pacman -S diff-so-fancy

# Debian / Ubuntu
sudo apt install diff-so-fancy

```

| [Ver diff so fancy en GitHub](https://github.com/so-fancy/diff-so-fancy) | [Autor so-fancy](https://github.com/so-fancy) | Escrito en Perl |
| :-: | :-: | :-: |

___

### [](#entr---esté-atento-a-los-cambios)[`entr`](https://github.com/eradman/entr) - Esté atento a los cambios

> `entr` le permite ejecutar un comando arbitrario cada vez que un archivo cambia. Puedes pasar un archivo, directorio, enlace simbólico o regex para especificar qué archivos debe vigilar. Es realmente útil para reconstruir proyectos automáticamente, reaccionar a logs, pruebas automatizadas, etc. A diferencia de otros proyectos similares, utiliza kqueue(2) o inotify(7) para evitar el sondeo y mejorar el rendimiento.

![entr-example-usage](assets/50-entr.png)

#### Instalación

```
# macOS (vía Homebrew)
brew install entr

# Arch Linux
sudo pacman -S entr

# Debian / Ubuntu
sudo apt install entr

```

| [Ver entr en GitHub](https://github.com/eradman/entr) | [Autor entr](https://github.com/eradman) | Escrito en C |
| :-: | :-: | :-: |

___

### [](#exiftool---lectura-y-escritura-de-metadatos)[`exiftool`](https://github.com/exiftool/exiftool) - Lectura y escritura de metadatos

> `exiftool` es una práctica utilidad para leer, escribir, eliminar y crear metainformación para una amplia variedad de tipos de archivos. No vuelva a filtrar accidentalmente su ubicación al compartir una foto.

![exiftool-example-usage](assets/50-exiftool.png)

| [Ver exiftool en GitHub](https://github.com/exiftool/exiftool) | [Autor exiftool](https://github.com/exiftool) | Escrito en Perl |
| :-: | :-: | :-: |

___

### [](#fdupes---buscador-de-archivos-duplicados)[`fdupes`](https://github.com/jbruchon/jdupes) - Buscador de archivos duplicados

> `fdupes` se utiliza para identificar y/o eliminar archivos duplicados dentro de directorios especificados. Es útil para liberar espacio en disco cuando tiene dos o más archivos idénticos.

![fdupes-example-usage](assets/50-fdupes.png)

| [Ver jdupes en GitHub](https://github.com/jbruchon/jdupes) | [Autor jbruchon](https://github.com/jbruchon) | Escrito en C |
| :-: | :-: | :-: |
___

### [](#fzf---buscador-de-archivos-difuso-mejor-find)[`fzf`](https://github.com/junegunn/fzf) - Buscador de archivos difuso _(mejor `find`)_

> `fzf` es un buscador de archivos difusos y una herramienta de filtrado extremadamente potente y fácil de usar. También tiene [plugins](https://github.com/junegunn/fzf/wiki/Related-projects) disponibles para la mayoría de los shells e IDEs, para mostrar resultados instantáneos durante la búsqueda. Este [post](https://www.freecodecamp.org/news/fzf-a-command-line-fuzzy-finder-missing-demo-a7de312403ff/) de Alexey Samoshkin destaca algunos de sus casos de uso.

![fzf-example-usage](assets/50-fzf.gif)

#### Instalación

```
# macOS (vía Homebrew)
brew install fzf

# Arch Linux
sudo pacman -S fzf

# Debian / Ubuntu
sudo apt install fzf

```

| [Ver fzf en GitHub](https://github.com/jbruchon/jdupes/fzf) | [Autor junegunn](https://github.com/junegunn) | Escrito en Go |
| :-: | :-: | :-: |

___

### [](#hyperfine---evaluación-comparativa-de-mandos)[`hyperfine`](https://github.com/sharkdp/hyperfine) - Evaluación comparativa de mandos

>`hyperfine` facilita la evaluación comparativa precisa de comandos o scripts arbitrarios. Se encarga de las ejecuciones de calentamiento, de limpiar la caché para obtener resultados precisos y de evitar interferencias de otros programas. También puede exportar los resultados como datos sin procesar y generar gráficos.

![hyperfine-example-usage](assets/50-hyperfine.png)

#### Instalación

```
# macOS (vía Homebrew)
brew install hyperfine

# Arch Linux
sudo pacman -S hyperfine

# Debian / Ubuntu
sudo apt install hyperfine
```

| [Ver hyperfine en GitHub](https://github.com/sharkdp/hyperfine) | [Autor sharkdp](https://github.com/sharkdp) | Escrito en Rust |
| :-: | :-: | :-: |

___

### [](#just---corredor-de-comandos-moderno-mejor-make)[`just`](https://github.com/casey/just) - Corredor de comandos moderno _(mejor `make`)_

> `just` es similar a `make` pero con algunas buenas adiciones. Te permite agrupar los comandos de tus proyectos en recopilaciones, que pueden ser fácilmente listadas y ejecutadas. Soporta alias, argumentos posicionales, diferentes shells, integración dot env, interprulación de cadenas, y casi todo lo que puedas necesitar.

![just-example-usage](assets/50-just.png)

#### Instalación

```
# macOS (vía Homebrew)
brew install just

# Arch Linux
sudo pacman -S just

# Debian / Ubuntu
sudo apt install just

```

| [Ver just en GitHub](https://github.com/casey/just) | [Autor casey](https://github.com/casey) | Escrito en Rust |
| :-: | :-: | :-: |

___

### [](#jq---procesador-json)[`jq`](https://github.com/stedolan/jq) - Procesador JSON

> `jq` es como `sed`, pero para JSON - puedes usarlo para cortar y filtrar y mapear y transformar datos estructurados con facilidad. Se puede utilizar para escribir consultas complejas para extraer o manipular datos JSON. También hay un [jq playground](https://jqplay.org/) que puedes usar para probarlo, o formular consultas con información en tiempo real.

| [Ver jq en GitHub](https://github.com/stedolan/jq) | [Autor stedolan](https://github.com/stedolan) | Escrito en C |
| :-: | :-: | :-: |
___

### [](#most---localizador-de-desplazamiento-multiventana-mejor-less)[`most`](https://www.jedsoft.org/most/) - Localizador de desplazamiento multiventana _(mejor less)_

> `most` es un paginador, para leer archivos largos o salidas de comandos. `most` soporta multi-ventanas y tiene la opción de no ajustar el texto.

| [Autor Jed](https://www.jedsoft.org/aboutme.html) | Escrito en S-Lang |
| :-: | :-: |
___

### [](#procs---visor-de-procesos-mejor-ps)[`procs`](https://github.com/dalance/procs) - Visor de procesos _(mejor ps)_

> `procs` es un visor de procesos fácil de navegar, tiene resaltado de color, facilita la clasificación y búsqueda de procesos, tiene árbol Ver y se actualiza en tiempo real.
![procs-example-usage](assets/50-procs.webp)

| [Ver procs en GitHub](https://github.com/dalance/procs) | [Autor dalance](https://github.com/dalance) | Escrito en Rust |
| :-: | :-: | :-: |
___

### [](#rip---herramienta-de-borrado-mejor-rm)[`rip`](https://github.com/nivekuil/rip) - Herramienta de borrado _(mejor rm)_

> `rip` es una herramienta de borrado segura, ergonómica y eficaz. Le permite eliminar archivos y directorios de forma intuitiva y restaurar fácilmente los archivos eliminados.

![rip-example-usage](assets/50-rip.webp)

| [Ver rip en GitHub](https://github.com/nivekuil/rip) | [Autor nivekuil](https://github.com/nivekuil) | Escrito en Rust |
| :-: | :-: | :-: |

___

### [](#ripgrep---búsqueda-dentro-de-archivos-mejor-grep)[`ripgrep`](https://github.com/BurntSushi/ripgrep) - Búsqueda dentro de archivos _(mejor `grep`)_

> `ripgrep` es una herramienta de búsqueda orientada a líneas que busca recursivamente un patrón regex en el directorio actual. Puede ignorar el contenido de `.gitignore` y omitir archivos binarios. Es capaz de buscar dentro de archivos comprimidos, o sólo buscar en una extensión específica, y entiende los archivos que utilizan varios métodos de codificación

![ripgrep-example-usage](assets/50-ripgrep.webp)

| [Ver ripgrep en GitHub](https://github.com/BurntSushi/ripgrep) | [Autor BurntSushi](https://github.com/BurntSushi) | Escrito en Rust |
| :-: | :-: | :-: |
___

### [](#rsync---transferencia-rápida-e-incremental-de-archivos)[`rsync`](https://rsync.samba.org/) - Transferencia rápida e incremental de archivos

> `rsync` te permite copiar archivos grandes localmente o desde o hacia hosts remotos o unidades externas. Puede utilizarse para mantener sincronizados archivos de varias ubicaciones y es perfecto para crear, actualizar y restaurar copias de seguridad.

| [Ver rsync en GitHub](https://github.com/WayneD/rsync) | [Autor WayneD](https://github.com/WayneD) | Escrito en C |
| :-: | :-: | :-: |

___

### [](#sd---buscar-y-reemplazar-mejor-sed)[`sd`](https://github.com/chmln/sd) - Buscar y reemplazar _(mejor `sed`)_
> `sd` es una herramienta de búsqueda y reemplazo fácil, rápida e intuitiva, basada en literales de cadena. Puede ejecutarse sobre un fichero, un directorio entero o cualquier texto canalizado.
![sd-example-usage](assets/50-sd.webp)

| [Ver sd en GitHub](https://github.com/chmln/sd) | [Autor chmln](https://github.com/chmln) | Escrito en Rust |
| :-: | :-: | :-: |
___

### [](#tre---jerarquía-de-directorios-mejor-tree)[`tre`](https://github.com/dduan/tre) - Jerarquía de directorios _(mejor `tree`)_

> `tre` muestra una lista de archivos en forma de árbol para tu directorio actual o uno especificado, con colores. Al ejecutarlo con la opción `-e`, numera cada elemento y crea un alias temporal que puedes usar para saltar rápidamente a esa ubicación

![tre-example-usage](assets/50-tre.webp)

| [Ver tre en GitHub](https://github.com/dduan/tre) | [Autor dduan](https://github.com/dduan) | Escrito en Rust |
| :-: | :-: | :-: |

___

### [](#xsel---acceso-al-portapapeles)[`xsel`](https://github.com/kfish/xsel) - Acceso al portapapeles

> `xsel` te permite leer y escribir en el portapapeles de selección X desde la línea de comandos. Es útil para enviar la salida de un comando al portapapeles o para pegar datos copiados en un comando.

| [Ver xsel en GitHub](https://github.com/kfish/xsel) | [Autor kfish](https://github.com/kfish) | Escrito en C |
| :-: | :-: | :-: |
___

## Aplicaciones de monitorización y rendimiento

### [](#bandwhich---monitor-de-utilización-de-ancho-de-banda)[`bandwhich`](https://github.com/imsnif/bandwhich) - Monitor de utilización de ancho de banda

> Muestra el uso de ancho de banda, información de conexión, hosts salientes y consultas DNS en tiempo real
![bandwhich-example-usage](assets/50-bandwhich.webp)

| [Ver bandwhich en GitHub](https://github.com/imsnif/bandwhich) | [Autor imsnif](https://github.com/imsnif) | Escrito en Rust |
| :-: | :-: | :-: |

___

### [](#ctop---métricas-y-monitoreo-de-contenedores)[`ctop`](https://github.com/bcicen/ctop) - Métricas y monitoreo de contenedores

> Como `top`, pero para monitorear el uso de recursos de contenedores en ejecución (Docker y runC). Muestra CPU, memoria y ancho de banda de red en tiempo real, así como el nombre, estado e ID de cada contenedor. También incluye un visor de logs integrado y opciones para gestionar (detener, iniciar, ejecutar, etc.) contenedores.

![ctop-example-usage](assets/50-ctop.webp)

| [Ver ctop en GitHub](https://github.com/bcicen/ctop) | [Autor bcicen](https://github.com/bcicen) | Escrito en Go |
| :-: | :-: | :-: |

___

### [](#bpytop---monitoreo-de-recursos-mejor-htop)[`bpytop`](https://github.com/aristocratos/bpytop) - Monitoreo de recursos _(mejor `htop`)_

> `bpytop` es un monitor de recursos rápido, interactivo y visual. Muestra los procesos principales en ejecución, el historial reciente de CPU, memoria, disco y red. Desde la interfaz puedes navegar, ordenar y buscar; también hay soporte para temas de color personalizados.

![bpytop-example-usage](assets/50-bpytop.webp)

| [Ver bpytop en GitHub](https://github.com/aristocratos/bpytop) | [Autor aristocratos](https://github.com/aristocratos) | Escrito en Python |
| :-: | :-: | :-: |

___

### [](#glances---monitor-de-recursos--web-y-api)[`glances`](https://github.com/nicolargo/glances) - Monitor de recursos + web y API

> `glances` es otro monitor de recursos, pero con un conjunto de características diferente. Incluye una vista web totalmente responsiva, una API REST y monitoreo histórico. Es fácilmente extensible y puede integrarse con otros servicios.

![glances-example-usage](assets/50-glances.webp)

| [Ver glances en GitHub](https://github.com/nicolargo/glances) | [Autor nicolargo](https://github.com/nicolargo) | Escrito en Python |
| :-: | :-: | :-: |

___

### [](#gping---herramienta-de-ping-interactiva-mejor-ping)[`gping`](https://github.com/orf/gping) - Herramienta de ping interactiva _(mejor `ping`)_

> `gping` puede ejecutar pruebas de ping en varios hosts, mostrando los resultados en un gráfico en tiempo real. También puede usarse para monitorear el tiempo de ejecución, cuando se usa con la opción `--cmd`.

![gping-example-usage](assets/50-gping.gif)

| [Ver gping en GitHub](https://github.com/orf/gping) | [Autor orf](https://github.com/orf) | Escrito en Rust |
| :-: | :-: | :-: |

___

### [](#dua-cli---analizador-y-monitor-de-uso-de-disco-mejor-du)[`dua-cli`](https://github.com/Byron/dua-cli) - Analizador y monitor de uso de disco _(mejor `du`)_

> `dua-cli` te permite ver de forma interactiva el espacio usado y disponible en cada unidad montada, y facilita liberar almacenamiento.

![dua-cli-usage-example](assets/50-dua-cli.webp)

| [Ver dua-cli en GitHub](https://github.com/Byron/dua-cli) | [Autor Byron](https://github.com/Byron) | Escrito en Rust |
| :-: | :-: | :-: |

___

### [](#speedtest-cli---utilidad-de-prueba-de-velocidad-en-línea-de-comandos)[`speedtest-cli`](https://github.com/sivel/speedtest-cli) - Utilidad de prueba de velocidad en línea de comandos

> `speedtest-cli` simplemente ejecuta una prueba de velocidad de internet, usando speedtest.net, pero directamente desde la terminal :)

![speedtest-cli-example-usage](assets/50-speedtest-cli.webp)

| [Ver speedtest-cli en GitHub](https://github.com/sivel/speedtest-cli) | [Autor sivel](https://github.com/sivel) | Escrito en Python |
| :-: | :-: | :-: |

___

### [](#dog---cliente-de-búsqueda-dns-mejor-dig)[`dog`](https://github.com/ogham/dog) - Cliente de búsqueda DNS _(mejor `dig`)_

> `dog` es un cliente de búsqueda DNS fácil de usar, con soporte para DoT y DoH, salidas coloridas y la opción de emitir JSON.

![dog-example-usage](assets/50-dog.webp)

| [Ver dog en GitHub](https://github.com/ogham/dog) | [Autor ogham](https://github.com/ogham) | Escrito en Rust |
| :-: | :-: | :-: |

___

## Productividad

#### Navega por la web, escucha música, revisa correos, gestiona calendarios, lee noticias y más, ¡todo sin salir de la terminal!

### [](#browsh---navegador-web-cli)[`browsh`](https://github.com/browsh-org/browsh) - Navegador web CLI

> `browsh` es un navegador de texto moderno, interactivo y en tiempo real, renderizado para TTYs y navegadores. Soporta navegación tanto con ratón como con teclado, y tiene muchas más funciones de lo que esperarías para una aplicación puramente de terminal. Además, ayuda a reducir el consumo de batería que afecta a los navegadores modernos y, con soporte para MoSH, puedes experimentar tiempos de carga más rápidos gracias al menor uso de ancho de banda.

![browsh-example-usage](assets/50-browsh.webp)

| [Ver browsh en GitHub](https://github.com/browsh-org/browsh) | [Autor browsh-org](https://github.com/browsh-org) | Escrito en JavaScript |
| :-: | :-: | :-: |

___

### [](#buku---gestor-de-marcadores)[`buku`](https://github.com/jarun/buku) - Gestor de marcadores

> `buku` es un gestor de marcadores para terminal, con muchas opciones de configuración, almacenamiento y uso. También dispone de una [interfaz web opcional](https://github.com/jarun/buku/tree/master/bukuserver#screenshots) y un [plugin para navegador](https://github.com/samhh/bukubrow-webext#installation) para acceder a tus marcadores fuera de la terminal.

![buku-example-usage](assets/50-buku.webp)

| [Ver buku en GitHub](https://github.com/jarun/buku) | [Autor jarun](https://github.com/jarun) | Escrito en Python |
| :-: | :-: | :-: |

___

### [](#cmus---reproductor--navegador-de-música)[`cmus`](https://github.com/cmus/cmus) - Reproductor / navegador de música

> `cmus` es un reproductor de música para terminal, controlado con atajos de teclado. Soporta una amplia gama de formatos y códecs de audio, y permite organizar pistas en listas de reproducción y aplicar configuraciones de reproducción.

![cmus-example-usage](assets/50-cmus.webp)

| [Ver cmus en GitHub](https://github.com/cmus/cmus) | [Autor cmus](https://github.com/cmus) | Escrito en C |
| :-: | :-: | :-: |

___

### [](#cointop---seguimiento-de-precios-cripto)[`cointop`](https://github.com/cointop-sh/cointop) - Seguimiento de precios cripto

> `cointop` muestra los precios actuales de criptomonedas y el historial de precios de tu portafolio. Soporta alertas de precio, gráficos históricos, conversión de divisas, búsqueda difusa y mucho más. Puedes probar la demo en la web [cointop.sh](https://cointop.sh/) o ejecutando `ssh cointop.sh`.

![cointop-example-usage](assets/50-cointop.webp)

| [Ver cointop en GitHub](https://github.com/cointop-sh/cointop) | [Autor cointop-sh](https://github.com/cointop-sh) | Escrito en Go|
| :-: | :-: | :-: |

___

### [](#ddgr---buscar-en-la-web-desde-terminal)[`ddgr`](https://github.com/jarun/ddgr) - Buscar en la web desde terminal

> `ddgr` es como [googler](https://github.com/jarun/googler), pero para DuckDuckGo. Es rápido, limpio y fácil, con soporte para respuestas instantáneas, autocompletado, bangs de búsqueda y búsqueda avanzada. Respeta tu privacidad por defecto, también tiene soporte para proxy HTTPS y funciona con Tor.

![dggr-example-usage](assets/50-ddgr.webp)

| [Ver ddgr en GitHub](https://github.com/jarun/ddgr) | [Autor jarun](https://github.com/jarun) | Escrito en Python |
| :-: | :-: | :-: |

___


### [](#micro---editor-de-código-mejor-nano)[`micro`](https://github.com/zyedidia/micro) - Editor de código _(mejor `nano`)_

> `micro` es un editor de código fácil de usar, rápido y extensible, con soporte para ratón. Como viene en un solo binario, la instalación es tan simple como `curl https://getmic.ro | bash`.

![micro-screenshot](assets/50-micro.webp)

| [Ver micro en GitHub](https://github.com/zyedidia/micro) | [Autor zyedidia](https://github.com/zyedidia) | Escrito en Go |
| :-: | :-: | :-: |

___

### [](#khal---cliente-de-calendario)[`khal`](https://github.com/pimutils/khal) - Cliente de Calendario

> `khal` es una aplicación de calendario para terminales, que muestra los próximos eventos, vistas del mes y de la agenda. Puedes sincronizarlo con cualquier calendario CalDAV, y añadir, editar y eliminar eventos directamente.

![khal-example-usage](assets/50-khal.webp)

| [Ver khal en GitHub](https://github.com/pimutils/khal) | [Autor pimutils](https://github.com/pimutils) | Escrito en Python |
| :-: | :-: | :-: |

___

### [](#mutt---cliente-de-email)[`mutt`](https://gitlab.com/muttmua/mutt) - Cliente de Email

> `mutt` es un cliente de correo clásico, basado en terminal, para enviar, leer y gestionar correos electrónicos. Soporta todos los principales protocolos de correo electrónico y formatos de buzón, permite archivos adjuntos, CCO/CC, hilos, listas de correo y notificaciones de estado de entrega.

![mutt-example-usage](assets/50-mutt.webp)

| [Ver mutt en GitHub](https://gitlab.com/muttmua/mutt) | [Autor muttmua](https://github.com/muttmua) | Escrito en C |
| :-: | :-: | :-: |

___

### [](#newsboat---lector-de-noticias-rss--atom)[`newsboat`](https://github.com/newsboat/newsboat) - Lector de noticias RSS / ATOM

> `newsboat` es un lector y agregador de feeds RSS, para leer las noticias, blogs y seguir las actualizaciones directamente desde el terminal.

![newsboat-example-usage](assets/50-newsboat.webp)

| [Ver newsboat en GitHub](https://github.com/newsboat/newsboat) | [Autor newsboat](https://github.com/newsboat) | Escrito en C++ |
| :-: | :-: | :-: |

___

### [](#rclone---gestionar-el-almacenamiento-en-la-nube)[`rclone`](https://github.com/rclone/rclone) - Gestionar el almacenamiento en la nube

> `rclone` es una práctica utilidad para sincronizar archivos y carpetas con varios proveedores de almacenamiento en la nube. Puede invocarse directamente desde la línea de comandos o integrarse fácilmente en un script como sustituto de las pesadas aplicaciones de sincronización de escritorio.

| [Ver rclone en GitHub](https://github.com/rclone) | Escrito en Go |
| :-: | :-: |

___

### [](#taskwarrior---todo--gestión-de-tareas)[`taskwarrior`](https://github.com/GothenburgBitFactory/taskwarrior) - Todo + gestión de tareas

> `taskwarrior` es una aplicación CLI de gestión de tareas/todo. Es simple y discreta, pero también increíblemente potente y escalable, con funciones avanzadas de organización y consulta. También hay un montón (¡más de 700!) de [plugins] adicionales (https://taskwarrior.org/tools/) para ampliar su funcionalidad e integrarse con servicios de terceros.

![task-warrior-example-usage](assets/50-taskwarrior.webp)

| [Ver taskwarrior en GitHub](https://github.com/GothenburgBitFactory/taskwarrior) | [Autor GothenburgBitFactory](https://github.com/GothenburgBitFactory) | Escrito en C++ |
| :-: | :-: | :-: |

___

### [](#tuir---terminal-ui-para-reddit)[`tuir`](https://gitlab.com/ajak/tuir) - Terminal UI para Reddit

> `tuir` es genial si quieres parecer que estás trabajando, ¡mientras en realidad navegas por Reddit! Tiene combinaciones de teclas intuitivas, temas personalizados, y también puede renderizar imágenes y contenido multimedia. También está [haxor](https://github.com/donnemartin/haxor-news) para noticias de hackers.

![tuir-example-usage](assets/50-tuir.webp)

| [Ver tuir on GitLab](https://gitlab.com/ajak/tuir) | [Autor ajak](https://github.com/ajak) | Escrito en Python |
| :-: | :-: | :-: |
___

## Dev Tools

### [](#httpie---cliente-de-pruebas-http--api)[`httpie`](https://github.com/httpie/httpie) - Cliente de pruebas HTTP / API

> `httpie` es un cliente HTTP, para pruebas, depuración y uso de APIs. Soporta todo lo que se puede esperar - HTTPS, proxies, autenticación, cabeceras personalizadas, sesiones persistentes, análisis JSON. El uso es simple con una sintaxis expresiva y salida coloreada. Al igual que otros clientes HTTP (Postman, Hopscotch, Insomnia, etc) HTTPie también incluye una interfaz web.

![httpie-example-usage](assets/50-httpie.webp)

| [Ver httpie en GitHub](https://github.com/httpie/httpie) | [Autor httpie](https://github.com/httpie) | Escrito en Python |
| :-: | :-: | :-: |

___

### [](#lazydocker---aplicación-completa-de-gestión-de-docker)[`lazydocker`](https://github.com/jesseduffield/lazydocker) - Aplicación completa de gestión de Docker

> `lazydocker` es una aplicación de gestión de Docker, que te permite Ver todos los contenedores e imágenes, gestionar su estado, leer registros, comprobar el uso de recursos, reiniciar/reconstruir, analizar capas, podar contenedores, imágenes y volúmenes no utilizados, y mucho más. Te ahorra la necesidad de recordar, escribir y encadenar múltiples comandos Docker.

![lazy-docker-example-usage](assets/50-lazydocker.webp)

| [Ver lazydocker en GitHub](https://github.com/jesseduffield/lazydocker) | [Autor jesseduffield](https://github.com/jesseduffield) | Escrito en Go |
| :-: | :-: | :-: |

___

### [](#lazygit---aplicación-completa-de-gestión-git)[`lazygit`](https://github.com/jesseduffield/lazygit) - Aplicación completa de gestión Git

> `lazygit` es un cliente git visual, en la línea de comandos. Fácilmente añadir, confirmar y puch archivos, resolver conflictos, comparar diffs, gestión de registros, y hacer operaciones complejas como aplasta y rebobina. Hay combinaciones de teclas para todo, colores, y es fácilmente configurable y ampliable.

![lazy-git-example-usage](assets/50-lazygit.webp)

| [Ver lazygit en GitHub](https://github.com/jesseduffield/lazygit) | [Autor jesseduffield](https://github.com/jesseduffield) | Escrito en Go |
| :-: | :-: | :-: |

___

### [](#kdash---aplicación-del-panel-de-control-de-kubernetes)[`kdash`](https://github.com/kdash-rs/kdash/) - Aplicación del panel de control de Kubernetes

> `kdash` es una herramienta de gestión de Kubernetes todo en uno. Ver métricas de nodo, ver recursos, transmitir registros de contenedor, analizar contextos y gestionar nodos, pods y espacios de nombres.

| [Ver kdash en GitHub](https://github.com/kdash-rs/kdash/) | [Autor kdash-rs](https://github.com/kdash-rs) | Escrito en Rust |
| :-: | :-: | :-: |

___

### [](#gdb-dashboard---depurador-de-visual-gdp)[`gdb-dashboard`](https://github.com/cyrus-and/gdb-dashboard) - Depurador Visual de GDB

> `gdb-dashboard` añade un elemento visual al depurador de GNU, para depurar programas C y C++. Analiza fácilmente la memoria, pasa por puntos de interrupción y registros Ver.

![gdb-dashboard-example-usage](assets/50-gdp-dashboard.webp)

| [Ver gdb-dashboard en GitHub](https://github.com/cyrus-and/gdb-dashboard) | [Autor cyrus-and](https://github.com/cyrus-and) | Escrito en Python |
| :-: | :-: | :-: |

___


## Servicios Externos

### [](#ngrok---proxy-inverso-para-compartir-localhost)[`ngrok`](https://ngrok.com/) - Proxy inverso para compartir localhost

> `ngrok` de forma segura* expone tu localhost a internet detrás de una URL única. Esto te permite compartir lo que estás trabajando con tus colegas remotos, en tiempo real. El uso es muy simple, pero también tiene un montón de características avanzadas para cosas como la autenticación, webhooks, cortafuegos, inspección de tráfico, dominios personalizados / comodín y mucho más.

![ngrok-example-usage](assets/50-ngrok.webp)

| [Ver ngrok en GitHub](https://github.com/inconshreveable/ngrok) | [Autor inconshreveable](https://github.com/inconshreveable) | Escrito en Go |
| :-: | :-: | :-: |

___

### [](#tmate---compartir-una-sesión-de-terminal-a-través-de-internet)[`tmate`](https://tmate.io/) - Compartir una sesión de terminal a través de Internet

> `tmate` te permite compartir instantáneamente una sesión de terminal en vivo con alguien en otra parte del mundo. Funciona a través de diferentes sistemas, soporta control de acceso / auth, puede ser auto-alojado, y tiene todas las características de Tmux

| [Ver tmate en GitHub](https://github.com/tmate-io/tmate) | [Autor tmate-io](https://github.com/tmate-io) | Escrito en C |
| :-: | :-: | :-: |

___

### [](#asciinema---grabar-y-compartir-sesiones-de-terminal)[`asciinema`](https://asciinema.org/) - Grabar y compartir sesiones de terminal

> `asciinema` es muy útil para grabar, compartir e incrustar fácilmente una sesión de terminal. Ideal para mostrar algo que has construido, o para mostrar los pasos de línea de comandos para un tutorial. A diferencia de los vídeos de grabación de pantalla, el usuario puede copiar y pegar el contenido, cambiar el tema sobre la marcha y controlar la reproducción.

| [Ver asciinema en GitHub](https://github.com/asciinema/asciinema) | [Autor asciinema](https://github.com/asciinema) | Escrito en Python |
| :-: | :-: | :-: |

___

### [](#navi---hoja-de-trucos-interactiva)[`navi`](https://github.com/denisidoro/navi) - Hoja de trucos interactiva

> `navi` permite navegar por las hojas de trucos y ejecutar comandos. Los valores sugeridos para los argumentos se muestran dinámicamente en una lista. Escribe menos, reduce los errores y ahórrate tener que memorizar miles de comandos. Se integra con [tldr](https://github.com/tldr-pages/tldr) y [cheat.sh](https://github.com/chubin/cheat.sh) para obtener contenido, pero también puedes importar otras cheatsheets, o incluso escribir las tuyas propias.

| [Ver navi en GitHub](https://github.com/denisidoro/navi) | [Autor denisidoro](https://github.com/denisidoro) | Escrito en Rust |
| :-: | :-: | :-: |

___

### [](#transfersh---intercambio-rápido-de-archivos)[`transfer.sh`](https://github.com/dutchcoders/transfer.sh/) - Intercambio rápido de archivos

> `transfer` hace que subir y compartir archivos sea realmente fácil, directamente desde la línea de comandos. Es gratis, soporta encriptación, te da una URL única, y también puede ser auto-alojado.
> He escrito una función de ayuda Bash para hacer el uso un poco más fácil, puedes [encontrarla aquí](https://github.com/Lissy93/dotfiles/blob/master/utils/transfer.sh) o probarla ejecutando `bash <(curl -L -s https://alicia.url.lol/transfer)`.

![transfer-sh-example-usage](assets/50-transfer-sh.webp)

| [Ver transfer.sh en GitHub](https://github.com/dutchcoders/transfer.sh) | [Autor dutchcoders](https://github.com/dutchcoders) | Escrito en Go |
| :-: | :-: | :-: |

___

### [](#surge---despliegue-un-sitio-en-segundos)[`surge`](https://surge.sh/) - Despliegue un sitio en segundos

> `surge` es un proveedor de alojamiento estático gratuito, que puedes desplegar directamente desde el terminal en un solo comando, ¡sólo ejecuta `surge` desde dentro de tu directorio `dist`! Soporta dominios personalizados, certificados SSL automáticos, soporte pushState, soporte de recursos cross-origin - ¡y es gratis!

![surge-sh-example-usage](assets/50-surge.webp)

___

### [](#wttrin---compruebe-el-tiempo)[`wttr.in`](https://github.com/chubin/wttr.in) - Compruebe el tiempo

> `wttr.in` es un servicio que muestra el tiempo en un formato digerible en la línea de comandos. Sólo tienes que ejecutar `curl wttr.in` o `curl wttr.in/London` para probarlo. Hay parámetros de URL para personalizar los datos devueltos, así como el formato.

![wrrt-in-example-usage](assets/50-wttr-in.webp)

| [Ver wttr.in en GitHub](https://github.com/chubin/wttr.in) | [Autor chubin](https://github.com/chubin) | Escrito en Python |
| :-: | :-: | :-: |

___

## Divertidos

### [](#cowsay---haz-que-una-vaca-ascii-diga-tu-mensaje)[`cowsay`](https://en.wikipedia.org/wiki/Cowsay) - Haz que una vaca ASCII diga tu mensaje

> `cowsay` es una vaca parlante configurable. Está basado en el [original](https://github.com/tnalpgge/rank-amateur-cowsay) de Tony Monroe

![cowsay-example-usage](assets/50-cowsay.webp)

| [Ver cowsay en GitHub](https://github.com/piuccio/cowsay) | [Autor piuccio](https://github.com/piuccio) | Escrito en JavaScript |
| :-: | :-: | :-: |

___

### [](#figlet---texto-de-salida-como-texto-de-arte-ascii-grande)[`figlet`](http://www.figlet.org/) - Texto de salida como texto de arte ASCII grande

> `figlet` muestra el texto como arte ASCII

![figlet-example-usage](assets/50-figlet.webp)

| [Ver figlet en GitHub](https://github.com/cmatsuoka/figlet) | [Autor cmatsuoka](https://github.com/cmatsuoka) | Escrito en C |
| :-: | :-: | :-: |

___

### [](#lolcat---haz-que-la-salida-de-la-consola-tenga-los-colores-del-arco-iris)[`lolcat`](https://github.com/busyloop/lolcat) - Haz que la salida de la consola tenga los colores del arco iris

> `lolcat` colorea de arco iris cualquier texto que se le pase

![lolcat-example-usage](assets/50-lolcat.webp)

| [Ver lolcat en GitHub](https://github.com/busyloop/lolcat) | [Autor busyloop](https://github.com/busyloop) | Escrito en Ruby |
| :-: | :-: | :-: |

___

### [](#neofetch---mostrar-datos-del-sistema-e-información-de-la-distribución)[`neofetch`](https://github.com/dylanaraps/neofetch) - Mostrar datos del sistema e información de la distribución

> `neofetch` imprime información de la distro y del sistema (para que puedas flexionar que usas Arch btw en r/unixporn)

![neofetch-example-usage](assets/50-neofetch.webp)

| [Ver neofetch en GitHub](https://github.com/dylanaraps/neofetch) | [Autor dylanaraps](https://github.com/dylanaraps) | Escrito en Bash |
| :-: | :-: | :-: |

Como ejemplo, estoy usando `cowsay`, `figlet`, `lolcat` y `neofetch` para crear un MOTD personalizado basado en el tiempo que se muestra al usuario cuando se conecta por primera vez. Les saluda por su nombre, muestra información del servidor y la hora, fecha, tiempo e IP. [Aquí está el código fuente](https://github.com/Lissy93/dotfiles/blob/master/utils/welcome-banner.sh).

![welcome](assets/50-neofetch-2.webp)
___

## Instalación y Gestión

La mayoría de nosotros tenemos un conjunto básico de aplicaciones y utilidades CLI en las que confiamos. Configurar una nueva máquina e instalar cada programa individualmente sería muy tedioso. Por eso, la tarea de instalar y actualizar tus apps de terminal es perfecta para automatizar. [Aquí](https://github.com/Lissy93/dotfiles/tree/master/scripts/installs) tienes algunos scripts de ejemplo que he escrito, que puedes añadir fácilmente a tus dotfiles o ejecutar de forma independiente para asegurarte de que nunca te falte una app.

Para usuarios de macOS, el método más sencillo es usar [Homebrew](https://brew.sh/). Solo tienes que crear un Brewfile (con `touch ~/.Brewfile`), luego listar cada una de tus apps y ejecutar `brew bundle`. Puedes mantener tu lista de paquetes respaldada poniéndola en un repositorio Git. Aquí tienes un ejemplo para empezar: [https://github.com/Lissy93/Brewfile](https://github.com/Lissy93/Brewfile)

En Linux, normalmente querrás usar el gestor de paquetes nativo (por ejemplo, `pacman`, `apt`). Por ejemplo, [aquí tienes un script](https://github.com/Lissy93/dotfiles/blob/master/scripts/installs/arch-pacman.sh) para instalar las apps anteriores en sistemas Arch Linux.

Las aplicaciones de escritorio en Linux pueden gestionarse de forma similar, usando Flatpak. De nuevo, [aquí tienes un script de ejemplo](https://github.com/Lissy93/dotfiles/blob/master/scripts/installs/flatpak.sh) :)

___

## Conclusión

Y eso es todo: una lista de útiles aplicaciones CLI y un método para instalarlas y mantenerlas actualizadas en todos tus sistemas.

Espero que algunas de estas te sean útiles :)

¡Me encantaría saber cuáles son tus aplicaciones CLI favoritas! Déjalo en los comentarios abajo.

### Información adicional

#### Qué no se incluyó

-   Esta lista no incluye lo básico, como Vim, Tmux, Ranger, ZSH, Git, etc., que probablemente ya usas
-   Tampoco he incluido nada demasiado específico o solo relevante para pocos usuarios
-   No se incluye nada específico de un sistema o que no sea multiplataforma (Linux/Unix, macOS)
-   Tampoco apps relacionadas con la terminal pero que no sean CLI (como emuladores de terminal)
-   Para la mayoría de los proyectos listados, hay muchas alternativas que logran cosas similares; por brevedad, esas tampoco se incluyeron

#### Créditos

Un gran reconocimiento a los autores y comunidades detrás de cada una de estas apps. Sin ellos y su trabajo, nuestra vida en la línea de comandos sería mucho menos genial. Donde ha sido posible, he intentado dar crédito a los autores, pero si me he olvidado de alguno, avísame abajo y haré una actualización.

#### Comentarios

¿Qué me he perdido? Me encantaría conocer tus aplicaciones CLI favoritas, ¡especialmente si hay alguna increíble que no he incluido!

También me gustaría conocer tus opiniones y sugerencias; siempre busco mejorar :)

#### Más información

Si te ha gustado esto, te recomiendo que eches un vistazo también a:

-   **[terminals-are-sexy](https://github.com/k4m4/terminals-are-sexy)** por Nikolaos Kamarinakis
-   **[awesome-shell](https://github.com/alebcay/awesome-shell)** por Caleb Xu
-   **[awesome-cli-apps](https://github.com/agarrharr/awesome-cli-apps)** por Adam Garrett-Harris

Si eres nuevo en la línea de comandos, **[The Art of Command Line](https://github.com/jlevy/the-art-of-command-line)**, de Joshua Levy, es un recurso excelente, al igual que **[Bash Guide](https://github.com/Idnan/bash-guide)**, de Adnan Ahmed.

Y si buscas inspiración, te encantará **[r/unixporn](https://www.reddit.com/r/unixporn/)** ⚡

___

* La versión original de este artículo se puede encontrar en [dev.to/lissy93](https://dev.to/lissy93/cli-tools-you-cant-live-without-57f6) (inglés).

* Autoría por [Alicia Sykes](https://www.aliciasykes.com/), traducción por [@elflacodeit](https://www.instagram.com/elflacodeit/), formateo y revisión por [@axelvf](https://www.instagram.com/axelvf/)
