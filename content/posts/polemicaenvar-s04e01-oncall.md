---
Description: "Polémica en /var S04E01 #oncall"
Keywords:
- sysadmin 
- sistemas
- oncall
- polemicaenvar
Section: 
Tags:
- sysarmy
- podcast
- polemicaenvar
- oncall
Thumbnail: assets/pager-911-640x480.jpg
socialImage: assets/pager-911-640x480.jpg
featuredImage: assets/pager-911-640x480.jpg
Title: Polémica en /var S04E01 - On Call 
Topics:
- sysarmy
- polemica
- mesa
- oncall
markup: markdown
date: 2020-05-27
---

En este episodio nos metemos de lleno en lo que significa estar de guardia, procesos, metodologías y todo lo que necesitas saber.

[Escuchanos en Spotify](https://open.spotify.com/episode/4PUqE3lbOI4vdwJKnNX2Oe?si=WJxn6KvoSwqN4ChEpTCMIQ)

<!--more-->

Cuales son los roles clave, como es el proceso de aprendizaje y cómo gestionar la compleja maquinaria de las operaciones en el momento de estar de guardia. Participan de este segmento [Vero](https://twitter.com/verovand), [Reshi](https://twitter.com/Rhapsody_Girl), [Andrea](https://twitter.com/peorth), [Godlike](https://twitter.com/godlike64), [Jolo](https://twitter.com/ajolo) y [Edu](https://twitter.com/jedux)

Dejamos algunas notas del episodio:

# 101
- En un mundo ideal, no sería necesario.
- La forma de manejar situaciones imprevistas.
- Aún con 100% automation, siempre pasa algo excepcional.
- Lo imprevisto no respeta agenda ni calendar.

# Diseño del oncall
- El grupo se turna en ser la persona en atender las alertas.
- Cobertura 24x7.
- La persona de turno hace todo lo humanamente posible para solucionar incidentes.
- La solución no tiene por qué ser “limpia” o “elegante”. Tiene que solucionar. YA.
- Si no se puede -> escalation!

# SLA
- Unidad de medida: SLA. Lo que los incidentes en definitiva rompen.
- “Cuánto tiempo puede estar esto caído?” (0 segundos no vale)
- Armar esquema de respuesta en base al SLA.
- Configurar alertas.
- Latencia humana (tiempo entre alerta emitida y hands on keyboard/garfios en ssh).
- Distintos servicios/aplicaciones pueden tener distinto SLA.
- Distintas guardias para cada componente? Una para todos y todos para una?

# Roster
- La guardia es la responsabilidad principal de ops.
- New hires -> training para el oncall (skills, shadowing, etc).
  - Definir ventana de tiempo para que los jr. pasen a la rotación de oncall.
- Ssr. -> al oncall
- Senior -> al oncall
  - Si no hacen guardias, peligra que se “desconecten” de los incidentes.

# Períodos
- Semanal
  - Hacer el corte en la mitad de la semana
- Diario
- Split (por turnos, cubriendo 24x7)
- Follow the Sun
- Requiere dispersión geográfica
- Mejor opción, puede cubrir 24x5 ~

# Notificaciones
- Sólo lo realmente urgente+importante es alerta. Evitar “El pastor y el lobo”.
- Alerta: se rompió el SLA o se va a romper, #fuego, destrucción.
- Para todo lo demás:
  - Se crea ticket
  - Se loguea a un archivo
  - No le importa a nadie
- No usar email como alerta.
- El email como método complementario funciona muy bien.
- Hay que despertar al oncall. Considerar alertas simultáneas, y que requieran ACK.

# OODA Loop
- Observe, Orient, Decide, Act. Deriva de jerga militar, fighter jet pilots. Kyle Brandt propuso aplicarlo a la administración de sistemas. High stress, quick reaction.
- Observe: logs, status, uso de recursos.
- Orient: interpretar los datos, armar una hipótesis de lo que creemos está pasando.
- Decide: cuál es el siguiente paso. Puede ser recabar más información.
- Act: hacer algo al respecto. Puede ser el fix, testear una hipótesis, o darnos más data.
- Es un loop, siempre hay varias iteraciones.

# Postmortems
- Analizar un outage y documentar qué pasó y por qué. Recomendar acciones a futuro.
- En todas las direcciones: comunicar a managers, equipos, usuarios. Interna y externamente.
- No empieza hasta que termina el outage. Primero el fix (quick o long term).
- No finger-pointing, blameless. Con culpa no hay transparencia.
- “Name and shame” -> “Cover your ass”
- “Blameless PostMortems and a Just Culture” - John Allspaw
- Accountability rather than blame

Hasta la próxima!
