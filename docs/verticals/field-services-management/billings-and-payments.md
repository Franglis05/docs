---
title: 2. Facturación y Pagos
category: Documentation
star: 9
sticky: 9
article: false
---

## Generar Facturas desde Línea de Orden

Una vez generada la Orden de venta (junto con la orden de compra y documento por pagar desde **"generar orden desde proyecto"**), a través del proceso **"Generar Factura desde línea de orden"** es posible de forma automática crear los documentos por cobrar (factura al cliente).

Para esto existe un requisito: la Orden de Venta debe estar seteada como **Permite Facturar = SI**. Debe seleccionarse la fecha de facturación, la accion en el documento (si la factura se genera en estado completo o en estado borrador) y el tipo de agrupación (por ejemplo: por orden).

El proceso cuenta con una sección de Criterio de Búsqueda con diferente parámetros que brindan eficiencia en la búsqueda de los registros a facturar tales como Orden de Venta, Fecha Prometida, Socio del Negocio, Proyecto, Agente Comercial, Categoría de Proyecto.

En el resultado de la búsqueda podrán visualizarse los datos esenciales de los registros con el objeto de individualizar aquellos que requieren facturarse.
Al seleccionar registros y ejecutar el proceso se crean los Documentos por cobrar vinculados a sus correspondientes órdenes de trabajo (en el caso de que seleccionen la acción sobre el documento "Completar", cambiará el estado de la orden de documentada por "Facturada").

### Tipo de Agrupación

Seleccionar un tipo de agrupación permite definir la forma en la cual se confeccionará el documento por cobrar.
Si se selecciona como tipo de agrupación "Proyecto" se emitirá un documento por cobrar por cada proyecto (previamente seleccionado). 
En el caso de seleccionar "Contrato", y elegir registros que estén vinculados a un mismo contrato, se emitirán todos en un mismo documento por cobrar (de existir diferentes contratos, se emitirá un comprobante por cada contrato).

Si se selecciona agrupar por Unidad, el proceso unificará en un mismo documento por cobrar aquellas wo de mismo Socio del Negocio y mismo dato Unidad (que se ingresa en la orden de trabajo). Este agrupamiento es similar al de PO reference (En este caso en lugar de agrupar por el dato Unidad, lo hará por el de referencia oc Cliente).

También cuenta con la opción de agrupar por "Socio del Negocio". En este caso al seleccionar un grupo de órdenes de trabajo para facturar, se agrupará por Socio de Negocio (y por contrato) en cada documento por cobrar.
Por último, al agrupar por "Orden" se generarán documentos por cobrar por las líneas de orden de trabajo que correspondan a una misma orden de venta.

![Generar Factura desde Línea de orden](/assets/img/docs/field-services-management/fis-services6.png)

## Enviar Facturas por Email

El navegador Enviar Facturas por Email permite realizar el envío de los Documentos por Cobrar en estado Completo a cada uno de sus clientes.

Cuenta con una sección de Criterio de Búsqueda para encontrar con mayor eficiencia los registros a ser enviados con parámetros tales como Agente Comercial, Factura, Proyecto, Orden.
El parámetro Impreso = NO posibilita visualizar solo aquellos Documentos por cobrar que no se imprimieron manualmente desde la consulta del documento (mientras que seteando SI, se podrán observar los ya impresos de forma individual y al dejar vacío el filtro se verán todos).

Dentro de los filtros es posible definir en "Enviar Factura A" si se desea enviar al Socio del Negocio (se envía al email definido en la pestaña Localización de Socio del Negocio), o al Representante de Ventas (se envía al email del Contacto vinculado al Socio del Negocio). En el caso de dejar vacío el filtro se enviará a ambos.

En la grilla se verán reflejado el resultado de la búsqueda con los datos esenciales por columna para identificar los registros que se desean enviar.

Una vez seleccionados aquellos registros a enviar, se ejecuta el proceso y en ventana emergente se selecciona el formato de Representación Impresa (esto dependiendo de ciertas condiciones como el País puede ser un dato por defecto o seleccionable) y al aceptar se inicia el envío por mail de los comprobantes seleccionados.

A partir del envío, las notificaciones ingresan en una rutina que envía en lote los correos, por un lapso determinado de tiempo y cantidad de correos (por ejemplo: 40 mails cada cinco minutos).

![Enviar Facturas por Mail](/assets/img/docs/field-services-management/fis-services15.png)

### Envío automático al completar Documento por Cobrar

Existe otra función de envío de Email por cada documento por cobrar al consultar individualmente el comprobante y cambiar su estado por "Completar". 
Esta acción dispara el envío del documento por mail al cliente.

Si los documentos por cobrar se generaran desde el navegador de Generar Factura desde Línea de Orden, para utilizar este envío individual deberían generarse masivamente en estado "Borrador" para luego consultarlos y completarlos (disparando el envío por Email).

Para los casos en los que se generen las facturas desde ese mismo navegador pero en estado completo existe el "Enviar Facturas por Email" detallado en el apartado anterior.

### Parametrización de Cola de Notificación

La Cola de Notificaiones funciona como una aplicación que se configura en el Registro de Aplicaciones de Solop ERP y utiliza para el envío de correos la configuración de envío de correos de la Compañía y/o Organización.

### Cola de Notificación

Cada evento que ejecuta un envío de información desde el sistema genera un registro de "cola de notificación". 
Este registro define el tipo de aplicación (ejemplo: correo electrónico).

Cuando se dispara una notificación desde el ERP, al generarse registro de cola de notificación, se graba como procesado = No (no enviado) y con el check de Activo = SI

El envío de notificación tiene diferentes funcionalidades: se puede generar desde

* El usuario
* La organización
* La compañia

From Account name: desde donde se origina la notificación.

Desde esta ventana es posible verificar la correcta salida de las notificaciones enviadas.
Y esto aplica tanto a los correos enviados por facturas a clientes como también para las notificaciones que se envían a los Agentes comerciales emitidos desde las órdenes de trabajo.

### Selección de Pago

Los documentos por pagar (por los servicios realizados por los diferentes agentes comerciales o recursos) se crean automáticamente junto con la orden de compra (al generar la orden de venta en estado completo). Por lo cual, el paso siguiente es generar la Selección de Pago.
Esto puede realizarse diariamente, o periódicamente (de forma semanal, quincenal, etc.)

En la ventana Selección de Pago debe seleccionarse El tipo de documento (Orden de Pago), la cuenta bancaria, la fecha del documento y la moneda. Luego debe setearse la selección de pago en Estado Completo.
La selección de pago puede realizarse sobre un agente comercial en particular o bien sobre los documentos por pagar pendientes de pago (uno, varios o todos), mediante el botón de seleccionar Documentos por pagar.

En paso posterior se selecciona la forma de pago y es posible imprimir el Pago generado (o exportar desde la ventana Imprimir/Exportar pagos).

![Selección de Pago](/assets/img/docs/field-services-management/fis-services7.png)