---
title: Analizando Cuentas Contables de Tránsito
category: Documentation
star: 9
sticky: 9
article: false
---

Las cuentas contables de tránsito también llamadas cuentas de Control en Solop ERP son cuentas temporales utilizadas para registrar movimientos contables intermedios, que luego se compensan cuando se completa el circuito de una operación. Sirven para reflejar correctamente el estado contable en cada etapa del proceso, especialmente cuando hay diferencia de tiempo entre el ingreso físico y el registro contable final.

Se podrá analizar los saldos contables y su correspondencia con los reportes auxiliares (documentos) vinculados a cada una de estas cuentas.

Las Cuentas Contables de Tránsito son:

1. Cheques en Tránsito
2. Cheques Depósito no Asignados
3. Pagos Seleccionados
4. Ajustes a Costos de Productos
5. Depósitos sin Facturar
6. Entregas sin Facturar (Ingresos no Facturados)
7. Recepciones sin Facturar (Depósitos no Facturados)

Aquí podrá encontrar algunos consejos que le ayudarán a controlar y encontrar discrepancias en algunas Cuentas Contables transitorias utilizadas por Solop ERP.

## Cheques en Tránsito (Activo)

La cuenta Cheques en tránsito es utilizada por Solop ERP para dejar registro de todo movimiento Financiero que esté registrado en el sistema pero que aún no fue verificado en la cuenta bancaria utilizada. El hecho de que se registre un Pago/Cobro en el sistema significará que por un lado, debería aumentar o reducir un Activo monetario (ej. Saldo del Banco) y por otro lado, cancelar una deuda o activo generado por un Documento por Pagar o Cobrar. La parte "Monetaria" de una Pago/Cobro es la que manejará la cuenta "cheques en tránsito" siendo una cuenta intermedia antes de confirmar su correspondiente Ingreso/Egreso del banco. Movimientos de la cuenta contable:

La cuenta Cheques en Tránsito se parametriza en la Cuenta Bancaria, campo Cheques en Transito.


**Cuando la Empresa cobra:**

Debita con: Cobros

Acredita con: Conciliación Bancaria

**Cuando la Empresa Paga:**

Debita con Conciliación Bancaria

Acredita con: Pagos

### Reporte de Pagos/Cobros sin conciliar

La composición de la Cuenta Contable Cheques en Tránsito se analiza en el **Reporte de Pagos sin Conciliar.**

Dicho reporte mostrará aquellos documentos de Pago/Cobro que involucren a Cuentas Bancarias y que no han sido conciliados aún.

### Analizando Pagos/Cobros sin conciliar mediante el Balance de Prueba.

Podrá realizar los siguientes pasos que le ayudará a comprender y verificar el saldo de esta cuenta:

#### Transacciones con una sola moneda

1. Emitir el Balance de Prueba de la cuenta contable "Cheques en Tránsito" por Socio de Negocio.
2. Exportar con formato XLSX.
3. Identifique las contabilizaciones que correspondan a transacciones anuladas. Píntar las anuladas.
4. Sumar las filas identificadas y verificar que sumen 0.
5. Vincular Pagos con Conciliaciones. Pintarlos. Verificar que sumen 0.
6. Vincular Cobros con Conciliaciones. Pintarlos. Verificar que semen 0.
7. Las transacciones que quedaron sin identificar corresponderá al saldo de la cuenta. Es decir a los Pagos/Cobros sin Conciliar.
8. También podrá emitir el Reporte de Pagos sin Conciliar (le mostrará los pagos no conciliados a la fecha, cualquier estado).

#### Transacciones en varias monedas

1. Emitir el Balance de Prueba de la cuenta contable "Cheques en Tránsito" por Socio de Negocio y Moneda.
2. Exportar con formato XLSX.
3. Identifique las contabilizaciones que correspondan a transacciones anuladas. Píntar las anuladas.
4. Sumar las filas identificadas y verificar que sumen 0.
5. Vincular Pagos con Conciliaciones. Pintarlos. Verificar que sumen 0.
6. Vincular Cobros con Conciliaciones. Pintarlos. Verificar que semen 0.
7. Las transacciones que quedaron sin identificar corresponderá al saldo de la cuenta. Es decir a los Pagos/Cobros sin Conciliar.

### Cuenta Cheques en Tránsito con Moneda Extranjera

Si la cuenta contable Cheques en Tránsito se utiliza para realizar transacciones en varias monedas o sólo en Moneda Extranjera, se deberá parametrizar el elemento contable como:

* Cuenta Banco
* Maneja Moneda Extranjera SI
* Moneda USD

De esta manera participará en el proceso de revaluación de saldos en Moneda Extranjera Cheques.

## Cheques Depósito no Asignados (Activo)  11130

El Saldo de esta cuenta representará el saldo actual de todos los Cobros que ya fueron registrados pero que aún no fueron asignados a que facturas estarían cancelando.

**Documento Cobro:**

La Cuenta Cheques Depositados sin Asignar es la cuenta que utiliza los Cobros para dejar registro de que existió un Cobro que debería terminar bajando el "Activo" del Documento por Cobrar pero que como aún no está identificado (en el Documento "Cobro") no baja directamente la cuenta de "Cuentas por Cobrar Comerciales".

Acción Contable Cobro:  Crédito (Haber)

Por esta razón, Solop ERP utiliza una cuenta puente intermedia para que luego otro documento (asiento) genere la correspondiente baja del Activo de "Cuentas por Cobrar Comerciales" (Cuenta que movió realmente la Factura pendiente) una vez sea Asignada la factura exacta que está cancelando el Cobro.

**Documento Asignación:**

En el momento de la Asignación es cuando se define exactamente la factura que se estará cancelando con el cobro/s en cuestión bajando ahora el saldo del Activo que existía en la Factura por Cobrar, cancelando también el saldo existente en la cuenta de "Cheques Depósitos sin Asignar"

Acción Contable Asignación:  Débito (Debe)

**Reporte Auxiliar de Cuenta: Pagos sin Asignar**

El reporte que explicará el saldo de la cuenta a nivel documental será el "Pagos sin Asignar" filtrando por "Transacción de Ventas = SI" (ya que sólo corresponde a los Cobros que aún no estén asignados.

Podrá realizar los siguientes pasos que le ayudará a comprender y verificar el saldo de esta cuenta:

**Controles recomendados:**

### Transacciones con una sola moneda

1. Emitir el Balance de Prueba de la cuenta contable "Cheques Depósito no Asignados" por Socio de Negocio.
2. Exportar con formato XLSX.
3. Identifique las contabilizaciones que correspondan a transacciones anuladas. Píntar las anuladas.
4. Sumar las filas identificadas y verificar que sumen 0.
5. Vincular Pagos con Asignaciones. Pintarlos. Verificar que sumen 0.
6. Vincular Cobros con Asignaciones. Pintarlos. Verificar que sumen 0.
7. Las transacciones que quedaron sin identificar corresponderá al saldo de la cuenta. Es decir a los Pagos/Cobros sin Asignar.
8. También podrá emitir el Reporte de Pagos sin Asignar (le mostrará los pagos no Asignados a la fecha , cualquier estado)

### Transacciones en varias monedas

1. Emitir el Balance de Prueba de la cuenta contable "Cheques Depósito no Asignados" por Socio de Negocio y Moneda.
2. Exportar con formato XLSX.
3. Identifique las contabilizaciones que correspondan a transacciones anuladas. Píntar las anuladas.
4. Sumar las filas identificadas y verificar que sumen 0.
5. Vincular Pagos con Asignaciones. Pintarlos. Verificar que sumen 0.
6. Vincular Cobros con Asignaciones. Pintarlos. Verificar que sumen 0.
7. Las transacciones que quedaron sin identificar corresponderá al saldo de la cuenta. Es decir a los Pagos/Cobros sin Asignar.

## Pagos Seleccionados (Pasivo)    21300

La cuenta “Pagos Seleccionados” es utilizada como puente entre las transacciones que se Pagan contra los Documentos que se están cancelando.

La cuenta *Pagos Seleccionados* se parametriza en la ventana Esquema Contable, pestaña por Defecto sector Banco.

Documentos que mueve esta cuenta:

**Pago:** Todos los Pagos que sean realizados que no tengan definido un Cargo ni que son “Anticipo” estarán impactando contra la cuenta contable “Pagos Seleccionado”

Acción Contable: Débito (Debe)

**Asignación:** Los Saldos existentes en la cuenta puente “Pagos Seleccionados” se bajarán (Acreditarán) con el documento “Asignación”. En este documento la idea es definir que Documentos estaría cancelando el Pago en cuestión que aún no está asignado. En las asignaciones se puede definir un Documento por Pagar como también un Cobro o incluso enviar el saldo contra un “Cargo”. En cualquier caso que se seleccione un pago que no sea un Anticipo se estará acreditando la cuenta “pagos Seleccionados”.

Acción Contable: Crédito (Haber)

**Reporte Auxiliar de Cuenta**

El saldo de la cuenta contable “Pagos Seleccionados” se debería poder explicar con el Reporte “Pagos sin Asignar”

## Ajustes a Costos de Productos (Pérdida)   51290

Esta cuenta de tránsito es utilizada entre los Productos recepcionados que son almacenables y su correspondiente factura, realizando el ajuste que corresponda entre el Costo de dicho Producto (que es el importe por el cuál se realiza la recepción o según la definición de Costeo que manejen) contra el precio que realmente fue Facturado.

**Movimientos de la cuenta contable:**

Debita con: Documento por Pagar                Acredita con: Asignación con Recepción

La cuenta Ajustes a Costos de Productos se parametriza en la ventana Esquema Contable, pestaña por Defecto sector Producto.

## Depósitos sin Facturar (Pasivo)    21190

La cuenta Depósitos sin Facturar (o Recepciones sin Facturar) se parametriza en la ventana Esquema Contable, pestaña por Defecto sector Socio del Negocio.

Esta cuenta de verificación refleja los Productos recepcionados y cuya recepción no se asignó a un Documento por Pagar.

**Movimientos de la cuenta contable:**

Debita con: Asignación                               Acredita con: Recepción

### Identificación de los documentos Entregas/Delivery sin facturar mediante Reporte

La composición de la Cuenta Contable Entrega Pendiente de Facturar se analiza en el **Reporte Recepciones sin Facturar**

Dicho reporte mostrará aquellos documentos de Recepción que no han sido asignados a facturas aún.

### Identificación de la composición del Saldo mediante el balance de Prueba

## Entrega pendiente de Facturar

La cuenta Pendiente de Facturar se parametriza en la ventana Esquema Contable, pestaña por Defecto sector Socio del Negocio.

La cuenta contable de *Entrega Pendiente de Facturar* (o Cuentas por Cobrar sin Facturar)  refleja los productos tipo Servicios con entregas realizadas y que aún no han sido facturadas.

**Movimientos de la cuenta contable:**

Debita con: Entrega/Delivery                                Acredita con: Documento por Cobrar

### Identificación de los documentos Entregas/Delivery sin facturar mediante Reporte

La composición de la Cuenta Contable Entrega Pendiente de Facturar se analiza en el **Reporte Entregas sin Facturar**

Dicho reporte mostrará aquellos documentos de Entrega/Delivery que no han sido facturados aún.

### Identificación de la composición del Saldo mediante el balance de Prueba

* Debita con: Asignación Recepción /Documento por Pagar
* Acredita con: Recepción

Reporte: Depósitos sin Facturar