---
Title: "La Historia de la URL"
Description: "La historia de cómo evolucionó la URL"
Keywords:
- history
- historia
- web
- internet

Tags:
- sysarmy
- history
- historia
- web
- internet

Thumbnail: assets/historia-url-thumbnail.jpg
socialImage: assets/historia-url-thumbnail.jpg
featuredImage: assets/historia-url-thumbnail.jpg

Topics:
- historia
- internet
- url

markup: markdown
date: 2022-08-25
draft: false
---

_La versión original de este post se puede encontrar en [The Cloudflare Blog](https://blog.cloudflare.com/the-history-of-the-url/) (inglés)._


El [11 de enero de 1982](https://www.rfc-editor.org/rfc/rfc805.txt) veintidós científicos de la computación se reunieron para discutir un problema con el “correo por computadora” (ahora conocido como email). Entre los presentes estaba [el tipo que fundaría Sun Microsystems](https://en.wikipedia.org/wiki/Bill_Joy), [el tipo que creó Zork](https://en.wikipedia.org/wiki/Dave_Lebling), [el tipo del NTP](https://en.wikipedia.org/wiki/David_L._Mills) y [el tipo que convenció al gobierno de pagar por Unix](https://en.wikipedia.org/wiki/Bob_Fabry). El problema era simple: había 455 nodos en la ARPANET y la situación se estaba saliendo de control.

![](assets/historia-url-1.jpg)

El problema se estaba gestando en ese momento porque la ARPANET estaba a punto de [migrar](https://www.rfc-editor.org/rfc/rfc801.txt) de su protocolo original, el [NCP](https://en.wikipedia.org/wiki/Network_Control_Program), al protocolo TCP/IP el cual actualmente usa lo que llamamos Internet. Con ese cambio, de repente, habría una multitud de redes interconectadas (una ‘Inter… red’’, InterNet), lo que requería un sistema de dominios ‘jerárquico’ en el cual ARPANET podría resolver sus propios dominios mientras que el resto de las redes resolvían los suyos.

Otras redes de ese momento tenían grandes nombres como “COMSAT”, “CHAOSNET”, “UCLNET” y ÏNTELPOSTNET” y eran mantenidas por grupos de universidades y compañías de todo Estados Unidos que querían la posibilidad de poder comunicarse, podían afrontar el alquiler de líneas de 56k de las compañías de teléfono y comprar el requerido [PDP-11s](https://en.wikipedia.org/wiki/PDP-11) para encargarse del ruteo.

![](assets/historia-url-2.jpg)


En el diseño original de ARPANET, un Centro de Información de Red (NIC) era responsable por el mantenimiento de un archivo que listaba todos los nodos de la red. El mismo era conocido como el archivo [**HOSTS.TXT**]()https://tools.ietf.org/html/rfc952), similar al archivo `/etc/hosts` de un sistema Linux o OS X actual. Cada cambio en la red [requería](https://www.rfc-editor.org/rfc/rfc952.txt) que el NIC lo transmitiera por FTP (un protocolo inventado en [1971](https://tools.ietf.org/html/rfc114)) a todos los nodos de la red, una carga significativa para su infraestructura.

Tener un solo archivo que liste todos los nodos de Internet, obviamente, no escalaría indefinidamente. La prioridad era el email de todos modos, ya que era el desafío predominante a tratar ese día. Su conclusión final fue la de crear un sistema jerárquico en el cual podías consultar a un sistema externo por el dominio o conjunto de dominios que necesitabas. En sus palabras:
> “La conclusión en este área fue que el identificador de casilla de correo actual usuario@nodo debía ser extendido a ‘usuario@nodo.dominio’ donde ‘dominio’ podía ser una jerarquía de dominios.”
Y así nació el dominio.

![](assets/historia-url-3.gif)

Es importante eliminar cualquier ilusión de que estas decisiones fueron tomadas a sabiendas del futuro que los dominios iban a tener. De hecho, la solución fue principalmente elegida porque era la que “ocasionaba menos dificultad para los sistemas existentes.” Por ejemplo, [una propuesta](https://www.rfc-editor.org/rfc/rfc799.txt) pretendía que las direcciones de mail tuvieran la forma de `<usuario>.<nodo>@<dominio>`. Si los nombres de usuario de mail de esos días no hubieran ya tenido ‘.’ entre sus caracteres tal vez hoy estarías mandándome mails a ‘zack.cloudflare@com’.

![](assets/historia-url-4.gif)

\
## UUCP y la Explosión de las Rutas

>Se ha dicho que la función principal de un sistema operativo es definir un número de diferentes nombres para el mismo objeto, para que se pueda ocupar de mantener el rastro de la relación entre todos los nombres diferentes. Los protocolos de red parecen tener de alguna manera la misma característica.

— David D. Clark, [1982](https://www.rfc-editor.org/rfc/rfc814.txt)

Otra [propuesta fallida](https://www.rfc-editor.org/ien/ien116.txt) proponía separar los componentes del dominio con el signo de exclamación (!). Por ejemplo, para conectarte con el nodo `ISIA` en `ARPANET`, te conectarías a `!ARPA!ISIA`. Podías entonces consultar por nodos usando comodines, así `!ARPA!*` te devolvería todos los nodos de `ARPANET`.

Este método de direccionamiento no era una divergencia loca del estándar, era un intento por mantenerlo. El sistema de nodos separados por signos de exclamación databa a una herramienta de transferencia de datos llamada [UUCP creada](http://www.cs.dartmouth.edu/~doug/reader.pdf) en 1976. Si estás leyendo esto en una computadora con OS X o Linux, `uucp` probablemente esté instalado y disponible en la terminal.

ARPANET fue introducida en 1969, y rápidamente se convirtió en una herramienta de comunicación poderosa… entre un puñado de universidades e instituciones gubernamentales que tenían acceso a ella. La Internet como la conocemos no estaría disponible públicamente fuera de las instituciones de investigación hasta [1991](http://www.cybertelecom.org/notes/nsfnet.htm), veintiún años después. Pero eso no significaba que los usuarios de computadoras no se estuvieran comunicando entre sí.

![](assets/historia-url-5.jpg)

En la era anterior a la Internet, el método general de comunicación entre computadoras era con una conexión telefónica directa punto a punto.Por ejemplo, si querías mandarme un archivo, harías que tu modem llame a mi modem, y transferiríamos el archivo. Para convertir esto en un red, por así decirlo, nació UUCP.

En este sistema, cada computadora tiene un archivo que lista los nodos que conoce, sus números de teléfono y un usuario y contraseña en cada nodo. Entonces creas un ‘camino’, desde tu computadora actual a la de destino, a través de nodos, los cuales sólo sabían cómo conectarse al próximo salto:

`sw-hosts!digital-lobby!zack`


![](assets/historia-url-6.jpg)

Esta dirección no sólo formaría un método de enviar archivos o conectarte con mi computadora directamente, también sería mi dirección de correo electrónico. En esta era anterior a los ‘servidores de correo’, si mi computadora estaba apagada no me podías mandar un email.

Mientras que el uso de ARPANET estaba restringido a universidades de primera, UUCP creó una Internet pirata para el resto de nosotros. Formó la base tanto para la [Usenet](https://en.wikipedia.org/wiki/Usenet) como la [BBS](https://en.wikipedia.org/wiki/Bulletin_board_system).


## DNS
En definitiva, el sistema de DNS que todavía usamos actualmente sería [propuesto](https://www.rfc-editor.org/rfc/rfc882.txt) en 1983. Si corres una consulta de DNS hoy, por ejemplo usando la herramienta `dig`, probablemente veas una respuesta que luce como esto:

    ;; ANSWER SECTION:
    google.com.   299 IN  A 172.217.4.206

Esto nos informa que google.com se encuentra en `172.217.4.206`. Como ya debes saber, la `A` nos informa que esto es un registro de dirección (‘address’), mapeando un dominio a una dirección IPv4. El `299` es el ‘tiempo de vida’, haciéndonos saber cuantos segundos de validez le quedan a este valor, antes de que requiera ser consultado nuevamente. ¿Pero qué significa el `IN`?

`IN` significa ‘Internet’. Como mucho de esto, este campo se remonta a la era cuando había varias redes de computadoras distintas que necesitaban interoperar. Otros valores potenciales eran `CH` para [CHAOSNET](https://en.wikipedia.org/wiki/Chaosnet) o `HS` para Hesiod que era el nombre para el servicio del [sistema Athena](https://en.wikipedia.org/wiki/Project_Athena). CHAOSNET murió hace mucho tiempo, pero una versión muy evolucionada de Athena todavía es utilizada por los estudiantes del MIT hasta hoy en día. Podés encontrar la lista de [clases de DNS](https://www.iana.org/assignments/dns-parameters/dns-parameters.xhtml) en el sitio de IANA, pero no debería sorprenderte que solo uno de los valores posibles es de uso común hoy en día.


## TLDs (Top Level Domains)

>Es extremadamente poco probable que otra TLDs vaya a ser creada.

— Jon Postel, [1994](https://tools.ietf.org/html/rfc1591)

Una vez decidido que los nombres de dominio debían ser ordenados jerárquicamente, fue necesario decidir qué se ubicaba en la raíz de esa jerarquía. Esa raíz es tradicionalmente demostrada con un solo ‘.’. De hecho, terminar todos tus dominios con un ‘.’ es semánticamente correcto, y funciona con tu navegador de internet: [google.com.](https://google.com.)

El primer TLD fue `.arpa`. Permitía a los usuarios direccionar sus viejos y tradicionales nombres de equipo de ARPANET durante la transición. Por ejemplo, si mi máquina había sido registrada como `hfnet`, mi nueva dirección sería hfnet.arpa. Eso fue solo temporal, durante la transición, los administradores de servidores tenían una decisión muy importante que tomar: ¿cuál de de los cinco TLDs iban a usar? “.com”, “.gov”, “.org”, “.edu” o “.mil”.
Cuando decimos que el DNS es jerárquico, lo que queremos decir es que hay un grupo de servidores DNS raíz que son responsables, por ejemplo de convertir `.com` en servidores de nombre `.com`, que a su vez responderán como llegar a `google.com`. La zona DNS raíz de internet está compuesta por trece clusters (grupos) de servidores DNS. Hay solo [13 clusters de servidores](https://www.internic.net/zones/named.cache), porque eso es lo que entra en un único paquete UDP. Históricamente, DNS era operado a través de paquetes UDP, lo que significa que la respuesta a un pedido no puede superar nunca los 512 bytes.

	;       This file holds the information on root name servers needed to
	;       initialize cache of Internet domain name servers
	;       (e.g. reference this file in the "cache  .  "
	;       configuration file of BIND domain name servers).
	;
	;       This file is made available by InterNIC 
	;       under anonymous FTP as
	;           file                /domain/named.cache
	;           on server           FTP.INTERNIC.NET
	;       -OR-                    RS.INTERNIC.NET
	;
	;       last update:    March 23, 2016
	;       related version of root zone:   2016032301
	;
	; formerly NS.INTERNIC.NET
	;
	.                        3600000      NS    A.ROOT-SERVERS.NET.
	A.ROOT-SERVERS.NET.      3600000      A     198.41.0.4
	A.ROOT-SERVERS.NET.      3600000      AAAA  2001:503:ba3e::2:30
	;
	; FORMERLY NS1.ISI.EDU
	;
	.                        3600000      NS    B.ROOT-SERVERS.NET.
	B.ROOT-SERVERS.NET.      3600000      A     192.228.79.201
	B.ROOT-SERVERS.NET.      3600000      AAAA  2001:500:84::b
	;
	; FORMERLY C.PSI.NET
	;
	.                        3600000      NS    C.ROOT-SERVERS.NET.
	C.ROOT-SERVERS.NET.      3600000      A     192.33.4.12
	C.ROOT-SERVERS.NET.      3600000      AAAA  2001:500:2::c
	;
	; FORMERLY TERP.UMD.EDU
	;
	.                        3600000      NS    D.ROOT-SERVERS.NET.
	D.ROOT-SERVERS.NET.      3600000      A     199.7.91.13
	D.ROOT-SERVERS.NET.      3600000      AAAA  2001:500:2d::d
	;
	; FORMERLY NS.NASA.GOV
	;
	.                        3600000      NS    E.ROOT-SERVERS.NET.
	E.ROOT-SERVERS.NET.      3600000      A     192.203.230.10
	;
	; FORMERLY NS.ISC.ORG
	;
	.                        3600000      NS    F.ROOT-SERVERS.NET.
	F.ROOT-SERVERS.NET.      3600000      A     192.5.5.241
	F.ROOT-SERVERS.NET.      3600000      AAAA  2001:500:2f::f
	;
	; FORMERLY NS.NIC.DDN.MIL
	;
	.                        3600000      NS    G.ROOT-SERVERS.NET.
	G.ROOT-SERVERS.NET.      3600000      A     192.112.36.4
	;
	; FORMERLY AOS.ARL.ARMY.MIL
	;
	.                        3600000      NS    H.ROOT-SERVERS.NET.
	H.ROOT-SERVERS.NET.      3600000      A     198.97.190.53
	H.ROOT-SERVERS.NET.      3600000      AAAA  2001:500:1::53
	;
	; FORMERLY NIC.NORDU.NET
	;
	.                        3600000      NS    I.ROOT-SERVERS.NET.
	I.ROOT-SERVERS.NET.      3600000      A     192.36.148.17
	I.ROOT-SERVERS.NET.      3600000      AAAA  2001:7fe::53
	;
	; OPERATED BY VERISIGN, INC.
	;
	.                        3600000      NS    J.ROOT-SERVERS.NET.
	J.ROOT-SERVERS.NET.      3600000      A     192.58.128.30
	J.ROOT-SERVERS.NET.      3600000      AAAA  2001:503:c27::2:30
	;
	; OPERATED BY RIPE NCC
	;
	.                        3600000      NS    K.ROOT-SERVERS.NET.
	K.ROOT-SERVERS.NET.      3600000      A     193.0.14.129
	K.ROOT-SERVERS.NET.      3600000      AAAA  2001:7fd::1
	;
	; OPERATED BY ICANN
	;
	.                        3600000      NS    L.ROOT-SERVERS.NET.
	L.ROOT-SERVERS.NET.      3600000      A     199.7.83.42
	L.ROOT-SERVERS.NET.      3600000      AAAA  2001:500:9f::42
	;
	; OPERATED BY WIDE
	;
	.                        3600000      NS    M.ROOT-SERVERS.NET.
	M.ROOT-SERVERS.NET.      3600000      A     202.12.27.33
	M.ROOT-SERVERS.NET.      3600000      AAAA  2001:dc3::35
	; End of file

Los servidores DNS raíz operan en cajas fuertes, dentro de jaulas cerradas. Hay un reloj dentro de la caja fuerte para asegurar que el video de las cámaras no fue cambiado por un ciclo.
En particular, teniendo en cuenta lo lenta que ha sido la implementación de [DNSSEC](https://en.wikipedia.org/wiki/Domain_Name_System_Security_Extensions), un ataque a uno de estos servidores podría permitir a un atacante redirigir todo el tráfico de Internet para una porción de los usuarios de Internet. Esto, por supuesto, sería la película de atracos más fantástica que se pueda hacer.

No debería sorprender a nadie que los servidores de nombre de los TLD raíz no cambian muy frecuentemente. [98%](http://dns.measurement-factory.com/writings/wessels-pam2003-paper.pdf) de las consultas que reciben los DNS raíz son por error, generalmente por clientes rotos o mal configurados que no almacenan bien sus resultados. Esto se convirtió en un problema tal que muchos operadores de DNS raíz tuvieron que [instanciar](https://www.as112.net/) servidores especiales simplemente para responderles “salí de acá” a toda la gente que hacía consultas de DNS reverso por sus direcciones IP locales.

Los servidores de nombre TLD son administrados por diferentes compañías y gobiernos alrededor del mundo ([Verisign](https://www.verisign.com/) administra `.com`). Cuando compras un dominio `.com`, alrededor de US $0.18 va la ICANN y US $7.85 va a Verisign.


##Punycode (Código insignificante)
Es raro en este mundo que los nombres tontos que nosotros los desarrolladores pensamos para un nuevo proyecto llegue al producto final y público. Podemos nombrar la base de datos de la compañía Delaware (porque ahí es donde todas las compañías son registradas), pero podés estar seguro de que para el momento en que llega a producción se llamará AlmacenamientoMetadaCompañía. Pero raramente, cuando todas las estrellas se alinean y el jefe está de vacaciones, alguna se escapa por las rajaduras.
Punycode es el sistema que usamos para codificar unicode en nombres de dominio. El problema que soluciona es simple, ¿cómo escribir 比薩.com cuando todo el sistema de Internet fue desarrollado usando el alfabeto [ASCII](https://en.wikipedia.org/wiki/ASCII) cuyo carácter más foráneo es el tilde?
No es tan simple como cambiar los dominios para usar [unicode](https://en.wikipedia.org/wiki/Unicode). Los [documentos originales](https://tools.ietf.org/html/rfc1035) que gobiernan los dominios especifican que deben ser codificados en ASCII. Todo equipamiento de hardware de internet de los últimos cuarenta años, incluyendo los router [Cisco](https://www.cisco.com/c/en/us/support/routers/crs-1-multishelf-system/model.html) y [Juniper](https://www.juniper.net/techpubs/en_US/release-independent/junos/information-products/pathway-pages/t-series/t1600/) usados para entregar esta página hacen esta suposición. 
La web en sí [nunca fue solo ASCII](http://1997.webhistory.org/www.lists/www-talk.1994q3/1085.html). Fue originalmente concebida para hablar [ISO 8859-1](https://en.wikipedia.org/wiki/ISO/IEC_8859-1) que incluye todos los caracteres ASCII, pero suma un grupo de caracteres especiales como ¼ y letras con marcas especiales como ä. Sin embargo, no contiene letras no latinas.
Esta restricción en el HTML fue eliminada en [2007](https://tools.ietf.org/html/rfc2070) y ese mismo año Unicode se [convirtió](https://googleblog.blogspot.com/2008/05/moving-to-unicode-51.html) en el conjunto de caracteres más popular de la web. Pero los dominios todavía están confinados al ASCII.

![](assets/historia-url-7.gif)

Como podrás adivinar, Punycode no fue la primera propuesta para solucionar este problema. Seguramente escuchaste hablar de UTF-8, que es una forma popular de codificar Unicode en bytes (el 8 es por los ocho bits en un byte). En el año [2000](https://tools.ietf.org/html/draft-jseng-utf5-01) varios miembros del IETF (Grupo de Tareas de Ingenieros de Internet) desarrollaron el UTF-5. La idea era codificar Unicode en trozos de 5 bits. Podías entonces mapear cada grupo de 5 bits con uno de los caracteres permitidos (A-V & 0-9) en los nombres de dominio. Así que si yo tenía un sitio para aprender el idioma japonés, mi sitio 日本語.com se convertía en el críptico M5E5M72COA9E.com.
Este método de codificación tenía bastantes desventajas. La primera, A-V y 0-9 eran usados como salida de la codificación, lo que significaba que si querías incluir uno de esos caracteres en tu dominio, tenía que ser codificado como todo lo demás. Esto generaba dominios muy largos, lo que es un problema serio cuando cada segmento de un dominio está limitado a 63 caracteres. Un dominio en el idioma de Myanmar estaría limitado a no más de 15 caracteres. Sin embargo, la propuesta realiza una sugerencia interesante para usar UTF-5 para permitir transmitir Unicode a través de código Morse o telegrama.
También estaba la cuestión de cómo hacerle saber al cliente que este dominio estaba codificado así podían mostrarlo con los caracteres Unicode apropiados en lugar de mostrar M5E5M72COA9E.com en mi barra de direcciones. Hubo [varias sugerencias](https://tools.ietf.org/html/draft-ietf-idn-compare-01), una de las cuales fue usar el bit que no se usaba de la respuesta de DNS. Era el “último bit no utilizado de la cabecera”, y la gente de DNS se “resistía mucho a entregarlo” sin embargo.
Otra idea fue empezar cada dominio usando este método de codificación con `ra–`. Hasta [ese momento](https://tools.ietf.org/html/draft-ietf-idn-race-00) (mediados de abril del 2000), no había dominios que empezaran con esos caracteres particulares. Si se algo sobre Internet, alguien registró el dominio `ra–` solo para molestar inmediatamente después de que se publicó la propuesta.
La [conclusión final](https://tools.ietf.org/html/rfc3492), se alcanzó en 2003, fue adoptar un formato llamado Punycode que incluía una forma de compresión delta que podría acortar dramáticamente nombres de dominio codificados. La compresión delta es una idea particularmente buena porque probabilísticamente todos los caracteres de tu dominio se encuentran en el mismo área general dentro de Unicode. Por ejemplo, dos caracteres en farsi van a estar mucho más cerca que un carácter en farsi y otro en hindi. Para dar un ejemplo de cómo funciona, si tomamos la frase sin sentido:
يذؽ
En un formato no comprimido, eso sería almacenado como tres caracteres: `[1620, 1584, 1597]` (basado en sus códigos Unicode). Para comprimir esto primero tenemos que ordenarlos numéricamente (registrando dónde estaban esos caracteres originalmente): `[1584, 1597, 1620]`. Luego podemos guardar el valor menor (`1584`), y el delta (diferencia) entre ese valor y el próximo carácter (`13`), y luego nuevamente para el próximo carácter (`23`), que es significativamente menos para transmitir y almacenar.
Punycode entonces codifica (muy) eficientemente esos enteros en caracteres permitidos en nombres de dominio, e inserta `xn–` al principio para informar a los consumidores que este es un dominio codificado. Notarás que todos los caracteres Unicode se ubican juntos al final del dominio. No solo codifican su valor, también codifican dónde deberían ser insertados dentro de la porción ASCII del dominio. Para poner un ejemplo, el sitio 熱狗sales.com se convierte en `xn–sales-r651m0e.com`. Cada vez que tipeás un nombre de dominio basado en Unicode en la barra de direcciones de tu navegador, es codificado de esta manera.
Esta transformación podría ser transparente, pero introduce un problema de seguridad importante. Toda clase de caracteres Unicode se imprimen como caracteres ASCII existentes. Por ejemplo, posiblemente no puedas ver la diferencia entre la letra a (“а”) minúscula cirílica y la letra a (“a”) latina. Si registro amazon.com en cirílico (xn-mazon-3ve.com), y me las arreglo para que lo visites, va a ser difícil para vos darte cuenta que estas en el sitio equivocado. Por esa razón, cuando visitás [🍕💩.ws](http://xn--vi8hiv.ws/), tu navegador muestra la versión aburrida `xn–vi8hiv.ws` en la barra de direcciones.


## Protocolo
La primera parte del URL es el protocolo que debería usarse para accederlo. El protocolo más común es el `http`, que es el simple protocolo de transferencia de documentos inventado por Tim Berners-Lee específicamente para la web. No era la única opción. [Algunas personas](http://1997.webhistory.org/www.lists/www-talk.1993q2/0339.html) creen que simplemente deberíamos haber usado Gopher. En lugar de ser de propósito general, Gopher está específicamente diseñado para enviar datos estructurados de manera similar a un árbol de archivos..
Por ejemplo si pedís el montaje `/Cars`, te podría devolver:


	1Chevy Camaro             /Archives/cars/cc     gopher.cars.com     70
	iThe Camaro is a classic  fake                  (NULL)              0
	iAmerican Muscle car      fake                  (NULL)              0
	1Ferrari 451              /Factbook/ferrari/451  gopher.ferrari.net 70

que identifica dos autos, junto con metadatos sobre ellos y dónde te podés conectar para más información. La idea era que tu cliente le daría procesada esta información de alguna manera en la que enlazaría las entradas con las páginas de destino.

![](assets/historia-url-8.gif)

El primer protocolo popular fue el FTP, que fue creado en 1971, como una manera de listar y descargar archivos de computadoras remotas. Gopher era una extensión lógica de esto,  que proveía un listado similar, pero incluía facilidades para leer también los metadatos de las entradas. Esto significaba que podía ser usado con propósitos más liberales como noticias o una simple base de datos. No tenía, sin embargo, la libertad y simplicidad que caracteriza al HTTP y el HTML.
HTTP es un protocolo muy simple, particularmente comparado con alternativas como el FTP o incluso el protocolo [HTTP/3](https://blog.cloudflare.com/http3-the-past-present-and-future/), que está aumentando en popularidad actualmente. Primero, el HTTP está completamente basado en texto, en lugar de estar compuesto por conjuros binarios a medida (que lo habrían hecho significativamente más eficiente). Tim Berners-Lee intuyó correctamente que usar un formato basado en texto haría más fácil el desarrollo y la solución de problemas en aplicaciones basadas en HTTP para generaciones de programadores.
El HTTP tampoco hace casi ninguna suposición respecto de lo que estás transmitiendo. A pesar de que fue inventado explícitamente para acompañar el lenguaje HTML, te permite especificar que tu contenido es de cualquier tipo (usando el MIME `Content-Type`, que era una nueva invención en ese momento). El protocolo en sí es bastante simple.

Una cosulta así:

	GET /index.html HTTP/1.1
	Host: www.example.com

Respondería:

	HTTP/1.1 200 OK
	Date: Mon, 23 May 2005 22:38:34 GMT
	Content-Type: text/html; charset=UTF-8
	Content-Encoding: UTF-8
	Content-Length: 138
	Last-Modified: Wed, 08 Jan 2003 23:11:55 GMT
	Server: Apache/1.3.3.7 (Unix) (Red-Hat/Linux)
	ETag: "3f80f-1b6-3e1cb03b"
	Accept-Ranges: bytes
	Connection: close

	<html>
		<head>
			<title>An Example Page</title>
		</head>
		<body>
			Hello World, this is a very simple HTML document.
		</body>
	</html>

Para poner esto en contexto, podes pensar que el sistema de redes que usa Internet empezando por el Protocolo Internet, el IP. El IP es responsable de llevar un pequeño paquete de datos (alrededor de 1500 bytes) de una computadora a otra. Arriba de eso tenemos el TCP, que es responsable de llevar bloques más grandes de datos como documentos enteros y archivos, enviándolos mediante muchos paquetes IP de manera confiable. Por encima de eso, implementamos un protocolo como el HTTP o el FTP, que especifica qué formato se debería usar para hacer que esos datos que enviamos vía TCP (o UDP, etc) sean entendibles y tengan sentido.
En otras palabras, el TCP/IP manda un conjunto de bytes a otra computadora, el protocolo dice qué son esos datos y qué significan.
Podes armar tu propio protocolo si querés, acomodar los bytes en tus mensajes TCP como quieras. El único requerimiento es que quien sea con quien estés hablando tiene que hacerlo en el mismo idioma. Por esta razón es común estandarizar estos protocolos.
Hay, por supuesto, protocolos menos importantes para jugar. Por ejemplo el protocolo [“Cita del día”](https://www.rfc-editor.org/rfc/rfc865.txt) (puerto 17), y el protocolo de [Caracteres Aleatorios](https://www.rfc-editor.org/rfc/rfc864.txt) (puerto 19). Parecen tontos hoy, pero también muestran cuán importante era un protocolo general de transmisión de documentos como el HTTP.


## Puerto
El lugar en la historia de Gopher y HTTP puede ser evidenciado por sus puertos por defecto. Gopher es el 70, HTTP el 80. El puerto HTTP fue asignado (probablemente por [Jon Postel](https://en.wikipedia.org/wiki/Jon_Postel) en la IANA) a pedido de Tim Berners-Lee en algún momento entre [1990](https://tools.ietf.org/html/rfc1060) y [1992](https://tools.ietf.org/html/rfc1340).
Este concepto de registrar ‘números de puerto’ predata incluso a Internet. El protocolo original NCP que usaban ARPANET las direcciones remotas eran identificadas por 40 bits. Los primeros 32 identificaban al nodo remoto, de manera similar a cómo funciona una dirección IP hoy en día. Los últimos 8 eran conocidos como los [AEN](https://tools.ietf.org/html/rfc433) (significaba “Otros Ocho Dígitos” por su sigla en inglés), y eran utilizados por la máquina remota de la manera que nosotros usamos un número de puerto, para separar mensajes destinados a diferentes procesos. En otras palabras, la dirección especifica a qué máquina debería ir el mensaje, y el AEN (o número de puerto) le dice a la máquina remota qué aplicación debe recibirlo.
Rápidamente [pidieron](https://tools.ietf.org/html/rfc322) que los usuarios registren estos ‘números de socket’ para limitar posibles colisiones. Cuando los números de puerto fueron expandidos a 16 bits por TCP/IP, el proceso de registración continuó.
Mientras que los protocolos tienen un puerto por defecto, tiene sentido permitir que se especifique un puerto manualmente para permitir desarrollos locales y la posibilidad de correr múltiples servicios en la misma máquina. Esa misma lógica fue la [base](http://1997.webhistory.org/www.lists/www-talk.1992/0335.html) para los prefijos de los sitios `www.`. En ese momento, era poco probable que alguien estuviera accediendo a la raíz del dominio, simplemente por correr un sitio web experimental. Pero si le das a los usuarios el nombre de nodo de tu máquina específica (`dx3.cern.ch`) estarías en problemas cuando necesites reemplazar esa máquina. Al usar un subdominio común (`www.cern.ch`) podes cambiar a qué apunta según lo requieras..


## El pedacito del medio
Como probablemente sabés, la sintaxis del URL pone una doble barra (`//`) entre el protocolo y el resto de la URL:

`http://cloudflare.com`

Esa doble barra fue heredada del sistema [Apollo](https://en.wikipedia.org/wiki/Apollo/Domain) que fue una de primeras estaciones de trabajo en red. El equipo de Apollo tenía un problema similar al de Tim Berners-Lee: necesitaban una forma de separar una ruta de la máquina en la que esa ruta se encuentra. Su solución fue crear un formato especial de ruta:


`//nombredeequipo/archivo/ruta/`

Y TBL copió ese formato. Por cierto, él ahora se [arrepiente](https://www.w3.org/People/Berners-Lee/FAQ.html#etc) de esa decisión, deseando que el dominio (en este caso `ejemplo.com`) fuera la primera parte de la ruta:

`http:com/ejemplo/foo/bar/baz`

>Las URLs nunca fueron pensadas para lo que se han convertido: una manera arcaica para que un usuario identifique un sitio en la Web. Desafortunadamente, nunca hemos podido estandarizar los URNs, que nos darían un sistema de nombres más útil. Decir que el sistema actual de URL es suficiente es como alabar la línea de comandos de DOS, y decir que la mayoría de la gente simplemente debería aprender la sintaxis de la línea de comandos. La razón por la cual tenemos un sistema de ventanas es para hacer las computadoras más fáciles de usar, y extender su uso. La misma línea de pensamiento debería llevarnos a una mejor forma de localizar sitios específicos en la web.

— Dougherty, [1996](https://lists.w3.org/Archives/Public/www-talk/1996JanFeb/0075.html)

Hay muchas formas diferentes de entender la ‘Internet’. Una es como un sistema de computadoras conectadas usando una red de computadoras. Esa versión de Internet nació en 1969 con la creación de ARPANET. Correo, archivos y chat, todo se movía sobre esa red antes de la creación del HTTP, el HTML, o el ‘navegador web’.
En 1992 Tim Berners-Lee creó tres cosas, dando a luz a los que *nosotros* consideramos Internet. El protocolo HTTP, el HTML y la URL. Su objetivo era traer a la vida el ‘Hipertexto’. El Hipertexto en su forma más simple es la habilidad de crear documentos que se enlazan entre sí. En ese momento era visto como una panacea de la ciencia ficción, para ser suplementado con la [Hipermedia](https://en.wikipedia.org/wiki/Hypermedia), y cualquier otra palabra a la que le pudieras agregar ‘Hiper’.
El requerimiento principal del Hipertexto era la habilidad de enlazar desde un documento a otro. En tiempos de TBL, sin embargo, estos documentos eran alojados en una multitud de formatos y accedidos a través de protocolos como [Gopher](https://en.wikipedia.org/wiki/Gopher_(protocol)) o FTP. Necesitaba una forma consistente de referenciar a un archivo que codificara su protocolo, su nodo en la Internet, y dónde existía en ese nodo.
En la [presentación original](https://www.w3.org/Conferences/IETF92/WWX_BOF_mins.html) de la World-Wide Web en mazo de 1992 TBL lo describió como un ‘Identificador de Documento Universal’ (UDI, por su sigla en inglés). Muchos [formatos diferentes](https://www.w3.org/Protocols/old/osi-ds-29-00.txt) fueron considerados para este identificador:

	protocol: aftp host: xxx.yyy.edu path: /pub/doc/README
 
	PR=aftp; H=xx.yy.edu; PA=/pub/doc/README;
 
	PR:aftp/xx.yy.edu/pub/doc/README
	
	/aftp/xx.yy.edu/pub/doc/README


Este documento también explica por qué los espacios deben ser codificados en las URLs (%20):


> El uso de caracteres de espacios en blanco ha sido evitado en los UDIs: los espacios
> no son caracteres legales. Esto fue hecho así por la frecuente
> introducción de caracteres de espacio blanco extraños cuando las líneas son terminadas
> por sistemas como el mail, o la necesidad de columnas estrechas, y
> por la  inter-conversión entre varias formas de espacios en blanco
> que ocurre durante la conversión de código de caracteres y la transferencia
> de texto entre aplicaciones.


Lo que es más importante entender, es que la URL era fundamentalmente una forma abreviada de referirse a la combinación de esquema, dominio, puerto, credenciales y una ruta que previamente tenía que ser entendida contextualmente para cada sistema de comunicación diferente.
Fue oficialmente definida por primera vez en un [RFC](https://www.ietf.org/rfc/rfc1738.txt) publicado en 1994.


`scheme:[//[user:password@]host[:port]][/]path[?query][#fragment]`


Este sistema permitió referenciar diferentes sistemas desde dentro del Hipertexto, pero ahora que casi todo el contenido está publicado sobre HTTP, tal vez ya no sea necesario. Ya en [1996](https://lists.w3.org/Archives/Public/www-talk/1996JanFeb/0075.html) los navegadores estaban agregando `http://` y `www.` a sus usuarios automaticamente (convirtiendo cualquier anuncio que todavía los tenga en algo realmente ridículo).


## Ruta
> No creo que la pregunta sea sobre si las personas pueden aprender el significado del URL, simplemente me parece moralmente despreciable forzar a la abuela o al abuelo a entender lo que, en definitiva, son convenciones del sistema de archivos de UNIX.

— Israel del Rio, [1996](https://lists.w3.org/Archives/Public/www-talk/1996JanFeb/0041.html)

El componente separado por barras de la URL debería ser familiar para cualquier usuario de cualquier computadora construida en los últimos cincuenta años. El sistema de archivos jerárquico en sí fue introducido por el sistema [MULTICS](http://www.multicians.org/). Su creador a su vez, lo atribuye a [una conversación de dos horas que tuvo con Albert Einstein](http://www.csl.sri.com/users/neumann/) en 1952.
MULTICS usaba el símbolo “mayor que” (\>) para separar los componentes de la ruta de archivos. Por ejemplo:
`\>usr\>bin\>local\>awk`
Esto era perfectamente lógico, pero desgraciadamente la gente de Unix [decidió](https://www.bell-labs.com/usr/dmr/www/cacm.html) usar '\>' para representar la redirección, delegando la separación de la ruta a la barra hacia adelante ('/', barra de dividir).


## Snapchateá a la Corte Suprema
>Estás equivocado. Estamos, ahora lo veo claramente, \* en desacuerdo \*. Vos y yo. 
>
>...
>
>Como persona me reservo el derecho de usar diferentes criterios para diferentes propósitos. Quiero poder darle nombres a trabajos genéricos, Y a traducciones particulares Y a versiones particulares. Quiero un mundo más rico que el que vos proponés. No quiero ser limitado por tu sistema de dos niveles de “documentos” y “variantes”.

— Tim Berners-Lee, [1993](http://1997.webhistory.org/www.lists/www-talk.1993q3/1003.html)

[La mitad](https://journals.cambridge.org/action/displayAbstract?fromPage=online&aid=9282809&fileId=S1472669614000255) de las URLs referenciadas por opiniones de la Corte Suprema de los Estados Unidos apuntan a páginas que ya no existen.Si leiste un paper académico en 2011, escrito en 2001, tuviste muchas posibilidades de que las URL no fueran [válidas](https://bmcbioinformatics.biomedcentral.com/articles/10.1186/1471-2105-14-S14-S5).
Había una [ferviente creencia](http://1997.webhistory.org/www.lists/www-talk.1993q2/0234.html) en 1993 de que las URL morirían en favor del ‘URN’. El Uniform Resource Name (Recurso de Nombre Uniforme) es una referencia permanente a una pieza de contenido dado que, a diferencia de la URL, no cambiará jamás o se romperá. Tim Berners-Lee describió inicialmente la “necesidad urgente” de ellos hacia [1991](http://1997.webhistory.org/www.lists/www-talk.1991/0018.html).
La forma más simple para crear un URN puede ser simplemente usar un hash criptográfico del contenido de la página, por ejemplo: `urn:791f0de3cfffc6ec7a0aacda2b147839`. Sin embargo, este método no cumple con el criterio de la comunidad web, ya que no había posibilidad de darse cuenta de a quién pedirle que convierta ese hash en una pieza de contenido real. Tampoco tenía en cuenta cambios de formato que muchas veces le ocurren a los archivos (comprimido vs descomprimido por ejemplo) que sin embargo representan el mismo contenido.

![](assets/historia-url-9.jpg)

En 1996 Keith Shafer y otros propusieron una solución al problema de las URL rotas. [El link](https://purl.oclc.org/docs/inet96.html) está roto. Roy Fielding publicó una sugerencia de implementación en julio de 1995. [Ese link](http://ftp.ics.uci.edu/pub/ietf/uri/draft-ietf-uri-roy-urn-urc-00.txt) está roto.
Pude encontrar estas páginas a través de Google, que funcionalmente ha convertido los títulos de las páginas en los URN de hoy. El formato URN fue finalizado en 1997, y esencialmente no se ha usado nunca desde entonces. La implementación en sí es interesante. La URN está compuesta por dos partes, una `autoridad` que puede resolver cierto tipo de URN, y el ID específico de ese documento en el formato que entiende la `autoridad`. Por ejemplo, `urn:isbn:0131103628` identificará un libro, formando un link permanente que puede (con suerte) ser convertido en un conjunto de URLs por tu resolvedor local `isbn`.
Dado el poder de los motores de búsqueda hoy en día, posiblemente, el mejor formato de URN podría ser una simple manera de que los archivos apunten a sus antiguas URLs. Lo que permitiría a los buscadores indexar esta información y vincularnos apropiadamente:

    <!-- On http://zack.is/history →
    <link rel="past-url" href="http://zackbloom.com/history.html">
    <link rel="past-url" href="http://zack.is/history.html">


##  Parámetros de consulta
>El formato "application/x-www-form-urlencoded" es de muchas maneras una monstruosidad aberrante, el resultado de muchos años de accidentes de implementación y adaptaciones que llevaron a un conjunto de requerimientos necesarios para la interoperabilidad, pero que de ninguna manera representa las buenas prácticas del diseño.

— [WhatWG URL Spec](https://url.spec.whatwg.org/#application/x-www-form-urlencoded)

Si has usado la web por algún tiempo, estás familiarizado con los parámetros de consulta. Le siguen a la porción de ruta de la URL, y codifican opciones como `?nombre=nachi&estado=caba`. Tal vez te resulte extraño que las consultas usen el carácter et (ampersand ‘&’) que es el mismo carácter usado en HTML para codificar (escapar) caracteres especiales. De hecho, si has usado HTML por un tiempo, seguramente has tenido que codificar ‘ets’ en URLs, convirtiendo `http://nodo/?x=1&y=2` en `http://nodo?x=1&#38;y=2` (esa confusión en particular siempre [ha existido](http://1997.webhistory.org/www.lists/www-talk.1992/0447.html).
Tal vez también hayas notado que las cookies siguen un formato similar, pero distinto: `x=1,y=2` que no conflictúa con la codificación de caracteres del HTML. La W3C no se olvidó de esta idea, animó a los implementadores para que soporten `;` a la vez que `&` en parámetros de consultas desde 1995.
Originalmente, esta sección de la URL era estrictamente usada para buscar ‘índices’. La Web fue creada originalmente para (y su financiación asignada para) crear un método de colaboración para físicos de altas energías. Esto no quiere decir que Tim Berners-Lee no sabía que lo que realmente estaba creando era una herramienta de comunicación de uso general. No [agregó soporte](http://1997.webhistory.org/www.lists/www-talk.1993q1/0286.html) para tablas hasta muchos años después, algo que los físicos habrían necesitado.
De cualquier manera, estos ‘físicos’ necesitaban una forma de codificar y vincular información, y una forma de buscar esa información. Para proveer eso, Tim Berners-Lee creó la etiqueta `<ISINDEX>`. Si `<ISINDEX>` aparecía en una página, informaba al navegador que esa era una página en la que se podía buscar. El navegador debería mostrar un campo de búsqueda, y permitir al usuario enviar una consulta al servidor.
Esa consulta estaba formateada como palabras claves separadas por un carácter de suma (+):
`http://cernvm/FIND/?sgml+cms`
Como todo en Internet, esta etiqueta fue abusada de todas las maneras posibles, incluyendo la posibilidad de proveer un campo de entrada para calcular raíces cuadradas. Rápidamente [se propuso](https://lists.w3.org/Archives/Public/www-talk/1992NovDec/0042.html) que tal véz esto era muy específico y que realmente se necesitaba una etiqueta general de `<input>` (entrada).
Esa propuesta en particular usa signos de suma para separar los componentes de lo que de cualquier manera se ve como una consulta GET moderna:
`http://algunnodo.lugar/alguna/ruta?x=xxxx+y=yyyy+z=zzzz`

Esto estuvo lejos de ser aclamado universalmente. [Algunos creían](https://lists.w3.org/Archives/Public/www-talk/1992NovDec/0032.html) que necesitábamos una manera de decir que el contenido del otro lado del vínculo podía ser buscable:
`<a HREF="wais://quake.think.com/INFO" INDEX=1>search</a>`

Tim Berners-Lee [pensó] que debíamos tener una manera de definir consultas fuertemente tipadas:
`<ISINDEX TYPE="iana:/www/classes/query/personalinfo">`

Puedo decir con confianza que, en retrospectiva, me alegro de que haya ganado la solución más genérica.
El verdadero trabajo en `<INPUT\>` [arrancó](http://1997.webhistory.org/www.lists/www-talk.1993q1/0079.html) en enero de 1993 basado en un viejo tipo de SGML. Fue (tal vez desafortunadamente), decidido que las entradas `<SELECT\>` necesitaban una estructura separada, mas rica:

    <select name=FIELDNAME type=CHOICETYPE [value=VALUE] [help=HELPUDI]> 
        <choice>item 1
        <choice>item 2
        <choice>item 3
    </select>

Como dato extra, reusar `<li>`, en lugar de introducir `<option>` fue [absolutamente](http://1997.webhistory.org/www.lists/www-talk.1993q2/0188.html)considerado. Hubo, por supuesto, propuestas de formas alternativas. [Una](http://1997.webhistory.org/www.lists/www-talk.1993q2/0168.html) incluía cierta sustitución de variables evocativa a lo que Angular podría hacer hoy:

    <ENTRYBLANK TYPE=int LENGTH=length DEFAULT=default VAR=lval>Prompt</ENTRYBLANK>
    <QUESTION TYPE=float DEFAULT=default VAR=lval>Prompt</QUESTION>
    <CHOICE DEFAULT=default VAR=lval>
        <ALTERNATIVE VAL=value1>Prompt1 ...
        <ALTERNATIVE VAL=valuen>Promptn
    </CHOICE>

En este ejemplo, las entradas son verificadas contra un tipo específico en `type`, y los valores `var` están disponibles en la página para ser usados en [sustitución de cadenas de texto](http://1997.webhistory.org/www.lists/www-talk.1993q2/0150.html) en URLs, tal como:

`http://cloudflare.com/apps/$appId`

Propuestas adicionales usaban en realidad `@`, en lugar de `=`, para separar componentes de la consulta:

`name@value+name@(value&value)`

Fue Marc Andreessen quien sugirió el método actual basado en lo que él ya había implementado en Mosaic:

`name=value&name=value&name=value`

Solo [dos meses después](http://1997.webhistory.org/www.lists/www-talk.1993q4/0437.html) Mosaic sumaría soporte para formularios `method=POST`, y los formularios HTML ‘modernos’ habían nacido.

Por supuesto, fue también la compañía de Marc Andreessen [Netscape](https://web.archive.org/web/19990421025406/http://home.mcom.com/newsref/std/cookie_spec.html) la que crearía el formato de las cookies (usando un separador diferente). Su propuesta fue dolorosamente miope, llevó al intento de introducir el encabezado [`Set-Cookie2`](https://www.ietf.org/rfc/rfc2965.txt), e introdujo problemas estructurales con los que lidiamos en Cloudflare al día de hoy.


##Fragmentos
La porción de la URL que sigue al ‘#’ es conocida como fragmento. Los fragmentos fueron parte de las URLs desde su [especificación inicial](https://www.w3.org/History/19921103-hypertext/hypertext/WWW/Addressing/Addressing.html), usados para vincular a una ubicación específica en la página que se estaba cargando. Por ejemplo, si tengo un texto ancla en mi sitio:

`<a name="bio"></a>`

Puedo vincularlo así:

`http://zack.is/#bio`

Este concepto fue gradualmente extendido a cualquier elemento (en lugar de solo anclas), y movido al atributo `id` en lugar de `name`:

`<h1 id="bio">Bio</h1>`

Tim Berners-Lee decidió usar este carácter basado en su conexión con las direcciones postales de los Estados Unidos (descontando el hecho de que él es Britanico). En [sus palabras](https://www.w3.org/People/Berners-Lee/FAQ.html#etc):

>En el correo caracol (correo tradicional) en los Estados Unidos, al menos, es común usar el símbolo cardinal para un número de departamento o número de unidad dentro de un edificio. Así que 12 Acacia Av #12 significa “El edificio en Avenida Acacia 12, y luego dentro de ese edificio la unidad conocida como la número 12”. Parece un carácter natural para la tarea. Ahora, http://www.example.com/foo#bar significa “Dentro del recurso http://www.example.com/foo, la vista conocida como bar”.

Resulta que el [sistema original de Hipertexto](https://en.wikipedia.org/wiki/NLS_(computer_system)), creado por Douglas Engelbart, también usaba el carácter ‘#’ para el mismo propósito. Esto puede ser una coincidencia o puede ser un caso accidental de “tomar prestada una idea”.

Los fragmentos no están explícitamente incluídos en los requerimientos HTTP, lo que significa que solo viven dentro del navegador. Este concepto probó ser muy valioso cuando fue momento de implementar la navegación del lado del cliente (antes de que [pushState](https://developer.mozilla.org/en-US/docs/Web/API/History_API) fuera introducido). Los fragmentos fueron también muy valiosos cuando llegó el momento de pensar sobre cómo podemos almacenar estados en las URLs sin enviarlos al servidor. ¿Qué podría significar eso? Explorémoslo:


## Granos de arena y Montañas
>Hay todo un estándar, tan asqueroso como el SGML, sobre Electronic data Intercahnge \[sic\] (intercambio electrónico de datos): formularios y envío de formularios. No sé nada al respecto, excepto que luce como fortran al revés, sin espacios.

— Tim Berners-Lee, [1993](http://1997.webhistory.org/www.lists/www-talk.1993q1/0091.html)

Hay una percepción popular de que los cuerpos de estandarización de Internet no hicieron mucho desde la finalización del HTTP 1.1 y el HTML en 4.01 en 2002 hasta el momento en que se empezó a utilizar el HTML 5. Este período es también conocido (solo por mí) como la Edad Oscura del XHTML. La verdad es que la gente de estandarización estaba *fantásticamente ocupada*. Simplemente estaba ocupada en cosas que finalmente no fueron tan valiosas.
Uno de esos esfuerzos fue la Web Semántica. El sueño era crear un Resource Description Framework (Estructura de Descripción de Recursos) (nota editorial: corré de cualquier equipo que busca crear un framework), el cual permitiría que los metadatos sobre el contenido fueran universalmente expresados. Por ejemplo, en lugar de crear una linda página web sobre mi Corvette Stingray, crearía un documento RDF describiendo su tamaño, color, y el número de multas por exceso de velocidad que he tenido manejándolo.
Esto, por supuesto, no es una mala idea. Pero el formato era basado en XML, y hubo un gran problema del huevo y la gallina entre tener el mundo entero documentado y hacer que los navegadores hagan algo útil con esa documentación.
Sí proveyó, sin embargo, un poderoso ambiente para discusiones filosóficas. Una de las mejores discusiones duró al menos diez años, y fue conocida por su increíble nombre [‘httpRange-14’](https://www.w3.org/2001/tag/issues.html#httpRange-14).
httpRange14 buscaba responder la pregunta fundamental de qué es una URL. ¿Una URL tiene que referir a un documento o puede referir a cualquier cosa? ¿Puedo tener una URL que apunta a mi auto?
No intentaron responder esa pregunta de ninguna manera satisfactoria. En su lugar hicieron foco en cómo y cuándo podemos usar redirecciones 303 para apuntar usuarios desde vínculos que no son documentos a los que sí lo son, y en cuándo podemos usar fragmentos URL (la parte después del ‘#’) para [apuntar usuarios a datos vinculados](http://blog.iandavis.com/2010/11/a-guide-to-publishing-linked-data-without-redirects/).
Para la mente pragmática de hoy en día, esto parecería ser una pregunta tonta. Para muchos de nosotros, podés usar una URL para lo que se te ocurra, y la gente usará tu “cosa” o no lo hará. Pero a la Web Semántica le importa solo la semántica, así que se armó.
Este tema en particular fue discutido el [1ro de julio de 2002](https://www.w3.org/2002/07/01-tag-summary#arch-doc), [15 de julio de 2002](https://www.w3.org/2002/07/15-tag-summary#L3330), [22 de julio de 2022](https://www.w3.org/2002/07/22-tag-summary#L3974), [29 de julio de 2002](https://www.w3.org/2002/07/29-tag-summary#httpRange-14), [16 de septiembre de 2002](https://lists.w3.org/Archives/Public/www-tag/2002Sep/0127), y en al menos otras 20 ocasiones en 2005. Fue resuelto por la gran [resolución httpRange-14](https://lists.w3.org/Archives/Public/www-tag/2005Jun/0039.html) de 2005, luego reabierta en [2007] y [2011] y [un nuevo llamado para nuevas soluciones] en 2012. La pregunta fue duramente discutida por el [pedante grupo](https://groups.google.com/forum/#!searchin/pedantic-web/httprange-14/pedantic-web/iLY6VFvN-H0/SXQwc-lOpM8J), que está muy bien nombrado. Lo único que no pasó fue que todos esos datos semánticos fueran puestos en la web detrás de una URL.


##Autenticación
Como ya sabrás, podés incluir nombre de usuario y contraseña en las URLs:
`http://zack:shhhhhh@zack.is`

El navegador luego codifica esos datos de autenticación en [Base64](https://en.wikipedia.org/wiki/Base64), y lo manda como un encabezado:

`Authentication: Basic emFjazpzaGhoaGho`

La única razón para el codificado en Base64 es para permitir caracteres que pueden no ser válidos en un encabezado, no provee protección a los valores de usuario y contraseña.
Particularmente en la Internet anterior al SSL, esto era muy problemático. Cualquiera que pudiera pispear tu conexión podía fácilmente ver tu contraseña. [Muchas alternativas](http://1997.webhistory.org/www.lists/www-talk.1993q3/0297.html) fueron propuestas incluido [Kerberos](https://en.wikipedia.org/wiki/Kerberos_(protocol)) que era un protocolo de seguridad muy usado tanto entonces como ahora.
Como con tantos ejemplos, sin embargo, la [propuesta de autenticación básica](http://1997.webhistory.org/www.lists/www-talk.1993q3/0882.html) fue la más fácil de implementar para los desarrolladores de navegadores (Mosaic). Esto la hizo la primera, y en definitiva la única, solución hasta que se le brindaron herramientas a los desarrolladores para crear sus propios sistemas de autenticación.


## La Aplicación Web
En el mundo de las aplicaciones web, es un poco raro pensar que la base de la web es el hipervínculo. Es un método para vincular un documento con otro que fue gradualmente mejorado con estilos, ejecución de código, sesiones, autenticación y en última instancia se convirtió en la experiencia social compartida de la informática que tantos investigadores de los 70s estaban tratando (y fallando) de crear. Al final, esa conclusión es válida para cualquier proyecto y startup de hoy o ayer: lo único que importa es la adopción. Si lográs que la gente lo use, sin importar la porquería que sea, te ayudarán a convertirlo en algo que necesitan.

El corolario es, por supuesto, nadie lo está usando, no importa cuán bueno es técnicamente. Hay incontables herramientas a las cuales fueron millones de horas de trabajo que precisamente nadie usa hoy en día.
*Esto fue adaptado de una publicación que originalmente apareció en el blog Eager. En 2016 Eager se convirtió en [Cloudflare Apps](https://www.cloudflare.com/apps).

* La versión original de este post se puede encontrar en [The Cloudflare Blog](https://blog.cloudflare.com/the-history-of-the-url/) (inglés).
* Traducción por [@jcasarini](https://twitter.com/jcasarini), revisión por []().
