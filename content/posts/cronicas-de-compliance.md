---
Title: "Crónicas de Compliance: Cómo el SysAdmin dejó la ansiedad y la preocupación"
Description: "Una historia de compliance, sudor y lágrimas, y un set de tools que te pueden ayudar en tus próximas aventuras"
Keywords:
- sysadmin
- compliance

Tags:
- sysarmy
- sysadmin
- compliance

Thumbnail: assets/cronicas-compliance-0.jpg
socialImage: assets/cronicas-compliance-0.jpg
featuredImage: assets/cronicas-compliance-0.jpg
externalPermlink: "https://medium.com/@jvmbruno-es/cr%C3%B3nicas-de-compliance-c%C3%B3mo-el-sysadmin-dej%C3%B3-la-ansiedad-y-la-preocupaci%C3%B3n-341b60f341ff"

Topics:
- sysarmy
- sysadmin
- compliance

markup: markdown
date: 2023-11-02
draft: false
---

_La publicación original de este post se puede encontrar en [Medium](https://medium.com/@jvmbruno-es/cr%C3%B3nicas-de-compliance-c%C3%B3mo-el-sysadmin-dej%C3%B3-la-ansiedad-y-la-preocupaci%C3%B3n-341b60f341ff)._

La vida del SysAdmin es complicada, solitaria e ingrata. Podría comenzar cualquier articulo con esa frase y todo sysadmin se seguirá identificando.

Cuando comienzas en un lugar nuevo, o un proyecto grande nuevo **siempre** te encontrás con desafíos, un rack con cables que van a Narnia y que nadie se atreve a tocar. “Tal vez si desconecto este cable de red, el microondas del piso 7 deja de andar”. Pero te arremangas y haces lo que nadie antes que vos se animó. Y rearmas ese rack, y lo dejas tan hermoso que esta para sacarle una foto y ponerlo en el living de tu casa. Y cada mañana pasas por ahi y lo miras y tu orgullo se infla. Y crees que eso fue lo peor, que ahora todo va a ser mas fácil. Y al día siguiente te encontras con un mail, de alguien que no es técnico, pidiéndote la implementación de algo que no tiene ningún sentido, pero hey! ya tomaron la decisión y jamás te consultaron si era siquiera posible. Pero después no te quieren cambiar el switch 3Com, que tiene mas cumpleaños que Laura de recepción, porque no hay presupuesto. Si, nos pasó, nos pasa, y nos pasara a todos los Sysadmins.

Si aun no te pasó, pronto te va a llegar un mail, del remitente mas inesperado, tal vez alguien de marketing o de ventas: _“Hey, tenemos que ser Compliance [inserte el nombre del compliance de moda] para fin de mes que mande un presupuesto y el cliente nos pidió, y les dije que si éramos”_.

Nosotros (al menos yo y en el grupo de gente con la que me hablo) somos criaturas técnicas, y muchas veces con poco tiempo en nuestras manos. Así que vamos y leemos la publicación sobre ese Compliance que nos piden, y en un mundo ideal esperamos un “Contraseñas deben tener mínimo 8 caracteres y un símbolo y expirar en 30 días”. Pero en cambio nos encontramos con _“A Memorized Secret authenticator is a secret value intended to be chosen and memorized by the user. Memorized secrets need to be of sufficient complexity and secrecy that it would be impractical for an attacker to guess or otherwise discover the correct secret value._ (Un autenticador de secreto memorizado es un valor secreto destinado a ser elegido y memorizado por el usuario. Los secretos memorizados deben tener una complejidad y secrecía suficientes para que sea impráctico que un atacante adivine o descubra de otra manera el valor secreto correcto).

Lo se, estuve ahi. Hace tiempo vengo trabajando en scripts (mayormente para plataformas Windows) que hacen los chequeos de Compliance (y también hay de seguridad, mejores practicas, etc), y es realmente complejo y sobre todo si no tienes tiempo para usar en eso. Estos Script de Validación (EventSentry validation scripts) son parte del software licenciado EventSentry, pero recientemente junto al Dev team, decidimos ponerlos de libre accesso, a través de la SysAdmin Tools (paquete de herramientas completamente free). Asi que si administras una red windows, y queres una ayuda en la parte de compliance y seguridad, es un buen tiempo de pegarle una mirada a Compliance Validator en las SysAdmin Tools. La puedes correr en desktop o en el server, elegir el tag del compliance, o seleccionar todo y ver que tan mal estas. Si te resulta de mucho valor, la misma funcionabilidad (junto a miles de otras) esta embebida en EventSentry. Les dejo algunas capturas de pantalla:

Se pueden seleccionar una, varias, o todos los Tags, dependiendo que clase de chequeos querríamos correr:

| ![](assets/cronicas-compliance-1.webp) |
| :------------------------------------: |
| Selección de Tags.                     |

La ventana de estados nos mostrara los scripts/chequeos que fueron efectuados y si pasaron o no. N/A mayormente informa que ese script/chequeo no aplica al equipo (puede que sea solo para Controladores de Dominio, Sistemas Operativos de Server, etc.). En la ventana al pie nos informa porque no paso. El botón de “More information” nos llevara a una página web donde nos mostrara mas información y como remediar el problema.

| ![](assets/cronicas-compliance-2.webp) |
| :------------------------------------: |
| Ventana de estado.                     |

Como siempre, ¡gracias por tu tiempo en leer este artículo!. Si llegaste hasta aca sin revisar tu teléfono ni distraerte con videos de gatitos, tienes mi respeto.

- SysAdmin Tools: https://www.eventsentry.com/sysadmintools
- EventSentry Validation Scripts: https://www.eventsentry.com/validationscripts
- EventSentry: https://www.eventsentry.com

> Autoría de [Javier V M Bruno](https://medium.com/@jvmbruno-es), publicado originalmente en [Medium](https://medium.com/@jvmbruno-es/cr%C3%B3nicas-de-compliance-c%C3%B3mo-el-sysadmin-dej%C3%B3-la-ansiedad-y-la-preocupaci%C3%B3n-341b60f341ff).
