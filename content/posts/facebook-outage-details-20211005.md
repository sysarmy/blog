---
title: "Más detalles sobre la falla del 4 de Octubre de Facebook."
date: 2021-10-05T19:12:18-03:00
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

Ahora que nuestras plataformas están funcionando como siempre después del corte de ayer, pensé que sería provechoso compartir con un poco más de detalle qué pasó y por qué, y lo más importante, que aprendimos de eso.

Este corte fue desencadenado por el sistema que maneja la capacidad de nuestra red de backbone global. El backbone es la red que Facebook construyó para interconectar todas las instalaciones de cómputo, que consiste en decenas de miles de kilómetros de cables de fibra óptica alrededor del mundo, y conectando todos nuestros centros de cómputos.

Esos centros de cómputos, vienen en diferentes formas. Algunos son edificios enormes, que albergan millones de máquinas que guardan datos y corren el pesado procesamiento de datos que mantiene nuestras plataformas corriendo, y otras instalaciones más pequeñas que conectan nuestra red de backbone hacia Internet y las personas que utilizan nuestras plataformas.

Cuando abrís una de nuestras aplicaciones y cargas tu feed o mensajes, el pedido de datos viaja desde tu dispositivo hasta la instalación más cercana, que se comunica directamente sobre nuestra red de backbone hasta un centro de cómputos más grande. Ahí es donde la información requerida por tu aplicación es recuperada, procesada y enviada nuevamente por la red hasta tu dispositivo.

El tráfico entre todas estas instalaciones de cómputo es manejado por routers, que resuelven a donde enviar toda la información que ingresa y que sale. Y en el día a día de trabajo manteniendo esta infraestructura, nuestros ingenieros a veces necesitan que parte del backbone sea puesto offline para mantenimiento – quizás para reparar una línea de fibra, agregar más capacidad, o actualizar el software del mismo router.

Esta fue la raíz del corte de ayer. Mientras se realizaba una de estos trabajos de rutina de mantenimiento, se utilizó un comando con la intención de evaluar la disponibilidad de la capacidad del backbone global, la cual inintencionadamente dio de baja todas las conexiones de nuestra red de backbone, desconectando efectivamente los centros de cómputos de Facebook a nivel global. Nuestros sistemas están diseñados para auditar este tipo de comandos, para prevenir errores como este, pero un bug en la herramienta de auditoría evitó que se detuviera el comando.

Este cambio causó una desconexión completa de nuestras conexiones de los servidores entre los centros de cómputos e Internet. Y esa pérdida total de conexión, causó un segundo problema que hizo que las cosas empeoraran.

Uno de los trabajos realizados por nuestras instalaciones más pequeñas es responder a consultas de DNS. DNS es la libreta de direcciones de Internet, permitiendo que los nombres de web simples que escribimos en los navegadores sean traducidos en direcciones IP de servidores. Esas solicitudes de traducción son respondidas por nuestros DNS autoritativos que residen en segmentos de red específicos, que luego son anunciados al resto de Internet a través de otro protocolo llamado “Border Gateway Protocol” (BGP ó Protocolo de puerta de enlace fronteriza).

Para asegurar una operación confiable, los servidores de DNS deshabilitan esos anuncios de BGP si ellos mismos no pueden comunicarse con nuestros centros de cómputos, dado que es una indicación de una conexión de red que no está funcionando. En el corte reciente, toda la red de backbone fue removida de operación, haciendo que estas locaciones se declaren a sí mismas como no saludables y retiraron esos anuncios de BGP. El resultado final, fue que nuestros servidores de DNS, se volvieron inalcanzables a pesar de que estaban operativos. Esto hizo que fuera imposible para el resto de Internet encontrar nuestros servidores.

Todo esto pasó muy rápido. Y mientras nuestros ingenieros trabajaban para determinar que era lo que estaba pasando y por qué, afrontaron dos grandes obstáculos: primero, no era posible acceder a nuestros centros de cómputos a través de los medios normales porque nuestra red estaba caída, y segundo, la pérdida total de los DNS rompió muchas de las herramientas internas que normalmente usamos para investigar y resolver cortes como este.

Nuestra red primaria y acceso fuera de banda estaba caída, así que enviamos ingenieros al centro de cómputos en persona para que diagnostiquen el problema y reinicien los sistemas. Pero esto tomó tiempo, porque estas instalaciones están diseñadas con altos niveles de seguridad física y lógica en mente. Son difíciles de acceder, y cuando estás adentro el hardware y los routers están diseñados para que sean difíciles de modificar aún cuando tengan acceso físico. Entonces tomó un tiempo extra activar el protocolo de acceso seguro necesario para que las personas accedieran físicamente y estuvieran en condiciones de trabajar en los servidores. Solo en ese momento pudimos confirmar el problema y poner de nuevo en línea la red de backbone.

Una vez que la conectividad de nuestra red de backbone fue restablecida a en nuestros centros de cómputos de diferentes regiones de, todos los servicios se restrablecieron. Pero el problema no estaba terminado – sabíamos que si volvíamos a activar nuestros servicios todos al mismo tiempo podía potencialmente causar nuevas caídas, debido al rápido aumento en el tráfico. Los centros de cómputos de manera individual estaban reportando caídas de tensión en el uso en el rango de las decenas de megawatts, y revertir repentinamente una caída en el consumo de energía podía poner en riesgo todo, desde sistemas eléctricos hasta caches.

Afortunadamente, este es un evento para el que estamos bien preparados gracias a los simulacros de “tormenta” que venimos realizando hace un largo tiempo. En un ejercicio simulamos una falla importante de un sistema, poniendo offline un servicio, un centro de cómputos o una región entera y haciendo pruebas de stress sobre toda la infraestructura y software involucrados. La experiencia de estos simulacros nos dio la confianza y la experiencia para traer las cosas online nuevamente y para manejar con cuidado el incremento de cargas. Finalmente, nuestros servicios volvieron a funcionar relativamente rápido y sin ninguna falla general. Y si bien nunca habíamos simulado una tormenta que implicara la caída de nuestra red de backbone global, ciertamente estaremos buscando maneras para simular eventos como este en el futuro.

Toda falla como esta es una oportunidad de aprender y hacernos mejores, y hay mucho que podemos aprender de este evento. Después de todo problema, pequeño o grande, hacemos un proceso de revisión para entender cómo podemos hacer nuestros sistemas más resilientes. Ese proceso ya está en marcha.

Hemos hecho un trabajo intenso endureciendo nuestros sistemas para prevenir accesos no autorizados, y fue interesante ver como ese endurecimiento nos ralentizó mientras tratábamos de recuperarnos del corte, causado no por actividad maliciosa, sino por un error de nuestra propia creación. Yo creo que encontrar el balance es importante – un  incremento en la seguridad del día a día versus un recupero más lento de un evento que esperamos ocurra con muy poca frecuencia. Desde aquí en más, nuestro trabajo es endurecer nuestros tests, simulacros, y sobre todo la resiliencia para estar seguros de que los eventos como este pasen con la menor frecuencia que sea posible.   

