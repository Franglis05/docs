---
title: Devolución a Proveedor
category: Documentation
star: 9
sticky: 9
article: false
---

Este módulo permite gestionar el proceso completo de **devoluciones de productos a proveedores** dentro de Solop ERP. Abarca desde la orden de devolución hasta la generación de la nota de crédito, incluyendo el movimiento de inventario y el control administrativo del circuito.

---

## Flujo General del Proceso

1. Identificación del documento a devolver (Orden de Compra / Factura / Recepción).
2. Creación de la **Orden de Devolución (Proveedor)**.
3. Generación de la **Orden de Devolución** desde la entrega o recibo.
4. Creación de la **Devolución a Proveedores**, que genera el movimiento de ingreso a inventario.
5. Emisión de la **Nota de Crédito** asociada.

---

## Paso a Paso

### 1. Identificar la Orden de Venta

- Buscar la **Orden de Compra** correspondiente.
- Verificar que el documento esté **recepcionado y facturado al 100%**.
- Corroborar desde la pestaña de documentos relacionados las recepciones asociadas.

### 2. Acceder a la Recepción

- Navegar desde la Orden de Compra o ingresar directamente a la ventana **Recepción de Productos**.
- Identificar la recepción que será objeto de devolución.

### 3. Crear Orden de Devolución (Proveedor)

- Ir a la ventana **Orden de Devolución Proveedor**.
- Crear nuevo documento del tipo `Autorización de Devolución`.
- Completar los siguientes campos:

  - **Proveedor**: Seleccionar el proveedor correspondiente.
  - **Motivo de Devolución**: Seleccionar de la lista (ej. *Producto en mal estado*).
  - **Agente Comercial**: Completar si es requerido.

- Guardar el documento.

### 4. Generar Orden de Devolución desde Recibo

- Desde la autorización creada, ir a **Acciones** > **Crear Orden de Devolución desde Entrega/Recibo**.
- Seleccionar la **Recepción correspondiente** (por ejemplo, 283).
- Seleccionar las líneas y cantidades a devolver (puede ser **parcial o total**).
- Confirmar y guardar. Se genera una **Orden de Devolución**, con valor y precio correspondiente.

> :::note
> Esta orden de devolución **no genera aún movimiento de inventario**. Su comportamiento es opuesto a una orden de venta.
> :::

---

### 5. Registrar la Devolución de Producto

- Ir a la ventana **Devolución Proveedor** y crear nuevo.
- Completar los datos del cliente.
- Ir a **Acciones** > **Crear Devolución desde Orden**.
- Seleccionar la **Orden de Devolución** pendiente (ej. 810).
- Validar los productos y cantidades.
- Confirmar y completar. Esto genera el **movimiento de inventario**.

---

### 6. Generar la Nota de Crédito

- Ir a la ventana **Documentos por Pagar**.
- Crear nuevo documento del tipo **Nota de Crédito**.
- Ir a `Crear Desde` > seleccionar devolución relacionada (Delivery Receipt).
- Seleccionar la línea (por ejemplo, de la orden 810).
- Cargar y completar la Nota de Crédito.

> :::note
> La nota de crédito se genera por el importe original facturado de los productos devueltos.
> :::

---

## Consideraciones Finales

- ✔️ El proceso permite devoluciones parciales o totales.
- ✔️ Cada paso queda vinculado al anterior (Orden de Venta > Recepción > Devolución > Nota de Crédito).
- ✔️ Se garantiza trazabilidad completa desde la orden inicial hasta la devolución y emisión de crédito.

---

## Ventanas Involucradas

- **Orden de Compra**
- **Recepción**
- **Orden de Devolución Proveedor**
- **Devolución Proveedor**
- **Documentos por Pagar** (Nota de Crédito)
