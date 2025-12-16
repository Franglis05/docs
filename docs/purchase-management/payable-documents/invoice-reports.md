---
title: Reportes de Facturas
category: Documentation
star: 9
sticky: 9
article: false
---

### Concepto

Los reportes de facturas son listados que que nos brindan información detallada sobre las diferentes facturas de Venta o Compra.
Se utilizan para obtener una vista parametrizada (por fecha, por Socio del negocio, por estado, etc.) de los diferentes registros con su información detallada de entidades relacionadas, importes y estado.
Cada reporte mantiene sus particularidades y sirven a distintas finalidades (de acuerdo a su nivel de detalle).

### Unbilled General

Este reporte muestra todas las Entregas/Recepciones que tengan líneas que aún no cuenten con un Match invoice realizado, que lo vincule con una Factura. O sea, Entregas/Recepciones pendiente de facturar

Se podrá obtener el mismo reporte tanto para Ventas como para Compras mediante el check de “Transacción de Ventas = SI/NO”

**Devoluciones (de Cliente/Proveedor)**

Las devoluciones de cliente y proveedor se muestran de igual manera que entregas y recepciones, pero con signo negativo.

#### Vistas (aplican al ordenamiento de datos, y se pueden crear las que sean necesarias):

* Unbilled General por Moneda y SDN
* Unbilled General por Contrato Moneda y Proyecto
* Unbilled General por Sello, Moneda y Proyecto

**Unbilled General por Contrato y Moneda**

Muestra el total pendiente de facturar en moneda contable, agrupado por contrato.

Se utiliza para comparar con el IF 120 Monitor de Venta columna Unbilled

**Unbilled General por Contrato, Moneda y Proyecto**

Muestra el total pendiente de facturar en moneda contable, agrupado por Proyecto

Se utiliza para comparar con el IF 121 Monitor de Venta por Proyecto, ingresando su contrato,  columna Unbilled.

**FIltros de OV que considera**

Estos son los tipos de documentos que filtra:

* "Orden de Venta (Compra y Consumo)"
* "OV Compra Consumo (Factura Medio-Cliente)"
* "OV Consumo Paquete"
* "OV Split Manual"
* "Orden de Venta con Aprobación"
* "Orden de Venta Intercompany"
* "Orden de Venta Honorarios"
* "Orden de Venta Fee"

### Facturas Cliente sin Entrega

Este tipo de reporte es común en empresas que venden productos o servicios y emiten facturas antes de que se realice la entrega o cumplimiento de la transacción.

Muestra Documentos Órdenes de Venta (Estado Completo o Cerrado) que ya tienen Factura emitida al Cliente (completa) pero que aún no se han Entregado al cliente (no tiene una entrega completa). O sea, Órdenes con factura y con entrega pendiente.

Columnas:

* Organización
* Sello Proyecto
* Proyecto
* Sello Orígen
* SdN
* SdN entrega Directa
* Nro.OV
* Nro. Factura
* Moneda
* Monto OV
* Monto Factura
* Monto entregado
* Monto facturado no entregado

#### Finalidad del reporte

El propósito principal del reporte de "Facturas Cliente Sin Entrega" es brindar información sobre las transacciones pendientes de entrega a clientes, incluyendo:

Detalle de las facturas: Muestra información detallada sobre cada factura emitida a clientes, como el número de factura, la fecha de emisión, el monto total, los productos o servicios incluidos, los impuestos aplicados y las condiciones de pago.

Estado de la entrega: Indica si la entrega física de los productos o la prestación de los servicios asociados a cada factura se ha completado o si está pendiente de realizarse.

Control de inventario: Ayuda a gestionar el inventario al identificar las ventas realizadas que aún no han sido entregadas, lo que permite planificar la logística de distribución y garantizar la disponibilidad de productos para satisfacer las órdenes de entrega.

Seguimiento de cobros: Facilita el seguimiento de los cobros pendientes asociados a las facturas emitidas, ya que las ventas pueden haberse realizado pero el pago aún no se ha efectuado debido a que la entrega está pendiente.

Gestión de clientes: Permite gestionar de manera eficiente las relaciones con los clientes al tener visibilidad sobre las transacciones pendientes de entrega, lo que facilita la comunicación con los clientes y el cumplimiento de los compromisos comerciales.

### Facturas Proveedor sin Entregar

Funcionamiento idéntico a “Facturas Clientes sin Entregar”, pero aplicado para documentos de proveedor (Documentos ordenes de compra en estado completo/cerrado con factura proveedor emitida pero sin recepción). O sea, Órdenes con factura y con entrega pendiente.

No se consideran en el reporte los tipos de documento de factura que tienen categoría de contabilidad “AP Invoice - Nota de Débito”.

#### Vistas (aplican al ordenamiento de datos, y se pueden crear las que sean necesarias):

* Unbilled General por SDN y Moneda, Contrato y Proyecto
* Unbilled General por Moneda y SDN
* Unbilled General por Moneda, Contrato y Proyecto

### Trade Creditors

* Nombre Reporte: Trade Creditors
* Descripción del Reporte: Órdenes de compra con factura pendiente de pago.
* Ayuda del Reporte: Muestra Órdenes con factura emitidas e impagas.
* Nombre en Menú: Trade Creditors

* Documentación: Muestra Órdenes de Compra que tienen un Proyecto asociado de Categoría (Agencia Creativa), cuyo Documento por Pagar aún está pendiente de Pago y tiene al menos una Recepción. O sea Órdenes con factura emitidas e impagas

#### Vistas (aplican al ordenamiento de datos, y se pueden crear las que sean necesarias):

* Unbilled General por SDN y Moneda
* Unbilled General por Moneda y SDN
* Unbilled General por Moneda, Contrato y Proyecto

### Billing de Cliente por Producto

Este Listado clasifica la facturación por Cliente desglosando lo facturado según Categoría de Producto y el Soporte.

#### Vistas (aplican al ordenamiento de datos, y se pueden crear las que sean necesarias):

* Billings por Producto y Moneda
* Billings por Tipo de Billing
* Billings por Grupo de Productos

### Detalles de Facturas y Margen

El informe refleja los detalles de las facturas de clientes y proveedores con márgenes (descuentos).
Muestra todas las facturas y sus líneas vinculadas con sus Órdenes.

En este reporte se podrán obtener todas las facturas emitidas entre determinadas fechas.
Podrán ser Documentos por cobrar o por pagar, dependiendo si se selecciona Transacción de Ventas SI o NO.

![Detalles de Facturas y Margen](/assets/img/docs/purchase-management/pum-reports3.png)

#### Detalle de Columnas que integran el reporte

|         Columna        |              Descripción                   |                            Ayuda                                 |  
| ---------------------- | ------------------------------------------ | ---------------------------------------------------------------- |
|   Socio del Negocio    |       Identifica un Socio del Negocio      | Persona con quien realiza transacciones. Cliente, proveedor, etc |
| Grupo de Socio del Neg |     ID del Grupo de Socio del Negocio      | Proporciona un método de definir valores para conjuntos de SDN   |
|       Producto         |       Producto, Servicio, Artículo         |        Identifica un artículo que se compra o vende              |
| Categoría del Producto |          Categoría de ese producto         |   Identifica Categoría del Producto para cálculo de precio       |
|        Cantidad        |  La cantidad se basa en la UM seleccionada |  La cantidad se convierte a la cantidad baja de UM del producto  |
|        Precio          |         Precio basado en la UM             | El precio ingresado convierte a precio real por conversión de UM |
|   Precio de Lista      |          Valor de Lista de Precio          |    Es el precio de lista oficial en la moneda del documento      |
|    Neto de Línea       |    Monto de línea sin flete ni cargos      | Monto de línea según cantidad y precio (Cantidad * Precio actual)|
|     Importe Margen     |             Valor Margen                   |    Diferencia entre precio Actual y Límite * por la Cantidad     |
|     Tipo Documento     |        Tipo de documento o reglas          |  Determina la secuencia del documento y las reglas de proceso    |
|        Factura         |      	Identificador de la factura       |  La ID de Factura identifica únicamente un documento de Factura  |
| Transacción de Ventas  |    Identifica tipo de transacción          |      Informa si la transacción es de Venta o Compra (SI/NO)      |

### Facturas Cobradas sin pagar a Proveedores

Este reporte visualiza las Órdenes de Venta cuyos Documentos por Cobrar se encuentren en un recibo de cobro en estado completo (cobrados), en relación a Documentos por Pagar completos, asociados a las Órdenes de Compra enlazadas a dichas Orden, que aún no estén pagados. Es decir, Facturas de Proveedor en relación a facturas de Cliente cobradas

### Facturas Cobradas a Cliente sin recibir Factura Proveedor

Este reporte mira los Documentos por Cobrar vinculados a las Órdenes de Venta que estén en un recibo de cobro Completo. A su vez, muestra registros si las respectivas Órdenes de Compra tienen líneas que no estén vinculadas a líneas de Documentos por Pagar. Si la Orden de Compra tiene todas sus líneas vinculadas a Documento por Cobrar, entonces no aparecerá en el reporte.

### Diario Compras y Ventas

Reporte contable donde se registran todas las operaciones relacionadas con compras y ventas que realiza una empresa durante un período específico, generalmente diario, semanal o mensual. Este registro es fundamental en contabilidad para llevar un control detallado de las transacciones comerciales de una empresa.

Este informe muestra todos los Documentos por Pagar o Documentos por Cobrar emitidos, mostrando de forma separada los importes fuentes, tasas de cambio del documento y los valores contables.

![Diario Compras y Ventas](/assets/img/docs/purchase-management/pum-reports4.png)

#### Finalidad del reporte

El "Diario de Compras y Ventas" sirve para varios propósitos importantes:

Registro de transacciones: Permite registrar todas las transacciones de compras y ventas realizadas por la empresa, incluyendo la fecha, descripción de la operación, proveedores o clientes involucrados, cantidades, precios unitarios, importes totales y condiciones de pago.

Control de cuentas por pagar y por cobrar: Facilita el control de las cuentas por pagar a proveedores y las cuentas por cobrar a clientes al registrar las operaciones de compra y venta de bienes o servicios a crédito.

Análisis de cash flow: Ayuda a analizar el cash flow de la empresa al registrar las operaciones de compra de inventario, pago de proveedores, ventas de productos o servicios, y cobro de clientes.

Registro de impuestos: Permite cumplir con las obligaciones fiscales al registrar las operaciones sujetas a impuestos, como el IVA (Impuesto al Valor Agregado) en el caso de Argentina, y calcular los montos a pagar o a recuperar.

Base para estados financieros: Sirve como base para preparar estados financieros como el Estado de Resultados y el Balance General, al proporcionar información detallada sobre las transacciones comerciales de la empresa.

#### Vistas (aplican al ordenamiento de datos, y se pueden crear las que sean necesarias):

* Por Documento
* Por Día
* Por Impuesto

#### Detalle de Columnas que integran el reporte (vista ejemplo: por documento)

|         Columna        |              Descripción                   |                            Ayuda                                 |  
| ---------------------- | ------------------------------------------ | ---------------------------------------------------------------- |
|         Número         |          Número del Documento              |          Número de secuencia del documento para cada registro    |
|     Tipo Documento     |        Tipo de documento o reglas          |  Determina la secuencia del documento y las reglas de proceso    |
|   Socio del Negocio    |       Identifica un Socio del Negocio      | Persona con quien realiza transacciones. Cliente, proveedor, etc |
|       F.Facturación    |        Fecha impresa en la factura         |   La fecha de la factura indica la fecha impresa en la factura   |
|      	Impuesto         |         Identificador del Impuesto         |    Indica el tipo de impuesto para esta línea del documento      |
|          Tasa          |   	  Tasa, impuesto o conversión         |	Porcentaje a ser multiplicado por la fuente para la conversión   |
|Total Base del Impuesto |  Base para calcular el total del impuesto  |   Indica el total base usado para calcular el total de impuesto  |
|    Total Impuesto      |   Total del impuesto para un documento     |         Despliega el total de impuesto para un documento         |


### Reporte de Notas de Crédito Emitidas a Clientes

Este informe muestra las Notas de Crédito emitidas a clientes con asignación.

### Transacción de Facturas

Este informe muestra los cabezales de facturas por fecha contable, incluyendo su información detallada y estado.

![Reporte de NC](/assets/img/docs/purchase-management/pum-reports5.png)

### Resumen de Facturas

Reporte que recopila de manera resumida la información clave relacionada con las transacciones de compras y ventas de una empresa. Este resumen proporciona una visión general de las facturas emitidas a clientes y recibidas de proveedores durante un periodo determinado.

Más específicamente, este informe muestra los cabezales de facturas por fecha de factura, incluyendo su información detallada, entidades relacionadas y estado.

![Resumen de facturas](/assets/img/docs/purchase-management/pum-reports6.png)

#### Finalidad del reporte

El propósito principal del resumen de "Facturas Cliente y Proveedor" es brindar una visión panorámica de las transacciones comerciales de la empresa, incluyendo:

Facturas a clientes: Incluye un resumen de todas las facturas emitidas a clientes durante el periodo especificado, mostrando información como el número de factura, la fecha de emisión, el monto total facturado, los productos o servicios vendidos, los impuestos aplicados y las condiciones de pago.

Facturas de proveedores: También presenta un resumen de las facturas recibidas de proveedores en el mismo periodo, indicando el número de factura, la fecha de recepción, el monto total facturado por los productos o servicios adquiridos, los impuestos aplicados y las condiciones de pago.

Control financiero: Facilita el control financiero al proporcionar una visión general de las obligaciones pendientes de pago por parte de los clientes y las deudas pendientes de cobro de los proveedores, lo que ayuda a gestionar el flujo de efectivo y mantener la liquidez adecuada.

Análisis de cuentas por cobrar y por pagar: Permite analizar las cuentas por cobrar a clientes y por pagar a proveedores, identificando las facturas vencidas, los saldos pendientes de cobro y pago, y evaluando la salud financiera de la empresa en relación con sus operaciones comerciales.

Gestión de relaciones comerciales: Ayuda a gestionar las relaciones comerciales con clientes y proveedores al tener una visión resumida de las transacciones realizadas, lo que facilita la comunicación, la negociación de términos comerciales y la toma de decisiones estratégicas.

#### Detalle de Columnas que integran el reporte

|         Columna        |              Descripción                   |                            Ayuda                                 |  
| ---------------------- | ------------------------------------------ | ---------------------------------------------------------------- |
|         Número         |          Número del Documento              |          Número de secuencia del documento para cada registro    |
|     Tipo Documento     |        Tipo de documento o reglas          |  Determina la secuencia del documento y las reglas de proceso    |
|   Socio del Negocio    |       Identifica un Socio del Negocio      | Persona con quien realiza transacciones. Cliente, proveedor, etc |
|         Moneda         |          Moneda para este registro         |    Indica la moneda a ser usada cuando se informe el registro    |
|       Gran Total       |            Total del documento             |          Identifica el total, incluye impuestos y fletes         |
|  Tipo de Conversión    |   Tipo de í­ndice de conversión de moneda   |I­ndice de conversión de monedas permite definir diferentes tarifas|
|     Fecha Contable     |   Fecha de contabilización del documento   |indica la fecha a ser usada en las cuentas de contabilidad general|
|      Descripción       |  Descripción corta opcional del registro   |         Una descripción esta limitada a 255 caracteres           |

### Facturación Diaria

Reporte que resume todas las facturas emitidas por una empresa en un día específico. Este reporte es una herramienta importante en la gestión financiera y comercial, ya que proporciona información detallada sobre las transacciones de ventas realizadas en un periodo breve de tiempo, en este caso, en un día.

Este informe muestra totales de facturas por Socio de negocio y por día.

![Facturación Diaria](/assets/img/docs/purchase-management/pum-reports7.png)

#### Finalidad del reporte

Control de ventas: Permite tener un registro detallado de todas las ventas realizadas en un día, incluyendo el número de factura, la fecha de emisión, el nombre o identificación del cliente, la descripción de los productos o servicios vendidos, los precios unitarios, los impuestos aplicados y el monto total facturado.

Seguimiento de ingresos: Facilita el seguimiento de los ingresos diarios de la empresa al mostrar de manera clara y organizada las ventas realizadas y los montos facturados, lo que ayuda a evaluar el desempeño financiero y la productividad comercial en un periodo corto de tiempo.

Control de inventario: Permite vincular las ventas registradas en el reporte con el inventario de productos disponibles, lo que ayuda a gestionar el stock, identificar productos más vendidos y planificar la reposición de inventario según la demanda diaria.

Análisis de tendencias: Al recopilar información diaria sobre las ventas, el reporte de facturación diaria permite analizar tendencias de ventas a corto plazo, identificar picos o variaciones en la demanda de productos o servicios, y tomar decisiones estratégicas en función de estos análisis.

Cumplimiento fiscal: Ayuda en el cumplimiento de obligaciones fiscales al proporcionar un registro detallado de las transacciones comerciales diarias, lo que facilita la generación de informes para la declaración de impuestos y la determinación de ingresos gravables.

#### Detalle de Columnas que integran el reporte

|         Columna        |              Descripción                   |                            Ayuda                                 |  
| ---------------------- | ------------------------------------------ | ---------------------------------------------------------------- |
| Transacción de Ventas  |    Identifica tipo de transacción          |      Informa si la transacción es de Venta o Compra (SI/NO)      |
|   Socio del Negocio    |       Identifica un Socio del Negocio      | Persona con quien realiza transacciones. Cliente, proveedor, etc |
| Grupo de Socio del Neg |     ID del Grupo de Socio del Negocio      | Proporciona un método de definir valores para conjuntos de SDN   |
|       F.Facturación    |        Fecha impresa en la factura         |   La fecha de la factura indica la fecha impresa en la factura   |
|    Neto de Línea       |    Monto de línea sin flete ni cargos      | Monto de línea según cantidad y precio (Cantidad * Precio actual)|
|% de Descuento de Línea |   Descuento de línea como un porcentaje    |       Indica el descuento para esta línea como un porcentaje     |
|   Agente Comercial     |           Agente de la Compañía            |            Indica el Agente comercial para esta región           |
| Tipo Documento Destino | Documento Destino para convertir Documentos|      La conversión documento es reflejada en el tipo actual      |



### Facturas sin Asignar

Es un informe que proporciona un listado de todas las facturas emitidas a clientes (cuentas por cobrar) y las facturas recibidas de proveedores (cuentas por pagar) que aún no han sido asignadas a pagos específicos. Este reporte es fundamental para la gestión financiera y de tesorería.

![Facturación Diaria](/assets/img/docs/purchase-management/pum-reports19.png)

#### Finalidad del reporte

1. Gestión de Cuentas por Cobrar y Pagar:

* Clientes: Permite a la empresa realizar un seguimiento de las facturas pendientes de cobro de los clientes, asegurando una gestión efectiva de las cuentas por cobrar.

* Proveedores: Facilita el seguimiento de las facturas pendientes de pago a los proveedores, gestionando adecuadamente las cuentas por pagar.

2. Control del Flujo de Caja:

* Ingresos: Proporciona una visión clara de los ingresos esperados al listar las facturas pendientes de cobro.

* Egresos: Ayuda a prever los desembolsos necesarios al listar las facturas pendientes de pago.

3. Seguimiento y Recordatorios:

* Clientes: Ayuda a identificar a los clientes con pagos pendientes y permite enviar recordatorios de pago y hacer un seguimiento proactivo para cobrar las facturas.

* Proveedores: Facilita el control de las obligaciones de pago, asegurando que las facturas se paguen a tiempo y evitando retrasos y posibles penalidades.

4. Análisis Financiero:

* Permite realizar un análisis financiero completo, evaluando la salud de las cuentas por cobrar y por pagar, y tomando decisiones estratégicas para mejorar la gestión de crédito y cobro.

5. Cumplimiento y Auditoría:

* Mantener un registro detallado de las facturas pendientes es esencial para auditorías internas y externas, asegurando que todas las transacciones se registren y gestionen correctamente.

6. Relaciones con Clientes y Proveedores:

* Clientes: Ayuda a mantener buenas relaciones con los clientes mediante una comunicación clara sobre sus obligaciones financieras.

* Proveedores: Facilita la gestión de relaciones con los proveedores al asegurar pagos oportunos y mejorar la transparencia en las transacciones.

7. Optimización del Capital de Trabajo:

* Clientes: Asegura que los ingresos se reciban de manera oportuna, mejorando la liquidez de la empresa.

* Proveedores: Ayuda a gestionar adecuadamente los desembolsos, manteniendo el capital de trabajo optimizado.

#### Detalle de Columnas que integran el reporte

|         Columna        |              Descripción                   |                            Ayuda                                 |  
| ---------------------- | ------------------------------------------ | ---------------------------------------------------------------- |
|   Socio del Negocio    |       Identifica un Socio del Negocio      | Persona con quien realiza transacciones. Cliente, proveedor, etc |
|    No. del Documento   |          Número del Documento              |          Número de secuencia del documento para cada registro    |
|     Tipo Documento     |        Tipo de documento o reglas          |  Determina la secuencia del documento y las reglas de proceso    |
|       F.Facturación    |        Fecha impresa en la factura         |   La fecha de la factura indica la fecha impresa en la factura   |
|        Factura         |      	Identificador de la factura       |  La ID de Factura identifica únicamente un documento de Factura  |
|       Gran Total       |            Total del documento             |          Identifica el total, incluye impuestos y fletes         |

### Facturación Semanal

Este informe muestra un total de factura por Socio del negocio y por semana.

![Facturación Semanal](/assets/img/docs/purchase-management/pum-reports8.png)

#### Detalle de Columnas que integran el reporte

El despliegue de campos es idéntico al reporte de Facturación Diaria. Lo que se modifica es la forma de reflejar la información. En este caso muestra la facturación "Por semana".

### Facturación Semanal de Producto

Este informe muestra un total de facturas por semana y por categoría de producto

![Semanal de producto](/assets/img/docs/purchase-management/pum-reports9.png)

### Facturación Mensual

Este informe muestra los totales de facturas por mes y por Socio del Negocio

![Facturación Mensual](/assets/img/docs/purchase-management/pum-reports10.png)

### Facturación Mensual de Producto

Este informe muestra totales de facturas mensual por categoría de Producto

![Mensual de producto](/assets/img/docs/purchase-management/pum-reports11.png)

### Facturación Mensual de Proveedor

Este informe muestra totales de facturas mensual por proveedor y categoría de producto.

![Mensual de Proveedor](/assets/img/docs/purchase-management/pum-reports12.png)

### Producto Facturado Mensualmente

Este informe muestra la cantidad facturada mensualmente por producto.

![Producto facturado mensualmente](/assets/img/docs/purchase-management/pum-reports13.png)

### Facturación Trimestral a Clientes por Proveedor

Este informe muestra totales de facturas por Proveedor y Cliente de productos por trimestre

![trimestral a clientes por proveedor](/assets/img/docs/purchase-management/pum-reports14.png)

### Facturación Trimestral a Clientes por Producto

 Este informe muestra totales de facturas en forma trimestral por cliente y categoría de producto

 ![Trimestral a clientes por producto](/assets/img/docs/purchase-management/pum-reports15.png)

### Facturación Trimestral por Producto

Este informe muestra totales de facturas en forma trimestral por producto y por Socio del Negocio

 ![Trimestral por producto](/assets/img/docs/purchase-management/pum-reports16.png)