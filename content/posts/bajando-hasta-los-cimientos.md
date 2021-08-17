---
title: "Bajando Hasta Los Cimientos De Las Computadoras Y Los Programas"
date: 2021-08-17
draft: false
description: "¿Cómo es que funciona este programa? ¿Qué hace por dentro el CPU para ejecutarlo?  ¿Cómo hace la compu para entender el código que escribí? ¿Cómo viaja mi push hasta GitHub?"

keywords:
    - sysarmy
    - sistemas
    - desarrollo
    - developer
    - administración de sistemas
    - binario
    - técnicas digitales
tags:
    - sysarmy
    - sistemas
    - desarrollo
    - developer
    - administración de sistemas
    - binario
    - técnicas digitales
topics:
    - sistemas

thumbnail: assets/bajando-hasta-los-cimientos3.png
socialImage: assets/bajando-hasta-los-cimientos3.png
featuredImage: assets/bajando-hasta-los-cimientos3.png
---
En esta oportunidad estoy escribiendo para aquellos que están llegando a este Mundo IT y quizás se preguntan ¿cómo es que funciona este programa? ¿Qué hace por dentro el CPU para ejecutarlo?
O quizás ya estas laburando y te seguís preguntando ¿cómo hace la compu para entender el código que escribí? ¿Cómo viaja mi push hasta GitHub?

La realidad que hay muchísimas cosas para explicar pero quiero bajar hasta los mismísimos cimientos, a la base de todo, porque es la mejor forma de arrancar a entender…

Estoy seguro que escuchaste alguna vez que “adentro de la computadora son todos CEROS y UNOS” o “los códigos de los programas son transformados en 0s y 1s para que la compu los pueda entender y ejecutar” o algo mas avanzado “por la red van 0s y 1s de una PC a otra”.

Es verdad, el sistema binario, el que usa solo dos símbolos: el 0 y el 1, documentado por Leibniz en el siglo XVIII y luego desarrollado por George Boole a mediados del 1800 no fue pensado para las computadoras, ni existian en sus sueños, sin embargo fue el elegido para poder representar, manejar, moldear, controlar y usar la información, los datos y las computadoras.

Pero voy a bajar un escalón mas, porque los 0s y 1s en realidad son una representación que los humanos tuvimos que adoptar para poder entender y usar las leyes de la física, puntualmente la ELECTRICIDAD, a donde quería llegar.

Cada carácter, número, dato, pixel de una imagen, tooodo en una computadora es una **señal eléctrica**, pero medir y controlar esas señales con alta precisión era muy difícil en un principio. 

![](assets/bajando-hasta-los-cimientos0.jpg)
Todo comenzó con los avances de Tesla y Edison para poder generar y controlar la electricidad en la década de 1880 (for the record: Soy Team Tesla). El querer hacer que la electricidad pueda utilizarse para crear máquinas que puedan facilitarnos la vida derivo en los inventos de Fleming (diodo) y De Forest (triodo) a inicios del 1900 que originaron la Electrónica (parte de la física que estudia los cambios y los movimientos de los electrones libres y la acción de las fuerzas electromagnéticas y los utiliza en aparatos que reciben y transmiten información.)

Para seguir simplificando la historia, en un momento se hizo necesario poder representar los estados eléctricos para poder controlar y poder utilizar y dar significado a las señales eléctricas. Hay electricidad / no hay electricidad, that is the question. Entonces tenemos un estado encendido (representado por una carga negativa), y el estado apagado (representado por una carga positiva). ¿Por qué de esta manera?, pues una carga negativa tiene más electrones, por lo que tiene mayor corriente y es utilizado para el estado encendido o alto voltaje.
Todos los sistemas electrónicos digitales funcionan bajo el principio del código binario. Existen dos posibles estados llamados: verdadero-falso, alto-bajo ó 1-0. Aunque la electricidad no es tan binaria, en realidad electricidad hay siempre pero varia su voltaje por lo que estos dos estados son representaciones abstractas de regiones de voltajes específicos. Por ejemplo, para un circuito integrado que opera a 5VDC, un 0 representa un voltaje entre -0.5V y 2.5V. Mientras que el 1 representa valores entre 3.5 y 5.5V.

![](assets/bajando-hasta-los-cimientos2.jpg)

El código binario permite entender y diseñar sistemas electrónicos digitales. Su sistema de numeración es de vital importancia para la electrónica y por ende para la informática, así se crearon los primeros equipos electrónicos que combinaban entradas eléctricas para dar significados y realizar algún proceso como respuesta.

Estas combinaciones se logran a partir del uso de las compuertas lógicas que utilizan el código binario para poder representar valores en sus entradas y proporcionar resultados. El funcionamiento de las compuertas depende de que tipo es la que se esta utilizando, ya que cada una reacciona de manera diferente, pero en términos generales, se encargan de verificar el estado lógico de cada una de sus entradas, y las comparan para poder arrojar un resultado.

![](assets/bajando-hasta-los-cimientos1.jpg)

A su vez los datos son representados por diferentes códigos que utilizando combinaciones de 0s y 1s pueden diferenciar símbolos, estructuras, operaciones, etc. Por ejemplo en el código ASCII el 01000001 representa la “A” y en parte es lo que transmite tu teclado por el cable al presionar esa tecla transformándola a impulsos eléctricos.

De esta forma también hay códigos en binario para transmitir desde tu celular la imagen que vas a postear en IG, viajando en pulsos eléctricos transformados en ondas electromagnéticas que llegan hasta el router Wi-Fi de tu casa para convertirse en pulsos de luz y ser enviados por fibra óptica hasta el router de tu empresa proveedora de Internet que se encargara de enviarla hasta el server de IG utilizando diferentes medios.

Ahora si, ya sabes que no son 0s y 1s corriendo de un lado para el otro de la computadora, es la electricidad lo que hace que la **Matrix** funcione, por eso seremos baterías…

![](assets/bajando-hasta-los-cimientos3.png)



