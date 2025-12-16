---
title: Cierre de Balance
category: Documentation
star: 9
sticky: 9
article: false
---

El Proceso de Cierre de Balance en Solop consta de varios pasos y controles que detallaremos a continuación:

* Actualizar Documento a Documento los Saldos Abiertos de Documentos por Cobrar y Documentos por Pagar
* Actualizar los Saldos Contables de las Cuentas Monetarias en Moneda Extranjera

A continuación les detallaremos cada uno de ellos.

## 1. Diferencia de Cambio no Realizada 

Solop ERP cuenta con un proceso para realizar el cálculo y aplicación contable correspondiente a la actualización de los saldos contables de las Cuentas por Cobrar y Cuentas por Pagar (que aún no hayan sido canceladas a la fecha de revaluación). 

Esquema Contable: Seleccionar el Esquema Contable que se quiere registrar la Diferencia de Cambio.
Tipo de Conversión de Revaluación: Tipo de Conversión de la revaluación.
Fecha de Revaluación: Fecha a realizar proceso
CP-CC: Cuentas X Pagar (incluye documentos a Pagar como son los cheques diferidos , Cuentas X Cobrar o ambas.
Incluir Todas las Monedas: No hacer click. Dejar Vacío
Moneda:  Dejar Vacío 
Revalorización Tipo de Documento: donde genera el asiento de revaluación (GL Document)- General Ledger (Contabilidad)

Dicho proceso realizará el cálculo necesario para actualizar la aplicación contable de los Saldos de todos aquellos Documentos por Cobrar y por Pagar que se encuentren Pendientes a la fecha de Revaluación. 

El Resultado lo mostrará en el Reporte de Diferencia de Cambio No Realizada detallando línea a línea los Documentos con el cálculo realizado.

### Reporte de Diferencia de cambio DXC y DXP no Realizada

La emisión del Reporte genera un Asiento Contable en borrador detallando línea a línea los ajustes que se estarían realizando documento por documento.

El mismo lo podrán encontrar en la Ventana de Diario Contable

El Lote del  Asiento Contable deberá completarse

Si desea anular un Asiento ya Completo deberá Anular y Corregir para que la fecha de anulación sea la misma que la del asiento.

::: warning
CUIDADO La acción Anular y Causación crea el asiento con la fecha de hoy.
:::

Emitir Reportes de Saldos Abiertos a la Fecha del proceso de:

Transacciones de Ventas incluyendo Cheques Diferidos 

No Transacciones de Venta incluyendo Cheques Diferidos

Considerar sólo las operaciones en Monedas Extranjeras ( no hay filtro de MONEDA).
Debe filtrarse externamente.

### Verificación de Diferencias de Cambio CXP y CXC

1. Verificar que reportes Auxiliares y Balance dan igual según Importe Fuente (Opcional)

a. Verificar Cuentas por Cobrar: Se deberá verificar que los importes de saldos pendientes reflejado en el reporte Saldo Pendiente a la Fecha de igual que sus correspondiente Saldo Contable. Para dar mayor facilidad para encontrar posibles diferencias, se recomienda utilizar en ambos reportes una vista similar donde agrupe primero por Moneda y luego por Socio del Negocio, de manera que se podrá comparar fácilmente entre Monedas Fuente de los documentos.
i. Obtener el reporte de “Saldos Abiertos a la Fecha” definiendo la misma fecha que se está realizando el Cierre de Balance, con el filtro de “Transacción de Ventas = Si”
ii. Obtener el Balance de Prueba para la cuenta “12110 - Cuentas por Cobrar Comerciales” y utilizar la vista del reporte “ Mayor Contable por Moneda / SDN”.
b. Verificar Cuentas por Pagar:
i. Obtener el reporte de “Saldos Abiertos a la Fecha”, con el filtro de “Transacción de Ventas = No”
ii. Obtener el Balance de Prueba para la cuenta “21100 - Cuentas por Pagar Comerciales” y utilizar la vista del reporte “ Mayor Contable por Moneda / SDN”.

2. Proceso de “Ajuste de Diferencia de Cambio No Realizada” (Factura Pérdida/Ganancia No Realizada)

3. Verificar que da igual reportes Auxiliares y Balance

a. Verificar Cuentas por Cobrar:
i. Obtener el reporte de “Saldos Abiertos a la Fecha”, con el filtro de “Transacción de Ventas = Si”
ii. Obtener el Balance de Prueba para la cuenta “12110 - Cuentas por Cobrar Comerciales” y utilizar la vista del reporte “ Mayor Contable por Moneda / SDN”.
b. Verificar Cuentas por Pagar:
i. Obtener el reporte de “Saldos Abiertos a la Fecha”, con el filtro de “Transacción de Ventas = No”
ii. Obtener el Balance de Prueba para la cuenta “21100 - Cuentas por Pagar Comerciales” y utilizar la vista del reporte “ Mayor Contable por Moneda / SDN”.

## 2. Diferencia de Cambio Cuentas Integrales

Este Proceso tomará todas las Cuentas Contables Integrales “definidas” como Moneda Extranjera. Considera la moneda que tenga asignada dicha cuenta. 

Este proceso no tomará las diferencias que existan en Cuentas Contables Integrales que sean afectadas por Documentos por Pagar o Documentos por Cobrar.

Monedas: moneda a considerar en revaluación
Tipo de Conversión:  Tipo Conversión utilizada en el proceso
Revalorización Tipo de Documento: GL   (General Ledger) donde genera el asiento de revaluación.

### Descripción del Proceso

El proceso de cambio de cuentas integrales analiza aquellas cuentas contables que estén definidos como "Moneda Extranjera=Y", considerando todos los movimientos que estén en moneda extranjera. Verifica que su saldo acumulado final sea realizado a la conversión correcta comparando con la Tasa de Cambio de la fecha definida (normalmente cierre de ejercicio). 

Si dicha cuenta tiene un saldo en alguna moneda extranjera, aplicará un asiento de ajuste por el importe en UYU que falte para que los USD queden registrados con su correcta conversión.

::: note
Importante: El proceso de "Diferencia de Cambio Cuentas Integrales" no mira saldos totales de cuentas contables a la fecha, sino que mira exclusivamente el saldo en cada una de las correspondientes monedas fuente. Esto significa que si bien una cuenta pueda tener un saldo cero a final de ejercicio, luego que se corra el proceso de diferencia de cambio, se actualizarán los USD que no estén actualizados correctamente y le aplicará un asiento de ajuste por diferencia de cambio de cuenta integral (Monetaria).
:::

### Comprobación del Proceso de Diferencia de Cambio de Cuentas Monetarias

Compare el saldo  actual (en la moneda esquema) de las cuentas contables monetarias y el saldo que debería tener a la fecha de cierre del Período como producto de multiplicar los saldos en moneda extranjera por la Tasa de Cambio de cierre del Período.
Ese producto debería ser el valor de la diferencia de cambio.

La emisión del Reporte genera un Asiento Contable en estado borrador con la Descripción Diferencia de Cambio Cuentas Integrales, detallando línea a línea los ajustes que se estarían realizando en las diferentes Cuentas Contables.

El mismo lo podrán encontrar en la Ventana de Diario Contable

El Lote del Asiento Contable deberá completarse

## 3. Cierre del Período Anual Fiscal

Este proceso cierra las cuentas de gastos/ingresos al final del Periodo Financiero. 
 
El proceso crea un Lote de Notas Contables, con una Nota Contable con cada cuenta de costo/gasto con saldo. Luego de completar el lote, el saldo de todas las cuentas de costo/gasto es cero, mientras el monto transferido corresponde al resultado bruto.
La cuenta destinataria se escoge como parámetro.

En el proceso se deberán definir los siguientes campos: 

Organización: Organización que desea correr el proceso. 
Esquema Contable: Seleccionar el Esquema Contable que se quiere registrar el Asiento de Cierre de Resultados.  
Cuenta Resultado del Ejercicio: Cuenta contable que se desea enviar el Resultado del Ejercicio. (Por defecto existe la cuenta “32101- Resultados del ejercicio”)
Fecha Cierre de Ejercicio: Fecha para la que se quiere realizar el Cierre de Resultado
Tipo de Documento: Seleccionar el Tipo de Documento “GL Journal Batch”
Categoría Contabilidad: Seleccionar la Categoría “Manual”

El Lote del  Asiento Contable deberá completarse

## 4. Cierre Ejercicio Cuentas Integrales (Opcional)

Este proceso cierra las cuentas Integrales al final del periodo anual fiscal para luego volver a abrirlas el 1er día del período siguiente como “Saldo Apertura”. La cuenta destinataria se escoge como parámetro. El proceso de cierre crea un Lote de Notas Contables, con una Nota Contable con cada cuenta Integral con saldo. 

El proceso de apertura crea un Lote de Notas Contables, con una Nota Contable con cada cuenta Integral con saldo. 

**Cierre**
Este proceso se utiliza en al final del Período Financiero para extornar todas las cuentas integrales.El proceso crea un Lote Contable de cada cuenta de Activo y la contracuenta se define como parámetro. También crea un Lote Contable con cada cuenta de Pasivo y Patrimonio y la contracuenta es la que se definió como parámetro.
El resultado es el cierre de todas las cuentas Integrales. El saldo de la cuenta parámetro es cero.

Este Asiento Contable se Completa automáticamente.

**Apertura**
Este proceso crea un Lote Contable de cada cuenta de Activo y la contracuenta definida como parámetro. También crea un Lote Contable con cada cuenta de Pasivo y Patrimonio y la contracuenta es la que se definió como parámetro.
El resultado es la apertura de todas las cuentas Integrales. El saldo de la cuenta parámetro es cero.

Este Asiento Contable se Completa automáticamente.