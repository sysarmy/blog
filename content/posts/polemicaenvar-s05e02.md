---
Description: "Las noticias de Marzo 2021! - Polémica en /var S05E02"
Keywords:
- sysadmin 
- discord
- microsoft
- agile
- icloud
- nft
- whatsapp
- oracle
- google
- polemicaenvar
Section: 
Tags:
- sysadmin 
- polemicaenvar
- microsoft
- oracle
- google
- discord
Thumbnail: assets/polemicaenvar-s05e02.jpeg
socialImage: assets/polemicaenvar-s05e02.jpeg
featuredImage: assets/polemicaenvar-s05e02.jpeg
Title: Las noticias de Marzo 2021! - Polémica en /var S05E02
Topics:
- sysadmin
- microsoft
- google
- discord
- oracle
- nft
- whatsapp
- icloud 
- polemicaenvar
markup: markdown
date: 2021-04-07
---

Participan de este episodio: [Edu](https://twitter.com/jedux), [Godlike](https://twitter.com/godlike64) y [Andrea](https://www.twitter.com/peorth)  

<!--more-->

{{< youtube EX_ORKWr6IY >}}

# Noticias

### [A person whose last name is ´True has been locked out of iCloud for 6 months](https://twitter.com/NGKabra/status/1368069088124149760)
Me fascinan las historias de data mal parseada. Sera porque tuve que renegar mucho tiempo con cosas muy bizarras en estos veintipico de aÃ±os que llevo programando. 
La cuestión es que una persona llamada Rachel True (si, True, como verdad en ingles) desde hace meses que no puede usar su cuenta de iCloud, porque al tratar de loguearse, le da un error diciendo "Imposible parsear el valor 'true' en el campo 'lastName'. 
Apellido, True, campo True... ya ven para que lado va esto, no? Si, probablemente Apple esta usando algun JSON con los datos de la persona, y al tratar de meter el apellido TRUE, le esta dando un error, porque lastName espera una palabra, pero no un 'true'. Probablemente lo mismo pase si se llama Richard False. Fallara también si alguien se llama Juan Carlos NULL? 
Little Bobby Tables ataca de nuevo!

### [The Agile Manifesto 20 years on: agility in software delivery is still a work in progress](https://www.zdnet.com/article/the-agile-manifesto-20-years-on-agility-in-software-delivery-is-still-a-work-in-progress/)	

### [A AT&T no le gusta el upload, ni la fibra, ni la banda ancha](https://arstechnica.com/tech-policy/2021/03/att-lobbies-against-nationwide-fiber-says-10mbps-uploads-are-good-enough/)

Todo empezó con un blog post, como empiezan la mayoría de los desastres en el siglo XXI. Joan Marsh, VP de AT&T respondió así tácitamente a una propuesta del Congreso de EEUU para desplegar banda ancha y fibra con 
velocidades de download Y upload de 100Mbps a zonas rurales que actualmente no tienen servicio. Para AT&T, la definición de banda ancha de la FCC, que tiene ya 6 años y la define como 25/3, está perfecto para trabajar por Zoom y aprendizaje remoto (cuando hablamos de una sola persona), y le parece que está bien cumplir con estas necesidades con VDSL, una tecnología que tiene 14 años. 
Pero claro, para entender a AT&T, recordemos que en 2014 le pidió por favor a la FCC que mantuviera el estándar de banda ancha en 4/1, diciendo que una velocidad de bajada de 10Mbps "era más que los que los estadounidenses necesitaban". Curiosamente lo mismo que dice ahora. También en su blog post hablaron de no hacer "overbuilding", que vendría a ser lo que AT&T cataloga 
como desplegar su cobertura en una zona en donde ya hay un ISP. Lo que sucede es que los usuarios a esto le llaman "competencia". En fin, suponemos que Elon va a terminar salvando a todos con Starlink, 
que ya ofrece en beta 100/20 con latencias de alrededor de 30ms (un chiste de latencia para los que vivimos del otro lado del Ecuador), e incluso promete reducir la latencia y 300Mbps de bajada para este año.

### [Microsoft in talks with Discord over $10 billion-plus acquisition](https://www.theverge.com/2021/3/22/22345792/microsoft-discord-acquisition-report-10-billion)	
Esta noticia es medio ipo-falopa, pero como es de jueguitos, me toco a mi. Microsoft esta en avanzadas tratativas de comprar DISCORD. Si, el programita que usan para charlar con su grupo de amigos, juegos, comunidades, etc.  Discord fue valuado recientemente en 7 billones de dolares, y Microsoft, que se nota que anda con ganas de gastar un poquito de plata, hizo una generosa 
oferta por un poco mas de 10 billones de dolares. Todavia al dia de hoy es un rumor, pero parece que Discord tuvo varias reuniones con distintas empresas, y ya firmo un contrato con una empresa (hint hint) y que se daria a conocer en cualquier momento quien es. Discord tiene mas de 140 millones de usuarios mensuales y reporto mas de 130 millones de dolares en ganancias. 
La mayoria de las funcionalidades son gratuitas, pero pagando 9.99 dolares por mes, tenes acceso a NITRO, que le da algunas funcionalidades mas copadas a tu comunidad. 
Recuerden que tenemos nuestro propio [discord](https://sysar.my/discord), que esta conectado a [Slack](https://sysar.my/slack) y también conectado a la red maestra del mundo mundial, IRC!
 
### [WhatsApp for work: Slack is turning into a full-on messaging app](https://www.protocol.com/slack-messaging-connect)

### [A Oracle no le gusta esto](https://www.theverge.com/2021/4/5/22367851/google-oracle-supreme-court-ruling-java-android-api)	
Después de más de 10 años entrando y saliendo de los juzgados, parece que termina la batalla legal entre Oracle y Google. Recordemos que Oracle, fresquito después de comprar a Sun en 2010, ese mismo año 
(que no se note tanto, chicos) demandó a Google por violación de patentes y copyright de Java en el sistema operativo Android. Para Oracle, Google desarrolló Android sin una licencia de Java y copió sus APIs. 
Ya en 2012 la cuestión de patentes fue desestimada por la justicia, y quedaba solo la parte de copyright, que siguió hasta hoy. Recordemos también que Google hizo una versión cleanroom (ingeniería inversa y recrear desde cero, sin violar copyright) de Java, sin acceso al código de Sun, que terminó transformándose en Dalvik. Parte de Dalvik incluía 37 llamadas de API y 11500 
líneas de código tomadas de Apache Harmony, otra implementación cleanroom de Java. Después de muchas idas y vueltas, el lunes 5 de abril SCOTUS (la Corte Suprema de Justicia de EEUU) falló a favor de Google, concluyendo que las APIs son significativamente diferentes de otros tipos de programas, y catalogó el accionar de Google como 'fair use' (el famoso "permitido" del copyright). 
Oracle, mal perdedor, sigue sosteniendo que Google se robó Java (sic). La pregunta que nos hacemos todos es: si Oracle compró Sun para demandar a Google por Android, qué va a hacer ahora?

### Discusión: [NFT](https://www.cnn.com/2021/03/23/tech/jack-dorsey-nft-tweet-sold/index.html)

Hasta el próximo episodio!
