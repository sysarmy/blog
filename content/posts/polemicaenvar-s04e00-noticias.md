---
Description: "Polémica en /var S04E00"
Keywords:
- sysadmin 
- sistemas
- desarrollo
- polemicaenvar
Section: 
Tags:
- sysarmy
- podcast
- polemicaenvar
- sistemas
Thumbnail: assets/larry_tesler.jpg
socialImage: assets/larry_tesler.jpg
featuredImage: assets/larry_tesler.jpg
Title: Polémica en /var S04E00
Topics:
- sysarmy
- polemica
- noticias
markup: markdown
date: 2020-04-06
---

Increíble pero cierto, arrancamos la 5ta temporada de Polémica en /var ! charlamos sobre algunas de las noticias que transcurrieron en el último mes(es).
Nos adaptamos a los tiempos que corren y cambiamos el formato a una videollamada donde repasamos lo más interesante del mundo de sistemas.

[Escuchanos en Spotify](https://open.spotify.com/episode/54rOiXC2dyoyKOaBxfw0IB?si=FYKsjR3ETeKWxMihlGlW5g)

<!--more-->

# Gracias a nuestros Sponsors de Nerdearla 2020
Accenture, WildLife, Santander, Despegar, Nubiral, PedidosYa, Cognizant/Softvision, Tiendanube, ASAPP, Onapsis, Galicia, Innovid, IBM, openqube

# Búsquedas laborales

#### Accenture
- [Python Developer](https://sysar.my/dI65xL): Python,Oracle and No Sql, Agile development

#### Despegar
- [Backend developer](https://sysar.my/HMC2lj): Java, Scala, NoSQL.

#### Santander 
- [Frontend developer](https://sysar.my/laN05W), agnóstico de tecnología

#### Wildlife Studios
- [Site Reliability Engineer](https://sysar.my/el08X6): Linux, AWS, Kubernetes


# Noticias

### [- Russia successfully disconnected from the internet](https://www-zdnet-com.cdn.ampproject.org/c/s/www.zdnet.com/google-amp/article/russia-successfully-disconnected-from-the-internet/)
Rusia probó desconectarse de internet y validar escenarios de continuidad de RUNET, escenarios de integridad, seguridad y estabilidad de la Internet, ademas de escenarios de seguridad móvil, proteccion de datos, habilidad para interceptar tráfico, etc.

### [Rambler will drop NGINX criminal case](https://www.zdnet.com/article/rambler-will-drop-nginx-criminal-case/)
Rambler, empresa que había denunciado a Nginx por copyright, dropea el caso criminal, podría seguir como caso civil. Toda la russian tech scene se le paró de manos a rambler

### [Linus Torvalds: Linux Scheduler Not To Blame For Google Stadia Port Issues](https://www.tomshardware.com/news/linus-torvalds-linux-scheduler-not-to-blame-for-google-stadia-port-issues)
Un developer culpó al scheduler de Linux por la forma en la que están implementados los spinlocks. Que daban hasta 100ms delay. Linus le respondió cómo usarlos correctamente, que no usen spinlocks en user space a menos que sepan lo que están haciendo y que la probabilidad de que sepa lo que está haciendo es nula.

### [Don’t Use ZFS on Linux: Linus Torvalds](https://itsfoss.com/linus-torvalds-zfs/)
Linus no va a mergear código de ZFS a menos que el abogado principal de Oracle o Larry Ellison le firme una carta permitiéndoselo.

### [Is SMS 2FA Secure?](https://www.issms2fasecure.com/) 
No.

### [ProtonVPN libera el código de todas sus aplicaciones](http://bit.ly/30H3wUP)

"Somos el primer proveedor de VPN en hacer esto"
Estudios han descubierto que más de un tercio de las VPNs para Android contienen realmente malware, muchas VPNs han sufrido importantes fallos de seguridad y muchos servicios VPN gratuitos que dicen proteger la privacidad están vendiendo secretamente los datos de los usuarios a terceros.

### [250 millones de registros de clientes de M$ expuestos](https://www.comparitech.com/blog/information-security/microsoft-customer-service-data-leak/)
Un error de configuración en una base de datos de soporte al cliente dejó al descubierto 14 años de registros de conversaciones entre clientes de Microsoft y su equipo de soporte.

### [CacheOut](https://cacheoutattack.com/)Leaking Data on Intel CPUs via Cache Evictions
An attacker can exploit the CPU's caching mechanisms to select what data to leak, as opposed to waiting for the data to be available. can violate nearly every hardware-based security domain, leaking data from the OS kernel, co-resident virtual machines, and even SGX enclaves. Todo < Q4 2018 está afectado. Ya hay updates de microcódigo disponibles.

### ["Poder Judicial: rotura del Storage HPXP 2400"](https://twitter.com/nicolaslucca/status/1222284746148995072?s=21)
El proveedor (Hewlett Packard) dice que no sabe si lo puede reparar y que el equipo ya ni se fabrica. Así que salieron a buscar proveedores urgentemente. Bueno, todo lo urgente que se puede esperar de un quilombo que comenzó hace una semana. Restauracion 48/72 horas.

### [Google Maps Hacks](https://twitter.com/simon_deliver/status/1223569659645112320?s=19) & [this twit](http://www.simonweckert.com/googlemapshacks.html)
Berlin, 99 telefonos, tardo un añoo en conseguir los 99 telefonos baratos y sus amigos le prestaron para armar alto bardo.


### [Researchers can 'steal' data by tracking a PC monitor's brightness](https://www.engadget.com/2020/02/05/stealing-data-by-tracking-lcd-brightness/) No network connection required.
Encontraron como “robar” datos usando el brillo del monitor
No te van a robar el password de root de tu maquina, sino que apunta mas a un caso donde una persona pueda, a traves de un malware, cambiar el brillo o configuraciones que pueden ser imperceptibles para el ojo humano, pero que una camara de seguridad podria llegar a ver. Es bastante rebuscado, con no correr nada que no estemos seguro de su preferencia no deberia haber problemas. 

### [Apple fined for slowing down old iPhones](https://www.bbc.com/news/technology-51413724)
25 million euros
So, it released a software update for the iPhone 6, iPhone 6s and iPhone SE which "smoothed out" battery performance.

### [Voyager 2 bounces back from glitch in interstellar space](https://www.space.com/voyager-2-resumes-science-operations.html)
On Jan. 25, the venerable probe, which has been exploring interstellar space since November 2018, failed to execute a spin maneuver as intended. As a result, two onboard systems remained on longer than planned. Lanzada en 1977 (voyager 1 & 2). 13.5 billion km from Earth. ~35 horas RTT. 3 computadoras on board (replicadas) 250KHz, 68KB. Benemérito y nunca bien ponderado reboot.

### [CDPWN](https://www.armis.com/cdpwn/)
Five critical zero-day vulnerabilities in various implementations of the Cisco Discovery Protocol (CDP) that can allow remote attackers to completely take over devices  without any user interaction.

### [The Computer Scientist Responsible for Cut, Copy, and Paste, Has Passed Away](https://gizmodo.com/larry-tessler-modeless-computing-advocate-has-passed-1841787408/amp?fbclid=IwAR3mbqxl3ip7crLyQrEOg4YmfSkkBVFiyMJAs4nB0HxmbxlWfqHdrVbivxE&__twitter_impression=true)
Tesler worked with Tim Mott to create a word processor called Gypsy that is best known for coining the terms “cut,” “copy,” and “paste” when it comes to commands for removing, duplicating, or repositioning chunks of text.

### [Hackearon la aplicación que avisa cuando llega el colectivo y los atacantes pidieron un “rescate” en criptomonedas](https://www.infobae.com/sociedad/2020/02/20/hackearon-la-aplicacion-que-avisa-cuando-llega-el-colectivo-y-los-atacantes-pidieron-un-rescate-en-bitcoins/)
Sistema funciona(ba) bastante bien y era bastante exacto. En Rosario no hay tantas lineas de colectivo, por lo que tampoco tenia muchos datos
Compartia base de datos/sistema con otras 3 ciudades (Santa Fe, Cordoba y Mar del plata)
No fue un ataque puntual a esto, probablemente se metieron por un server no parcheado. 
Ransomware
No tenian backup (!), pero eventualmente volvio a funcionar. No se dijo si se pago el rescate o aparecio un backup perdido
Google maps como alternativa


### [Murió el inventor del código Konami, el truco más famoso de la historia de los videojuegos: funciona hasta en Netflix](https://www.clarin.com/tecnologia/murio-inventor-codigo-konami-truco-famoso-historia-videojuegos-funciona-netflix_0_TPl-qdzk.html)
Arriba, arriba, abajo, abajo, izquierda, derecha, izquierda, derecha, B, A
Todo empezó con Gradius, un juego “matamarcianos” de 1985 que Konami lanzó en los arcades. Hashimoto, el programador de la versión de NES del juego, se cansó de la altísima dificultad del juego. Juego que él mismo había desarrollado, por cierto. Al ejecutar esa combinacion de movimientos y botones, el juego le daba al jugador todos los powerups inmediatamente
En Netflix, Google Hangouts, Facebook tambien se puede (o podia) correr
35 años despues el codigo sigue vivo y muchos cheaters hunters es lo primero que ejecutan al probar un juego nuevo


### [Let's Encrypt issues one-billionth web security certificate](https://www.zdnet.com/google-amp/article/lets-encrypt-issues-1-billionth-web-security-certificate/)
In less than five years, Let's Encrypt has secured almost 200 million websites with free TLS certificates.
81% websites usan https hoy en día. 200 million websites.

### [Let's Encrypt identified a bug in their CAA checking and disabled issuance for 2h 12m whilst they patched](https://twitter.com/Scott_Helme/status/1234853555116421121?s=19)
Hubo un problema en el código que verifica los registros CAA (Certificate Authority Authorization - The purpose of the CAA record is to allow domain owners to declare which certificate authorities are allowed to issue a certificate for a domain.). 3M de certificados afectados, LE estuvo mandando notificaciones y revocando certs. Hay comandos para chequear en la página de LE si estás afectado (incidente 4 de marzo). Ante la duda -> regenerar.


### [TikTok Told Moderators to Suppress Posts by “Ugly” People and the Poor to Attract New Users](https://twitter.com/amartino/status/1239549154524872704?s=09) & [this](https://theintercept.com/2020/03/16/tiktok-app-moderators-users-discrimination/)
TikTok habría desarrollado en algún momento reglas de moderación para perseguir el contenido de aquellos que tuvieran una forma corporal "anormal, barriga cervecera, obesidad" o que tuvieran "rasgos faciales feos o deformidades". "un intento contundente y temprano para prevenir el bullying", pero ya no se encuentran operativas y, en algunos casos, nunca lo estuvieron.

### [Linux Kernel's Floppy Disk Code Is Seeing Improvements In 2020](https://www.phoronix.com/scan.php?page=news_item&px=Linux-5.7-Floppy-Improvements)
This isn't just a couple one-liner patches either for Linux's floppy code but is 586 lines of new code and 613 deletions -- principalmente ARM

### [German Military Laptop Sold on eBay Included Classified Missile Information](https://www.nytimes.com/2020/03/17/world/europe/germany-missile-laptop.html)
Pentium III, 12mb de memoria, pesa 4.5kg, Windows 2000 --  a confidential user manual and schematics for a surface-to-air missile system that Germany’s air force still uses.

### [The Next Chapter of Meetup](www.meetup.com/blog/the-next-chapter-of-meetup/)
Meetup has divested from WeWork and has been acquired by an investment group formed for the express purpose of acquiring Meetup. 
In 2019 alone, there were over 30 million hours of human connections on Meetup. That’s an average of 15,000 events per day. Those events took place in 193 countries, in over 2,200 cities, and were hosted by over 30,000 organizers.

## Coronavirus
--------------

### [Spying concerns raised over Iran's official COVID-19 detection app](https://www.zdnet.com/google-amp/article/spying-concerns-raised-over-irans-official-covid-19-detection-app/?__twitter_impression=true)
Google removes Iran's official COVID-19 detection app from the Play Store.
La app irani guardaba el numero y la geolocalizacion.
Google da de baja todas las apps referidas al Coronavirus en Google Play

### [After SETI, 'Folding@Home' Takes Up the Fight Against COVID-19](https://science.slashdot.org/story/20/03/07/1733254/after-seti-foldinghome-takes-up-the-fight-against-covid-19)
Seti @ home fue usada durante muchisimos años por la gente para buscar vida extraterrestre
Corre en el tiempo idle de tu maquina, analizando archivos de audio, buscando patrones “fuera de lo comun”. 
Hace unos años se dio de baja
Folding @ Home tomo la posta para usar el tiempo idle de tu computadora, y ahora quieren usarlo para encontrar las estructuras de la proteina relacionada al COVID-19
NO ES PARA BUSCAR LA VACUNA especificamente, sino para entender como “funciona” molecularmente el virus, se espera que estos datos puedan usarse para encontrar anticuerpos, que eventualmente puedan ayudar a armar la vacuna

### [Italian hospital saves Covid-19 patients lives by 3D printing valves for reanimation devices](https://www.3dprintingmedia.network/covid-19-3d-printed-valve-for-reanimation-device/)

### [La cuarentena por coronavirus hizo crecer el uso de videojuegos: Fortnite a la cabeza](https://www.infobae.com/gaming/2020/03/13/la-cuarentena-por-coronavirus-hizo-crecer-el-uso-de-videojuegos-fornite-a-la-cabeza/)
Datos de Italia
Junto a Call of Duty, el battle royale de Epic Games es el elegido por los jugadores para pasar la cuarentena
Pokemon Go, uno de los mas afectados (la gente no puede salir a “cazar” los pokemons. La empresa esta buscando alternativas para permitir que la gente siga jugando sin salir de sus hogares
Algunas empresas de videojuegos (indies y estudios grandes) han lanzado campañas a traves de sus redes sociales regalando codigos de juegos para que la gente tenga nuevos juegos para jugar en distintas plataformas.
Epic games esta regalando en Rayman si quieren aprovechar


### [CABASE Internet Index Estado de Internet en Argentina y la Región Segundo Semestre 2019](https://www.cabase.org.ar/el-70-de-los-hogares-con-internet-contrata-el-servicio-de-banda-ancha-en-combo-con-tv-paga-yo-telefonia/)
Caida del ADSL, Aumento Cablemodem, Tibio aumento de la Fibra optica. Netflix bajo calidad y youtube también para reducir 25% del tráfico generado.

