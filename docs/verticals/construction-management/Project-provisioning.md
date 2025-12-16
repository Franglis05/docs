---
title: 2. Aprovisionamiento de Proyecto
category: Documentation
star: 9
sticky: 9
article: false
---

El aprovisionamiento de un proyecto de Constructora es el proceso mediante el cual se planifica, gestiona y coordina la adquisición de materiales, insumos y servicios necesarios para llevar a cabo un proyecto de construcción. 
El objetivo del aprovisionamiento es asegurar que los recursos necesarios estén disponibles en el momento adecuado y en las cantidades correctas para evitar retrasos y garantizar la eficiencia en la ejecución del proyecto.

El aprovisionamiento implica la gestión de la cadena de suministro para obtener los recursos esenciales como materiales de construcción (cemento, acero, ladrillos, etc.), equipos, herramientas y servicios (subcontratistas, maquinaria) que se utilizarán en las diferentes fases de la obra. Este proceso es crítico en la industria de la construcción, ya que una mala planificación del aprovisionamiento puede generar retrasos, sobrecostos y desperdicio de recursos.

El aprovisionamiento abarca diversas etapas, desde la identificación de necesidades, la selección de proveedores, la compra o alquiler de materiales y equipos, hasta la recepción y almacenamiento en el sitio de obra.

## *Necesidades de Proyecto*

Es una función clave que permite gestionar y planificar los recursos y materiales necesarios para ejecutar un proyecto de construcción. Este proceso ayuda a identificar, organizar y prever las demandas que el proyecto tendrá en cuanto a materiales, mano de obra, equipos, y otros insumos, con el fin de garantizar que todos estos elementos estén disponibles en el momento adecuado para evitar retrasos y optimizar el uso de los recursos.

El Navegador de Necesidades de Proyecto implica la planificación detallada de todos los recursos que se requerirán durante las diferentes fases de un proyecto de construcción. A través de este proceso se identifican y registran los materiales, equipos, servicios, y recursos humanos necesarios, así como las cantidades, fechas de entrega y costos estimados.

Incluye la evaluación de los requerimientos del proyecto con base en el plan de trabajo, especificaciones técnicas, presupuestos y cronogramas. El ERP permite automatizar y optimizar este procedimiento, generando informes y alertas para mantener un control riguroso sobre las necesidades a medida que el proyecto avanza.

Desde el *Navegador Necesidades de Proyecto* es posible seleccionar el proyecto y la Fase (opcional). Al aceptar se desplegará el listado de todo lo que necesita alimentar ese proyecto (o Fase) para llevarse a cabo (los productos).

Luego, desde los parámetros es posible seleccionar si se desea generar una Orden de compra (para abastecer con los productos necesarios al proyecto/fase) o bien una requisición (una solicitud interna de compra), o un Movimiento de Inventario (del almacén fuente al Proyecto)

![Necesidades de Proyecto](/assets/img/docs/construction-management/com-image3.png)

### *Crear Orden de Compra desde Línea de Requisición*

Es el procedimiento mediante el cual se convierte una solicitud de compra interna (requisición) en una orden de compra oficial que se envía a los proveedores para adquirir los materiales, equipos o servicios necesarios para el proyecto de construcción.

Este proceso es fundamental para garantizar que los recursos solicitados por el equipo de construcción, ya sea desde la obra o desde los departamentos de logística y compras, se gestionen de manera formal, eficiente y con un control detallado en el ERP

El navegador permite la búsqueda de las diferentes requisiciones pendientes por proyecto, por fase, etc. Con el fin de generar la correspondiente orden de compra por los productos comprendidos en cada requisición.

Se define el Proveedor, tipo de documento y fecha.

En el caso de no poseer precios de productos, es posible generar la orden de compra en estado "Preparar" (y no completar). Para luego, cuando se confirme precio de productos, se consulte la orden de compra, se definan los precios y se cambie el estado por "Completo".

![Crear OC](/assets/img/docs/construction-management/com-image4.png)

### *Salida de Proyecto desde Compra/Inventario*

Este proceso en el ERP está diseñado para optimizar la gestión de materiales en los proyectos de construcción, integrando en un solo paso tanto la recepción de los productos como su inmediata asignación y baja del stock por su consumo en un proyecto específico.

#### Descripción:

* Recepción de productos:

Se registran los productos que llegan a la obra o al almacén relacionados con un proyecto en particular.
Se actualiza el stock de la empresa, indicando que los productos han sido recibidos de acuerdo con la orden de compra o planificación del proyecto.

* Salida automática por consumo en el proyecto:

En el mismo paso, el Solop ERP registra la salida inmediata de estos productos del inventario, asignándolos directamente al consumo del proyecto para el cual están destinados.
Se vincula el consumo de estos materiales a los costos del proyecto de manera automática, reflejando el gasto en tiempo real en la contabilidad del proyecto.

* Propósito y beneficios:

Automatización del flujo de materiales: Este proceso evita pasos manuales adicionales al combinar la recepción y el consumo en un solo movimiento, lo que optimiza el tiempo y reduce errores administrativos.

Control de costos en tiempo real: La empresa tiene visibilidad inmediata sobre los costos de materiales que se van asignando al proyecto, lo que facilita un control financiero más preciso y una gestión eficiente del presupuesto.

Trazabilidad: Se garantiza la trazabilidad de los productos desde su llegada hasta su consumo, proporcionando un historial detallado de cada material vinculado al proyecto, algo esencial para auditorías y gestión de calidad.

Reducción de tareas administrativas: Al hacer coincidir en un único paso la entrada y salida de materiales, se reducen las tareas administrativas, como la creación de movimientos separados para la recepción y el consumo, aumentando la eficiencia operativa.

El Navegador Salida de proyecto desde Compra/Inventario se refiere al procedimiento mediante el cual los materiales y recursos adquiridos o almacenados en inventario son asignados y transferidos a un proyecto específico para su utilización en las obras.

Este proceso es crucial para gestionar adecuadamente los recursos necesarios para la ejecución del proyecto y para mantener un control preciso sobre el uso y la disponibilidad de los materiales.

El proceso de salida de proyecto es la transferencia de materiales o recursos (comprados o almacenados) desde el inventario central de la constructora hacia el sitio de obra o área donde se ejecutará el proyecto. Esto incluye el seguimiento y la documentación de la salida de insumos como cemento, acero, ladrillos, herramientas, y otros recursos que serán utilizados en el proyecto de construcción.

Permite seleccionar las órdenes de compra recibidas (o bien permite seleccionar desde nuestro inventario) los productos que se deseen enviar al costo del Proyecto (se define la fecha del movimiento). O sea, permite realizar el movimiento de productos desde nuestro propio stock o desde una compra realizada.

![Salida de Proyecto](/assets/img/docs/construction-management/com-image5.png)

En el caso de realizarlo desde una compra, genera dos movimientos en un solo paso: realiza la recepción de los productos de la compra, y genera la salida por proyecto (o sea, los baja de stock por cosumo en un proyecto determinado).

**Para mayor información sobre Recepción de Productos:** - [Recepción de Productos](../../purchase-management/reception)

**Para mayor información sobre Movimiento de inventario:** - [Movimiento de inventario](../../material-management/inventory-move)