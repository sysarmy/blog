---
title: "La propagación del DNS no existe"
keywords:
    - dns
tags:
    - dns
topics:
    - dns
thumbnail: assets/la-propagacion-de-dns-no-existe.png
socialImage: assets/la-propagacion-de-dns-no-existe.png
featuredImage: assets/la-propagacion-de-dns-no-existe.png
externalPermlink: "https://www.nslookup.io/blog/dns-propagation-does-not-exist/"
date: 2021-04-19
markup: Markdown
draft: false
---
La propagación del DNS no existe

Una falacia muy extendida entre los profesionales de la informática es que el [DNS](https://es.wikipedia.org/wiki/Sistema_de_nombres_de_dominio) se propaga por alguna red. Tan extendida, de hecho, que hay un par de sitios dedicados a visualizar la propagación geográfica de los registros DNS. Pero la propagación del DNS no existe.

<!--more-->

Un {{< canonical href="https://www.nslookup.io/blog/dns-propagation-does-not-exist/" text="artículo" >}} de [Ruurtjan Pul](https://twitter.com/Ruurtjan)

# Entonces, ¿cómo funciona?

Cuando se solicitan registros DNS al servidor que es autoritativo para ese dominio (es decir, a quien le "pertenece"), éste acompañará esos registros con un TTL (time to live, tiempo de vida). Esto indica cuánto tiempo puede seguir utilizando esos valores antes de que deba solicitar una nueva copia. Los registros se almacenan en una caché en tu dispositivo. Eliminar la necesidad de consultar el servidor DNS cada vez acelera las cosas y descarga los servidores DNS.

Muchos proveedores de servicios de Internet proporcionan servidores de caché de DNS a sus abonados. También hay algunos servidores DNS públicos, ofrecidos por [Google](https://developers.google.com/speed/public-dns), [Cloudflare](https://www.cloudflare.com/es-es/learning/dns/what-is-1.1.1.1/) y otros. Todos ellos se denominan servidores DNS recursivos/resolutivos. Pueden proporcionarle una respuesta consultando al servidor DNS autoritativo. Estos servidores recursivos utilizan el TTL para almacenar en caché los registros en su lado. Así que *hay varias capas de caché*: en estos servidores y en tu dispositivo.

Por supuesto, es posible que los registros hayan sido modificados, y que obtengas una versión antigua de los registros que todavía estaba en la caché. Se dice que estos registros son obsoletos. Por lo tanto, cuando esto ocurre, no se debe a que los registros no se hayan propagado todavía, sino a que la caché está obsoleta.

La obsolescencia depende de los tiempos incidentales de las solicitudes anteriores, y no están correlacionados con la geolocalización de un servidor DNS o su lugar en alguna red física o lógica.

Otra forma de verlo es que los registros no se empujan (se propagan), sino que se extraen (se consultan y se almacenan en la caché).

# Un cambio sugerido en la terminología

Entonces, puede que "propagación del DNS" no sea la mejor elección de palabras. Pero, ¿por qué es importante?

Bueno, las palabras provocan asociaciones y dan forma a la manera en que pensamos sobre algo. Así que la terminología que utilizamos es importante desde una perspectiva pedagógica. Cuando se dice que algo se propaga, alguien que no ha aprendido cómo funciona el DNS asumirá que de alguna manera se propaga a través de una red. Y todos los que sí saben cómo funciona tuvieron que aprenderlo en algún momento. Será más fácil aprenderlo si utilizamos palabras que provoquen las asociaciones adecuadas.

Así que eliminemos esta falacia y hablemos de expiración de la caché en lugar de propagación.

![Meme Ohlala señor francés](assets/la-propagacion-de-dns-no-existe-meme.jpg)

* Traducción, revisión y publicación colaborativa de @jedux y [Daniel-DZ](https://github.com/Daniel-DZ).

