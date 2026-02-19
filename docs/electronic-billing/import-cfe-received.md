---
title: Importación Comprobantes Fiscales Electrónicos Recibidos
category: Documentation
star: 9
sticky: 9
article: false
---

Las empresas emisoras electrónicas también pueden recibir comprobantes fiscales electrónicos (CFE) de sus proveedores. Con un sistema integrado, estos documentos pueden importarse automáticamente, optimizando tiempos y reduciendo errores manuales.

Esta guía describe el proceso de importación de CFE recibidos en Solop ERP desde InvoiCy, con control de datos y validación previa.

---

## Requisitos Previos

- Ser emisor electrónico autorizado.
- Tener acceso a la plataforma InvoiCy.
- Contar con configuración base del proveedor (Socio del Negocio, productos, cargos).

---

## 1. Carga de Datos

La carga inicial se realiza por organización. Se deben indicar los rangos de fechas o período para obtener los CFE recibidos aún no importados.

### Procedimiento:

1. Ingresar a la ventana **Importar Documentos CxC/CxP**.
2. Ejecutar la carga con fechas definidas.
3. Se mostrará un **Log de proceso**, detallando:
   - CFE cargados
   - Cantidad de líneas detectadas
   - Posibles errores

::: tip
Esta etapa genera una carga preliminar en una **tabla intermedia**, pero aún no crea documentos en el sistema.
:::

### Verificación previa:

Es posible comparar los CFE en InvoiCy para confirmar que coincidan con los detectados por el sistema.

![Importar CFE Recibidos](/assets/img/docs/electronic-billing/elb-billing1.png)

---

## 2. Control de Líneas

En la ventana **Importar Documentos CxC/CxP**, se presentan las líneas a importar tal como figuran en los CFE. Desde aquí se puede:

- Verificar la información línea por línea.
- Completar datos faltantes (productos, cargos, socios del negocio).

### Identificación del Proveedor

El sistema buscará un proveedor existente a partir del **RUT del emisor**. Si existe, se asignará automáticamente al campo **Socio del Negocio**.

---

### Asociación de líneas

#### a. Cargo por Defecto

- Útil cuando un proveedor factura siempre el mismo concepto.
- Se define un **Cargo** al Socio del Negocio.
- Se configura desde la ventana **Cargo**, en el campo “Socio del Negocio”.

#### b. Importe y líneas en borrador

- Permite importar factura con líneas descriptivas (cantidad, precio, descripción).
- La asignación de productos se realiza manualmente luego.
- Útil si el proveedor varía los conceptos facturados.

#### c. Productos definidos

- Requiere que los productos estén creados en el sistema con el **Código de Proveedor** configurado.
- Asocia líneas automáticamente por producto, cantidad y precio.

#### d. Documento por pagar vinculado a Orden de Compra

- Si el proveedor indica la **Orden de Compra** en el CFE, se puede asociar automáticamente.
- La identificación de líneas se realiza mediante coincidencia por:
  - Código de proveedor
  - Precio
  - Cantidad
  - Descripción

![Importar CFE Recibidos](/assets/img/docs/electronic-billing/elb-billing2.png)

---

## 3. Completar Datos

Desde el botón **Procesos**, seleccionar **Completar Datos de Factura recibida**.

### Procedimiento:

1. Se abrirá un **buscador inteligente** con filtros:
   - Impuesto
   - Fecha
   - Número de documento
   - Número de identificación

2. Se mostrarán las líneas con datos obligatorios faltantes (producto, cargo o socio).

3. Seleccionar cada línea y completar los datos en la parte inferior de la ventana.

---

## 4. Generación de Facturas

Una vez completada toda la información, ejecutar el proceso **Importación de Facturas**.

### Pasos:

1. Seleccionar organización y acción:
   - Preparar (estado Borrador)
   - Completar (estado Finalizado)

2. Se mostrará una ventana con el resultado:
   - Cantidad de facturas generadas
   - Total de líneas procesadas
   - Mensajes de error (si corresponde)

3. Consultar la columna **Mensaje Error Importación** para revisar problemas específicos.

> Al finalizar, se habrán generado los Documentos por Pagar en el sistema, listos para seguimiento.

![Importar CFE Recibidos](/assets/img/docs/electronic-billing/elb-billing3.png)

![Importar CFE Recibidos](/assets/img/docs/electronic-billing/elb-billing4.png)
