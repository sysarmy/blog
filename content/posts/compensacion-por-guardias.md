---
Title: "Compensación por guardias"
Description: "Este artículo es una traduccción de la segunda parte y final de una serie sobre guardias. La Parte 1 —publicada la semana pasada, en inglés— cubre las buenas prácticas de las guardias."
Keywords:
- guardias
- oncall
- sre
- mejores-practicas
- remuneracion

Tags:
- sysarmy
- oncall
- guardias
- mejores-practicas

Thumbnail: assets/template.jpg
socialImage: assets/template.jpg
featuredImage: assets/template.jpg

Topics:
- guardias
- oncall
- sre
- mejores-practicas
- remuneracion

markup: markdown
date: 2022-08-22
draft: false
---

_La versión original de este post se puede encontrar en [The Pragmatic Engineer](https://blog.pragmaticengineer.com/oncall-compensation/) (inglés)._

Este artículo es la segunda parte y final de una serie sobre guardias. La [parte 1](https://newsletter.pragmaticengineer.com/p/healthy-oncall-practices) (en inglés) —publicada la semana pasada— cubre las buenas prácticas de las guardias. En esta emisión, nos ahondaremos en:

1. **Filosofía de guardias a lo ancho de la industria.** ¿Cómo diferentes grupos de empresas tratan la práctica de guardias y la compensación?
2. **Compañías que pagan y las que no.** Un panorama de más de 120 empresas y su manera de pagarlas, versus otras que no.
3. **¿Cuánto pagan las empresas?** Datos de 80 empleadores, el conjunto de datos más grande de este estilo publicado a la fecha.
4. **Compañías que no pagan.** ¿Cómo manejan las guardias?
5. **Mala cultura de guardias.** Ejemplos de lugares donde las guardias pueden ser razón de alejarse/quejarse.

En esta nota, analizaremos más de 80 puntos de datos sobre cómo diferentes empresas pagan por las guardias. A continuación una vista previa de los datos que discutiremos:

![](assets/oncall_comp_1.png)

## 1. Filosofías de guardia en la industria

   Mirando toda la industria, hay varias filosofías diferentes.

1. **“Estar de guardia es tu único trabajo”.** Algunas compañías contratan técnicos dedicados específicamente a estar de guardia, hacerse cargo de alertas, mejorar la infraestructura de las guardias. Este rol es llamado ‘Ingeniero de DevOps’ en algunas compañías, SRE (Site Reliability Engineer, Ingeniero de Confiabilidad de Sitio) en otras, y puede ser llamado también ‘Ingeniero de Operaciones’.

    El rol está bien definido así que las expectativas son claras y los turnos son escalonados, para tener una carga de trabajo razonable.

    Estos roles son típicos en empresas más tradicionales, muchas de las cuales están en transición de un modelo de Operaciones, a uno de entrega continua. Este rol también se encuentra generalizado en industrias altamente reguladas. Compañías que priorizan el bienestar de los ingenieros de software posiblemente opten por este modelo, o al menos tienen gente dedicada a estar de guardia para aliviar la carga de los ingenieros de la organización.

2. **“No es parte de tu trabajo fuera del horario laboral”.** Muchas empresas no esperan que los ingenieros estén de guardia fuera del horario laboral. Estas compañías típicamente son:
    * Empresas locales que sirven a clientes locales que usan el servicio durante la jornada normal de trabajo. Muchos servicios B2B podrían caer en esta categoría. En estos casos, los clientes no tienen problemas si el sistema no funciona fuera del horario laboral.
    * Empresas en las que la caída de sistemas fuera del horario laboral no es un problema importante. Estas son pequeñas empresas o aquellas que operan con poca o ninguna competencia comercial.
    * Startups con pocos o ningún cliente.
    * Agencia de desarrollo y consultoras generalmente no cubren guardias, aunque puede llegar a haber excepciones dependiendo del contrato con el cliente.

3. **“No es parte de tu trabajo fuera del horario laboral, pero podríamos llegar a intentar llamarte”**.

    Una variación de los dos casos anteriores, cuando la compañía no espera que los ingenieros de software estén disponibles. Sin embargo, tienen a alguien de guardia, y esa persona podría intentar comunicarse con los ingenieros de software durante una caída del sistema. De todos modos, no se requiere que el ingeniero conteste el teléfono.

    Esto es el caso típico en pequeñas empresas y startups donde los incidentes son pocos y muy esporádicos como para requerir guardias “oficiales”. Es más común en compañías donde los fundadores trabajan a la par, y pueden resolver la mayoría de los problemas por sí mismos, por tanto cargan con la mayor parte de la carga de las guardias, en lugar de los ingenieros.

4. **“Es parte del trabajo de todos los ingenieros de software y operamos en regiones que regulan cómo deben ser compensadas con paga y tiempo libre”.**

    Hay muchos países que regulan la paga de las guardias y el tiempo libre, la lista fue cubierta en la Parte 1. La mayoría de las empresas que operan estas regiones estructuran la compensación por guardias en concordancia con las regulaciones locales.

    Digo la “mayoría” ya que dos grupos, técnicamente, van a violar las regulaciones:

    1. Compañías con una oficina satélite y gerencia que desconoce las reglas locales. En este caso, recaería en los empleados locales comunicar sobre la regulación y lograr que se aplique la compensación correspondiente.
    2. Pequeñas compañías para las cuales seguir regulaciones inadecuadas para empresas tecnológicas ocasionarían más daños que beneficios. En algunos países, las regulaciones para guardias han sido redactadas para grupos como los bomberos, o la policía. Mientras esas reglas tienen sentido para muchas profesiones no digitales, los requerimientos de la regulación podrían ser demasiado rígidos para ser adoptados por pequeñas empresas de tecnología. Por lo tanto, podrían llegar a esquivarlas y compensar con algo parecido, pero no seguirlas al pie de la letra.

5. **“Es parte del trabajo, pero reconocemos la molestia con paga y tiempo libre adicional”.**

    Empresas empáticas reconocen que estar de guardia es otra carga que necesita ser compensada, sin importar la falta de una regulación local que los obligue. Estas compañías ofrecen paga, y podrían ofrecer también la habilidad de tomarse tiempo libre, o una compensación mixta. Empresas que típicamente son así:

    * Firmas tradicionales que ya pagan guardias en otras partes del negocio. Para ellas, pagar a los ingenieros de software para estar de guardia es un hecho.
    * Compañías que pagan igual o por debajo de la media del mercado. Sin pagar por el tiempo de la gente, estos lugares verán mucho desgaste o rotación de personal, ya que los ingenieros buscarán oportunidades en otra parte.
    * Compañías invirtiendo en prácticas sanas de guardia. Estas compañías ven a las guardias como un costo que debe ser cuantificado, y así lo hacen.

6. **“Es voluntario para la mayoría de la gente, y lo alentamos con paga y tiempo libre”.**

    El grupo final son compañías que realmente necesitan gente de guardia, pero se las arreglan para estructurarlo de tal forma de hacerlo de manera voluntaria. Consiguen suficientes voluntarios compensando generosamente por estar de guardia. Usualmente, estos lugares tienen gente dedicada a las guardias trabajando a la par de ingenieros DevOps o SREs.

    ¿Y qué pasa si no hay suficiente gente como para cubrir las guardias? La compañía se podría reservar el mandato de determinar que cualquiera puede estar de guardia hasta que haya la cantidad suficiente de voluntarios, pero pagando generosamente por su tiempo. En la mayoría de los casos, las compañías con las que hablé que implementan las guardias de esta manera consiguen reclutar suficientes voluntarios.

    Por ejemplo, un ingeniero de The Guardian - el diario y sitio web ubicado en el Reino Unido - me compartió que sus guardias son voluntarias y funciona bien:

    > “Nuestras guardias se pagan £750 por semana. Es una rotación voluntaria de 2 ingenieros cada semana. Por encima de la paga, se te alienta a descansar después de tu turno. Las guardias son populares y no tenemos problemas para llenar la rotación.”

    Las guardias voluntarias pueden funcionar bien si la cantidad de gente que se requiere para cubrirlas es muy menor al número de ingenieros en la compañía.

7. **“Es parte del trabajo de todos los ingenieros de software y no se paga adicionalmente”.**

    Este método es común en muchas compañías. Algunas de las cuales resaltan:

    * Compañías pagando el tope del mercado. Los lugares que se ubican en el nivel más alto de la [naturaleza trimodal de los salarios](https://blog.pragmaticengineer.com/software-engineering-salaries-in-the-netherlands-and-europe/) (inglés) usualmente pagan mucho más sin compensar por las guardias, que compañías de niveles menores con muy generosas compensaciones por las mismas.
    * Big Tech. La mayoría de las grandes compañías de tecnología no pagan las guardias con dinero. Google es la única excepción.
    * Startups con poco capital. Las guardias son parte del trabajo en startups que no tienen grandes inversiones. Este es el caso de la mayoría de las startups con financiación pre semilla o semilla, mientras que algunas Serie A también operan así.
    * Compañías que se salen con la suya. Incluso si no están pagando el tope del mercado, compensar por las guardias es un gasto adicional. Muchas compañías tratarán de evitarlo, si lo pueden lograr.

Algunas firmas compensan con tiempo libre, en lugar de dinero. Esto puede variar desde invitar a la gente a que entre más tarde si fueron llamados la noche anterior, hasta ofrecer un número específico de días a modo de vacaciones pagas por cada semana trabajada de guardia. Para compañías que de por sí ya ofrecen vacaciones ilimitadas, ofrecer días libres no cambia nada de la política existente, por lo que no será visto como una medida beneficiosa.

Aunque listo siete filosofías diferentes, en realidad, hay dos principales maneras de pensar sobre las guardias:

1. **Las guardias para los ingenieros de software son adicionales**
    1. “Estar de guardia es tu único trabajo.”
    2. “No es parte de tu trabajo fuera del horario laboral.”
    3. “No es parte de tu trabajo fuera del horario laboral, pero te podríamos llamar durante ese momentos.”
    4. “Es parte del trabajo para todos los ingenieros de software y operamos en regiones que regulan cómo se debe comenzar con paga y tiempo libre.”
    5. “Es parte del trabajo, pero reconocemos la molestia con paga y tiempo libre adicional.”
    6. “Es voluntario para la mayoría de la gente, y lo alentamos con paga y tiempo libre.”

2. **Las guardias son parte del trabajo**

   7. “Es parte del trabajo para todos los ingenieros de software y no se paga adicionalmente."

## 2. Empresas que pagan por las guardias, y aquellas que no

Estar de guardia significa que tenés que estar alerta y tener tu laptop con vos todo el tiempo, así podés responder llamados y empezar a resolver incidentes en cuestión de minutos. La mayoría de los ingenieros de software que están de guardia tienden a tener esta responsabilidad por una semana.

Estar de guardia puede ser molesto/disruptivo de dos grandes maneras:

* **Modifica tus planes personales, fuera del trabajo.** ¿Querés ir a ver una película con tu hijo, o tal vez a una cita? Llevá tu teléfono y tu laptop y está listo para salir de inmediato si recibís un aviso. Para cualquier evento durante la noche, los fines de semana o durante las vacaciones, necesitás conseguir alguien que te cubra con una guardia secundaria - si hay alguien disponible - o estar listo para que tu tiempo personal sea cortado. Algunas personas acomodan sus eventos sociales para que no coincidan con sus semanas de guardia.

* **Interrumpe tu sueño.** A las alertas no les importa qué hora es y pueden despertarte en medio de la noche. Podrías tener que hacer una investigación a las 3 de la mañana. Esto me ha pasado más de una vez. Interrumpir tu descanso puede tener consecuencias en la salud a corto y largo plazo, según estudios científicos.

Muchos países tienen regulaciones estrictas para las guardias, algunas de ellas incluso determinando la cantidad correcta de horas de descanso ininterrumpido por día o por semana.

El sitio de manejo de incidentes incident.io (del cual soy inversor) llevó a cabo una encuesta donde obtuvo 200 respuestas, y encontró que mientras del 70% de los encuestados dijo que cada equipo era responsable por la rotación de guardias, alrededor del 40% eran compensados por las mismas.

> “Curiosamente, esto era más común en organizaciones más grandes (más de 5000 empleados) que en pequeñas o medianas empresas que participaron en la encuesta. En aquellos casos en los que se compensaba, la mayoría pagaba un monto fijo por tiempo de guardia (por ejemplo, $X por hora, día o semana). Pero el valor en dólares pagado variaba significativamente, de $5 a $1000 por semana, con promedio semanal de $540”.

Para esta serie sobre guardias, invité a la gente a compartir sobre si sus compañías pagan por las guardias, y si lo hacían, cuánto. A continuación una colección de empresas que no pagan a los ingenieros de software por las guardias - pero aún así requieren que se hagan - y las que sí lo hacen. Esta es una colección de datos de gente que lo compartió anónimamente. La lista no es exhaustiva, y hay empresas que faltan. Sin embargo, es el conjunto de datos más grande al respecto publicado a la fecha.

Al respecto de las empresas en la columna de “Unpaid oncall” (“Guardias no remuneradas"), las mismas deben seguir las regulaciones locales para compensación por guardias en aquellos países que lo requieren, tal como discutimos en la Parte 1 de la serie.

Así que, ¿qué compañías pagan y cuáles no?

![](assets/oncall_comp_2.png)

![](assets/oncall_comp_3.png)


**Vamos a hablar sobre el elefante en la habitación: Las grandes empresas de tecnología generalmente no pagan por estar de guardia.** Excepto por Google, y exceptuando regiones donde están obligadas a pagarlas, no las compensan. ¿Por qué pasa esto?

Una de las mayores razones es que estas empresas pagan los mayores salarios del mercado: en el tercer y más alto nivel del modelo trimodal de compensaciones. Así que aún no pagando por las guardias, pagan más que muchas otras que pagan menos, pero compensan adicionalmente por las mismas.

Y es razonable argumentar que en cierto punto, tienen razón. Entre estas dos ofertas, ¿cuál es más interesante?

1. $140.000 dólares en compensación total. Guardias pagadas adicionalmente, a $800-$1200 dólares por semana, alcanzando un adicional de $8.000-$12.000 dólares por año.
2. $310.000 dólares en compensación total ($180.000 de salario básico + el resto en acciones). Las guardias no se pagan.

Muchas startups muy bien financiadas que pagan cerca del tope del mercado también esperan que se realicen guardias.

El único dato curioso es cómo Google, además de pagar el tope del mercado, también paga por las guardias, e invierte en prácticas sanas al respecto, como lo hemos cubierto en la Parte 1 de la serie.

## 3. ¿Cuánto pagan las empresas?

¿Cuánto pagan las empresas para compensar por las guardias? La respuesta es: varía un montón. Esto varía desde cerca de $100 dólares por semana, a aproximadamente $1250 dólares por semana - e incluso más para algunos ingenieros de Google.

**¿Cómo las pagan?** Está dividido en 3 formas, ordenadas por frecuencia:

1. **Monto fijo** por semana o por día de guardia. El mismo monto es pagado, sin importar si hubo incidentes que necesitaron atención o no. La mayoría de las empresas que las pagan lo hacen así.
2. **Monto fijo para guardias pasivas, mas paga extra por horas trabajadas fuera del horario laboral.** Otra forma es tener un monto fijo por guardias pasivas. Sin embargo, cuando ocurre un incidente y los ingenieros tienen que pasar tiempo mitigando, pueden pedir compensación adicional por este tiempo. Esto es generalmente un múltiplo de su valor por hora, y aumenta en fines de semana o feriados. Muchos países obligan a hacerlo así, aun si las compañías pagan decentemente por las guardias pasivas.
3. **Sólo se paga por incidentes trabajados fuera del horario laboral.** Algunas compañías no pagan por las guardias pasivas, pero sí si se ven obligados a trabajar durante la noche o los fines de semana. Este trabajo es, por lo general, para mitigar un incidente.  La mayoría de las compañías que pagan de esta manera, lo hacen así por regulaciones locales, que obligan a pagar horas extras durante la noche o los fines de semana.

A continuación un resumen de cómo pagan distintas compañías.

![](assets/oncall_comp_4.png)

![](assets/oncall_comp_5.png)

![](assets/oncall_comp_6.png)

![](assets/oncall_comp_7.png)

![](assets/oncall_comp_8.png)

Algunos datos curiosos sobre los montos detallados más arriba:

* **Brasil y España: paga regulada.** Ambos países tienen regulaciones claras sobre cómo deben ser pagadas las guardias para todas las empresas con subsidiarias locales.
* **Alemania: usualmente pagan sin que haya regulación.** Las empresas alemanas generalmente pagan por las guardias, aún no habiendo regulación local sobre el pago de guardias pasivas, sólo está regulado la obligatoriedad del tiempo de descanso.
* **Reino Unido: algunas empresas pagan, aún ante la falta de regulación.** Aunque el RU no obliga a pagar por las guardias, es más común ver empresas que lo hacen allí a diferencia de los Estados Unidos, por ejemplo. Esto puede ser debido a que las empresas del Reino Unido están contratando remotamente en otros países europeos donde sí están obligados a pagar.
* **Estados Unidos: pocas compañías pagan.** Sin embargo, aquellas que sí lo hacen, tienden a hacerlo globalmente. Google, Intercom, Spotify, LaunchDarkly, CircleCI y PayPal, para mencionar algunas, son las que pagan por guardias pasivas, incluso en los Estados Unidos.

## 4. Empresas que no pagan, pero premian las guardias

En empresas que no compensan por las guardias, ¿hay una aproximación diferente? Al hablar con ingenieros de software de guardia en estas empresas, muchos compartieron que si obtienen algunos beneficios, sobre todo relacionados con tiempo libre. A continuación un resumen al respecto:

| Compañía              | Política (citas de empleados) |
| --------------------- | ----------------------------- |
| Apple                 | “Los equipos de SRE cubren la mayoría de las guardias. Los SREs que cubren los fines de semana, obtienen esos días libres durante la semana siguiente. Las guardias pasivas son muy raras para los ingenieros de software. Cuando las tenés, obtenés la cantidad de días que estuviste de guardia como días libres la semana siguiente." |
| Microsoft (US)        | “En mi equipo hacemos 3 turnos al año en el que estás de guardia 24/7." “En Bing, la rotación es de jueves a jueves. No nos pagan las guardias, pero sí obtenemos el viernes siguiente a las mismas libre. Si la semana de guardia fue muy intensa, el ingeniero que la trabajó podría pedir más tiempo libre. Hacemos dos rotaciones de guardias primarias y dos de respaldo al año, en promedio.” |
| Shopify               | “Los equipos en producción tienen rotaciones donde el primario tiene la responsabilidad durante 7 días seguidos. Las rotaciones tienden a tener 4 a 8 ingenieros. Obtenemos un día libre después de cada turno.” |
| Walmart               | “Pagan por mis dispositivos y mi conexión a Internet y horas extras para personas que están de guardia o son llamados fuera del horario de trabajo.” |
| Amazon (Países Bajos) | “Hubo un aumento para todos los que necesitaban estar de guardia en Amazon Países Bajos, alrededor de 2017-2018. Sin embargo no se pagan extra." |
| FreshBooks            | “La empresa te da tiempo libre por estar de guardia. 1 día a la semana por estarlo. Si te llaman fuera del horario laboral, obtenés 1.5 horas por hora trabajada."|
| Gopuff                | “En teoría nos podemos tomar tiempo libre extra, pero ya tenemos vacaciones ilimitadas. Mi equipo tiene una semana de guardia de nivel 1 o 2 cada 6 meses.” |
| Pivotal               | “Tenemos una política en la cual todo tiempo pasado resolviendo incidentes fuera del horario laboral, se compensa con el doble en tiempo libre durante el horario laboral. Así que, si pasaste 2 horas durante la noche resolviendo un incidente, te podes tomar hasta 4 horas durante la jornada laboral.” |
| PagerDuty             | “Si estás de guardia durante un feriado o vacaciones, te dan días extras en compensación por el tiempo que estuviste.” |
| Adobe (Romania)       | “Las guardias antes se pagaban, pero después la compañía le aumentó el sueldo a los que las hacían y eliminó el extra. Siguiendo esta política, los ingenieros que tenían que estar de guardia fuera del horario laboral, estaban habilitados para pedir tiempo libre en correspondencia a las horas de guardia que hubieran hecho.” |
| Carwow                | “Dos ingenieros rotan cada semana, se los alienta a pedir tiempo libre si entran en acción. Obligatorias para líderes técnicos, opcional para ingenieros senior." |
| OFX                   | “Ofrecen 2 veces el tiempo pasado en actividades de guardia, si eso pasa.” |
| Una scaleup de serie B | “Un desarrollador está de guardia y es responsable por el monitoreo y por incidentes en producción. No nos pagan, pero si hay un problema, obtenemos el doble del tiempo que pasamos solucionandolo en tiempo extra de vacaciones.”

_Empresas que ofrecen tiempo libre, en lugar de efectivo._

| Compañía                 | Política (citas de empleados) |
| ------------------------ | ----------------------------- |
| Sixt (alquiler de autos) |“Los EMs saben por qué algo no fue completado en el sprint actual, pasándose al siguiente. No cuestionan el retraso si estabas de guardia.” |
| Box                      | “Es típico que se espere menos carga laboral para el sprint si estás de guardia.” |
| Upgrade.com              | “Técnicamente estamos autorizados a tomarnos tiempo libre, pero como siempre estamos tan ocupados, eso raramente sucede.” |

_Compañías sin una cultura de ofrecer tiempo libre por las guardias._

## 5. Mala cultura de guardias

Durante mi investigación, me encontré con algunos ejemplos de malas prácticas respecto de las guardias.

**Twilio** es una compañía sobre la que recibí un número inusual de quejas al respecto. Todos los contribuyentes tuvieron una mirada negativa sobre cómo actualmente se llevan a cabo guardias en la misma.

Así es como un ingeniero de software que trabaja en la empresa detalla las expectativas de Twilio:

> “La duración de los turnos es discutida libremente con los equipos. Generalmente, es de 7 días, pero en equipos con menos miembros, 2 o 3, también pueden hacer rotaciones de 3 días. Si estás en un equipo de 4, estás casi en ‘la cárcel de las guardias’ 2 de cada 4 semanas (semana secundaria + primaria).
>
> Últimamente, ha habido fuertes discusiones internas dentro de los equipos de Investigación y Desarrollo (más que nada al respecto de las guardias) por esto.
>
> Reglas generales - de nuevo, cada equipo las puede variar:
> 
> 1. Se espera que actúes dentro de los 10 minutos desde que se dió la alarma.
> 2. Se espera que actúes dentro de los 5/10 minutos dentro del POC (punto de contacto - alertado por otro equipo o persona).
> 3. Nada de drogas o exceso de alcohol durante las guardias.
> 4. Escalá pronto si encontrás problemas.
> 5. Podés viajar, si podes respetar todo lo anterior.

Muchos ingenieros trabajando en la empresa me dijeron que la carga laboral durante las guardias es muy alta, los equipos están con poco personal, las guardias no se pagan, y alguien incluso usó el término “cárcel de guardias”, como dije más arriba. Algunas citas adicionales de ingenieros de software y gerentes de esa compañía:

* “Twilio no paga nada adicional por estar de guardia, tampoco obtengo tiempo libre después de un turno tortuoso. Odio la vida de guardia y cuando sea el momento de cambiar, prefería no hacerlas. Estoy de guardia cada 4 semanas.”
* “Hay servicios críticos que tienen asignados poco personal, a los encargados de esos servicios les niegan la contratación de gente porque “no mueven la aguja”."
* “La gente está empezando a tomar medidas drásticas por la alta carga laboral de las guardias, llegando a renunciar. Así que ahora, sumado al estrés hay un alto nivel de desgaste debido a la falta de reconocimiento institucional.

¿Cual es la razón por la alta carga de las guardias? Hablé con algunos ingenieros que tenían dos o más años de experiencia. Esto es lo que dijeron:

* **Mucho ‘ADN de Amazon’**. Mucha de la gerencia de ingeniería viene de Amazon, y se concentran en la excelencia operacional. Esto significa reglas estrictas para las guardias.
* **Crecer muy rápido** en un corto tiempo. Los ingenieros con los que hablé me dijeron sobre cómo la compañía creció agresivamente en 2020 y 2021, duplicando el tamaño de la organización de ingeniería en 2021, mientras que crecía 5 veces en los últimos 3 años de ~1500 empleados en 2019, a más de 7000 empleados de tiempo completo a comienzos de 2022.
* **Muchos sistemas a medida.** Estos sistemas a medida complican la solución de problemas de base durante las guardias. A su vez, como tantos de los sistemas son a medida, no es práctico mezclar las guardias entre los equipos.
* **Agotamiento de personas con experiencia.** Twilio sufrió de agotamiento severo en 2021, gracias al mercado en alza. Los ingenieros me dijeron que muchas personas con conocimientos sobre en detalle sobre los sistemas a medida renunciaron. La salida de estas personas ocasionó un problema para resolver cosas de base.
* **Sin reemplazo.** Un ingeniero dijo: “Mi área perdió más de la mitad de sus ingenieros en los últimos dos meses. No hay reemplazos en camino, y la carga de las guardias se incrementó significativamente. La gente seguramente se seguirá yendo y es un riesgo operacional quedarse acá.”
* **Un problema de deuda técnica poco reconocido.** Los ingenieros me cuentan que sienten que la empresa no reconoce el nivel de deuda técnica que posee, hasta hace poco. Actualmente están tomando medidas que - una vez completadas - también deberían solucionar problemas con las guardias.
* **La luz al final del túnel.** Muchos mencionaron como la nueva gerencia que viene de lugares como Google están poniendo más atención a prácticas más sanas respecto de las guardias, aceptando que el estado actual es insostenible.

La buena noticia en Twilio es que la gerencia parece saber de la insostenibilidad del estado actual de las guardias, y está trabajando en solucionar el problema. Los ingenieros con los que hablé compartieron cómo mientras el burnout está golpeando a muchos de ellos, siente que los líderes están tratando de solucionar las cosas y empoderarlos. Uno de los que habló conmigo me dijo cómo siente que lo que está manteniendo la empresa a flote es la forma de pensar de muchos de los ingenieros con más años de experiencia; asumen que las cosas están bien como están - incluída la alta carga laboral de las guardias. 

**Amazon** es otra empresa donde el estrés en las guardias es alto y no son compensadas - a menos de que estén reguladas localmente, como en Brasil o España. En Prime Video en el RU, la compensación por guardias fue heredada: cuando Amazon adquirió la startup LoveFilm en 2011 - una startup que se transformó en Prime Video - la compensación por guardias era parte de todos los contratos al corriente y futuros, y se mantuvo de esa manera.

Las guardias es una de las mayores cosas negativas de trabajar en Amazon.

> “Lo malo: Alta carga laboral de guardia y en horario normal. Se espera que los equipos operen bien sus sistemas, y esto se hace de una manera que resulta en guardias estresantes. Los problemas operacionales necesitan ser solucionados inmediatamente en lugar de escalarlos.”

Diferentes equipos y organizaciones, tienen diferentes cargas durante las guardias. La gente que trabaja en Alexa y Redshift comparten historias sobre cargas laborales extremas durante las mismas.

Los gerentes de ingeniería - llamados SDMs (Gerentes de Desarrollo de Software) - de Amazon han intentado ayudar con la carga de las guardias ofreciendo días libres. Tal como nos cuenta un actual ingeniero de Amazon:

> “Luego de laboriosas guardias en el área de Alexa Devices, muchos SDMs han permitido que la gente se tome tiempo libre pago para compensar (si te quedas hasta tarde, entrá tarde, si trabajaste un fin de semana, tomate días libres, etc.) Esto no es una política oficial, un cambio en la gerencia (como una reorganización, algo que sucede bastante seguido) y cualquier tiempo libre acumulado “por debajo de la mesa” desaparece.”

Sin embargo, he leído algunas historias de empleados que sufrieron agotamientos extremos debido a la carga excesiva durante las guardias, y este agotamiento manteniéndose en puestos futuros. Un ingeniero de software con quien hablé me contó cómo se agotan tanto por el trabajo en las prácticas de guardias de Amazon, que les costó unos meses acomodarse a su nuevo trabajo en una startup debido a que se estaban recuperando mental y físicamente de la opresión sufrida en Amazon.

**Otros ejemplos.** Algunos ingenieros tienen historias preocupantes que comparto a modo advertencia:

* “Algunos equipos han tenido volúmenes de alertas dramáticamente diferentes por años en mi empresa. Hay equipos en los que la gente quiere trabajar debido a su importante misión, pero esos mismos equipos tienen guardias. Por ninguna razón pasaría a trabajar con esos equipos, siendo que el pase incluiría tantas horas extras no remuneradas fuera del horario laboral.” De una compañía valuada en 13.000 millones de dólares.
* “Nunca había hecho guardias hasta que trabajé para esta compañía, y era la única duda que tenía al respecto sobre empezar a trabajar con ellos. En definitiva, fue una de las razones por las que me fuí. Las guardias para mi equipo no parecían terribles, pero tenía cero interés en estar listo para conectarme al trabajo a cualquier hora del día. Si me hubieran pagado por mi tiempo, tal vez habría cambiado de opinión." De una compañía valuada en 3000 millones de dólares.
* “Estar de guardia era parte del trabajo, pero no estaba mencionado con claridad en el contrato. Tu informe anual podría verse afectado por no alcanzar ciertas expectativas durante las guardias.” Empresa de datos financieros de los Estados Unidos.
* “Tenemos una cultura de esperar que se pongan actualizaciones en producción aún si pasaste toda la noche solucionando una caída severa… tenemos problemas por esta razón.” Empresa de automatización de depósitos.

**¿Por qué las malas prácticas de guardias pueden ser problemáticas?** Pueden impactar directamente en el agotamiento de los ingenieros de software y su bienestar. Para ponerlo en pocas palabras, las malas prácticas de guardias llevarán a más ingenieros a renunciar, a más gente a agotarse y a menos gente recomendando para trabajar en la empresa.

El ejemplo de Twilio debería ser una advertencia desde mi punto de vista. Mientras la compañía ha sido un suceso comercial, ha tenido grandes problemas con el agotamiento, y no se las ha arreglado para acomodar el problema de las guardias, lo que en definitiva puede ocasionar que el tema del agotamiento empeore.


## Conclusiones

Basado en mi investigación exhaustiva y anecdótica del estado actual de la industria, parecería ser que hay dos filosofías principales respecto al premio por las guardias:

1. **Las guardias para los ingenieros de software es parte del trabajo.** Muchas empresas operan así, sobre todo las grandes empresas de tecnología - salvo por el ejemplo de Google - y startups con crecimientos rápidos. Cuanto más se paga, más se espera que haya guardias.
2. **Las guardias para ingenieros de software son adicionales.** Empresas que se preocupan por tener prácticas sanas respecto de las guardias o quieren minimizar el agotamiento de los ingenieros de software, se aseguran de que las guardias sean adicionales y ofrecen algo en compensación. La compensación puede ser dinero, tiempo libre, o disminución de tareas para SREs o DevOps que demuestran dedicación, o hacer las rotaciones voluntarias.

Puedo decir que estaba viviendo en una “burbuja de guardias” antes de investigar este tema que tiene un impacto tan importante en la vida laboral y personal de tantas personas. Habiendo trabajado en compañías donde las guardias son parte del trabajo, no son pagas, y vienen con mucha presión, asumí que así era como funcionaban en todos lados.

Sin embargo este artículo y su investigación subyacente revelan que el hecho de dar por sentadas las tareas de guardia está lejos de ser la norma en realidad. Muchas compañías - pequeñas y grandes, startups y tradicionales - pagan extra por ellas. En algunos lugares no pagan con dinero, pero sí ofrecen tiempo libre a cambio.

Hemos explorado las prácticas sanas de guardia en la parte 1 de esta serie. Espero que los datos sobre qué empresas pagan y cuánto ayuden a formar tu política de guardias.

Y no te olvides que los ingenieros pueden definir cómo se realizan las guardias, no solo los gerentes; tal como nos cuenta la ingeniera de software Anna Baker de LaunchDarkly en la parte 1.

> “Teníamos un exingeniero de Intercom que se ocupó en desarrollar los nuevos procesos de guardias en la empresa, y procuramos implementar algunas de las prácticas que hemos visto que funcionan bien. Es bastante increíble que un ingeniero esté defendiendo las guardias de su empleador anterior. Aunque terminamos con un modelo un tanto diferente, definitivamente tomamos nota y quiero asegurarme de reconocerlo.”

* La versión original de este post se puede encontrar en [The Pragmatic Engineer](https://blog.pragmaticengineer.com/oncall-compensation/) (inglés).
* Traducción por [@jcasarini](https://twitter.com/jcasarini), revisión por [@nachichuri](https://twitter.com/Nachichuri).
