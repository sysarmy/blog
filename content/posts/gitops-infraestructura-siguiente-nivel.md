---
Description: "Gitops, infraestructura al siguiente nivel"
Keywords:
- sysadmin 
- sistemas
- consejos
- tips
- gitops
Section: 
Tags:
- sysarmy
- gitops
- kubernetes
- sistemas
- aprender
Thumbnail: assets/gitops-image-0.png
socialImage: assets/gitops-image-0.png
featuredImage: assets/gitops-image-0.png
Title: Gitops, infraestructura al siguiente nivel
Topics:
- sysadmin 
- sistemas
- consejos
- kubernetes
- argo
- continous
markup: markdown
date: 2020-07-03
---

La infraestructura evoluciona y al mismo tiempo trae nuevos desafíos. **¿Puede GitOps ser el nuevo factor determinante en la industria?**

DevOps más allá de un rol, es también una filosofía, en la cual hacer las cosas de la manera más automatizada e incorporando el conjunto de skills propios de Desarrollo y de Operaciones. Esto comenzó hace aproximadamente unos 10 años, con la aparición, primero de [Puppet](https://puppet.com/ "Configuration management") y [Chef](https://www.chef.io/products/automate/), y luego con [Ansible](https://www.ansible.com/). Fue un proceso predecible ya que [DevOps](https://en.wikipedia.org/wiki/DevOps) (y posiblemente también [SRE](https://landing.google.com/sre/)), son en su mayoría una evolución de la antigua posición de System Administrator, que permite adaptar a ellos mismos a un nuevo rol para satisfacer los requisitos de la industria que se va actualizando junto con el paso del tiempo.


<!--more-->

Implementar este conjunto de filosofías que conducen a automatizar las tareas de una compañía no es una tarea sencilla; Requiere coordinación entre los equipos, y modificar como entendemos e interactuamos con el ciclo de vida de las aplicaciones (ALM). Actualmente es natural pensar sobre una aplicación como un conjunto de piezas diferentes orquestadas y trabajando armoniosamente en conjunto.  
Algunos años atrás (no tantos), esto era completamente diferente. Las aplicaciones eran principalmente monolíticas, y permanecían instaladas en los mismos servidores por una enorme cantidad de tiempo (haciendo la recuperación ante incidentes dificultosa y por sobre todas las cosas lenta). Con la aparición de las RESTful API, los microservicios y los proveedores de Cloud todo comenzó a cambiar, modificando el paradigma que veníamos utilizando para desarrollar. 

[Docker](posts/que-es-docker) (o su principio con LXC) en gran parte, fue responsable de comenzar este cambio de pensamiento y metodología. Terminando con largas horas al inicializar un nuevo nodo, instalar paquetes y configurar archivos de texto plano o un algún registro en una base de datos relacional. 

Actualmente, desarrollar una nueva aplicación y ponerla en producción, requiere ejecutar un comando (o hacer click en un botón), para buildear, esperar un par de minutos a que termine, actualizar la imagen en el registro de Docker y finalmente deployar con la posibilidad de tener el mismo artifact ejecutándose en diferentes entornos con variaciones mínimas de la configuración y lo suficientemente testeado. 

En los últimos años hemos comenzado a crear software mucho más confiable, con metodologías ágiles y creando tests automáticos que evitan, en cierta forma el error humano, beneficiando todo el ciclo del desarrollo de software con nuevas herramientas ([Jenkins](https://www.jenkins.io/), [CircleCI](https://circleci.com/), [Travis](https://travis-ci.org/), [Sonar](https://www.sonarqube.org/), Linters) y nuevas metodologías (Testing automation e Integración Continua) pero por su contrapartida, la infraestructura no tuvo el mismo nivel de evolución.

GitOps es una filosofía que está cambiando el paradigma y va a continuar haciéndolo en los próximos años. 10% es en herramientas, y un 90% en filosofía.
Tener infraestructura como código (IaaC) debe ser un objetivo para cualquier equipo de DevOps o SRE.

*Argo CD Es una herramienta declarativa para realizar GitOps continuous delivery en Kubernetes. El componente principal de Argo CD  es el Application Controller que constantemente monitorea las aplicaciones y compara el estado en ejecución de estas contra la declaración del estado deseado, definido en los repositorios.*

![](assets/gitops-image-2.jpeg "Gitops")

## Pero qué es GitOps? 

[Kubernetes](https://kubernetes.io/) ha comenzado una verdadera revolución en la industria. Permitiendo cambiar la forma en que solíamos deployar y buildear infraestructura. GitOps nos desafía a automatizar nuestra infraestructura tanto como podamos, teniendo en cuenta la trazabilidad, y el versionado. 
Convirtiendo a nuestros repositorios en una “Source of Truth” para toda nuestra infraestructura, como también para las aplicaciones.

En este punto, el ciclo de vida del desarrollo y de toda la infraestructura depende en el modelo de “branching”. Algunas empresas prefieren usar “master” como “Source of Truth”, y utilizar “short-lived branches” para el trabajo diario, creando pequeños incrementos (o commits) con los cambios deseados. Otros preservan master, y efectúan deployments sobre release branches, que más tarde se mergearan a master, una vez que la integración del codigo en produccion esta lo suficientemente probada, aumentando la confiabilidad de “master” como unica “Source of Truth”. 

Hay casos, como Microsoft, específicamente con Azure que prefieren utilizar Milestones, que duran exactamente lo que dura un Sprint en el desarrollo de Azure y deployando estos pero a su vez creando branches cada vez que necesitan desplegar un “Hot fix”

Independientemente del modelo de branching, implementar la filosofía GitOps va a llevar al [Sistema de Control de versiones (SCM)](https://git-scm.com/) a un lugar central en la infraestructura, convirtiéndolo en un centro de comando para las operaciones diarias. 

![](assets/gitops-image-1.png "Gitops")

### GitOps se basa en un conjunto de reglas que deben ser seguidas:

#### 1. Descripción declarativa de todos los componentes.

La Infraestructura como Código es un hecho en cualquier organización moderna. Desarrollar infraestructura declarativa nos garantiza que siempre la misma infraestructura va a ser deployada. Esta puede ser alterada (o no) por condiciones específicas al entorno, pero bajo un esquema controlado.  

Kubernetes es un ejemplo bastante bueno de como la infraestructura declarativa puede ser definida. Alterar el comportamiento basado en el entorno es muchas veces necesario debido a la naturaleza donde el software necesita ejecutarse (no existen los mismos requerimientos en un entorno de QA que en uno de Producción). Algunas herramientas como [Helm](https://helm.sh/) pueden realizar estas modificaciones por nosotros proveyendo diferentes declaraciones acorde al entorno donde se necesita ejecutar, aunque siempre tenemos la premisa de escribir código declarativo donde estamos fijando nuestros manifest a versiones/tags/commits específicos y así evitar desplegar cambios no deseados. 

#### 2. El estado deseado debe estar versionado en Git

Existen dos estados diferentes para un cluster: El estado deseado y el estado Canónico. Escribir infraestructura como código puede crear algunos momentos en el tiempo en el cual lo que se encuentra deployado difiere de lo que se declaró en los repositorios (estos “delta” de tiempo pueden durar minutos o pueden existir por largos periodos de tiempo).  

Una de las claves de GitOps es tener al sistema de control de versiones (SCM) como una pieza central de la infraestructura donde sea posible versionar los cambios y alterar el estado del cluster (guiandolo hacia el estado deseado) solamente aprobando y mergeando un Pull-Request y protegiendo nuestro branch master para forzar pasar por el sistema adecuado de aprobaciones y revisión de codigo. El sistema automático de delivery va a llevar gradualmente el cambio que se realizó en el repositorio hasta los entornos deseados. Además de verse beneficiado con la capacidad que tiene Git de reconstruir el historial de commits y poder volver al estado deseado de una manera práctica y sencilla. 

Es una buena práctica mantener dos repositorios, uno para la aplicación y otro para el o los manifest donde cada commit a la aplicación, va a resultar en un nuevo deploy.

#### 3. Solo los cambios aprobados pueden ser aplicados automáticamente

Los cambios en un cluster pueden ser hechos solamente aprobando un Pull-Request. Imaginemos  lo siguiente: Un desarrollador quien está trabajando en una nueva funcionalidad necesita proveer un conjunto de pods ejecutando Redis en Kubernetes. Para esto, el desarrollador edita un archivo YAML (o JSON) en el repositorio, y declara el deployment en Kubernetes que contiene los pods con la versión  elegida de Redis y la cantidad réplicas. Luego este mismo developer crea un Pull-Request a fin de mergear el branch con master. Finalmente, luego de la revisión de arquitectura, el testing y discutir mediantes comentarios en el Pull Request (la misma interfaz de GitHub permite esto), el equipo de SRE analiza y decide mergear el cambio y esto, automáticamente se aplica y provisiona el servicio deseado en cuestión de minutos.

Esto tiene algunas ventajas técnicas y no técnicas. Promueve la discusión a fin de entender otros puntos de vistas u otras soluciones a un problema dado, además de mejorar la experiencia de los desarrolladores reduciendo la complejidad. 

Si vemos algunas de las ventajas técnicas notamos que llevamos nuestro SCM como parte central de la estrategia de deployment de la organización, utilizando todas las características que el mismo provee y realizamos una integración relativamente sencilla. Deployar en este punto solo significa mergear un Pull-Request. Por su parte revertirlo y corregir un estado no deseado es solamente revertir el cambio anteriormente hecho. 

#### 4. Agentes monitorean el estado y alertan en divergencias

**La filosofía GitOps está basada principalmente en las herramientas existentes.** La implementación de nuevas herramientas pasa a ser una etapa opcional aunque seleccionando las  adecuadas podemos sacar provecho de  las mismas de una manera muchas más óptimas. Podemos continuar usando nuestras herramientas de Continuous Integration/Continuous Delivery, nuestro SCM y el mismo registro de Docker a fin de asegurar al clúster en ejecución alcanzar el estado deseado. Hay algunas herramientas que pueden ayudar a alertar y corregir las diferencias en la configuración. Esto convierte al cluster en sí mismo como un agente stateful corriendo externamente o en dentro del mismo cluster. *ArgoCI* puede colaborar a asegurar que el estado deseado matchea exactamente con el estado en ejecución verificando constantemente el SCM y disparando alertas mediante Webhooks.

Las medidas correctivas por sí solas no son suficientes sin observabilidad y monitoreo. Soluciones existentes pueden ser implementadas para medir la disponibilidad del cluster ([NewRelic](https://newrelic.com/), [DataDog](https://www.datadoghq.com/), [SumoLogic](https://www.sumologic.com/)) y alertar las divergencias alertando al equipo de DevOps o SRE cuando ellos necesiten intervenir.

Ciertamente herramientas como [ArgoCI](https://argoproj.github.io/) pueden ayudar a implementar la metodología de GitOps sin demasiado intervención. Probablemente el ciclo de manejo de aplicaciones debe ser rediseñado para soportarlo, pero una vez hecho esto se puede ver reflejado con algunos de los beneficios y mejoras como lo es reducir los tiempos de un deployment, incrementar la productividad y mejorar la estabilidad proveyendo alta disponibilidad, entre otros beneficios.

#### 5. Disaster Recovery

En este punto todos coincidimos en algo: ***A nadie le gusta, ni quiere, estar bajo un incidente y ejecutar un plan de Disaster Recovery, a su vez somos conscientes de que las contingencias suceden.***

Algunas empresas, actualmente, tienen estrictos procedimientos a fin de reducir el MTTR o el MTTA, pero independientemente de la naturaleza del incidente, normalmente necesitamos  la intervención humana para solucionarlo.
Cuando hablamos sobre incidentes relacionados a la infraestructura todo se pone peor dada su propia naturaleza y función clave de cualquier organización. 
Muchas veces tenemos infraestructura muy susceptibles a errores (humanos, o no), y estar constantemente haciendo cambios vuelve las cosas aún peor. Corriendo el riego, en cada uno de estos cambios de tener un recurso no disponible desde minutos hasta horas (o quizás días). Realizar RCAs, luego de los incidentes ayuda a la industria a evitar cometer dos veces el mismo error, pero qué pasa con el tiempo? (las métricas no son menos importantes). Bien, GitOps viene al rescate. 

Tener repositorios versionados con todos los cambios realizados ayuda a SRE o Devops a reducir el tiempo de recuperación ante una contingencia. Lo que antiguamente era volver a deployar diferentes componentes de infraestructura, esperar a que los jobs terminen, configurarlos (manual o automáticamente), entre otras tareas, hoy se ve reducido solamente a identificar qué commit provocó el incidente, revertirlo y esperar a que el cluster matchee con el estado deseado. Herramientas de consolidación como ArgoCI nos ayudan a poder lograr esta difícil tarea con un mínimo esfuerzo de manera automática o mediante una aprobación. 

Si un corte de energía sucede en un datacenter y se pierden todas las instancias, deployar otro cluster en otra región geográfica es posible. Mantener redundancia con herramientas de consolidación es importante para asegurar un escenario  real de alta disponibilidad y a su vez, mejorar la confiabilidad y las métricas. Los cambios en la infraestructura no vienen solos, ellos necesitan ser deployados con tests para garantizar su funcionalidad. Actualmente GitHub,  GitLab, BitBucket o el mismo Jenkins proveen la habilidad de ejecutar “actions” o “pipelines” que pueden ayudarnos a ejecutar diferentes tipos de tests en nuestra infraestructura. 
La trazabilidad de los cambios es fundamental, pero se vuelve mucho más importante si viene acompañada de tests adecuados para conocer el impacto y funcionamiento de cualquier modificación en nuestra infraestructura de base. 

GitOps está recién empezando a dar sus primeros pasos en la industria, pero sin dudas, desarrollar la siguiente generación de sistemas requiere realizar cambios globales en la forma que las compañías están desarrollando software e infraestructura. La automatización se ha convertido en una parte central y la industria se está esforzando para llevarla al siguiente nivel.

Articulo original: [“GitOps, building the next generation infrastructure (Inglés)”](https://www.linkedin.com/pulse/gitops-building-next-generation-infrastructure-facu-de-la-cruz/) 

##### Sobre el autor

**Facu de la Cruz**  Actualmente trabajando para ASAPP Inc. y con más de 12 años de experiencia en la industria cuento con un sólido background en Cloud Computing, Linux, Seguridad y TCP/IP networking.
- [Linkedin](https://www.linkedin.com/in/fmdlc/)
- fmdlc.unix@gmail.com

##### Bibliografía:
- [Argo CD - Declarative GitOps CD for Kubernetes](https://argoproj.github.io/argo-cd/)
- [WeaveWorks - Guide To GitOps](https://www.weave.works/technologies/gitops/)

