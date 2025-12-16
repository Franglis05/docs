---
title: Carga de contratos manual (Educación)
category: Documentation
star: 9
sticky: 9
tag: 
  - Educación
article: false
---

## Carga de Alumno-Contrato (Educación)

Mediante esta ventana se permite generar la importación de un contrato y todas sus entidades relacionadas (alumno, familia, miembros, contactos), pero de forma manual, en vez de utilizar una planilla excel.

### 1. Datos Alumno y Localización

En este grupo de datos se define la información del ALUMNO (hijo) y su localización. La mayoría de los datos son obligatorios.

Se controla que el Socio del Negocio (SDN) alumno no exista, mediante el código de SDN igual a nro. de identificación, email y nombre (se intenta obtener mediante estos tres parámetros), en caso de existir se asigna el mensaje de error correspondiente en la línea y no se procesa ese registro.

![Datos de Socio del Negocio](/assets/img/docs/basic-rules/bid-import-SDN.png)

### 2. Datos Contrato

Aquí se definen los datos relacionados al contrato y la familia. Para la familia se puede seleccionar una ya existente en el campo "Familia", o ingresando el nombre de familia en "Nombre de Familia" se creará una nueva.
Es válido mencionar que si se ingresa el nombre de una familia existente, se vincularán tanto el estudiante, como el contrato y los contactos a esa familia previamente creada (función de utilidad para cuando sea necesario cargar hermanos u otros contactos a una misma familia).
Respecto al contrato es importante definir el rango fecha entre Fecha inicio y Fin programado (y Fin de Terminación) que generalmente se configura por año calendario.

![Datos del Contrato](/assets/img/docs/basic-rules/bid-import-contract.png)


### 3. Datos Contactos (RP y familiares)

Existen tres grupos de contacto, donde "Contacto 1" es destinado al responsable de pago (sea Madre, Padre, etc.) mientras que a los dos contactos restantes se los podrá cargar como familiares del alumno (si bien no serán responsables de pago, es posible marcarlos como "envía Email", caso en el cual serán notificados de las cuotas pendientes).

Se busca obtener el SDN a facturar (con el mismo método usado para el alumno), si el mismo no existe entonces se crea al realizar la importación.

Si se ingresa nombre de contacto 1, 2 o 3, se ponen como obligatorios los demás campos necesarios para su creación.

![Datos de Contactos](/assets/img/docs/basic-rules/bid-import-contact.png)

### 4. Ejecutar importación

Para proceder a importar el contrato y demás entidades, se debe ir a la opción "Importación de Contrato", ubicada en el ícono de Procesos, según imágen siguiente:

![Proceso de Importación](/assets/img/docs/basic-rules/bid-import-importation.png)

![Datos de Acción sobre Documento](/assets/img/docs/basic-rules/bid-import-doc-action.png)

La "Acción del Documento" que se seleccione, aplicará al Contrato, según se desee que el mismo queden en estado 'Completo' o 'En Proceso'.

Luego de finalizado el proceso, se mostrará un aviso con la información de los registros generados en el sistema, y para el caso de entidades que hayan tenido error, los mismos se podrán visualizar en el siguiente campo:

![Mensajes de Error](/assets/img/docs/basic-rules/bid-import-error-message.png)

### Ejemplo de Importación Alumno-Contrato:

![Ejemplo de importación](/assets/img/docs/basic-rules/bid-import-example.mp4)

### Validación de entidades generadas por importación:

![Validación de Datos Importación](/assets/img/docs/basic-rules/bid-import-verification.mp4)

::: note
Este funcionamiento es similar al de todos los demás procesos de importación en el sistema (diario contable, estados de cuenta, etc).
:::