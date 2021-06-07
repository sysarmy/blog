---
title: "AWS Account Hardening"
date: 2021-06-02T00:06:00-03:00
draft: true
description: "Unos cuantos consejos para reforzar la seguridad de tus cuentas en AWS."
thumbnail: assets/aws-account-hardening.png
socialImage: assets/aws-account-hardening.png
featuredImage: assets/aws-account-hardening.png
---

Un [artículo original](https://github.com/sercasti/aws-hardening) de [sercasti](https://github.com/sercasti/)

## Tabla de contenidos

1. [Configuración inicial para reforzar la seguridad de tu cuenta]({{< relref "/posts/aws-account-hardening.md#inicial" >}})
2. [Medidas adicionales que serán útiles]({{< relref "/posts/aws-account-hardening.md#adicional" >}})
3. [Qué hacer si tu cuenta ha sido comprometida]({{< relref "/posts/aws-account-hardening.md#comprometido" >}})
4. [Periódicamente]({{< relref "/posts/aws-account-hardening.md#periodicamente" >}})

## Configuración inicial para reforzar la seguridad de tu cuenta: {id=inicial}

- [Habilita la autenticación multifactor (MFA) en el usuario root](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_root-user.html#id_root-user_manage_mfa) y en [cualquier usuario de IAM](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_mfa.html) con acceso a la consola. Habilitar MFA puede ayudar a asegurar las cuentas y evitar que usuarios no autorizados inicien sesión en las cuentas sin un token de seguridad.

- [Elimina todas las llaves programáticas de IAM de la cuenta root,](https://docs.aws.amazon.com/IAM/latest/UserGuide/best-practices.html#lock-away-credentials) no deberías usarlas en absoluto. Si de alguna manera esas llaves de acceso se filtran, se tiene acceso sin restricciones para hacer cualquier cosa.

- [Habilitar los servicios de registro de AWS CloudTrail](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/cloudtrail-create-and-update-a-trail.html) - Crear un nuevo rastro [NT: Trail], sólo para las escrituras, y habilita la vista [NT: insight] del rastro. Esto generará 50 centavos de dólar de cargo mensual, aunque ayudará a detectar y prevenir incidentes de seguridad.

  ![](assets/aws-account-hardening-cloudtrail.png)

- [Activa la detección de anomalías de costos de AWS](https://docs.aws.amazon.com/awsaccountbilling/latest/aboutv2/getting-started-ad.html#create-ad-alerts), es gratis:

  ![](assets/aws-account-hardening-costAnomaly.png)

- No compartas las credenciales IAM entre varias personas, [crea usuarios IAM individuales](https://docs.aws.amazon.com/IAM/latest/UserGuide/best-practices.html#create-iam-users) para cada persona de tu equipo (es gratis).

- Utiliza el "Principio del mínimo privilegio" para tus roles IAM, [concede el mínimo privilegio a cada usuario/rol](https://docs.aws.amazon.com/IAM/latest/UserGuide/best-practices.html#grant-least-privilege) 

- Configura una [política de contraseñas](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_passwords_account-policy.html) para los usuarios de IAM.

- Establece [contactos alternativos](https://console.aws.amazon.com/billing/home?#/account) en las preferencias de tu cuenta.

- [Información adicional](https://docs.aws.amazon.com/IAM/latest/UserGuide/best-practices.html)

---

## Medidas adicionales que serán útiles {id=adicional}

- Crear una [alarma de facturación de CloudWatch](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/monitor_estimated_charges_with_cloudwatch.html) para evitar fugas.

- Habilitar [GuardDuty](https://aws.amazon.com/guardduty/), no sólo ayudará en la parte reactiva de las incidencias, sino que también las prevendrá. GuardDuty te alertará cuando haya configuraciones inseguras, superficies de ataque o vulnerabilidades conocidas en tus recursos o instancias de AWS. Este servicio tiene una prueba gratuita de 30 días que puede utilizar para validar sus cuentas.

- Agrupar las cargas de trabajo en función del propósito empresarial y la propiedad [NT: ownership] utilizando [diferentes cuentas de AWS](https://docs.aws.amazon.com/whitepapers/latest/organizing-your-aws-environment/benefits-of-using-multiple-aws-accounts.html) (son gratuitas). Al separar cargas de trabajo[alcance de permisos?] en diferentes cuentas reduces el radio de explosión, fuerzas el aislamiento lógico de recursos, evitas dependencias y conflictos, restringes el acceso a datos sensibles y limitas el alcance del impacto. Piensa en ello como una agrupación lógica, lo que mejor se adapte a tu escenario, por ejemplo, por entorno (dev, prod, test), o por aplicación.
Esto también ayudará con las cuotas de servicio y la gestión de costos.
  
  Puedes configurar una organización de AWS (es gratis) para centralizar la facturación en una sola cuenta pagadora, y crear SCP (políticas de control seguras) para restringir cosas que sabes con certeza que nunca deben ocurrir en ninguna de esas cuentas, por ejemplo, regiones que nunca deben usarse, o tipos de instancia que nunca deben ejecutarse. 

  ![](assets/aws-account-hardening-createOrg.png)
  ![](assets/aws-account-hardening-scpscreated.png")

  No olvides [aplicar la política](https://aws.amazon.com/blogs/security/how-to-use-service-control-policies-to-set-permission-guardrails-across-accounts-in-your-aws-organization/) a la cuenta después de crearla. 

  Encontrarás algunos ejemplos de SCP en la carpeta /scps del [repositorio del autor orignal de este artículo en inglés](https://github.com/sercasti/aws-hardening), y puedes encontrar más en [la Gúia para Organizaciones](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_policies_scps_examples.html) de la documentacíon de AWS.

---

## Qué hacer si tu cuenta ha sido comprometida {id=comprometido}

- Paso 1: Inicia sesión [como el usuario raíz de la cuenta de AWS](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_root-user.html) (no su usuario de IAM). [Elimina la clave de acceso de AWS expuesta](https://aws.amazon.com/premiumsupport/knowledge-center/delete-access-key/) y elimina cualquier clave de acceso programática de la cuenta raíz que se haya podido crear durante la infracción.

- Paso 2: Dentro de IAM en tu consola, encontrarás un elemento de menú llamado [Informe de credenciales](https://aws.amazon.com/premiumsupport/knowledge-center/delete-access-key/), descarga el informe de credenciales y utilízalo para rotar y eliminar todas las claves de acceso de la cuenta raíz y de AWS Identity and Access Management (IAM). Para asegurar tu cuenta, elimina todos los usuarios, roles y políticas de IAM no autorizados y revoca todas las credenciales temporales, elimina todos los usuarios de IAM potencialmente no autorizados y, a continuación, [cambia la contraseña](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_passwords_admin-change-user.html) de todos los demás usuarios de IAM.

- Paso 3: Comprueba que la información de tu cuenta y los contactos alternativos son correctos en las preferencias de la [cuenta](https://console.aws.amazon.com/billing/home?#/account).

- Paso 4: Comprueba tu registro de CloudTrail para ver si hay actividad no autorizada, como la creación de usuarios de IAM no autorizados, políticas, roles o credenciales de seguridad temporales.
Utiliza las capacidades de búsqueda para rastrear lo que se hizo con las credenciales comprometidas y revierte cada acción una a la vez.
Si estas credenciales se utilizaron para crear nuevos usuarios o credenciales, será necesario repetir ese análisis para cada uno, para deshacer todo lo que se ha hecho durante el incidente.
Incluso si no has creado ningún rastro para tu cuenta, el "Historial de eventos" te muestra los últimos 90 días de eventos de gestión (y esos no se pueden borrar).
Intenta rastrear el inicio del incidente, encuentra la primera llamada a la API de operaciones "ConsoleLogin" no reconocidas, o nombres de eventos "CreateAccount", o cualquier tipo de actividad que sea sospechosa, prueba diferentes filtros (Nombre del evento, clave de acceso de AWS, tipo de recurso, nombre de usuario) para encontrar dónde empezó todo, y luego rastrea desde ahí, para seguir cualquier ramificación del incidente.
Fíjate en que las entradas de Cloudtrail incluyen la dirección IP y el agente de usuario [NT: User Agent], lo que puede ayudar a la hora de intentar relacionar diferentes llamadas a la API.

- Paso 5: Revisa tu cuenta de AWS en busca de cualquier uso no autorizado de AWS, como instancias EC2 no autorizadas, funciones Lambda u ofertas de EC2 Spot.
Para comprobar el uso, inicia sesión en tu consola de administración de AWS y revisa cada página de servicio.
Elimina cualquier recurso de tu cuenta que no hayas creado, como las instancias y [AMI de Amazon Elastic Compute Cloud (Amazon EC2)](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/terminating-instances.html), los volúmenes de Amazon Elastic Block Store [(Amazon EBS)](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ebs-deleting-volume.html), las [instantáneas](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ebs-deleting-snapshot.html), los usuarios de [IAM](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_users_manage.html#id_users_deleting).

- Paso 6: Comprueba todos los buckets públicos en busca de credenciales filtradas o bibliotecas obsoletas que puedan estar exponiendo variables de entorno.

- Paso 7: Comprueba todos los repositorios de código para asegurarte de que las credenciales de IAM no han sido enviadas a los atacantes.  [FIXME: intrusores? jerga]

- Paso 8: Responde a las notificaciones que recibas de AWS Support a través del [Centro de AWS Support](https://console.aws.amazon.com/support/).
Si no puedes iniciar sesión, utiliza el [formulario de contacto](https://pages.awscloud.com/contact-us-account-support.html).
Si tienes alguna pregunta o duda, crea un nuevo caso [FIXME: caso?] de AWS Support en el [Centro de AWS Support](https://console.aws.amazon.com/support/).

- Paso 9: Revisa tu [factura](https://docs.aws.amazon.com/awsaccountbilling/latest/aboutv2/invoice.html). Tu factura puede ayudarle a identificar los recursos que no has creado.

- Paso 10: Utiliza el [analizador de acceso de IAM](https://docs.aws.amazon.com/IAM/latest/UserGuide/what-is-access-analyzer.html) para comprobar si existen recursos restantes creados por el atacante que podrían ser utilizados como puertas traseras.
Este es un [servicio gratuito](https://console.aws.amazon.com/access-analyzer/), detectará cualquier recurso compartido fuera de la cuenta.

- Paso 11: Revisa las recomendaciones del principio de este documento, para reforzar la seguridad de tu cuenta.

Información adicional: 
https://aws.amazon.com/es/premiumsupport/knowledge-center/potential-account-compromise/

---

## Periódicamente {id=periodicamente}

- Revisa [Trusted advisor](https://aws.amazon.com/premiumsupport/technology/trusted-advisor/), es un servicio gratuito que cubrirá algunos puntos de datos en tus cuentas y levantará banderas rojas sobre problemas de seguridad.

- Recuerda desactivar las credenciales de AWS de las personas que van a dejar la empresa, antes de que lo hagan.

- Utiliza [roles](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_switch-role-ec2.html) para las aplicaciones que se ejecutan en instancias de Amazon EC2, en lugar de claves de acceso.

- [Rota las credenciales](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_access-keys.html#Using_RotateAccessKey) regularmente.

- Elimina las [credenciales innecesarias](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_finding-unused.html).

Estas recomendaciones se derivan de la primera fase del modelo de madurez de la seguridad de AWS, ya que se trata de beneficios rápidos para comenzar con seguridad tu viaje en la nube. Si quieres profundizar en este modelo, no dudes en visitar [AWS Security Maturity Model](https://maturitymodel.security.aws.dev/).

Si quieres ir a por todas, y ejecutar una herramienta para evaluar tu seguridad en AWS, prueba [Prowler](https://github.com/toniblyx/prowler).
Prowler es una herramienta de seguridad para realizar evaluaciones de las mejores prácticas de seguridad de AWS, auditorías, respuesta a incidentes, monitorización continua, endurecimiento y preparación forense. 

### Algunas capturas de Prowler:
![](assets/aws-account-hardening-prowler-1.png)
![](assets/aws-account-hardening-prowler-2.png)
![](assets/aws-account-hardening-prowler-3.png)
