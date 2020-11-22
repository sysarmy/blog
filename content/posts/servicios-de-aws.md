---
Description: "Un repaso de los servicios de AWS"
Keywords:
- aws
- cloud
Section: 
Tags:
- aws
- cloud
Thumbnail: assets/aws-services.png
socialImage: assets/aws-services.png
featuredImage: assets/aws-services.png
Title: Un repaso de los servicios de AWS
Topics:
- aws
- cloud
markup: markdown
date: 2020-11-23
---

Amazon Web Services [Publicado el 20/05/2020](https://adayinthelifeof.nl/2020/05/20/aws.html)

Frecuentemente, me encuentro usando Amazon Web Services (AWS) como mi “nube”. No sólo para mis propios proyectos, sino que casi todos los clientes para los que trabajo usan Amazon para alojar sus aplicaciones. Con el paso del tiempo sumás mucha experiencia en AWS: sabés cómo configurar (correctamente) VPC’s, cuando usar ECS, EC2 o un lambda para alojar código e incluso servicios como S3, SNS y SQS ya no son un desafío.

Pero hay muchos servicios de AWS disponibles. Y me refiero a: MUCHOS. Actualmente, hay 163 (!) servicios diferentes disponibles desde el Amazon Dashboard, cada uno con su propio funcionamiento, dificultades, problemas y mejores prácticas.

<!--more-->

# Descubriendo AWS

Puede que te des cuenta que es probablemente imposible profundizar en cada servicio y entender completamente cómo funcionan y realmente, no necesitas saber realmente los detalles exactos. Pero tener un entendimiento básico sobre cada servicio puede ser un gran beneficio como programador, arquitecto o administrador. Hace más fácil encontrar una solución preexistente para tu problema.

Por eso, me metí en todos y cada uno de los servicios para averiguar exactamente qué hacen y cómo funcionan a un nivel básico. Intenté experimentar con la mayor cantidad de componentes posible (si el tiempo y el dinero lo permitían, no quería gastar 15000 USD en AWS Data Exchange). Intenté capturar qué hace el servicio en una sola línea para darte una panorama general.

Creo que la mayoría de las descripciones son lo suficientemente correctas pero si tenés alguna sugerencia o corrección, por favor avisanos.


### Cómputo
* **EC2**: Servidores virtuales privados.
* **Lightsail**: Proveedor de hosting de Amazon (VPS, DNS, Almacenamiento).
* **Lambda**: Funciones que se pueden ejecutar en Python, NodeJS, Go, etc. Pueden ejecutarse varias en paralelo.
* **Batch**: Ejecutar software jobs en contenedores de Docker sobre máquinas EC2.
* **Elastic Beanstalk**: Ejecutar software en máquinas virtuales administradas.
* **Serverless Application Repository**: Repositorio de apps serverless que se pueden desplegar (en Lambda).
* **AWS Outposts**: Ejecutar servicios de Amazon en tu propio datacenter.
* **EC2 Image Builder**: Crear imágenes EC2 automáticamente.

### Almacenamiento

* **S3**: Almacenamiento de archivos / objetos. No se utiliza principalmente para montaje de sistema de archivos, pero podés descargar archivos directamente a través de HTTP.
* **EFS**: NFS. Montar discos de red a tus máquinas.
* **FSx**: Sistemas de archivos Windows / Lustre que se pueden conectar a máquinas EC2.
* **S3 Glacier**: Sistema de almacenamiento de bajo costo para backups y similares.
* **Storage Gateway**: iSCSI para conectar S3 a tu propia máquina (remota).
* **AWS Backup**: Creación de backups automáticos de diferentes servicios de AWS (EC2, RDS, etc).

### Containers

* **Elastic Container Registry**: Almacenar imágenes de Docker (Similar a DockerHub).
* **Elastic Container Service**: Ejecutar contenedores, tanto en tus máquinas EC2 o en máquinas administradas llamadas Fargate.
* **Elastic Kubernetes Service**: Kubernetes as a service.

### Bases de Datos

* **RDS**: Bases de datos administradas (PostgreSQL, MySQL, etc).
* **DynamoDB**: Base de datos no relacional grande y escalable.
* **ElastiCache**: Máquinas Memcache y Redis administradas.
* **Neptune**: Base de datos de grafos.
* **Amazon Redshift**: Almacena muchos datos que pueden ser procesados a través de streams (Warehousing).
* **Amazon QLDB**: Base de datos para información inmutable y criptográficamente verificable (Transacciones monetarias, etc).
* **Amazon DocumentDB**: Clon de MongoDB (ya no es compatible).
* **Amazon Keyspaces**: Clon de Apache Cassandra administrado.

### Migración y transferencia

* **AS Migration Hub**: Migrar cosas desde tu DC a AWS.
* **Application Discovery Service**: Descubrir servicios en tu datacenter.
* **Database Migration Service**: Migrar DBs a RDS mientras las mantiene online (También puede convertir estructuras).
* **Server Migration Service**: Migrar VMs a Amazon.
* **AWS Transfer Family**: Servicio (s)FTP con S3 como backend. Subir a un FTP, almacenar directamente en un S3.
* **Snowball**: Obtené una máquina de AWS, conectala a tu DC, transferí información a AWS, devolvé la máquina.
* **DataSync**: Sincronizar información entre tu DC y AWS.

### Redes y entrega de contenido

* **VPC**: Crear tus propias VPNs dentro de AWS.
* **CloudFront**: CDN.
* **Route 53**: Administrar DNS.
* **API Gateway**: Crear APIs HTTP y conectarlas a diferentes backends.
* **Direct Connect**: Crear una conexión (física) entre vos (o tu DC) y AWS.
* **AWS App Mesh**: Ejecutar automáticamente Envoy como soporte para tus containers (ECS o EKS).
* **AWS Cloud Map**: Descubrimiento de servicios para tus contenedores.
* **Global Accelerator**: Ejecutar tu app en edge locations para que estén más cerca de tus clientes (CDN para apps).

### Developer Tools

* **CodeStar**: Desarrollar apps rápidamente usando plantillas y CodeCommit, CodeBuild, etc.
* **CodeCommit**: Repositorios de código (Amazon’s git).
* **CodeBuild**: Servicio de CI.
* **CodeDeploy**: Servicio de deployment.
* **CodePipeline**: Entrega de código con flujos de trabajo.
* **Cloud9**: IDE Online.
* **X-Ray**: Permite trazabilidad de tus apps, soporta Python, NodeJS, Go, etc.

### Robotics

* **AWS RoboMaker**: Solución en la nube para programadores de robótica que permite simular, testear y deployar apps robóticas de manera segura.

### Customers Enablement

* **AWS IQ**: Tablero de trabajo: Contratar expertos en AWS para lo que necesites.
* **Support**: Centro de soporte de AWS.
* **Managed Services**: Dejar que AWS maneje tus servicios de AWS.

### Blockchain

* **Amazon Managed Blockchain**: Cadenas de bloques

### Satellite

* **Ground Station**: Radios de tiempo compartido y grandes antenas apuntando al espacio.

### Quantum Technologies

* **Amazon Braket**: Amazon Braket es un servicio de informática cuántica totalmente administrado que ayuda a los investigadores y desarrolladores a iniciarse en la tecnología para acelerar la investigación y el descubrimiento.

### Management & Governance


* **AWS Organizations**: Configurar (sub) organizaciones y cuentas.
* **CloudWatch**: Logging de varios componentes de AWS.
* **AWS Auto Scaling**: Escalar recursos basado en inputs y reglas personalizadas.
* **CloudFormation**: Plantillas para crear y configurar componentes de AWS (Terraform/sls).
* **CloudTrail**: Encontrar quién hizo qué en tus servicios de AWS.
* **Config**: Auditar las configuraciones de tus servicios de AWS.
* **OpsWorks**: Usar Ansible para automatizar cosas.
* **Service Catalog**: Administrar una lista de ítems/códigos que tenes en la nube.
* **Systems Manager**: Ver información de tus recursos agrupada de la manera que quieras (P. ej: específica de cada app)
* **AWS AppConfig**: Almacenar y publicar configuraciones de apps.
* **Trusted Advisor**: Comprueba tu cuenta en busca de problemas (costo, performance, seguridad, etc).
* **Control Tower**: Administrar muchas cuentas.
* **AWS License Manager**: Administrar licencias.
* **AWS Well-Architected Tool**: Generar cuestionarios sobre tu arquitectura para ver si se siguen buenas prácticas.
* **Personal Health Dashboard**: StatusPage para AWS.
* **AWS Chatbot**: Conectar AWS a Slack.
* **Launch Wizard**: Deployar MSSQL o SAP
* **AWS Compute Optimizer**: Encuentra tus recursos y te aconseja sobre cómo ahorrar dinero.

### Media Services

* **Elastic Transcoder**: Encoding de archivos almacenados en S3 a otros formatos
* **Kinesis Video Streams**: Capturar streams de video.
* **MediaConnect**: https://aws.amazon.com/mediaconnect/ 
* **MediaConvert**: Convertir videos en diferentes formatos.
* **MediaLive**: Compartir videos en vivo con otras personas.
* **MediaPackage**: https://aws.amazon.com/mediapackage/ 
* **MediaStore**: https://aws.amazon.com/mediastore/ 
* **MediaTailor**: Insertar anuncios en tus emisiones.
* **Elemental Appliances & Software**: Crear videos on-premise. Básicamente un mix de todos los anteriores servicios (Probablemente sea costoso). 

### Machine Learning

* **Amazon SageMaker**: Herramientas de ML.
* **Amazon CodeGuru**: Optimizar código Java con ML.
* **Amazon Comprehend**: Entender y clasificar información como emails, tweets, etc.
* **Amazon Forecast**: Crear pronósticos en base a la información.
* **Amazon Fraud Detector**: Detección de fraude mediante ML. https://aws.amazon.com/fraud-detector/ 
* **Amazon Kendra**: Servicio de búsqueda que permite hacer preguntas.
* **Amazon Lex**: Crear bots de chat y voz.
* **Amazon Machine Learning**: Deprecado. Utilizar SageMaker.
* **Amazon Personalize**: Crear recomendaciones personalizadas basadas en datos (mahout??).
* **Amazon Polly**: Convertir texto a discursos en diferentes lenguajes.
* **Amazon Rekognition**: Reconocer objetos y personas en imágenes.
* **Amazon Textract**: Convertir texto encontrado en imágenes (OCR).
* **Amazon Transcribe**: Convertir audio a texto.
* **Amazon Translate**: Traducir texto de un lenguaje a otro.
* **AWS DeepLens**: Una cámara que hace machine learning.
* **AWS DeepRacer**: Una especie de juego en el que se programa un auto de carreras para que compita con otros.
* **Amazon Augmented AI**: Permite meter personas en el proceso de aprendizaje de la AI.
* **AWS DeepComposer**: Música generada por computadora. Es tan horrible como suena. (Doy fe)

### Analytics

* **Athena**: Consultar información almacenada en S3.
* **EMR**: Elastic Map/Reduce.
* **CloudSearch**: Sistema de búsqueda de documentos de AWS (Como Elasticsearch).
* **Elasticsearch Service**: Elasticsearch as a service.
* **Kinesis**: Recopilar grandes cantidades de información para hacer analytics (Como ELK).
* **QuickSight**: Servicio de BI.
* **Data Pipeline**: Mover y transformar datos a DynamoDB, RDS, S3, etc.
* **AWS Data Exchange**: Encontrar APIs que podes consumir, puede ser bastante costoso.
* **AWS Glue**: Servicio de ETL. Enriquecer, validar datos.
* **AWS Lake Formation**: Crear data lakes.
* **MSK**: Kafka as a service.

### Security, Identity, & Compliance


* **IAM**: Sistema de permisos de AWS que controla usuarios y servicios de AWS.
* **Resource Access Manager**: Compartir ciertos recursos de AWS como Route53, licencias, EC2 con otras cuentas.
* **Cognito**: Sistema de administración de usuarios y contraseñas. Útil para administrar los usuarios de tus apps.
* **Secrets Manager**: Key/value store de secretos. Puede rotar secretos automáticamente.
* **GuardDuty**: Encontrar automáticamente tus logs de CloudTrail/VPC en busca de amenazas.
* **Inspector**: Encontrar automáticamente problemas (de seguridad) en tus redes y máquinas.
* **Amazon Macie**: Analizar información de tus S3 y buscar datos PII.
* **AWS Single Sign-On**: Permitir SSO en tus apps.
* **Certificate Manager**: Administrar e incluso crear certificados SSL gratuitos.
* **Key Management Service**: Administra claves secretas.
* **Cloud HSM**: Módulos de seguridad de hardware. Permite generar y operar con claves criptográficas.
* **Directory Service**: Active Directory as a service.
* **WAF & Shield**: Firewall de aplicaciones web (para load balancers, Cloudfront, API Gateway). Permite configurar tus propias reglas o usar unas predefinidas.
* **AWS Firewall Manager**: Administrador de firewall para diferentes cuentas en tu organización.
* **Artifact**: Documentos para cloud compliance (Certificación 27001, etc).
* **Security Hub**: Revisor de seguridad general que utiliza GuardDuty, Inspector, Macie, etc.
* **Detective**: Registrar problemas de seguridad encontrados (en Security Hub, etc).

### Mobile

* **AWS Amplify**: Dejar que AWS genere aplicaciones (frontend y backend) y las deploye automáticamente.
* **Mobile Hub**: Ahora parte de AWS Amplify.
* **AWS AppSync**: Crear API backends a los que te podes conectar. Pueden ser creados a través de Amplify.
* **Device Farm**: AWS BrowserStack. Probar apps en diferentes dispositivos móviles y navegadores.

### AR & VR

* **Amazon Sumerian**: Motor y Editor 3D para prototipado rápido de experiencias AR/VR y 3D.

### Application Integration

* **Step Functions**: Máquinas de estado escritas en el lenguaje de Amazon.
* **Amazon AppFlow**: Conecta apps automáticamente (Zapier?). Por ejemplo: Slack con S3. 
* **Amazon EventBridge**: Una especie de sistema eventbus.
* **Amazon MQ**: ActiveMQ
* **Simple Notification Service**: Sistema de notificaciones que puede notificar a través de emails, API endpoints, SMS, etc.
* **Simple Queue Service**: Sistema de colas de mensajes.
* **SWF**: Crear flujos de trabajo.

### AWS Cost Management

* **AWS Cost Explorer**: Muestra una vista general y proyección de tus presupuestos.
* **AWS Budgets**: Crear presupuestos para tus componentes de AWS.
* **AWS Marketplace Subscriptions**: Encontrar (y comprar) AMI’s con software instalado.

### Customer Engagement

* **Amazon Connect**: Plataforma de callcenter de AWS.
* **Pinpoint**: Crear emails, SMS o llamadas de voz transaccionales basadas en plantillas.
* **Simple Email Service**: Enviar emails. Proveedor de emails.

### Business Applications

* **Alexa for Business**: Conectar Alexa a tus necesidades de negocio.
* **Amazon Chime**: Alternativa a Zoom de AWS. 
* **WorkMail**: Alternativa a Gmail / Calendar de AWS.

### End User Computing

* **WorkSpaces**: Escritorios virtuales de Windows o Linux.
* **AppStream 2.0**: Transmitir aplicaciones ejecutándose nativamente hacia tu navegador.
* **WorkDocs**: Almacenar tus documentos y administrarlos online.
* **WorkLink**: Conectar usuarios móviles a tu intranet.

### Internet Of Things

* **IoT Core**: Administrar flotas de dispositivos IoT a través de un broker MQTT.
* **FreeRTOS**: Sistema operativo RTOS para microcontroladores para conectar automáticamente a IoT Core o Greengrass.
* **IoT 1-Click**: Administrar botones 1-Click que pueden  ser conectados a otros sistemas como Lambda.
* **IoT Analytics**: Limpieza y guardado de mensajes en un data store para analytics.
* **IoT Device Defender**: Detectar problemas no deseados en tus dispositivos y tomar medidas.
* **IoT Device Management**: Organizar dispositivos IoT en grupos, programar trabajos en los dispositivos y configurar acceso remoto.
* **IoT Events**: Monitorear telemetría de los dispositivos y luego disparar otros servicios de AWS o trabajos en los mismos dispositivos.
* **IoT Greengrass**: Un message broker que puede almacenar los mensajes en un buffer para grupos de hasta 200 dispositivos, que pueden comunicar y procesar información localmente si la conectividad a IoT Core es intermitente.
* **IoT SiteWise**: Recolectar, organizar, analizar y visualizar información de equipos industriales a escala.
* **IoT Things Graph**: Diseñador similar a Cloudformation para graficar cómo se deberían comunicar los dispositivos con otros servicios de AWS.

### Game Development

* **Amazon GameLift**: Deployar servidores de juegos con baja latencia en AWS.

Gracias a Brian Thomas Smith por llenar los espacios en blanco sobre IoT. Gracias a todos los demás de #HN quienes sugirieron cambios y actualizaciones en los diferentes servicios.

# Conclusión

Con más de 150 servicios corriendo en Amazon AWS, es prácticamente imposible ser un experto en todos ellos. Y eso está bien: cuando te ocupas de grandes clusters EKS o ECS, las probabilidades de que toques servicios IoT son nulas. He encontrado que la mayoría de los servicios están muy bien explicados y son fáciles para comenzar.

Uno de los mayores problemas son los servicios de IoT: Ya que no tengo experiencia con dispositivos inteligentes, MQTT o IoT en general, finalmente configurar una simple aplicación en Go para que se conecte a IoT-Core, y conecte diferentes reglas, pipelines, analytics, etc a ella. Aún así no queda muy claro qué es lo que realmente hacen los diferentes servicios. Con suerte habrá expertos IoT de AWS para iluminarme.

- [Artículo original](https://adayinthelifeof.nl/2020/05/20/aws.html) de [Joshua Thijssen](https://adayinthelifeof.nl/about-me/)
- Traducción y ajuste [marcorichetta](https://github.com/marcorichetta) [#27](https://github.com/sysarmy/disneyland/issues/27)
