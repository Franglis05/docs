---
title: Compra Directa a un Proveedor en nombre de Cliente
category: Documentation
star: 9
sticky: 9
tag: 
  - Agencia
article: false
---

Cuando el Proyecto incluya realizar una compra específica a un proveedor pero que no es necesario pasar por el proceso de generar una Solicitud de Cotización (RFQ), se podrá gestionar la misma de forma directa desde una Fase.

En este caso, los pasos a seguir serán:

Definir el Proyecto mínimo con Nivel de Línea “Fase”

En la Fase activar el check Entrega Directa

Definir un Proveedor como “Socio del Negocio de Entrega Directa”

En las Líneas de Tarea definir el Producto, precio y cantidad

Desde la Fase generar una Orden de Venta al Cliente pero Generar la Orden desde el botón de Generar Orden de Venta ubicado en la Fase.

Seleccionar Tipo de Orden “Orden de Venta con Aprobación”

Dicho Proceso generará una Orden de Venta con el Proveedor definido como Entrega Directa. Esto hará que al completarse la Orden de Venta, se genera automáticamente una Orden de Compra al Proveedor enlazada con esta Orden de Venta.

La Orden de Compra se podrá encontrar en el campo “Orden enlazada” de la Orden de Venta.

::: note
IMPORTANTE: Tener en cuenta que el Producto definido en la línea de la Orden de Venta, deberá estar definido tanto en la Lista de Precios de la Orden de Venta, como también en la Lista de Precios que el Proveedor tenga definida por defecto en su definición de Socio del Negocio. Para evitar esto podemos dejar el campo Lista de Precios de Compra del Proveedor vacío.
:::