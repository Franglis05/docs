---
title: Nota de Crédito
category: Documentation
star: 9
sticky: 9
article: false
---

Es un documento que se aplica a una factura, con la finalidad de reflejar un descuento, un cobro de un gasto incurrido de más, o alguna devolución de productos que el socio de negocio tipo cliente haya comprado.

## Nota de Crédito Cliente

Existen las siguientes razones por la cual se debe realizar una Nota de Crédito:

**Solicitud del Cliente de Re-facturación:** Se recibe solicitud del cliente que necesita que su Orden de Compra sea Facturada nuevamente por lo que se debe hacer una NC sobre la Factura ya realizada.

**Servicio Entregado No Aceptado:** Cuando un servicio se realizó (Delivery) pero que no es aceptado por el Cliente total o parcialmente por lo cual solicita una *Devolución* junto con su correspondiente *Nota de Crédito*.

**Servicio Facturado pero No Entregado:** Cliente solicita Nota de Crédito por la Facturación de un servicio que no fue entregado.

**NC Manual por Diferencia de Precio o Descuento Financiero:** NO RECOMENDADO

### Generar Devoluciones a Cliente

Se deberá realizar la “Devolución de Cliente” cuando un Cliente solicita o el Ejecutivo de Ventas solicita en nombre del cliente, la emisión de una Nota de Crédito debido a una “Entrega” (Delivery) No aceptada por el cliente. Esta “Devolución Cliente” deberá ser generada desde el Proceso “Generar Devoluciones”, seleccionando la Orden de Venta del Cliente que se querrá devolver.

Este proceso se deberá realizar si se desea “Corregir” un checking ya realizado en un Período anterior que se encuentra ya CERRADO. Lo que realizará esta “Devolución Cliente” son 2 acciones:

Generar un Movimiento contrario a la Entrega realizada por el Checking. Restando así el Ingreso reconocido con dicha “Entrega”

Generar una Devolución de Proveedor Espejo, es decir se generará una Devolución Cliente y una Devolución Proveedor por la MISMA CANTIDAD definida. Dichas devoluciones luego quedarán a la espera de sus correspondientes Notas de Crédito. Administración podrá ver las Devoluciones Cliente que están pendientes de Generar Nota de Crédito y del lado del Proveedor estarán las “Devoluciones Proveedor” (o RMA) pendientes de generar Notas de Crédito Proveedor cuando estas lleguen.

### Generación de Nota de Crédito

Este acto se complementa con la Generación posterior de la “Nota de Crédito Cliente” a partir de la Devolución Cliente. Esta acción se podrá realizar mediante el Proceso “Generar Nota de Crédito por Devolución”

### Generar NC Desde Devolución

Para que aparezca la información se deberá seleccionar el Tipo de Documento “Devolución Cliente” y se recomienda definir en Acción del Documento “Preparar”se generará un Documento por Cobrar del tipo “e-Factura Nota de Crédito” en estado “En Proceso”. El encargado de facturación deberá tomar el mismo, verificar las Línea CFE y simplemente Completarlo. Dicho documento se debería haber generado con toda la información correspondiente de “Sello, Sello Origen, Contrato de Servicios, DxC que Asignará, Proyecto, etc.

### Control Nota de Crédito sólo si está facturado

Las devoluciones se podrán realizar siempre y cuando exista una Entrega/Recepción pero estas, si bien pueden aparecer no podrán ser Facturadas. Si se intenta Facturar dará Error “Not Invoiced” verificando así que dicha devolución sea sobre una línea que está Facturada.

### Servicio Facturado pero No Entregado

Para este caso, debido a que el importe que se deberá generar una Nota de Crédito aún no fue Entregado, es decir no se realizó Checking, para solicitar la creación de una Nota de Crédito por las Cantidades que fueron Facturadas pero no fueron Entregadas bastará que el Usuario “Cierre” la Orden de Venta correspondiente. Al Cerrar una Orden de Venta las “Cantidad Ordenada” de sus líneas son llevadas a la “Cantidad Entregada”.

### Control de Facturación correcta en Órdenes de Venta

El sistema, luego de Cerrar una Orden, realizará un control de verificar si la Orden de Venta está Correctamente Facturada. Este Control implica 2 verificaciones:

Control de Cantidades: En cada una de sus líneas se verificará que su “Cantidad Facturada” NO sea SUPERIOR a la “Cantidad Ordenada”. En caso de encontrar alguna línea que sea superior, es decir que se haya Facturado más de lo Ordenado y que la Orden esté Cerrada, se generará automáticamente una “Solicitud de Nota de Crédito” detallando la Orden de Venta y Factura vinculada y se le asignará al Departamento “Administración”. Este control se aplicará siempre y cuando dicha Orden no haya sido “Modificada”

1. Control de Totales (Orden Modificada): Si en el primer control no encontró nada por lo que deba realizar una Solicitud de NC, se deberá continuar con el siguiente paso que será analizar el “Total de Líneas” de la Orden es Menor que el “Total de Líneas” del Documento por Pagar vinculado a la misma. En caso de que la Orden sea Menor que el DxP entonces deberá correr el proceso de “Solicitud de NC”.

### Generar Nota de Crédito Cliente desde la Factura

Para generar una Nota de Crédito Cliente mediante la opción **“Crear desde”** se utilizará la ventana Documentos por Cobrar.

Se deberá ingresar:

* Tipo de Documento: Nota de Crédito
* Socio de Negocio: Cliente al que se facturará
* Tipo Autorización Devolución: Motivo por el cual se hace la Nota de Crédito

Guardaremos el cabezal y seleccionaremos el botón “Crear desde".

Este botón permitirá crear la Nota de crédito desde una Orden de venta o compra, Factura o Recibo.

![Nota de Crédito](/assets/img/docs/sales-management/sam-agency8.png)

Seleccionaremos el tipo de documento, el documento en cuestión y realizaremos la búsqueda smartbrowser.

Esta búsqueda nos mostrará todas las líneas del documento, las cuales podemos seleccionar mediante un “check” modificando sus cantidades si se desea.

Luego correremos el proceso seleccionando el botón de OK.

Inmediatamente el sistema cargará las líneas a la Nota de crédito (donde se podrán modificar las cantidades y los importes) y definirá en la pestaña CFEs Referidos la factura que estoy asignando.

Por último procederemos a completar la Nota de Crédito.

La misma quedará con el check “pagado” siempre que haya sido por el total de la factura.

![Selección](/assets/img/docs/sales-management/sam-agency9.png)

::: note
Para ingresar una Nota de crédito Proveedor se utiliza el mismo procedimiento de ingreso de una factura de compra, indicando como Tipo de documento una Nota de crédito.
:::

### Solicitud de Re-facturación

En caso que se solicite realizar una Nota de Crédito a un Cliente pero sin modificar la Entrega correspondiente ya que está correcta, se deberá generar una Solicitud del Tipo “Solicitud de Nota de Crédito”.

La Solicitud deberá ser creada desde la ventana de “Órdenes de Venta” o “Documentos por Cobrar” desde el Documento en cuestión en base a cuál se debe generar la Nota de Crédito. La Solicitud debe ser enviada a un Usuario de Administración y también definir el “Departamento”: Administración de manera que pueda visualizar dicha solicitud y proceder con la Generación de la NC.

Para generar la NC se deberá generar la misma desde la Ventana “Documentos por Cobrar” seleccionando el SDN a quien será generada. Para obtener la información de la Factura que se estará cancelando se deberá seleccionar la misma desde el botón “Crear Desde”. Con este proceso se definirá todos los campos igual a como estaba la Factura generada. En caso de tener que modificar la Cantidad que se desea hacer NC se deberá ir a las líneas a modificarlas manualmente.

Luego de “Completar” la Nota de Crédito, la Orden de Venta que había sido Facturada quedará nuevamente disponible para volver a ser Facturada.

El asiento contable es el inverso a la Factura.

A continuación es explicado el procedimiento para registrar en Solop ERP una nota de crédito de cuentas por cobrar.

## Registro de Nota de Crédito

Ubique y seleccione en el menú de Solop ERP, la carpeta **Gestión de Ventas**, luego seleccione la carpeta **Facturas de Ventas**, por último seleccione la ventana **Documentos por Cobrar**.

![Campo](/assets/img/docs/sales-management/sam-sales-image10.png)

Imagen 1. Menú de Solop ERP

Podrá visualizar la ventana **Documentos por Cobrar**, con todos los registros de documentos por cobrar cargados a Solop ERP.

* Monoregistro

![Campo](/assets/img/docs/sales-management/sam-sales-image11.png)

* Multi registro

![Campo](/assets/img/docs/sales-management/sam-sales-image1111.png)

Imagen 2. Ventana Documentos por Cobrar

Seleccione el icono **Registro Nuevo**, ubicado en la barra de herramientas de Solop ERP, para crear un nuevo registro en la ventana **Documentos por Cobrar**.

Seleccione en el campo **Organización**, la organización para la cual se encuentra realizando el documento **Nota de Crédito CxC**.

Seleccione en el campo **Orden de Venta**, la orden de venta correspondiente al registro que se encuentra realizando.

Podrá visualizar en el campo **Fecha de la Orden**, la fecha contable de la orden de venta seleccionada en el campo **Orden de Venta**.

Introduzca en el campo **No. del Documento**, el número de identificación correspondiente al documento que se encuentra realizando.

Si no es ingresado ningún valor en el campo, Solop ERP tomará el número de secuencia establecido para el tipo de documento al guardar el registro.

Introduzca en el campo **Referencia de Orden de Socio del Negocio**, la referencia de la orden del socio del negocio.

Introduzca en el campo **Descripción**, una breve descripción correspondiente al registro que se encuentra realizando.

Seleccione el tipo de documento a generar en el campo **Tipo de Documento Destino**, la selección de este define el comportamiento del documento que se está elaborando, dicho comportamiento se encuentra explicado en el documento Tipo de Documento elaborado por Solop ERP.

El checklist **Auto-Servicio**, que el registro es una entrada del autoservicio o se puede cambiar vía autoservicio.

Seleccione en el campo **Fecha de Facturación**, la fecha en la cual es aplicada la nota de crédito que se encuentra realizando.

Seleccione en el campo **Fecha Contable**, la fecha en la cual es aplicada la nota de crédito que se encuentra realizando.

Seleccione en el campo **Socio del Negocio**, el socio del negocio al cual se encuentra aplicando la nota de crédito.

Podrá visualizar en el campo **Dirección del Socio del Negocio**, la dirección del socio del negocio seleccionado anteriormente en el campo **Socio del Negocio**.

Podrá visualizar en el campo **Usuario**, el usuario del socio del negocio seleccionado anteriormente en el campo **Socio del Negocio**.

Seleccione en el campo **Lista de Precios**, la lista de precios con la cual se encuentra aplicando la nota de crédito.

Podrá visualizar en el campo **Moneda**, la moneda asociada a la lista de precios seleccionada en el campo **Lista de Precios**.

Seleccione en el campo **Agente Comercial**, el agente comercial involucrado en la transacción por la cual se encuentra realizando la nota de crédito.

El checklist **Imprimir Descuento**, imprime el descuento en la factura y la orden.

Seleccione la opción **A Crédito**, para indicar como se pagará la factura.

Seleccione en el campo **Término de Pago**, el término que establece la condición, el método y tiempo de pago de la transacción que se encuentra realizando.

El checklist **Impreso en Impresora Fiscal**, indica que el documento es impreso en impresora fiscal.

Seleccione en el campo **Lista**, la opción correspondiente al registro que se encuentra realizando.

Seleccione en el campo **Factura Afectada**, la factura a la cual le será aplicada la nota de crédito que se encuentra realizando.

Introduzca en el campo **Código Sunagro**, el código de superintendencia nacional de gestión agroalimentaria.

El checklist **Documento Fiscal**, indica que el registro en el que se encuentra es un documento fiscal.

Introduzca en el campo **Control No**, el número de control fiscal establecido para el registro que se encuentra realizando.

Seleccione en el campo **Actividad**, la actividad relacionada con el registro que se encuentra realizando.

Seleccione en el campo **Centro de Costos**, el centro de costos relacionado con el registro que se encuentra realizando.

Seleccione en el campo **Región de Ventas**, la región de ventas relaconada con el registro que se encuentra realizando.

Seleccione el icono **Guardar Cambios**, ubicado en la barra de herramientas de Solop ERP, para guardar el registro de los campos de la pestaña **Factura**.

### Línea de la Factura

Seleccione la pestaña **Línea de la Factura**, para cargar los detalles de la nota de crédito que se encuentra realizando.

![Campo](/assets/img/docs/sales-management/sam-sales-image42.png)

Imagen 33. Pestaña Línea de la Factura de la Ventana Documentos por Cobrar

Podrá visualizar en el campo **No. Línea**, el número de línea correspondiente al registro que se encuentra realizando en la pestaña **Línea de la Factura**.

Seleccione en el campo **Producto**, el producto por el cual se encuentra aplicando la nota de crédito.

Seleccione en el campo **Cargo**, el cargo por el cual se encuentra aplicando la nota de crédito.

Introduzca en el campo **Descripción**, una breve descripción correspondiente al registro que se encuentra realizando.

Seleccione en el campo **Cantidad**, la cantidad relacionada al registro que se encuentra realizando.

Seleccione en el campo **UM**, la unidad de medida relacionada al registro que se encuentra realizando.

Introduzca en el campo **Precio**, el precio correspondiente a la nota de crédito que se encuentra realizando.

Podrá visualizar en el campo **Precio Actual**, el precio actual ingresado en el campo **Precio**.

Podrá visualizar en el campo **Precio de Lista**, el precio de lista oficial.

Seleccione en el campo **Impuesto**, el tipo de impuesto a aplicar en el registro que se encuentra realizando.

Seleccione en el campo **Factura Afectada**, la factura afectada para asignar la nota automáticamente.

Seleccione en el campo **Actividad**, la actividad correspondiente al registro que se encuentra realizando.

Seleccione en el campo **Centro de Costos**, el centro de costos correspondiente al registro que se encuentra realizando.

Seleccione en el campo **Amortización de Préstamo**, la amortización de préstamo.
Seleccione en el campo **Activo Fijo**, el activo fijo relacionado con el registro que se encuentra realizando.

Podrá visualizar en el campo **Neto de Línea**, el neto de la línea.

Seleccione el icono **Guardar Cambios**, ubicado en la barra de herramientas de Solop ERP, para guardar el registro de los campos de la pestaña **Línea de la Factura**.

Seleccione la pestaña principal **Factura** y ubique la opción **Completar**, en la parte inferior izquierda de la ventana.

Seleccione la acción **Completar** y la opción **OK**, para culminar el proceso.

![Campo](/assets/img/docs/sales-management/sam-sales-image62.png)

Imagen 53. Acción Completar y Opción OK de la Ventana Documentos por Cobrar

### Consultar Asignación de Nota de Crédito Aplicada

Ubique el registro de la factura asociada a la nota de crédito, en este caso se ubica la factura **76** y posteriormente seleccione la pestaña **Facturas Pagadas**.

![Campo](/assets/img/docs/sales-management/sam-sales-image63.png)

Imagen 54. Pestaña Facturas Pagadas de la Ventana Documentos por Cobrar

Haga clic contrario en el campo **Asignación** y seleccione la opción **Acercar** en el menú visualizado.

![Campo](/assets/img/docs/sales-management/sam-sales-image64.png)

Imagen 55. Acercar Asignación de Pago de la Factura por Cobrar

Podrá visualizar el registro de la asignación creada al completar el documento **Nota de Crédito de CxC**.

![Campo](/assets/img/docs/sales-management/sam-sales-image65.png)

Imagen 56. Registro de Asignación de Pago de Nota de Crédito de CxC

Seleccione la pestaña **Asignaciones**, para visualizar la información del monto de la nota de crédito aplicada a la factura.

![Campo](/assets/img/docs/sales-management/sam-sales-image66.png)

Imagen 57. Pestaña Asignaciones de la Ventana Consulta de Asignación
