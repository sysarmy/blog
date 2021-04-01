---
Description: "SQLite no es una base de datos de juguete"
Keywords:
- sqlite 
- bases de datos
- dba
Section: 
Tags:
- sqlite 
- bases de datos
- dba
Thumbnail: assets/sqlite-no-es-una-base-de-datos-de-juguete.svg
socialImage: assets/sqlite-no-es-una-base-de-datos-de-juguete.svg
featuredImage: assets/sqlite-no-es-una-base-de-datos-de-juguete.svg
Title: "SQLite no es una base de datos de juguete"
Topics:
- sqlite 
- bases de datos
- dba
markup: markdown
date: 2021-04-01
draft: false
---
Ya sea que trabajes en desarrollo, analisis de datos, control de calidad, DevOps o producto, [SQLite](https://www.sqlite.org/) es una herramienta perfecta para vos. Aquí contamos por que.

## Algunos hechos bien conocidos para comenzar:

* SQLite es el DBMS más común del mundo, incluido en todos los sistemas operativos populares.
* SQLite no tiene servidor.
* Para quienes desarrollan, SQLite está integrado directamente en la aplicación.
* Para todos los demás, existe una conveniente consola de base de datos (REPL), que se proporciona como un solo archivo (sqlite3.exe en Windows, sqlite3 en Linux / macOS).

<!--more-->

# Consola, importación y exportación

La consola es una característica excelente de SQLite para el análisis de datos: más poderosa que Excel y más simple que `pandas`. Se pueden importar datos CSV con un solo comando y la tabla se crea automáticamente:

    > .import --csv city.csv city
    > select count(*) from city;
    1117

La consola admite funciones básicas de SQL y muestra los resultados de las consultas en una bonita tabla dibujada en ASCII. Las funciones avanzadas de SQL también son compatibles, pero más sobre eso más adelante.

    select
      century || ' century' as dates,
      count(*) as city_count
    from history
    group by century
    order by century desc;

    ┌────────────┬────────────┐
    │   dates    │ city_count │
    ├────────────┼────────────┤
    │ 21 century │ 1          │
    │ 20 century │ 263        │
    │ 19 century │ 189        │
    │ 18 century │ 191        │
    │ 17 century │ 137        │
    │ ...        │ ...        │
    └────────────┴────────────┘

Los datos se pueden exportar como SQL, CSV, JSON, incluso Markdown y HTML. Toma solo un par de comandos:

    .mode json
    .output city.json
    select city, foundation_year, timezone from city limit 10;
    .shell cat city.json
    [
        { "city": "Amsterdam", "foundation_year": 1300, "timezone": "UTC+1" },
        { "city": "Berlin", "foundation_year": 1237, "timezone": "UTC+1" },
        { "city": "Helsinki", "foundation_year": 1548, "timezone": "UTC+2" },
        { "city": "Monaco", "foundation_year": 1215, "timezone": "UTC+1" },
        { "city": "Moscow", "foundation_year": 1147, "timezone": "UTC+3" },
        { "city": "Reykjavik", "foundation_year": 874, "timezone": "UTC" },
        { "city": "Sarajevo", "foundation_year": 1461, "timezone": "UTC+1" },
        { "city": "Stockholm", "foundation_year": 1252, "timezone": "UTC+1" },
        { "city": "Tallinn", "foundation_year": 1219, "timezone": "UTC+2" },
        { "city": "Zagreb", "foundation_year": 1094, "timezone": "UTC+1" }
    ]

Si sos más un BI que una persona de consola, las herramientas populares de exploración de datos como [Metabase](https://www.metabase.com/), [Redash](https://redash.io/) y [Superset](https://superset.apache.org/) son compatibles con SQLite.

# JSON nativo

No hay nada más conveniente que SQLite para analizar y transformar JSON. Puede seleccionar datos directamente de un archivo como si fuera una tabla normal. O importe datos a la tabla y seleccione desde allí.

    select
      json_extract(value, '$.iso.code') as code,
      json_extract(value, '$.iso.number') as num,
      json_extract(value, '$.name') as name,
      json_extract(value, '$.units.major.name') as unit
    from
      json_each(readfile('currency.sample.json'))
    ;
    ┌──────┬─────┬─────────────────┬──────────┐
    │ code │ num │      name       │   unit   │
    ├──────┼─────┼─────────────────┼──────────┤
    │ ARS  │ 032 │ Argentine peso  | peso     │
    │ CHF  │ 756 │ Swiss Franc     │ franc    │
    │ EUR  │ 978 │ Euro            │ euro     │
    │ GBP  │ 826 │ British Pound   │ pound    │
    │ INR  │ 356 │ Indian Rupee    │ rupee    │
    │ JPY  │ 392 │ Japanese yen    │ yen      │
    │ MAD  │ 504 │ Moroccan Dirham │ dirham   │
    │ RUR  │ 643 │ Russian Rouble  │ rouble   │
    │ SOS  │ 706 │ Somali Shilling │ shilling │
    │ USD  │ 840 │ US Dollar       │ dollar   │
    └──────┴─────┴─────────────────┴──────────┘

No importa qué tan profundo sea el JSON: puede extraer cualquier objeto anidado :

    select
      json_extract(value, '$.id') as id,
      json_extract(value, '$.name') as name
    from
      json_tree(readfile('industry.sample.json'))
    where
      path like '$[%].industries'
    ;
    ┌────────┬──────────────────────┐
    │   id   │         name         │
    ├────────┼──────────────────────┤
    │ 7.538  │ Internet provider    │
    │ 7.539  │ IT consulting        │
    │ 7.540  │ Software development │
    │ 9.399  │ Mobile communication │
    │ 9.400  │ Fixed communication  │
    │ 9.401  │ Fiber-optics         │
    │ 43.641 │ Audit                │
    │ 43.646 │ Insurance            │
    │ 43.647 │ Bank                 │
    └────────┴──────────────────────┘

# CTE y operaciones de conjuntos

Por supuesto, SQLite admite Expresiones de tabla comunes (cláusula `WITH`) y `JOIN`, ni siquiera daré ejemplos aquí. Si los datos son jerárquicos (la tabla se refiere a sí misma a través de una columna como parent_id), `WITH RECURSIVE` será útil. Cualquier jerarquía, por profunda que sea, se puede "desenrollar" con una sola consulta.

    with recursive tmp(id, name, level) as (
      select id, name, 1 as level
      from area
      where parent_id is null

      union all

      select
        area.id,
        tmp.name || ', ' || area.name as name,
        tmp.level + 1 as level
      from area
        join tmp on area.parent_id = tmp.id
    )

    select * from tmp;
    ┌──────┬──────────────────────────┬───────┐
    │  id  │           name           │ level │
    ├──────┼──────────────────────────┼───────┤
    │ 93   │ US                       │ 1     │
    │ 768  │ US, Washington DC        │ 2     │
    │ 1833 │ US, Washington           │ 2     │
    │ 2987 │ US, Washington, Bellevue │ 3     │
    │ 3021 │ US, Washington, Everett  │ 3     │
    │ 3039 │ US, Washington, Kent     │ 3     │
    │ ...  │ ...                      │ ...   │
    └──────┴──────────────────────────┴───────┘

¿Conjuntos? No hay problema: `UNION`, `INTERSECT`, `EXCEPT` están a su servicio.

    select employer_id
    from employer_area
    where area_id = 1

    except

    select employer_id
    from employer_area
    where area_id = 2;

¿Calcular una columna basándose en varias otras? Ingrese las columnas generadas:

    alter table vacancy
    add column salary_net integer as (
      case when salary_gross = true then
        round(salary_from/1.04)
      else
        salary_from
      end
    );

Las columnas generadas se pueden consultar de la misma manera que las 'normales':

    select
      substr(name, 1, 40) as name,
      salary_net
    from vacancy
    where
      salary_currency = 'JPY'
      and salary_net is not null
    limit 10;

# Estadística matemática

¿Estadística descriptiva? Fácil: media, mediana, percentiles, desviación estándar, lo que sea. Tendrá que cargar una extensión, pero también es un solo comando (y un solo archivo).

    .load sqlite3-stats

    select
      count(*) as book_count,
      cast(avg(num_pages) as integer) as mean,
      cast(median(num_pages) as integer) as median,
      mode(num_pages) as mode,
      percentile_90(num_pages) as p90,
      percentile_95(num_pages) as p95,
      percentile_99(num_pages) as p99
    from books;
    ┌────────────┬──────┬────────┬──────┬─────┬─────┬──────┐
    │ book_count │ mean │ median │ mode │ p90 │ p95 │ p99  │
    ├────────────┼──────┼────────┼──────┼─────┼─────┼──────┤
    │ 1483       │ 349  │ 295    │ 256  │ 640 │ 817 │ 1199 │
    └────────────┴──────┴────────┴──────┴─────┴─────┴──────┘

> Nota sobre extensiones. A SQLite le faltan muchas funciones en comparación con otros DBMS como PostgreSQL. Pero son fáciles de agregar, que es lo que hace la gente, por lo que resulta bastante complicado.
> Por lo tanto, decidí hacer un conjunto consistente de extensiones, dividido por área de dominio y compilado para los principales sistemas operativos. Hay pocos de ellos todavía, pero hay más en camino:
> [sqlite-plus @ GitHub](https://github.com/nalgeon/sqlite-plus/)

Más diversión con las estadísticas. Puede trazar la distribución de datos directamente en la consola. Mira qué lindo que es:

    with slots as (
      select
        num_pages/100 as slot,
        count(*) as book_count
      from books
      group by slot
    ),
    max as (
      select max(book_count) as value
      from slots
    )
    select
      slot,
      book_count,
      printf('%.' || (book_count * 30 / max.value) || 'c', '*') as bar
    from slots, max
    order by slot;
    ┌──────┬────────────┬────────────────────────────────┐
    │ slot │ book_count │              bar               │
    ├──────┼────────────┼────────────────────────────────┤
    │ 0    │ 116        │ *********                      │
    │ 1    │ 254        │ ********************           │
    │ 2    │ 376        │ ****************************** │
    │ 3    │ 285        │ **********************         │
    │ 4    │ 184        │ **************                 │
    │ 5    │ 90         │ *******                        │
    │ 6    │ 54         │ ****                           │
    │ 7    │ 41         │ ***                            │
    │ 8    │ 31         │ **                             │
    │ 9    │ 15         │ *                              │
    │ 10   │ 11         │ *                              │
    │ 11   │ 12         │ *                              │
    │ 12   │ 2          │ *                              │
    └──────┴────────────┴────────────────────────────────┘

# Performance

SQLite funciona con cientos de millones de registros. Los `INSERTS` regulares muestran alrededor de 240K registros por segundo en mi computadora portátil. Y si conecta el archivo CSV como una tabla virtual (hay una extensión para eso), las inserciones se vuelven 2 veces más rápidas.

    .load sqlite3-vsv

    create virtual table temp.blocks_csv using vsv(
        filename="ipblocks.csv",
        schema="create table x(network text, geoname_id integer, registered_country_geoname_id integer, represented_country_geoname_id integer, is_anonymous_proxy integer, is_satellite_provider integer, postal_code text, latitude real, longitude real, accuracy_radius integer)",
        columns=10,
        header=on,
        nulls=on
    );
    .timer on
    insert into blocks
    select * from blocks_csv;

    Run Time: real 5.176 user 4.716420 sys 0.403866
    select count(*) from blocks;
    3386629

    Run Time: real 0.095 user 0.021972 sys 0.063716


Existe una opinión popular entre los desarrolladores de que SQLite no es adecuado para la web, porque no admite el acceso concurrente. Esto es un mito. En el modo de registro de escritura anticipada (disponible desde hace mucho tiempo), puede haber tantos lectores simultáneos como desee. Solo puede haber un escritor concurrente, pero a menudo uno es suficiente.

SQLite es perfecto para aplicaciones y sitios web pequeños. [sqlite.org](https://sqlite.org) utiliza SQLite como base de datos, sin preocuparse por la optimización (200 solicitudes por página). Maneja 700K visitas por mes y sirve páginas más rápido que el 95% de los sitios web que he visto.

# Documentos, gráficos y búsqueda

SQLite admite índices parciales e índices en expresiones, como lo hacen los DBMS 'grandes'. Puede crear índices en columnas generadas e incluso convertir SQLite en una base de datos de documentos. Simplemente almacene JSON sin procesar y cree índices con `json_extract()`-ed columns:

    create table currency(
      body text,
      code text as (json_extract(body, '$.code')),
      name text as (json_extract(body, '$.name'))
    );

    create index currency_code_idx on currency(code);

    insert into currency
    select value
    from json_each(readfile('currency.sample.json'));
    explain query plan
    select name from currency where code = 'EUR';

    QUERY PLAN
    `--SEARCH TABLE currency USING INDEX currency_code_idx (code=?)

> También puede usar SQLite como una base de datos gráfica. Un montón de complejos WITH RECURSIVE harán el truco, o tal vez prefiera agregar un poco de Python:
> [simple-graph @ GitHub](https://github.com/dpapathanasiou/simple-graph)

La búsqueda de texto completo funciona desde el primer momento:

    create virtual table books_fts
    using fts5(title, author, publisher);

    insert into books_fts
    select title, author, publisher from books;

    select
      author,
      substr(title, 1, 30) as title,
      substr(publisher, 1, 10) as publisher
    from books_fts
    where books_fts match 'ann'
    limit 5;
    ┌─────────────────────┬────────────────────────────────┬────────────┐
    │       author        │             title              │ publisher  │
    ├─────────────────────┼────────────────────────────────┼────────────┤
    │ Ruby Ann Boxcar     │ Ruby Ann's Down Home Trailer P │ Citadel    │
    │ Ruby Ann Boxcar     │ Ruby Ann's Down Home Trailer P │ Citadel    │
    │ Lynne Ann DeSpelder │ The Last Dance: Encountering D │ McGraw-Hil │
    │ Daniel Defoe        │ Robinson Crusoe                │ Ann Arbor  │
    │ Ann Thwaite         │ Waiting for the Party: The Lif │ David R. G │
    └─────────────────────┴────────────────────────────────┴────────────┘

Quizás necesite una base de datos en memoria para cálculos intermedios? Una sola línea de código Python:

    db = sqlite3.connect(":memory:")

Incluso puede acceder a él desde múltiples conexiones:

    db = sqlite3.connect ("file :: memory:? Cache = shared")

# Y mucho más

Allí son funciones de ventana elegantes (como en PostgreSQL). `UPSERT`, `UPDATE FROM` y `generate_series()`. Índices R-Tree. Expresiones regulares, búsqueda difusa y geo. En términos de características, SQLite puede competir con cualquier DBMS 'grande'.

También hay excelentes herramientas en torno a SQLite. Me gusta especialmente Datasette, una herramienta de código abierto para explorar y publicar conjuntos de datos SQLite. Y DBeaver es un excelente IDE de base de datos de código abierto con soporte para las últimas versiones de SQLite.

Autor original [@ohmypy](https://twitter.com/ohmypy), [artículo original](https://antonz.org/sqlite-is-not-a-toy-database/), comentarios (que vale la pena leer) en [Hacker News](https://news.ycombinator.com/item?id=26580614) 

revisó y publicó @jedux.