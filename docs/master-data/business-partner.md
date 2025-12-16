---
title: Socio del Negocio
category: Documentation
star: 9
sticky: 9
article: false
---

El socio del negocio generalmente es un sujeto jurídico o natural con el que la organización establece una alianza temporal o permanente a fin de obtener un beneficio común.

En Solop ERP no es la excepción, en este sentido, es un participante obligatorio en una transacción administrativa, este puede actuar como cliente, proveedor y empleado, es decir, no existe una transacción de egreso (Compras) o ingreso (Ventas) sin la previa definición del proveedor o cliente (Socio del Negocio), no existe una nómina sin un empleado (Socio del Negocio), en otras palabras, es obligatorio la previa configuración de esta entidad en Solop ERP para emitir transacciones administrativas y contables.

Este registro tiene un rol determinante en los asientos contables generados en Solop ERP, desempeñándose como una de las dimensiones contables más relevantes, permitiendo agrupar la información de forma eficiente para facilitar el control de aquello que deseamos cuantificar, por tal motivo, la correcta definición determinará los resultados en los asientos y reportes contables de los que disponen nuestros clientes, cabe considerar, que estos valores son heredados de forma predeterminada desde el grupo de socio de negocio seleccionado en este registro, no obstante, el usuario tiene la opción de modificar la configuración contable para casos excepcionales.

En esta ocasión **Solop ERP** pretende ofrecerle una guía fácil para la definición básica de un socio de negocio en Solop ERP, dentro de este orden de ideas, es importante seguir paso a paso cada procedimiento, de ello dependerá el éxito de los registros resultantes.

- Registro de Socio del Negocio
  - Proveedor
  - Cliente
  - Empleado

## Registro de Socio del Negocio

En el menú de Solop ERP, ubique y seleccione la carpeta **Relación con Socio del Negocio**, luego seleccione la carpeta **Reglas de Socios del Negocio** y finalmente seleccione la ventana **Socio del Negocio**.

![Menú de Solop ERP](/assets/img/docs/master-data/mad-master-menu1.png)

Imagen 1. Menú de Solop ERP

En esta ventana se registran los datos principales que la empresa requiere del socio del negocio cliente. Cada uno de los campos con el símbolo (\*) son obligatorios para el registro.

A continuación visualizará la ventana **Socio del Negocio**, dónde debe seleccionar el icono de **Registro Nuevo** que se encuentra ubicado en la barra de herramientas de Solop ERP.

![Ventana Principal Socio del Negocio](/assets/img/docs/master-data/mad-master-window1.png)

Imagen 2. Ventana Principal Socio del Negocio

Proceda al llenado de los campos necesarios que a continuación se detallan.

Seleccione la organización en el campo **Organización**.

La organización le permite definir la entidad legal ó una sub-unidad a la cual pertenece el socio de negocio, si la organización es "*", este estará disponible para todas las organizaciones al procesar documentos y transacciones, pero si por el contrario, ha seleccionado una organización diferente, este registro únicamente estará disponible para la organización seleccionada.

Generalmente los **Socios de Negocios** son registros compartidos entre entidades organizacionales, por esta razón **Solop ERP** recomienda la creación con organización "*" para evitar duplicidad e inconvenientes contables, de esta forma garantizamos la homogeneidad de los datos maestros.

Introduzca el código de socio del negocio en el campo **Código**.

El código es un dato único e irrepetible que protege la entrada de los registros, evitando la duplicidad de los mismos, generalmente se refiere al número de identificación que acredite la identidad de una persona natural una entidad jurídica, por ejemplo, una cédula de identidad o un RIF.

Si no es ingresado un dato en este campo Solop ERP genera un dato de tipo numérico autoincrementable.

Se recomienda no ingresar caracteres especiales como puntos, guiones u otros que alteren el registro en este campo.

Seleccione el socio de negocio padre en el campo **Socio de Negocio Padre**.

El socio de negocio padre no es un campo obligatorio, sin embargo, es un campo que permite la agrupación de sub-entidades dependientes (socios de negocios hijos) de un socio de negocio, para explicarlo mejor veamos el siguiente ejemplo:

Imaginemos un proveedor de tipo cadena cuyo nombre es **Cadena Única C.A**, esta tendrá dos tiendas físicas, **Cadena Unica Centro C.A** y **Cadena Única Oriente C.A** respectivamente. Para este caso el **Socio de Negocio Padre** es **Cadena Única C.A**,quedando agrupado de forma que las dos tiendas serán hijas de **Cadena Única C.A**, de esta forma al emitir reportes financieros podríamos generarlos desde el Socio de Negocio Padre (**Cadena Única C.A**), agrupando todos los saldos de las tiendas por el padre ó podría generar los reportes únicamente por tienda.

Generalmente esta opción es utilizada para franquicias, cadenas o corporaciones.

Introduzca el nombre del socio del negocio en el campo **Nombre**.

El nombre se refiere a la razón social, siendo esta el nombre ó la denominación con la que está registrado en los documentos legales, el nombre es utilizado a nivel administrativo, formal y jurídico.

Introduzca el nombre 2 del socio del negocio en el campo **Nombre 2**.

El nombre 2 varía su uso dependiendo de la naturaleza del socio del negocio (Cliente, Proveedor o Empleado), si es un cliente o un proveedor es opcional, y generalmente se utiliza para colocar la denominación comercial, por el contrario, si es un empleado es obligatorio, siendo este campo correspondiente al apellido, el mismo será impreso en los reportes administrativos y jurídicos.

Introduzca una breve descripción referente al socio del negocio cliente en el campo **Descripción**.

La descripción no es un campo obligatorio,sin embargo, le permite dejar descripciones o notas de interés para el registro.

Seleccione el checklist **Entidad Acumulada**.

Entidad acumulada no es un campo obligatorio, sin embargo, le permite definir al socio del negocio como entidad sumaria, lo que significa que si el socio de negocio tiene este check activo será un **Socio de Negocio Padre**.

Seleccione en el campo **Estado de Crédito**.

El estado del crédito no es un campo obligatorio, sin embargo, le permite definir el comportamiento para la gestión del crédito del socio de negocio, actúa conjuntamente con el campo **Saldo Actual** y **Límite de Crédito** ubicado en la pestaña **Cliente**, este puede variar entre las siguiente opciones dependiendo de las necesidades:

**Sin Verificación de Crédito**: Establecido de forma manual, omite la evaluación para los socios de negocios a los que no se evalúa el crédito, equivalente a **Sin límite de Crédito**.

**Crédito Correcto**: Activa la gestión de crédito por estar dentro del límite de cŕedito.

**Crédito Verificación**: Es establecido de forma automática por Solop ERP al evaluar el crédito, cuando el saldo actual está por encima del % de crédito en verificación (por defecto es 90%) del límite de crédito pero no alcanza el 100%.

**Crédito Retenido**: Es establecido de forma automática por Solop ERP al evaluar el crédito, cuando el saldo actual está por encima del límite de crédito, bloqueando la posibilidad de completar ordenes de ventas, completar facturas y emitir entregas.

**Crédito Detenido**: Establecido de forma manual, bloqueando la posibilidad de completar ordenes de ventas, completar facturas y emitir entregas.

Podrá visualizar el saldo actual que posee el cliente en el campo **Saldo Actual**.

El saldo actual es un campo solo lectura, actualizado de forma automática, aumentando o disminuyendo al emitir cuentas por cobrar o cuentas por pagar, controlando el estado de crédito.

Podrá visualizar el número de identificación autogenerado a partir del campo **Código** en el campo **Número de Identificación**

El número de identificación se refiere al número que acredita la identidad de una persona natural una entidad jurídica, por ejemplo, una cédula de identidad o un RUT, este campo mantiene incidencia en la generación de documentos fiscales como facturas, retenciones y comprobantes ARC.

Seleccione el checklist **Exento de Impuesto en Venta**.

Exento de Impuesto de Venta, no es un campo obligatorio, por defecto está establecido en falso, permite la omisión de impuestos al generar ordenes de ventas, es decir si un producto es gravado, hará una excepción para este socio de negocio, emitiendo la orden de venta con el producto en cuestión con impuesto (0%).

Seleccione el checklist **Exento de Impuesto en Compra**, para definir al socio del negocio como exento de impuesto.

Exento de Impuesto de Compra, no es un campo obligatorio, por defecto está establecido en falso, permite la omisión de impuestos al generar ordenes de compras, es decir si un producto es gravado, hará una excepción para este socio de negocio, emitiendo la orden de compra con el producto en cuestión con impuesto (0%).

Seleccione el grupo de impuestos en el campo **Grupo de Impuestos**.

Introduzca el código DUNS del socio del negocio en el campo **DUNS**.

El código DUNS no es un campo obligatorio, sin embargo, le permite introducir el número DUNS (Data Universal Numbering System o Sistema Universal de Numeración de Datos), el mismo es un un número de identificación proporciona la identidad única a cada empresa a nivel internacional.

Introduzca el número de referencia socio del negocio en el campo **No. de Referencia**.

El número de Referencia no es un campo obligatorio, sin embargo, le permite introducir un número fijo que utiliza el socio de negocio para gestiones administrativas, este tiene incidencia en las órdenes de compra o venta dependiendo la naturaleza de la entidad, siendo establecido de forma automática en las mismas.

Introduzca el código NAICS o SIC del socio del negocio en el campo **NAICS/SIC**.

El código NAICS/SIC no es un campo obligatorio, sin embargo, le permite introducir el código NAICS (American Industry Classification System ó Sistema de Clasificación Industrial de América del Norte), este es un código utilizado en los Estados Unidos, Canadá y México para clasificar la industria y actividades económicas.

Introduzca la valuación ABC en el campo **Valuación ABC**.

La valuación ABC no es un campo obligatorio, sin embargo, le permite establecer una evaluación clasificatoria del socio de negocio cliente.

Seleccione el grupo de socio del negocio en el campo **Grupo de Socio del Negocio**

El grupo de Socio del Negocio, permite categorizar sus socios de negocio de una forma específica, lo cual es eficiente a la hora de emitir asientos contables y reportes, para entenderlo mejor veamos el siguiente ejemplo:

Imaginemos que tenemos una cartera de clientes que manejan diferentes monedas, para categorizar de forma específica sería: **Clientes Nacionales** y **Clientes Internacionales**, de esta forma podría emitir reportes de cuentas por cobrar para clientes nacionales e Internacionales respectivamente.

Adicionalmente, define en el socio de negocio funciones y parámetros a partir de la categoría, entre las que se encuentran:

**Impresión a Color**: Define el color con los que serán mostrados en el arbol.

**Info Confidencial**: Permite ingresar información confidencial en solicitudes Web.

**Lista de Precios Venta**: Define lista de precios empleada en ordenes de venta y factura de cuentas por cobrar.

**Lista de Precios Compra**: Define lista de precios empleada en ordenes de compra y factura de cuentas por pagar.

**Esquema de Descuento OV**: Define esquema de descuento empleado en ordenes de venta y factura de cuentas por cobrar.

**Esquema de Descuento OC**: Define esquema de descuento empleado en ordenes de compra y factura de cuentas por pagar.

**Porcentaje de Crédito en Verificación de Cliente**: Define el porcentaje de crédito disponible para la evaluación del crédito previo a que un socio de negocio pase de crédito correcto a crédito en verificación.

**Porcentaje de Tolerancia OC/Factura**: Define el porcentaje de diferencia que puede existir entre el precio de la orden de compra y el precio de la factura de cuentas por pagar, porcentaje de holgura con el cual podría ser completados estos documentos sin pasar por el flujo de aprobación.

**Contabilidad**: Define cuentas contables en la que se realizarán los asientos contables dependiendo de la naturaleza del socio de negocio (Clientes o Proveedores).

Seleccione el tipo de cuenta en el campo **Tipo de Cuenta**.

El tipo de cuenta no es un campo obligatorio, sin embargo, le permite a los vendedores conocer con perfección las características de sus clientes y los diferentes tipos de clientes definidos en la empresa y así realizar un mejor estudio de mercado.

Seleccione el lenguaje en el campo **Lenguaje**.

El lenguaje no es un campo obligatorio, sin embargo, define el idioma con que será impreso los formatos de impresión asociados a este Socio de Negocio.

Seleccione el tipo de industria en el campo **Tipo de Industria**.

El tipo de industria no es un campo obligatorio, sin embargo, define la tipología de industria en la que se encuentra el Socio de Negocio.

Seleccione el segmento en el campo **Segmento**.

El segmento no es un campo obligatorio, sin embargo, permite segmentar socios de negocios de manera rigurosa, identificar patrones que pueden ser usados para asignar un segmento.

Seleccione el grupo de ventas en el campo **Grupo de Ventas**.

El grupo de ventas no es un campo obligatorio, sin embargo, permite categorizar al socio de negocio en un grupo de venta con objetivos referente a marketing y promociones.

Introduzca la dirección de la página web en el campo **Dirección Web**.

La dirección Web no es un campo obligatorio, sin embargo, permite registrar el sitio web del socio del negocio (Cliente y Proveedores) en el cual se administra la información de contacto de la empresa para solucionar sus inquietudes, realizar compras y gestión de solicitudes, aprovechando oportunidades de negocio que se encuentran en la red.

Seleccione el checklist **Prospecto Activo**.

Prospecto Activo no es un campo obligatorio, por defecto está establecido en falso, sin embargo al seleccionarlo indica que el socio de negocio de tipo cliente está activo.

Seleccione la opción **Liga Organización**, para ejecutar el proceso.

El proceso liga organización es ejecutado para los casos en los que la organización en gestión requiere generar documentos o solicitudes que son cubiertas por otra organización, para entenderlo mejor veamos el siguiente ejemplo:

Imaginemos que tenemos una organización (**Inversión del Norte**) donde existe un proveedor **Inversión del Sur C.A**, este es ligado a la organización **Inversión del Sur**.

Cuando **Inversión del Norte** emite una orden de compra configurada para emitir contra documento con el proveedor **Inversión del Sur C.A**, es emitida una orden de venta para **Inversión del Norte** que satisface la orden de compra.

Para ejecutar este proceso debe tomar en cuenta los siguientes parámetros:

**Organización Existente**: Seleccione una organización existente, si el campo queda vacío, se creará una organización con el nombre del socio de negocio de forma automática.

**Tipo de Organización**: Seleccione tipo de organización previa definición.

**Límite de Acceso al Rol**: Seleccione un rol existente si desea que sólo un rol específico tenga acceso a esta organización, si el campo queda vacío, el rol ClientAdmin y ClientUser tendrán acceso a esta organización.

Seleccione la opción **OK** y será ejecutado el proceso.

Las configuraciones por límite de acceso a rol es modificable desde los roles.

La organización puede ser ligada únicamente a un socio de negocio, para corregir un error en la asignación de la organización, ejecute el proceso: Desliga de Socio de Negocio a organización.

Introduzca el valor de ingresos en el campo **Valor Esperado**.

El valor esperado no es un campo obligatorio, sin embargo, permite ingresar un monto informativo de la rentabilidad esperada, basada en una estimación ingresos de un cliente.

Podrá visualizar el valor total de transacciones que posee el cliente en el campo **Valor Total Transacciones**.

El valor total transacciones es un campo solo lectura, actualizado de forma automática, sumando cada ingreso generado por este cliente, el mismo permite evaluar la rentabilidad de un cliente potencial.

Introduzca el costo de adquisición en el campo **Costo de Adquisición**.

El costo de adquisición no es un campo obligatorio, sin embargo, permite registrar el monto total correspondiente al costo generado para lograr convertir un prospecto a cliente.

Introduzca la cantidad de empleados en el campo **Empleados**.

Empleados no es un campo obligatorio, sin embargo, le permite evaluar la cantidad de empleados de una empresa prospecto, funge como un dato informativo para ser utilizada en cotizaciones por ejemplo.

Introduzca el porcentaje de participación en el campo **Participación**.

La participación no es un campo obligatorio, sin embargo, le permite mantener el control porcentualmente de la proporción obtenidas de las compras del cliente en la producción o distribución de productos o servicios.

Esto puede generar fidelización del cliente, dando la oportunidad de evaluar promociones y descuentos para aquellos clientes en los cuales su participación sea alta, y a su vez, mayor oportunidad en el aumento de la cartera de cliente creando programas para ventas cruzadas y sugestivas, comercializando así más productos y servicios.

Introduzca el número de ventas total en el campo **Volumen de Ventas**.

El volumen de ventas no es un campo obligatorio, sin embargo, permite registrar el número de ventas efectivas de un cliente, estas cifras generalmente son auditadas en reuniones directivas para evaluar la rentabilidad y expansión del negocio o si por el contrario sus ventas disminuyen.

Adicionalmente este datos es producto de supervisión para controlar volumen de ventas en comparación a pronósticos de ventas, estableciendo una estimación de cantidades mínimas a vender para mantener un equilibrio en la organización.

Introduzca la fecha de la primera venta en el campo **Primera Venta**.

La primera venta no es un campo obligatorio, sin embargo, permite registrar la fecha de la primera venta de forma informativa, útil para evaluar descuentos y promociones por aniversarios

Seleccione el check **Entrega Directa**

El check entrega directa no es un campo obligatorio, sin embargo, permite registrar el socio de forma informativa, útil para generar reportes e indicar que los envíos de las notas se envían del vendedor directamente al cliente.

Seleccione el tipo de persona en el campo **Tipo de Persona**.

El tipo de persona se refiere a la forma legal como está está constituida una organización, entre las cuales tenemos las siguientes opciones:

**Jurídica Domiciliada**: Persona Jurídica Domiciliada es una empresa constituida dentro del territorio nacional, que cumple sus obligaciones y resguarda la empresa con su patrimonio.

**Jurídica No Domiciliada**: Persona Jurídica No Domiciliada es una empresa constituida fuera del territorio nacional, que cumple sus obligaciones y resguarda la empresa con su patrimonio.

**Natural Residente**: Persona Natural Residente es una persona residente en el país que asume las obligaciones, responsabilidades y resguarda las obligaciones con patrimonio propio.

**Natural No Residente**: Persona Natural No Residente es una persona residente fuera del país, que asume las obligaciones, responsabilidades y resguarda las obligaciones con patrimonio propio.

Adjunte el logo de la empresa en el campo **Logo**.

El logo no es un campo obligatorio, sin embargo permite guardar logotipos de socios de negocios.

Seleccione el icono **Guardar Cambios** ubicado en la barra de herramientas para guardar los datos ingresados.

Recuerde guardar el registro de los campos cada vez que se vaya a posicionar en una pestaña de la ventana socio del negocio.

- Proveedor
  - Registro de Proveedor
- Cliente
  - Registro de Cliente
- Empleado
  - Registro de Empleado

### Proveedor

Un socio del negocio proveedor es aquella persona u organización que provee de productos y servicios a otra que lo necesite para su consumo, los transforme para su venta o los compre para venderlos sin modificaciones.

Solop ERP tiene la funcionalidad de permitirle a las organizaciones llevar un control de las transacciones realizadas con proveedores internos y externos.
Un proveedor interno puede ser un proveedor nacional, este puede presentarse bajo tres (3) condiciones, proveedor empleado de la organización, proveedor cliente nacional de la organización o simplemente proveedor nacional.

De igual manera, un proveedor externo puede ser un proveedor internacional, este puede presentarse bajo dos (2) condiciones, proveedor cliente internacional de la organización o simplemente proveedor internacional. A continuación se define el proceso para la creación de socio del negocio proveedor en Solop ERP.

- Registro de Proveedor
  - Pestaña Cuenta Bancaria
  - Pestaña Localización
  - Pestaña Contacto

#### Registro de Proveedor

Para registrar un proveedor, es necesario que sea realizado el procedimiento regular explicado en el documento **Registro de Socio del Negocio**, elaborado por **Solop ERP**.

Luego de culminar el procedimieto de registro de socio del negocio, seleccione la pestaña **Proveedor** que se encuentra del lado izquierdo de la ventana socio del negocio, para identificar al socio del negocio como proveedor de la empresa.

Esta pestaña le indica a Solop ERP si el socio del negocio que se esta registrando es un proveedor

![Pestaña Proveedor](/assets/img/docs/master-data/mad-master-proveedor1.png)

Imagen 1. Pestaña Proveedor

La pestaña **Proveedor** se compone de:

- Un checklist **Proveedor**.
- Los datos principales del socio del negocio donde los campos **Compañía**, **Organización**, **Código** y **Nombre**, vienen cargados de la ventana principal **Socio del Negocio**.
- Ademas posee un grupo de campos que definen la configuración de retenciones a aplicar al socio del negocio, dichos campos se encuentran explicados en los documentos Configuración Esencial de la Retención de IVA, Configuración Esencial de la Retención de ISLR y Configuración Esencial de la Retención Municipal.

Seleccione el checklist **Proveedor** para habilitar en Solop ERP el socio del negocio como proveedor de la compañía u organización.

De no ser tildado el checklist **Proveedor**, Solop ERP no tomará el socio del negocio como proveedor.

Al tildar el checklist **Proveedor** podrá apreciar un grupo de campos necesarios para la compra de productos al mismo, dichos campos no son obligatorios ya que pueden ser definidos en el documento **Orden de Compra** al momento de su elaboración.

El campo **Regla de Pago** establece la regla de pago definitiva para las compras al socio del negocio proveedor que se esta registrando, para este ejemplo la regla de pago utilizada es **A Crédito**.

El campo **Lista de Precios de Compra** establece la lista de precios definitiva para las compras al socio del negocio proveedor que se esta registrando, para este ejemplo la lista de precios utilizada es **Compra (UYU)**.

El campo **Término Pago Orden de Compra** establece el término de pago definitivo para las compras al socio del negocio proveedor que se esta registrando, para este ejemplo el término de pago utilizado es **Crédito a 15 días**.

El campo **Esquema del Descuento en OC** establece el descuento definitivo para las compras al socio del negocio proveedor que se esta registrando, para este ejemplo el esquema de descuento utilizado es **Compras Porcentaje Simple**.

El campo **Exento de (IGTF)** establece que no se aplicará el impuesto **IGTF** al socio del negocio proveedor que se esta registrando

### Pestaña Cuenta Bancaria

En esta pestaña se registran los datos bancarios del socio del negocio proveedor, con el checklist **Activo** se pueden registrar los datos de la tarjeta de crédito del socio del negocio. Así mismo, con el checklist **ACH** se pueden registrar los datos de la cuenta bancaria del socio del negocio.

Seleccione la pestaña **Cuenta Bancaria** que se encuentra ubicada del lado izquierdo de la ventana socio del negocio. Por defecto se encuentra tildado el checklist **Activo**.

![Pestaña Cuenta Bancaria](/assets/img/docs/master-data/mad-master-count1.png)

Imagen 9. Pestaña Cuenta Bancaria

#### Checklist Activo

Seleccione en el campo **Tarjeta de Crédito**, el tipo de tarjeta de crédito que posee el socio del negocio proveedor que esta registrando.

Introduzca en el campo **Número**, el número de tarjeta de crédito del socio del negocio proveedor que esta registrando.

Introduzca en el campo **Código Verificación**, el código de verificación de la tarjeta de crédito del socio del negocio proveedor que esta registrando, este código son los últimos tres números del reverso de la tarjeta.

Introduzca en el campo **Mes de Expiración**, el mes de expiración de la tarjeta de crédito del socio del negocio proveedor que esta registrando.

Introduzca el año de expiración de la tarjeta de crédito del socio del negocio proveedor que esta registrando en el campo **Año de Expiración**.

Introduzca el nombre de referencia de la tarjeta en el campo **Nombre**, en este campo va el nombre del titular de la tarjeta de crédito que esta registrando.

Este proceso se realiza con la finalidad de registrar la tarjeta de crédito del socio del negocio.

#### Checklist ACH

Para registros de cuentas bancarias, tilde el checklist **ACH**, a continuación se reflejarán los campos para el registro de la cuenta bancaria del socio del negocio proveedor.

En el campo **Banco** seleccione el banco a registrar con ayuda del icono identificador (adjunto imagen).

A continuación visualizará la siguiente ventana con los diferentes bancos, dónde debe seleccionar el banco que posee el socio del negocio proveedor y la opción **OK** para cargar los datos a la ventana.

![Ventana Bancos](/assets/img/docs/master-data/mad-master-windows1.png)

Imagen 10. Ventana Bancos

Seleccione en el campo **Tipo de Cuenta Bancaria**, el tipo de cuenta correspondiente a la cuenta del socio del negocio proveedor.

Introduzca en el campo **No. De Cuenta**, el número de cuenta del socio del negocio proveedor que esta registrando.

Introduzca en el campo **Nombre**, el nombre del titular de la cuenta bancaria que esta registrando.

### Pestaña Localización

La localización de un socio del negocio es muy importante por diferentes motivos y más si el socio del negocio es proveedor. Ya que las transacciones de compras serán realizadas al mismo, en esta pestaña se deben registrar con exactitud los datos de la dirección del socio del negocio.

Seleccione la pestaña **Localización** que se encuentra ubicada del lado izquierdo de la ventana socio del negocio.

![Pestaña Localización](/assets/img/docs/master-data/mad-master-location1.png)

Imagen 22. Pestaña Localización

A continuación visualizará la siguiente ventana, dónde debe ingresar la dirección exacta del socio del negocio proveedor que esta registrando.

![Ventana de Localización](/assets/img/docs/master-data/mad-master-location-4.png)

Imagen 23. Ventana de Localización

::: warning
Recuerde guardar el registro de los campos cada vez que se vaya a posicionar en una pestaña de la ventana socio del negocio.
:::

### Pestaña Contacto

En esta pestaña se registran todos los datos de contacto que se tengan del socio del negocio proveedor.

Seleccione la pestaña **Contacto** que se encuentra ubicada del lado izquierdo de la ventana socio del negocio, para proceder a llenar los campos necesarios.

![Pestaña Contacto](/assets/img/docs/master-data/mad-master-contac1.png)

Imagen 24. Pestaña Contacto

Introduzca en el campo **Nombre**, el nombre del socio del negocio contacto para las transacciones entre las empresas.

Introduzca en el campo **Email**, el email del socio del negocio contacto para las transacciones entre las empresas.

Introduzca en el campo **Teléfono**, el teléfono del socio del negocio contacto para las transacciones entre las empresas.

::: note
Este procedimiento realizado aplica solo para los Socios del Negocio que cumplan el rol de Proveedor.
:::

### Cliente

Si es usted un usuario en etapa de iniciación le recomendamos leer el capítulo anterior, Socios del Negocio de Solop ERP, donde respondimos la interrogante común: **¿Qué es un Socio de Negocio?**, esto con la intención de proveer en este material una información más digerible.

Como resultado de lo anteriormente expuesto, se puede concluir que un socio de negocio que actúa como cliente, es una entidad jurídica o natural que adquiere productos o servicios provenientes de la empresa,estos pueden ser:

- **Clientes Nacionales:** Realizan transacciones que generan ingresos a la empresa (Ventas) dentro del territorio.
- **Clientes Internacionales:** Realizan transacciones que generan ingresos a la empresa(Ventas) fuera del territorio, esto se conoce como exportación.

Esta categorización en Solop ERP es conocida como **Grupo de Socio de Negocio** y es la base contable (en su mayoría) para las operaciones emitidas a partir de este registro maestro, no obstante, el usuario tiene la opción de realizar configuraciones excepcionales para ciertos clientes.

Para este caso, usted tendría por categoría diferentes cuentas contables, Cuenta por Cobrar Nacionales y Cuenta por Cobrar Internacionales respectivamente.

Ahora bien, si es usted usuario de Solop ERP, seguramente se ha hecho preguntas que le han complicado la operativa de algún modo. Para facilitar su día a día **Solop ERP** quiere responder algunas preguntas frecuentes con las que nos topamos en nuestra experiencia como consultores e implementadores de Solop ERP:

**¿Si un socio de negocio es proveedor o empleado, y ahora funge como cliente, debo crearlo nuevamente?**

No, esto ha ocasionado en innumerables oportunidades duplicidades de registros e incongruencias en resultados. Bastará con ubicar con el código del socio del negocio al mismo y configurar como lo indica este material.

**Si la categoría es por ejemplo Cliente Nacional, ¿cómo actúa contablemente siendo cliente y proveedor?**

Pues bien, la categoría generalmente hace referencia a la agrupación contable a la que pertenece el socio de negocio cuando es registrado por primera vez, la misma contempla en su definición las cuentas contables a establecer en la pestaña de cliente y en la de proveedor, esto de alguna manera solventa la inquietud de no poder colocar dos tres grupos de socios de negocios, si desea conocer más del ¿cómo opera esta agrupación? de la que hablo vaya a **Grupo de Socio de Negocio**.

**¿Cómo agrupar por vendedor a mis clientes para emitir un reporte?**

Para ofrecer una eficiente administración en distribución y seguimiento de clientes y pedidos generados, Solop ERP ofrece al usuario dos opciones:

- **Por Región de Ventas:** De esta forma se asigna la región de venta a un cliente, a su vez, ésta depende de un asesor de ventas.Esto permite una mayor facilidad en el mantenimiento por ausencia de vendedores, si su cliente posee más de una dirección podría configurar más de un asesor.
- **Por Asesor Especifico:** De esta forma se asigna un vendedor especifico al cliente directamente, omitiendo configuraciones en la localización.

**¿Qué columnas configuradas en el cliente es información transferida a la orden de venta?**

Existen múltiples reglas que permiten predefinir valores en transacciones dependiendo de la configuración:

- **Regla de facturación:** Define si la facturación después del pedido será después de la entrega, programada con el cliente o inmediatamente.
- **Regla de entrega:** Define si la entrega después del pedido será después del cobro, a disponibilidad del producto o forzado.
- **Descuentos:** Define esquemas de descuentos basados en volumen de ventas, promociones o % estáticos.
- **Vendedor o Asesor de Ventas:** Define el agente que garantiza la satisfacción y el cumplimiento de las demandas del cliente.
- **Regla de pago:** Define la metodología con la que generalmente el cliente cancela sus deudas.
- **Programas de Pago:** Define esquemas de pagos y estructuras de cuotas para la cancelación de sus deudas.
- **Lista de Precio:** Define lista de precio y moneda con la que generalmente el cliente cancela sus deudas.

Entre muchos otros campos más que son predeterminados desde el socio de negocio, pasando por la orden de venta y la factura, ellos definen comportamientos en funcionalidades versátiles dentro de Solop ERP.

**¿Cómo configuro un descuento para el cliente?**

Solop ERP le permite aplicar un Esquema de Descuentos(previamente configurado) al cliente, en este sentido, el usuario podrá definir reglas específicas aplicando % de descuentos planos o basado en volumen, si desea profundizar más el tema, le invitamos a ver nuestro instructivo de **Esquema de Descuentos**.

**¿Cómo bloqueo el límite de crédito para el cliente?**

Podrá configurar estados de crédito para definir el comportamiento del análisis del crédito en el Socio de Negocio, el mismo actúa junto al **Saldo Actual** y **Límite de Crédito** para realizar la evaluación, si desea profundizar más el tema, le invitamos a ver nuestro instructivo de Socio del Negocio.

**¿Cómo configuro un cliente exento de impuesto?**

Para concluir el preámbulo, le invitamos a tomar en cuenta cada una de estas acotaciones, de seguro serán de utilidad, y a futuro le garantizará un eficiente manejo de una herramienta tan potente como lo es Solop ERP.

- Registro de Cliente
  - Pestaña Cuenta Bancaria
  - Pestaña Localización
  - Pestaña Contacto

#### Registro de Cliente

Para registrar un cliente, es necesario que sea realizado el procedimiento regular explicado en el documento **Registro de Socio del Negocio**, elaborado por **Solop ERP**.

Luego de culminar el procedimieto de registro de socio del negocio, seleccione la pestaña **Cliente** que se encuentra del lado izquierdo de la ventana socio del negocio, para identificar al socio del negocio como cliente de la empresa.

En esta pestaña es registrada la información que la empresa requiere del socio del negocio cliente al momento de una venta al mismo. Cada uno de los campos que la misma contiene son necesarios en algún punto de la transacción de ventas.

![Pestaña Cliente](/assets/img/docs/master-data/mad-master-client1.png)

Imagen 1. Pestaña Cliente

A continuación visualizará la siguiente imagen, dónde debe tildar el checklist **Cliente**.

![Checklist Cliente](/assets/img/docs/master-data/mad-master-checklist-client1.png)

Imagen 2. Checklist Cliente

Al tildar el checklist **Cliente**, podrá apreciar diferentes campos que establecen los términos o reglas para las transacciones de ventas al socio del negocio cliente que esta registrando. Dichos campos no son obligatorios porque pueden ser establecidos al momento de generar la orden de venta al socio del negocio.

Introduzca en el campo **Copias del Documento**, el número de copias a ser impresas de cada documento generado al socio del negocio cliente.

Seleccione en el campo **Regla de Facturación**, la regla establecida para facturar al socio del negocio cliente.

Seleccione en el campo **Programa de Facturación**, la frecuencia usada cuando se generan las facturas.

Seleccione en el campo **Regla de Entrega**, la regla establecida para entregar al cliente los productos o servicios.

Seleccione en el campo **Vía de Entrega**, como serán entregados los productos o servicios de la orden.

Seleccione en el campo **Lista de Precios**, la lista de precios establecida para las ventas al socio del negocio cliente que esta registrando.

Seleccione en el campo **Esq List Precios/Desc**, el esquema para calcular el porcentaje de descuento comercial.

Podrá apreciar en el campo **% Descuento**, el porcentaje de descuento configurado en el esquema de descuento.

Seleccione en el campo **Regla de Pago**, la forma de pago de las facturas establecida para el socio del negocio cliente que esta registrando.

Seleccione en el campo **Término de Pago**, las condiciones de pago de las facturas establecida para el socio del negocio que esta registrando.

Seleccione en el campo **Agente Comercial**, asignado a la región donde se encuentra el socio del negocio cliente.

Seleccione en el campo **Morosidad**, la regla de morocidad para facturas vencidas.

Introduzca en el campo **Referencia de Orden de Socio del Negocio**, el número estándar de referencia para las órdenes de compra.

Seleccione el checklist **Imprimir Descuento**, si desea imprimir en la factura y en la orden de venta el descuento aplicado.

Introduzca en el campo **Descripción de Orden**, una descripción estándar para se utilizadas en las órdenes a generar al socio del negocio cliente que esta registrando.

Seleccione en el campo **Formato de Impresión**, el formato de impresión a utilizar en las facturas del socio del negocio cliente.

Introduzca en el campo **Mín de Vida útil %**, tiempo mínimo de vida útil que tienen los productos.

Introduzca en el campo **Límite de Crédito**, el límite de crédito establecido para el socio del negocio cliente que esta registrando.

Podrá visualizar en el campo **Crédito Usado**, el crédito usado por el socio del negocio cliente que esta registrando.

Introduzca en el campo **Tiempo Gracia Cobro**, los días de gracia que tiene el socio del negocio antes de que el agente comercial le realice el cobro.

### Pestaña Cuenta Bancaria

En esta pestaña se registran los datos bancarios del socio del negocio cliente, con el checklist **Activo** se pueden registrar los datos de la tarjeta de crédito del socio del negocio. Así mismo, con el checklist **ACH** se pueden registrar los datos de la cuenta bancaria del socio del negocio.

Seleccione la pestaña **Cuenta Bancaria** que se encuentra ubicada del lado izquierdo de la ventana socio del negocio. Por defecto se encuentra tildado el checklist **Activo** (idéntica pestaña que cuenta bancaria proveedor)

#### Checklist Activo

Seleccione en el campo **Tarjeta de Crédito**, el tipo de tarjeta de crédito que posee el socio del negocio cliente que esta registrando.

Introduzca en el campo **Número**, el número de tarjeta de crédito del socio del negocio cliente que esta registrando.

Introduzca en el campo **Código Verificación**, el código de verificación de la tarjeta de crédito del socio del negocio cliente que esta registrando, este código son los últimos tres números del reverso de la tarjeta.

Introduzca en el campo **Mes de Expiración**, el mes de expiración de la tarjeta de crédito del socio del negocio cliente que esta registrando.

Introduzca el año de expiración de la tarjeta de crédito del socio del negocio cliente que esta registrando en el campo **Año de Expiración**.

Este proceso se realiza con la finalidad de registrar la tarjeta de crédito del socio del negocio.

#### Checklist ACH

Para registros de cuentas bancarias, tilde el checklist **ACH**, a continuación se reflejarán los campos para el registro de la cuenta bancaria del socio del negocio (mismo check que en cuenta bancaria proveedor).

Introduzca en el campo **IBAN**, el código IBAN conformado por el código del país (2 dígitos) más el código de control de la localidad donde se encuentra la sucursal del banco (2 dígitos). Para ejemplificar el registro es utilizado el código **UY21**

En el campo **Banco** seleccione el banco a registrar con ayuda del ícono identificador.

A continuación visualizará la ventana con los diferentes bancos (misma ventana que en cuenta bancaria proveedor), dónde debe seleccionar el banco que posee el socio del negocio cliente y la opción **OK** para cargar los datos al formulario.

Seleccione el tipo de cuenta correspondiente a la cuenta del socio del negocio cliente en el campo **Tipo de Cuenta Bancaria**.

Introduzca en el campo **No. De Cuenta**, el número de cuenta del socio del negocio cliente que esta registrando.

Este proceso se realiza con la finalidad de registrar la cuenta del socio del negocio.

Introduzca el nombre de referencia en el campo **Nombre**, en este campo va el nombre del titular de la tarjeta de crédito o de la cuenta bancaria que esta registrando.

Introduzca en el campo **Dirección**, la dirección de la entidad bancaria poseedora de la tarjeta de crédito.

Introduzca en el campo **Ciudad**, el nombre de la ciudad donde se encuentra la entidad bancaria poseedora de la tarjeta de crédito.

Introduzca en el campo **Código Postal**, el código postal de la ciudad donde se encuentra la entidad bancaria poseedora de la tarjeta de crédito.

Introduzca en el campo **Estado**, el nombre del estado donde se encuentra la entidad bancaria poseedora de la tarjeta de crédito.

Introduzca en el campo **País Cuenta**, el nombre del país donde se encuentra la entidad bancaria poseedora de la tarjeta de crédito.
Introduzca en el campo **Licencia de Conducir**, el número de licencia de conducir del socio del negocio cliente que esta registrando.

Introduzca en el campo **No. Seguro Social**, el número de cédula del titular de la tarjeta de crédito o cuenta bancaria que esta registrando.

Introduzca en el campo **Cta. Correo Electrónico**, el correo electrónico asociado a la tarjeta de crédito o cuenta bancaria que esta registrando.

Seleccione en el campo **Dirección Verificada**, si la dirección de la entidad bancaria se encuentra verificada.

Seleccione en el campo **Código Postal Verificado**, si el código postal de la entidad bancaria se encuentra verificado.

### Pestaña Localización

La localización de un socio del negocio cliente es muy importante por diferentes motivos, ya que las transacciones de ventas serán realizadas al mismo, en esta pestaña se deben registrar con exactitud los datos de la dirección del socio del negocio.

Seleccione la pestaña **Localización** que se encuentra ubicada del lado izquierdo de la ventana socio del negocio (misma que Localización proveedor).

Introduzca en el campo **Localización / Dirección**, la dirección de localización del socio del negocio cliente con ayuda del identificador.

Seleccione en el campo **País**, el país donde se encuentra domiciliado el socio del negocio que esta registrando

Seleccione en el campo **Estado**, el estado donde se encuentra domiciliado el socio del negocio que esta registrando.

Seleccione en el campo **Ciudad**, la ciudad donde se encuentra domiciliado el socio del negocio que esta registrando.

Introduzca la dirección detallada del socio del negocio cliente en el campo **Dirección 1** y seleccione la opción **OK**

Introduzca en el campo **Teléfono**, el número de teléfono local para contactar al socio del negocio cliente.

Introduzca en el campo **Teléfono Móvil**, el número de teléfono móvil para contactar al socio del negocio cliente.

Introduzca en el campo **Fax**, el fax para contactar al socio del negocio cliente.

Introduzca en el campo **ISDN**, el ISDN para contactar al socio del negocio cliente.

Podrá apreciar tildados los checklist **Dirección Entregar-A**, **Dirección Facturar-A**, **Dirección Pagar-Desde** y **Dirección Remitir-A**, indicando cada uno de ellos un comportamiento diferente.

El checklist **Dirección Facturar-A** establece la localización ingresada como la dirección para facturar.

El checklist **Dirección Pagar-Desde** establece la localización ingresada como la dirección desde donde paga las facturas el socio del negocio y donde son enviadas las cartas de morosidad.

El checklist **Dirección Remitir-A** establece la localización ingresada como la dirección para el envío de los pagos.

Seleccione en el campo **Región de Ventas**, la región o área de ventas en la que se encuentra localizado el socio del negocio cliente.

Para conocer más sobre las regiones de ventas que puede tener una compañía u organización, visite el documento **Registro de Región de Ventas**, elaborado por **Solop ERP**.

Introduzca en el campo **Código SICA**, el código SICA del socio del negocio cliente.

Recuerde guardar el registro de los campos cada vez que se vaya a posicionar en una pestaña de la ventana socio del negocio.

### Pestaña Contacto

En esta pestaña se registran todos los datos de contacto que se posea el socio del negocio cliente. De igual manera, es creado su usuario de acceso en Solop ERP (idéntica pestaña que Contacto proveedor).

Seleccione la pestaña **Contacto** que se encuentra ubicada del lado izquierdo de la ventana socio del negocio, para proceder a llenar los campos necesarios.

El contacto (Usuario) permite registrar las diferentes personas de contacto que tiene la empresa con el socio del negocio cliente que esta registrando. Un ejemplo de esta pestaña puede ser, un jefe o persona de contacto por departamento para que a la hora de alguna venta de productos o servicios al socio del negocio cliente, se contacte a la persona correspondiente.

Introduzca en el campo **Nombre**, el nombre completo de la persona de contacto con el socio del negocio cliente que esta registrando.

Introduzca en el campo **Descripción**, una breve descripción de la persona de contacto con el socio del negocio cliente que esta registrando

Introduzca en el campo **Comentarios**, los comentarios o información adicional sobre el registro de la persona de contacto con el socio del negocio cliente.

El checklist **Activo**, indica que el registro se encuentra activo en el sistema.

Seleccione el checklist **Es Gerente de Proyecto**, para indicar que la persona de contacto con el socio del negocio cliente es gerente de proyecto.

Seleccione el checklist **Es Miembro de un Proyecto**, para indicar que la persona de contacto con el socio del negocio cliente es miembro de un proyecto.

Seleccione el checklist **Usuario de Autenticación** para que sean reflejados los campos necesarios para crear el usuario del socio del negocio cliente.

Seleccione el checklist **Usuario Interno**, para indicar que la persona de contacto con el socio del negocio cliente es usuario interno.

Introduzca en el campo **Código**, el usuario de la persona de contacto con el socio del negocio cliente para ingresar a Solop ERP.

Solop ERP tiene establecido como estándar de creación de usuario y contraseña en Solop ERP, la inicial del primer nombre en minúscula, seguido del primer apellido completo, con la primera letra del mismo en mayúscula.

Introduzca en el campo **Contraseña**, la contraseña de la persona de contacto con el socio del negocio cliente para ingresar a Solop ERP.

Solop ERP tiene establecido como estándar de creación de usuario y contraseña en Solop ERP, la inicial del primer nombre en minúscula, seguido del primer apellido completo, con la primera letra del mismo en mayúscula.

Seleccione el checklist **Usuario de Tienda Web**, para indicar que la persona de contacto con el socio del negocio es usuario de tienda web.

Introduzca en el campo **Email**, el correo electrónico de la persona de contacto con el socio del negocio para las transacciones entre las empresas.

Seleccione en el campo **Saludo**, la forma de saludar a la persona de contacto con el socio del negocio en los documentos a ser enviados.

Seleccione en el campo **Dirección del Socio del Negocio**, la dirección de ubicación de la persona de contacto con el socio del negocio.

Introduzca en el campo **Título**, el nombre del socio del negocio cliente.

Seleccione en el campo **Cumpleaños**, la fecha de nacimiento de la persona de contacto con el socio del negocio.

Introduzca en el campo **Teléfono**, el teléfono para localizar a la persona de contacto con el socio del negocio para las transacciones entre las empresas.

Introduzca en el campo **Teléfono Móvil**, el teléfono móvil para localizar a la persona de contacto con el del socio del negocio.

Introduzca en el campo **Fax**, el fax de contacto del socio del negocio.

Seleccione en el campo **Tipo de Notificación**, la forma de enviar notificaciones a la persona de contacto con el socio del negocio.

Seleccione en el campo **Posición**, la posición de trabajo de la persona de contacto con el socio del negocio.

Podrá apreciar el checklist **Acceso Total Socio del Negocio**, que al estar tildado indica que la persona de contacto con el socio del negocio cliente posee acceso total a su rol.

Seleccione el icono **Guardar Cambios** en la barra de herramientras de Solop ERP, para guardar el registro de los campos.

Este procedimiento realizado aplica solo para los Socios del Negocio que cumplan el rol de Cliente.

### Empleado

Un socio del negocio empleado es aquella persona que presta sus servicios como trabajador en una determinada empresa u organización, desempeñando un cargo y recibiendo un salario a cambio de sus servicios.

Solop ERP permite realizar un registro único y detallado de toda la información que la organización requiere del empleado en su respectivo momento, ya sea para pagos, capacitaciones, retenciones o remuneraciones. De igual manera, permite registrar información referente a seguro, experiencia laboral, educación, familiares, dependientes, entre otros.

A continuación se define el proceso para la creación de socio del negocio empleado en Solop ERP.

#### Registro de Empleado

Luego de culminar el procedimieto de registro de socio del negocio, seleccione la pestaña Empleado que se encuentra del lado izquierdo de la ventana socio del negocio, para identificar al socio del negocio como empleado de la empresa.

En esta pestaña es registrada la información que la empresa requiere del socio del negocio empleado al momento de interactuar o generar operaciones para el mismo. Cada uno de los campos que la misma contiene son necesarios en algún punto de la transacción con el empleado.

![Menú de Solop ERP](/assets/img/docs/master-data/mad-master-menu-4.png)

## 🧾 Guía de Usuario: Creación de Socio del Negocio desde un campo

Esta guía está destinada a explicar el proceso para crear un nuevo Socio del Negocio dentro del sistema desde otra entidad (Ejemplo: documento por cobrar)

🟢 1. Ingreso a ventana Documentos por Cobrar (aplica sobre ventanas estándar como documentos por pagar, órdenes de venta/compra, etc.)

* Acceder al campo "Socio del Negocio" de la ventana haciendo click izquierdo sobre el menú desplegable.

* Seleccionar la opción "Crear Socio".

Esta ventana puede personalizarse según la definición de pantalla (Display Definition), similar a la utilizada en otros módulos como Calendarios.

💡 Es posible configurar otras vistas adicionales como "Información del Socio" o "Saldos del Socio del Negocio", según las necesidades de la organización.

![Pestaña Contacto](/assets/img/docs/master-data/mad-master-contact3.png)

![Pestaña Contacto](/assets/img/docs/master-data/mad-master-contact4.png)

![Pestaña Contacto](/assets/img/docs/master-data/mad-master-contact5.png)

### 📝 2. Datos Iniciales

Campos obligatorios y personalizables:

* Clave de Búsqueda: identificador del socio (código).

* Nombre: Nombre del Socio del Negocio

Otros campos visibles pueden agregarse o quitarse según la configuración del sistema.

::: note
🔧 Esta ventana es flexible y puede ser adaptada para mostrar los campos relevantes según cada tipo de negocio.
:::

### 📍 3. Direcciones del Socio

Al momento de crear el socio, se puede ingresar información de dirección.

Tipos de direcciones disponibles:

* Dirección de Entrega

* Dirección de Facturación

Se puede seleccionar una sola opción o ambas, según corresponda.

📌 La referencia de dirección indica el uso que se le dará (entrega, factura o ambas).

### 🔒 4. Consideraciones sobre campos editables

Si el campo "Socio del Negocio" aparece como solo lectura, no se asigna automáticamente al momento de la creación (es decir, que permitirá crear SDN desde el campo Socio del Negocio cuando este se encuentre editable).

En entornos donde ese campo esté habilitado, el sistema asigna directamente el nombre en el alta.

### 🔍 5. Consulta de información del Socio

A través del botón "Información del Socio" se puede visualizar:

* Datos básicos del socio

* Direcciones vinculadas

* Agregar nuevas direcciones desde esta vista

✅ Esta funcionalidad permite consultar y editar información sin necesidad de ingresar completamente a la ventana del socio. Ahorra pasos y mejora la experiencia del usuario.

::: note
✅ Recomendaciones Finales

Utilizar la personalización de la pantalla para optimizar los datos según el tipo de socio (cliente, proveedor, empleado).

Aprovechar los accesos directos a información complementaria sin salir de la pantalla principal.

Verificar que los campos obligatorios estén correctamente cargados antes de validar la creación.
:::

Esta guía permite al usuario crear un nuevo Socio del Negocio de forma fácil, flexible y adaptada a las necesidades operativas del sistema.