---
Description: "¿Qué es Docker y qué soluciones brinda?"
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
Title: ¿Qué es Docker y qué soluciones brinda?
Topics:
- sysarmy
- docker
- containers
- linux
markup: markdown
date: 2020-04-11
---

Es probable que la palabra [_contenedores_](https://www.docker.com/resources/what-container) sea moneda corriente en nuestro lugar de trabajo o algo relativamente desconocido. De una u otra forma, la necesidad de utilizarlos va creciendo a medida que lo hace la complejidad de las aplicaciones que creamos. Cuando cada una de ellas depende de ciertas librerías, de algún intérprete específico, o de una base de datos en particular, necesitamos tener cuidado para que no entren en conflicto unas con otras. Es ahí donde Docker entra en juego para facilitar el desarrollo, el despliegue y el funcionamiento de nuestras aplicaciones al mejor estilo plug and play: instalamos y funciona. En este artículo compartimos una explicación de alto nivel sobre cómo sucede todo esto detrás de escena.

## Ya hablamos de contenedores, pero… ¿qué son?

Si no podemos asegurarnos de que nuestras aplicaciones funcionen de la misma forma en los servidores donde las desplegamos que en nuestros entornos de desarrollo, nuestro destino es pasar largas horas solucionando problemas en producción. Por suerte, hay una alternativa mucho más feliz (y prácticamente libre de riesgos) utilizando contenedores Docker en Linux.

> Cuando decimos Docker, por lo general nos referimos al servicio que hace posible ejecutar contenedores, comúnmente llamado Docker Engine. Debido a que comparte el nombre con [la empresa](https://www.docker.com/) y la comunidad que la crearon y la mantienen, suele ser difícil precisar -al menos al principio- sobre cuál estamos hablando en un momento dado. Además, la herramienta que se provee para gestionar contenedores se llama de igual forma, aunque con la primera letra en minúsculas (`docker`). 

La manera más simple de entender qué es un contenedor es comenzar pensando en **un paquete que incluye tanto una aplicación como todo lo necesario para que funcione**. Este paquete recibe el nombre de **imagen** y se convierte en **contenedor** propiamente dicho cuando se ejecuta por primera vez. De largada, esto nos libera de la necesidad de disponer de un entorno de desarrollo complejo y nos ahorra el tiempo de puesta en funcionamiento y el gasto extra de infraestructura. Al mismo tiempo, nos asegura que cuando movemos un contenedor de un ambiente a otro (desarrollo / prueba / producción) no habrá inconvenientes porque todo lo que necesita está incluído en sí mismo. 

Más estrictamente hablando, podemos considerar a un contenedor como **un ambiente que ejecuta sus propios procesos, tiene sus propias interfaces de red y puntos de montaje, y se encuentra completamente aislado de otros contenedores**, lo que aumenta la seguridad. Sin embargo, accede al kernel del sistema operativo donde está instalado a través de Docker (o mejor dicho, del Docker Engine) como se observa en la imagen de abajo:

![Estructura de Docker](/assets/estructura-docker.png)

Otra característica distintiva que vemos arriba es que, a diferencia de la virtualización tradicional (que emula hardware), Docker hace lo propio con el kernel del sistema operativo (lo comparte entre todos los contenedores que administra). Por esta razón, los contenedores tienden a ser pequeños en tamaño y en uso de recursos comparados a una máquina virtual ya que no requieren un sistema operativo propio para funcionar (otra ventaja para anotar).

## Instalar Docker

Pensar en máquinas virtuales vs. contenedores es útil para entender la diferencia conceptual entre ambas tecnologías, pero no significa que una necesariamente deba excluir a la otra. Más bien, cuando las combinamos instalando Docker y ejecutando contenedores sobre una máquina virtual, obtenemos lo mejor de ambos mundos.
La opción recomendada para instalar Docker Engine CE (Community Edition) en Linux consiste en seguir los siguientes pasos:

1. Asegurarnos de que no hay otra versión de Docker instalada en el sistema 

Puede suceder que el gestor de nuestra distribución no encuentre los siguientes paquetes instalados en primera instancia, pero eso no es nada para alarmarse.

**Debian / Ubuntu:**

    sudo apt-get purge docker docker-engine docker.io containerd runc

**CentOS:**

    sudo yum remove docker docker-client docker-client-latest docker-common docker-latest docker-latest-logrotate docker-logrotate docker-engine

2. Instalar dependencias y agregar los repositorios de Docker incluyendo la clave GPG

**Debian / Ubuntu** (actualizamos el índice de paquetes al comienzo y al final):

    sudo apt-get update
    sudo apt-get install apt-transport-https ca-certificates curl gnupg2 software-properties-common
    curl -fsSL https://download.docker.com/linux/debian/gpg | sudo apt-key add -
    sudo add-apt-repository "deb [arch=amd64] https://download.docker.com/linux/debian $(lsb_release -cs) stable"
    sudo apt-get update

**CentOS**:

    sudo yum install -y yum-utils device-mapper-persistent-data lvm2
    sudo yum-config-manager --add-repo https://download.docker.com/linux/centos/docker-ce.repo

3. Instalar Docker

**Debian / Ubuntu:**

    sudo apt-get install docker-ce docker-ce-cli containerd.io

**CentOS:**

    sudo yum install docker-ce docker-ce-cli containerd.io

4. Iniciar el servicio

    sudo systemctl start docker

Una vez que Docker Engine esté ejecutándose, podremos crear un contenedor simple como explicamos a continuación. Si bien es posible crear un contenedor desde cero, para finalizar este artículo haremos uso de una imagen previamente creada.

## Nuestro primer contenedor

[Docker Hub](https://hub.docker.com/) es un repositorio de imágenes Docker que contiene tanto alternativas oficiales (creadas y mantenidas por empresas) como no oficiales (provenientes de desarrolladores individuales o equipos independientes de cualquier parte del mundo). Una de las imágenes más populares que se utiliza a menudo con fines didácticos al introducir el mundo de Docker a nuevos adeptos es **whalesay**, una variación del **cowsay** clásico de Linux. Como es de esperarse, la figura que se muestra es una ballena (del logo de Docker) en vez de la famosa vaca.

Para ejecutar **whalesay** utilizaremos `docker run` de la siguiente forma. La primera vez que lo hagamos, `docker` descargará la imagen de Docker Hub, mientras que en ejecuciones posteriores la utilizará sin necesidad de hacerlo nuevamente.

    sudo docker run docker/whalesay cowsay "Aguanten Docker y sysarmy!"

![Ejecución de whalesay](/assets/docker-whalesay-sysarmy.png)

En próximos artículos describiremos otros comandos para administrar contenedores y crear los nuestros propios. ¡Nos leemos en breve!