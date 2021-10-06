---
title: "Más detalles sobre la falla del 4 de Octubre de Facebook."
date: 2021-10-05
draft: false

description: "Más detalles sobre la falla del 4 de Octubre de Facebook."

keywords:
    - facebook
    - outage
tags:
    - sysarmy
    - facebook
    - outage
topics:
    - outage

thumbnail: assets/facebook-outage-details-20211005.jpg
socialImage: assets/facebook-outage-details-20211005.jpg
featuredImage: assets/facebook-outage-details-20211005.jpg
---

NdE: Tomamos el [Artículo original](https://engineering.fb.com/2021/10/05/networking-traffic/outage-details/) y lo pasamos a español.

Ahora que nuestras plataformas están levantadas y corriendo como siempre después del corte de ayer, pensé que sería provechoso compartir un poco más de detalles de qué pasó y porqué, y lo mucho muy importante, que aprendimos de eso.

Este corte fue desencadenado por el sistema que maneja nuestra capacidad de red backbone global. El backbone es la red que Facebook construyó para conectar todas las instalaciones de cómputo juntas, que consiste en decenas de miles de cables de fibra óptica, atravesando el globo, y conectando todos nuestros centros de cómputos.

Esos centros de cómputos, vienen en diferentes  formas. Algunos son edificios enormes, que albergan millones de máquinas que guardan datos y corren el pesado procesamiento de datos que mantiene nuestras plataformas corriendo, y otras instalaciones más pequeñas, que conectan nuestra red backbone hacia “EL internet” y las personas que utilizan nuestras plataformas.

Cuando abrís una de nuestras apps y cargas tu feed o mensajes, el pedido de datos viaja desde tu dispositivo hasta la instalación más cercana, que se comunica directamente sobre nuestra red backbone, hasta un centro de cómputos más grande. Ahí es donde la información requerida por tu app, es recuperada y procesada, y se envía nuevamente por la red hasta tu dispositivo.

El tráfico entre todas estas instalaciones de cómputo, es manejado por routers, que resuelven a donde enviar toda la data que ingresa y que sale. Y el extenso día a día de trabajo, manteniendo esta infraestructura, nuestros ingenieros a veces necesitan que parte del backbone sea puesto offline para mantenimiento – quizás para reparar una línea de fibra, agregar más capacidad, o actualizar el software del mismo router.

Esta fue la raíz del corte de ayer. Mientras se realizaba una de estos trabajos de rutina de mantenimiento, se utilizó un comando con la intención de evaluar la disponibilidad de la capacidad del Backbone global, la cual inintencionadamente, dio de baja todas las conexiones de nuestra red troncal, desconectado efectivamente los centros de cómputos de Facebook a nivel global. Nuestros sistemas están diseñados para auditar los comandos como estos, para prevenir errores como este, pero un Bug en la herramienta de auditoría, no permitió que se detuviera el comando.

Este cambio causó una desconexión completa de nuestras conexiones de los servidores entre los centros de cómputos e internet. Y esa pérdida total de conexión, causó un segundo problema, que hizo que las cosas se pusieran peor.

Uno de los trabajos realizados por una de nuestras instalaciones  más pequeñas es responder a consultas de DNS. DNS es el libro de direcciones de internet, habilitando los nombres web simples que escribimos en los navegadores, en direcciones IP de servidores. Esas solicitudes de traducción son respondidas por nuestros nombres de servidores autoritarios que se ocupan de saber bien las direcciones IP, que sucesivamente son publicadas al resto de internet, a través de otros protocolos, llamados “Border Gateway Protocol” (BGP ó Protocolo de puerta de enlace fronteriza).

Para asegurar una operación confiable, los servidores de DNS, deshabilitan esos avisos de BGP, si ellos mismos no pueden comunicarse con nuestros centros de cómputos, desde que es una indicación de una conexión de red dañada. En el corte reciente, toda la red troncal fue retirada de operación, haciendo que estas locaciones se declaren a sí mismas dañadas, y retiraron esos avisos de BGP. El resultado final, fue que nuestros servidores de DNS, se volvieron inalcanzables a pesar de que estaban todavía operativos. Esto hizo que fuera imposible para el resto de internet encontrar nuestros servidores.
Todo esto pasó muy rápido. Y como nuestros ingenieros resolvieron que era lo que estaba pasando y porque, afrontaron dos grandes obstáculos: primero, no era posible acceder a nuestros centros de cómputos a través de nuestros medios normales, porque nuestra red estaba caída, y segundo, la pérdida total de los DNS, rompió muchas de las herramientas internas que normalmente usamos para investigar y resolver cortes como este.

Nuestra red primaria y  acceso fuera de banda estaba caída, así que enviamos ingenieros al centro de cómputos en persona, para que depuren el problema, y reinicien los sistemas. Pero esto tomó tiempo, porque estas instalaciones están diseñadas con altos niveles de seguridad física y de sistema en mente. Son difíciles de acceder, y cuando estás adentro, el hardware y los routers, están diseñados para que sean difíciles de modificar, aun cuando tengan acceso físico. Entonces tomó un tiempo extra activar el protocolo de acceso seguro necesarios para que las personas asistieran físicamente, y estuvieran habilitados para trabajar en los servidores. Solo en ese momento pudieron confirmar el problema y devolver nuestro backbone de nuevo en línea.

Una vez que nuestra conectividad de red backbone fue restablecida a través de las regiones de centros de cómputos, todo volvió con eso. Pero el problema no estaba terminado – sabíamos que volviendo a activar nuestros servicios todos al mismo tiempo, podía potencialmente causar un nuevo round de choques, debido al aumento en el tráfico. Los centros de cómputos de manera individual, estaban reportando caídas de tensión en el uso, en el rango de decenas de mega watts, y de repente revirtiendo una caída en el consumo de energía, podía poner en riesgo todo, desde sistemas eléctricos hasta caches.

Afortunadamente, este es un evento para el que estamos bien preparados gracias a los simulacros de “tormenta” que venimos realizando por un largo tiempo. En un ejercicio, simulamos una falla de un sistema mayor, poniendo offline un servicio, un centro de cómputos, o una región entera, haciendo pruebas de stress de toda la infraestructura y software involucrados. La experiencia de estos simulacros nos dieron la confianza y la experiencia para traer las cosas online de nuevo, y para manejar con cuidado el incremento de cargas. Al final, nuestros servicios volvieron a estar levantados relativamente rápido, sin ir más lejos, ninguna falla de todo el sistema. Y mientras nunca habíamos estado en una tormenta simulada de la caída de nuestro backbone global,  nosotros ciertamente estaremos buscando caminos para simular eventos como este hacia adelante.

Toda falla como esta, es una oportunidad de aprender y hacernos mejores, y es todo para nosotros poder aprender de esta. Después de todo asunto, pequeño o grande, nosotros hacemos una revisión del proceso, para entender cómo podemos hacer nuestros sistemas más flexibles. Ese proceso ya está en marcha.
Hemos hecho un trabajo extenso, endureciendo nuestros sistemas para prevenir accesos no autorizados, y fue interesante ver como ese endurecimiento nos ralentizó mientras tratábamos de recuperarnos del corte, causado no por actividad maliciosa, sino por un error de nuestra propia creación. Yo creo que un intercambio como este es valioso – un  incremento en la seguridad día a día, vs un recupero más lento del que un evento que  esperamos que sea raro. Desde aquí en más, nuestro trabajo es endurecer nuestros test, simulacros, y sobre todo la flexibilidad de estar seguros de que los eventos como este pasen tan raramente como sea posible.   

