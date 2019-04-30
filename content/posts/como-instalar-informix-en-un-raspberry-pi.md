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
Slug: como-instalar-informix-en-un-raspberry-pi
Tags:
- sysarmy
Title: Como instalar Informix en un Raspberry PI
Topics:
- Development
- Leadership
- Systems
Url: 2015/09/07/como-instalar-informix-en-un-raspberry-pi
date: 2015-09-07
---

<p>Ésta es una receta para instalar Informix Dynamic Server Developer Edition en una RaspberryPi utilizando raw devices (Como somos sysadmines, queremos raw devices).</p>
<p>Se me ocurrió realizar esta guía dado que Informix es un excelente motor de base de datos y poco conocido o que goza de la reputación de “misterioso”, entonces, para aprender Informix, que mejor que una RaspberryPi, un poco de tiempo y las ganas de aprender algo nuevo !</p>
<p>Prerequisitos:</p>
<ul>
<li>RaspberryPi modelo B</li>
<li>Por lo menos una SD para el sistema operativo de la RaspberryPi y un pendrive de ocho gigas para los raw devices. Recomendable: una SD para el booteo, un pendrive para el sistema operativo y otro pendrive para la base de datos. Esta última configuración es la que vamos a usar en este tutorial.</li>
<li>Como sistema operativo se utiliza raspbian con los paquetes libaio1 y lvm2 instalados a mano, ya que no vienen instalados por defecto.</li>
<li>El Informix propiamente dicho, <strong>Informix Developer Edition for Linux ARM v6 32 (Raspberry PI) Version 10UC4DE</strong>, (es un tar llamado ids.12.10.UC4DE.Linux-ARM6.tar) desde <strong><a href="https://www-01.ibm.com/marketing/iwm/iwm/web/reg/pick.do?source=ifxids&amp;lang=en_US" target="_blank">el sitio de IBM</a></strong> . Hay que registrarse como usuario para obtener el IbmId, son sólo 5 minutos.</li>
</ul>
<p><strong>Instalación</strong></p>
<p>Parto de la base que tenes la raspi instalada con raspbian, funcionando, y con acceso de root. Antes que nada hay que instalar dos paquetes que no vienen instalados por defecto: <strong>libaio1</strong> y <strong>lvm2</strong>.</p>
<p><em>Consideraciones: En mi raspi tengo dos pendrive y una SD, como les había contado antes. Así que, seguramente el nombre del dispositivo asociado al pendrive va a ser distinto (se puede copiar, reemplazar y pegar también)</em></p>
<p><strong><em>Como root:</em></strong></p>
<pre>apt-get install libaio1
apt-get install lvm2</pre>
<p>Una vez agregados los paquetes: vamos a crear el grupo y usuario Informix.</p>
<pre>addgroup informix
adduser --ingroup informix Informix</pre>
<p>Vamos a preparar el almacenamiento para la base de datos (los famosos raw devices):</p>
<p>Primero, vamos a determinar cuál es nuestro pendrive, que vamos a utilizar para nuestra base creándole los raw devices:</p>
<p>Ejecutamos dmesg para ver nuestro pendrive</p>
<pre><em>[ 4.766035] scsi 1:0:0:0: Direct-Access Kingston DataTraveler 2.0 1.00 PQ: 0 ANSI: 4</em>
<em>[ 4.780904] sd 1:0:0:0: [sdb] 15148608 512-byte logical blocks: (7.75 GB/7.22 GiB)</em>
<em>[ 4.794613] sd 1:0:0:0: [sdb] Write Protect is off</em>
<em>[ 4.840400] sd 1:0:0:0: [sdb] Attached SCSI removable disk</em>
</pre>
<p>Ya sabemos que es <em><strong>sdb</strong></em>. Entonces procedamos a armar los raw devices.</p>
<p>Antes que nada, el proceso en sí mismo, conceptualmente es: generar logical volumes sobre el pendrive y despues, sobre cada uno de los lv's generar un raw device.</p>
<p>Creamos los logical volume</p>
<pre>root@raspberrypi:~# <strong>pvcreate /dev/sdb</strong>
Writing physical volume data to disk "/dev/sdb"
Physical volume "/dev/sdb" successfully created
root@raspberrypi:~# <strong>vgcreate vginformix /dev/sdb</strong>
Volume group "vginformix" successfully created
root@raspberrypi:~# <strong>lvcreate -n lvrootdbs -L +500M vginformix</strong>
Logical volume "lvrootdbs" created
root@raspberrypi:~# <strong>lvcreate -n lvdatadbs00 -L +2G vginformix</strong>
Logical volume "lvdatadbs00" created
root@raspberrypi:~#<strong> lvcreate -n lvdatadbs01 -L +2G vginformix</strong>
Logical volume "lvdatadbs01" created
root@raspberrypi:~# <strong>lvcreate -n lvtempdbs00 -L +500M vginformix</strong>
Logical volume "lvtempdbs00" created
root@raspberrypi:~# <strong>lvcreate -n lvlogsdbs -L +500M vginformix</strong>
Logical volume "lvlogsdbs" created
</pre>
<p><em>Chequeamos que hayan sido creados bien.</em></p>
<pre>root@raspberrypi:~# <strong>lvs</strong>
LV          VG         Attr     LSize   Pool Origin Data%  Move Log Copy%  Convert
lvdatadbs00 vginformix -wi-a---   2.00g
lvdatadbs01 vginformix -wi-a---   2.00g
lvlogsdbs   vginformix -wi-a--- 500.00m
lvrootdbs   vginformix -wi-ao-- 500.00m
lvtempdbs00 vginformix -wi-a--- 500.00m
</pre>
<p><em>Generamos los raw devices</em>.</p>
<pre>root@raspberrypi:~# <strong>raw /dev/raw/raw1 /dev/vginformix/lvrootdbs</strong>
root@raspberrypi:~# /dev/raw/raw1:  bound to major 254, minor 0
root@raspberrypi:~# <strong>raw /dev/raw/raw2 /dev/vginformix/lvdatadbs00</strong>
root@raspberrypi:~# /dev/raw/raw2:  bound to major 254, minor 1
root@raspberrypi:~# <strong>raw /dev/raw/raw3 /dev/vginformix/lvdatadbs01</strong>
root@raspberrypi:~# /dev/raw/raw3:  bound to major 254, minor 2
root@raspberrypi:~# <strong>raw /dev/raw/raw4 /dev/vginformix/lvtempdbs00</strong>
root@raspberrypi:~# /dev/raw/raw4:  bound to major 254, minor 3
root@raspberrypi:~# <strong>raw /dev/raw/raw5 /dev/vginformix/lvlogsdbs</strong>
root@raspberrypi:~# /dev/raw/raw5:  bound to major 254, minor 4
</pre>
<p>Una vez generados los raw devices, tenemos que cambiarles el propietario y los permisos de acceso, y luego verificamos que haya quedado todo bien. (es muy importante tomar nota del nombre de los raw)</p>
<pre>root@raspberrypi:~# <strong>chown informix.informix /dev/raw/raw[0-9]</strong>
root@raspberrypi:~# <strong>chmod 660 /dev/raw/raw[0-9]</strong>
root@raspberrypi:~# <strong>ls -la /dev/raw</strong>

total 0
drwxr-xr-x  2 root     root        160 Jun 20 12:43 .
drwxr-xr-x 14 root     root       3380 Jun 20 12:41 ..
crw-rw----  1 informix informix 162, 1 Jun 20 12:38 raw1
crw-rw----  1 informix informix 162, 2 Jun 20 00:31 raw2
crw-rw----  1 informix informix 162, 3 Jun 20 00:31 raw3
crw-rw----  1 informix informix 162, 4 Jun 20 00:32 raw4
crw-rw----  1 informix informix 162, 5 Jun 20 12:43 raw5
crw-------  1 root     root     162, 0 Dec 31  1969 rawctl
</pre>
<p>Ahora viene la parte de instalación del motor de base de datos.</p>
<p>Antes que nada, es conveniente mover y descomprimir el archivo de instalación de Informix en un directorio temporal.</p>
<pre><strong>mv ids.12.10.UC4DE.Linux-ARM6.tar /tmp</strong>
<strong>cd /tmp</strong>
<strong>tar xvf ids.12.10.UC4DE.Linux-ARM6.tar</strong>
</pre>
<p>Vamos a encontrar el archivo <strong>ids_install</strong>. Ese archivo es el ejecutable de nuestro asistente de instalación.</p>
<pre>root@raspberrypi:/tmp# ls -la
total 910192
drwxrwxrwt  6 root root        4096 Jun 20 00:32 .
drwxr-xr-x 22 root root        4096 May 29 23:59 ..
drwxr-xr-x  2 root daemon      4096 Dec 17  2014 doc
drwxrwxrwt  2 root root        4096 Jun 19 22:17 .ICE-unix
-rw-r--r--  1 root root   466042880 Jan  5 16:17 ids.12.10.UC4DE.Linux-ARM6.tar
-rwx------  1 root root   465965056 Dec 18  2014 ids_install
drwx------  2 root root        4096 Jun 20 00:12 mc-root
drwxrwxrwt  2 root root        4096 Jun 19 22:17 .X11-unix
</pre>
<p>Lo ejecutamos:</p>
<pre>root@raspberrypi:/tmp# <strong>./ids_install</strong>
</pre>
<p>Nos aparecerá la siguiente pantalla:</p>
<pre>============================================
Bundle Software
============================================
*
* Texto de la licencia
* 
	1. Accept the license, 2. Decline the License, 3. Continue Reading.
</pre>
<p>Aparecen los terminos de la licencia.</p>
<ul>
<li><strong>Y la aceptamos, presionando 1</strong></li>
</ul>
<p>Después nos aparece la pantalla de presentación de software a instalar, las opciones por defecto son las que nos sirven.</p>
<pre>============================================
Informix Software Bundle
============================================
Select the Products to Install:

[X] 1. 'Informix_Dynamic_Server'.
[X] 2. 'Informix_JDBC'.
[X] 3. 'Informix_ClientSDK'.
[ ] 4. 'Informix_Connect'.

============================================
</pre>
<blockquote><p><strong>Informix Dynamic Server</strong> es el servidor propiamente dicho.<br />
<strong>Informix JDBC</strong> son los drivers de Informix para Java<br />
<strong>Informix ClientSDK</strong> es el sdk para programar aplicaciones cliente usando librerias de funciones nativas.</p></blockquote>
<p><strong>Apretamos ENTER para aceptar las opciones por defecto.</strong></p>
<pre>============================================
Informix Software Bundle
============================================
*
*
*
Specify a directory where to install the products:
ENTER to proceed:<strong>/opt/IBM/informix</strong>
</pre>
<p><em>En este punto, vamos a especificar el directorio de instalación a <strong>/opt/IBM/informix</strong> apretamos 1 para aceptar la licencia de IDS</em></p>
<p>Esperar un rato largo, servirse un café, una gaseosa, o lo que guste, mientras se instala el motor de base de datos.</p>
<p>Después aparece la instalación del SDK</p>
<pre>============================================
Informix_ClientSDK
============================================
*
* Texto de la licencia
* 
	1. Accept the license, 2. Decline the License, 3. Continue Reading.
</pre>
<p>Cuando llegue el momento de instalar el SDK, <strong>volver a apretar 1 para aceptar la licencia</strong></p>
<p>Por último aparece ésta pantalla:</p>
<pre>============================================
Informix_ClientSDK
============================================
*
*
* 
	Installation was successful.
============================================

<em><strong>root@raspberrypi:/tmp#</strong></em>
</pre>
<p>En la próxima entrega, les voy contar como configurar el motor de base de datos, crear la primera base y hacer nuestra primera consulta.</p>
<p>Saludos, y hasta la próxima</p>
