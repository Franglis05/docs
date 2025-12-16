---
title: Punto de Venta
category: Documentation
star: 9
sticky: 9
article: false
---

## Mantenimientos

### ¿Por qué al intentar completar una orden de venta  no se completa - POS?

Es posible que la Orden de Venta ya tenga un Pago/Cobro asignado, si es asi, no dejara completar hasta que no se elimine el Pago/Cobro asociado a la Orden de Venta. Luego dejara completar.

### ¿Por qué al generar un comprobante factura contado no aparece en la caja al hacer detalles de caja?

El motivo por el cuál no se generó un Cobro Contado al completar la Orden de Venta es que la misma fue completada desde la Ventana de Ordenes de Venta desde ZK y la orden tiene definido una Terminal de Punto de Venta.

Cuando una Orden de Venta es completada desde la ventana de ordenes de venta desde ZK y tiene definido una terminal PDV, al completarse NO HACE el cobro automáticamente pese a que se le defina "Contado".

Sólo generará el cobro automáticamente al completarse si está definida como "EFECTIVO" y no tiene definida ninguna terminal PDV. En ese caso generará un cobro a la Caja que se tenga definida como Predeterminada.

## Acciones

### Se puede Generar desde el POS una factura a credito?

Esa funcionalidad no esta implementada todavia en el POS, para hacerlo debe realizarse desde la ventana Documentos Por Cobrar. 

### Como se define la Tasa de Cambio y POS:

El tipo tasa de cambio esta definida en la ventana Terminal PDV en el campo “Tipo de Conversión”. Si es “Company” no se carga automaticamente, la define el Cliente o la define OpenUp con una duración especifica. Si es “Spot”, existe un proceso que se ejecuta por medio del CRON y carga la tasa de forma automatica a diario.

### Cierre de Caja (qué ocurre si no genero la apertura de caja)

Al realizar la apertura de Caja se genera un registro de cierre de caja por el recibo de apertura.

En el caso que se omita este paso de realizar la apertura. El ERP debería generar el registro de cierre de caja desde el primer cobro. Aun así, se han detectado casos en los cuales el registro de cierre de caja no se realiza.

Para estos casos, posteriormente, se debió generar el registro de cierre de caja de forma manual vinculando las transacciones del día a la caja correspondiente (con el objeto de poder realizar el cierre del punto de venta).

Se configura como Tipo documento apertura: recibo de caja.

Cada vez que se genera un cobro o pago se crea una línea al registro de cierre de caja.

Se trata de una conciliación bancaria aplicada a las cuentas de Caja.

La cuenta de caja es un Bank account excepto que es una definición de caja (cuenta de caja, y no bancaria).

Debe definirse un cargo predeterminado por apertura, de lo contrario no podrá operar el punto de venta.

Al generar una nueva orden se visualizarán valores pre seteados para el punto de venta pero que pueden ser modificados. Tal como el tipo de documento (e ticket o e factura), Socio de negocio (por default estará configurado como "Mostrador" (socio no identificado) pero se podrán seleccionar diferentes socio clientes o bien crear uno nuevo (si el usuario posee permisos para dicha función.

Para completar la orden de venta, primero debe cobrarse.

Al generar el cobro, se mostrarán los diferente métodos de pago vinculados al punto de venta.

Al crear el cobro, la orden de venta queda en estado completo. Se genera documento por cobrar (estado pagado) y el pago/cobro correspondiente.

Se agrega el movimiento (de la orden de venta cobrada) al cierre de caja en estado borrador (no la concilia).

El paso anterior al cierre de caja es realizar un retiro de caja: se elige un agente cobrador y se genera un movimiento retiro de caja como línea del cierre de caja.

### Cómo realizar un pago: Forma de Pago Caja en Documentos por Cobrar

Para poder realizar un cobro en ‘Efectivo’, cuando en el contexto no hay un POS, el tipo de documento utilizado en la orden de venta debe tener asociado una cuenta bancaria. 

Dicha cuenta bancaria será la utilizada para realizar el Pago/Cobro.

## Procesos

### ¿En el Cierre de Caja de Punto de Venta qué muestra el campo “Diferencia Monto”?

El campo “Diferencia Monto” representa el monto resultante de la sumatoria del Monto total de la apertura más el Total cobrado menos el Total de los retiros.

El proceso de Cierre del Punto de venta permite generar un cierre pese a que no cierre la caja en 0, sin definir la diferencia de quiebre de caja obligatoriamente.
El parámetro "Diferencia Monto" del proceso de cierre de caja, muestra el resultado de restar el monto total de cobros al total de importes de OV, para el POS en cuestión.
El mencionado parámetro parámetero se encuentra editable, para poder digitar manualmente el monto de diferencia, quedando de esa forma correctamente la línea de la conciliación.

### ¿En el Cierre de Caja de Punto de Venta qué muestra el campo “Diferencia Edo. de Cuenta”?

El campo “Diferencia Edo. de Cuenta” representa el saldo que posee la cuenta Caja 

en la que se encuentra realizando el proceso “Cierre de Caja”.