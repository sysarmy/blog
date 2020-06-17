---
Description: "Tu empresa todavia usa servidores físicos?"
Keywords:
- sysadmin 
- servers
- hardware
Section: 
Slug: todavia-se-usan-servers-fisicos
Tags:
- sysarmy
Title: ¿Tu empresa todavía usa servidores físicos? ¿Por qué?
Topics:
- hardware
- servers
- Systems
Thumbnail: /blog/assets/cse-847beic-r1k28lpb_front_1.jpg
date: 2020-05-19
markup: markdown
draft: true
---

Nos cruzamos con [esta pregunta](https://news.ycombinator.com/item?id=23089999) en hacker news _"Is your company sticking to on-premise servers? Why?"_ y nos tomamos el trabajo de compilar algunas respuestas.

<!--more-->

Disclaimer: La traducción se realizó con estandares sysarmy no aprobados por la real academia española.

### Pregunta:

"He administrado servidores por algun tiempo ya. En mi casa, en datacenter, en la nube...
Cuanto más aprendo mas creo que la nube es la unica solucion competitiva actual, también para industrias como la bancaria o medica con estrictos estandares de seguridad.
Honestamente falló en encontrar una buena razon para no usar los servicios en la nube, al menos para negocios. Por costo, seguridad, etc.

Cuáles son las *razones para seguir con hardware fisico* hoy en dia para proyectos nuevos? Me estoy perdiendo de algo?""

### Respuestas (relevantes a criterio del editor):

>Como muchos otros han señalado: Costo.
>Soy el CTO de una comunidad de gamers de tamaño moderado, Hypixel Minecraft, que opera alrededor de 700 máquinas dedicadas alquiladas para dar servicio a 70k-100k jugadores concurrentes. Impulsamos alrededor de 4 PB / mes en el ancho de banda de salida, algo así como el percentil 95 de 32 gbps. Los grandes proveedores de la nube nos han presupuestado repetidamente un orden de magnitud más que el costo de toda nuestra flota ... SOLO en costos de ancho de banda. Incluso si traemos nuestros propios ISP y hacemos conexiones cruzadas para usar solo la capacidad de cómputo de la nube, todavía cobran altos costos por salir por nuestros ISP.

---

>La nube es excelente si su carga de trabajo es variable y errática y no puede comprometerse razonablemente con los términos (años), o si su equipo es tan pequeño que no tiene los recursos para administrar la infraestructura usted mismo, pero con un tamaño de equipo de > 10 sus administradores de sistemas que funcionan con metal desnudo pagarán sus propios salarios en ahorros en la nube.

---

>Hace unos años, estaba tratando de iniciar una empresa y ponerla en marcha. Tuvimos que tomar decisiones sobre nuestro stack tecnológico y si íbamos a usar AWS y construir alrededor de su infraestructura. Nuestro negocio tenía muchos datos y requería transferir grandes conjuntos de datos desde afuera a nuestras bases de datos. Incluso en nuestros primeros prototipos, nos dimos cuenta de que no podíamos escalar de manera rentable en AWS. Me di cuenta de que podíamos colocar y alquilar racks, instalar HW, contratar personas para mantener, etc. por mucho menos de lo que podríamos usar la nube. Me sorprendió la diferencia. Recuerdo haberle dicho a mi cofundador por qué alguien usa AWS, puedes hacerlo a tu manera más barato.

---

>Estoy convencido de que una gran parte del éxito financiero de la nube se debe a cómo permite a los CTO / CIO cumplir sus fantasías sobre tener una aplicación megaescalable, incluso si sus cargas de trabajo son muy regulares y previsible.
Es una opción sensata dados los incentivos, también. Cloud bullshit clickbait ocupa un lugar destacado en una gran cantidad de publicaciones técnicas de trabajo en estos días.

---

>Desde la perspectiva del desarrollador, prefiero trabajar con proveedores en la nube porque puedo hacer más con menos desarrolladores porque no estoy tratando con administradores de sistemas también. Puedo lanzar un clúster EMR con un esfuerzo mínimo y obtener un producto que funcione rápidamente.
Estas cosas no importan para las grandes empresas establecidas porque ya tienen equipos DevOps, SysAdmin y Desarrollo. Pero para las tiendas de desarrollo más pequeñas, hace una gran diferencia cuando puede generar un poco más de eficiencia de su personal de desarrollo.

---

>Ese puede ser el caso de una startup. Pero en el entorno de TI corporativo promedio, la infraestructura del servidor local y la jungla de procedimientos / política es tan terrible que solo tiene que alejarse de ella. Antes de que la "nube" se pusiera de moda, era políticamente difícil o imposible alojar su proyecto en algún lugar fuera de la mala infraestructura corporativa, pero ahora hay una manera de presentar la elección de una manera agradable.

---

>Voy a entrar aquí. Aunque estoy de acuerdo con todo lo que ustedes han dicho. Sus comentarios parecen estar sesgados en una perspectiva de que todas las compañías se están ejecutando en los Estados Unidos, Canadá, Alemania, etc., países muy desarrollados donde el poder es constante y se puede confiar en ellos. La mano de obra calificada para ejecutar estos servidores está disponible para contratar. Las partes y la infraestructura están disponibles para alquilar o comprar. La mayoría del mundo no es así, pero hay compañías formidables en todo el mundo y, para ellos, este es un aspecto menos confiable de su compañía.
Para darle una idea, si desea ejecutar un centro de datos o sus propios servidores en algunos países, necesita un generador de reserva (porque la electricidad no es un hecho) y el Diesel utilizado para operar estos generadores es importado y la economía de estos países es inestable, por lo que el tipo de cambio fluctúa, por lo que de repente el costo de mantener su sitio actualizado se convierte en una variable y ahora está sujeto a anuncios del gobierno (ni siquiera de una manera autoritaria malvada), políticas e impuestos de importación. Ante todo esto, tener una factura estable de AWS con infraestructura confiable no tiene precio para estas compañías

---

>Dropbox hizo lo mismo hace unos años: movió todo, desde Amazon S3 a su propio almacenamiento.
Supongo que lo hicieron por razones de costo.

NdE: [link a la noticia de Dropbox](https://techcrunch.com/2017/09/15/why-dropbox-decided-to-drop-aws-and-build-its-own-infrastructure-and-network/)

---

>Lo mismo aquí: CTO de una empresa mediana.
Nuestros costos de infraestructura de TI son 1/10 del costo de la nube, simplemente porque me siento cómodo teniendo una máquina en las instalaciones y trabajando en ellas (en algún momento yo mismo).
Tenemos dos docenas de servidores en dos ubicaciones. Es más tiempo de configuración, pero el mantenimiento es bastante bajo.

---

>El factor para las pequeñas empresas que he notado en los lugares donde he estado es eso (como consultor de desarrollo). Los lugares que usan la nube a menudo aumentan mucho. Dado que la nube no limita a los desarrolladores, es muy fácil simplemente "crear un nuevo xx" y no pensar en los costos a largo plazo.
A menos que sea realmente pequeño, tenga cargas de trabajo variables, entonces la nube tal vez no sea para usted. A menos que el costo sea una pequeña parte del costo total de la plataforma, como no está realmente relacionado con la cantidad de usuarios / ventas que tiene.

---

>Me he dado cuenta de que las pequeñas empresas están más preocupadas por las facturas reales que entran, mientras que las grandes empresas están más preocupadas por la falta percibida de velocidad / agilidad en su desarrollo.
Podríamos pasar tiempo asegurándonos de usar las instancias de aurora más pequeñas posibles en AWS o podríamos estandarizar una versión para admitir y usar el tamaño más pequeño de esa versión que esté disponible. Gastamos mucho en esta capacidad adicional en algunos lugares, pero aumenta enormemente nuestra velocidad en otros lugares.

---
>Costo. Actualmente pagamos menos de 5000 € mensuales por 500 TB / mes en tráfico y 50 CPU Ryzen. Amazon sería $ 30,000 de tráfico + $ 100,000 de cómputo.
Es un trabajo de medio tiempo para 1 persona. La mayor parte del trabajo se destina a coordinar las actualizaciones de paquetes con Ansible. Puedo incluir $ 1000 en el cálculo si eso te hace sentir mejor;)
Todo se implementa con Ansible, monitoreado con Monit. Los servidores tienen unidades de suministro de energía redundantes y unidades de disco duro intercambiables en caliente SATA, por lo que puede solucionar problemas menores de hardware sin tener que reiniciar. Como resultado, tenemos más de un año de tiempo de actividad en un servidor típico.
Por otro lado, hemos sido golpeados con varios cortes de S3. Tengo la sensación de que la nube necesita una conmutación por error totalmente automática porque falla mucho más a menudo que todos nuestros servidores de metal desnudo combinados.
---
> La nube es excelente si su carga de trabajo es variable y errática
O si solo está constantemente iterando en un producto grande con muchos ingenieros. Los salarios de esos ingenieros casi siempre superan todos sus costos en la nube, por lo que hacerlos productivos es rentable. Cosas como SNS / SQS / S3 / VPC / ELB / etc. le ahorrará innumerables horas y, a menudo, compensará los mayores costos de la nube con una mayor productividad del desarrollador.
---

