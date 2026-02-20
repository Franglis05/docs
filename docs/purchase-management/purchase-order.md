---
title: Órdenes de Compra
category: Documentation
star: 9
sticky: 9
article: false
---

Esta documentación está destinada a definir cada uno de los procedimientos de la elaboración de órdenes de compra en Solop ERP para cualquier organización, es importante seguir al pie de la letra cada uno de los procedimientos descritos aquí recuerde que de eso dependerá el buen uso del ERP.

- Crear Orden de Compra desde Requisición
  - Registro de Orden de Compra desde Requisición
  - Consultar y Completar Orden de Compra Generada
- Crear Orden de Compra desde Líneas de la Requisición
  - Crear Orden de Compra desde Líneas de la Requisición
- Orden de Compra Directa
  - Registro de Orden de Compra Directa
- Orden de Compra Multimoneda

## Crear Orden de Compra desde Requisición

En Solop ERP es posible generar automáticamente mediante el proceso **Crear OC desde Requisición**, un documento de **Orden de Compra** con la información suministrada en el documento de **Requisición** previamente elaborado.

La ventana del proceso **Crear OC desde Requisición**, contiene diferentes campos que permiten generar la orden de compra según lo seleccionando en los mismos.

El proceso consiste en seleccionar el documento de requisición en el campo **Requisición de Material** y culminar el mismo seleccionando la opción **OK** para que posteriormente sea generado el documento **Orden de Compra**, indicando en la ventana del proceso el número de dicho documento.

El presente material elaborado por Solop ERP, pretende ofrecerle una explicación eficiente a nuestros clientes del procedimiento a seguir para generar en Solop ERP una orden de compra desde una requisición, en su versión 3.9.2.

- Registro de Orden de Compra desde Requisición
- Consultar y Completar Orden de Compra Generada

### Registro de Orden de Compra desde Requisición

Para ejemplificar el registro de crear orden de compra desde requisición, es utilizado el documento de requisición.

![Campo](/assets/img/docs/purchase-management/pum-purchase-image315.png)

Imagen 1. Documento de Requisición

Ubique y seleccione en el menú de Solop ERP, la carpeta **Gestión de Compras**, luego seleccione el proceso **Crear OC desde Requisición**.

![Campo](/assets/img/docs/purchase-management/pum-purchase-image316.png)

Imagen 2. Menú de Solop ERP

Podrá visualizar la ventana del proceso **Crear OC desde Requisición** con diferentes campos que pueden ser utilizados para generar la orden de compra según lo requerido por el usuario.

![Campo](/assets/img/docs/purchase-management/pum-purchase-image317.png)

Imagen 3. Ventana del Proceso Crear OC desde Requisición

Seleccione en el campo **Requisición de Material**, el documento de requisición por el cual será generado el documento de **Orden de Compra**.

Seleccione en el campo **Organización**, la organización para la cual esta realizando el documento **Orden de Compra**.

Seleccione en el campo **Almacén**, el nombre del almacén donde serán almacenados los productos registrados en el documento de requisición seleccionado.

Para generar una orden de compra desde una requisición determinada, los campos principales son **Requisición de Material**, **Organización** y **Almacén**. La selección de los campos **F. Documento**, **Fecha Requerida**, **Prioridad**, **Usuario**, **Producto**, **Categoría del Producto** y **Grupo de Socio del Negocio**, quedan a criterio de lo requerido por el usuario. De igual forma el checklist **Consolidado en un Documento**.

Seleccione la opción **OK**, para generar la orden de compra desde la requisición seleccionada anteriormente.

Podrá visualizar en la ventana del proceso **Crear OC desde Requisición**, el número del documento de **Orden de Compra** generado.

### Consultar y Completar Orden de Compra Generada

Ubique y seleccione en el menú de Solop ERP, la carpeta **Gestión de Compras**, luego seleccione la ventana **Órdenes de Compra**.

![Campo](/assets/img/docs/purchase-management/pum-purchase-image323.png)

Imagen 9. Menú de Solop ERP

Al buscar el documento **Orden de Compra** con ayuda del número de documento generado en la ventana del proceso **Crear OC desde Requisición**, se puede visualizar el mismo de la siguiente manera.

![Campo](/assets/img/docs/purchase-management/pum-purchase-image324.png)

Imagen 10. Orden de Compra Generada desde el Proceso Crear OC desde Requisición

::: tip
El proceso genera el documento **Orden de Compra** en estado **Borrador** y la opción establecida de estado del documento es **Preparar**.
:::

Seleccione en el campo **Agente Compañía**, el usuario que esta realizando la orden de compra.

Seleccione la pestaña **Línea Orden Compra**, para ingresar el precio unitario de los productos solicitados.

![Campo](/assets/img/docs/purchase-management/pum-purchase-image326.png)

Imagen 12. Pestaña Línea Orden Compra

Introduzca en el campo **Precio**, el precio unitario de los productos solicitados en el documento **Requisición**.

Seleccione la pestaña **Orden de Compra** para regresar a la ventana principal del registro, luego seleccione la opción **Preparar**, ubicado en la parte inferior derecha del documento para completar el mismo.

![Campo](/assets/img/docs/purchase-management/pum-purchase-image328.png)

Imagen 14. Opción Preparar

Seleccione la acción **Completar** y la opción **OK**, para completar el documento **Orden de Compra**.

### Crear Orden de Compra desde Líneas de la Requisición

En Solop ERP es posible generar automáticamente mediante el proceso **Crear Orden de Compra desde Líneas de la Requisición**, un documento de **Orden de Compra** con la información suministrada en el documento de **Requisición** previamente elaborado.

El presente material elaborado por Solop ERP, pretende ofrecerle una explicación eficiente a nuestros clientes del procedimiento a seguir para generar en Solop ERP una orden de compra desde las líneas de la requisición.

Crear Orden de Compra desde Líneas de la Requisición

### Crear Orden de Compra desde Líneas de la Requisición

Para ejecutar el procedimiento de manera correcta, debe existir obligatoriamente un registro de requisición en estado **Completo**.

![Campo](/assets/img/docs/purchase-management/pum-purchase-image330.png)

Imagen 1. Requisición

Dicha requisición contiene dos (2) líneas.

![Campo](/assets/img/docs/purchase-management/pum-purchase-image331.png)

Imagen 2. Pestaña Línea Requisición

Ubique y seleccione en el menú de Solop ERP, la carpeta **Gestión de Compras**, luego seleccione el proceso **Crear Orden de Compra desde líneas de la Requisición**.

![Campo](/assets/img/docs/purchase-management/pum-purchase-image332.png)

Imagen 3. Menú de Solop ERP

Podrá visualizar la ventana del proceso **Crear Orden de Compra desde líneas de la Requisición**, con diferentes campos que le permite al usuario filtrar la información en base a lo requerido para generar la orden de compra con las líneas seleccionadas de dicha requisición.

![Campo](/assets/img/docs/purchase-management/pum-purchase-image333.png)

Imagen 4. Ventana del Proceso Crear Orden de Compra desde Líneas de Requisición

Introduzca en el campo **No. del Documento**, el número de documento de la requisición por la cual requiere filtrar la información.

Seleccione en el campo **Organización**, la organización para la fue realizada la requisición.

Seleccione en el campo **Tipo de Documento**, el tipo de documento con el cual fue generada la requisición.

Seleccione en el campo **Prioridad**, la prioridad con la cual fue generada la requisición.

Seleccione en el campo **Fecha Requerida**, la fecha en la que fueron requeridos los productos cargados a las líneas de la requisición.

Seleccione en el campo **F. Documento**, la fecha en la que fue generado el documento de requisición.

Seleccione en el campo **Usuario**, el usuario que genero el documento de requisición.

Seleccione en el campo **Almacén**, el almacén utilizado para generar la requisición.

Seleccione en el campo **Lista de Precios**, la lista de precios utilizada para generar la requisición.

Introduzca en el campo **Descripción**, la descripción ingresada en la requisición.

Introduzca en el campo **Total de Líneas**, el total de las líneas de la requisición.

Seleccione en el campo **Socio del Negocio**, el socio del negocio seleccionado en las líneas de la requisición.

Seleccione en el campo **Orden de Venta**, la orden de venta relacionada a la requisición.

Seleccione en el campo **Producto**, el producto seleccionado en las líneas de la requisición.

Seleccione en el campo **Cargo**, el cargo relacionado a la requisición.

Introduzca en el campo **Cantidad**, la cantidad del producto ingresada en las líneas de la requisición.

Introduzca en el campo **Neto de Línea**, el neto de la línea de la requisición.

Seleccione en el campo **Organización de la Transacción**, la organización de la transacción de la requisición.

Seleccione en el campo **Actividad**, la actividad por la cual requiere filtrar la información.

Seleccione en el campo **Campaña**, la campaña por la cual requiere filtrar la información.

Seleccione en el campo **Proyecto**, el proyecto por el cual requiere filtrar la información.

Seleccione en el campo **Centro de Costos**, el centro de costos por el cual requiere filtrar la información.

Seleccione en el campo **Usuario 2**, el usuario dos (2) por el cual requiere filtrar la información.

Seleccione en el campo **Usuario e**, el usuario tres (3) por el cual requiere filtrar la información.

Seleccione en el campo **Usuario 4**, el usuario cuatro (4) por el cual requiere filtrar la información.

Seleccione la opción **Comenzar Búsqueda**, para filtrar la información en base a lo seleccionado en los campos nombrados anteriormente.

Podrá visualizar los resultados de la búsqueda, donde se refleja la información ingresada en las líneas de la requisición.

![Campo](/assets/img/docs/purchase-management/pum-purchase-image360.png)

Imagen 31. Resultados de Búsqueda

Seleccione las líneas de la requisición para crear la orden de compra desde las mismas.

::: tip
Al seleccionar cualquiera de los registros, se habilitan diferentes campos que le permiten al usuario ingresar o modificar los valores en los mismos.
:::

Seleccione en el campo **Tipo de Documento**, el tipo de documento con el cual será generado el documento **Orden de Compra**.

![Campo](/assets/img/docs/purchase-management/pum-purchase-image362.png)

Imagen 33. Campo Tipo de Documento

Seleccione en el campo **Prioridad**, la prioridad con la cual será generado el documento **Orden de Compra**.

Seleccione en el campo **Socio del Negocio**, el socio del negocio con el cual será generada la orden.

Seleccione en el campo **Dirección del Socio del Negocio**, la dirección del socio del negocio seleccionado para la orden.

Seleccione en el campo **Fecha de la Orden**, la fecha de la orden con la cual será generada la orden.

Seleccione en el campo **Fecha Prometida**, la fecha prometida con la cual será generada la orden.

Seleccione en el campo **Agente Comercial**, el agente comercial con el cual será generada la orden.

Seleccione en el campo **Termino de Pago**, el termino de pago con el cual será generado el documento **Orden de Compra**.

Seleccione en el campo **Lista de Precios**, la lista de precios con la cual será generada la orden.

Introduzca en el campo **Referencia de Orden de Socio del Negocio**, la referencia de orden de socio del negocio.

Seleccione en el campo **Acción del Documento**, la acción de documento con la cual será generado al documento **Orden de Compra**.

Seleccione la opción **OK**, para generar el documento **Orden de Compra** en base a lo seleccionado en los campos nombrados anteriormente.

Al ubicar en la ventana **Órdenes de Compra**, el registro de la orden de compra creado, podrá visualizar que el mismo fue generado en estado **Borrador**.

![Campo](/assets/img/docs/purchase-management/pum-purchase-image374.png)

Imagen 45. Registro de Orden de Compra

Seleccione la pestaña **Línea Orden Compra**, de la ventana **Órdenes de Compra**.

![Campo](/assets/img/docs/purchase-management/pum-purchase-image375.png)

Imagen 46. Pestaña Línea de Orden

Introduzca en el campo **Precio**, el precio del producto correspondiente al registro de la línea en la que se encuentra.

::: tip
Recuerde guardar el registro de los campos en pestaña **Línea Orden Compra**
:::

Seleccione la pestaña principal **Orden de Compra** para proceder a completar el registro.

Seleccione la opción **Preparar**, ubicado en la parte inferior de la ventana **Órdenes de Compra**.

Seleccione la acción **Completar** y la opción **OK**, para completar el proceso.

![Campo](/assets/img/docs/purchase-management/pum-purchase-image379.png)

Imagen 50. Acción Completar y Opción OK

## Orden de Compra Directa

Una orden de compra es un documento elaborado por el departamento de compras de una empresa determinada, contiene los productos y servicios que dicha empresa necesita, la cantidad y los precios acordados con el proveedor a la que va dirigida, así como el sello del departamento de compras y la firma del jefe de dicho departamento.

En Solop ERP es posible generar una orden de compra directa. El presente material elaborado por Solop ERP, pretende ofrecerle una explicación eficiente a nuestros clientes del procedimiento a seguir para generar en Solop ERP una orden de compra, en su versión 3.9.2.

Registro de Orden de Compra Directa

### Registro de Orden de Compra Directa

Una Orden de Compra en Solop ERP, es un tipo de documento emitido por la empresa para realizar pedidos a sus diferentes proveedores. En ella se detalla: la cantidad a comprar, el tipo de producto, precio y condiciones de pago, así como también la forma de entrega.

Para el registro de un documento en Solop ERP debe tener en cuenta que existen campos que son de carácter obligatorio, estos campos están identificados con el carácter especial:(\*) de color rojo.

::: tip
Asegúrese de que cada campo que se encuentre identificado como carácter obligatorio, contenga la información requerida, de lo contrario no podrá completar el registro.
:::

Ubique en el menú de Solop ERP la carpeta **Gestión de Compras**, luego seleccione la ventana **Órdenes de Compra**, adjunto imagen para referencia.

Seleccione el icono **Registro Nuevo** en la barra de herramientas de Solop ERP para crear un nuevo documento.

![Campo](/assets/img/docs/purchase-management/pum-purchase-image381.png)

Imagen 2. Registro Nuevo

Seleccione en el campo **Compañía**, el nombre de la compañía de la cual se emite el documento **Orden de Compra**.

Seleccione en el campo **Organización**, el nombre de la organización de la cual se está emitiendo el documento **Orden de Compra**.

El valor en el campo organización debe ser diferente del símbolo (\*) ya que éste símbolo hace referencia a todas las Organizaciones.

En el campo **No. de Documento**, no es necesario ingresarlo en forma manual, al momento de realizar un registro, Solop ERP genera un número de secuencia automáticamente para el documento, al seleccionar la opción guardar del nuevo registro de orden de compra.

En el campo **Descripción**, Puede introduzca una breve descripción referente a la orden de compra que se está realizando, este campo es opcional.

Seleccione el tipo de documento a generar, en el campo **Tipo de Documento Destino**, la selección de éste define el comportamiento del documento que se está elaborando, dicho comportamiento se encuentra definido en el documento Tipo de Documento elaborado por Solop ERP

Seleccione en el campo **Fecha de la Orden**, la fecha de elaboración del documento **Orden de Compra**.

Seleccione en el campo **Fecha Prometida**, la fecha de entrega de la orden, prometida por el proveedor.

En el campo **Socio del Negocio**, debe seleccionar el nombre del socio del negocio (proveedor) al que se le emite el documento **Orden de Compra**.

Si el Socio de negocio, tiene más de una dirección registrada, debe seleccionar la dirección del socio del negocio, caso contrario, si posee dirección única, esta información se refleja automáticamente en el campo **Dirección del Socio del Negocio** una vez haya seleccionado el nombre del socio de negocio.

En la sección de **Entrega**, se encuentran los siguientes grupos de campos: almacén, entrega directa y usuario, estos hacen referencia a:

* Almacén, en el cual se requiere el producto o servicio (Es de Carácter obligatorio)

* Entrega Directa, Indica que el proveedor realizará la entrega directamente al cliente.

* Usuario, Indica el Nombre del usuario de sistema.

En el campo seleccionable **Vía de Entrega**, debe seleccionar la opción que indique, de qué manera serán entregados los productos o servicios de la orden.

En el campo seleccionable **Regla de Costo de Flete**, debe seleccionar la regla para cargar los costos del flete, por lo general se establece: Flete Incluido.

Seleccione la prioridad de la orden en el campo **Prioridad**, este campo indica la urgencia de los productos o servicios que se están ordenando en el documento, sin embargo, el documento trae predeterminado la opción **Media**.

En la sección de **Facturación**, se encuentran los siguientes grupos de campos, (Todos de carácter obligatorio, para el registro de la orden que será emitida)

**Lista de Precios**, siempre debe ser Compras, esta determina el precio, margen y costo de los artículos comprados.

**Moneda**, dependerá del Tipo de Documento seleccionado, es decir, si el tipo de documento es : **Orden de Compra Nacional** la moneda será (VES) moneda nacional en curso. Caso contrario, **Orden de Compra Importación** la moneda será, cualquier moneda extranjera que sea utilizada por la compañía para realizar este tipo de compras, ejemplo:(USD,EUR,COP, entre otros).

**Agente de la Compañía**, será el agente de compras para el documento.

**Término de pago**, indica las condiciones, método y tiempo de pago de la compra.

Recuerde guardar el registro de la ventana, seleccionando el icono **Guardar** ubicado en la barra de herramientas, una vez guardado el nuevo registro, podrá avanzar a la pestaña **Línea Orden Compra**.

Seleccione la pestaña **Línea Orden Compra** y proceda seleccionando el Producto o Servicio a ordenar. Si la orden de compra contiene varios productos, el campo **Nro. de Línea**, indicará el orden y despliegue de los mismos dentro del documento. Una vez que guarde el primer producto, deberá seleccionar nuevo, incrementando así el número de líneas por productos en el documento.

Los campos **Compañía**, **Organización**, **Orden de Compra**, **Socio del Negocio** y **Dirección del Socio del Negocio**, vienen precargados de la ventana principal **Orden de Compra**.

![Campo](/assets/img/docs/purchase-management/pum-purchase-image401.png)

Imagen 22. Línea Orden Compra

En la Sección **Cantidades**, se encuentra el siguiente grupo de Campos: cantidad, unidad de medida, cantidad ordenada, cantidad facturada. cantidad reservada y cantidad entregada.

**Cantidad**, indica la cantidad del producto en la compra.

\*\*Unidad de Medida, indica la unidad de medida del producto ordenado.

\*\*Cantidad Facturada, indica la cantidad de un producto que ha sido facturado.

\*\*Cantidad Reservada, indica la cantidad del producto que ha sido reservado para otras órdenes.

\*\*Cantidad Entregada, indica la cantidad de un producto que ha sido entregado.

En la sección Cantidades, solo deberá ingresar la información en el primer campo, el cual es Cantidad. Los demás, presentaran movimientos sólo sí se se han realizado para la orden de compra, más de una recepción, en relación a la cantidad total de la compra.

Seleccione en el campo **Cantidad**, la cantidad a ordenar del producto o servicio seleccionado.

Seleccione la unidad de medida del producto seleccionado en el campo **UM**, esta puede ser unidad, gramos, kilos, toneladas, entre otras.

En la Sección **Totales** se encuentran los siguientes grupos de campos:

**Precio**, este precio está basado en la unidad de medida.

**Precio de Costo**, indica el precio por unidad de medida, incluyendo todos los costos (Fletes, Traslados, entre otros)

**Precio Actual**, indica el precio para un producto en la moneda fuente.

**Precio Lista**, indica el precio de la lista oficial en la moneda del documento.

**Impuesto**, indica el tipo de impuesto para esta línea del documento.

**Descuento**, indica el impuesto aplicado o tomado como un porcentaje.

Introduzca el precio unitario del producto seleccionando en el campo **Precio**, este precio es el establecido por el socio del negocio proveedor.

Seleccione el impuesto en el campo **Impuesto**, este puede variar dependiendo del impuesto aplicable al producto seleccionado.

Recuerde guardar el registro de la pestaña **Línea Orden Compra** con el icono **Guardar** de la barra de herramientas de Solop ERP, antes de cambiar a la ventana principal **Orden de Compra**.

Regrese a la ventana principal **Orden de Compra** y seleccione la opción **Completar** ubicada en la parte inferior derecha del documento.

## Orden de Compra Multimoneda

Ubique y seleccione en el menú de Solop ERP, la carpeta **Gestión de Compras**, luego seleccione la ventana **Órdenes de Compra**.

Seleccione el icono **Registro Nuevo** en la barra de herramientas de Solop ERP para crear un nuevo documento.

Seleccione en el campo **Organización**, el nombre de la organización de la cual se está emitiendo el documento **Orden de Compra Multimoneda**.

El valor en el campo organización debe ser diferente del símbolo (\*) ya que éste símbolo hace referencia a todas las Organizaciones.

En el campo **No. de Documento**, no es necesario ingresarlo en forma manual, al momento de realizar un registro, Solop ERP genera un número de secuencia automáticamente para el documento, al seleccionar la opción guardar del nuevo registro de orden de compra multimoneda.

En el campo **Descripción**, Puede introduzca una breve descripción referente a la orden de compra multimoneda que se está realizando, este campo es opcional.

Seleccione el tipo de documento a generar, en el campo **Tipo de Documento Destino**, la selección de éste define el comportamiento del documento que se está elaborando, dicho comportamiento se encuentra definido en el documento Tipo de Documento elaborado por Solop ERP.

Para realizar una orden de compra multimoneda, puede ser utilizado cualquier tipo de documento de orden de compra.

Seleccione en el campo **Fecha de la Orden**, la fecha de elaboración del documento **Orden de Compra Multimoneda**.

Seleccione en el campo **Fecha Prometida**, la fecha de entrega de la orden, prometida por el proveedor.

En el campo **Socio del Negocio**, debe seleccionar el nombre del socio del negocio (proveedor) al que se le emite el documento **Orden de Compra Multimoneda**.

Seleccione en el campo **Socio del Negocio a Facturar**, el socio del negocio a facturar.

Si el socio de negocio, tiene más de una dirección registrada, debe seleccionar la dirección del socio del negocio, caso contrario, si posee dirección única, esta información se refleja automáticamente en el campo **Dirección del Socio del Negocio** una vez haya seleccionado el nombre del socio de negocio.

Seleccione en el campo **Dirección Factura**, la dirección del socio del negocio para la factura.

Seleccione en el campo **Usuario**, el usuario del socio del negocio seleccionado.

Seleccione en el campo **Contacto Entrega Directa**, el usuario de contacto para la entrega directa.

Seleccione en el campo **Almacén**, el almacén en el cual se requiere el producto o servicio

Seleccione el check **Entrega Directa**, que indica que el proveedor realizará la entrega directamente al cliente.

La selección de este check es obligatoria y permite generar un documento por pagar (factura), en una moneda diferente a la moneda de la orden de compra.

De no ser tildado el check **Entrega Directa**, no se podrá generar un documento por pagar (factura) con una moneda diferente a la moneda con la que fue realizada la orden de compra.

Al tildar el check **Entrega Directa**, se habilitan los siguientes campos

Seleccione en el campo **Socio del Negocio Entrega Directa**, el socio del negocio al cual serán entregados los productos incluidos en la orden.

Seleccione en el campo **Dirección Entrega Directa**, la dirección de localización del socio para la entrega.

Seleccione en el campo **Contacto Entrega Directa**, el usuario de contacto del socio para la entrega.

En el campo seleccionable **Vía de Entrega**, debe seleccionar la opción que indique, de qué manera serán entregados los productos o servicios de la orden.

En el campo seleccionable **Regla de Costo de Flete**, debe seleccionar la regla para cargar los costos del flete, por lo general se establece: Flete Incluido.

Seleccione la prioridad de la orden en el campo **Prioridad**, este campo indica la urgencia de los productos o servicios que se están ordenando en el documento, sin embargo, el documento trae predeterminado la opción **Media**.

Seleccione en el campo **Lista de Precios**, la lista de precios con la cual será generada la orden de compra.

Por tratarse de una orden de compra multimoneda, la lista de precios que se debe seleccionar debe ser **Compras (USD)** o **Compras (UYU)**. Esta determina el precio, margen y costo de los artículos comprados.

El valor en el campo **Moneda**, dependerá de la lista de precios seleccionada en el campo **Lista de Precios**.

El campo se encuentra solo lectura por lo que su valor solo puede ser modificado cambiando la lista de precios para establecer en el mismo, cualquier moneda extranjera que sea utilizada por la compañía para realizar este tipo de compras..

Seleccione en el campo **Tipo de Conversión**, el tipo de conversión con el cual fue negociada la compra con el proveedor.

Recuerde que debe tener creado el tipo de conversión con su respectiva tasa de conversión antes de completar el proceso. Si desconoce el procedimiento, puede consultar el material Conversión Manual, el mismo explica de manera detallada los procesos a realizar para crear un Tipo de Conversión, su Tasa de Conversión desde la Ventana Moneda y su Tasa de Conversión desde la Ventana Tasa de Cambio.

Seleccione en el campo **Agente Compañía**, el agente de compras para el documento.

Seleccione el check **Imprimir Descuento**, para imprimir el descuento en la factura y la orden.

Seleccione en el campo **Término de pago**, las condiciones, método y tiempo de pago de la compra.

Recuerde guardar el registro de la ventana, seleccionando el icono **Guardar** ubicado en la barra de herramientas, una vez guardado el nuevo registro, podrá avanzar a la pestaña **Línea Orden Compra**.

Seleccione la pestaña **Línea Orden Compra** y proceda al llenado de los campos seleccionando el producto o servicio a ordenar. Si la orden de compra contiene varios productos, el campo **Nro. de Línea**, indicará el orden y despliegue de los mismos dentro del documento. Una vez que guarde el primer producto, deberá seleccionar el icono **Registro Nuevo**, incrementando así el número de líneas por productos en el documento.

Los campos **Compañía**, **Organización**, **Orden de Compra**, **Socio del Negocio** y **Dirección del Socio del Negocio**, vienen precargados de la ventana principal **Orden de Compra**.

Seleccione en el campo **Producto**, el producto correspondiente a la orden de compra que se encuentra realizando.

Introduzca en el campo **Cantidad**, la cantidad del producto seleccionado.

Seleccione en el campo **Unidad de Medida**, la unidad de medida del producto seleccionado.

Esta unidad de medida puede ser unidad, gramos, kilos, toneladas, entre otras.

En el campo **Cantidad Ordenada**, se indica la cantidad ordenada del producto seleccionado.

Este campo toma de manera automática, el valor ingresado en el campo **Cantidad**.

En el campo **Cantidad Entregada**, se indica la cantidad del producto que ha sido recepcionada.

Este campo estará en cero (0), hasta que sea generado un documento de recepción con dicho producto, asociando la orden de compra.

En el campo **Cantidad Reservada**, se indica la cantidad del producto que ha sido reservado para otras órdenes.

Seleccione en el campo **Cantidad Facturada**, la cantidad de un producto que ha sido facturado.

Este campo estará en cero (0), hasta que sea generado un documento de cuentas por pagar (factura) con dicho producto, asociando la orden de compra.

Introduzca en el campo **Precio**, el precio del producto seleccionado.

Este precio está basado en la unidad de medida del producto, lo que quiere decir, que si el producto seleccionado tiene unidad de medida **Caja** y dicha caja contiene seis (6) unidades, Solop ERP tomará el precio ingresado como precio de la caja y no como precio de cada unidad que compone la caja.

Introduzca en el campo **Precio de Costo**, el precio de costo del producto seleccionado.

Este precio indica el precio por unidad de medida, incluyendo todos los costos (fletes, traslados, entre otros)

En el campo **Precio Actual**, se indica el precio para un producto en la moneda fuente.

Introduzca en el campo **Precio Lista**, el precio de lista oficial en la moneda del documento.

Seleccione en el campo **Impuesto**, el tipo de impuesto para esta línea del documento.

Introduzca en el campo **Descuento**, el descuento aplicado o tomado como un porcentaje.

En el campo **Neto de Línea**, se indica el total neto de la línea basado en la cantidad y el precio actual. Cualquier cargo adicional o flete no es incluido.

Recuerde guardar el registro de la pestaña **Línea Orden Compra** con el icono **Guardar** de la barra de herramientas de Solop ERP, antes de cambiar a la ventana principal **Orden de Compra**.

Regrese a la pestaña principal **Orden de Compra** y seleccione la opción **Completar** ubicada en la parte inferior derecha del documento.

Seleccione la acción **Completar** y la opción **OK**.