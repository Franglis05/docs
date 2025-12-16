---
title: Emisión Comprobantes Fiscales Electrónicos
category: Documentation
star: 9
sticky: 9
article: false
---

Una vez generados los documentos por cobrar en Solop ERP, el sistema puede enviar los comprobantes fiscales electrónicos (CFE) a la entidad fiscal correspondiente. Este proceso incluye validaciones clave para garantizar la integridad fiscal y cumplir con los requisitos normativos.

---

## Verificación del Envío

Una vez completado un documento, se puede consultar su estado desde la ventana:

**Bitácora de Documento Electrónico**, donde se visualiza:

- Código QR generado
- URL de descarga
- Número fiscal asignado
- Código de seguridad
- Estado de firma y envío
- Notas u observaciones

* **"Archivo firmado correctamente"** indica aceptación por parte del organismo fiscal.

::: warning
En caso de error o rechazo, se mostrará en la sección **Notas** o **Información adicional**.
:::

---

## Numeración Fiscal

- Una vez asignado un número fiscal, **no puede reutilizarse**.
- Si el documento es **rechazado**, se pierde ese número y el siguiente disponible será utilizado.
- Esta lógica garantiza una numeración fiscal consecutiva y no duplicada.

---

## Visualización e Impresión

La representación impresa del comprobante puede obtenerse de las siguientes maneras:

- Desde el botón **"Imprimir Comprobante Fiscal"** (único habilitado).
- Desde la **URL de descarga**, que genera el PDF oficial.

::: warning
No se deben utilizar otros botones de impresión que ofrece la interfaz por defecto, ya que no están soportados para CFEs.
:::

---

## Procesamiento de Documentos

Esta sección describe cómo funciona el envío de documentos electrónicos, sus validaciones, y el uso de colas de procesamiento.

### 1. Control Previo a Envío

Antes del envío, asegurarse de:

* a. Configuración de ubicación del emisor

- El proveedor de facturación electrónica exige una *dirección registrada* para el emisor.
- Si falta, el sistema generará un error al intentar el primer envío.

* b. Tipo de documento electrónico habilitado

- Solo se enviarán documentos cuyo tipo tenga activado:
  - `¿Maneja Facturación Electrónica? = Sí`
- Documentos sin esta marca serán *omitidos automáticamente* del envío.

---

### 2. Envío Manual de Documentos

Si un documento no fue enviado automáticamente, puede reenviarse desde el proceso:

**"Enviar factura a servicios de facturación electrónica"**

Pasos:

1. Seleccionar el documento pendiente.
2. Ejecutar el proceso.

El sistema validará que:

- El documento sea electrónico.
- No haya sido enviado previamente.
- Cumpla con todos los datos fiscales requeridos.

* Si alguna validación falla, se mostrará un error como:

> `"Error: el documento no es electrónico"`

---

### 3. Cola de Procesamiento

Si la opción `¿Enviar después de completar?` está desactivada, los documentos se agregan a una **cola de procesamiento**.

* Características:

- Ejecutable en intervalos programados.
- Permite **procesamiento masivo** de facturas.
- Funciona de forma **paralela**, sin bloquear otros documentos.

Ideal para:

- Procesos en segundo plano
- Volúmenes altos de emisión

---

### 4. Configuración de la Cola

Pasos para revisar o configurar la cola:

1. Ir a la ventana **Tipo de Cola**.
2. Seleccionar la cola de **Facturación Electrónica**.

* Esta cola está configurada con procesamiento en paralelo, lo que permite mayor velocidad y eficiencia.

---

## Recomendaciones Finales

✔ Verificar y configurar la **ubicación del emisor** antes del primer envío.  
✔ Asegurarse de que el tipo de documento tenga el check de **Facturación Electrónica** activo.  
✔ Utilizar la **cola de procesamiento** para manejar grandes volúmenes.  
✔ Aprovechar las validaciones automáticas para evitar errores en producción y asegurar cumplimiento fiscal.
