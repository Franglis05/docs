---
title: Configuración Comprobantes Fiscales Electrónicos
category: Documentation
star: 9
sticky: 9
article: false
---

El circuito de facturación electrónica requiere configurar correctamente distintos elementos del sistema para permitir la emisión y el envío exitoso de comprobantes fiscales electrónicos (CFE) a la entidad fiscal correspondiente.

Este documento detalla la configuración previa necesaria en el ERP antes de emitir comprobantes fiscales.

---

## Requisitos Previos

Antes de generar un comprobante fiscal electrónico, se deben cumplir las siguientes condiciones:

- Definir correctamente un **socio del negocio** válido.
- Asociar al socio un **grupo de impuestos** con tipo de CFE adecuado.
- Configurar el **tipo de documento fiscal** con los parámetros necesarios.

---

## Definición de Entidades 

### 1. Socio del negocio

Antes de emitir cualquier documento electrónico, es indispensable seleccionar un **socio del negocio** válido (cliente).  
*Ejemplo*: Casa Gutiérrez.

#### Grupo de impuestos

El **grupo de impuestos** asociado al socio del negocio define el **tipo de documento fiscal electrónico** que se utilizará en el envío a la entidad fiscal.

* Ejemplos comunes:

- Cédula / DNI / Pasaporte / Otros → *e-Ticket*
- Empresas u organizaciones → *e-Factura*

* Consideraciones:

- El grupo de impuestos debe tener definidos los tipos de CFE válidos.
- Si no se asigna un grupo de impuestos válido al socio, el sistema no podrá completar ni enviar correctamente el documento.

---

### 2. Tipo documento fiscal

Cada tipo de documento fiscal que se utilice para generar un CFE (facturas, notas de crédito, etc.) debe cumplir con la siguiente configuración:

- Tener definido un **tipo de CFE válido**.
- Tener activada la opción **¿Maneja facturación electrónica? = Sí**.
- Tener activada la opción **¿Enviar después de completar? = Sí**.

---

::: warning
Importante: Solo debe existir un tipo de documento fiscal por instancia. No se deben definir diferentes tipos por organización.
:::