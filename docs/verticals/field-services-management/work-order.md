---
title: 1a. Órdenes de Trabajo Field Services
category: Documentation
star: 9
sticky: 9
article: false
---

## Generación de órdenes de trabajo

Una orden de trabajo es considerado un Proyecto para Solop ERP.
Se trata de una unidad de gestión que agrupa un conjunto de entidades que le dan forma y describen un determinado Servicio.

El primer paso para la creación de una Orden de trabajo es ingresar en la ventana el nombre del cliente (Socio del negocio del cual hereda la dirección, lista de precio y región de ventas), la fecha de inicio del servicio a realizar y seleccionar una categoría de Proyecto (y la unidad o departamento).
En este paso solo se genera el evento (no se asignan recursos o productos). Además el sistema creará una línea de proyecto vacía para agilizar el proceso.

![Orden de Trabajo](/assets/img/docs/field-services-management/fis-services2.png)

### Estados de la Orden de Trabajo

La orden presentará diferentes estados de acuerdo a su condición o momento del proceso donde se encuentre:

**New:** es el estado por defecto al crear nuevo proyecto.

**Assigned:** cuando se asigna el agente comercial por primera vez.

**Confirmed:** cuando se asigna el producto a la línea/s del proyecto.

Este estado se asigna cuando todas las líneas del proyecto tienen asignado producto.

**Documented:** cuando se han generado órdenes de venta.

Al crearlo desde el proceso Generar Orden desde Proyecto, o desde el proceso de la propia orden de trabajo

**Invoiced:** el proyecto ha sido facturado al cliente

Este estado se debe asignar cuando se marque el check de 'Facturado' en un OV que tenga el proyecto.

## Asignación de Recursos

Desde la ventana de Navegador de Proyectos es posible visualizar aquellas órdenes de trabajo que aun no posean agente comercial (es quien realizará el servicio), seteando el parámetro Agente de Compañía como filtro "No tiene valor".

Para agilizar la búsqueda, el navegador posee diferente parámetros como Cliente, Agente Compañía, Fecha Inicio, Categoría de Trabajo, Región. 
Estos parámetros también se visualizan en el resultado de la búsqueda como columnas para poder identificar el registro que se desea actualizar.

Una vez asignado a un agente comercial (se selecciona el que corresponda y se ejecuta desde el botón "Project Selection"), el sistema le envía una notificación (solicitud) por el servicio a realizar al agente comercial en cuestión (es posible configurar el envío del mensaje por diferentes vehículos de comunicación).

Esta acción cambiará el estado de la orden de trabajo de "Nuevo" a "Asignado".

![Navegador de Proyectos](/assets/img/docs/field-services-management/fis-services3.png)

### Requisitos para el envío automático de la notificación

Existen dos condiciones para que aplique el envío de la solicitud:

* El estado de la orden de trabajo debe ser la definida como "Predeterminada" (Estado: Nuevo)

* Se realiza una validación para establecer si ha cambiado el valor "Agente Comercial".

Al cumplirse estas condiciones el sistema genera el envío de la notificación, y modifica el Estado "Nuevo" por el siguiente estado de la Orden de Trabajo (Asignado).

## Confirmación de Servicio realizado

Una vez realizado el servicio (ejemplo: painting), el agente comercial confirma el trabajo realizado.

Esto permite al departamento de Administración buscar desde el navegador de proyectos (por agente comercial) e ingresar en el campo Trabajo realizado los trabajos a facturar y setear "Trabajo verificado" = SI (así como agregar las notas correspondientes al servicio realizado).

Posteriormente en la orden de trabajo vinculada a ese servicio se agregará en la línea (o líneas si es más de un trabajo realizado) de orden de trabajo el/los productos confirmados por el agente comercial.

En ventana de orden de trabajo es posible visualizar el campo "Fecha de Verificación", en modo de sólo lectura.
En este campo se asigna la fecha en la cual el check "Trabajo Verificado" se marca en 'Y', ya sea de forma manual en la ventana, o mediante en proceso "Navegador de Proyectos" (si el check de verificado se marca en 'N', la actual fecha de verificación se borra).

En dicho proceso se existe una columna con el dato "Fecha de Verificación" y también como filtro.

## Navegador de Líneas de Proyeccto

El navegador de proyectos permite hacer más eficiente la tarea de definir productos en las órdenes de trabajo de manera masiva.
En la sección "Criterio de búsqueda" cuenta con diferentes parámetros para encontrar de manera ágil aquellos registros que se deseen actualizar tales como Orden de Trabajo, Cliente, Región, Agente Compañía, Fecha Inicio, Categoría de Trabajo.
En el resultado de la búsqueda se verán estos datos en columna a los fines de encontrar los registros a aplicar producto.

Al seleccionar un registro habilita la posibilidad de asignar un producto y en otra columna puede agregarse una descripción de línea (como nota aclaratoria). 
Al ejecutar el proceso quedará el producto definido en la línea de la orden de trabajo seleccionada y cambiará su estado de Asignado a "Confirmado".

![Línea de Proyecto](/assets/img/docs/field-services-management/fis-services10.png)

Es válido mencionar que en particular, este navegador se utiliza para definir producto solo en los casos en los cuales la orden de trabajo tenga pactado un solo servicio. 
Para los casos en los cuales deban generarse más cantidad de líneas (más de un producto/servicio) se deberá definir desde la consulta de la orden de trabajo, en sus líneas.

![Línea de Proyecto](/assets/img/docs/field-services-management/fis-services4.png)

## Generar Orden desde Línea de Proyecto

Es posible generar este proceso de dos formas:

* Desde el **navegador Generar orden desde Línea de Proyecto** se la selecciona y le crea en forma automática (heredando los datos de la orden de trabajo) una orden de venta en estado completo. 
Esta orden en estado completo genera una orden de compra (si la orden de venta posee costo asociado) y un documento por pagar (este último corresponde al servicio realizado por el agente comercial o recurso).

Cuenta con parámetros para agilizar la búsqueda de los registros tales como Socio del Negocio, Proyecto, Agente Comercial, Fecha Inicio, Lista de Precios. 
El filtro de Estado del Proyecto posee un valor por defecto: "Confirmado", con el objeto de que solo se muestren los registros que tienen definido producto (con posibilidad de cambiar el valor del parámetro).

Este navegador muestra líneas de proyectos abiertos y permite generar las órdenes de venta según los filtros aplicados.

La "cantidad a facturar" de cada línea será la diferencia entre la cantidad planeada y la "cantidad ordenada" (suma de cantidades en Órdenes de Venta completas o cerradas, para la línea de proyecto en cuestión).

El "importe a facturar" es la cantidad a facturar multiplicado por el precio planeado de la línea de proyecto.

El navegador sólo mostrará las líneas de proyecto que tengan cantidad a facturar mayor a cero.

Al procesar se genera una Orden de Venta por cada proyecto, con el tipo de documento, estado y fecha seleccionados. 
Emite mensaje restrictivo si una línea no tiene definido el producto.

También se genera la Orden de Compra por costo asociado, y su correspondiente Documento por Pagar (según parametrización del tipo de documento de la Orden de Compra). El Proveedor de la Orden de Compra será el que tiene asociado el agente comercial del proyecto, siempre y cuando éste Socio del Negocio esté marcado como "Proveedor".

El proceso devolverá la cantidad de Órdenes de Venta creadas y sus identificadores numéricos.

* Desde la misma **orden de trabajo**, es posible seleccionar el proceso de generar orden y se corre individualmente para el proyecto consultado.

![Generar Orden desde Línea de Proyecto](/assets/img/docs/field-services-management/fis-services5.png)

## Diferentes definiciones de Precio de Compra

Solop ERP contempla diferente formas de calcular el precio de compra ajustándose a las necesidades del negocio y aplicando diferentes lógicas por Categoría de Producto, por dificultad del trabajo realizado, por lista de precios o por tareas ejecutadas por personal interno (sin valor de compra).

### Definición Simple

En este caso el producto/servicio posee un precio fijo que se obtiene de una lista de precio (Compra).
Un mismo producto/servicio puede contar con una lista de precio, la cual puede presentar múltiples "versiones de lista de precio". 

En este sentido, existirá la lista de precio "Venta", la cual puede tener una versión de lista de precio por cada cliente. Y a su vez una lista de precio de compra (con precio único o con versiones de lista de precio por proveedor).

![Definición Simple](/assets/img/docs/field-services-management/fis-services14.png)

### Definición por Porcentaje de Costo

En estos casos no se aplica el precio de lista de compra, sino que se utiliza un importe a partir de un porcentaje según el precio de venta definido (de la lista de precio venta que corresponda). Es decir, permite aplicar como precio de compra, un porcentaje (el cual es posible definir de antemano) del precio de venta.

Este porcentaje se define en el campo **esquema de descuento** asociado en la ventana Socio del Negocio, pestaña proveedor, para definir los % de descuento para cada categoría de producto.

Al momento de crearse la Orden de Compra, cuando el producto no tiene precio de compra o su precio es cero, se toma el precio de la línea de orden de venta, y se obtiene el porcentaje de descuento según el esquema del proveedor.

En la línea de la Orden Compra creada es posible visualizar el porcentaje aplicado.

![Porcentaje de Costo](/assets/img/docs/field-services-management/fis-services13.png)

### Definición con Porcentaje de Dificultad

Existe un criterio de "dificultad del servicio" donde es posible definir manualmente en cada orden de trabajo la ponderación de la dificultad del mismo. Este porcentaje aplica solamente a la definición del precio de compra de dicho servicio.

El porcentaje se debe definir en la línea del proyecto, campo "Multiplicador de dificultad". 
Por defecto el valor es "1" (sigue siendo el % definido incialmente de costo), pero podría suceder que si el trabajo puntual presenta una mayor dificultad se agregue un "10 usd" más, es decir que se defina en la línea del proyecto un 1.1 y entonces se considera este importe en la multiplicación para definir el precio de compra.

Al momento de crearse la Orden de Compra, si la línea de proyecto asociada a la línea de la Orden de Venta tiene definido una dificultad mayor a cero, entonces se multiplica el precio de lista de la orden de compra por el multiplicador de dificultad (ejemplo: 1.1).

De esta forma se obtiene el nuevo precio de lista, al cual luego se aplica el porcentaje de descuento, en caso que se obtenga desde el proveedor.

![Porcentaje Dificultad](/assets/img/docs/field-services-management/fis-services12.png)

### Definición para Servicios realizados por empleados internos (sin costo directo)

Pueden existir productos/servicios que no posean un costo asociado. En estos casos no se genera ningún Documento por pagar al generar órdenes de este tipo de productos, ya que serán realizados por personal de la empresa (no facturan por servicio realizado).

Para que este caso se cumpla, existe una condición para que no se genere la línea de Orden de Compra:

* El producto debe estar definido como Comprado = NO

Al momento de aplicar el proceso de generar órdenes se crea normalmente la Orden de Venta (para su posterior facturación al cliente) y la orden de compra se genera en valor cero.

![Servicios sin costo directo](/assets/img/docs/field-services-management/fis-services11.png)

### Servicios Adicionales sin Precio de Lista

Ciertos servicios pueden requerir el cobro de adicionales o recargos variables por tareas preparatorias o actividades "extra".
Para estos casos se cuenta con Productos en cada Lista de Precio como "Other Clean" u "Other Paint" con valor "0" (cero).
Al confirmar este tipo de servicios, en la orden de trabajo se generan dos líneas:

* Una por el servicio específico a realizar

* Y otra línea por el adicional o recargo (agregando el valor que corresponda manualmente). Podrá ser solo una línea adicional o las que correspondan de acuerdo a los recargos a facturar posteriormente.