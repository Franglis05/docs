---
title: Orden de Venta
category: Documentation
star: 9
sticky: 9
article: false
---

# Órdenes de Venta

## Descripción

La ventana **Órdenes de Venta** permite registrar y gestionar documentos que autorizan la venta de productos y servicios a clientes. Una orden de venta puede utilizarse como pedido, pre factura o cotización, y sirve como documento base para generar entregas, guías y facturas.

## ¿Cuándo se utiliza?

Se utiliza cuando el cliente solicita la compra de productos o servicios y es necesario registrar formalmente la operación para su posterior procesamiento (entrega y facturación).

## Acceso

Gestión de Ventas → Órdenes de Venta → Órdenes de Venta

## Campos principales

### Pestaña Orden

- **Organización**  
  Organización para la cual se registra la orden de venta.

- **Tipo de Documento Destino**  
  Define el comportamiento del documento que se está elaborando.

- **Fecha de la Orden**  
  Fecha en la que el cliente realiza la solicitud del producto o servicio.

- **Fecha Prometida**  
  Fecha comprometida para la entrega del producto o servicio.

- **Socio del Negocio**  
  Cliente al cual se le realizará la venta.

- **Socio del Negocio a Facturar**  
  Socio del negocio que será impreso en la factura.

- **Dirección del Socio del Negocio**  
  Dirección de localización del cliente.

- **Dirección Factura**  
  Dirección que se imprimirá en la factura para la entrega del producto o servicio.

- **Usuario**  
  Usuario de contacto del socio del negocio cliente.

- **Contacto Entrega Directa**  
  Usuario de contacto del socio del negocio para entregas directas.

- **Regla de Entrega**  
  Define cómo serán entregados los productos o servicios al cliente.

- **Prioridad**  
  Prioridad asignada a la orden de venta.

- **Almacén**  
  Almacén desde el cual se despacharán los productos o servicios.

- **Entrega Directa**  
  Indica que el documento será enviado directamente del vendedor al cliente.

- **Vía de Entrega**  
  Forma en que serán entregados los productos o servicios.

- **Regla de Costo de Flete**  
  Define cómo se cargan los costos de flete al cliente.

- **Regla de Facturación**  
  Define cómo serán facturados los productos o servicios.

- **Lista de Precios**  
  Lista de precios utilizada para la venta.

- **Moneda**  
  Moneda utilizada en la operación de venta.

- **Agente Comercial**  
  Vendedor o agente comercial asignado a la operación.

- **Imprimir Descuento**  
  Indica si el descuento se imprimirá en los documentos de la orden y la factura.

- **Término de Pago**  
  Condición bajo la cual el cliente realizará el pago.

- **Código de Promoción**  
  Código de promoción vigente al momento de la venta.

- **Tipo de Pago**  
  Tipo de pago utilizado en la orden de venta y la factura.

- **Centro de Costos**  
  Elemento definido para la combinación de cuentas.

- **Actividad**  
  Actividad del negocio utilizada para el costeo.

### Pestaña Línea de la Orden

- **Producto**  
  Producto o servicio a vender.

- **Descripción**  
  Descripción del producto o servicio seleccionado.

- **Cantidad**  
  Cantidad a vender del producto o servicio.

- **UM**  
  Unidad de medida utilizada para la venta.

- **Precio**  
  Precio por unidad del producto o servicio.

- **Impuesto**  
  Impuesto aplicado al producto o servicio.

- **Neto de Línea**  
  Monto neto calculado según la cantidad y el precio ingresado.

## Acciones disponibles

- **Registro Nuevo**  
  Permite crear una nueva orden de venta.

- **Guardar Cambios**  
  Guarda la información ingresada en la orden.

- **Completar**  
  Finaliza el registro de la orden de venta y habilita su procesamiento.

## Consideraciones importantes

- La orden de venta puede generar documentos posteriores como entregas, guías y facturas.
- El comportamiento del documento depende del **Tipo de Documento Destino** seleccionado.

### Validación de Inventario

- La validación de disponibilidad depende del check **Validar Disponibilidad** configurado en el tipo de documento.
- Para que la validación funcione:
  - El tipo de documento debe tener habilitado **Validar Disponibilidad**.
  - Las líneas de la orden deben tener cantidades mayores a cero.
  - Solo aplica a líneas con productos asociados.
  - El producto debe tener habilitado el check **Almacenado**.
  - El almacén utilizado es el indicado en la línea de la orden.
- Esta configuración no aplica a las órdenes de devolución.

## Ejemplo de uso

Un cliente solicita productos que se registran en una orden de venta, indicando el socio del negocio, los productos, cantidades y precios. Al completar la orden, el sistema permite continuar con el proceso de entrega y facturación.