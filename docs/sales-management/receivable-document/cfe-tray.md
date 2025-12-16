---
title: Bandeja CFE
category: Documentation
star: 9
sticky: 9
article: false
---

## Documentos CFE de conceptos Recurrentes y no Recurrentes

La ventana "Bandeja CFE" audita todas la transacciones respecto al proceso de facturación electrónica.
Se deberán primero importar todos los Conceptos a Facturar (informes de gasto) que se desean facturar para luego generar el proceso de facturación masivamente.

La Bandeja CFE permite realizar la Facturación Electrónica de servicios en cuotas Recurrentes y no Recurrentes. De esta forma es posible generar las cuotas creadas desde los contratos.

Se inicia generando un registro de Bandeja CFE ingresando un nombre (y descripción opcional).
Al grabar el registro se habilita la generación masiva de facturas (documentos por cobrar) en tres pasos y a partir de los conceptos a facturar previamente creados.

**Bandeja CFE**

![Bandeja CFE](/assets/img/docs/education-management/edum-image10.png)

### Primer paso: Seleccionar Conceptos a Facturar 

Desde esta opción se abre una ventana emergente en la cual se pueden elegir los filtros con el objeto de agrupar aquellos conceptos a facturar que deseamos facturar masivamente (y se vincularán al registro de Bandeja CFE creado).
Posee filtros tales como Socio del Negocio, Socio del Negocio a Facturar, Fecha del concepto, lista de precios, etc, para acotar la búsqueda de conceptos que deseemos facturar.

**Filtros Seleccionar Conceptos a Faturar**

![Filtros](/assets/img/docs/education-management/edum-image11.png)

Parámetros

![Selección](/assets/img/docs/sales-management/sam-sales-image515.png)

Seleccionar Conceptos

### Segundo paso: Generar Facturas desde Conceptos 

Luego de haber seleccionado los conceptos, podemos verificar en la solapa Conceptos a facturar que se hayan vinculado todos los conceptos deseados **(también se actualizará el número de Total Conceptos a Facturar de Solapa Principal)**.

![Solapa Conceptos a Facturar](/assets/img/docs/sales-management/sam-sales-image517.png)

Solapa Conceptos a Facturar

Posteriormente al elegir la opción de Generar Facturas desde Conceptos se abrirá una ventana emergente en la cual nos indicará en qué estado se crearán los documentos por cobrar (siempre definido como en borrador o en proceso). 

![Generar Facturas](/assets/img/docs/sales-management/sam-sales-image516.png)

Generar Facturas

### Tercer paso: Completar Facturas Generadas 

La instancia anterior genera los documentos por cobrar y permite verificarlos en la solapa Facturas **(también se actualizará el número de Total CFE Generados de Solapa Principal)**.

![Solapa Facturas](/assets/img/docs/sales-management/sam-sales-image518.png)

Solapa Facturas

Si todos sus datos están correctos podemos seleccionar Completar Facturas Generadas lo cual cambiará a estado Completo en forma masiva a todas las facturas generadas.



::: note
Los Tipo de Documento de CFE se asignan automáticamente según el tipo de Documento de cada Socio del Negocio:
RUT: Tipo de documento e-factura
Cédula: Tipo de documento e-ticket
:::