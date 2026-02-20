---
title: Conversión Monetaria
category: Documentation
star: 9
sticky: 9
article: false
---

Solop ERP permite definir diferentes conversiones monetarias y estas a su vez, aplicar diferentes tasas de cambio que permiten realizar la conversión de una moneda a otra para gestionar de manera efectiva las transacciones de compra/venta de la empresa u organización. El proceso de conversión monetaria se puede realizar de forma manual o automática, y es explicado de manera detallada en sus respectivos documentos.

- Conversión Manual
- Tipo de Conversión
- Tasa de Conversión desde la Ventana Moneda
- Tasa de Conversión desde la Ventana Tasa de Cambio
- Conversión Automática
- Conversión Automática por Tipo de Conversión

## Conversión Manual

La conversión manual consiste en crear en Solop ERP los tipos de conversión con los cuales va a trabajar la empresa. Esta funcionalidad permite lo siguiente:

Tasa de Conversión Diaria: Al trabajar con diferentes monedas en los procesos de compra/venta de la organización, se vuelve obligatoría la creación de las tasas de cambio diariamente en los diferentes tipos de conversión con los que trabaja dicha organización. Adicional a ello, la fecha final del rango o periodo de la tasa de cambio, siempre debe ser igual a la fecha de inicio de dicho rango o periodo.

En el caso de que el usuario intente crear una tasa de cambio con el mismo tipo de conversión y moneda utilizado previamente el mismo día, al intentar guardar el registro existirá una validación que no permitirá completar el proceso.

Vista monoregistro:

![Campo](/assets/img/docs/accounting-management/acm-accounting-image997.png)

Vista multiregistro:

![Campo](/assets/img/docs/accounting-management/acm-accounting-image9970.png)

Imagen 1. Ejemplo de Validación

Crear Tasa Recíproca: Esta funcionalidad permite que al guardar el registro sea creada de manera automática una tasa de cambio como reverso.

::: tip
Un ejemplo de este caso puede ser cuando el usuario crea una tasa de cambio de moneda **UYU** a moneda **USD** con una tasa multiplicadora 2 entonces automáticamente se creará una tasa de cambio de moneda **USD** a **UYU** con la tasa multiplicadora 0.5
:::

## Tipo de Conversión

Ubique y seleccione en el menú de Solop ERP, la carpeta **Análisis de Desempeño**, luego seleccione la carpeta **Reglas Contables**, por último seleccione la ventana **Tipo de Conversión**.

![Campo](/assets/img/docs/accounting-management/acm-accounting-image207.png)

Imagen 2. Menú de Solop ERP

Podrá visualizar la ventana **Tipo de Conversión**, con los diferentes registros que contiene dicha ventana.

Vista monoregistro:

![Campo](/assets/img/docs/accounting-management/acm-accounting-image208.png)

Vista multiregistro:

![Campo](/assets/img/docs/accounting-management/acm-accounting-image2008.png)

Imagen 3. Ventana Tipo de Conversión

Seleccione el icono **Registro Nuevo**, ubicado en la barra de herramientas de Solop ERP.

Seleccione en el campo **Organización**, la organización para la cual esta creando el registro de tipo de conversión.

Introduzca en el campo **Código**, el código correspondiente al registro de tipo de conversión que se encuentra realizando, para este caso es utilizado el código **BCU**.

Introduzca en el campo **Nombre** el nombre correspondiente al registro de tipo de conversión que se encuentra realizando, para este caso es utilizado el nombre de conversión **BCU**.

Introduzca en el campo **Descripción**, una breve descripción correspondiente al registro de tipo de conversión que se encuentra realizando.

El checklist **Activo**, indica que el registro se encuentra activo y puede ser utilizado en cualquier transacción que lo requiera.

Seleccione el checklist **Predeterminado**, para indicar como predeterminado el registro que se encuentra realizando.

::: tip
Recuerde guardar los cambios realizados seleccionando el icono **Guardar Cambios**, ubicado en la barra de herramientas de Solop ERP.
:::

#### Tasa de Conversión desde la Ventana Moneda

Ubique y seleccione en el menú de Solop ERP, la carpeta **Análisis de Desempeño**, luego seleccione la carpeta **Reglas Contables**, por último seleccione la ventana **Moneda**.

![Campo](/assets/img/docs/accounting-management/acm-accounting-image215.png)

Imagen 11. Menú de Solop ERP

Seleccione el registro de la moneda para la cual requiere registrar una tasa de conversión. Para ejemplificar el registro es utilizada la moneda **USD**.

![Campo](/assets/img/docs/accounting-management/acm-accounting-image216.png)

Imagen 12. Registro de Moneda USD en Solop ERP

Seleccione la pestaña **Tasas de Cambio** para navegar entre los diferentes registros de tasas de cambio correspondientes a la moneda **USD**.

![Campo](/assets/img/docs/accounting-management/acm-accounting-image217.png)

Imagen 13. Pestaña Tasas de Cambio de la Ventana Moneda

Seleccione el icono **Registro Nuevo** para crear un nuevo registro de tasas de cambio.

::: tip
La tasa de cambio se debe crear de dólares a pesos y de pesos a dólares.
:::

Seleccione en el campo **Moneda Hacia**, la moneda para la cual requiere convertir el dinero. Para ejemplificar el registro es utilizada la moneda **UYU**.

Seleccione en el campo **Tipo de Conversión**, el tipo de conversión a utilizar. Para este caso es utilizado el tipo de conversión **BCU**, creado anteriormente.

Seleccione en el campo **Válido Desde**, la fecha desde la cual es válida la tasa de conversión que se encuentra realizando.

Seleccione en el campo **Válido Hasta**, la fecha hasta la cual es válida la tasa de conversión que se encuentra realizando.

Introduzca en el campo **Factor de Base a Destino**, la tasa por la que serán multiplicados los montos de las transacciones donde sea utilizado el tipo de conversión seleccionado anteriormente. Para ejemplificar el registro es utilizada la tasa **40,0**.

::: tip
Recuerde guardar los cambios realizados seleccionando el icono **Guardar Cambios**, ubicado en la barra de herramientas de Solop ERP.
:::

#### Tasa de Conversión desde la Ventana Tasa de Cambio

Ubique y seleccione en el menú de Solop ERP, la carpeta **Análisis de Desempeño**, luego seleccione la carpeta **Reglas Contables**, por último seleccione la ventana **Tasa de Cambio**.

![Campo](/assets/img/docs/accounting-management/acm-accounting-image224.png)

Imagen 20. Menú de Solop ERP

Podrá visualizar la ventana **Tasa de Cambio**, con diferentes campos que permiten registrar las tasas de cambio según el tipo de conversión.

![Campo](/assets/img/docs/accounting-management/acm-accounting-image997.png)

Imagen 21. Ventana Tasa de Cambio

Seleccione el icono **Registro Nuevo**, para crear un nuevo registro de tasa de cambio según el tipo de conversión.

Seleccione en el campo **Organización**, la organización para la cual se encuentra realizando el registro de tasa de cambio.

Seleccione en el campo **Moneda**, la moneda origen de la conversión.

Seleccione en el campo **Moneda Hacia**, la moneda destino de la conversión.

Seleccione en el campo **Tipo de Conversión**, el tipo de conversion de la tasa de cambio que se encuentra registrando.

Seleccione en el campo **Válido Desde**, la fecha de inicio del periodo de validez de la tasa de cambio.

Seleccione en el campo **Válido Hasta**, la fecha final del periodo de validez de la tasa de cambio.

Introduzca en el campo **Factor de Destino a Base**, la tasa por la que serán multiplicados los montos de las transacciones donde sea utilizado el tipo de conversión seleccionado anteriormente. Para ejemplificar el registro es utilizada la tasa **40,0**.

::: tip
Recuerde guardar los cambios realizados seleccionando el icono **Guardar Cambios**, ubicado en la barra de herramientas de Solop ERP.
:::

### Tipo Conversión Spot o Documento

El tipo de conversión Spot es el que se carga de forma diaria (ya sea automáticamente por la consulta al BCU o manualmente cuando por algún motivo de conexión pudo no haberse cargado). Se utilizará esa tasa Spot diaria para las diferentes operaciones/transacciones realizadas en el dia.

El tipo conversión Documento se trata de una tasa de cambio específica para un documento en particular que sea multimoneda. Por ejemplo en un recibo de cobro multimoneda al seleccionar el tipo conversión "Documento" se habilitará un campo para ingresar la tasa manualmente y al grabar el recibo de cobro se guardará esa tasa de tipo Documento en el registro de tasa de cambio del día (como tasa tipo Documento)

## Conversión Automática

Ubique y seleccione en el menú de Solop ERP, la carpeta **Análisis de Desempeño**, luego seleccione el proceso **Consultar Tasa de Cambio al BCU**.

Podrá visualizar la ventana del proceso **Consultar Tasa de Cambio al BCU**, para ejecutar el mismo.

![Campo](/assets/img/docs/accounting-management/acm-accounting-image234.png)

Imagen 2. Ventana Consultar Tasa de Cambio al BCU

La ventana del proceso **Consultar Tasa de Cambio al BCU** contiene lo siguiente:

Campo Fecha: Permite ingresar la fecha para ejecutar la búsqueda de la tasa de cambio a actualizar (debe setearse la fecha del día anterior, en el caso de requerir tasa de cambio del 21/02, se ingresará fecha 20/02)

Este proceso es utilizado cuando por algún motivo no se realizó la carga automática de la tasa de cambio en el sistema. Al ejecutar dicho proceso busca la tasa del día ingresado y la actualiza.