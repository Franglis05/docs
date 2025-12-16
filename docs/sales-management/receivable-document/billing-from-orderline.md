---
title: Facturación desde línea de Orden de Venta
category: Documentation
star: 9
sticky: 9
article: false
---

### Generar Factura desde Línea de Orden de Venta

Ubique y seleccione en el menú de Solop ERP, la carpeta **Gestión de Ventas**, luego seleccione la carpeta **Facturas de Ventas**, por último seleccione la ventana **Genera Factura desde Líneas de la Orden**.

![Campo](/assets/img/docs/sales-management/sam-sales-image237.png)

Imagen 1. Menú de Solop ERP

Las órdenes de venta generadas en el sistema pueden ser facturadas de manera ágil y masiva utilizando el proceso **“Generar Factura desde Línea de Orden”.**

![Generar OV desde Cuota de Contrato](/assets/img/docs/sales-management/sam-agency3.png)

#### Precondiciones

Para poder facturar una Orden de Venta, esta tiene que estar

* Estado: Completo
* Con el check “Permite Facturar” = SI
* Regla de Facturación: Inmediata

En este proceso se podrá aplicar el filtro que desee para encontrar aquellas líneas de ordenes que cumplan con dichas condiciones.

Dentro de los filtros a definir podemos encontrar:

Seleccione en el campo **Agente Comercial**, el agente comercial por el cual se va a filtrar la búsqueda.

Seleccione en el campo **Fecha de la Orden**, la fecha de orden por la cual se va a filtrar la búsqueda.

Seleccione en el campo **Fecha Prometida**, la fecha prometida por la cual se va a filtrar la búsqueda.

Seleccione en el campo **Socio del Negocio**, el socio del negocio por el cual se va a filtrar la búsqueda.

Seleccione en el campo **Producto**, el producto por cual se va a filtrar la búsqueda.

La selección del producto puede realizarce ingresando en el campo **Producto**, el **Código** del producto requerido. De igual manera, se puede realizar la búsqueda ingresando el **Código de Barra** o **UPC/EAN** en lugar del código del producto.

#### Generar Factura

Y comenzaremos la búsqueda, a continuación obtendremos las líneas de Orden de Venta que cumplan con la condición.

Procederemos a marcar el check que esté como primer columna para todas las líneas que se deseen facturar.

En la parte inferior de esta ventana veremos distintas opciones utilizadas al momento de generar la factura:

**Fecha de Facturación:** (Obligatorio) Fecha de facturación del Documento por Cobrar generado.

**Acción en el Documento:**

* **Preparar:** Si desea ver la Factura antes de completarla puede seleccionar la opción “Preparar” de manera de que se genere el documento primero en estado “En Proceso” y así poder verificar que todo esté correctamente definido. En este caso al generar el proceso se creará la factura con un Nro de Borrador “DR-2222” y podrá acceder a la misma tanto desde el proyecto u Orden desde donde se generó, cómo también buscando en la ventana “Documentos por Cobrar” según el Nro de borrador presentado abajo a la izquieda del Proceso.
* **Completar:** Si uno está seguro de la información que estará facturando también puede seleccionar la acción “Completar” de manera de que se completen automáticamente las facturas al correr el proceso.

**Organización de la Transacción:** Es la organización con la que se está logeado, necesario cuando el documento pasa a estado completo, debido a que no se pueden realizar envíos a DGI de un documento con una organización que no es con la que se está logueado.

**Criterio de Agrupación:** Según el Criterio de Agrupación definido es la forma en que el sistema agrupará las líneas de órdenes en una Factura, estas puede ser por:

* **Socio del Negocio:** Generará una Factura con todas las líneas de Orden de por cada Socio del Negocio diferente.
* **Contrato:** Generará una factura por cada Contrato establecido en las Órdenes de Venta, agrupará en esa factura todas las Órdenes que pertenezcan al mismo contrato.
* **Proyecto:** Si la línea tiene definido el Proyecto utilizará esta referencia y en caso de no tenerlo establecido tomará el de su respectiva orden (puede ser que en una misma agrupación algunas líneas tengan Proyecto relacionado y a la vez otras que se tenga que obtener de su respectivo Cabezal), Siguiendo este criterio se generará un Documentos por Cobrar por proyecto diferente.
* **Orden:** La agrupación que agrupa menos registros, se generará cada factura agrupando líneas de Orden por su respectivo cabezal.
* **Impuesto:** Agrupará por Impuesto definido en cada Línea de Orden seleccionada. Se generará una factura por tipo de impuesto encontrado. El criterio de agrupación no es por % (Ej: 22%, 10% o 0%), sino por diferente Tipo de Impuesto.
* **Orden de Compra Cliente:** Si se selecciona este Criterio de Facturación se generará una Factura por cada Número de la Orden de Compra Cliente que se encuentre en todas las líneas seleccionadas. Este criterio de agrupación incluye además la clasificación según diferentes clientes.

Seleccione las líneas de la orden desde las cuales requiere que sea generada la factura.

![Ventana Selección](/assets/img/docs/sales-management/sam-agency4.png)

![Campo](/assets/img/docs/sales-management/sam-sales-image2450.png)

Seleccione en el campo **Fecha de Facturación**, la fecha en la cual se esta realizando la facturación.

Podrá visualizar que el checklist **Consolidado en un Documento**, se encuentra tildado por defecto.

Seleccione en el campo **Organización de la Trans**, la organización para la cual esta generando la factura.

Seleccione en el campo **Acción en el Documento**, la acción con la cual se generará la factura.

Seleccione el tipo de documento a generar en el campo **Tipo de Documento Destino**, la selección de este define el comportamiento del documento que se esta elaborando, dicho comportamiento se encuentra explicado en el documento Tipo de Documento elaborado por Solop ERP.

Seleccione el checklist **Agregar Línea de Referencia en Factura**, para que las líneas de referencia sean agregadas a la factura.

Seleccione la opción **OK**, para generar el documento en base a lo seleccionado en los campos anteriormente explicados.

Podrá visualizar en histórico de Procesos, el resultado del proceso realizado anteriormente.

![Campo](/assets/img/docs/sales-management/sam-sales-image253.png)

Imagen 17. Resultado del Proceso Realizado

#### **Criterio de Facturación (definición de Líneas de Factura)**

El **Criterio de Facturación** permite generar líneas más resumidas de la información que se está Facturando, adaptando así según la necesidad de cliente, definiendo en ellas la información exacta que el cliente desea recibir en cada “Concepto de Facturación”.

Debido a que el ERP puede tener una definición muy detallada de las “líneas de las órdenes” presentando en ellas un concepto de **Servicios**, **Cantidades** y **Precios** que si bien puede ser de gran utilidad para la gestión interna y el control de sus Costos, en ciertas ocasiones a los clientes no les interesa contar con tal detalle.

De esta manera, el **Criterio de Facturación** que tendrá cada Factura será criterio que se va a utilizar para generar las líneas que se detallarán en el CFE (e-Factura o e-Ticket).

### Facturación de Honorarios en Línea independiente

El Criterio de Facturación aplicará siempre para las líneas de “Inversión” del cliente, agrupando según el criterio seleccionado. Esto quiere decir que el criterio nunca aplicará la agrupación para aquellas líneas que correspondan a Honorarios Variables calculados en un Proyecto o Fase de Proyecto, estos siempre irán en una línea aparte detallando que son Honorarios.

**Facturar en moneda distinta con la que se generó el Proyecto:**

Si se desea facturar en una moneda distinta con la que se generó el Proyecto podremos cambiar la misma en la Orden de Venta indicando la correspondiente tasa de cambio, (en el caso que la misma se encuentre en estado Borrador).

En el caso que las Ordenes de venta estén Completas se deberán anular y generar de nuevo, ya que si se reactivan se tendrán que anular la Ordenes de Venta Honorarios que se generen.

#### **Otros Criterios**

Además de los criterios definidos manualmente, siempre se agrupará una factura teniendo en cuenta que deben ser:

* Para un mismo Socio de Negocio
* Una misma localización para ese Socio de Negocio (Su dirección de facturación seleccionada)
* Misma Moneda: Tener en cuenta que es la moneda a Facturar de la Orden de Venta, por si la misma hace un cruzamiento de monedas.

Estos son requerimientos obligatorios por la naturaleza del CFE.

Nota: En el caso que se defina la opción para Completar el documento se ejecutará automáticamente el proceso Generar líneas de CFE.

#### Formato Tradicional

Para la facturación de artículos o servicios tradicionales, una línea de Orden de Venta será facturado en una línea de Factura, detallando lo mismo que se define en la línea de la orden de vetna en la línea de cada factura (Producto, Precio, Cantidad, Descripción).

Reglas: 
* Factración inmediata
* Facturación de lo entregado
* Permite Facturar en OV (opcional)

### Generar Líneas de CFE

En vista a que las líneas del Documento por Cobrar no siempre se corresponden con las líneas a enviar en el CFE e imprimir en la representación impresa, además de disponer en esta venta a de las líneas del documento (la pestaña convencional), se ha agregado una pestaña donde figuran las líneas que deberán enviarse en el CFE.

A grandes rasgos es la misma información que las líneas convencionales del Documento por Cobrar solo que en un estado más resumido.

**Precondición:** Para generar o Modificar las líneas CFE, la factura no puede estar completa porque en este caso ya estaría enviada a DGI y no tendría sentido realizar modificaciones sobre sus respectivas líneas.

**Observación:** No aplica para Resguardos

En el cabezal del Documento por Cobrar en la sección Facturación hay un campo llamado **“Criterio de Facturación”**, este campo indica dentro de este documento cómo deben agruparse sus respectivas líneas (en orden jerárquico).

* Factura: Realizará solo una línea agrupando todas las líneas de este documento: Descripción de línea queda vacío, deberá completarse manualmente
* Contrato: Descripción de línea: (Línea Factura) -> Proyecto -> Contrato.Nombre (Ver Nota 1)
* Proyecto: Descripción de línea: (Línea Factura) -> Descripción del Proyecto (Ver Nota 1)
* Fase de Proyecto: Descripción de línea: (Línea Factura) -> Descripción de Fase (Ver Nota 2)
* Línea: Descripción de línea: (Línea Factura) -> Si tengo Producto utilizo su nombre y descripción, Si no tengo Producto pero si Cargo utilizo Nombre y Descripción del Cargo. Si no tengo ninguno retornará un error.

::: note
Siempre que para todas las líneas de Factura tenga el mismo proyecto, en caso contrario quedará vacío
:::

:::note
Siempre que para todas las líneas de Factura tenga la misma fase de proyecto, en caso contrario quedará vacío
:::

### Proceso automático

El Criterio que se definirá en cada factura será el que cada cliente tenga definido en su ficha, pudiendo ser por Línea (normal), por Proyecto, por Fase de Proyecto o por Factura. .

Al utilizar como criterio “Proyecto”, el sistema agrupará en una línea a todas las líneas del Proyecto y definirá la descripción de la misma según el campo “Detalle Factura” ubicado en el Proyecto en cuestión.

::: note
Siempre se agrupan las líneas que no sean Honorarios ya que éstos van en otra línea a parte.
:::

Si utilizamos como criterio “Fase del proyecto”, el sistema agrupará todas las líneas de una fase en una línea, por lo que la factura tendrá tantas líneas de CFE como fases se estén facturando. En la descripción de cada línea se obtendrá según el campo “Detalle Factura” ubicado en cada Fase del Proyecto en cuestión.

Este proceso se puede realizar de forma automática o manual.

### **Configuración del Socio del Negocio**

#### **Criterio de Líneas en Factura**

En cada Socio del Negocio se podrá pre configurar el criterio de facturación que se desee. Esto se debe definir en la pestaña Cliente de la ventana Socio del Negocio en el campo Criterio de Facturación.

![Socio del Negocio](/assets/img/docs/sales-management/sam-agency7.png)

### Facturación por Proyecto

Al facturar por Proyecto el sistema generará una línea por todas las líneas que posea el Proyecto con la descripción del mismo, la cual obtiene del campo “Detalle en Factura” del cabezal del Proyecto.

En la ventana Socio del Negocio, pestaña Cliente, en el campo “Criterio de Facturación” se puede indicar “Proyecto”, para este Socio de negocio. De esta forma se puede automatizar este procedimiento ya que la factura tomará de forma automática este dato.

Luego, mediante la ventana Generar factura desde línea de Orden, se procederá a facturar buscando entre las diferentes líneas que tengan las Órdenes de Venta en estado Completo.

En la parte inferior de esta ventana veremos distintas opciones utilizadas al momento de generar la factura.

* Fecha de Facturación: (Obligatorio)
* Acción en el Documento: (Preparar, completar)
* Organización de la Trans.
* Criterio de Agrupación: Es el criterio para agrupar las líneas de orden ya sea por Socio de negocio, Contrato, Proyecto, Orden , Impuesto, POReference, Adicionales).

::: note
Tener en cuenta que el “Criterio de Agrupación” y el “Criterio de Facturación” NO son lo mismo.
:::

Luego seleccionaremos el botón de OK y se generará el Documento por cobrar correspondiente.

Al mismo podemos acceder desde el ícono de documentos relacionados desde el cabezal de la orden de venta.

Este factura tendrá definido en el cabezal de la misma, en la región de Facturación, el correspondiente Criterio de Facturación elegido.

Si elige no hacerse este procedimiento de forma automática lo podremos hacer manualmente.

Para realizarlo seleccionaremos la opción “Proyecto” en el campo Criterio de Facturación de la factura y a continuación correremos el proceso “Generar líneas de factura para CFE” utilizando el ícono de la tuerca.

Generará también en la pestaña Línea de la factura CFE una línea cuya Descripción tendrá definida lo mismo que se definió en el campo “Detalle en Factura” en el cabezal del Proyecto.

**Siempre se agrupan las líneas que no sean Honorarios ya que éstos van en otra línea a parte.**

### **Facturación por Fase**

Al facturar por Fase el sistema generará una línea agrupándolas por Fase del Proyecto con la descripción de las mismas, las cuales obtiene del campo “Detalle en Factura” de las fases del Proyecto.

En la ventana Socio del Negocio, pestaña Cliente, en el campo Criterio de Facturación se puede indicar “Fase de Proyecto”, para este Socio de negocio.

De esta forma se puede automatizar este procedimiento ya que la factura tomará de forma automática este dato.

Luego, mediante la ventana Generar factura desde línea de Orden, se procederá a facturar buscando entre las diferentes líneas que tengan las Órdenes de Venta en estado Completo.

Podremos acceder al Documento por cobrar desde el ícono de documentos relacionados desde el cabezal de la orden de venta.

Este factura tendrá definido en el cabezal de la misma, en la región de Facturación, el correspondiente Criterio de Facturación elegido.

Si elige no hacerse este procedimiento de forma automática podremos hacerlo manualmente.

Para realizarlo seleccionaremos la opción “Proyecto” en el campo Criterio de Facturación de la factura y a continuación correremos el proceso “Generar líneas de factura para CFE” utilizando el ícono de la tuerca.

Generará también en la pestaña Línea de la factura CFE la cantidad de líneas según la cantidad de fases que tenga el Proyecto.

Estas líneas tendrán definidas en el campo “Descripción” lo mismo que se definió en el campo “Detalle en Factura” a las fases del Proyecto.

**Siempre se agrupan las líneas que no sean Honorarios ya que éstos van en otra línea a parte.**

#### Facturar al Cliente en moneda diferente al Costo

En caso que al Cliente se le deba Facturar en otra moneda, la Orden de Venta deberá ser en la misma moneda que se comprará al Proveedor, pero se podrá definir en la Orden de Venta una moneda diferente a ser Facturado junto con su Tasa de Cambio acordada.

En caso de querer definir la Tasa de conversión luego de completar la Orden o modificar la misma luego de completarla se podrá hacer desde el proceso.

### Proceso Manual

Si para alguna factura en especial se desea utilizar un Criterio de Facturación diferente al que tiene definido el Cliente por defecto, se podrá generar el mismo desde el cabezal de la factura.

Si se desea realizar el proceso de forma manual se deben seguir los siguientes pasos luego de generar la factura:

Elegir en el campo “Criterio de Facturación” ubicado en la Factura el Nuevo Criterio que se desee aplicar.

![Criterio de Facturación](/assets/img/docs/sales-management/sam-agency5.png)

Luego procederemos a correr el proceso “Generar líneas de factura para CFE”, seleccionando la opción desde los Procesos asociados a la Factura.

![Criterio de Facturación](/assets/img/docs/sales-management/sam-agency6.png)