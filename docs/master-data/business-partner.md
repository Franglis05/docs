---
title: Socio del Negocio
category: Documentation
star: 9
sticky: 9
article: false
---

# Socio del Negocio

## Descripción

La ventana **Socio del Negocio** permite registrar y administrar la información de las personas naturales o jurídicas con las que la organización mantiene una relación comercial o administrativa en **Solop ERP**.

Un Socio del Negocio es un participante obligatorio en las transacciones del sistema y puede actuar como **Cliente**, **Proveedor** y/o **Empleado**. No es posible emitir transacciones de compras, ventas, nómina ni generar asientos contables sin que exista previamente un Socio del Negocio configurado.

Este registro tiene un rol determinante en los asientos contables y reportes, ya que funciona como una de las dimensiones contables principales del sistema.

---

## ¿Cuándo se utiliza?

Esta ventana se utiliza cuando es necesario:

- Registrar un nuevo cliente, proveedor o empleado.
- Actualizar información administrativa, fiscal o de contacto de un socio existente.
- Configurar parámetros comerciales, crediticios o contables asociados a un socio.
- Consultar información general del socio del negocio para operaciones administrativas.

---

## Acceso

En el menú de Solop ERP:

**Relación con Socio del Negocio → Reglas de Socios del Negocio → Socio del Negocio**

---

## Registro de Socio del Negocio

En esta ventana se cargan los datos principales del socio.  
Los campos marcados con (\*) son obligatorios.

Para crear un nuevo registro:
1. Seleccione el ícono **Registro Nuevo** en la barra de herramientas.
2. Complete los campos requeridos.
3. Guarde los cambios antes de cambiar de pestaña.

---

## Campos principales

### Organización

Define la entidad legal o subunidad a la que pertenece el socio del negocio.

- Si se selecciona `"*"`, el socio estará disponible para todas las organizaciones.
- Si se selecciona una organización específica, el registro solo estará disponible para esa organización.

> **Recomendación:** Solop ERP sugiere crear los socios con organización `"*"` para evitar duplicidad de registros e inconvenientes contables.

---

### Código

Identificador único e irrepetible del socio del negocio.

- Generalmente corresponde a un número de identificación legal (cédula, RIF, RUT, etc.).
- Si no se ingresa, el sistema genera un código numérico autoincrementable.
- Se recomienda no utilizar caracteres especiales.

---

### Socio de Negocio Padre

Permite agrupar socios dependientes bajo un socio principal.

- No es obligatorio.
- Se utiliza comúnmente para franquicias, cadenas o corporaciones.
- Facilita la generación de reportes consolidados.

---

### Nombre

Razón social o denominación legal del socio del negocio.

---

### Nombre 2

Uso variable según el tipo de socio:

- **Cliente / Proveedor:** campo opcional, usualmente para nombre comercial.
- **Empleado:** campo obligatorio, corresponde al apellido.

---

### Descripción

Campo opcional para agregar notas o información relevante del socio.

---

### Entidad Acumulada

Cuando está activo, define al socio como una entidad sumaria (Socio Padre).

---

### Estado de Crédito

Define el comportamiento del control crediticio del socio.

Opciones disponibles:
- **Sin Verificación de Crédito**
- **Crédito Correcto**
- **Crédito Verificación**
- **Crédito Retenido**
- **Crédito Detenido**

Este estado actúa junto con los campos **Saldo Actual** y **Límite de Crédito**.

---

### Saldo Actual

Campo de solo lectura que muestra el saldo vigente del socio, actualizado automáticamente.

---

### Número de Identificación

Número generado a partir del campo **Código**.  
Se utiliza en documentos fiscales como facturas y comprobantes.

---

### Exento de Impuesto en Venta

Permite omitir impuestos en órdenes de venta para este socio.

---

### Exento de Impuesto en Compra

Permite omitir impuestos en órdenes de compra para este socio.

---

### Grupo de Impuestos

Define el grupo impositivo aplicable al socio.

---

### Grupo de Socio del Negocio

Permite categorizar socios para efectos contables y comerciales.

Desde este grupo se heredan configuraciones como:
- Listas de precios de venta y compra
- Esquemas de descuento
- Porcentajes de crédito
- Parámetros contables
- Tolerancias en órdenes y facturas

---

### Otros campos informativos

Campos no obligatorios que permiten enriquecer el perfil del socio, tales como:
- DUNS
- No. de Referencia
- NAICS / SIC
- Valuación ABC
- Tipo de Cuenta
- Lenguaje
- Tipo de Industria
- Segmento
- Grupo de Ventas
- Dirección Web
- Prospecto Activo
- Valor Esperado
- Valor Total Transacciones (solo lectura)
- Costo de Adquisición
- Empleados
- Participación
- Volumen de Ventas
- Primera Venta
- Entrega Directa
- Tipo de Persona
- Logo

---

## Liga Organización

Proceso que permite asociar un socio del negocio a una organización.

Parámetros:
- **Organización Existente**
- **Tipo de Organización**
- **Límite de Acceso al Rol**

Cada organización puede estar ligada a un único socio del negocio.

---

## Pestañas según rol del Socio del Negocio

### Proveedor

Permite identificar al socio como proveedor.

- Debe tildarse el checklist **Proveedor**.
- Los campos visibles definen reglas de compra, listas de precios, términos de pago y esquemas de descuento.
- Incluye configuración de retenciones según documentos específicos.

Subpestañas:
- **Cuenta Bancaria**
- **Localización**
- **Contacto**

---

### Cliente

Permite identificar al socio como cliente.

- Debe tildarse el checklist **Cliente**.
- Los campos definen reglas de facturación, entrega, precios, descuentos, crédito y cobranzas.

Subpestañas:
- **Cuenta Bancaria**
- **Localización**
- **Contacto**

---

### Empleado

Permite identificar al socio como empleado de la organización.

- Centraliza la información necesaria para pagos, remuneraciones y gestión del personal.
- Se accede desde la pestaña **Empleado** luego de crear el socio.

---

## Creación de Socio del Negocio desde otros documentos

Es posible crear un Socio del Negocio directamente desde otras ventanas (por ejemplo, Documentos por Cobrar).

Pasos generales:
1. Hacer clic en el campo **Socio del Negocio**.
2. Seleccionar **Crear Socio**.
3. Completar los datos iniciales.
4. Registrar direcciones según corresponda.

Esta ventana puede personalizarse para mostrar solo los campos necesarios según el tipo de operación.

---

## Recomendaciones generales

- Guardar los cambios antes de cambiar de pestaña.
- Evitar duplicar socios; un mismo registro puede cumplir múltiples roles.
- Utilizar correctamente el Grupo de Socio del Negocio para garantizar coherencia contable.
- Mantener actualizada la información de contacto y localización.

Esta ventana constituye uno de los registros maestros más importantes de Solop ERP y su correcta definición impacta directamente en la operativa y los reportes del sistema.
