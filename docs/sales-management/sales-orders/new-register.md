---
title: Nuevo Registro OV
category: Documentation
star: 9
sticky: 9
article: false
---

# Nuevo Registro – Orden de Venta

## Descripción
La acción **Nuevo Registro** permite crear una nueva orden de venta en el sistema, registrando la información necesaria para autorizar la venta de productos o servicios a un cliente.

## ¿Cuándo se utiliza?
Se utiliza cuando es necesario generar una nueva orden de venta para registrar un pedido, pre factura o cotización solicitada por un cliente.

## Acceso
Gestión de Ventas → Órdenes de Venta → Órdenes de Venta  
Barra de herramientas → **Registro Nuevo**

## Paso a paso

### 1. Crear nuevo registro
Seleccionar el ícono **Registro Nuevo** en la barra de herramientas para iniciar una nueva orden de venta.

### 2. Completar datos de la pestaña Orden
Ingresar la información general de la orden:

- Seleccionar la **Organización**.
- Definir el **Tipo de Documento Destino**.
- Indicar la **Fecha de la Orden**.
- Indicar la **Fecha Prometida**.
- Seleccionar el **Socio del Negocio** cliente.
- Seleccionar el **Socio del Negocio a Facturar**.
- Definir la **Dirección del Socio del Negocio**.
- Definir la **Dirección Factura**.
- Seleccionar el **Usuario** de contacto.
- Seleccionar el **Contacto Entrega Directa**.
- Definir la **Regla de Entrega**.
- Asignar la **Prioridad** de la orden.
- Seleccionar el **Almacén**.
- Marcar **Entrega Directa** si corresponde.
- Seleccionar la **Vía de Entrega**.
- Definir la **Regla de Costo de Flete**.
- Definir la **Regla de Facturación**.
- Seleccionar la **Lista de Precios**.
- Seleccionar la **Moneda**.
- Asignar el **Agente Comercial**.
- Marcar **Imprimir Descuento** si corresponde.
- Definir el **Término de Pago**.
- Ingresar el **Código de Promoción**, si aplica.
- Seleccionar el **Tipo de Pago**.
- Seleccionar el **Centro de Costos**.
- Seleccionar la **Actividad**.

Guardar los cambios del registro.

### 3. Completar líneas de la orden
Acceder a la pestaña **Línea de la Orden** y cargar los productos o servicios:

- Seleccionar el **Producto** o servicio.
- Ingresar la **Descripción**.
- Indicar la **Cantidad**.
- Seleccionar la **UM**.
- Ingresar el **Precio**.
- Seleccionar el **Impuesto**.

El sistema calculará automáticamente el **Neto de Línea**.

### 4. Completar la orden
Regresar a la pestaña **Orden**, seleccionar la acción **Completar** y confirmar la operación.

## Resultado esperado
La orden de venta queda registrada y completada, habilitando su posterior procesamiento para entregas, guías y facturación.

## Consideraciones importantes

- El comportamiento de la orden depende del **Tipo de Documento Destino** seleccionado.
- La disponibilidad de productos puede ser validada según la configuración del tipo de documento.
- La orden debe contar con al menos una línea de producto o servicio para ser completada.

## Información faltante / a validar

- Campos obligatorios mínimos para guardar la orden.
- Comportamiento del sistema ante errores de validación.
- Posibilidad de modificar una orden luego de completada.
- Permisos o roles necesarios para crear órdenes de venta.
