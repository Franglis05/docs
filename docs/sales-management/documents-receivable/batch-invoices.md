---
title: Facturas por Lote
category: Documentation
star: 9
sticky: 9
article: false
---

# Facturas por Lote

## Descripción

La ventana **Facturas por Lote** permite ejecutar el circuito de facturación a clientes de forma centralizada y eficiente, agrupando múltiples cargos o cuotas en un único proceso de generación y emisión de facturas.

La interfaz es similar a la antigua ventana de Bandeja CFE, incorporando mejoras en la visualización y el control del proceso.

## ¿Cuándo se utiliza?

Se utiliza cuando se requiere facturar de manera masiva múltiples cuotas, cargos o conceptos a uno o varios socios de negocio, evitando la generación manual de facturas individuales.

## Acceso

Gestión de Ventas → Facturas de Ventas → Facturas por Lote

## Campos principales

* El campo obligatorio a llenar es el de agente comercial.

* El campo Organización se auto completa con la Org con la cual se haya logueado el usuario (con posibilidad de modificarla).

* El campo Fecha documento se define default la fecha del día (con posibilidad de modificarla).

* El campo Moneda se define automáticamente la moneda local (puede modificarse).

### Encabezado del lote

- **Tipo de transacción**  
  Define el tipo de operación del lote.  
  Valor documentado: Venta.

- **Fecha de generación de las facturas**  
  Fecha en la que se generan las facturas incluidas en el lote.

### Líneas del lote

Cada línea representa una cuota a facturar y contiene las siguientes referencias:

- **Informe de Gasto**  
  Referencia al informe de gasto asociado.

- **Línea del Contrato**  
  Referencia a la línea del contrato que origina la cuota.

- **Actividad**  
  Actividad asociada a la cuota facturada.

- **Precio final**  
  Monto final de la cuota, con el descuento ya aplicado.

## Acciones disponibles

- **Crear desde “Informe de Gastos”**  
  Permite generar las líneas del lote a partir de cuotas existentes.

- **Generar Facturas**  
  Genera las facturas correspondientes a las líneas del lote en estado “Preparar”.

- **Imprimir Comprobante**  
  Permite imprimir el comprobante fiscal generado.

## Flujo general del proceso

### 1. Preparación del lote

Se crea el encabezado del lote definiendo:
- Tipo de transacción.
- Fecha de generación de las facturas.

Luego se ejecuta la acción **Crear desde “Informe de Gastos”**, donde el usuario:
- Selecciona la fecha de la cuota a facturar.
- Selecciona el socio del negocio a facturar.
- Define si los conceptos son recurrentes o no recurrentes mediante la opción **Auto-Servicio**.

El sistema carga automáticamente las cuotas que se encuentran en estado **Completo**, generando una línea por cada cuota.

### 2. Generación de facturas

Al ejecutar **Generar Facturas**:
- Las facturas se crean inicialmente en estado **Preparar**, como borradores.
- El sistema no actualiza automáticamente los indicadores, por lo que es necesario ejecutar un proceso manual para refrescar cantidades y totales.

Se muestra un resumen con:
- Cantidad de líneas generadas.
- Cantidad de líneas facturadas.
- Cantidad total de facturas.
- Facturas sin procesar.

Las líneas se agrupan por:
1. Responsable de pago.
2. Socio del negocio.

### 3. Visualización de facturas electrónicas

Según la información fiscal del socio del negocio:
- Si posee cédula registrada, se genera un **e-Ticket**.
- Si posee RUT, se genera una **e-Factura**.

Desde cada línea se puede visualizar:
- Estado del documento (Borrador).
- Datos del cliente.
- Precio, descuentos y referencias al contrato, informe de gasto y actividad.

### 4. Procesamiento y finalización

Una vez verificados los datos, las facturas se completan, generando el correspondiente número de **CFE (Comprobante Fiscal Electrónico)**.

El comprobante puede consultarse desde:
- Bitácora de documentos electrónicos.
- Información electrónica del documento.
- URL de acceso al comprobante.

## Gestión de errores en facturación por lote

Cuando se produce un error durante el procesamiento de un lote:
- Las facturas procesadas correctamente quedan completadas.
- Las facturas con error quedan guardadas sin procesar.

El sistema no revierte el procesamiento completo del lote.

### Comportamiento esperado

- Las facturas exitosas no se revierten aunque otras fallen.
- Las facturas con error pueden corregirse y reprocesarse de manera individual.

## Ejemplo de uso

Se genera un lote con dos líneas correspondientes a distintos diseños:
- Una línea se procesa correctamente y la factura queda en estado **Completo**.
- La otra línea presenta un error de configuración y la factura queda guardada sin procesar.

## Consideraciones importantes

- El proceso puede ejecutarse de forma masiva para múltiples cuotas y socios de negocio.
- Es recomendable revisar el estado de cada factura luego del procesamiento.
- Este comportamiento permite ahorrar tiempo al evitar rehacer el lote completo ante errores puntuales.