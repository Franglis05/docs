---
title: Lote de Procesador de Pagos
category: Documentation
star: 9
sticky: 9
article: false
---

# Lote de Procesador de Pagos

## Descripción

La ventana **Lote de Procesador de Pagos** permite gestionar, consolidar y conciliar los cobros realizados a través de procesadores de pago externos (como Getnet, tarjetas de crédito/débito, pasarelas de pago online). Esta funcionalidad facilita el control de las comisiones, tarifas, retenciones e impuestos que los procesadores de pago descuentan del monto total cobrado, así como la conciliación bancaria de los fondos recibidos.

El sistema permite crear lotes que agrupan múltiples transacciones de cobro, calcular automáticamente las tarifas y comisiones aplicadas por el procesador, y generar los documentos contables correspondientes (cuentas por cobrar, cuentas por pagar) para reflejar correctamente el movimiento financiero.

## ¿Cuándo se utiliza?

Se utiliza cuando la empresa procesa cobros online a través de procesadores de pago externos y necesita:

Casos típicos:
- Consolidar los cobros recibidos a través de tarjetas de crédito/débito o pasarelas de pago
- Registrar y descontar las comisiones y tarifas cobradas por el procesador de pago
- Generar documentos por pagar para las comisiones del procesador
- Generar documentos por cobrar para el monto neto a recibir del procesador
- Conciliar los pagos recibidos del procesador con los estados de cuenta bancarios
- Asignar los pagos del procesador a los lotes correspondientes

## Acceso

Gestión de Saldos Pendientes → Lote de Procesador de Pagos

Tabla: `C_PaymentProcessorBatch`

## Campos principales

### Pestaña Lote de Procesador de Pagos

- **Compañía**
  Compañía a la cual pertenece el lote.

- **Organización**
  Organización específica dentro de la compañía.

- **Tipo de Documento**
  Tipo de documento "Lote de Procesador de Pagos" que define la numeración y comportamiento del lote.

- **No. del Documento**
  Número secuencial único del lote.

- **F. Documento**
  Fecha del documento del lote (generalmente la fecha de corte del procesador).

- **Moneda**
  Moneda en la que se procesan las transacciones del lote.

- **Configuración de Lote de Procesador de Pago**
  Configuración que define el procesador de pago (ej: Getnet, Mercado Pago, etc.).

- **Socio del Negocio**
  Procesador de pago o banco que procesa las transacciones (configurado como proveedor).

- **Dirección del Socio del Negocio**
  Dirección del procesador de pago.

- **Cuenta Bancaria (Transitoria)**
  Cuenta bancaria transitoria donde se registran inicialmente los cobros desde el punto de venta antes de ser transferidos a la cuenta final.

- **Cuenta Final**
  Cuenta bancaria donde el procesador deposita el monto neto (después de descontar comisiones).

- **Total del Pago**
  Suma total de todos los cobros procesados en el lote.

- **Total Descuento**
  Total de descuentos aplicados.

- **Total de Tarifa**
  Suma de todas las tarifas/comisiones cobradas por el procesador de pago.

- **Monto de Retención**
  Total de retenciones aplicadas (impuestos retenidos).

- **Total del Impuesto**
  Total de impuestos adicionales.

- **Gran Total**
  Total general del lote (Total del Pago - Total Descuento).

- **Total Abierto**
  Monto pendiente de cobro al procesador (Total del Pago - Total de Tarifa - Monto de Retención - Total del Impuesto).

- **Total Pagado**
  Monto ya recibido del procesador y asignado al lote.

- **Generar Cobro Automático**
  Indica si se debe generar automáticamente el documento por cobrar al completar el lote.

- **Carga de Tarifa Manual**
  Permite ingresar manualmente las tarifas para cada línea del lote.

- **Crear Lineas desde Estado de Cuenta**
  Permite crear automáticamente las líneas del lote desde un estado de cuenta bancario.

### Pestaña Pagos

Esta pestaña contiene las líneas individuales de cada cobro procesado que forma parte del lote.

- **Pago**
  Referencia al cobro/pago original generado desde el punto de venta o ventana de cobros.

- **Monto del Pago**
  Importe total del cobro realizado al cliente.

- **Tarifa**
  Monto de la comisión/tarifa cobrada por el procesador por esta transacción específica.

- **Retención**
  Monto de retención aplicado (si aplica).

- **Impuesto**
  Impuesto adicional sobre la transacción.

- **Monto Abierto**
  Monto neto de la transacción (Monto del Pago - Tarifa - Retención - Impuesto).

## Acciones disponibles

- **Crear Lineas desde Estado de Cuenta**
  Permite importar automáticamente las líneas del lote desde un estado de cuenta bancario de la cuenta transitoria.

- **Generar Documento por Pagar**
  Crea una factura de proveedor por el total de tarifas/comisiones que se deben al procesador de pago.

- **Generar Documento por Cobrar**
  Crea un documento por cobrar (cuenta por cobrar) por el monto neto que el procesador debe transferir a la empresa (Total Abierto).

- **Asignar Pagos**
  Permite asignar los pagos recibidos del procesador (registrados en estados de cuenta bancarios) a las líneas del lote correspondiente.

- **Completar**
  Completa el lote y genera los asientos contables correspondientes.

## Flujo del proceso

### 1. Configuración Inicial

Antes de trabajar con lotes de procesador de pagos, es necesario:
- Configurar el procesador de pago en el sistema (banco, cuenta transitoria, cuenta final)
- Definir el socio de negocio (proveedor) que representa al procesador
- Configurar el tipo de documento "Lote de Procesador de Pagos"
- Configurar el terminal de punto de venta para utilizar el procesador


### 2. Realización de Cobros

Los cobros se realizan normalmente desde el punto de venta (PDV) o la ventana de cobros:
- El cliente paga con tarjeta de crédito/débito
- El sistema registra el cobro completo en la cuenta bancaria transitoria
- Se genera un registro de pago en el sistema

### 3. Creación del Lote de Procesador de Pagos

Crear un nuevo lote ingresando:
- Socio de negocio (procesador de pago)
- Dirección y cuenta bancaria del procesador
- Cuenta bancaria transitoria (donde están los cobros)
- Cuenta final (donde el procesador depositará el neto)
- Configuración del procesador de pago

### 4. Importación de Líneas de Cobro

Utilizar la acción **"Crear Lineas desde Estado de Cuenta"** para:
- Seleccionar el estado de cuenta bancario de la cuenta transitoria
- Importar automáticamente todas las transacciones de cobro del período

El sistema crea una línea por cada cobro procesado.

### 5. Cálculo de Tarifas y Comisiones

Para cada línea del lote:
- Revisar el monto del pago (cobrado al cliente)
- Ingresar manualmente la tarifa cobrada por el procesador (si "Carga de Tarifa Manual" está activa)
- El sistema calcula automáticamente el monto abierto/neto


**Nota importante**: Actualmente no existe un cálculo automático de tarifas basado en porcentajes. Las tarifas deben ingresarse manualmente según la liquidación del procesador.

### 6. Generación de Documentos por Pagar

Ejecutar la acción **"Generar Documento por Pagar"**:
- El sistema crea una factura de proveedor por el total de tarifas
- Esta factura se asigna al socio de negocio (procesador de pago)
- Representa el costo por comisiones del servicio del procesador

### 7. Generación de Documentos por Cobrar

Ejecutar la acción **"Generar Documento por Cobrar"**:
- El sistema crea un documento por cobrar por el monto neto (Total Abierto)
- Representa el dinero que el procesador debe depositar en la cuenta final
- Se genera automáticamente una salida de la cuenta transitoria


### 8. Conciliación y Asignación de Pagos

Cuando el procesador transfiere el dinero:
- Registrar el/los pagos recibidos en la cuenta final mediante estados de cuenta bancarios
- Utilizar la acción **"Asignar Pagos"** para vincular los pagos recibidos con el lote
- El sistema actualiza el campo "Total Pagado"
- Repetir este proceso para cada transferencia recibida del procesador


**Nota**: Los procesadores pueden realizar múltiples transferencias en diferentes fechas para un mismo lote.

## Consideraciones importantes

- Verificar que todas las configuraciones del procesador de pago estén correctas antes de procesar cobros (cuenta transitoria, cuenta final, socio de negocio).
- Asegurarse de que todos los documentos estén completos antes de cerrar/completar el lote.
- Las tarifas actualmente deben ingresarse manualmente según la liquidación del procesador. No existe un cálculo automático basado en porcentajes.
- El lote puede estar relacionado con múltiples conciliaciones bancarias, ya que los procesadores suelen pagar en diferentes días o incluso meses.
- Si un cobro en el punto de venta se procesa por el procesador pero la venta no se completa en el sistema (error de sistema/red), el voucher no quedará registrado. En estos casos, actualmente no es posible agregar líneas manualmente en la pestaña Pagos.
- La relación entre pagos y lotes se almacena en la tabla `C_PPBatchLine`.
- Los cobros quedan registrados en la cuenta transitoria hasta que se completa el lote y se generan los documentos correspondientes.
- El campo "Generar Cobro Automático" permite automatizar la creación del documento por cobrar al completar el lote.

## Ejemplo de uso

### Escenario: Procesamiento de cobros con Getnet

**Contexto**: Una empresa retail procesa cobros con tarjeta a través del procesador Getnet desde su punto de venta.

**Paso 1**: Durante el día 14/12, se realizan 3 ventas con tarjeta:
- Venta 1: UYU 390
- Venta 2: UYU 530
- Venta 3: UYU 330
- **Total cobrado**: UYU 1,250

**Paso 2**: El 15/12, se crea un nuevo Lote de Procesador de Pagos:
- Socio de Negocio: "BANCO SANTANDER SA"
- Cuenta Transitoria: "Financieras"
- Cuenta Final: "Cuenta UYU"
- Configuración: "Getnet"

**Paso 3**: Se ejecuta "Crear Lineas desde Estado de Cuenta" seleccionando el estado de cuenta de la cuenta transitoria. El sistema importa las 3 transacciones.

**Paso 4**: Se ingresan las tarifas manualmente según liquidación de Getnet:
- Línea 1: Pago UYU 390, Tarifa UYU 30, Monto Abierto UYU 360
- Línea 2: Pago UYU 530, Tarifa UYU 30, Monto Abierto UYU 500
- Línea 3: Pago UYU 330, Tarifa UYU 30, Monto Abierto UYU 300
- **Total Pago**: UYU 1,250
- **Total Tarifa**: UYU 90
- **Total Abierto**: UYU 1,160

**Paso 5**: Se ejecuta "Generar Documento por Pagar":
- Se crea factura de proveedor por UYU 90 (comisiones de Getnet)

**Paso 6**: Se ejecuta "Generar Documento por Cobrar":
- Se crea cuenta por cobrar por UYU 1,160 (monto neto a recibir)
- Sale UYU 1,160 de la cuenta transitoria

**Paso 7**: Getnet realiza las transferencias en 3 fechas diferentes:
- 18/12: UYU 200
- 20/12: UYU 460
- 22/12: UYU 500

**Paso 8**: Se registran los pagos mediante estados de cuenta bancarios en la cuenta final y se asignan al lote usando "Asignar Pagos". El campo "Total Pagado" se actualiza hasta llegar a UYU 1,160.

**Resultado**: El lote queda completamente conciliado, reflejando correctamente:
- Los cobros originales (UYU 1,250)
- Las comisiones del procesador (UYU 90)
- Los fondos netos recibidos (UYU 1,160)
- Los asientos contables correspondientes

## Recursos adicionales


### Casos de soporte comunes

- **Vouchers de tarjeta que no aparecen en el lote**: Verificar que el cobro esté asociado a la cuenta transitoria correcta y que la fecha del cobro corresponda al período del lote.
- **Diferencias entre liquidación del procesador y sistema**: Revisar que todas las tarifas estén correctamente ingresadas y que no falten transacciones por importar.
- **Cobros procesados pero ventas no finalizadas**: Si el PDV procesa el pago por el procesador pero no finaliza la venta, el voucher no quedará registrado. Esto requiere análisis técnico y posiblemente ajuste manual en el procesador.
