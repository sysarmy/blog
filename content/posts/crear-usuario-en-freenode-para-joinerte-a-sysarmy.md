---
Description: "Crear una cuenta y Joinearse a sysarmy"
Keywords:
- sysadmin 
- sistemas
- join sysarmy
- sysarmy chat
- chat
- freenode
Section: 
Tags:
- sysarmy
- join
Thumbnail: https://i.etsystatic.com/15770998/r/il/3fe54c/1314770713/il_794xN.1314770713_n3sd.jpg
socialImage: https://i.etsystatic.com/15770998/r/il/3fe54c/1314770713/il_794xN.1314770713_n3sd.jpg
featuredImage: https://i.etsystatic.com/15770998/r/il/3fe54c/1314770713/il_794xN.1314770713_n3sd.jpg
Title: How to Join sysarmy 
Topics:
- sysarmy
- join
- chat
markup: markdown
date: 2020-04-10
---

# Qué?

Simple, vamos a explicar como unirse al chat de sysarmy creando un usuario dentro de freenode con el cliente XChat en Ubuntu.

<!--more-->

## A la consola

Primero, a descargar el Xchat. 

```bash
sudo apt-get install -y xchat
```

Después, abrimos el [XChat](http://xchat.org/) e ingresan lo que le pide según su situación procesal:

* Información de Usuario:
  - **Apodo**: Su handler, nickname o como quieren aparecer
  - **Segunda opción**: Si eso llega a estar tomado, como queren aparecer
  - **Tercera opción**: Ok, si estás en este punto es porque tenés mucha mala suerte. 
  - **Nombre se usuario**: Tu username. Es diferente del handler. O sea, no es lo mismo. Me refiero, tu apodo lo podés cambiar, el nombre de usuario no. Si, no es como el tatuaje de tu pareja que te hiciste que lo tenés que ir tapando.
  - **Nombre Real**: Eeeh.... obvio no?

## Creando el usuario en Freenode

Bueno, acá viene la papota de la papota. Acá está lo interesante que es donde vamos a crear nuestro usuario dentro de los servidores de Freenode.
Si todo fue bien, la consola de la aplicación de chat tendría que decirte algo como:

```
* - Thank you for using freenode!
* End of /MOTD command.
* ipf0rward establece modo +i ipf0rward
```

Bien, para registrar el nickname sería

```
/msg nickserv register [password] [email address]
```

Por lo que en mi caso sería: 

```
/msg nickserv register 1234 ipforward@meleeisland.iwp
```

Y nos responde algo como lo que sigue:

```
-NickServ- An email containing nickname activation instructions has been sent to ipforward@meleeisland.iwp.
-NickServ- If you do not complete registration within one day, your nickname will expire.
-NickServ- ipf0rward is now registered to ipforward@meleeisland.iwp, with the password 1234.
```

Bien, ahora vamos a nuestra cuenta de mail y vamos a ver que Freenode nos envió un mail. En ese mail se encuentra el challenge de Freenode y vamos a tener que ingresar el string que nos piden. En mi caso es algo así 

```
/msg NickServ VERIFY REGISTER ipf0rward y0uD0ntc4re
```

Para confirmar, nos devuelve un mensajito parecido a esto:

```
-NickServ- Thank you for verifying your e-mail address! You have taken steps in ensuring that your registrations are not exploited.
```
## Join #sysarmy

Listo, el resto solo queda unirse a la comunidad e ingresar
```
/msg NickServ identify y0uD0ntc4re
/join #sysarmy
```
Y listo. La próxima vez que te queiras conectar simplemente ingresá a

Enjoy!

Escrito por [ipf0rw4rd twitter](https://twitter.com/ipf0rw4rd)

[Visit my blog :-)](https://blog.ipforward.co)

[Artículo Original](https://blog.ipforward.co/2020/04/09/join_sysarmy/)


