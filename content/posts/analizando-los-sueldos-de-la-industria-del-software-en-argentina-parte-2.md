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
Slug: analizando-los-sueldos-de-la-industria-del-software-en-argentina-parte-2
Tags:
- sysarmy
Thumbnail: /blog/assets/1-p-i0_gpvcdhpg_uokpnayq.png
Title: Analizando los sueldos de la industria del software en Argentina (Parte 2)
Topics:
- Development
- Leadership
- Systems
Url: 2016/09/06/analizando-los-sueldos-de-la-industria-del-software-en-argentina-parte-2
date: 2016-09-06
---

<p class="graf--p">En el <a class="markup--anchor markup--p-anchor" href="2016/08/29/analizando-los-sueldos-de-la-industria-del-software-en-argentina-parte-1/">primer post</a> hicimos un <strong class="markup--strong markup--p-strong">análisis exploratorio</strong> general de los sueldos, en este vamos a realizar una <strong class="markup--strong markup--p-strong">inferencia estadística</strong>. Otra vez, todo el código se encuentra <a class="markup--anchor markup--p-anchor" href="https://github.com/fernandezpablo85/sysarmy-salaries-data-2016" target="_blank">disponible acá</a>.</p>
<h4 class="graf--h4">Hipótesis</h4>
<p class="graf--p">Primero formulamos una hipótesis:</p>
<blockquote class="graf--blockquote"><p>Los salarios varían significativamente según el género</p></blockquote>
<p class="graf--p">Para probar nuestra hipótesis, intentaremos refutar la <a class="markup--anchor markup--p-anchor" href="https://en.wikipedia.org/wiki/Null_hypothesis" target="_blank">hipótesis nula</a>, que simplemente sería lo contrario (los salarios no varían según el género)</p>
<h4 class="graf--h4">Primer problema: los tamaños de las muestras</h4>
<p class="graf--p">Recordemos la distribución de salarios discriminada por género:</p>
<figure class="graf--figure"><img class="graf-image" src="assets/f1817-1n0b5rjw1akpfg95wv6lttg.png" /></figure>
<p class="graf--p">El problema en este caso es la diferencia entre participantes de la encuesta varones y mujeres. Usemos un gráfico de barras para hacerlo más evidente:</p>
<figure class="graf--figure"><img class="graf-image" src="assets/7b162-1p-i0_gpvcdhpg_uokpnayq.png" /></figure>
<p class="graf--p">Hay <strong class="markup--strong markup--p-strong">298 mujeres y 3.631 hombres </strong>en nuestro dataset. Si consideramos a la muestra como representativa de la población, <strong class="markup--strong markup--p-strong">habría aproximadamente una mujer cada 10 hombres</strong>, o un 7.5% del total de trabajadores de software.</p>
<p class="graf--p">Con esta limitación en mente, vamos a tratar de poner a prueba nuestra hipótesis utilizando 3 estrategias alternativas.</p>
<h4 class="graf--h4">Usar muestras de tamaño comparable</h4>
<p class="graf--p">Sería muy bueno tener misma cantidad de mujeres que de hombres. Una alternativa sería salir a encuestar más mujeres. La otra (más fácil) es “recortar” la muestra de varones.</p>
<p class="graf--p">Para esta última tomamos una muestra aleatoria de <strong class="markup--strong markup--p-strong">298 varones</strong> de nuestros datos y comparamos las dos. Vamos a usar una función del histograma de ggplot llamada “dodge” para que no apile las barras sino que las ponga una al lado de la otra:</p>
<figure class="graf--figure"><img class="graf-image" src="assets/dd48a-1j_gwvmsmgm_up4q0xjijwq.png" /></figure>
<p class="graf--p">Si bien parece haber mayor cantidad de mujeres en los deciles más bajos, a simple vista las distribuciones no muestran una diferencia importante que nos sugiera descartar la hipótesis nula.</p>
<h4 class="graf--h4">Comparar las áreas de las distribuciones</h4>
<p class="graf--p">Otra forma de salvar el problema de las cantidades es utilizar <strong class="markup--strong markup--p-strong">un gráfico de densidad de área. </strong>Este tipo de gráfico no compara unidades absolutas sino que estima porcentaje de muestras bajo la curva (para más información, la técnica que usa ggplot para esto se llama <a class="markup--anchor markup--p-anchor" href="https://en.wikipedia.org/wiki/Kernel_density_estimation" target="_blank">Kernel Density Estimation o KDE</a>).</p>
<p class="graf--p">Probemos la técnica generando una distribución normal aleatoria, usando la función <a class="markup--anchor markup--p-anchor" href="https://stat.ethz.ch/R-manual/R-devel/library/stats/html/Normal.html" target="_blank">rnorm</a>:</p>
<figure class="graf--figure"><img class="graf-image" src="assets/5f21b-16uwyu7tt-xdorx6vrsccig.png" /></figure>
<p class="graf--p">Vemos una campana de Gauss casi perfecta, en este caso con una media de 5 y una desviación estándar de 2. Nótese que <strong class="markup--strong markup--p-strong">no importa la cantidad de elementos, el eje Y no presenta cantidades sino porcentajes. </strong>En este caso el gráfico se hizo con 5.000 elementos pero uno de 50.000 mostraría un área similar.</p>
<p class="graf--p">Grafiquemos las curvas estimadas de densidad para varones y mujeres, usando esta vez la totalidad de los datos:</p>
<figure class="graf--figure"><img class="graf-image" src="assets/40b37-1wnpbdljfrptlljmqdracyq.png" /></figure>
<p class="graf--p">Las curvas de densidad son similares. Este gráfico tampoco hace evidente una diferencia entre las medias. Vamos al tercer paso.</p>
<h4 class="graf--h4">ANOVA</h4>
<p class="graf--p">Para finalizar vamos a usar una herramienta llamada <a class="markup--anchor markup--p-anchor" href="https://en.wikipedia.org/wiki/Analysis_of_variance" target="_blank">ANOVA o <em class="markup--em markup--p-em">Analysis of Variance</em></a><em class="markup--em markup--p-em">. </em>La técnica se utiliza para comparar medias de distribuciones y determinar si la variación entre esas medias puede ser explicada por el azar.</p>
<p class="graf--p">Con R esto es muy sencillo, se arma un modelo lineal y se calcula el anova con la función homónima:</p>
<pre class="graf--pre">&gt; model &lt;- lm(Income ~ Gender, data=clean)
&gt; anova(model)</pre>
<pre class="graf--pre">Analysis of Variance Table</pre>
<pre class="graf--pre">Response: Income
            Df     Sum Sq    Mean Sq F value   Pr(&gt;F)   
Gender       1 1.8123e+09 1812255174  9.5573 0.002006 **
Residuals 3927 7.4464e+11  189620819                    
---
Signif. codes:  0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1</pre>
<p class="graf--p">De toda la información que R nos devuelve, nos interesa el <strong class="markup--strong markup--p-strong">Pr(&gt;F) </strong>que en este caso es <strong class="markup--strong markup--p-strong">0.002. </strong>Este número es la probabilidad de observar estos resultados si las distribuciones de salarios por género fueran iguales.</p>
<p class="graf--p">Esto es <strong class="markup--strong markup--p-strong">significativo.</strong></p>
<p class="graf--p">Lo que ANOVA nos dice es que, suponiendo que la distribución de salario es independiente del género, <strong class="markup--strong markup--p-strong">la probabilidad de encontrar una muestra con esta diferencia salarial entre géneros es del 0.2%</strong>, dicho de otra manera <strong class="markup--strong markup--p-strong">una en quinientos.</strong></p>
<p class="graf--p">Podemos decir entonces que es <strong class="markup--strong markup--p-strong">muy poco probable que se deba al azar</strong> y concluir, por tanto, que las distribuciones no son iguales.</p>
<h4 class="graf--h4">Conclusión</h4>
<p class="graf--p">Pudimos descartar nuestra hipótesis nula. Descubrimos que efectivamente <strong class="markup--strong markup--p-strong">las mujeres cobran menos que los hombres en la industria</strong>. Como vimos a lo largo de este proceso, a veces esto no es evidente y requiere probar distintas fórmulas o estrategias para corroborar nuestra hipótesis.</p>
<p class="graf--p">Saludos!</p>
<p class="graf--p">Gracias a: <a class="markup--anchor markup--p-anchor" href="https://twitter.com/enekaz" target="_blank">Nadia Kazlauskas</a>, <a class="markup--anchor markup--p-anchor" href="http://twitter.com/thecoldsessions" target="_blank">Mauro García Aurelio</a>, <a class="markup--anchor markup--p-anchor" href="https://twitter.com/andavip" target="_blank">Román Avila</a>, <a class="markup--anchor markup--p-anchor" href="https://twitter.com/esacrosa" target="_blank">Alejandro Crosa</a>, <a class="markup--anchor markup--p-anchor" href="https://twitter.com/andresdb2" target="_blank">Andrés de Barbará</a>, <a class="markup--anchor markup--p-anchor" href="https://twitter.com/marianobarrios" target="_blank">Mariano Barrios</a></p>
