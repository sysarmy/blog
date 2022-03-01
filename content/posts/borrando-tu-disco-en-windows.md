---
Title: "Cómo borrar tu disco por completo en Windows"
date: 2022-03-01
draft: false
Description: "¿Sacándote de encima una compu? Te contamos cómo cuidar tu privacidad borrando toda la información de tu disco."
markup: markdown

Keywords:
  - hdd
  - ssd
  - información
  - seguridad
  - privacidad
Tags:
  - sysarmy
  - hdd
  - ssd
  - información
  - seguridad
  - privacidad
Topics:
  - hdd
  - ssd
  - información
  - seguridad
  - privacidad

Thumbnail: assets/hddwipe-thumbnail.jpg
socialImage: assets/hddwipe-thumbnail.jpg
featuredImage: assets/hddwipe-thumbnail.jpg
externalPermlink: "https://www.backblaze.com/blog/how-to-wipe-pc-ssd-or-hard-drive/"
---

_La versión original de este post se puede encontrar en [Backblaze](https://www.backblaze.com/blog/how-to-wipe-pc-ssd-or-hard-drive/) (en inglés)._

¿Seguís guardando una compu vieja porque no sabes cómo limpiar el disco y borrar toda tu información personal? ¿Te preocupa que haya datos incluso después de vaciar la papelera de reciclaje? (Spoiler: sí, hay.)

Siempre está la opción usar un bate. De verdad, la destrucción física es uno de los caminos a seguir (más sobre eso más adelante). Pero hay formas mucho más fáciles y confiables, aunque menos terapéuticas, de asegurarte de que tu PC con Windows esté tan limpia como el día que salió de la fábrica.


### Primero lo primero: copia de seguridad 👀

Antes de salir a buscar el bate (o seguir los sencillos pasos a continuación), por favor asegurate de que tus datos estén respaldados usando una [estrategia de respaldo 3-2-1](https://www.datos101.com/en/blog/copias-de-seguridad-que-es-la-regla-3-2-1/), guardando tres copias de los datos, en dos tipos de medios, con una copia de seguridad en otro lugar físico. La primera copia es la que está en tu computadora. La segunda se puede guardar en un disco duro externo u otro medio externo. Y la tercera copia debería guardarse en una ubicación externa como _la nube_. Si no estás haciendo una copia de seguridad de una copia externa, ahora es un buen momento para comenzar.

Windows 7, 8, 8.1, 10 y 11 tienen utilidades básicas que se pueden usar para crear una copia de seguridad local en un disco duro externo, que se puede usar para mover archivos a una computadora nueva o simplemente para tener una copia de seguridad local por seguridad. Una vez que hayas realizado una copia de seguridad, vamos a poder borrar el disco interno de tu computadora.

## Cómo limpiar completamente una PC

Primero, tenés que averiguar si tu PC con Windows tiene un [disco duro](https://es.wikipedia.org/wiki/Unidad_de_disco_duro) (HDD) o un [disco de estado sólido](https://es.wikipedia.org/wiki/Unidad_de_estado_s%C3%B3lido) (SSD). La mayoría de las computadoras de escritorio y notebooks de los últimos años empezaron a venir con SSD, pero se puede averiguar fácilmente para mayor seguridad:

1. Abrí **Configuración**.
2. Escribí "**Desfragmentar**" en la barra de búsqueda.
3. Hacé clic en "**Desfragmentar y optimizar sus unidades**".
4. Ahí vas a poder ver el tipo de medio de tu disco.

![](assets/hddwipe-type.png)

## Cómo borrar el disco de Windows

Ahora que sabemos qué tipo de disco tenés, hay dos opciones para limpiar tu PC:

1. _Restablecer_: en la mayoría de los casos, limpiar una PC es tan simple como reformatear el disco y reinstalar Windows usando la función de _Restablecer_. Si solo estás reciclando, donando o vendiendo tu PC, la función _Restablecer_ hace que sea relativamente difícil para alguien recuperar tus datos, especialmente si también están cifrados. Esto se puede hacer fácilmente en las versiones de Windows 8, 8.1, 10 y 11 para un HDD o SSD.
2. _Borrado seguro con herramientas de terceros_: si restablecer no te da suficiente seguridad de que tus datos no se pueden recuperar, o si tenés una PC con Windows 7 o anterior, hay otra opción. Hay una serie de herramientas de terceros que se pueden usar para borrar de forma segura tu disco, que veremos a continuación. Estas son diferentes dependiendo de si tenés un HDD o un SSD.

Seguí estas instrucciones para las diferentes versiones de Windows para restablecer tu PC:

### Cómo borrar un disco en Windows 10 y 11

1. Entrá en **Configuración** → **Sistema** (**Actualización y seguridad** en Windows 10) → **Recuperación**.
2. En "**Restablecer esta PC**", hacé clic en "**Restablecer**". (En Windows 10 apretá en "**Comenzar**").
3. Elegí "**Eliminar todo**" (si no estás desechando tu computadora, podés usar "_Mantener mis archivos_" para darle a la computadora una buena limpieza para mejorar el rendimiento).
4. Te va a pedir que elijas volver a instalar Windows a través de "_Descarga de la nube_" o "_Reinstalación local_". Si te levantaste con mucha generosidad y querés dejarle al próximo propietario de tu PC una versión nueva de Windows, elegí "_Descarga de la nube_". Esto va a usar Internet. Si lo que planeás es desechar o reciclar tu PC, "_Reinstalación local_" funciona bien.
5. En "**Configuración adicional**", hacé clic en "**Cambiar configuración**" y activá la opción "_Limpiar datos_". Esto lleva más tiempo, pero es la opción más segura.
6. Hacé clic en "**Restablecer**" para iniciar el proceso.

### Cómo borrar un disco en Windows 8 y 8.1

1. Andá a **Configuración** → **Cambiar la configuración de PC** → **Actualizar y recuperar** → **Recuperación**.
2. En "**Quitar todo y reinstalar Windows**", hacé clic en "**Comenzar**", luego hacé clic en "**Siguiente**".
3. Seleccioná "**Limpiar toda la unidad**". Esto lleva más tiempo, pero es la opción más segura.
4. Hacé clic en "**Restablecer**" para iniciar el proceso.

## Borrado seguro utilizando herramientas de terceros

Si tu PC tiene una versión anterior de Windows o si querés tener más control sobre el proceso de borrado, hay algunas herramientas de terceros de código abierto para borrar el disco de tu PC, dependiendo de si tenés un HDD o un SSD.

### Borrado seguro de un HDD

El proceso para borrar un HDD implica sobrescribir los datos, y hay muchas utilidades para hacerlo por tu cuenta:

1. [DBAN](https://dban.org/): esta herramienta ha existido durante años y es una utilidad de limpieza conocida y confiable para HDDs. Se encarga de hacer varios pases de reescrituras (binarios y ceros) en el disco. Para usarlo tenés que descargarlo a una unidad USB y ejecutarlo desde ahí.
2. [Disk Wipe](https://www.diskwipe.org/): otra utilidad gratuita que hace varias reescrituras de datos binarios. Podés elegir entre varios métodos diferentes para sobrescribir el disco. Disk Wipe también es portable, por lo que no es necesario instalarlo para usarlo.
3. [Eraser](https://eraser.heidi.ie/): otra herramienta de uso gratuito. Da mayor control sobre cómo borra el disco. Al igual que Disk Wipe, se puede elegir entre diferentes métodos que incluyen diferentes cantidades de reescrituras, o también elegir una cantidad personalizada.

Tené en cuenta que cualquier herramienta de borrado de disco que realice varias reescrituras va a tomar bastante tiempo para completar.

Si estás usando Windows 7 o más, y sólo estás buscando reciclar tu PC, podés frenar acá. Si tenés la intención de vender o donar tu PC, vas a necesitar los CD de instalación (¿te acordás de esas cosas brillantes redondas?) o también una imagen, para reinstalar una versión nueva de Windows.

### Borrado seguro de un SSD

Si tenés un SSD, es posible que quieras tomarte el tiempo para cifrar tus datos antes de borrarlos para asegurarte de que no se puedan recuperar. ¿Por qué? [La forma en que los SSD almacenan y recuperan los datos es diferente de los HDD](https://www.kingston.com/latam/solutions/personal-storage/ssd-vs-hdd-differences).

Los HDD almacenan los datos en una ubicación física en el plato del disco. Los SSD almacenan datos usando circuitos electrónicos y células de memoria individuales organizadas en páginas y bloques. Escribir y reescribir los mismos bloques una y otra vez desgasta el disco a lo largo del tiempo. Por este motivo, los SSD usan "_nivelación de desgaste_" para escribir en toda la unidad, lo que significa que tus datos no se almacenan en una ubicación física, sino que se distribuye por todo el disco.

Cuando se le pide a un SSD que borre datos, no los sobrescribe, sino que escribe la nueva información en un bloque distinto sin usar. Esto tiene implicaciones al borrar un SSD, y alguno de tus datos _podría_ quedar colgado en alguna parte del SSD incluso después de que haya sido borrado, hasta que la nivelación de desgaste decida sobreescribir ese bloque en específico. Por este motivo, es una buena práctica cifrar los datos en un SSD antes de borrarlo. De esta manera, si quedan datos, al menos nadie podrá leerlo sin una clave de cifrado.

No _tenés_ que cifrar los datos primero, pero si el restablecimiento de Windows no alcanza y llegaste hasta acá, entendemos que es un paso que querés tomar. Incluso si no estás reciclando tu computadora o si tenés un HDD, cifrar tus datos es una buena práctica. Si tu notebook cae en las manos equivocadas, el cifrado hace que sea mucho más difícil para los delincuentes acceder a tu información personal.

Cifrar tus datos no es complicado, pero no todas las computadoras con Windows son iguales. Primero, verificá si tu dispositivo tiene habilitado el cifrado por defecto:

1. Abrí el menú Inicio.
2. Bajá y entrá en el menú desplegable "**Herramientas administrativas de Windows**".
3. Apretá en "**Información del sistema**". También podés buscar "_información del sistema_" en la barra de tareas.
4. Si el valor de "**Compatibilidad con cifrado de dispositivo**" es "_Cumple con los requisitos previos_", genial, el cifrado está habilitado en tu dispositivo.

Si no, el siguiente paso es verificar si el dispositivo tiene BitLocker incorporado:

1. Abrí la configuración.
2. Escribí "_bitlocker_" en la barra de búsqueda.
3. Hacé clic en "**Administrar BitLocker**".
4. Hacé clic en "**Encender BitLocker**" y seguí las indicaciones.

Si ninguna de estas opciones está disponible, podés usar software de terceros para cifrar tu SSD. [Veracrypt](https://veracrypt.fr/en/Home.html) y [Axcrypt](https://www.axcrypt.net/) son buenas opciones. Recordá registrar la clave de cifrado en algún lugar y también el sistema operativo, la versión del sistema operativo y la herramienta de cifrado utilizada para poder recuperar los archivos más adelante si es necesario.

Una vez que hayas cifrado tus datos, el siguiente paso es borrar, y hay algunas opciones:

1. [Parted Magic](https://partedmagic.com/store/): la herramienta de borrado de terceros más recomendada para SSD, pero cuesta 13 dólares. Es una herramienta de arranque como algunas de las herramientas de borrado de HDD, hay que descargarla a una unidad USB y ejecutarla desde ahí.
2. [ATA Secure Erase](https://industrial.apacer.com/en-ww/Technology/ATA-Secure-Erase): es un comando que básicamente electrocuta al SSD. Usa un pico de voltaje para eliminar electrones almacenados. Si bien esto suena dañino (y sí, genera un poco de desgaste), es perfectamente seguro. No sobrescribe los datos como otras herramientas de borrado seguro, por lo que en realidad hay menos daño hecho al SSD.

## La opción nuclear

Cuando no hay otra alternativa más que la destrucción total, asegurate de al menos hacerlo de manera segura. Pregunté para ver si nuestro equipo podría recomendar la mejor manera de reventar el disco. A nuestro administrador de sistemas senior, Tim Lucas, le gustan los explosivos, pero no lo recomendamos. _Podés_ limpiar un disco duro con un imán, proceso conocido como _desmagnetización_, pero un imán de heladera común no va a funcionar. Tendrías que abrir la computadora y sacarle el disco duro, y vas a necesitar un imán de neodimio, uno que sea lo suficientemente fuerte como para eliminar los dígitos (ambos en el disco duro y los que están en tu mano) en el proceso. No es la forma más segura de hacerlo, tampoco.

Si vas a desarmar tu PC para llegar al disco duro de todas maneras, perforar algunos agujeros a través de los platos o darle un baño de ácido son mejores opciones, como nuestro CEO, Gleb Budman, explicó en este artículo de [Scientific American](https://www.scientificamerican.com/article/how-to-destroy-a-hard-drive-permanently/) (en inglés). Los agujeros distorsionan los platos, y el ácido corroe la superficie. Ambos hacen que un HDD se vuelva ilegible.

Al final, todavía seguimos sosteniendo que la forma más segura de destruir un HDD, y la única forma en que recomendaríamos destruir físicamente un SSD, es **triturarlo**. Te recomendamos consultar con tu centro de reciclaje de electrónica local para ver si tienen una trituradora que se pueda usar (o si al menos te dejarían ver cómo unos engranajes de metal gigantes destruyen el disco). Sin embargo, la trituración _debería_ ser el último recurso. Los discos generalmente duran de 5 a 10 años, y millones se destruyen cada año antes del final de su vida útil. Si bien destruir tu disco duro puede ser muy divertido, seguramente puedas encontrar algo aún más divertido de hacer con ese disco viejo.

¿Todavía tenés preguntas sobre cómo borrar o destruir de forma segura tus discos? Contanos en los comentarios. Y si tenés curiosidad por cómo borrar un HDD o SSD desde Mac, leé nuestra guía [acá](https://www.backblaze.com/blog/how-to-wipe-a-mac-hard-drive/) (en inglés).

- La versión original de este post se puede encontrar en [Backblaze](https://www.backblaze.com/blog/how-to-wipe-pc-ssd-or-hard-drive/) (inglés).
- Autoría de [Molly Clancy](https://www.backblaze.com/blog/author/molly/), traducción por [@nachichuri](https://twitter.com/Nachichuri), revisión por [@jedux](https://twitter.com/jedux).
