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
Slug: analizando-los-sueldos-de-la-industria-del-software-en-argentina-parte-1
Tags:
- sysarmy
Thumbnail: /blog/assets/1-y7wayzgfzmxktejssq3prq.png
Title: Analizando los sueldos de la industria del software en Argentina (Parte 1)
Topics:
- Development
- Leadership
- Systems
Url: 2016/08/29/analizando-los-sueldos-de-la-industria-del-software-en-argentina-parte-1
date: 2016-08-29
---

{{% img src="/blog/assets/1-y7wayzgfzmxktejssq3prq.png" class="half right" %}}
<p class="graf--p">Un tiempo atrás, hicimos una encuesta sobre el estado laboral de los trabajadores de software en Argentina y divulgamos los resultados de la misma, <a class="markup--anchor markup--p-anchor" href="https://drive.google.com/open?id=1axuz2PvpbQp85hpbV9Fk6tXKx0XHvx-Z" target="_blank" rel="noopener">disponibles acá</a>.</p>
<p class="graf--p">Hoy vamos a analizarlos paso a paso, usando el lenguaje R. Todo el código está <a class="markup--anchor markup--p-anchor" href="https://github.com/fernandezpablo85/sysarmy-salaries-data-2016/" target="_blank" rel="noopener">disponible online</a> con licencia MIT.</p>
<p class="graf--p">Ante cualquier duda, comentario o mejora, abran un ticket en el repo. También respondo por twitter en <a class="markup--anchor markup--p-anchor" href="https://twitter.com/fernandezpablo" target="_blank" rel="noopener">@fernandezpablo</a></p>
<h4 class="graf--h4">Data Munging</h4>
<p class="graf--p">Los datos se encuentran en formato .csv, que es muy fácil de consumir desde R:</p>
<pre class="graf--pre">&gt; sueldos &lt;- read.csv('argentina.csv')</pre>
<pre class="graf--pre">&gt; nrow(sueldos)</pre>
<pre class="graf--pre">[1] 4001</pre>
<p class="graf--p">Perfecto! tenemos <strong class="markup--strong markup--p-strong">4001 sueldos de argentina</strong>. Lamentablemente hay algunos inconvenientes:</p>
<ul class="postList">
<li class="graf--li">Hay sueldos <strong class="markup--strong markup--li-strong">netos y brutos</strong></li>
<li class="graf--li">Los nombres de las columnas no son los mejores (“Tengo” para edad, “Qu…tan.conforme.est..s.con.tu.sueldo.”, etc).</li>
<li class="graf--li">Algunos salarios son obviamente <strong class="markup--strong markup--li-strong">ficticios o están mal ingresados</strong> (hay algunos de $1, otros de más de un millón)</li>
</ul>
<p class="graf--p">Vamos a hacer lo que se denomina <em class="markup--em markup--p-em">data munging</em> que es básicamente transformar los datos para solucionar los problemas descriptos anteriormente. La función que hace esto se puede <a class="markup--anchor markup--p-anchor" href="https://github.com/fernandezpablo85/sysarmy-salaries-data-2016/blob/master/sysarmy.r#L9-L51" target="_blank" rel="noopener">ver acá</a>.</p>
<p class="graf--p">Los datos “limpios” están en el archivo <a class="markup--anchor markup--p-anchor" href="https://github.com/fernandezpablo85/sysarmy-salaries-data-2016/blob/master/clean.csv" target="_blank" rel="noopener">clean.csv</a> en el repo, por si alguien quiere utilizarlos para crear sus propias visualizaciones.</p>
<h4 class="graf--h4">Histograma</h4>
<p class="graf--p">Con los datos en el formato que queremos, podemos empezar con algunas visualizaciones simples. Un histograma que nos muestre la distribución de los salarios, por ejemplo:</p>
<p><img src="assets/eba8f-1i7omjwjvzse1pk6oncxmxw.png" /></p>
<p id="c03d" class="graf--p graf-after--figure">La distribución es <em class="markup--em markup--p-em">right skewed</em>, lo que significa que no simétrica como una <em class="markup--em markup--p-em">distribución normal</em> sino que se “estira” hacia la derecha (ver <a class="markup--anchor markup--p-anchor" href="https://en.wikipedia.org/wiki/Skewness" target="_blank" rel="nofollow noopener">Skewness</a>). Esto nos indica que hay algunos <strong class="markup--strong markup--p-strong">sueldos muy altos</strong> comparados con la media.</p>
<p id="c805" class="graf--p graf-after--p">Pero ¿cuál es la media? podemos agregar una línea vertical que nos la resalte:</p>
<p><img src="assets/3ded9-1u9ljitzxi07oo7xqhtgjhw.png" /></p>
<p id="d16d" class="graf--p graf-after--figure">La media está en <strong class="markup--strong markup--p-strong">$25.597,71 </strong>(salario bruto, recordemos).</p>
<p id="6cbf" class="graf--p graf-after--p">En las distribuciones no normales como ésta, la media no coincide con el centro de la distribución. En estos casos se puede agregar la <strong class="markup--strong markup--p-strong">mediana</strong>, que está en <strong class="markup--strong markup--p-strong">$22.857,14</strong>:</p>
<p><img src="assets/c9b13-1y7wayzgfzmxktejssq3prq.png" /></p>
<p id="c45a" class="graf--p graf-after--figure">Otro valor interesante es la <strong class="markup--strong markup--p-strong">moda</strong>, el valor que más se repite. En este caso es <strong class="markup--strong markup--p-strong">$21.428,5714</strong>. Si bien es un número raro, recuerden que llegamos a él después de nuestra “normalización” de salario neto/bruto. En este caso probablemente se refiere a <strong class="markup--strong markup--p-strong">$15.000 </strong>de salario neto (en mano).</p>
<h4 id="3d2b" class="graf--h4 graf-after--p">Manejo de Outliers</h4>
<p id="68ac" class="graf--p graf-after--h4">También podemos eliminar los <em class="markup--em markup--p-em">outliers</em> de la muestra, para concentrarnos en el la parte más densa de la distribución. Un método popular para esto es el de <a class="markup--anchor markup--p-anchor" href="http://datapigtechnologies.com/blog/index.php/highlighting-outliers-in-your-data-with-the-tukey-method/" target="_blank" rel="nofollow noopener">Tukey</a>. Antes de “limpiar” los outliers, veamos qué datos nos quitaría de nuestra muestra:</p>
<p><img src="assets/6484b-1c8rx2gpgzn3jlopnbxtgpg.png" /></p>
<p id="18ef" class="graf--p graf-after--figure">De correr el filtro de Tukey para los outliers, todo salario arriba de <strong class="markup--strong markup--p-strong">$46.571,43 </strong>sería descartado (el método también elimina outliers “bajos”, pero en este caso la línea de corte da negativo y por lo tanto no descarta datos).</p>
<p id="6ede" class="graf--p graf-after--p">Los sueldos altos representan en este caso información importante (a mi entender) y por lo tanto no serán descartados para futuros análisis, pero el <a class="markup--anchor markup--p-anchor" href="https://github.com/fernandezpablo85/sysarmy-salaries-data-2016/blob/master/sysarmy.r" target="_blank" rel="nofollow noopener">código disponible</a> permite hacer este recorte cambiando la línea:</p>
<pre id="238b" class="graf--pre graf-after--p">clean &lt;- cleanup(df, handleOutliers = identity)</pre>
<p id="d8f0" class="graf--p graf-after--pre">por esta otra:</p>
<pre id="a9bd" class="graf--pre graf-after--p">clean &lt;- cleanup(df, handleOutliers = tukey)</pre>
<h4 id="0886" class="graf--h4 graf-after--pre">To Be Continued…</h4>
<p id="baba" class="graf--p graf-after--h4">Ya tenemos una idea de la distribución y los datos limpios para seguir analizando ¿qué podríamos preguntarnos ahora? Algo interesante sería poder ver la distribución de salario discriminada por sexo:</p>
<p class="graf--p graf-after--h4"><img src="assets/f1817-1n0b5rjw1akpfg95wv6lttg.png" /></p>
<p id="2b9b" class="graf--p graf-after--figure">A simple vista lo que se puede ver es que hay un porcentaje menor de mujeres en nuestra muestra (de hecho son <strong class="markup--strong markup--p-strong">290 mujeres</strong> y <strong class="markup--strong markup--p-strong">3563 varones</strong>) pero ¿las distribuciones son similares? ¿cobran más los hombres o las mujeres en la industria de software argentino?</p>
<p id="cc86" class="graf--p graf-after--p">La respuesta a estos y otros interrogantes más, en el próximo post 😊</p>
<p id="9c67" class="graf--p graf-after--p">Saludos!</p>
<p id="4845" class="graf--p graf-after--p graf--last"><strong class="markup--strong markup--p-strong">Agradecimientos</strong> a la gente que comentó y sugirió mejoras: <a class="markup--anchor markup--p-anchor" href="https://twitter.com/FedericoBayle" target="_blank" rel="nofollow noopener">Federico Baylé</a>, <a class="markup--anchor markup--p-anchor" href="http://marianobarrios/" target="_blank" rel="nofollow noopener">Mariano Barrios</a>, <a class="markup--anchor markup--p-anchor" href="https://twitter.com/enekaz" target="_blank" rel="nofollow noopener">Nadia Kazlauskas</a>, <a class="markup--anchor markup--p-anchor" href="https://twitter.com/thecoldsessions" target="_blank" rel="nofollow noopener">Mauro García Aurelio</a>, <a class="markup--anchor markup--p-anchor" href="https://twitter.com/andavip" target="_blank" rel="nofollow noopener">Román Ávila</a> y <a class="markup--anchor markup--p-anchor" href="https://twitter.com/andresdb2" target="_blank" rel="nofollow noopener">Andrés de Barbará</a>.</p>
