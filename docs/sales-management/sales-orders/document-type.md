---
title: Tipos de Documentos
category: Documentation
star: 9
sticky: 9
article: false
---

## Órdenes de Venta: Tipo documento destino y subtipo OV

Para realizar un registro de orden de venta, el primer paso es seleccionar el tipo de orden de venta (tipo documento destino).

Cada tipo de documento destino posee por defecto un subtipo OV.

Por ejemplo, el tipo orden Pos Order (e factura) tiene como subtipo OV "orden facturada automáticamente.

Al completar lla orden (en este caso) se genera la factura (no la entrega).

La OV en sí, genera diferentes documentos (al pasar al estado completo). Es una característica de las órdenes de venta.

A su vez, el sub tipo OV orden a crédito genera una factura a crédito (a un determinado plazo de pago) y crea la entrega también.

El sub tipo OV orden almacén cuando se completa, genera una entrega (no genera ni factura ni cobro).

El subtipo OV orden estandar no genera otros documentos al completar la OV. Cada área realiza su labor por separado en diferentes momentos (entrega, factura, cobro).

El subtipo OV orden prepagada genera entrega y cobro  (pero no la factura).

El subtipo OV orden punto de venta genera todos los documentos (entrega, factura y cobro). Es una opción que ya no se utiliza. Se reemplazó por la orden facturada automáticamente.