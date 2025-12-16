---
title: 3. Facturación
category: Documentation
star: 9
sticky: 9
article: false
---

El proceso de facturación de un proyecto de Cnstructora es el conjunto de procedimientos mediante los cuales la empresa genera y emite facturas a sus clientes por los servicios prestados o los bienes suministrados durante el desarrollo del proyecto. Este proceso es esencial para documentar los ingresos, asegurar el pago por los trabajos realizados y mantener un control financiero adecuado a lo largo del proyecto.

El proceso de facturación implica la creación de documentos fiscales (facturas) que reflejan las cantidades de trabajo realizado, los materiales utilizados, y otros costos asociados a las obras de construcción. La factura detalla el monto total a pagar, las fechas de vencimiento, y las condiciones de pago, además de cualquier impuesto o gravamen aplicable.

El proceso varía según el tipo de proyecto y el modelo de facturación acordado entre la constructora y el cliente. Por ejemplo, en proyectos de gran envergadura, la facturación puede ser por avance de obra, lo que implica la emisión de facturas en función del porcentaje de trabajo completado.

## *Generar orden desde Línea de Proyecto*

Es un navegador cuya funcionalidad permite crear una orden de venta a partir de las líneas de un proyecto específico. Este proceso es clave en la gestión de proyectos de construcción.

En este paso, este Navegador permite generar orden de venta por líneas de proyecto (permite la preparación para facturar de el avance de un determinado proyecto).

Desde un grupo de parámetros permite individualizar las líneas sobre las cuales se realizará la orden de venta y luego se define el tipo de documento, la fecha y la acción sobre el documento (preparar o completar).

En una primera instancia se generará una exportación (a excel por ejemplo) de aquellas líneas que estén en situación de ser facturadas para enviar y notificar al cliente.

Esta exportación brinda información del avance del proyecto, de los productos con cantidad cotizada, cantidad cometida y cantidad a facturar.

Luego de la aprobación del cliente se procede a completar la orden de venta para su posterior facturación.

![Generar Orden](/assets/img/docs/construction-management/com-image6.png)

## *Generar Factura desde Línea de Orden*

El Navegador Generar Factura desde Línea de Orden implica convertir las órdenes de venta realizadas por los clientes en facturas que reflejan el detalle de los bienes y servicios proporcionados. Este proceso es crucial para documentar los ingresos de la empresa y asegurar el cobro adecuado de los proyectos o servicios vendidos.

El proceso comienza cuando se realiza una orden de venta para adquirir bienes o servicios de la constructora (por ejemplo, materiales de construcción o servicios de obra). Cada orden de venta incluye líneas que detallan los productos o servicios solicitados, sus cantidades, precios y condiciones de entrega.

El ERP permite que, una vez cumplida la orden de venta (entrega de bienes o ejecución de servicios), las líneas de esa orden de venta se utilicen para generar automáticamente una factura. La factura es el documento que formaliza la transacción comercial y que el cliente debe abonar.

Este Navegador permite visualizar las líneas de órdenes de venta en estado completo, que se encuentran en situación de generar la factura a cliente.

Es posible seleccionar el tipo de agrupación para generar facturas: por proyecto, por orden, etc. y al seleccionar las líneas de orden y ejecutar el proceso generará tantas facturas (documentos por cobrar) como correspondan según la agrupación seleccionada.

Se selecciona la fecha del documento y la acción sobre el documento (preparar o completar).

En el caso de seleccionar la acción "Completar" ingresa en el circuito de envío de facturas a la entidad fiscal (según corresponda) así como el envío de la representación gráfica a los clientes vía e mail.

::: note
La condición para que se encuentre una orden de venta pendiente de facturar es que se defina a la misma como Permite Facturar = SI
:::

![Generar Factura](/assets/img/docs/construction-management/com-image7.png)

**Para mayor información sobre Generar Factura desde Línea de Orden:** - [Facturación desde línea de Orden de Venta](../../sales-management/receivable-document/billing-from-orderline)

## Reporte "Detalle de Avance de Proyecto"

Es un informe que proporciona un análisis detallado sobre el estado actual de un proyecto de construcción respecto a sus diferentes "Fases" y Líneas de Fase. Este reporte incluye información clave como el porcentaje de avance físico, los costos incurridos, las tareas completadas, los recursos utilizados y la comparación entre el progreso planificado y el real. 

Sirve como una herramienta fundamental para monitorear y controlar el desempeño del proyecto a lo largo del tiempo.

Ofrece una visión detallada y en tiempo real del estado del proyecto de construcción en términos de:

* Tareas completadas versus tareas pendientes.
* Recursos utilizados y necesarios para las próximas fases.
* Costos acumulados en comparación con el presupuesto original.
* Cumplimiento del cronograma planificado.
* Desviaciones en plazos o costos que pueden afectar la entrega final.

Este informe se genera automáticamente en el ERP a partir de los datos ingresados sobre las diferentes actividades del proyecto y los recursos asociados, como mano de obra, materiales, equipos, y costos.

El reporte "Detalle de Avance de Proyecto" muestra los mismos datos que el Navegador *Generar Orden desde Línea de Proyecto*.
Permite filtrar por parámetros de Proyecto y Fase de Proyecto.

### Detalle de columnas

- Total Planeado: es el total planeado de la línea de proyecto

- Cant. Planeada: es la cantidad planeada de la línea de proyecto

- Cuenta Facturada: es el importe de cuenta facturada de la línea de proyecto

- Cant. Facturada: es la cantidad facturada de la línea de proyecto

- Cant. Cometida: es la cantidad cometida de la línea de proyecto

- % Trabajo Terminado: es el % de trabajo terminado de la línea de proyecto

- % Facturado: si la cant. planeada de la línea de proyecto es mayor a cero entonces será el resultado de (cuenta facturada * 100)/cant. planeada, de lo contrario el valor de esta columna será cero

- % a Facturar: es el resultado de (% trabajo terminado - % facturado)

- Cant. a Facturar: es el resultado de (cant. cometida - cant. facturada)

- Importe a Facturar: es el resultado de (cant. a facturar * precio planeado de línea de proyecto)

### Reporte disponible para los roles:

* Administrador

* Constructora - Admin