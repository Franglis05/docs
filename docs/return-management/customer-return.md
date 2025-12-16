---
title: Devolución a Cliente
category: Documentation
star: 9
sticky: 9
article: false
---

Este módulo permite gestionar el proceso completo de **devoluciones de productos a clientes** dentro de Solop ERP. Abarca desde la orden de devolución hasta la generación de la nota de crédito, incluyendo el movimiento de inventario y el control administrativo del circuito.

---

## Flujo General del Proceso

1. Identificación del documento a devolver (Orden de Venta / Factura / Entrega).
2. Creación de la **Orden de Devolución (Cliente)**.
3. Generación de la **Orden de Devolución** desde la entrega o recibo.
4. Creación de la **Devolución Cliente**, que genera el movimiento de ingreso a inventario.
5. Emisión de la **Nota de Crédito** asociada.

---

## Paso a Paso

### 1. Identificar la Orden de Venta

- Buscar la **Orden de Venta** correspondiente.
- Verificar que el documento esté **entregado y facturado al 100%**.
- Corroborar desde la pestaña de documentos relacionados las entregas asociadas.

### 2. Acceder a la Entrega

- Navegar desde la Orden de Venta o ingresar directamente a la ventana **Entregas**.
- Identificar la entrega que será objeto de devolución.

### 3. Crear Orden de Devolución (Cliente)

- Ir a la ventana **Orden de Devolución Cliente**.
- Crear nuevo documento del tipo `Autorización de Devolución`.
- Completar los siguientes campos:

  - **Cliente**: Seleccionar el cliente correspondiente.
  - **Motivo de Devolución**: Seleccionar de la lista (ej. *Producto en mal estado*).
  - **Agente Comercial**: Completar si es requerido.

  ![Campo](/assets/img/docs/return-management/rem-return-image1.png)

- Guardar el documento.

### 4. Generar Orden de Devolución desde Entrega

- Desde la autorización creada, ir a **Acciones** > **Crear Orden de Devolución desde Entrega/Recibo**.
- Seleccionar la **entrega correspondiente** (por ejemplo, 283).
- Seleccionar las líneas y cantidades a devolver (puede ser **parcial o total**).
- Confirmar y guardar. Se genera una **Orden de Devolución**, con valor y precio correspondiente.

> :::note
> Esta orden de devolución **no genera aún movimiento de inventario**. Su comportamiento es opuesto a una orden de venta.
> :::

![Campo](/assets/img/docs/return-management/rem-return-image2.png)

![Campo](/assets/img/docs/return-management/rem-return-image3.png)

---

### 5. Registrar la Devolución de Producto

- Ir a la ventana **Devolución Cliente** y crear nuevo.
- Completar los datos del cliente.
- Ir a **Acciones** > **Crear Devolución desde Orden**.
- Seleccionar la **Orden de Devolución** pendiente (ej. 810).
- Validar los productos y cantidades.
- Confirmar y completar. Esto genera el **movimiento de entrada a inventario**.

![Campo](/assets/img/docs/return-management/rem-return-image4.png)

![Campo](/assets/img/docs/return-management/rem-return-image5.png)

---

### 6. Generar la Nota de Crédito

- Ir a la ventana **Documentos por Cobrar**.
- Crear nuevo documento del tipo **Nota de Crédito**.
- Ir a `Crear Desde` > seleccionar devolución relacionada (Delivery Receipt).
- Seleccionar la línea (por ejemplo, de la orden 810).
- Cargar y completar la Nota de Crédito.

> :::note
> La nota de crédito se genera por el importe original facturado de los productos devueltos.
> :::

![Campo](/assets/img/docs/return-management/rem-return-image6.png)

---

## Consideraciones Finales

- ✔️ El proceso permite devoluciones parciales o totales.
- ✔️ Cada paso queda vinculado al anterior (Orden de Venta > Entrega > Devolución > Nota de Crédito).
- ✔️ Se garantiza trazabilidad completa desde la orden inicial hasta la devolución y emisión de crédito.

---

## Ventanas Involucradas

- **Orden de Venta**
- **Entregas**
- **Orden de Devolución Cliente**
- **Devolución Cliente**
- **Documentos por Cobrar** (Nota de Crédito)
