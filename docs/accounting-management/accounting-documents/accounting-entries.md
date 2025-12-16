---
title: Asientos Contables
category: Documentation
star: 9
sticky: 9
article: false
---

## Gestión de Compras

### Orden de Compra

Si no se manejan “Compromisos” no se realiza asiento contable.

### Recepción

|          Cuenta            |    Debe    |    Haber   |     Depende de    |          Campo          |  
| -------------------------- | ---------- | ---------- | ----------------- | ----------------------- |
| 14120 - inverntario Prod.A | 100,000.00 |  0.00      |  Producto         | Ingreso Inventario      |
| 21190 - Depósitos s)Fact.  | 0.00       | 100,000.00 | Socio del Negocio | Depósitos no Facturados |

### Asignación inventario (sin diferencia de Precio)

|             Cuenta               |    Debe   |   Haber   |   Depende de  |         Campo          |  
| -------------------------------- | --------- | --------- | ------------- | ---------------------- |
| 21190 - Depósitos s/Fact         | 28,352.00 | 0.00      | Socio del Neg | Depósitos no Fact.     | 
| 51290 - Ajustes a Cost. de Prod. | 0.00      | 28,352.00 | Producto      | Conciliación de invent |

### Asignación inventario (Con diferencia de Precio)

|             Cuenta               |    Debe   |   Haber   |   Depende de  |         Campo          |  
| -------------------------------- | --------- | --------- | ------------- | ---------------------- |
| 21190 - Depósitos s/Fact         | 30,000.00 | 0.00      | Socio del Neg | Depósitos no Fact.     | 
| 51290 - Ajustes a Cost. de Prod. | 0.00      | 28,352.00 | Producto      | Conciliación de invent |
| 58100 - Variación en precio Fact | 0.00      | 1,648.00  | Producto      | Variación en Precio    |

### Documento por Pagar (Producto Almacenable)

|             Cuenta               |    Debe   |   Haber   |   Depende de  |         Campo          |  
| -------------------------------- | --------- | --------- | ------------- | ---------------------- |
| 152110 - IVA Compras             | 0.00      | 0.00      | Tasa de Imp.  | Impuesto al comprar    | 
| 51290 - Ajustes a Cost. de Prod. | 10,000.00 | 0.00      | Producto      | Conciliación de invent |
| 51290 - Ajustes a Cost. de Prod. | 18,352.00 | 0.00      | Producto      | Variación en Precio    |
| 21110 - Acreedores por Compras   | 0.00      | 28,352.00 | Socio del Neg | CxP del Proveedor      |

### Documento por Pagar (Producto No Almacenable)

|             Cuenta               |    Debe   |   Haber   |   Depende de  |         Campo          |  
| -------------------------------- | --------- | --------- | ------------- | ---------------------- |
| 152110 - IVA Compras             | 7.073.44  | 0.00      | Tasa de Imp.  | Impuesto al comprar    | 
| 51117 - Costos Internet          | 32,152.00 | 0.00      | Producto      | Costos o Gastos Prod.  |
| 21110 - Acreedores por Compras   | 0.00      | 39,225.44 | Socio del Neg | CxP del Proveedor      |

### Documento por Pagar (Gastos)

|             Cuenta               |    Debe   |   Haber   |   Depende de  |         Campo          |  
| -------------------------------- | --------- | --------- | ------------- | ---------------------- |
| 74100 - Iva pérdida              | 0.00      | 0.00      | Tasa de Imp.  | Gastos de Impuesto     | 
| 78100 - Combustibles             | 3,720.00  | 0.00      | Prod/Cargo    | Costos o Gastos Prod.  |
| 21110 - Acreedores por Compras   | 0.00      | 3,720.00  | Socio del Neg | CxP del Proveedor      |

## Gestión de Ventas

### Orden de Venta

Si no se manejan “Compromisos” no se realiza asiento contable.

### Entrega (Delivery)

|          Cuenta            |    Debe    |    Haber   |     Depende de    |          Campo          |  
| -------------------------- | ---------- | ---------- | ----------------- | ----------------------- |
| 51100 - Costo Venta Prod   | 4,000.00   |  0.00      |  Producto         | COGS del Producto       |
| 14120 - Inventario de Prod | 0.00       | 4,000.00   |  Producto         | Inventario de Producto  |

### Documento por Cobrar 

|                 Cuenta                  |    Debe    |   Haber    |     Depende de    |          
| --------------------------------------- | ---------- | ---------- | ----------------- | 
| 21610 - Impuestos por pagar             | 0.00       | 66,000.00  | Tasa de Impuesto  | 
| 41000 - Ventas Productos                | 0.00       | 270,000.00 | Producto          |
| 41000 - Ventas Productos                | 0.00       | 30,000.00  | Producto          |
| 12110 - Cuentas por Cobrar Comerciales  | 366,000.00 | 0.00       | Socio del Negocio | 

## Gestión Financiera

### Cobro

|           Cuenta                  |    Debe    |    Haber   | Depende de |           Campo         | 
| --------------------------------- | ---------- | ---------- | ---------- | ----------------------- |
| 11110 - Cheques en Tránsito       | 108,629.19 |  0.00      |  Banco     | Banco Mov. no Concil.   |
| 11130 - Cheques Depósit. no Asig. | 0.00       | 108,629.19 |  Banco     | Recaudos sin Asignar    |

### Asignación (Moneda UYU)

|           Cuenta                  |    Debe    |    Haber   | Depende de    |          Campo       | 
| --------------------------------- | ---------- | ---------- | ------------- | -------------------- |
| 12110 - Cuentas por Cobrar Com.   | 0.00       | 715,534.00 | Socio del Neg | CxC Clientes         |
| 11130 - Cheques Depósit. no Asig. | 715,534.00 | 0.00       |  Banco        | Recaudos sin Asignar |

### Asignación (Moneda USD)

Al Asignar  compara los tipos de Cambio que tuvo la misma cuando fue Cobrada y Facturada

**Diferencia de Cambio Ganada**

|             Cuenta               |    Debe   |   Haber   |   Depende de  |         Campo         |  
| -------------------------------- | --------- | --------- | ------------- | --------------------- |
| 12110 - Cuentas x Cobrar Com.    | 0.00      | 79,056.69 | Socio del Neg | CxC Clientes          | 
| 80540 - Ganancia Realizada       | 0.00      | 5,268.52  | Esquema Cont. | Cta. Ganan. realizada |
| 12115 - Cuentas x Cobrar Serv.   | 5,268.52  | 0.00      | Socio del Neg | CxC Clientes          |
| 11130 - Cheques Depósit. no Asig | 79,056.69 | 0.00      | Banco         | Recaudos sin Asignar  |

**Diferencia de Cambio Perdida**

Al Asignar  compara los tipos de Cambio que tuvo la misma cuando fue Cobrada y Facturada

|             Cuenta               |    Debe   |   Haber   |   Depende de  |         Campo        |  
| -------------------------------- | --------- | --------- | ------------- | -------------------- |
| 12110 - Cuentas x Cobrar Com.    | 0.00      | 73,788.17 | Socio del Neg | CxC Clientes         | 
| 82540 - Pérdida Realizada        | 5,268.52  | 0.00      | Esquema Cont. | Pérdida realizada    |
| 12115 - Cuentas x Cobrar Serv.   | 0.00      | 5,268.52  | Socio del Neg | CxC Clientes         |
| 11130 - Cheques Depósit. no Asig | 73,788.17 | 0.00      | Banco         | Recaudos sin Asignar |

### Pago

|           Cuenta                |    Debe    |    Haber   | Depende de    |          Campo         | 
| ------------------------------- | ---------- | ---------- | ------------- | -----------------------|
| 21300 - Pagos Seleccionados     | 3,720.00   | 0.00       | Banco         | Pagos sin Asignar      |
| 11110 - Cheques en Tránsito     | 0.00       | 3,720.00   | Banco         | Banco Mov no Concil.   |

### Asignación (Pago - Documento por Pagar)

|           Cuenta                |    Debe    |    Haber   | Depende de    |          Campo         | 
| --------------------------------| ---------- | ---------- | ------------- | -----------------------|
| 21110 - Acreedores por Compras  | 3,720.00   | 0.00       | Socio del Neg | CxP del Proveedor      |
| 21300 - Pagos Seleccionados     | 0.00       | 3,720.00   | Banco         | Pagos sin Asignar      |

### Cheque Diferido por Pagar

Emisión

|           Cuenta                |    Debe    |    Haber   | Depende de     |         Campo          |
| ------------------------------- | ---------- | ---------- | -------------- | -----------------------|
| 15300 - Cta Puente Cheque Dif.  | 186,361.52 | 0.00       | Cargo Definido | Cargo Gasto e ingreso  |
| 21200 - Cheques Dif. a pagar    | 0.00       | 186,361.52 | Esquema Contab | Cheques Dif x pagar    |

### Pago Diferido

Cancelación de Deuda tipo Nota de Crédito) simultáneo a la creación del Cheque

|           Cuenta                |    Debe    |    Haber   | Depende de     |         Campo          |
| ------------------------------- | ---------- | ---------- | -------------- | -----------------------|
| 21110 - Acreedores por Compras. | 186,361.52 | 0.00       | Socio del Neg  | CxP del Proveedor      |
| 15300 - Cta Puente Cheque Dif.  | 0.00       | 186,361.52 | Cargo          | Cargo Gasto e ingreso  |

### Asignación (Cobro Diferido - Documento por Cobrar)

Igual que una Nota de Crédito, Debita el saldo de Acreedores por Compras ya en el Documento Nota de Crédito. La asignación sólo se realiza por si existe diferencia de Cambio en la Asignación.

|           Cuenta                |    Debe    |    Haber   | Depende de     |         Campo          |
| ------------------------------- | ---------- | ---------- | -------------- | -----------------------|
| 21110 - Acreedores por Compras. | 186,361.52 | 0.00       | Socio del Neg  | CxP del Proveedor      |
| 21110 - Acreedores por Compras. | 0.00       | 186,361.52 | Socio del Neg  | CxP del Proveedor      |

### Débito de Cheque

Cuando el Tercero a quién se le entrega el Cheque realiza el Depósito. Más adelante se puede generar un Proceso de realizar el Débito de manera automática cuando el mismo se vence.

|           Cuenta                |    Debe    |    Haber   | Depende de     |         Campo         |
| ------------------------------- | ---------- | ---------- | -------------- | ----------------------|
| 21300 - Pagos Seleccionados     | 3,000.00   | 0.00       | Banco          | Pagos sin Asignar     |
| 11110 - Pagos en Tránsito       | 0.00       | 3,000.00   | Banco          | Banco Mov. no Concil. |

### Asignación (Cheque Diferido por Cobrar - Débito de Cheque)

|           Cuenta                |    Debe    |    Haber   | Depende de     |         Campo         |
| ------------------------------- | ---------- | ---------- | -------------- | ----------------------|
| 21200 - Cheques Dif. a Pagar    | 3,000.00   | 0.00       | Esquema Cont.  | Cheques Dif x Pagar   |
| 21300 - Pagos Seleccionados     | 0.00       | 3,000.00   | Banco          | Banco Mov. no Concil. |

### Cheque Diferido por Cobrar

|           Cuenta                |    Debe    |    Haber   | Depende de     |         Campo          |
| ------------------------------- | ---------- | ---------- | -------------- | -----------------------|
| 21200 - Cheques Dif. x Cobrar   | 23,713.14  | 0.00       | Esquema Cont.  | Cheques Dif x Pagar    |
| 15300 - Cta Puente Cheque Dif.  | 0.00       | 23,713.14  | Cargo Definido | Cargo Gasto e Ingreso  |

### Cobro Diferido

Documento del Tipo Nota de Crédito que genera el Cheque Diferido por Cobrar para “Bajar” el saldo de los Documentos por Cobrar que está cancelando. 

|           Cuenta                |    Debe    |    Haber   | Depende de     |         Campo          |
| ------------------------------- | ---------- | ---------- | -------------- | -----------------------|
| 15300 - Cta Puente Cheque Dif.  | 23,713.14  | 0.00       | Cargo          | Cargo Gasto e Ingreso  |
| 12110 - Cuentas x Cobrar Com.   | 0.00       | 23,713.14  | Socio del Neg  | CxC del Cliente        |


### Asignación (Cobro Diferido - Documento por Pagar)

mismo momento que cobro diferido

|           Cuenta                |    Debe    |    Haber   | Depende de     |         Campo          |
| ------------------------------- | ---------- | ---------- | -------------- | -----------------------|
| 12110 - Cuentas x Cobrar Com.   | 23,713.14  | 0.00       | Socio del Neg  | CxC del Cliente        |
| 12110 - Cuentas x Cobrar Com.   | 0.00       | 23,713.14  | Socio del Neg  | CxC del Cliente        |

### Asignación (Cobro Diferido - Documento por Pagar en Moneda USD)

mismo momento que cobro diferido

|             Cuenta               |    Debe   |   Haber   |   Depende de  |         Campo           |  
| -------------------------------- | --------- | --------- | ------------- | ----------------------- |
| 12110 - Cuentas x Cobrar Com.    | 23,713.14 | 0.00      | Socio del Neg | CxC Clientes            | 
| 12110 - Cuentas x Cobrar Com.    | 83.67     | 0.00      | Socio del Neg | CxC Clientes            |
| 82540 - Pérdida/Ganan. Realizada | 0.00      | 83.67     | Esquema Cont. | Pérdida/Ganan Realizada |
| 12110 - Cuentas x Cobrar Com.    | 0.00      | 23,713.14 | Socio del Neg | CxC Clientes            |

### Depósito de Cheque Diferido por Cobrar

Cuando el Tercero a quién se le entrega el Cheque realiza el Depósito. Más adelante se puede generar un Proceso de realizar el Débito de manera automática cuando el mismo se vence.

|           Cuenta                |    Debe    |    Haber   | Depende de    |          Campo         | 
| ------------------------------- | ---------- | ---------- | ------------- | -----------------------|
| 11110 - Cheques en Tránsito     | 23,713.14  | 0.00       | Banco         | Banco Mov no Concil.   |
| 11130 - Cheques Depós. no Asig  | 0.00       | 23,713.14  | Banco         | Banco Recaud. sin Asig |

### Asignación (Depósito - Cheque Diferido por Cobrar)

|           Cuenta                |    Debe    |    Haber   | Depende de    |          Campo         | 
| ------------------------------- | ---------- | ---------- | ------------- | -----------------------|
| 11130 - Cheques Depós. no Asig  | 23,713.14  | 0.00       | Banco         | Banco Recaud. sin Asig |
| 12120 - Cheques Dif x Cobrar    | 0.00       | 23,713.14  | Esquema Cont. | Cheques Dif x Cobrar   |

### Conciliación Bancaria

Por cada línea de Estado de Cuenta se puede tener las siguientes aplicaciones contables

|             Cuenta            |    Debe   |   Haber   |   Depende de  |         Campo             |  
| ----------------------------- | --------- | --------- | ------------- | ------------------------- |
| 11100 - Banco Santander UYU   | 23,713.14 | 0.00      | Banco         | Bancos                    | 
| 11110 - Cheques en Tránsito   | 83.67     | 0.00      | Banco         | Banco Mov no Concil.      |
| 79600 - Otros Gastos          | 0.00      | 83.67     | Cargo         | Gasto o Ingr según signo  |
| 82100 - Intereses             | 0.00      | 23,713.14 | Banco         | +Ingr/-Gasto x int Banc.  |

### Cuentas Puente

### Cheques en Tránsito (Activo)

La cuenta Cheques en tránsito es utilizada por Solop para dejar registro de todo **movimiento Financiero** que esté registrado en el sistema pero **que aún no fue verificado en la cuenta bancaria** utilizada. 

El hecho de que se registre un Pago/Cobro en el sistema significa que por un lado, debería aumentar o reducir un Activo monetario (ej. Saldo del Banco) y por otro lado, cancelar una deuda o activo generado por un Documento por Pagar o Cobrar. 

La parte “Monetaria” de una Pago/Cobro es la que maneja la cuenta “cheques en tránsito” siendo una cuenta puente antes de confirmar su correspondiente Ingreso/Egreso del banco.

Movimientos de la cuenta contable:

La cuenta Cheques en Tránsito se parametriza en la Cuenta Bancaria, campo Cheques en Transito.

**Saldo en cuenta Cheques En Tránsito**

Si se cuenta con saldo en la cuenta Cheques en tránsito significa que existen Pagos o Cobros procesados que aún no fueron conciliados en su correspondiente cuenta bancaria.

#### Reporte Auxiliar

Reporte Auxiliar de la cuenta “Cheques En tránsito” -> “Pagos sin Conciliar” o “Detalles del Pago”.

Mediante el reporte Auxiliar, se podrá visualizar todos con el mismo ordenamiento cómo se compone el saldo de la cuenta contable. A diferencia del mayor contable, desde el reporte podemos ver específicamente los movimientos que deberían estar ocasionando dicho saldo en la cuenta.