---
Description: "Proxyjump, la opción de SSH de la que probablemente nunca hayas escuchado hablar"
Keywords:
- sysadmin 
- ssh
- proxy
- jumphost
- bastion
Section: 
Tags:
- sysadmin 
- ssh
- proxy
- jumphost
- bastion
Thumbnail: assets/proxyjump_5_akrI3NN_Ai7lO1ci.jpg
socialImage: assets/proxyjump_5_akrI3NN_Ai7lO1ci.jpg
featuredImage: assets/proxyjump_5_akrI3NN_Ai7lO1ci.jpg
Title: "Proxyjump, la opción de SSH de la que probablemente nunca hayas escuchado hablar"
Topics:
- sysadmin 
- ssh
- proxy
- jumphost
- scripts
- bastion
markup: markdown
date: 2020-12-19
draft: false

---

Hoy en día, es cada vez más común que los Penetration Testers, los investigadores de seguridad, Red Teams y **casi cualquier persona que trabaje en sistemas** requieran algún tipo de tunneling dentro y fuera de la infraestructura de una organización. Los red teams  internos, especialmente, que pueden necesitar delimitar su infraestructura de comando y control, probablemente emplearán túneles [SSH](https://www.ssh.com/ssh/tunneling/) (o VPN, pero esa será en otra publicación) de su infraestructura externa (como callback servers, alojamiento web, correo, etc. ) hacia los activos Internos. 

La configuración de estos túneles puede volverse bastante compleja y difícil de administrar, especialmente una vez que aumenta el número de saltos entre servidores.

<!--more-->

# Tunneling

![](assets/proxyjump_0_6CDo8qwaLsxZcFB8.jpg)

Los túneles SSH en cascada pueden ser un verdadero dolor de cabeza.
Para el propósito de esta publicación de blog, se ha configurado un entorno como se muestra a continuación. El objetivo es garantizar que los beacons de las víctimas puedan llegar al teamserver host que se encuentra en las profundidades del datacenter corporativo.

![](assets/proxyjump_1_QtXI5oI-D15ceS3z.png)

Históricamente, debido a mi propia ignorancia de las opciones avanzadas de SSH, intentaría administrar estos múltiples túneles conectando en cascada cada túnel a otro:

![](assets/proxyjump_2_zlM5vN8xcIZKD3Nt.png)

Para asegurar que las balizas lleguen al último salto podría llegar al teamserver interno, los comandos de túnel múltiples se ven así:

    [teamserver]
    ssh -R 8080:127.0.0.1:80 internal-proxy -f -N

    [Int. Proxy Server]
    ssh -R 8080:127.0.0.1:8080 external-proxy -f -N

    [Ext. Proxy Server ]
    ssh -R 0.0.0.0:8080:127.0.0.1:8080 last-hop -f -N

Después de ejecutar cada uno de los respectivos comandos, una simple solicitud web demuestra que la solicitud web sigue a cada uno de los túneles hasta el teamserver.

![](assets/proxyjump_3_qdDqfCNlcQPwJpIN.png)
![](assets/proxyjump_4_OaO9na6FNeG0C1Qz.png)

Configurar esto requiere que cada uno de estos comandos se ejecute en las respectivas máquinas. Sin embargo, cualquier cambio requiere matar el túnel en cada punto y volver a ejecutarlo. El dolor de cabeza en la práctica, sin algún tipo de software de administración que se ejecute en cada uno de los servidores, se vuelve muy evidente. Debe existir una forma más sencilla de gestionar estos túneles.

# ProxyJump

![](assets/proxyjump_5_akrI3NN_Ai7lO1ci.jpg)

Al igual que descubrimos el mes pasado sobre Aliens, ¡[ProxyJump](https://en.wikibooks.org/wiki/OpenSSH/Cookbook/Proxies_and_Jump_Hosts) es algo real!
Entra [ProxyJump](https://en.wikibooks.org/wiki/OpenSSH/Cookbook/Proxies_and_Jump_Hosts), una opción avanzada de SSH que es simplemente una simplificación de ProxyCommand (```ProxyCommand ssh proxy-host -W% h:% p```). ProxyJump permite que un túnel SSH pivote a través de un host SSH (proxy) a otro. La opción ProxyJump puede ser invocada por `-J` en la línea de comando:
    
    ssh -J internal-proxy last-hop -f -N

Mi preferencia personal es usar una configuración SSH (_/home/user/.ssh/config_) y llaves SSH (si no, se le pedirá una contraseña para iniciar sesión en cada salto de ProxyJump). Aquí, se puede especificar un solo salto como tal para SSH:
    
    Host internal-proxy
       HostName 10.20.30.253
       Port 22
       User nopriv
       IdentityFile /home/nopriv/.ssh/id_rsa
    Host last-hop
       HostName 10.100.2.240
       Port 22
       User nopriv
       IdentityFile /home/nopriv/.ssh/id_rsa
       ProxyJump internal-proxy

Guardando el ejemplo anterior y ejecutando el comando `ssh last-hop`, el prompt de last-hop se presenta a continuación (con output de `netstat`). Se ve internal-proxy conectado a través del puerto TCP 22 y viceversa.

![](assets/proxyjump_6_bMFeEgZWWmpBFNwR.png)

Ok, ¿qué pasa con los proxies múltiples? Como se hace referencia [aquí](https://en.wikibooks.org/wiki/OpenSSH/Cookbook/Proxies_and_Jump_Hosts), uno debe simplemente encadenar los proxies en el orden del más cercano al más lejano del servidor del equipo en la configuración SSH:

    Host internal-proxy
       HostName 10.20.30.253
       Port 22
       User nopriv
       IdentityFile /home/nopriv/.ssh/id_rsa
    Host external-proxy
       HostName 10.100.2.200
       Port 22
       User nopriv
       IdentityFile /home/nopriv/.ssh/id_rsa
       ProxyJump internal-proxy
    Host next-hop
       HostName 10.100.2.210
       Port 22
       User nopriv
       IdentityFile /home/nopriv/.ssh/id_rsa
       ProxyJump external-proxy
    Host last-hop
       HostName 10.100.2.240
       Port 22
       User nopriv
       IdentityFile /home/nopriv/.ssh/id_rsa
       ProxyJump next-hop

Ejecutando `ssh last-hop` y luego ejecutando `netstat` desde last-hop, se muestra que `next-hop` es el único sistema conectado a través del puerto TCP 22 a `last-hop`:

![](assets/proxyjump_7_zEVxPtJ0syTNhLta.png)

Entonces, ¿cómo ayuda esto a hacer un túnel hacia adelante? Bueno, simplemente agregando la línea `RemoteForward 8080 127.0.0.1:80` al final de la configuración SSH configurará el puerto remoto hacia adelante:

    Host last-hop
       HostName 10.100.2.240
       Port 22
       User nopriv
       IdentityFile /home/nopriv/.ssh/id_rsa
       ProxyJump next-hop
       RemoteForward 8080 127.0.0.1:80

Después de guardar la configuración y ejecutar esta vez (_ssh last-hop_), un `netstat` rápido en  last-hop  muestra que 8080 ahora está vinculado. Además, el uso de curl para solicitar last-hop:8080 muestra que el túnel efectivamente reenvía cualquier solicitud de last-hop a través de next-hop, external-proxy e internal-proxy al teamserver en el puerto 80:

![](assets/proxyjump_8_JpdH0YiLpskQvFcN.png)

Si diferentes hosts de salto usan archivos de identidad distintos, el usuario y el archivo de identidad solo necesitan coincidir con su respectivo host en la configuración. Por ejemplo, en nuestra configuración de demostración, usaremos user2 como una identidad en el proxy interno y nopriv en el last-hop:

    Host internal-proxy
       HostName 10.20.30.253
       Port 22
       User user2
       IdentityFile /home/nopriv/.ssh/user2
    […]
    Host last-hop
       HostName 10.100.2.240
       Port 22
       User nopriv
       IdentityFile /home/nopriv/.ssh/id_rsa
       ProxyJump internal-proxy

Ejecutando nuestro comando ssh last-hop ,presenta un inicio de sesión con éxito en el last-hop a través de internal-proxy, external-proxy y next-hop:

![](assets/proxyjump_9_7-wR2SDk30xpHR_-.png)

El intercambio de llaves con internal-proxy verifica que las credenciales de user2 se usaron en la autenticación:

![](assets/proxyjump_10_Q8gsu5j5Whabx-V_.png)

# Conclusión

En resumen, ProxyJump es una manera fácil de administrar túneles SSH a través de proxies, extendiendo servicios que pueden estar en las profundidades del datacenter corporativo o en la nube a donde se  los necesite. El uso de ProxyJump minimiza la cantidad de túneles separados requeridos y cuando se combinan configuraciones SSH, la modificación de dichos túneles es bastante simple y rápida.

* [Artículo Original](https://medium.com/maverislabs/proxyjump-the-ssh-option-you-probably-never-heard-of-2d7e41d43464)
* Traducción y ajuste [modri](https://github.com/GeekBeardLinks) [#43](https://github.com/sysarmy/disneyland/issues/43)
