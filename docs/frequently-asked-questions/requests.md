---
title: Solicitudes
category: Documentation
star: 9
sticky: 9
article: false
---

## Mantenimientos

### ERROR en envío de emails

El motivo del error puede ser que la casilla de gmail no está permitiendo la conexión del sistema con el gmail.

**SOLUCIÓN:**

En acceso de Aplicaciones poco seguras se debe Permitir el acceso de aplicaciones poco seguras.

Se debe marcar este check en Y.

Puede pasar de que al enviar correos una vez por mes de esta manera, se desactiva automáticamente. En estos casos se debería verificar antes de enviar que el correo esté con este permiso habilitado.

### Parametrización

1. A nivel de Compañía se define la configuración del Servidor de Correo, cuenta y contraseña de envío:
2. Realizar prueba de envío para verificar que pueda conectarse al servidor de correo con dicha cuenta, enviará un email de prueba.
3. Al modificar una solicitud, primero se revisará si el usuario tiene un correo con contraseña definido y realiza el envío con su correo:
4. Si el usuario no tiene parametrizado estos datos, va a obtener el correo de la Compañía para realizar el envío.
5. Realizará el envío a los correos de los usuarios que están parametrizados en estos campos.

#### Mejora: Servidor de Correo para el Usuario

* Al momento de realizar un envío de email con el correo de un usuario, este no tiene la configuración de correo por lo que obtiene la información del servidor desde la Compañía, esto causa que de un error cuando el usuario tiene un correo que debería utilizar una configuración de servidor de correo diferente. e.g.: Compañía usa gmail, y el usuario utiliza un correo de la empresa.

* Solución:
  * Definir a nivel de usuario la configuración de servidor de correo como se implementó a nivel de Compañía para esta cuenta de correo
  * Definir un check que indique si el usuario al enviar un email utiliza el correo de la Compañía o si utiliza su propio email, en caso de utilizar el suyo se deberán cargar los campos:
    * Configuración de servidor de correo
    * ID Usuario (la cuenta de correo)
    * Su respectiva contraseña

#### Adjunto con nombre poco legible

* Al realizar el envío por mail de un pdf de una ventana, el PDF que se envía como adjunto tiene un nombre poco legible
* Solución:
  * Definir con un archivo temporal de Java un archivo con prefijo que cumpla el siguiente patrón:
    * Compañía
    * Ventana transaccional: tipo y número de documento. Otra ventana: Formato de impresión (nombre)
    * Timestamp Actual
  * Sufijo:
    * .pdf (o la extensión que corresponda)

## Acciones

### Requisitos para que un usuario interno de Solop ERP pueda ver solicitudes

Para que un usuario de autenticación pueda ver “Solicitudes” en Solop ERP de otros usuarios, debe tener asignado un Socio del Negocio. Luego, ese Socio del Negocio, en la pestaña “Empleado” debe tener marcada la opción de “Agente Comercial”.

