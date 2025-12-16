---
title: Proyecto de Medios
category: Documentation
star: 9
sticky: 9
tag: 
  - Agencia
article: false
---

## Proyecto de Medios

En un Proyecto de Medios se gestionará la Inversión que un cliente quiera realizar sobre los Tipos de Medio y Medios que desee.

Sobre cada proyecto se podrá asignar Órdenes de Compra realizadas a los Medios, Órdenes de Venta (Órdenes de Facturación) a los Clientes así como también el registro de las correspondientes Facturas tanto de compra como de venta.

Las Compras a los medios realizadas para los clientes podrán ser realizadas de dos maneras, solicitando tanto la compra como la publicación en conjunto o bien se podrá realizar una Pre-Compra para luego ir consumiendo el saldo mediante Órdenes de Publicidad independientes.

La idea es que mediante el Proyecto se pueda obtener un vistazo de situación de la compra de medios solicitada por el cliente.

En cada proyecto se definirá los siguientes puntos:

**Clasificación según diferentes “Etiquetas”:** estas pueden ser Cliente, Marca del Cliente, Tipo de Trabajo, Sello, etc.

**Gerente de Proyecto:** este normalmente es el “Ejecutivo de Cuenta” que tenga el cliente pero puede cambiar en algunos proyectos.

**Generación de Órdenes de Venta:** sobre las cuales se podrá gestionar su Facturación.

**Detalle de Línea de Factura:** Opcionalmente

**Reportes:** se podrá generar diferentes Reportes financieros sobre el estado de los proyectos.

### Campos del Proyecto Manuales

Se deberán definir manualmente de forma obligatoria los siguientes campos:

* **Socio del Negocio**
* **Nombre**
* **Marca Cliente**
* **Lista de Precios:** Es según la Lista de Precios que se define la Moneda que se manejará en el Proyecto.

La moneda del Proyecto la determina la moneda que Facturará el Proveedor

*En caso que al Cliente se le deba Facturar en otra moneda, la Orden de Venta deberá ser en la misma moneda que se comprará al Proveedor, pero se podrá definir en la Orden de Venta una moneda diferente a ser Facturado junto con su Tasa de Cambio acordada.* 

### Campos del Proyecto Automáticos

Los siguientes campos, entre otros, se definirán de manera automática (igualmente se podrán modificar si se desea).

* **Moneda**
* **Agente Comercial:** El campo “Agente Comercial” en el cabezal de un Proyecto tomará de forma automática al usuario logueado en el sistema siempre que este tenga el check de “Agente comercial” en “Y”, en la Pestaña “Empleado” de la ventana “Socio de negocio”.
* **Sello Origen:** Cuando se guarda un proyecto se realiza lo siguiente:

  Según la Categoría de Proyecto se definirá el Sello Origen

correspondiente que tenga definido el Contrato del Cliente en sus “Partes del Contrato”.

Según las siguientes Categoría de Proyecto se obtendrá el sello definido para el siguiente tipo de empresa:

Categoría de Proyecto          Tipo de Empresa

Proyecto de Agencia            Agencia Creativa

Proyecto de Medios             Agencia de Medios

Proyecto RRPP                  Agencia RRPP

Proyecto de Medios Digitales Agencia de Medios Digitales

::: note
Si no se obtuvo sello de origen se lanza una excepción.
:::

* **Almacén:** El almacén en un proyecto se definirá de manera automática según el almacén que tenga definido el Cliente en la pestaña Cliente ventana Socio del Negocio.

![Proyecto de Medios](/assets/img/docs/project-management/prm-project4.png)

### Tamaño del Proyecto (Campo “Nivel de Línea”)

Un Proyecto podrá tener diferentes niveles según su complejidad o tamaño. Dentro del Nivel seleccionado, se contará con una pestaña de Líneas donde se podrá definir cada uno de los Productos que se estará manejando. Sobre estos Productos definidos se generará una Orden de Venta al Cliente y una Orden de Compra al Proveedor del Medio.

Los diferentes niveles posibles son: Proyecto, Fase y Tarea.

**Nivel PROYECTO:** No usar Nivel Proyecto para los Proyectos de Medios

**Nivel FASE:** Se utilizará cuando el Proyecto sea de Compra y Consumo (mismo momento).

**Nivel TAREA:** Se utilizará cuando el Proyecto sea de Pre-Compra o Inversión y luego su Consumo (En momentos diferentes).

![Nivel Fase](/assets/img/docs/project-management/prm-project5.png)

![Nivel Tarea](/assets/img/docs/project-management/prm-project6.png)

### Checkin de la Pauta

Luego de contar con una **“Orden de Publicidad (Compra y Consumo)”** en Estado “Completo”, la misma se deberá confirmar mediante el Checking.

El checking se puede acceder desde los Procesos definidos en el Proyecto de Medios que se estará verificando. Para ver los procesos del Proyecto se deberá oprimir el botón de proceso ubicado en la Barra de Herramientas seleccionando “Checking”.

Al realizar la búsqueda desde el SmartBrowser de Checkin, deberá seleccionar las líneas que han sido emitidas, confirmando a su vez la cantidad en cuestión de dicha emisión.

![Checking](/assets/img/docs/project-management/prm-project7.png)

### Reporte “Detalle de Almacenamiento Simple”

Se podrá confirmar el ingreso de los productos al almacén mediante el reporte de “Detalle de Almacenamiento Simple” seleccionando el Almacén en cuestión.

![Detalle de Almacenamiento Simple](/assets/img/docs/project-management/prm-project8.png)

### Proyecto de Medios Compra y Consumo

Se entiende como “Compra y Consumo” cuando se desee realizar una compra a un Medio en nombre de un Cliente y a su vez, en el mismo documento se solicita también su emisión.

* Proyecto
  * Compra y Consumo en Canal 4 (FASE): Orden de Venta (Compra y Consumo)
    * Línea con Producto a emitir
    * Línea con Producto a emitir
    * Línea con Producto a emitir

Para poder generar una Orden de Compra en nombre de un Cliente, primero se deberá generar una Orden de Venta al Cliente. A continuación se detallan los pasos a seguir para su operativa:

**Se comienza generando un Proyecto con nivel de línea “Fase”**

Una vez con el Proyecto creado se deberá crear una Fase definiendo el Proveedor a quien se realizará la compra. Se deberá generar una Fase por proveedor.

Luego de definir el Proveedor en la Fase, se deberá ir a la pestaña “Línea de la Fase” donde se deberán definir los Productos a ser Emitidos. En este caso tenemos dos opciones:

::: note
 Crear una línea por Producto: en este Caso se deberá definir en cada línea:
:::

  * Fechas Desde: Fecha obligatoria a definir a partir de cuando es la Emisión
  * Fecha Hasta: opcionalmente si desea definir un Hasta puede definirlo.
  * Descripción: Datos extra que desea aclarar del Producto.
  * Material
  * Producto
  * Precio
  * Cantidad

::: note
Crear una línea por Emisión de Producto: esta opción es más detallada definiendo una línea por Emisión y no las cantidades totales en una línea. Se deberán definir los mismos datos el punto a tantas emisiones como hayan.
:::

### Algunas ayudas aplicables:

**Creando una Línea:** Las líneas se desplegarán en formato grilla, para completarlas se deberá hacer click en el primer campo “Fecha Emisión”, para avanzar al siguiente campo podrá hacerlo con la tecla “Intro”.

**Copiar Registro:** Una vez termine de completar una línea, se podrá copiar la misma utilizando el botón de la barra de herramientas “Copiar Registro”, una nueva línea será generada con la misma información, sólo deberá modificar lo que corresponda (Fecha de Emisión, Programa, etc).

**Producto:** En cada una de las líneas se deberá definir el producto que será Emitido. Para seleccionar el producto puede hacer click en el buscador del campo, abriendo la ventana de Información del Producto. En ella podrá realizar los filtros que considere necesario para encontrar el Producto exacto a ser consumido. Dentro de los campos que puede utilizar se recomienda definir el Proveedor del mismo que debería ser el mismo a quién se está generando la Orden de Compra. A su vez, también se podrá apoyar en el campo “Medio” y “Soporte” de los productos.

Una vez definido el Proveedor y los Productos en las líneas, se deberá proceder a realizar una Orden de Venta del tipo “Orden de Venta (Compra y Consumo)” desde el botón “Generar Orden de Venta”.

Al confirmar el proceso, una Orden de Venta será generada apareciendo el número de la misma en la esquina inferior izquierda de la ventana. Para acceder a ella se podrá utilizar el botón de “Visualiza Detalle” en la Barra de Herramientas de la Ventana Proyecto.

La Orden generada también aparecerá en el campo Orden de Venta de la Fase. Para acceder a ella podrá hacer click en el campo “Orden de Venta”.

La Orden de Venta es el Documento que se Facturará al Cliente. La misma tendrá definido a su vez, en el campo “Socio del Negocio Entrega Directa” el Proveedor del Medio al cual se le generará una Orden de Compra Espejo por los Medios correspondientes.

La Orden de Venta se deberá Completar, de manera que se genere automáticamente la Orden de Compra al Proveedor del Medio.

La Orden de Compra será del Tipo “Orden de Publicidad (Compra y Consumo)” se generará en estado Borrador por lo que se deberá navegar a la misma y Completarla para terminar con el proceso.

### Representación impresa:

Desde la Ventana Orden de Compra se podrá obtener la Representación Impresa de la misma que deberá ser enviada al Proveedor del Medio.

### Checkin de la Pauta

Luego de contar con una “Orden de Publicidad (Compra y Consumo)” en Estado “Completo”, la misma se deberá confirmar mediante el Checking.

El checking se puede acceder desde los Procesos definidos en el Proyecto de Medios que se estará verificando. Para ver los procesos del Proyecto se deberá oprimir el botón de proceso ubicado en la Barra de Herramientas seleccionando “Checking”.

Al realizar la búsqueda desde el SmarBrowser de Checkin, deberá seleccionar las líneas que han sido emitidas, confirmando a su vez la cantidad en cuestión de dicha emisión.

### Compra paquete por importe

Se considera una Pre-Compra o Compra con Inversión cuando se realiza una compra a un Medio en nombre de un Cliente para que la misma pueda ser Consumida en un momento diferente a la Compra en cuestión.

El **Nivel de Línea “TAREA”** se deberá utilizar para realizar una **Pre-Compra** en Nombre de un Cliente para su posterior **Consumo**. Esto sería cuando sólo se realiza la compra en un medio de determinado *Importe de Inversión*, sin especificar los Productos que se estarán Consumiendo.

En este caso los niveles serán clasificados de la siguiente manera:

**FASE:** A Nivel de Fase se deberá definir el *Proveedor del Medio* que se realizará la Compra. En caso de ser una Pre-Compra, también se deberá definir en el Producto el correspondiente de “Inversión”. Importante seleccionar un producto con la Tasa de Impuesto que corresponda (Iva Básico o Exento).

**TAREAS:** Dentro de cada Fase se crearán las diferentes TAREAS por cada Consumo que se consumirá la Inversión en cuestión. Los Productos se deberán definir en las Líneas de Tarea, definiendo Producto, Fecha Emisión, Descripción del Programa, Cantidad y Precio.

### Pre-Compra

Se comienza generando un Proyecto con nivel de línea “Tarea”:

* En la ventana de Proyecto de Medios se deberá crear un proyecto definiendo:
  * **Cliente**
  * **Marca del Cliente**
  * **Nombre del Proyecto**
  * **Nivel de Línea:** Tarea
  * **Lista de Precios**
  * **Campos Automáticos:** Según el Cliente seleccionado se cargarán los siguientes Campos:
    * Contrato de Servicio
    * Sello
    * Sello Origen
* Término de pago
* Almacén del cliente

  
La inversión se debe definir desde una FASE del Proyecto de Medios.

En la misma, se deberá definir el Proveedor del Medio que se realizará la Compra.

Para que el sistema permita elegir un Proveedor en el campo **Socio del negocio Entrega Directa** es importante que el mismo:

* Esté creado con la Organización con la que se encuentra logueado el usuario o con Organzación (\*).
* En la ventana Socio de negocio, en su cabezal debe tener marcado el check de “activo” y en la pestaña Proveedor el check de “Proveedor”.

En el Campo de Producto se deberá definir el correspondiente de “Inversión” junto con su correspondiente Importe en el campo “Total Planeado”. Importante seleccionar un producto con la Tasa de Impuesto que corresponda (Iva Básico o Exento).

Una vez definido el Proveedor, el Producto y el importe, se deberá proceder a realizar una Orden de Venta del tipo “Orden de Venta (Inversión)” desde el botón “Generar Orden de Venta”.

Al confirmar el proceso, una Orden de Venta será generada apareciendo el número de la misma en la esquina inferior izquierda de la ventana. Para acceder a ella se podrá utilizar el botón de “Visualiza Detalle” en la Barra de Herramientas de la Ventana Proyecto.

La Orden de Venta es el Documento que se Facturará al Cliente. La misma tendrá definido a su vez, en el campo “Socio del Negocio Entrega Directa” el Proveedor del Medio al cual se le generará una Orden de Compra Espejo por los Medios correspondientes.

La Orden de Venta se deberá Completar, de manera que se genere automáticamente la Orden de Compra al Proveedor del Medio. Para Completar la Orden de Venta el sistema controlará que la misma tenga el Check de “Aprobado por Cliente” en “Y” y que tenga adjunto la aprobación en cuestión. Esta Orden de Compra se definirá en el campo “Orden Enlazada”. La Orden de Compra se generará en estado Borrador a la espera que el Departamento de Compras verifique la misma y la complete.

Desde la Orden de Compra se podrá obtener la Representación Impresa de la misma que deberá ser enviada al Proveedor del Medio.

### Consumo

Desde la tarea se deberá crear una Orden de Venta del Tipo “Orden de Venta (Consumo)” tomando los datos definidos en la misma y en sus líneas. En las Líneas de la Tarea se deberá definir los Productos a ser Consumidos, definiendo Fecha Emisión, Producto, Descripción del Programa, Cantidad y Precio.

Las líneas se desplegarán en formato grilla, para completarlas se puede ir definiendo uno a uno los campos utilizando “Intro” para pasar al siguiente campo. Una vez termine de completar una línea, se podrá copiar la misma utilizando el botón de la barra de herramientas “Copiar Registro”, una nueva línea será generada con la misma información, sólo deberá modificar lo que corresponda (Fecha de Emisión, Programa, etc).

**Producto:** en cada una de las líneas se deberá definir el producto que será Emitido. Para seleccionar el producto puede hacer click en el buscador del campo, abriendo la ventana de Información del Producto. En ella podrá realizar los filtros que considere necesario para encontrar el Producto exacto a ser consumido. Dentro de los campos que puede utilizar se recomienda definir el Proveedor del mismo que debería ser el mismo a quién se está generando la Orden de Compra. A su vez, también se podrá apoyar en el campo “Medio” y “Soporte” de los productos.

Una vez definidas todas las líneas que se desea pautar, se deberá proceder a realizar una Orden de Venta del tipo “Orden de Venta (Consumo)” desde el botón “Generar Orden de Venta”.

Al confirmar el proceso, una Orden de Venta será generada apareciendo el número de la misma en la esquina inferior izquierda de la ventana. Para acceder a ella se podrá utilizar el botón de “Visualiza Detalle” en la Barra de Herramientas de la Ventana Proyecto.

La Orden de Venta (Consumo) se deberá Completar, de manera que se genere automáticamente la Orden de Compra (Consumo) correspondiente. Una vez con la Orden de Compra (Consumo) completa, la misma podrá ser enviada al Proveedor del Medio en cuestión mediante su representación impresa.

Ambas consumirán sus Órdenes de Pre-Compra correspondientes (Orden de Venta y Orden de Compra), quedando a la espera de ser confirmados mediante el “Checking”.

### Checking

Luego de contar con una “Orden de Publicidad (Consumo)” o una “Orden de Publicidad (Compra y Consumo)” en Estado “Completo”, la misma se deberá confirmar mediante el Checking.

El checking se puede acceder de dos maneras, una opción es directo desde los Procesos definidos en el Proyecto de Medios que se estará verificando. Para ver los procesos del Proyecto se deberá oprimir el botón de proceso ubicado en la Barra de Herramientas seleccionando “Checking”. Otra opción es directo desde el proceso Checkin ubicado en el menú, en este caso se podrá filtrar según desee pudiendo ver más de un proyecto a la vez para confirmar.

Al realizar la búsqueda desde el SmarBrowser de Checkin, deberá seleccionar las líneas que han sido emitidas, confirmando a su vez la cantidad en cuestión de dicha emisión.

En caso de querer confirmar la No Emisión se deberá seleccionar la línea, definir la cantidad en 0.

En caso de que dicha Cantidad a su vez deberá Liberar Saldo de una Pre-Compra además se deberá marcar el Check de “Liberar Saldo” en Y.

Creación de un “Proyecto de Medios” donde realizará la Inversión del cliente. La idea es que dentro de un mismo Proyecto se controle lo **Ordenado con lo Facturado**. Como se manejan diferentes criterios de Facturación que de recepción de Productos a inventario, se decide manejar mediante la FASE la “*Inversión”*, y mediante la Tarea y líneas de la Tarea la *“Recepción”*.

### Compra Inventario

#### Se comienza generando un Proyecto con nivel de línea “Tarea”

* En la ventana de Proyecto de Medios se deberá crear un proyecto definiendo:
  * **Cliente**
  * **Marca del Cliente**
  * **Nombre del Proyecto**
  * **Nivel de Línea:** Tarea
  * **Lista de Precios**
  * **Campos Automáticos:** Según el Cliente seleccionado se cargarán los siguientes Campos:
    * Contrato de Servicio
    * Sello
    * Sello Origen
* Término de pago
* Almacén del cliente

### Definición del Proveedor de la Inversión:

#### En la Fase del Proyecto se deberá definir el Proveedor donde se realizará la inversión

Para que el sistema permita elegir un Proveedor en el campo **Socio del negocio Entrega Directa** es importante que el mismo:

* Esté creado con la Organización con la que se encuentra logueado el usuario o con Organización (\*).
* En la ventana Socio de negocio, en su cabezal debe tener marcado el check de “activo” y en la pestaña Proveedor el check de “Proveedor”.

### Orden de Inventario:

Desde la Tarea se crea la **Orden de Inventario** donde se definirán los Productos a comprar. El proceso de generar una Compra de Inventario deberá comenzar realizando la definición de todos los Productos que se estarán adquiriendo para consumir en el futuro dentro las líneas de una Tarea de Proyecto.

Para ello se deberá detallar cada uno de los productos que se estarán adquiriendo en “Líneas de Tarea” con el Precio acordado de los mismos. Una vez se tengan todos los Productos definidos en Líneas de Tarea, se podrá ver el TOTAL en el campo “Total Planeado” de la Tarea.

Una vez confirmado el importe se deberá generar la “Orden de Inventario” desde el Proceso “Generar Orden”. IMPORTANTE la Orden de Inventario es una orden de Sub tipo de OV “Propuesta”.

La Orden de Venta se definirá en el Campo Orden de Venta de la Tarea. Se debe navegar hacia la Orden de Venta para poder Completarla.

Al Completar la Orden de Venta se generará la Orden de Compra al Proveedor definido. Se podrá navegar a la Orden de Venta desde el campo “Orden enlazada” desde la Orden de Venta

Al completar la Orden de Compra de tipo de documento “Orden de Compra Inventario”, los Productos definidos en ella se habrán recepcionado automáticamente en el Almacén definido en el Proyecto. Ésta Almacén debería ser el Almacén definido para el Cliente por el cual se compró los productos.

### Orden de Venta y Orden de Compra a Facturar

Desde la **FASE** se deberá crear una “Orden de Venta Inversión”, ésta será realizada según el Producto genérico definido en la FASE (Ej: Inversión TV) y por el Importe Total. Este producto será el que finalmente será facturado, tanto al Cliente como por el Proveedor.

Para el caso que una Orden de Venta u Orden de Compra deba ser Facturada en diferentes “Cuotas” se deberá:

* **Producto a Facturar:** Como la facturación no se realizará producto a Producto que fue solicitado, se debe definir un Producto Genérico que será el que finalmente será facturado.
* **Descripción:** Escribir en la Descripción de la FASE cómo se desea que sea Facturado para que Administración se entere.
* **Cantidad:** Además se deberá definir en Cantidad las diferentes Cuotas que tendrá. Además en el Campo “Cantidad” de la Fase se deberá definir la Cantidad de Cuotas que se desea Facturar, ya sea por el Medio o al Cliente. Ver que como Precio Unitario se deberá visualizar el importe de cada una de las cuotas a ser Facturado.

### Consumo de Inventario

Cuando un cliente cuente con inventario previamente comprado y se quiera consumir parte del mismo, se deberá crear directamente una Orden de Venta del tipo “Orden de Pauta”. En la misma se deberá definir el *Proveedor* y el *Almacén* del Cliente definiendo “Entrega Directa” = N. En las líneas se deberá definir cada uno de los Productos que se desean emitir así como su Cantidad correspondiente. Esta Orden de Pauta una vez se confirme es la que generará la Entrega del Inventario bajándolo de stock.

* Pendiente de definir: Ver cómo se quiere gestionar el Precio en las Órdenes de Pauta.
* Esta Orden de Pauta no será facturada nunca ya que se entiende que ya se facturó mediante la Orden de Venta Inversión que se compró el Inventario.

### Conversión de Productos en Inventario

Los productos que existan en inventario podrán ser canjeados por otros productos desde la ventana de “Inventario Uso Interno” (podrá definirse el nombre que deseen). En esta ventana se podrá realizar una Conversión entre un Producto que está actualmente en inventario por otro nuevo, disminuyendo el inventario de uno y aumentando el otro. Esta Conversión se realizará sin ningún tipo de control, siendo responsabilidad del usuario controlar que dicha conversión sea según lo acordado con el Proveedor.

Contablemente el sistema actualmente Descuenta el importe en cuestión por el producto que se va, pero no está haciendo la entrada del producto que se recibe. Confirmar si se desea:

Se quiere que contabilice correctamente dando la entrada contablemente del nuevo producto. No se desea realizar ningún asiento contable por esta transacción.

### Vista de la Orden de Venta navegando desde el Proyecto

Otra opción puede ser utilizando la Navegación a Documentos Relacionados existente en todos los documentos

Tener en cuenta que la Orden de Venta que se genere siempre tendrá en su Descripción el nombre del Proyecto / Fase / Tarea desde donde se generó. Además, se definirá en la Descripción de la línea de Orden de Venta la *Descripción* que se defina en la línea del Proyecto.

### Controles en la Orden de Venta

* Aprobado por Cliente
* Archivo Adjunto

Las Órdenes de Venta cuentan con un control de Aprobación de Clientes. Para poder completar la Orden de Venta se deberá Marcar en “Y” el Check “Aprobado por Cliente” y además contar con un archivo adjunto a dicha Orden. La idea es que se adjunte la autorización que se tuvo del cliente para proceder con dicho pedido.