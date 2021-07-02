---
title: "apt-undo, reinstalar paquetes removidos por error"
date: 2021-07-02
draft: false
description: "Una receta rápida para reinstalar paquetes removidos por error con apt."

keywords:
    - apt
    - apt-undo
    - linux
    - ubuntu
    - debian

tags:
    - linux
    - apt

topics:
    - linux administration

thumbnail: assets/apt-undo-cover.jpg
socialImage: assets/apt-undo-cover.jpg
featuredImage: assets/apt-undo-cover.jpg
---

Te llega un ticket: "No me puedo loguear al server", siendo hábiles operadores consultamos "hiciste algún cambio?" a lo que nos responden "solo desinstale un paquete".

![](https://media.giphy.com/media/TEHn0Ly4cyvPBXPAjR/giphy.gif)

El paquete desinstalado fue `python3` en un server con Ubuntu 20.04 que esta conectado a un Freeipa. La desintalacion se llevo puestos todos los paquetes del servicio sssd y además netplan por lo que al reiniciar el server (acción cuestionable pero necesaria) también perdimos conectividad.

El comando en cuestión `sudo apt autoremove python3`... 

En el log se puede observar el efecto devastador:

![](assets/apt-undo-python3.png)

## Se puede hacer un ctrl-z a esto? Se puede deshacer un apt autoremove? 

Si.

Las primeras búsquedas de Google apuntan a una herramienta `apt-undo` en [esta pregunta de StackOverflow](https://askubuntu.com/questions/247549/is-it-possible-to-undo-an-apt-get-install-command). Pero el ppa no esta más.

Sin embargo buscando mas a fondo aparece [esta respuesta en Stackoverflow](https://serverfault.com/questions/380856/how-to-undo-apt-get-remove) con un snippet de 4 lineas de bash salvador que dejamos a continuación. 

Simple y elegante busca en dpkg.log todo lo que fue Removido y arma la linea para volver a instalarlo con apt-get.

![](https://media.giphy.com/media/ugOMVsKh9pMWxji7w4/giphy.gif)

    echo '#!/bin/bash' > restore
    echo sudo apt-get install `grep Remove /var/log/apt/history.log | tail -1 | sed -e 's|Remove: ||g' -e 's|([^)]*)||g' -e 's|:[^ ]* ||g' -e 's|,||g'` >> restore
    chmod +x restore 
    ./restore

Es una solución final? probablemente no porque resta verificar si se removieron configuraciones u otros archivos locales, sin embargo al tener por lo menos los paquetes restaurados estamos mas cerca del punto de llegada.

Y por si no quedó claro, desinstalar paquetes como `python3` no es una buena idea.
