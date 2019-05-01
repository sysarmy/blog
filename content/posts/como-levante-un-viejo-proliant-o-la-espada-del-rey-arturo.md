---
Description: "Sysarmy - Comunidad de sistemas"
Keywords:
- sysadmin 
- sistemas
- desarrollo
- developer
- administración de sistemas
- administrador de sistemas
- linux
- cloud
- docker
- kubernetes
Section: 
Slug: como-levante-un-viejo-proliant-o-la-espada-del-rey-arturo
Tags:
- sysarmy
Thumbnail: /blog/assets/img_20170703_201217_766.jpg
Title: Como levanté un viejo Proliant (O la espada del Rey Arturo)
Topics:
- Development
- Leadership
- Systems
Url: 2017/08/15/como-levante-un-viejo-proliant-o-la-espada-del-rey-arturo
date: 2017-08-15
---

<p><em>Por <a href="http://twitter.com/pcarboni">Pablo Carboni</a>.</em></p>
<p>El sábado de la última semana de junio, asistí a <a href="http://nerdear.la">nerdear.la 2017</a> - puntual, 9hs - a las charlas previstas. Además de eso, concurrí con una vieja notebook (año 2000), con todo sus elementos originales, CDs grabados inclusive, de FreeBSD(4.x), lista para donarla al Museo de la Informática.</p>
<p>En el evento había como desafío 'revivir' un Compaq Proliant DL360 G1 (2001) e instalarle un servidor web.</p>
<p>Todo el mundo había intentado bootear diferentes CDs de Linux....sin éxito. Me habían comentado que estuvieron incluso el día anterior hasta 4 horas(!!) y nada. Incluso probaron reconectar varias veces la lectora, inútilmente.</p>
<p>Por mi parte, con la curiosidad (y a veces insistencia) que me caracteriza, probé iniciar el server. Observé que el BIOS testeaba OK la lectora (breve parpadeo de la misma) y luego booteaba el RAID-1 armado con sus discos de 36GB. Luego entonces, me pregunté: ¿Por qué no pruebo con los CDs que tengo grabados hace 15 años? Quizás sea lectora sucia, o bien velocidad de grabación.</p>
<p>Luego de insertar un FreeBSD 4.9, booteó sin problemas e instalé todo lo necesario como para que tenga red. Incluso, le puse un viejo Bash + lynx. La página de Google.com se visualizó enseguida! (sin soporte de https) Nota: Dada la antigüedad del OS, es necesario hacer una serie de upgrades adicionales para llevarlo a FreeBSD 11.0, e instalar un NGINX o bien un Apache.</p>
<p>Durante la fiesta de cierre de nerdear.la, Werner Almesberger -habitué de eventos de SysArmy- , hizo la extraña(?) comparación entre la espada del Rey Arturo y el CD de instalación que usé para levantar el server en 2 minutos ;-)</p>