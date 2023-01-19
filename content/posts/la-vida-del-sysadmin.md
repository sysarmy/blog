---
Title: "La Vida del Sysadmin"
Description: "Una historia de Patch Tuesdays"
Keywords:
- sysarmy
- sysadmin
- sistemas
- updates
- herramientas

Tags:
- sysarmy
- sysadmin
- sistemas
- updates
- herramientas

Thumbnail: assets/la-vida-del-sysadmin-000.png
socialImage: assets/la-vida-del-sysadmin-000.png
featuredImage: assets/la-vida-del-sysadmin-000.png
externalPermlink: "https://medium.com/@jvmbruno-es/la-vida-del-sysadmin-una-historia-de-patch-tuesdays-4641bfc1aac"

Topics:
- sysarmy
- sysadmin
- sistemas
- updates
- herramientas

markup: markdown
date: 2023-01-18
draft: false
---

_Autoría de [Javier V M Bruno](https://medium.com/@jvmbruno-es), publicado originalmente en [Medium](https://medium.com/@jvmbruno-es/la-vida-del-sysadmin-una-historia-de-patch-tuesdays-4641bfc1aac)._

El Administrador de Sistemas, bien conocido como Sysadmin. Este dignatario de la red, las compus, y de, básicamente, todo lo que refiera a tecnología. Este personae que es odiado por las restricciones de seguridad, y es rápidamente olvidado cuando todo funciona bien.

En la que nadie piensa cuando internet funciona bien, pero es el primero en la lista a la hora de que “facebukk.com” dice “dominio no existe”. Quien es atacado a primeras horas del día con un “No puedo imprimir” sin un previo “Buen día, como estas?”. Al que se le trae una laptop personal para ser arreglada, con la promesa de unas facturas, que luego nunca llegan.

Si sos Sysadmin seguramente te sentiste identificado, lo se, nos paso y nos pasa a todos. Mientras Roxana de recepción no para de llamarte porque no puede escuchar su radio favorita porque la pagina no carga, nunca abriendo un ticket. Vos lees que este Patch Tuesdays de Enero tiene como 98 CVEs de los cuales como 10 son críticos.

Nuevamente en la lista de los CVE lees actores conocidos como: NTLM, ODBC Driver, RPC, Print Spooler, Microsoft Office, Microsoft Exchange Server, etc. Y por dentro decís “Cuando van a arreglar todo de manera definitiva?”

Pero no te queda otra, ya es tarde para volver atrás y elegir otra carrera. Ya te decidiste, vas a ser el mejor Sysadmin. Algunos días dudas de tu salud mental, pero te arremangas y seguís adelante.

Necesitas estar en todos lados y al mismo tiempo agregar papel a la impresora de Carla, del segundo piso, que estaba eufórica que no podia imprimir.

Lamentablemente no hay software para hacer que Carla lea el mensaje de error antes de llamarte. Pero si hay software para poder revisar que los parches han sido aplicados. Tengas o no un WSUS. Yo uso EventSentry. Por ejemplo, con los validation scripts puedo ver rápidamente que equipo de la red no esta corriendo el último build (patch):

![](assets/la-vida-del-sysadmin-1.png)
<p style="text-align: center;">Demo Link [Aquí](http://demo.eventsentry.com/softwareinventory?search.type=detailed&search.refresh=&search.group=&search.agg=&search.union=&report=&pageDefault=&search.query=&search.fromDate=&hour=&minute=&meridian=&search.fromTime=&search.toDate=&hour=&minute=&meridian=&search.toTime=&search.limit=50&search.order=application.name&search.sort=asc&columns=recorddate&columns=group&columns=computer&columns=application&columns=version&columns=update&columns=check&columns=downloadurl&columns=endoflife&search.page=1&refresh=).</p>

O, si quisiera, también podría revisar que se haya aplicado un parche especifico:

![](assets/la-vida-del-sysadmin-2.png)
Demo Link [Aquí](http://demo.eventsentry.com/softwareinventory?search.type=detailed&search.refresh=&search.group=&search.agg=&search.union=&report=&pageDefault=&search.query=&search.fromDate=&hour=&minute=&meridian=&search.fromTime=&search.toDate=&hour=&minute=&meridian=&search.toTime=&search.limit=50&search.order=application.name&search.sort=asc&columns=recorddate&columns=group&columns=computer&columns=application&columns=version&columns=update&columns=check&columns=downloadurl&columns=endoflife&search.page=1&refresh=).

Y usando la búsqueda puedo buscar, por ejemplo, si el parche para el CVE-2023–21674 (KB5022282) (Windows Advanced Local Procedure Call (ALPC) Elevation of Privilege Vulnerability) fue aplicado en la computadora del CEO:

![](assets/la-vida-del-sysadmin-3.png)
Demo Link [Aquí](http://demo.eventsentry.com/softwareinventory?search.type=detailed&search.refresh=&search.group=&search.agg=&search.union=&report=&pageDefault=&search.query=&search.fromDate=&hour=&minute=&meridian=&search.fromTime=&search.toDate=&hour=&minute=&meridian=&search.toTime=&search.limit=50&search.order=application.name&search.sort=asc&columns=recorddate&columns=group&columns=computer&columns=application&columns=version&columns=update&columns=check&columns=downloadurl&columns=endoflife&search.page=1&refresh=).

Pero no solo de Windows, también puedo saber si algún software de alguna de las computadoras esta desactualizado:

![](assets/la-vida-del-sysadmin-4.png)
Demo Link [Aquí](http://demo.eventsentry.com/softwareinventory?search.type=detailed&search.refresh=&search.group=&search.agg=&search.union=&report=&pageDefault=&search.query=&search.fromDate=&hour=&minute=&meridian=&search.fromTime=&search.toDate=&hour=&minute=&meridian=&search.toTime=&search.limit=50&search.order=application.name&search.sort=asc&columns=recorddate&columns=group&columns=computer&columns=application&columns=version&columns=update&columns=check&columns=downloadurl&columns=endoflife&search.page=1&refresh=).

Tambien puedo revisar si la impresora esta sin papel, o se quedo sin toner, antes de ir hasta la oficina de Carla:

![](assets/la-vida-del-sysadmin-5.png)

Lo mejor de todo esto, es que absolutamente todo lo publicado aca, viene por defecto en EventSentry. No hay que pasar horas configurando o activando opciones. Con el deploy por defecto ya tenemos todo esto.

Hay algunas cosas del día a día del que no podes tener control. Pero definitivamente podes tener control sobre la red, los dispositivos y, lo mas importante, los parches.

- Autoría de [Javier V M Bruno](https://medium.com/@jvmbruno-es), publicado originalmente en [Medium](https://medium.com/@jvmbruno-es/la-vida-del-sysadmin-una-historia-de-patch-tuesdays-4641bfc1aac).
