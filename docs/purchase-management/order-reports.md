---
title: Reportes de Órdenes
category: Documentation
star: 9
sticky: 9
article: false
---

## Concepto

Los reportes de órdenes son listados que nos brindan información detallada sobre las diferentes órdenes de Venta o Compra.
Se utilizan para obtener una vista parametrizada (por fecha, por Socio del negocio, por estado, etc.) de los diferentes registros con su información detallada de entidades relacionadas, importes y estado.
Cada reporte mantiene sus particularidades y sirven a distintas finalidades (de acuerdo a su nivel de detalle).

### Listado de Ordenes

Reporte que muestra información detallada sobre las órdenes de venta y compra realizadas por una empresa o entidad en un periodo específico. Estas órdenes representan compromisos de compra o venta de productos o servicios y son parte fundamental de la gestión comercial de una empresa.

Este informe muestra todas las líneas de órdenes tanto Órdenes de Venta como Órdenes de Compra (indicando Transacción de Venta: SI/NO) existentes en el sistema, informando los siguientes importes:

* Importe Ordenado
* Importe Entregado
* Importe Facturado

* Importe Pendiente de Entregar
* Importe Pendiente de Facturar
* Importe Entregado No Facturado
* Importe Facturado No Entregado

![Listado de Órdenes](/assets/img/docs/purchase-management/pum-reports1.png)

#### Finalidad del reporte

El reporte de Órdenes de Venta y Compra sirve para varios propósitos importantes:

Seguimiento de órdenes: Permite llevar un registro detallado de todas las órdenes de venta y compra realizadas por la empresa, incluyendo información como la fecha de la orden, el cliente o proveedor involucrado, la descripción de los productos o servicios, las cantidades solicitadas, los precios acordados y los plazos de entrega o pago.

Control de inventario y producción: Facilita el control del inventario y la producción al proporcionar información sobre las órdenes de compra de materias primas o productos para la fabricación, así como las órdenes de venta de productos terminados o servicios a clientes.

Gestión de clientes y proveedores: Permite gestionar de manera eficiente las relaciones con clientes y proveedores al tener un registro organizado de las órdenes de venta y compra realizadas con cada uno de ellos, lo que facilita el seguimiento de pagos, entregas y acuerdos comerciales.

Análisis de ventas y compras: Sirve como herramienta para analizar las tendencias de ventas y compras de la empresa, identificar patrones de demanda, evaluar la efectividad de las estrategias comerciales y tomar decisiones informadas sobre inventario, producción y relaciones comerciales.

Se puede verificar que los importes definidos por este Reporte de “Listado de Órdenes” se pueda corresponder con los siguientes:

* **Importe Facturado:** Se puede validar con el reporte de “Diario de Ventas y Compras” clasificando según Socio del Negocio. El Importe Fuente en cada Moneda se podrá validar con el importe Facturado definido en el Reporte de “Listado de Órdenes”.
* **Importe Entregado No Facturado:** Se puede validar con el importe de “Unbilled” en moneda Fuente. Adicionalmente el Reporte de “Unbilled General” también mostrará su correspondiente conversión y esta a su vez se podrá corresponder con el saldo de la Cuenta Contable de Unbilled.
* **Importe Facturado no Entregado:** Se podrá validar en moneda fuente con el reporte de “Facturas Cliente sin Entregar” o “Facturas Proveedor sin Entregar” así como también con la columna de “Deferred” del Monitor tanto de Compras como de Ventas respectivamente.

**Pendiente de Entregar:** se corresponderá con la columna de “Compromiso” del Monitor de Compras o de Ventas respectivamente.

#### Vistas del Reporte de Ordenes (aplican al ordenamiento de datos, y se pueden crear las que sean necesarias):

* Ordenes de Compra por Tipo de Orden
* Ordenes por Moneda y Contrato
* Ordenes por Moneda Contrato y Proyecto

#### Detalle de Columnas que integran el reporte (Ejemplo vista por Proyecto)

|         Columna        |              Descripción                   |                            Ayuda                                 |  
| ---------------------- | ------------------------------------------ | ---------------------------------------------------------------- |
|       Proyecto         |           Proyecto Financiero              | Permite rastrear y controlar actividades internas o externas     |
|   Socio del Negocio    |      Identifica un Socio Comercial         | Persona con quien realiza transacciones. Cliente, proveedor, etc |
|       F. Orden         |           Fecha de pedido                  |          Indica la fecha en que se ordenó un artículo            |
|    Tipo de Orden       |          Tipo de documento destino         | Puede convertir tipos de documentos de oferta a pedido o factura |
|     Nro. Orden         |                Orden                       |                       Documento de control                       |
|       Producto         |       Producto, Servicio, Artículo         |        Identifica un artículo que se compra o vende              |
| Categoría del Producto |        Categoría de un Producto            |      Identifica la categoría a la que pertenece el producto      |
|        Precio          |         Precio basado en la UM             | El precio ingresado convierte a precio real por conversión de UM |
|        Moneda          |      La moneda para este registro          | Moneda que se utiliza al procesar o informar sobre este registro |
|      Total Neto        |   Monto de línea sin flete ni cargos       | Monto de línea según cantidad y precio (Cantidad * Precio actual)|
|       Proveedor        |             Socio Comercial                |                 Socio comercial que abastece                     |
|        Estado          |       Estado actual del documento          |                  Indica el estado de un documento                |



### Transacción de Orden

Reporte que detalla las transacciones asociadas a las órdenes de venta y compra realizadas por una empresa. Este reporte proporciona información específica sobre las transacciones financieras, logísticas y comerciales relacionadas con cada orden de venta o compra.

Este reporte presenta cabezales de las Órdenes de Compra o de Venta (seleccionando el check Transacción de venta SI/NO) entre determinadas fechas y con su correspondiente información y status.

![Transacción de Orden](/assets/img/docs/purchase-management/pum-reports2.png)

Muestra los cabezales de las Órdenes, tanto de Ventas como de Compras.

* Contrato
* Proyecto
* Orden Enlazada
* Importes Totales

#### Finalidad del reporte

El propósito principal del reporte de "Transacción de la Orden de Venta y Compra" es brindar una visión detallada de cómo se ha llevado a cabo cada orden de venta o compra, incluyendo:

Información de la orden: Incluye detalles sobre la orden de venta o compra, como el número de orden, la fecha de la orden, los productos o servicios involucrados, las cantidades, los precios unitarios, los descuentos aplicados y los impuestos.

Transacciones financieras: Muestra todas las transacciones financieras asociadas a la orden, como los pagos recibidos por las ventas o los pagos realizados por las compras, junto con los métodos de pago utilizados y las fechas de pago.

Procesamiento logístico: Informa sobre el procesamiento logístico de la orden, incluyendo la preparación de la mercancía, los envíos realizados, las fechas de entrega, las devoluciones o cancelaciones, y cualquier incidencia logística relacionada.

Estado de la orden: Indica el estado actual de la orden de venta o compra, como si está en proceso, completada, cancelada o pendiente de aprobación, proporcionando una visión general del progreso de la transacción.

#### Detalle de Columnas que integran el reporte

|         Columna        |              Descripción                   |                            Ayuda                                 |  
| ---------------------- | ------------------------------------------ | ---------------------------------------------------------------- |
|    No del Documento    |    Número de secuencia del documento       | El N° lo genera en automático el sistema por tipo de documento   |
|   Socio del Negocio    |      Identifica un Socio del Negocio       | Persona con quien realiza transacciones. Cliente, proveedor, etc |
|       F. Orden         |           Fecha de la orden                |             Indica la fecha en que se ordenó un artículo         |
|    Agente Comercial    |           Agente de la Compañía            |           Indica el agente comercial para esa región             |
|        Almacén         |          Almacén y punto de servicio       |    Indica locación única donde los productos son almacenados     |
|  Regla de Facturación  |    Frecuencia y métodos de facturación     |  Define forma y frecuencia de facturación a un socio del negocio |
|      Proyecto          |          Proyecto Financiero               |          Permite realizar un seguimiento y control interno       |
|   Lista de Precio      |     Identificador de Lista de Precio       | Determinan el precio, margen y costo de artículos (compra/venta) |
|        Moneda          |             Moneda del registro            | Indica moneda utilizada cuando se procesa o informa el registro  |
|   Total de Líneas      |  Total de todas las líneas del documento   |  Despliega total de todas las líneas en la moneda del documento  |
|      Gran Total        |           Total del Documento              | Identifica el total incluyendo impuestos en moneda del documento |
|  Estado del Documento  |        Estado Actual del Documento         |     Indica el estado del documento en un momento determinado     |
|   Tipo de Documento    |        Tipo de documento o reglas          |    Determina la secuencia del documento y reglas del proceso     |
|         Tasa           |      Tasa de conversión de moneda          |  define la tasa para convertir moneda fuente a moneda contable   |
|    Región de Venta     |       Región de cobertura de ventas        |         Indica un área de cobertura de ventas específica         |
|  Cálculo de comisiones |       Cálculo o proceso de comisiones      |   identificador único define ejecución específica de comisiones  |
|      Descripción       |  Descripción corta opcional del registro   |            Descripción limitada a 255 caracteres                 |	
|    Fecha Contable      |  Fecha de contabilización del registro     |   Indica la fecha a utilizar en cuentas de contabilidad general  |

## Detalle de la Orden

Es un informe que proporciona una descripción completa de las órdenes de compra y venta realizadas por una empresa durante un período específico. Este reporte incluye información detallada sobre cada orden, como la fecha, los productos o servicios involucrados, las cantidades, los precios, los proveedores o clientes, y el estado de la orden.

![Detalle de la Orden](/assets/img/docs/purchase-management/pum-reports17.png)

#### Finalidad del reporte

* Monitoreo de Transacciones: Permite realizar un seguimiento detallado de todas las órdenes de compra y venta, asegurando que cada transacción se lleve a cabo según lo planeado y ayudando a identificar cualquier problema o retraso en el proceso.

* Gestión de Inventarios: Ayuda a gestionar los niveles de inventario al proporcionar una visión clara de los productos que se han ordenado para compra y los que se han vendido, facilitando una mejor planificación y reposición de stock.

* Control Financiero: Proporciona información detallada sobre los costos y los ingresos asociados con las órdenes de compra y venta, lo que es esencial para la gestión y el análisis financiero de la empresa.

* Relaciones con Proveedores y Clientes: Facilita la gestión de relaciones con proveedores y clientes al mantener un registro claro y detallado de todas las transacciones, ayudando a resolver disputas y a mantener una comunicación efectiva.

* Cumplimiento y Auditoría: Asegura el cumplimiento con las normativas contables y fiscales al proporcionar un registro detallado de todas las órdenes de compra y venta, lo cual es vital para las auditorías internas y externas.

* Análisis de Rendimiento: Permite evaluar el rendimiento de proveedores y clientes, identificando aquellos que son más confiables o rentables, y ayudando a tomar decisiones informadas sobre futuras transacciones.

* Optimización de Procesos: Ayuda a identificar ineficiencias en el proceso de compra y venta, proporcionando datos que pueden utilizarse para mejorar los tiempos de entrega, reducir costos y optimizar la gestión del inventario.

* Planificación Estratégica: Proporciona información valiosa para la planificación estratégica, ayudando a prever la demanda futura, planificar las compras y ajustar las estrategias de ventas.

#### Vistas

* Detalle de la Orden
*Detalle de la Orden Simple

#### Detalle de Columnas que integran el reporte  (ejemplo vista: Detalle de la Orden Simple)

|         Columna        |              Descripción                   |                            Ayuda                                 |  
| ---------------------- | ------------------------------------------ | ---------------------------------------------------------------- |
|       F. Orden         |           Fecha de la orden                |             Indica la fecha en que se ordenó un artículo         |
|     Orden de Venta     |                Orden de Venta              |      La ID de la orden de ventas es un identificador único       |
|   Socio del Negocio    |      Identifica un Socio del Negocio       | Persona con quien realiza transacciones. Cliente, proveedor, etc |
|       Producto         |       Producto, Servicio, Artículo         |        Identifica un artículo que se compra o vende              |
|        Precio          |         Precio basado en la UM             | El precio ingresado convierte a precio real por conversión de UM |
|    Cantidad Ordenada   |             Cantidad Ordenada              |        Indica la cantidad de un producto que fue ordenada        |
|   Cantidad a Facturar  |             Cantidad Facturada             |     Indica la cantidad de un producto que ha sido facturado      |

## Órdenes Abiertas

Es un informe que proporciona una visión detallada de todas las órdenes de venta y compra (seteando "Transacción de venta" SI/NO respectivamente) que aún presentan cantidades pendientes de entregar o facturar. Estas órdenes están en diferentes etapas del proceso y aún están activas, lo que significa que los productos o servicios aún no se han entregado completamente o los pagos no se han realizado en su totalidad.

El reporte de "Órdenes Abiertas" incluye información sobre:

* Órdenes de Venta Abiertas: Detalles de todas las órdenes de venta pendientes, incluyendo la fecha de la orden, el cliente, los productos o servicios ordenados, las cantidades, los precios, los estados de las órdenes (por ejemplo, procesado, pendiente de envío, parcialmente enviado), y cualquier otra información relevante.

* Órdenes de Compra Abiertas: Detalles de todas las órdenes de compra pendientes, incluyendo la fecha de la orden, el proveedor, los productos o servicios ordenados, las cantidades, los precios, los estados de las órdenes (por ejemplo, procesado, pendiente de recepción, parcialmente recibido), y cualquier otra información relevante.

![Detalle de la Orden](/assets/img/docs/purchase-management/pum-reports18.png)

#### Finalidad del reporte

* Monitoreo y Seguimiento: Permite a los gerentes y al personal de operaciones monitorear el estado de todas las órdenes abiertas. Esto es esencial para asegurarse de que las órdenes se están procesando según lo planeado y para identificar cualquier retraso o problema que deba ser abordado.

* Gestión de Inventarios: Ayuda a gestionar los niveles de inventario al proporcionar una visión clara de los productos que están en proceso de ser recibidos (en el caso de órdenes de compra) o enviados (en el caso de órdenes de venta). Esto permite una mejor planificación y previsión de las necesidades de inventario.

* Planificación Financiera: Facilita la planificación financiera al proporcionar una visión de los ingresos esperados de las órdenes de venta abiertas y los gastos previstos de las órdenes de compra abiertas. Esto es crucial para la gestión del flujo de caja y la previsión financiera.

* Mejora del Servicio al Cliente: Permite a los equipos de ventas y servicio al cliente proporcionar información precisa y actualizada a los clientes sobre el estado de sus órdenes, mejorando la satisfacción del cliente y la transparencia en las transacciones.

* Control de Proveedores: Ayuda a gestionar y controlar las relaciones con los proveedores al monitorear el cumplimiento de las órdenes de compra y asegurarse de que los proveedores estén entregando los productos o servicios según lo acordado.

* Optimización de Procesos: Identifica cuellos de botella y áreas de mejora en los procesos de ventas y compras, permitiendo a la empresa optimizar sus operaciones y aumentar la eficiencia.

* Auditoría y Cumplimiento: Proporciona una documentación detallada de todas las órdenes abiertas, lo cual es esencial para auditorías internas y externas y para asegurar el cumplimiento con las políticas y regulaciones de la empresa.

#### Vistas

* Órdenes Abiertas

#### Detalle de Columnas que integran el reporte

|         Columna        |              Descripción                   |                            Ayuda                                 |  
| ---------------------- | ------------------------------------------ | ---------------------------------------------------------------- |
|     F. Prometida       |        Fecha de promesa de la orden        |      Indica la fecha en que la orden fue prometida al cliente    |
|    Orden de Venta      |           ID de Orden de Venta             |              Identificador único de la orden de venta            |
|       F. Orden         |           Fecha de la orden                |             Indica la fecha en que se ordenó un artículo         |
|   Tipo de Documento    |        Tipo de documento o reglas          |    Determina la secuencia del documento y reglas del proceso     |
|  Estado del Documento  |        Estado Actual del Documento         |     Indica el estado del documento en un momento determinado     |
|   Socio del Negocio    |      Identifica un Socio del Negocio       | Persona con quien realiza transacciones. Cliente, proveedor, etc |
|   Dirección del SDN    |   Identifica la dirección para este SDN    |        Indica el domicilio legal de un Socio del Negocio         |
|        Usuario         |      ID de Usuario dentro del sistema      |              Identifica un usuario único en el sistema           |
|        Moneda          |             Moneda del registro            | Indica moneda utilizada cuando se procesa o informa el registro  |
|        Almacén         |          Almacén y punto de servicio       |    Indica locación única donde los productos son almacenados     |
|    Agente Comercial    |           Agente de la Compañía            |           Indica el agente comercial para esa región             |
|       Producto         |       Producto, Servicio, Artículo         |        Identifica un artículo que se compra o vende              |
|       Cantidad         |  La cantidad incorporada se basa en la UM  |        Se convierte a la cantidad baja de UM del producto        |
|           UM           |                Unidad de Medida            | 	  La UM define una unidad de medida única no monetaria       |
|    Precio Unitario     |               Precio Actual                |       Indica el precio para un producto en la moneda fuente      |
|    Cantidad Ordenada   |             Cantidad Ordenada              |        Indica la cantidad de un producto que fue ordenada        |
|        Precio          |         Precio basado en la UM             | El precio ingresado convierte a precio real por conversión de UM |
|       Actividad        |            Actividad de Negocio            |    Indican tareas que son ejecutadas en el curso de un negocio   |
|        Aprobado        |Indica si este documento requiere aprobación| Indica si este documento requiere aprobación antes ser procesado |
| Conjunto de Atributos  |     Conjunto de Atributos de Producto      |           Define los sistemas de la cualidad de producto         |
|        Campaña         |        Identificación comercial            |                 Identificación comercial primordial              |