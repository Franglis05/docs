---
title: Flujo de Pago a Proveedores
category: Documentation
star: 9
sticky: 9
article: false
---

## Descripción del circuito

### 1. Generar Selección de Pagos

Inicialmente en la Ventana Selección de Pagos elegimos el Proveedor a pagar y Moneda.

Ejecutamos el botón de acción Seleccionar DXP (con control).

Esto abre una ventana emergente (smart browser): filtramos por la moneda que deseamos pagar y seleccionamos **Comenzar búsqueda**.

Esto desplegará en el visor de pantalla aquellos documentos (que coincidan con los filtros ingresados) que posean saldo abierto (impago).

Elegimos el/los documentos por pagar a abonar.

Al volver a la ventana de Selección de Pagos, podremos ver en el visor de pantalla los datos del dcocumento seleccionado en solapa Facturas **Proveedor a Pagar**.

### 2. Completar Selección de Pagos

Previamente seleccionados los documentos a pagar es posible **Completar** el registro de selección de pagos (o bien setearlo en **Preparar**, en el caso de requerir una aprobación interna).

### 3. Imprimir Selección de Pagos

Desde el botón de procesos (de la barra de comandos) se selecciona "Impresión Selección de Pagos" para obtener representación gráfica del documento (con su correspondiente detalle: proyecto, factura, importe, moneda, etc.).

### 4. Generar Pago/cobro

Una vez que se Completa el documento (el cual puede quedar configurado con su correspondiente cuenta bancaria, o bien setearla en tiempo posterior), es posible generar el pago desde el botón de procesos: **Generar PagoCobro**.

Esto abre una ventana emergente de proceso en donde se setea la **cuenta bancaria** (o se verá por defecto la configurada en la selección de pago) y la **Regla de Pago**.

### 5. Generar Recibo de Pago

Cuando el proveedor se acerca a recibir la cobranza, se emite el Recibo de pago (seleccionando el proveedor correspondiente).

Elegimos Crear desde Selección de Pagos. Esto abre ventana emergente de proceso en la cual seleccionamos la que corresponde.

Al aceptar se llenan los campos  del recibo de pago con los datos por defecto heredados de la selección de pago (documentos asignados, pagos contado o cheque según corresponda).

Se finaliza el circuito al Completar el Recibo de Pago (en el caso de contar con un recibo de canje, se deberá ingresar el número en el cabezal, sección Recibo de Canje.

![Diagrama](/assets/img/docs/balance-management/bam-balance-image414.png)
