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
Slug: analizando-los-sueldos-de-la-industria-del-software-en-argentina-parte-3
Tags:
- sysarmy
Thumbnail: /blog/assets/1-0yjdyv9xusf8w3_g7zdf-q.png
Title: Analizando los sueldos de la industria del software en Argentina (Parte 3)
Topics:
- Development
- Leadership
- Systems
Url: 2016/10/12/analizando-los-sueldos-de-la-industria-del-software-en-argentina-parte-3
date: 2016-10-12
---

<section class="section section--body">
<div class="section-divider layoutSingleColumn"></div>
<div class="section-content">
<div class="section-inner layoutSingleColumn">
<h3 class="graf graf--h3">Analizando los sueldos de la industria del software en Argentina (Parte 3)</h3>
<blockquote class="graf graf--blockquote"><p>hay una diferencia significativa entre la proporción de hombres y mujeres en el decil mejor pago (top 10%) de la industria del software en Argentina.</p></blockquote>
<p class="graf graf--p"><a class="markup--anchor markup--p-anchor" href="2016/09/06/analizando-los-sueldos-de-la-industria-del-software-en-argentina-parte-2/">En el post anterior</a> concluimos que efectivamente había una diferencia en el salario medio dependiendo del género. En este tercer análisis intentaremos rechazar la siguiente hipótesis:</p>
<blockquote class="graf graf--pullquote"><p>Los cargos con sueldos más altos son ocupados equitativamente por hombres y mujeres.</p></blockquote>
<p class="graf graf--p">Para responder esta pregunta debemos primero obtener algunos datos de nuestro dataset:</p>
<ul class="postList">
<li class="graf graf--li">Cuál es el decil más alto?</li>
<li class="graf graf--li">Qué proporción de hombres y mujeres tienen un salario mayor o igual a ese valor?</li>
<li class="graf graf--li">Podemos atribuir la diferencia (de haberla) entre proporciones al azar?</li>
</ul>
<h4 class="graf graf--h4">Cuál es el decil más alto (de nuestra muestra)?</h4>
<p class="graf graf--p">Podemos usar R para calcular el decil más alto de nuestra muestra:</p>
<pre class="graf graf--pre">&gt; quantile(clean$Income, 0.9)
     90%</pre>
<pre class="graf graf--pre">41428.57</pre>
<p class="graf graf--p">Podemos ver entonces que el decil más alto para sueldos de software en Argentina es entonces de $<strong class="markup--strong markup--p-strong">41428.57 brutos.</strong></p>
<h4 class="graf graf--h4">Qué proporción de hombres y mujeres tienen un salario mayor o igual a ese valor?</h4>
<p class="graf graf--p">Para responder esta pregunta podemos usar la función <code class="markup--code markup--p-code">table</code></p>
<pre class="graf graf--pre">&gt; table(clean$Gender, clean$Income &gt;= 41428.57)</pre>
<pre class="graf graf--pre">FALSE TRUE</pre>
<pre class="graf graf--pre">F   276   22</pre>
<pre class="graf graf--pre">M  3256  375</pre>
<p class="graf graf--p">Como vemos, la cantidad de mujeres que pertenecen al último decil es <strong class="markup--strong markup--p-strong">22 de 276 o sea un 7.9%</strong> en el caso de los hombres este número es <strong class="markup--strong markup--p-strong">375 de 3256, un 11.5%.</strong></p>
<p class="graf graf--p">La diferencia de porcentaje es entonces del <strong>3.6% aproximadamente</strong>.</p>
<h4 class="graf graf--h4">Podemos atribuir la diferencia entre proporciones al azar?</h4>
<p class="graf graf--p">Como vimos, hay una diferencia entre el porcentaje de hombres y mujeres en el decil más alto de salarios. Hay dos hipótesis que pueden explicar esta diferencia:</p>
<ul class="postList">
<li class="graf graf--li">La diferencia entre proporciones se debe al azar de la muestra. (Hipótesis Nula)</li>
<li class="graf graf--li">La diferencia entre proporciones es muy grande como para atribuirla al azar, la diferencia es estadísticamente significativa. (Hipótesis Alternativa)</li>
</ul>
<p class="graf graf--p">Para la diferencia de proporciones podemos aplicar el <strong class="markup--strong markup--p-strong">teorema central del límite</strong>: la diferencia entre dos proporciones de una muestra (p^¹ -p^²) tiene una <strong class="markup--strong markup--p-strong">distribución normal</strong> con <strong class="markup--strong markup--p-strong">centro en la verdadera diferencia</strong> entre proporciones (p1-p2), con <strong class="markup--strong markup--p-strong">una desviación estándar conocida</strong> (la fórmula es algo larga, la vamos a usar más adelante para evaluar nuestra hipótesis). Para más información sobre este tema en particular, <a class="markup--anchor markup--p-anchor" href="http://stattrek.com/estimation/difference-in-proportions.aspx?Tutorial=AP" target="_blank">ver aquí</a>.</p>
<p class="graf graf--p">Resumiendo, tenemos una distribución normal con los siguientes valores:</p>
<pre class="graf graf--pre">Media = 0  # p1 — p2 para la hipótesis nula es cero</pre>
<pre class="graf graf--pre">Desviación estándar = 
sqrt((p1 * (1 - p1) / n1) + (p2 * (1 - p2) / n2))</pre>
<pre class="graf graf--pre"># siendo:
# p1 = porcentaje de hombres en el último decil
# n1 = total de hombres
# p2 = porcentaje de mujeres en el último decil
# n2 = total de mujeres</pre>
<pre class="graf graf--pre"># por lo tanto
Desviación estándar = 0.016</pre>
<p class="graf graf--p">Pasemos a graficar nuestra distribución normal:</p>
<figure class="graf graf--figure"><img class="graf-image" src="assets/f79a6-17cc7_uy5pzkvju1xgqxzjg.png" /></figure>
<p class="graf graf--p">Según <a class="markup--anchor markup--p-anchor" href="https://en.wikipedia.org/wiki/68%E2%80%9395%E2%80%9399.7_rule" target="_blank">la regla de 68–95–99.7</a> casi la totalidad de las muestras de una distribución normal caen en -/+ 3 desviaciones estándar (0.016).</p>
<p class="graf graf--p">Podemos ahora graficar sobre esta distribución el <strong class="markup--strong markup--p-strong">3.6%</strong> de diferencia que observamos en nuestra muestra:</p>
<figure class="graf graf--figure"><img class="graf-image" src="assets/2339d-10yjdyv9xusf8w3_g7zdf-q.png" /></figure>
<p class="graf graf--p">De ser válida la hipótesis nula, <strong class="markup--strong markup--p-strong">la probabilidad de obtener esta diferencia es del 1.4%</strong>, si tomamos un nivel de significación del 5% (el utilizado comúnmente en ciencia) <strong class="markup--strong markup--p-strong">podemos descartar la hipótesis nula.</strong></p>
<h4 class="graf graf--h4">Conclusión</h4>
<p class="graf graf--p">Usando el teorema central del límite para las proporciones determinamos que <strong class="markup--strong markup--p-strong">hay una diferencia estadísticamente significativa entre la proporción de hombres y mujeres en el decil mejor pago de la industria del software en Argentina.</strong></p>
</div>
</div>
</section>
<section class="section section--body">
<div class="section-divider layoutSingleColumn">
<hr class="section-divider" />
</div>
<div class="section-content">
<div class="section-inner layoutSingleColumn">
<p class="graf graf--p">Muchas gracias a Sebastián Waisbrot, Nadia Kazlauskas, Pablo Astigarraga, Sebastián Friseb y Mauro García Aurelio que revisaron el draft.</p>
</div>
</div>
</section>
