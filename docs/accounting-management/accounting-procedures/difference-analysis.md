---
title: Análisis de Diferencias
category: Documentation
star: 9
sticky: 9
article: false
---

### Analizando la Diferencia de Cambio no Realizada

El proceso para realizar la verificación Contable con los Saldos Abiertos que existe en los Auxiliares se puede realizar mediante los siguientes pasos:

### Verificación del Ajuste Cuentas por Pagar y por Cobrar

* Verificar que todos dan igual según Importe Fuente (Opcional)

* Obtención de Reporte de Saldos Abiertos cuentas por Cobrar

* Balance de Prueba Cuenta “Cuentas por Cobrar Comerciales”

* Obtención de Reporte de Saldos Abiertos cuentas por Pagar

* Balance de Prueba Cuenta “Cuenta por Pagar Comerciales”

*  Proceso de “Ajuste de Diferencia de Cambio No Realizada” (Factura Pérdida/Ganancia No Realizada)

* Verificar que da igual reportes Auxiliares y Balance

* Obtención de Reporte de Saldos Abiertos cuentas por Cobrar

* Balance de Prueba Cuenta “Cuentas por Cobrar Comerciales”

* Obtención de Reporte de Saldos Abiertos cuentas por Pagar

* Balance de Prueba Cuenta “Cuenta por Pagar Comerciales”

### Explicación del Ajuste realizado por el Proceso de DIferencia de Cambio No Realizada

El proceso de diferencia de cambio No Realizada puede controlarse, para ello deberá exportar a Excel el Reporte que brinda el proceso del cálculo de Diferencia de Cambio No Realizada al momento que la ejecuta. Cuidado, este reporte presentará el cálculo realizado y no podrá obtenerse nuevamente a menos que genere el proceso una vez más, generando así el Asiento del Ajuste nuevamente.

En la planilla verá documento por documento sus aplicaciones en moneda fuente, en moneda esquema, los importes revaluados considerando la tasa de cambio seleccionada y las diferencias a revaluar.

## Comprobación de Cálculo de Diferencia de Cambio no Realizada

Como forma de comprobación del proceso realizado usted podrá emitir los siguientes reportes:

### En Documentos por Pagar y Documentos por Cobrar

Emitir Reportes de Saldos Abiertos a la Fecha del proceso de:

* Transacciones de Ventas incluyendo Cheques Diferidos
* No Transacciones de Venta incluyendo Cheques Diferidos

Considerar sólo las operaciones en Monedas Extranjeras (no hay filtro de MONEDA, las deberá excluir en una planilla externa)

## Verificación de Diferencias de Cambio Cuentas por Pagar y Cuentas por Cobrar

Obtener el Informe Financiero “Balancete de Cuentas Contables” a fecha de Cierre de Ejercicio

Verificación de Saldos Contables de Cuentas de Documentos:

En estos casos, las líneas de Ganancia/Pérdida por Diferencia de Cambio Realizada se realizan SIEMPRE con Moneda del Esquema Contable, de manera que no estarán clasificadas como con Moneda USD sino con UYU si su esquema contable está en UYU.

1. Seleccione Organización
2. Transacción de Ventas: SI
3. A Fecha de cierre de fecha de Período Financiero
4. Con Cheques Diferidos

* **Esquema Contable:** Seleccionar el Esquema Contable que se quiere registrar la Diferencia de Cambio.
* **Tipo de Conversión de Revaluación:** Tipo de Conversión de la revaluación.
* **Fecha de Revaluación:** Fecha a realizar proceso
* **CP-CC: Cuentas por Pagar:** (incluye documentos a Pagar como son los cheques diferidos , Cuentas por Cobrar o ambas.
* **Incluir Todas las Monedas:** No hacer click. Dejar Vacío
* **Moneda:** Dejar Vacío
* **Revalorización Tipo de Documento:** donde genera el asiento de revaluación (GL Document)- General Ledger (Contabilidad)

Dicho proceso realizará el cálculo necesario para actualizar la aplicación contable de los Saldos de todos aquellos Documentos por Cobrar y Documentos por Pagar que se encuentren Pendientes de Pago/Cobro a la fecha de Revaluación.

El Resultado lo mostrará en el Reporte de Diferencia de Cambio No Realizada detallando línea a línea los Documentos con el cálculo realizado.


### Reporte de Diferencia de Cambio Documentos por Cobrar y Documentos por Pagar no Realizada

La emisión del Reporte genera un Asiento Contable en borrador detallando línea a línea los ajustes que se estarían realizando documento por documento.

Este mismo lo podrán encontrar en la Ventana de Diario Contable, en forma de Asiento Contable

El Lote del Asiento Contable deberá completarse

### Anular el Asiento de Revaluación

Si desea anular un Asiento ya Completo deberá Anular y Corregir para que la fecha de anulación sea la misma que la del asiento.

CUIDADO La acción Anular y Causación crea el asiento con la fecha de hoy.

Si es necesario, puede realizar la revaluación de las cuentas de Cuentas por cobrar más de una vez durante el mismo período. La revaluación posterior en el mismo período ajusta los resultados de la revaluación anterior, y cada revalorización genera un lote de asientos de extorno automáticamente.

### Asiento de revaluación de Cuentas por Cobrar

Cuando se realiza una revaluación de Cuentas por cobrar, el sistema crea un lote de Contabilidad general con los resultados de la revaluación. El lote actualiza la cuenta de ganancia (o pérdida) no realizada especificada para la moneda con el monto de ganancia (o pérdida) calculada en el formulario

Como resultado del proceso de revaluación, el sistema calcula las ganancias y pérdidas no realizadas y crea un asiento de revaluación con inversión automática. Las ganancias y pérdidas no realizadas resultantes se registran en las cuentas del Libro que especifique

Usted especifica las cuentas en las que se publican las ganancias y pérdidas no realizadas en los recuadros Cuenta de ganancia no realizada y Cuenta de pérdida no realizada .