---
title: Actualizar Contratos Educación
category: Documentation
star: 9
sticky: 9
tag:
  - Educación
article: false
---

## Actualizar Contratos Educación (cambio de año)

Este proceso permite generar de forma automática la renovación de contratos de alumnos por el pasaje de un año a otro mediante un conjunto de filtros que permiten seleccionar los contratos a actualizar, cerrando los del año finalizado y creando los del año siguiente con el nuevo producto, tipo de servicio, actividad y fechas (inicio, fin programado, fecha contable y fecha documento).

### 1. Configurar producto sustituto para cada curso

Para que el sistema actualice correctamente los contratos por pasaje de año, se deberán pre setear a los diferentes productos, sus productos sustitutos. De esta manera al ejecutar el proceso de actualización de contrato (por ejemplo) ERP Solop cerrará los contratos de "Año primero" y creará para esos mismos alumnos (de los contratos seleccionados) los contratos para "Año segundo", con sus nuevas fechas.

#### Definición de Datos:

En la ventana producto, sección "Sustituto" se deberá definir el curso siguiente (producto correlativo siguiente) en el campo Sustituto.

![Producto Sustituto](/assets/img/docs/education-management/sem-substitute2.png)

::: note
Producto: LT (Little Todddlers).
El producto que le sigue a este sería el "Toddlers" (del ejemplo práctico en la imagen), por esta razón se deberá definir el mismo como "Sustituto".
:::

En la misma ventana producto, sección "Memo" se deberá definir la Actividad.

![Actividad](/assets/img/docs/education-management/sem-activity3.png)

::: note
Actividad: En la pestaña memo se deberá definir la Actividad que se vinculará con el producto en cuestión. Esta actividad será la que se defina en la línea del los contratos que correponda en la actualización.
:::

En el cabezal de Producto debe estar definido el "Tipo de Servicio".

![Tipo de Servicio](/assets/img/docs/education-management/sem-service4.png)

::: note
Tipo de Servicio: desde el tipo de servicio se tomará la definición de recurrencia de la línea del Contrato. O sea, si se trata de un servicio mensual (kinder, Año Primero) o un servicio específico no mensual (Taller, Natación).
:::

### 2. Selección de Filtros

Una vez realizadas las configuraciones previas, al momento de correr el proceso de Actualización de Contratos contamos con diferentes filtros para ajustar la búsqueda:

* Contrato de Servicio: cuando necesitamos actualizar un Contrato en particular.
* Socio del Negocio: permite filtrar por el alumno
* Socio del Negocio a facturar: permite filtrar por el responsable de pago (padre, madre, etc. del alumno).
* F. Documento: permite filtrar por fecha de documento (en el caso que se posean contratos de diferentes años.
* Actividad: es el filtro más utilizado, permite buscar los contratos de cada curso a actualizar.

![Filtros y Nuevos Datos](/assets/img/docs/education-management/sem-filter5.png)

### 3. Definición de nuevos datos y Ejecución del Proceso

Una vez definidos los filtros y realizada la búsqueda nos abrirá en el visor de la pantalla la lista de los contratos (que respondan a los filtros pre seleccionados) con sus datos principales y con opción de seleccionar todos, o algunos de ellos.

Debajo del visor podremos observar diferentes campos que se corresponden con los nuevos datos a configurar en los contratos del nuevo año:

* F. Documento: se debe ingresar la fecha de documento (contrato), en general es el primer día del año.
* Fecha Contable: en general también es el primer día del año.
* Fecha Inicio: es la fecha a partir de la cual comenzará generar las diferentes cuotas (en el proceso posterior de generar cuotas de contrato), generalmente es el primer día de marzo.
* Fin Programado: es la fecha fin del contrato, generalmente es el último día del año.
* Tipo de Servicio: si este campo se deja vacío en forma automática se definirá en el nuevo contrato el producto sustituto pre seteado en el producto del contrato anterior. Caso contrario, se puede forzar en este campo cual será el curso (producto) a asignar a los nuevos contratos.
* Acción en el documento: permite definir si los contratos se crearán en estado "preparar" (borrador) o "completar".

Al  ejecutar el proceso, los Contratos seleccionados quedarán en estado "Cerrado" y se crearán nuevos contratos a partir de los anteriores (con mismos datos de alumnos, descuentos, etc.) aplicando las nuevas fechas, tipo de servicio, producto y actividad.

::: note
Los nuevos contratos quedan disponibles para continuar con los siguientes pasos que serían:
:::

* Correr el Proceso de Actualización de Precios: actualiza el precio de contrato de acuerdo a la versión de lista de precio vigente.
* Correr el Proceso de Generación de cuotas de Contratos: Esto genera las cuotas mensuales según el rango fecha que se seleccione en "Fecha Hasta" (generalmente se elige generar hasta mitad de año por posibles cambios de precio en segundo semestre).

![Actualización de Precio y Generación de cuotas de Contrato](/assets/img/docs/education-management/sem-update6.png)

### Ventana Motivo de Cancelación del Contrato

En esta ventana se deben definir todos los motivos a utilizar para cerrar un contrato.

El motivo "Egreso" presenta marcado el check "Motivo Final", para que sea el motivo que el proceso tome por defecto para cerrar un contrato cuyo producto no tiene un sustituto.

![Motivo Egreso](/assets/img/docs/service-management/sem-image1.png)

El proceso de "Actualización de Contratos" presenta el campo "Acción", según este campo se despliegan los demás campos necesarios. El mismo despliega las siguientes opciones:

Cerrar Contrato: se debe seleccionar un motivo, y el contrato se cierra y se asigna el motivo elegido al contrato
Cerrar y Crear Nuevo Contrato: el contrato se cierra y se crea uno nuevo, pero en caso de que el producto del contrato a cerrar no tenga un sustituto, entonces el contrato se cierra con el motivo "Egreso" (motivo Final), y no se crea un nuevo contrato

::: note
al cerrar, anular o completar un contrato se ejecuta el proceso de actualización de hijos.
:::

![Motivo Egreso](/assets/img/docs/service-management/sem-image2.png)

![Motivo Egreso](/assets/img/docs/service-management/sem-image3.png)

Motivo en ventana de Contrato:

![Motivo Egreso](/assets/img/docs/service-management/sem-image4.png)

### Ejemplo de Actualización de Contrato por cambio de año:

![Actualización de Contrato](/assets/img/docs/service-management/sem-update-contract.mp4)

#### Verificación de Datos en nuevo contrato:

![Verificación de Datos](/assets/img/docs/service-management/sem-verification.mp4)