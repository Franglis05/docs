---
title: Documento por Cobrar
category: Documentation
star: 9
sticky: 9
article: false
---

# Documentos por Cobrar

## Descripción

La ventana **Documentos por Cobrar** permite gestionar los documentos legales que representan deudas de clientes con la organización, originadas por la venta de productos o servicios. Desde esta ventana es posible visualizar, registrar y procesar facturas de cuentas por cobrar, así como notas de crédito o débito cuando corresponda.

## ¿Cuándo se utiliza?

Se utiliza cuando la organización necesita:
- Registrar una factura de venta de forma directa.
- Gestionar documentos de cuentas por cobrar asociados a clientes.
- Procesar y completar documentos legales de facturación dentro del circuito de ventas.

## Acceso

Gestión de Ventas → Facturas de Ventas → Documentos por Cobrar

## Campos principales

Los siguientes campos se utilizan en la gestión de documentos por cobrar:

- **Organización**  
  Organización para la cual se registra el documento por cobrar.  
  En general se define automáticamente según la organización con la que el usuario inicia sesión, con posibilidad de modificación.

- **Tipo de Documento Destino**  
  Define el tipo de documento a generar (por ejemplo: e-factura, e-ticket, nota de crédito).  
  Determina el comportamiento del documento.

- **Fecha de Facturación**  
  Fecha en la que se realiza la venta y la facturación del producto o servicio.

- **Fecha Contable**  
  Fecha contable asociada a la operación de venta y facturación.

- **Socio del Negocio**  
  Cliente al cual se le factura el producto o servicio.

- **Dirección del Socio del Negocio**  
  Dirección del cliente asociada al documento por cobrar.

- **Lista de Precios**  
  Lista de precios utilizada para la venta del producto o servicio.

- **Moneda**  
  Moneda utilizada en el documento.  
  Se determina en función de la lista de precios seleccionada.

- **Término de Pago**  
  Condición o plazo establecido para el pago del documento por parte del cliente.

### Pestaña Línea de la Factura

- **Producto**  
  Producto o servicio vendido al cliente.

- **Cantidad**  
  Cantidad de productos o servicios facturados.

- **UM**  
  Unidad de medida del producto o servicio facturado.

- **Precio**  
  Precio unitario del producto o servicio.

- **Impuesto**  
  Impuesto aplicado a la venta del producto o servicio.

- **Neto de Línea**  
  Resultado del cálculo del precio unitario por la cantidad ingresada.

## Acciones disponibles

- **Registro Nuevo**  
  Permite crear un nuevo documento por cobrar.

- **Guardar Cambios**  
  Guarda la información ingresada en el documento.

- **Procesar Factura**  
  Inicia el procesamiento del documento por cobrar.

- **Completar**  
  Finaliza el documento y deja registrada la factura en el sistema.

## Consideraciones importantes

- El **Tipo de Documento Destino** define el comportamiento del documento por cobrar.
- Los datos obligatorios para el registro incluyen el **Socio del Negocio** y el **Tipo de Documento Destino**.
- El documento debe contar con al menos una línea de factura para poder ser procesado y completado.

## Ejemplo de uso

Un usuario registra una factura de cuentas por cobrar para un cliente, cargando los datos generales del documento y las líneas correspondientes a los productos o servicios vendidos, y luego completa la factura para dejarla registrada en el sistema.