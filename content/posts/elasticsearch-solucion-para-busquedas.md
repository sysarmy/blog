---
Title: "Elasticsearch, solución para la busqueda"
Description: "Descubre cómo Elasticsearch permite indexar, buscar y analizar grandes volúmenes de datos en tiempo real, convirtiéndolo en una herramienta esencial para empresas que requieren alta escalabilidad y rendimiento."
Keywords:
- sysarmy
- elasticsearch
- elk
- observability
- logging

Tags:
- sysarmy
- elasticsearch
- elk
- observability
- logging

Thumbnail: assets/elasticesarch-cover.png
socialImage: assets/elasticesarch-cover.png
featuredImage: assets/elasticesarch-cover.png
externalPermlink: "https://blog.devgenius.io/elasticsearch-solution-to-searching-71116220c82f"

Topics:
- elasticsearch
- elk
- observability
- logging

markup: markdown
date: 2024-03-20
draft: false
---
# Un motor de búsqueda y análisis de nivel empresarial

Elasticsearch es un motor de búsqueda de texto completo para nuestros propios datos. Indexa y permite buscarlos a través de una interfaz HTTP. Es un motor de búsqueda distribuido basado en Lucene. Puede escalar a petabytes de datos. Admite multiples usuarios y alta concurrencia. Ofrece resultados de búsqueda casi en tiempo real. Elasticsearch también es un componente de un conjunto de herramientas de código abierto conocido como ELK Stack.
<!--more-->

## Casos de uso de Elasticsearch

- Log operativo y análisis de logs (ELK)
- Contenido de un sitio y búsqueda de media
- Búsqueda de texto completo
- Datos y métricas de eventos
- Visualización de datos con Kibana

## Clúster

![Esquema de elastic](assets/cluster.png)

Un clúster de Elasticsearch es una colección distribuida de nodos en los que cada uno realiza una o más operaciones. Cada nodo ejecuta una instancia de Elasticsearch. El clúster es escalable horizontalmente. Al agregar nodos adicionales al clúster, podemos escalar la capacidad del clúster de manera lineal mientras mantenemos un rendimiento similar. Los nodos se agregan creando y usando un token de enrolamiento.

Los nodos del clúster se pueden diferenciar según el tipo específico de operaciones que realizan. En los clústeres de alta disponibilidad, designamos diferentes conjuntos de nodos para diferentes funciones del clúster. Para definir roles de nodo, podemos establecer la configuración de esta ``` manera:node.roles: [ master | data | ingest ] ```

## Nodo amo

Cada clúster tiene un único nodo amo en cualquier momento y sus responsabilidades incluyen mantener la salud y el estado del clúster. Los nodos amos funcionan como coordinadores para crear, eliminar, administrar índices y asignar índices y fragmentos subyacentes a los nodos apropiados del clúster.

## Nodo elegible-amo

Los nodos elegibles para amos son aquellos candidatos a ser nodos amos.

## Nodo de datos

Los nodos de datos contienen los datos del índice real y manejan la búsqueda y agregación de datos.

## Nodo solo coordinador

Estos nodos transmiten solicitudes de consulta a todos los fragmentos relevantes y agregan sus respuestas en un conjunto ordenado globalmente, que se devuelve al cliente. Estos nodos actúan como equilibrador de carga.

## Nodo de ingesta

Los nodos de ingesta se pueden configurar para preprocesar datos antes de que se ingieran. Como algunos de los procesadores, como el procesador grok, pueden consumir muchos recursos, es beneficioso dedicar nodos separados para la canalización de ingesta, ya que las operaciones de búsqueda no se verán afectadas por el procesamiento de ingesta. De lo contrario, los nodos de datos realizarán esta tarea.

En grandes clústeres de nubes, tendremos un nodo amo dedicado, 2 o más nodos de ingesta, 2 o más nodos de coordinación y múltiples nodos de datos.

Dado que los nodos de datos almacenan los datos, deberían tener discos adjuntos. SSD para datos cálidos y HDD para datos fríos. También necesitamos una gran memoria (RAM) para los nodos de datos, ya que almacenan datos en el buffer.

    > Elasticsearch está escrito en Java y ejecuta procesos en JVM. Utiliza grupos de subprocesos para diferentes procesos.

``` GET /_cat/thread_pool/search?v&h=host,name,active,rejected,completed ```

## Índice

El índice es una colección de tipos similares de documentos. Es una entidad lógica. Físicamente está asignado a fragmentos. El índice está asociado con configuraciones, asignaciones, alias y plantillas.

## Alias ​​de índice

Un alias es un nombre de índice virtual que puede apuntar a uno o más índices. Esto elimina la necesidad de realizar un seguimiento de qué índice específico consultar, en caso de que los datos estén distribuidos entre índices.

![Como se compone un indice](assets/index-aliases.png)

```
GET _cat/aliases?v 
POST _aliases 
{ 
  "acciones" : [ 
    { 
      "agregar" : { 
        "índice" : "índice-1" , 
        "alias" : "alias1"
       } 
    } 
  ] 
}
```

Los alias de índice también ayudan en la migración de índices sin tiempo de inactividad.

## Fragmentos

Los índices se dividen horizontalmente en partes llamadas fragmentos . Los fragmentos son un índice de Lucene independiente. Son los componentes básicos del índice.

Elasticsearch [recomienda](https://www.elastic.co/guide/en/elasticsearch/reference/current/size-your-shards.html#shard-size-recommendation) que cada fragmento tenga menos de 65 GB (AWS [recomienda](https://docs.aws.amazon.com/opensearch-service/latest/developerguide/sizing-domains.html) que tengan menos de 50 GB), por lo que podríamos crear índices basados ​​en el tiempo en los que cada índice contenga entre 16 y 20 GB de datos, lo que proporciona algo de espacio para el crecimiento de los datos.

    > Fragmentos primarios y de replicación

Para obtener los fragmentos de un índiceGET _cat/shards/index

Ciclo de vida del fragmento: Inicializando → Iniciado → Reubicación → No asignado
```
{ 
    "configuración"  :  { 
        "índice"  :  { 
            "número_de_fragmentos"  :  8 , 
            "número_de_réplicas"  :  2 
        } 
    } 
}
```

## Translog/búfer de memoria

Las confirmaciones de Lucene son demasiado costosas para realizar en cada cambio individual, por lo que cada copia de fragmento también escribe operaciones en su registro de transacciones conocido como translog. Cada fragmento tiene un translog. Los datos del translog solo se conservan en un disco con la confirmación de Lucene. En caso de error, esto se repite para confirmar los cambios no guardados. Durante una confirmación, todos los segmentos en la memoria se fusionan en un solo segmento y se guardan en el disco.

![Modelo de persistencia](assets/elasticsearch-persis-model.png)
![Ciclo de vida de un documento](assets/elasticsearch-persis-model2.png)

    > Actualizacion: el contenido del búfer de memoria se copia en un segmento recién creado en la memoria y se borra el translog. Sucede cada segundo.

    > Tirado: los segmentos en memoria se escriben en el disco. Los segmentos más pequeños se fusionan en segmentos más grandes.

## Segmentos

El índice de Lucene se divide en archivos más pequeños llamados segmentos. Los segmentos son un índice invertido y son inmutables. Lucene busca en todos los segmentos de forma secuencial. Por lo tanto, tener muchos segmentos puede afectar el rendimiento. Elasticsearch fusiona los segmentos para crear nuevos segmentos eliminando documentos eliminados. La fusión también ayuda a combinar segmentos más pequeños en segmentos más grandes, ya que los segmentos más pequeños tienen un rendimiento de búsqueda deficiente.

## Documentos

Un documento es una unidad de información que se pasa a Elasticsearch para su almacenamiento. Los documentos son archivos JSON que se almacenan dentro de un índice de Elasticsearch y se consideran la unidad base de almacenamiento. Los documentos son inmutables. En caso de una actualización, el archivo anterior se reemplaza por el nuevo. El campo _version en la respuesta del documento es cosa del pasado y ya no tiene significado.

## Archivos

tipos de datos como binario, booleano, palabra clave, números, fechas, texto, geo_shape, search_as_you_type

## Metacampos

>    _index: nombre del índice
>    _type
>    _id: identificación única del documento
>    _source: documento JSON original antes de aplicar cualquier analizador/transformación.
>    _all : contiene todos los demás campos de su documento

Mapeo indicativo del objeto ES con la base de datos:

> MySQL => Bases de datos => Tablas => Fila => Columna => Índice
> Elasticsearch => Índices => Tipos => Documentos => Propiedades => Mapeo

## Estructuras de datos internas utilizadas por ES

    > Índice invertido: para datos de texto
    > Árbol BKD: datos numéricos, de fecha y geoespaciales
    > doc_values: clasificación y agregaciones

## Analizadores

Elasticsearch proporciona analizadores que definen cómo se debe indexar y buscar el texto. Los analizadores se utilizan durante la indexación para analizar frases y expresiones en sus términos constitutivos. Definido dentro de un índice, un analizador consta de un único tokenizador y cualquier número de filtros de tokens.

![Analizadores](assets/analyzers.png)

El analizador tiene tres componentes:

    - Filtros de caracteres(html_strip)
    - Tokenizador(standard)
    - Filtro de tokens(lowercase)

Elasticsearch tiene muchos analizadores, tokenizadores y filtros de tokens integrados.
```
POST /_analyze 
{ 
  "texto" : "Este texto será analizado con el analizador ESTÁNDAR" 
  "analizador" : "estándar"
 } 

POST /_analyze 
{ 
  "texto" : "Este texto será analizado con el analizador ESTÁNDAR" 
  "char_filter" : [] , 
  "tokenizer" : "estándar" , 
  "filtro" : [ "minúsculas" ] 
}
```

## Plantilla de índice

Una plantilla de índice es un esqueleto mediante el cual se crea un nuevo índice.

## Gestión del ciclo de vida del índice

Cada índice pasa por diferentes fases (caliente → tibio → frío → eliminado). Según una configuración predefinida, ILM modelará los índices de una fase a otra.

![ciclo de un indice](assets/index-lifecycle.png)


## Canalización de ingesta

Los canales de ingesta nos permiten aplicar transformaciones como eliminación de campos , extracción de información o incluso enriquecimiento de datos antes de indexar un documento. Una canalización consta de varias tareas configurables conocidas como procesadores . Elasticsearch almacena las canalizaciones como una estructura de datos interna en el estado del clúster.

```
GET _nodes/ingest?filter_path=nodes.*.ingest.processors 
PUT _ingest/pipeline/blog-demo-pipeline 
{ 
  "versión" : 1, 
  "descripción" : "Canalización de demostración para blog mediano" , 
  "procesadores" : [ {
     " 
      set" : { 
        "descripción" : "Establecer valor predeterminado de etiqueta" , 
        "campo" : "StoryTag" , 
        "valor" : "Ingeniería de datos"
       } 
    }, 
    { 
      "minúsculas" : { 
        "campo" : "autor"
       } 
    } , 
    { 
      "eliminar" : { 
        "campo" : "lecturas_externas"
       } 
    } 
  ] 
} 

POST _ingest/pipeline/blog-demo-pipeline/_simulate 
{ 
  "docs" : [ 
    {...} 
  ] 
} 
POST usuarios /_doc?pipeline= blog-demo-pipeline 
{...} 

POST _reindex 
{ 
  "fuente" : { 
    "índice" : "nombre de índice existente"
   }, 
  "destino" : { 
    "índice" : "nuevo nombre de índice" , 
    "tipo_op" : "crear " , 
    "pipeline" : "blog-demo-pipeline"
   } 
}
```
## Replicación de datos

![Replicacion de datos](assets/data-replication.png)

Elasticsearch tiene conceptos de fragmento primario y fragmento de réplica .

El proceso de replicar datos del fragmento primario al fragmento de réplica se llama replicación de datos. La consideración principal de la replicación de datos es el retraso ( lag ) de la réplica y el primario. Si Lag es siempre 0, entonces se trata de una replicación en tiempo real con la mayor confiabilidad. Elasticsearch implementa la replicación de datos con la ayuda de la replicación de documentos y la replicación de segmentos .

## Indexación de documentos

Los datos de entrada a Elasticsearch se analizan y tokenizan antes de almacenarlos. Normalmente, la biblioteca de Lucene solo almacena los tokens analizados. Elasticsearch también almacena el documento original tal como se recibió en un campo especial llamado `_source`. Aunque consume espacio de almacenamiento adicional, el campo `_source` es fundamental para proporcionar la funcionalidad de actualización de documentos y también es necesario para las operaciones de reindexación.

## Enrutamiento de documentos

Elasticsearch utiliza un algoritmo de enrutamiento para distribuir nuestros documentos a los fragmentos subyacentes durante la indexación. Cada uno de los documentos se indexará en un solo fragmento primario. Los documentos están distribuidos uniformemente, por lo que no hay posibilidad de que uno de los fragmentos se sobrecargue.

El algoritmo de enrutamiento es una fórmula simple en la que Elasticsearch deduce el fragmento de un documento durante la indexación o la búsqueda:

```
shard = hash ( id ) % número_de_fragmentos
```

La función hash espera una identificación única, generalmente una identificación de documento o incluso una identificación personalizada proporcionada por el usuario.

Nota: Los documentos no se recuperan del fragmento principal, pero ES aprovecha la Selección de réplica adaptable (ARS) para seleccionar un fragmento del grupo de replicación.

## El flujo de solicitudes de índice en ES

1.La solicitud es recibida por un nodo coordinador.
2.El nodo enruta documentos a sus índices y fragmentos.
3.Los fragmentos primarios y de réplica escriben (en paralelo) los documentos en translog.
4.Los documentos se normalizan (mapeo y análisis) y se almacenan en un búfer en memoria.
5.Los índices se actualizan para que se puedan realizar búsquedas.
6.Lucene confirma nuevos segmentos en los discos.

## Búsqueda de documentos

> Fase de consulta : el nodo coordinador enruta la solicitud a todos los fragmentos del índice. Los fragmentos, de forma independiente, realizan búsquedas y crean una cola de prioridad de los resultados ordenados por puntuación de relevancia. Todos los fragmentos devuelven los ID de los documentos coincidentes y las puntuaciones relevantes al nodo coordinador. El nodo coordinador crea una nueva cola de prioridad y ordena los resultados globalmente. El nodo coordinador crea una cola de prioridad que ordena los resultados de todos los fragmentos y devuelve los 10 resultados principales.
> Fase de recuperación : los nodos coordinadores solicitan los documentos originales de los fragmentos. Los fragmentos enriquecen los documentos y los devuelven al nodo coordinador.
> Guardado de documentos : frecuencia de plazo (TF), frecuencia inversa de documento (IDF), norma. relevance_score = TF * IDF. Podemos adjuntar un indices_boost objeto al mismo nivel que el objeto de consulta. Esto aumentará la precedencia del índice impulsado. Ahora ES utiliza el algoritmo Okapi BM25 para calcular la relevancia.

Existen varios tipos de predicados de consultas de búsqueda:

> Término,
> Los identificadores de términos
> existen comodines
de rango Prefijo expresión regular match_phrasse, multi_match, match_all sinónimos difusos

## Filtro vs contexto de consulta

El contexto del filtro proporciona una respuesta Sí/No en la coincidencia con la consulta proporcionada. Los filtros se almacenan en caché de forma predeterminada y no contribuyen a la puntuación de relevancia del documento. Sin embargo, el contexto de consulta muestra qué tan bien coincide cada documento con la consulta. Hace uso de analizadores para tomar una decisión. Los resultados incluyen una puntuación de relevancia.

A menos que sea una búsqueda de texto completo o un tipo de búsqueda de puntuación de relevancia, se recomienda la búsqueda de contexto de filtro. Los filtros son generalmente más rápidos en comparación con las consultas.

## Enfoques de paginación

- from / size : el fromparámetro define la cantidad de elementos que queremos omitir desde el principio. El sizeparámetro es el número máximo de visitas que se devolverán.
- API _scroll : se utiliza para recuperar una gran cantidad de resultados. Se parece a los cursores de las bases de datos SQL. No recomendado para solicitudes de usuarios. Debe usarse en modo por lotes.
- buscar_después
- Punto en el tiempo (PIT)

## Agregación

> Agregación de métricas: suma, mín., máx., promedio.
> Agregados de métricas numéricas/no numéricas.
> Agregados de depósitos: ordena los resultados de la consulta en un grupo.
> Agregados de canalización: canaliza el agregado de una etapa a otra.

## Flujo de datos

Los flujos de datos simplifican el manejo de datos de series temporales. Maneja alias de índice de sustitución e índices, y define asignaciones y configuraciones comunes para los índices de respaldo. Aprovecha las políticas de Index Statement Management (ISM).

## Configuraciones

> Flush_threshold_size
> índice_buffer_size
> actualizar_intervalo
> threadpool.bulk.queue_size

## Instalación en K8

```
helm repo add bitnami https://charts.bitnami.com/bitnami
# helm repo add elastic https://helm.elastic.co
helm install elasticsearch --set master.replicas=3,coordinating.service.type=LoadBalancer bitnami/elasticsearch
kubectl port-forward svc/elasticsearch-master 9200
curl localhost:9200
```

Nota: ES utiliza 9200 para API y búsqueda, 9300 para comunicación entre nodos.

## Operadores de K8

```
# Elastic
kubectl create -f https://download.elastic.co/downloads/eck/2.5.0/crds.yaml
kubectl apply -f https://download.elastic.co/downloads/eck/2.5.0/operator.yaml

# opensearch
helm repo add opensearch-operator https://opster.github.io/opensearch-k8s-operator/
helm install opensearch-operator opensearch-operator/opensearch-operator
```

Trabajando con Python

```
# pip install elasticsearch
# pip install opensearch-py 

from elasticsearch import Elasticsearch 
from elasticsearch import helpers
import pandas as pd

df = (
    pd.read_csv("wiki_movie_plots_deduped.csv")
    .dropna()
    .sample(5000, random_state=42)
    .reset_index()
)
 
url = 'http://root:root@localhost:9200'  
es = Elasticsearch(url)  
# es = Elasticsearch([{'host': 'localhost', 'port': 9200}])

mappings = {
        "properties": {
            "title": {"type": "text", "analyzer": "english"},
            "ethnicity": {"type": "text", "analyzer": "standard"},
            "director": {"type": "text", "analyzer": "standard"},
            "cast": {"type": "text", "analyzer": "standard"},
            "genre": {"type": "text", "analyzer": "standard"},
            "plot": {"type": "text", "analyzer": "english"},
            "year": {"type": "integer"},
            "wiki_page": {"type": "keyword"}
    }
}

index_name = "movies"


index_exists = es.indices.exists(index = index_name)

if not index_exists:  
  es.indices.create(index = index_name, mappings = mapping, ignore=400)

# curl -XGET [http://localhost:9200/retail_store]
docs = []
for i, row in df.iterrows():
    doc = {
        "title": row["Title"],
        "ethnicity": row["Origin/Ethnicity"],
        "director": row["Director"],
        "cast": row["Cast"],
        "genre": row["Genre"],
        "plot": row["Plot"],
        "year": row["Release Year"],
        "wiki_page": row["Wiki Page"]
    }
    docs.append(doc)
            
helpers.bulk(es, docs, index=index_name, doc_type='_doc')

query = {  
  "query" : {  
    "bool" : {  
      "must" : {  
         "match_phrase" : {  
            "cast" : "jack nicholson",
         }  
      },
      "filter": {"bool": {"must_not": {"match_phrase": {"director": "roman polanski"}}}},  
    }  
  }  
}

results = es.search(index=index_name, body=query, size = 20)

# get all hits
# helpers.scan(client=es, query=query, index=index_name) 

es.delete(index = index_name, id = doc_id)
# es.delete_by_query(index = index_name, query = query)

es.indices.put_settings(index=index_name, body={"key": "value"})

es.indices.delete(index='movies')
```

La configuración incluye propiedades específicas del índice, como la cantidad de fragmentos, analizadores, etc. El mapeo se utiliza para definir cómo se supone que se almacenan e indexan los documentos y sus campos. Definimos los tipos de datos para cada campo o utilizamos mapeo dinámico para campos desconocidos.

Nota: Para las API masivas, mientras trabaja con cURL utilice elContent-Type: application/x-ndjson

## Indexación por niveles

Elasticsearch nos permite tener diferentes niveles y, por tanto, diferentes perfiles de hardware para los nodos de datos. Lo hacemos estableciendo el node.roleatributo en el elasticsearch.ymlarchivo de configuración.

    > Caliente — data_hot
    > Tibio — data_warm
    > Frío — data_cold
    > Congelado — data_frozen

![organizacion de los indices](assets/tiered-indexing.png)

## API básicas

```
POST <index-name>/_search?explain=true
GET <index1>,<index2>,<index3>/_search 
GET /_cluster/health
GET /_cat/indices?h=index
GET index/_settings
GET index/_mapping
DELETE /document-index/_doc/id
POST document-index/_delete_by_query?conflicts=proceed
{
 "query": {
 "match_all": {}
 }
}
GET /_analyze
{
  "analyzer" : "standard",
  "text" : "Hello, from Elastic Search."
}
```

## Interactuando con spark

```
# via package
--packages org.elasticsearch:elasticsearch-hadoop:7.10.1
# or via pip
!pip install elasticsearch-hadoop

df = spark.read
    .format("org.elasticsearch.spark.sql")
    .option("es.nodes","http://host:9200")
    .option("es.read.metadata", "true")
    .option("es.read.field.include", "text,user")
    .load("index/type")

df.write
    .format("org.elasticsearch.spark.sql")
    .option("es.nodes","http://localhost:9200")
    .option("es.write.operation", "upsert")
    .save("index/type")
```

## Herramientas de administración de Elasticsearch

(cerebro)[https://github.com/lmenezes/cerebro]

## Personalización de Elasticsearch con complementos

Elasticsearch tiene una arquitectura de complemento que permite ampliar y personalizar la funcionalidad. Los complementos son generalmente archivos de artefactos empaquetados (jar, zip, rpm) que se guardan en una ubicación específica. Podemos utilizar elasticsearch-pluginla herramienta de línea de comandos para instalar, enumerar y eliminar complementos. Algunas categorías de complementos comunes son:

> Complemento de extensión API 
> Complemento de snapshots 
> Complemento de discovery 
> Complemento de mapeo
> Complemento de integración

`GET _cat/complements`

## Empresas que utilizan Elasticsearch

    Swiggy, Quora, AutoDesk, Adobe, Walmart, Grab, Tinder, Uber, Visa, Compass, Pearson, Pinterest, Wikimedia, Netflix

## Cuellos de botella

- Administrador de clústeres : a medida que el número de nodos supera los 300, el sistema se vuelve lento y el reinicio del clúster se vuelve lento.
- Asignador de fragmentos
- Sin controlador de admisión para consultas incorrectas : sin prevención proactiva para consultas incorrectas
- El costo de almacenamiento se vuelve alto para una mayor retención de datos
- Acoplamiento directo entre complemento y núcleo , sin segmentación de recursos
- Elasticsearch no permite la instalación en múltiples centros de datos.

## Oferta de nube en AWS

AWS ofrece el servicio OpenSearch, que es un fork de Elasticsearch. Hay dos ofertas en este servicio: administrado y serverless. La oferta de AWS tiene las siguientes ventajas:
> Alertas de seguridad mejoradas
> Analizador de rendimiento
> Compatibilidad con consultas SQL
> Gestión de índices
> Búsqueda de vecino k-más cercano

## Trabajos futuros en proceso para OpenSearch
> Almacenamiento remoto
> Almacenamiento en caché inteligente
> Replicación cruzada y completa del clúster

## Resumen

En pocas palabras, la indexación de ES se puede resumir en los siguientes pasos

- Envío de datos a API
- Los datos se enrutan al índice, al nodo y al fragmento
- Mapeo, normalización y análisis
- Persistencia al disco
- Datos disponibles para buscar

Gracias por leer !!

* Traducción, revisión y publicación colaborativa de @vmariano, @nachichurri.
* articulo original: https://blog.devgenius.io/elasticsearch-solution-to-searching-71116220c82f
