---
title: Devolución Cliente/proveedor
category: Documentation
star: 9
sticky: 9
tag: 
  - Agencia
article: false
---

## Devoluciones

### Devoluciones a Cliente

Se deberá realizar la “Devolución de Cliente” cuando un Cliente solicita o el Ejecutivo de Ventas solicita en nombre del cliente, la emisión de una Nota de Crédito debido a una “Entrega” (Delivery) No aceptada por el cliente.

Esta “Devolución Cliente” deberá ser generada desde el Proceso “Generar Devoluciones”, seleccionando la Orden de Venta del Cliente que se querrá devolver.

### Generar Devoluciones (Proceso)

Este proceso se deberá realizar si se desea “Corregir” un checking ya realizado en un Período anterior que se encuentra ya CERRADO. Lo que realizará esta “Devolución Cliente” son 2 acciones:

Generar un Movimiento contrario a la Entrega realizada por el Checking. Restando así el Ingreso reconocido con dicha “Entrega”

Generar una Devolución de Proveedor Espejo, es decir se generará una Devolución Cliente y una Devolución Proveedor por la MISMA CANTIDAD definida. Dichas devoluciones luego quedarán a la espera de sus correspondientes Notas de Crédito. Administración podrá ver las Devoluciones Cliente que están pendientes de Generar Nota de Crédito y del lado del Proveedor estarán las “Devoluciones Proveedor” (o RMA) pendientes de generar Notas de Crédito Proveedor cuando estas lleguen.

### Devolución al Proveedor

El proceso de “Generar Devoluciones” generará también una “Devolución Proveedor” por la Cantidad que se definió en el proceso, el precio será tomado desde la Orden de Compra correspondiente a la Recepción que se estará devolviendo.

Para generar la Nota de Crédito del Proveedor se deberá ir directo a la ventana “Documentos por Pagar” y crear el cabezal de la Nota de Crédito Proveedor correspondiente. Luego se deberá crear las líneas a partir del Proceso “Crear Desde” desd donde se deberá seleccionar la opción “RMA”