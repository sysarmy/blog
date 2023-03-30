---
Title: ¿De dónde viene PING? ¿Cuál es su verdadera función? Yo te cuento.
Description: "Historia de las tecnologías de información: el comando PING."
Keywords:
- ping
- redes
- sistemas

Tags:
- ping 
- redes
- internet

Thumbnail: assets/ale-ping.png
socialImage: assets/ale-ping.png
featuredImage: assets/ale-ping.png

Topics:
- internet 
- historia
- redes
- sistemas

markup: markdown
date: 2023-03-30
draft: false
---

Ping, etimológicamente hablando, es, o mejor dicho, era, el sonido que emitía un sonar. El sonido era muy parecido al que emite un objeto al golpear una superficie metálica. Piensen en una campanita de escritorio de hotel o de la cocina de un restaurant, por ejemplo.

En inglés, la onomatopeya, o la descripción de ese sonido particular se escribe como "_ping_" supongo que en castellano diríamos "_tilín_" (Jaja).

En fin, por qué les cuento esto, porque, justamente, el sonar de un submarino (_SOund NAvigation and Ranging_) emite ese pulso de sonido. Dicho pulso viaja en forma sub-acuática hasta que se topa con alguna superficie y allí regresa. Luego el sonar calcula el tiempo que tardó (viajando a la velocidad del sonido) entre que salió del pinger del sonar hasta que volvió, y con eso miden la distancia y la posición del objeto.

Funciona de una manera muy similar al radar (_RAdio Detection And Ranging_) excepto que el radar emite señales de radio en vez de sonido (que en definitiva son la misma cosa).

> _Nota al márgen:_ El sonido es una onda al igual que la radio, pero, a diferencia de esta última, no es electromagnética. Es decir, el sonido no requiere de electricidad para propagarse PERO sí requiere de un medio. El sonido no se puede propagar en el vacío, y las ondas electromagnéticas si. Imaginense si el sonido pudiera propagarse en el vacío, las explosiones solares serían insoportables en la superficie terrestre.  

¿Qué tiene que ver todo esto con el ping que utilizamos en administración de sistemas?  

Porque, justamente, el ping (software) se desarrolló en la división de informática de la armada estadounidense a inicios de los años 80.

El Ping tiene mi edad, 39 años. Se inventó en diciembre de 1983. Su propósito fue inspirado en el sonar submarino.  

Ping utiliza el [protocolo ICMP](https://es.wikipedia.org/wiki/Protocolo_de_control_de_mensajes_de_Internet) (Internet Control Message Protocol) sobre IP. Es decir, puede enviar una solicitud ICMP echo a un host objetivo cualquiera y luego cuando el host recibe la solicitud y la responde automáticamente con un [ICMP echo](https://es.wikipedia.org/wiki/Protocolo_de_control_de_mensajes_de_Internet#Echo_Reply), el programa la recibe y, fundamentalmente calcula el tiempo que tardó en enviar y recibir, si han habido perdidas de paquetes y luego un promedio de lo que ha tardado el ida y vuelta de las solicitudes y respuestas recibidas.  

El PING puede diagnosticar latencia pero no es muy eficaz en muchos casos por que no siempre una latencia en un resultado ping es un indicador del estado de la red, ya que nada nos garantiza que el software del otro lado este funcionando correctamente, esté respondiendo en forma instantánea, o no esté ignorando ICMP echo requests.

El uso más práctico de la utilidad PING es para ver si podemos alcanzar un host desde nuestra red o subred rápidamente. Es una herramienta de análisis que nunca debe utilizarse por sí sola, por los motivos detallados en el párrafo anterior pero que nos pueden dar una idea de donde estamos.

* Por [Alexia Rivera](https://lachicadesistemas.com.ar) para Sysarmy.