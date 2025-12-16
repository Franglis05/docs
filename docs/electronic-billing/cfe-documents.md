---
title: Comprobantes Fiscales Electrónicos
category: Documentation
star: 9
sticky: 9
article: false
---

La funcionalidad de Comprobantes Fiscales Electrónicos (CFE) permite generar documentos electrónicos desde Solop ERP, los cuales se envían automáticamente a la entidad fiscal correspondiente, siguiendo la estructura y normativa de cada país.

Este documento describe cómo crear, completar, anular y emitir notas de crédito sobre comprobantes fiscales electrónicos, así como una guía rápida para su emisión correcta.

---

## Requisitos Previos

- Contar con un socio del negocio registrado.
- El tipo de documento utilizado debe tener activadas las siguientes opciones:
  - "¿Maneja facturación electrónica?" = Sí
  - "¿Enviar después de completar?" = Sí
- Tener asignado un grupo de impuestos al socio del negocio, con tipo de CFE válido (e-ticket, e-factura, etc.).

---

## Creación CFE

### 1. Nuevo documento

1. Ingresar a la ventana **Documentos por Cobrar** o acceder desde el proceso correspondiente.
2. Seleccionar el **socio del negocio**.
3. Verificar que el **tipo de documento** tenga habilitadas las opciones:
   - “¿Maneja facturación electrónica?” = Sí
   - “¿Enviar después de completar?” = Sí
4. Seleccionar el **tipo de documento fiscal** correspondiente.

![Documento por Cobrar](/assets/img/docs/electronic-billing/elb-billing11.png)

---

### 2. Agregar líneas

Se pueden agregar manualmente o utilizar la función **Crear desde** para importar líneas desde otros documentos (como órdenes o recibos).

* Para agregar manualmente:

1. Seleccionar un **producto** y definir la **cantidad**.
2. Al guardar la línea, el sistema actualizará automáticamente los totales del documento.

---

### 3. Completar y enviar

1. Hacer clic en el botón **Completar**.
2. Si la configuración es correcta, el documento se enviará automáticamente a la entidad fiscal.

---

## Anulación de Comprobantes

- Solo se puede anular un comprobante si fue *rechazado* por la entidad fiscal.
- En ese caso, se puede marcar como *anulado* y el documento quedará liberado.

::: warning
Las facturas anuladas por el organismo fiscal deben ser anuladas manualmente en el ERP.
:::

- Si el comprobante fue *aceptado y firmado*, no se puede anular. En su lugar, se debe emitir una **nota de crédito**.

---

## Emisión Nota de Crédito

Cuando un comprobante ya fue enviado y no puede anularse, se debe emitir una nota de crédito.

Pasos:

1. Hacer una copia del documento original.
2. Cambiar el tipo de documento a **Nota de crédito**.
3. Usar la función **Crear desde** para replicar las líneas del documento original.
4. En el campo **Factura asignada**, seleccionar la factura original (obligatorio).
5. Completar el documento.

::: warning 
Si no se define la factura asignada, el sistema no permitirá completar la nota de crédito.
:::

---

## Guía Rápida: Emisión

1. Seleccionar el **socio del negocio**.
2. Verificar que tenga un grupo de impuesto con *tipo de CFE definido*.
3. Seleccionar un **tipo de documento fiscal** con:
   - Tipo de CFE válido.
   - “¿Maneja facturación electrónica?” = Sí
   - “¿Enviar después de completar?” = Sí
4. Ingresar líneas de productos.
   - Al guardar, el sistema actualiza los totales.
5. Completar el documento.
   - Se genera la numeración fiscal y se envía automáticamente a la DGI si la configuración es correcta.
6. Verificar el estado en la **Bitácora de Documento Electrónico**:
   - Envío, firma, errores, QR, URL de descarga.
7. Imprimir el comprobante:
   - Utilizar únicamente el botón **Imprimir Comprobantes Fiscales** o la URL de descarga.
8. En caso de errores o reenvíos:
   - Ejecutar la opción **Autorizar documento por cobrar** con “Enviar”.
   - Luego utilizar **Enviar factura a servicio de facturación electrónica**.

---

## Resultado Esperado

Al finalizar el procedimiento, el comprobante se emite y envía correctamente a la entidad fiscal. El estado del documento se puede verificar en la bitácora, y es posible descargar o imprimir el comprobante validado.

