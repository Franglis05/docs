---
title: Servicios Tercerizados
category: Documentation
star: 9
sticky: 9
article: false
---

## Acciones

### Al crear nuevo Soocio del Negocio proveedor, ¿se definen en automático los datos Lista de precio compra y esquema descuento?

Pueden setearse de forma automática al crear el Proveedor, siempre y cuando esos datos de Lista de precio compra y esquema descuento se encuentren previamente definidos en el Grupo de Socio de Negocio al que corresponda.

### ¿Es posible cargar manualmente comprobantes del sistema anterior con un tipo de documento diferente al que se utiliza para emitir los nuevos documentos por cobrar?

Esto es posible definiendo un tipo de documento diferente desde el proceso Generar Factura desde línea de orden (el tipo de documento para cargar las manuales del sistema anterior es "invoice V-cita").

Si se deja vacío (el campo tipo de documento) entonces se define el tipo de documento por defecto definido en el Tipo de Orden de Venta que se esté facturando: En su caso será "Invoice", ya que es el que tiene definido el tipo de Orden de venta "Sales Order".

### Existe una ventana para poder visualizar claramente los precios de productos y actualizarlos cuando sea necesario?

Tanto para consulta de precios de producto como para actualizar precios, se cuenta con la ventana "Versión de Lista de Precio".

Desde ella es posible tener una visual completa de los productos con sus precios y gestionar cualquier cambio relacionado al importe/valor por producto.

### ¿Cómo se define la Localización de Socio del Negocio?

El configurador del sistema "UY_SET_BPLOCATION_NAME_FROM_COUNTRY" indica si el nombre de la localización de Socio Del Negocio se debe generar a partir del formato definido en el país.

En ese caso se obtiene primero la dirección/es (address1, address2, address3, address4), y luego según el formato definido en el país en el campo "Formato de impresión de dirección", se concatenan los demás datos de ciudad, región y código postal. El texto resultante será el definido en el nombre de la localización del Socio Del Negocio.

## Procesos

### ¿Existe un proceso para agilizar la creación del Socio de Negocio con su correspondiente Contrato de servico y Lista de Precio?

Esto es posible realizarlo desde el proceso "Crear Contrato y Lista de Precios", accesible desde los procesos en ventana de socio del negocio.

Este proceso crea la lista de precios de venta y la asocia al SDN en cuestión, y además si se marcó el check "Crear Contrato", crea un contrato en estado completo para dicho Socio del Negocio.

El proceso se ejecutá correctamente si se cumplen las siguientes condiciones:

* El socio del negocio tiene marcado el check de "Es Cliente"

* El socio del negocio no posee asignada lista de precio

* El socio del negocio tiene definida una localización y se marcó el check de "Crear Contrato"

* El socio del negocio tiene definido el agente comercial y se marcó el check de "Crear Contrato"

El proceso genera mensaje restrictivo si:

* El Socio del Negocio no tiene mrcado el check de "Es Cliente"

* El Socio del Negocio tiene asignada una lista de precios

* El Socio del Negocio no tiene definida una localización y se marcó el check de "Crear Contrato"

* El Socio del Negocio no tiene definida el agente comercial y se marcó el check de "Crear Contrato"