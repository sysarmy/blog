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
Slug: multiples-vulnerabilidades-en-openssl-esto-es-lo-que-hay-que-hacer
Tags:
- sysarmy
Thumbnail: /blog/assets/drown-1.png
Title: Múltiples Vulnerabilidades en OpenSSL – Esto es lo que hay que hacer
Topics:
- Development
- Leadership
- Systems
Url: 2016/03/17/multiples-vulnerabilidades-en-openssl-esto-es-lo-que-hay-que-hacer
date: 2016-03-17
---

<p><em>Post original escrito por <a href="https://twitter.com/johannorrman">Johan Norrman</a> de <a href="https://detectify.com/">Detectify</a> para <strong>sysarmy</strong>.</em></p>
<p>&nbsp;</p>
<p class="western"><span style="color:#000000;"><span style="font-family:Arial, serif;"><span lang="en-US">Marzo podría haber empezado mejor para el equipo de OpenSSL. Durante la última semana, el equipo de desarrollo de OpenSSL publicó dos CVEs de alto impacto, </span></span></span><span style="color:#0000ff;"><u><a href="https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2016-0800"><span style="color:#000000;"><span style="font-family:Arial, serif;"><span lang="en-US">CVE-2016-0800</span></span></span></a></u></span><span style="color:#000000;"><span style="font-family:Arial, serif;"><span lang="en-US"> y </span></span></span><span style="color:#0000ff;"><u><a href="https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2016-0703"><span style="color:#000000;"><span style="font-family:Arial, serif;"><span lang="en-US">CVE-2016-0703</span></span></span></a></u></span><span style="color:#000000;"><span style="font-family:Arial, serif;"><span lang="en-US">. En este post, explicamos cómo las CVEs pueden comprometer tu seguridad y qué pasos podés tomar para asegurarte.</span></span></span></p>
<p class="western"><span style="color:#000000;"><span style="font-family:Arial, serif;"><span style="font-size:medium;"><span lang="en-US"><b>CVE-2016-0800 (DROWN) </b></span></span></span></span></p>
<p class="western"><span style="color:#000000;"><span style="font-family:Arial, serif;"><span lang="en-US">Probablemente hayas escuchado hablar acerca de CVE-2016-0800 por su nick, "DROWN". Según </span></span></span><span style="color:#0000ff;"><u><a href="https://drownattack.com/"><span style="color:#1155cc;"><span style="font-family:Arial, serif;"><span lang="en-US">drownattack.com</span></span></span></a></u></span><span style="color:#000000;"><span style="font-family:Arial, serif;"><span lang="en-US"> un servidor es vulnerable a DROWN si utiliza conexiones SSLv2 o si su llave privada se comparte con cualquier otro servidor que permita SSLv2 (ver CVE-2016-0703 abajo).</span></span></span></p>
<p class="western"><span style="color:#000000;"><span style="font-family:Arial, serif;"><span lang="en-US"><b>Qué puede pasar: </b></span></span></span><span style="color:#000000;"><span style="font-family:Arial, serif;"><span lang="en-US">al acceder a un servidor vulnerable a DROWN, el atacante puede obtener información como ser usuarios, contraseñas, números de tarjetas de crédito o cualquier otra información sensible enviada por medio del servidor</span></span></span><span style="color:#000000;"><span style="font-family:Arial, serif;"><span lang="en-US">.</span></span></span></p>
<p class="western"><span style="color:#000000;"><span style="font-family:Arial, serif;"><span lang="en-US"><b>Qué tengo que hacer:</b></span></span></span></p>
<ul>
<li>
<p class="western"><span style="color:#000000;"><span style="font-family:Arial, serif;"><span lang="en-US">Asegurarte de actualizar OpenSSL a la versión recomendada.</span></span></span></p>
<ul>
<li>
<p class="western"><span style="color:#000000;"><span style="font-family:Arial, serif;"><span lang="en-US">Si usás 1.0.1 actualizá a 1.0.1s</span></span></span></p>
</li>
<li>
<p class="western"><span style="color:#000000;"><span style="font-family:Arial, serif;"><span lang="en-US">Si usás 1.0.2 actualizá a 1.0.2g</span></span></span></p>
</li>
</ul>
</li>
<li>
<p class="western"><span style="color:#000000;"><span style="font-family:Arial, serif;"><span lang="en-US">Deshabilitar SSLv2 – cómo hacer esto varía dependiendo del software que se esté usando.</span></span></span></p>
</li>
</ul>
<p class="western"><span style="color:#000000;"><span style="font-family:Arial, serif;"><span lang="en-US">Si no estás seguro respecto de ser vulnerable o no, podés usar servicios como </span></span></span><span style="color:#0000ff;"><u><a href="http://www.detectify.com/"><span style="color:#1155cc;"><span style="font-family:Arial, serif;"><span lang="en-US">Detectify</span></span></span></a></u></span><span style="color:#000000;"><span style="font-family:Arial, serif;"><span lang="en-US">, que muestran un aviso si aún estás utilizando SSLv2 al realizar un scan (ver foto).</span></span></span></p>
<p><a href="assets/detectify1.png" rel="attachment wp-att-430"><img class="alignnone wp-image-430 size-large" src="assets/detectify1.png" alt="" width="720" height="329" /></a></p>
<p class="western"><span style="color:#000000;"><span style="font-family:Arial, serif;"><span lang="en-US"><b>Aprendé más sobre DROWN:  </b></span></span></span></p>
<p class="western"><span style="color:#000000;"><span style="font-family:Arial, serif;"><span lang="en-US">Si querés saber más sobre OpenSSL y DROWN, te recomendamos </span></span></span><span style="color:#0000ff;"><u><a href="https://www.openssl.org/blog/blog/2016/03/01/an-openssl-users-guide-to-drown/"><span style="color:#1155cc;"><span style="font-family:Arial, serif;"><span lang="en-US">este post</span></span></span></a></u></span><span style="color:#000000;"><span style="font-family:Arial, serif;"><span lang="en-US"> de parte del equipo de OpenSSL.</span></span></span></p>
<p class="western"><span style="color:#000000;"><span style="font-family:Arial, serif;"><span style="font-size:medium;"><span lang="en-US"><b>CVE-2016-0703 </b></span></span></span></span></p>
<p class="western"><span style="color:#000000;"><span style="font-family:Arial, serif;"><span lang="en-US">El segundo problema, CVE-2016-0703, sólo afecta las versiones de OpenSSL anteriores al 19 de marzo de 2015, y se soluciona en OpenSSL 0.9.8zf, 1.0.0r, 1.0.1m y 1.0.2a. </span></span></span></p>
<p class="western"><span style="color:#000000;"><span style="font-family:Arial, serif;"><span lang="en-US"><b>Qué puede pasar:</b></span></span></span><span style="color:#000000;"><span style="font-family:Arial, serif;"><span lang="en-US"> permite que un atacante remoto realice un ataque de recuperación de llave del tipo divide-y-vencerás (divide-and-conquer key recovery attack). Espiando el handshake de SSLv2 el atacante puede determinar la llave privada de SSLv2, en consecuencia derivando en una versión mucho más eficiente de DROWN.</span></span></span></p>
<p class="western"><span style="color:#000000;"><span style="font-family:Arial, serif;"><span lang="en-US"><b>Qué tengo que hacer:</b></span></span></span></p>
<ul>
<li>
<p class="western"><span style="color:#000000;"><span style="font-family:Arial, serif;"><span lang="en-US">Asegurarte de actualizar a OpenSSL 0.9.8zf, 1.0.0r, 1.0.1m y 1.0.2a, dependiendo de la versión que uses ahora.</span></span></span></p>
</li>
<li>
<p class="western"><span style="color:#000000;"><span style="font-family:Arial, serif;"><span lang="en-US">Leer la información de seguridad de tu proveedor de software para determinar si hay alguna acción extra necesaria para estar asegurado.</span></span></span></p>
</li>
</ul>
<p class="western"><span style="color:#000000;"><span style="font-family:Arial, serif;"><span lang="en-US"><b>Comentarios de Detectify: </b></span></span></span></p>
<p class="western"><span style="color:#000000;"><span style="font-family:Arial, serif;"><span lang="en-US">"Mantener tu infraestructura actualizada se vuelve más y más fácil a medida que más empresas migran a una cultura DevOps. Los responsables de parchar y mantener los entornos de producción actualizados son ahora parte de tu equipo de desarrollo y no son sólo responsables de asegurarse que los servidores están funcionando. Sin embargo, parchar tus servidores de producción siempre será un desafío, y mantenerlos al día debería ser siempre la prioridad” dice el CIO de Detectify, Johan Norman.</span></span></span></p>
<p class="western">
