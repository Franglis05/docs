---
title: Nuevo Registro DXC
category: Documentation
star: 9
sticky: 9
article: false
---

# Nuevo Registro – Documento por Cobrar

## Descripción

Esta guía describe el procedimiento paso a paso para registrar una **Factura de Cuentas por Cobrar** en Solop ERP, desde la creación del documento hasta su completado.

## ¿Cuándo se utiliza?

Se utiliza cuando la organización necesita emitir una factura de venta de forma directa para un cliente, sin partir de una orden de venta u otro documento previo.

## Acceso

Gestión de Ventas → Facturas de Ventas → Documentos por Cobrar

## Paso a paso para registrar una Factura

### 1. Crear un nuevo documento

Dentro de la ventana **Documentos por Cobrar**, seleccionar el icono **Registro Nuevo** ubicado en la barra de herramientas de Solop ERP.

### 2. Completar los datos generales del documento

En la pestaña principal del documento, completar los siguientes campos:

- **Organización**  
  Seleccionar la organización para la cual se registra el documento por cobrar.  
  En general se completa automáticamente según la organización con la que el usuario inició sesión.

- **Tipo de Documento Destino**  
  Seleccionar el tipo de documento a generar (por ejemplo: e-factura, e-ticket, nota de crédito).

- **Fecha de Facturación**  
  Ingresar la fecha en la que se realiza la venta y facturación del producto o servicio.

- **Fecha Contable**  
  Ingresar la fecha contable correspondiente a la operación.

- **Socio del Negocio**  
  Seleccionar el cliente al cual se le factura el producto o servicio.

- **Dirección del Socio del Negocio**  
  Seleccionar la dirección del cliente asociada al documento.

- **Lista de Precios**  
  Seleccionar la lista de precios que será utilizada para la facturación.

- **Moneda**  
  Se completa automáticamente según la lista de precios seleccionada.

- **Término de Pago**  
  Seleccionar la condición de pago acordada con el cliente.

Guardar los cambios utilizando el icono **Guardar Cambios**.

### 3. Cargar las líneas de la factura

Acceder a la pestaña **Línea de la Factura** y completar la información correspondiente a los productos o servicios facturados:

- **Producto**  
  Seleccionar el producto o servicio vendido.

- **Cantidad**  
  Ingresar la cantidad facturada.

- **UM**  
  Verificar o seleccionar la unidad de medida correspondiente.

- **Precio**  
  Visualizar el precio unitario del producto o servicio.

- **Impuesto**  
  Seleccionar el impuesto aplicable a la venta.

- **Neto de Línea**  
  El sistema calcula automáticamente el importe neto en función del precio y la cantidad ingresada.

Guardar los cambios utilizando el icono **Guardar Cambios**.

### 4. Procesar y completar la factura

Regresar a la pestaña principal **Factura** y seleccionar la opción **Procesar Factura** ubicada en la parte inferior del documento.

Seleccionar la acción **Completar** y confirmar con **OK**.

Una vez completado, el documento queda registrado como factura de cuentas por cobrar en el sistema.

## Acciones disponibles

- **Registro Nuevo**
- **Guardar Cambios**
- **Procesar Factura**
- **Completar**

## Consideraciones importantes

- El documento debe contar con al menos una línea de factura para poder ser procesado.
- El comportamiento del documento depende del **Tipo de Documento Destino** seleccionado.
- Los datos del cliente y las condiciones de pago deben estar correctamente definidos antes de completar la factura.