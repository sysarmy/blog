---
Description: "Entendiendo la fork() Bomb :(){ :|:& };: de bash "
Keywords:
- bash
- forkbomb
Section: 
Tags:
- bash
- forkbomb
Thumbnail: assets/entendiendo-la-fork-bomb-de-bash.jpeg
socialImage: assets/entendiendo-la-fork-bomb-de-bash.jpeg
featuredImage: assets/entendiendo-la-fork-bomb-de-bash.jpeg
Title: "Entendiendo la fork() Bomb :(){ :|:& };: de bash"
Topics:
- bash
- forkbomb
markup: markdown
date: 2021-04-05
draft: false
---
Una fork bomb (bomba fork) es una forma de ataque del tipo _denial-of-service_ (DoS) o [denegación de servicio](https://es.wikipedia.org/wiki/Ataque_de_denegaci%C3%B3n_de_servicio), utilizada contra sistemas basados en Unix. Como su nombre lo indica, utiliza la operación **[fork](https://en.wikipedia.org/wiki/Fork_(system_call))**, donde un proceso crea una copia de sí mismo. 

La conocida cadena ``` :(){ :|:& };: ``` no es nada más que una función de bash, la cual se ejecuta recursivamente. Comúnmente, es utilizada por sysadmins para testear limitaciones sobre usuarios en cuanto a cantidad de procesos que pueden ejecutar en un servidor. 

En linux, dichos límites de procesos pueden ser configurados desde ``` /etc/security/limits.conf ``` o vía el módulo pam_limits de [Linux-PAM](https://wiki.archlinux.org/index.php/PAM_(Espa%C3%B1ol)) desde ``` /etc/security/limits.d ``` y así poder evitar esta forma de ataque. Una vez activada la bomba de forma exitosa en el sistema, puede no ser posible retornar a un estado de operación normal sin tener que realizar un reboot forzado, ya que la única solución a una fork bomb es destruir todas las instancias de la misma.

<!--more-->

> **WARNING**: Los siguientes ejemplos pueden crashear tu sistema.

##  Analizando el código de la fork() Bomb ``` :(){ :|:& };: ```

`:()` - Define una función con nombre `:`. Es una función que no acepta argumentos. La sintáxis de una función en Bash tiene la siguiente forma:


```bash
foo(){
    arg1=$1
    arg2=$2
    echo 'Bar...'
    #do_something on $arg argument
}
```

La `fork()` bomb se define de la siguiente manera:

```bash
 :(){
     :|:&
 };:
```

`:|:` - La función se llama a sí misma ([recursión](/blog/posts/entendiendo-la-fork-bomb-de-bash/)) y redirecciona el output o salida, utilizando el operador pipe `|`, a otra llamada de la de la misma funcion `:`. La magia está en que se llama dos veces a la función y así comienza el bombardeo al sistema.

`&` - Pone el llamado de la función en background de manera que los procesos hijos (copias) no mueran y así se comen los recursos del sistema.  

`;` - Finalización de la definición de la función

`:` - Llamado (call) de la función, AKA setteo de la bomba.

De manera un poco más legible, la función se puede definir de la siguiente manera:

```bash
bomb() {
    bomb | bomb &
}; bomb
```

Un sistema Unix correctamente configurado no debería caerse cuando se dispara una fork bomb. 

## Previniendo una fork bomb en Linux

Una posible forma de prevenir el ataque es limitando el numero de procesos que pueden correr los usuarios. La información de la cantidad máxima actual se puede obtener ejecutando el siguiente comando:

```
ulimit -u
```

Otra forma:

``` 
ulimit -a
```

![Ejecución comando ulimit -a](assets/fork-bomb-ulimit-a.png)

 El número 50922 indica que el usuario puede correr 50922 procesos. Para proteger el sistema de una fork bomb, es necesario disminuir dicho valor. Para limitar la sesión a, por ejemplo, 5000 procesos, se utiliza el siguiente comando:

```
ulimit -S -u 5000
```

> **WARNING**: No utilices valores de ulimit muy bajos! Esto puede ocasionar problemas a la hora de trabajar con el sistema. 

Ahora, al correr la fork bomb:

```bash
:(){ :|:& };:
```

Se obtendrá el siguiente output:

```bash
bash: fork: Resource temporarily unavailable
bash: fork: Resource temporarily unavailable
bash: fork: Resource temporarily unavailable
bash: fork: Resource temporarily unavailable
bash: fork: Resource temporarily unavailable
bash: fork: Resource temporarily unavailable
bash: fork: Resource temporarily unavailable
```

De esta forma, estaríamos evitando este tipo de ataques. Se puede ver además, corriendo el comando pgrep, la cantidad límite (actual) the threads:

```bash
pgrep -wcu $USER
```

Salida de ejemplo:

```bash
5002
```

Ahora podes comprar [la remera forkbomb en la tienda de sysarmy](https://tienda.sysarmy.com/productos/fork/?variant=107398458) o el [sticker pack con la forkbomb](https://tienda.sysarmy.com/productos/sysarmy-sticker-pack-0/) y explicarle a todos que significa!

Artículo original en [cybercity.biz](https://www.cyberciti.biz/faq/understanding-bash-fork-bomb/), traducción al español [efsbl](https://github.com/efsbl), revisó @jedux.
