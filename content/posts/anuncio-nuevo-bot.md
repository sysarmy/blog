---
title: "Nuevo bot para nuestro server de Discord"
date: 2024-07-08
Description: "La semana pasada salio a producción el bot renovado para nuestro server de Discord. Aquí vas a encontrar información útil, y una introrucción a cómo colaborar."
draft: false

Keywords:
  - comunidad   
  - bot   
  - softwaredevelopment   
  - discord  
  - coding   
  - python

Tags:
  - discord  
  - coding   
  - python

Topics:
  - comunidad   
  - bot   
  - softwaredevelopment   
  - discord  
  - coding   
  - python

Thumbnail: assets/discordicon.png
socialImage: assets/discordicon.png
featuredImage: assets/discordicon.png
externalPermlink: "https://github.com/sysarmy/BOFH_discordbot"
---


Hola,

Finalmente nos decidimos a migrar el Bot de Discord y ya esta funcionando en el server de Sysarmy.

Esto fue algo que hicimos como proyecto personal nocturno, durante las últimas semanas / meses con @qwor01 (Nacho). ¿Por qué? 

Básicamente por tres razones:
- El bot actual estaba desactualizado. Fue codeado hace mucho por el gran Chino (sqee) en Perl, pero queremos mejorarlo y abrirlo a la comunidad.
- Estamos aburridos
- Proyecto personal para re-aprender python

**Algunos puntos importantes para aclarar:**

Somos muy juniors. No somos programadores Python (de hecho yo directamente no soy programador), por lo que consideramos esta versión del bot como la 0.1. **Hay código spaghetti. Hay mugre. Si. No se asusten.** Hay muchísimas cosas que se pueden mejorar, refactorizar, etc. Para eso lo opensourceamos.

Todas las contribuciones son bienvenidas y si tienen ganas de mejorar algo, simplemente manden pull request o nos contactan por el server. Por supuesto que si lo quieren usar para algún proyecto personal, adelante nomás 🙂 es GPL.

Toda la información técnica está en el readme del repo (https://github.com/sysarmy/BOFH_discordbot), pero si tienen ganas de agarrar la pala, acá van algunos puntos importantes para que tengan como contexto al momento de levantar el código:

1. **bridgebotID = **Ese es el ID de un segundo bot corriendo actualmente que tiene como función bridgear usuarios que vienen a Discord de otros canales (Telegram, IRC, Slack). Por una cuestión higiénica por ahora lo dejamos separado, pero en algún momento la idea sería poder también mergearlo.
2. **API keys = **Para algunas funciones usamos algunas APIs específicas de servicios como coinranking, weatherapi, etc. Revisar bien el readme y hacerse cuentas gratis ahí para probar. Si quieren probar algún proveedor / servicio similar, adelante. Pero por ahora usamos estas por una cuestión de costo y compatibilidad.

Eso es todo. Gracias especiales a:
- @godlike por ayudarnos con un par de consultas técnicas
- @jedux por el setup inicial, testing y hosting
- Sysarmy mods por el betatest
- Discord.py por documentar todo tan bien