---
title: Proyecto de Agencia Creativa
category: Documentation
star: 9
sticky: 9
tag: 
  - Agencia
article: false
---

## Proyecto de Agencia Creativa

Los Proyectos de Agencia Creativa se utilizan para crear, implementar y gestionar estrategias y campañas de marketing para ayudar a otras empresas a promover sus productos o servicios. 

Estas agencias ofrecen una variedad de servicios, que pueden incluir marketing digital, publicidad, relaciones públicas, diseño gráfico, desarrollo de contenido, gestión de redes sociales, SEO (optimización de motores de búsqueda), SEM (marketing en motores de búsqueda) y análisis de datos. 

Su objetivo principal es aumentar la visibilidad, el alcance y las ventas de sus clientes a través de tácticas efectivas y personalizadas. Solop ERP contempla estos procesos, diseñando un circuito que se adapta a sus necesidades.

El Proyecto de Agencia Creativa será donde se deba ingresar todo pedido realizado por el cliente. Desde el Proyecto se vinculará todos los documentos que se haya generado a causa dicho Pedido a lo largo de toda la organización (Solicitudes, Orden de Compra, Orden de Venta, Cotizaciones, Tareas, etc) y será desde donde se defina la facturación a realizar.

Cada Proyecto de Agencia podrá tener un Brief, este será la descripción del servicio solicitado por el Cliente. Este se puede definir tanto en un Campo Texto o bien adjuntando un archivo directo en el Proyecto. Según el tamaño y complejidad del mismo, este podrá ser por Fases, Tareas y Solicitudes vinculadas separando así el trabajo a realizar.

A su vez, directo desde un Proyecto se podrá generar las Órdenes de Venta definiendo lo que deberá facturar en relación al mismo.

### Se deberán definir obligatoriamente en el cabezal los siguientes Campos:

* Socio del Negocio 

* Nombre 

* Marca 

* Categoría del Proyecto 

* Nivel de línea 

* Fecha Inicio (creación) 

* Fecha Límite 

* Lista de Precios

### Campos Automáticos

#### Según la Lista de precio seleccionada:

* Moneda

![Proyecto de Agencia](/assets/img/docs/project-management/prm-project1.png)

#### Según el Cliente seleccionado:

* Término de pago: siempre que se encuentre definido en El cliente. 

* Almacén del Cliente: El almacén en un proyecto se definirá de manera automática según el almacén que 
tenga definido el Cliente en la pestaña Cliente ventana Socio del Negocio. 

* Contrato de Servicio: (En caso que el Cliente posea más de uno, el sistema tomará el primer Contrato creado que encuentre, por lo que se sugiere en estos casos elegir el Contrato en este campo de forma manual). 

* Sello.

* Sello Origen: Cuando se guarda un proyecto se realiza lo siguiente:

Según la Categoría de Proyecto se definirá el Sello Origen correspondiente que tenga definido el contrato en sus “Partes del Contrato”.

#### Según las siguientes Categoría de Proyecto se obtendrá el sello definido para el siguiente tipo de empresa:

* Categoría de Proyecto

* Tipo de Empresa

* Proyecto de Agencia

* Agencia Creativa

* Proyecto de Medios

* Agencia de Medios

* Proyecto RRPP

* Agencia RRPP

* Proyecto de Medios Digitales

* Agencia de Medios Digitales

::: note
Si no se obtuvo sello de origen se lanza una excepción.
:::

![Partes del Contrato](/assets/img/docs/project-management/prm-project2.png)

#### Según el usuario logueado en el sistema:

* Agente Comercial: Este campo en el cabezal de un Proyecto tomará de forma automática al usuario logueado en el sistema siempre que este tenga el check de “Agente comercial” en “Y”, en la Pestaña “Empleado” de la ventana “Socio de negocio”.

## Generación de órdenes de trabajo

Una orden de trabajo es considerado un Proyecto para Solop ERP.
Se trata de una unidad de gestión que agrupa un conjunto de entidades que le dan forma y describen un determinado Servicio.
Además, se trata de una dimensión contable, con el fin de poder obtener reportes financieros por Proyecto.

El primer paso para la creación de una Orden de trabajo es ingresar en la ventana el nombre del cliente (Socio del negocio del cual hereda la dirección y lista de precio), el campo Nombre (nombre de la campaña), fechas (opcionales), seleccionar una categoría de Proyecto, clase de Proyecto y una Descripción (o brief, dato manual opcional).
Al grabado queda generado el registro de orden de trabajo (cabezal).

![Proyecto de Marketing](/assets/img/docs/agency-management/agm-agency1.png)

### Líneas de Orden de Trabajo

Una vez creado el cabezal de la orden de trabajo (Proyecto) el ejecutivo puede crear la/s líneas de la orden.
Se trata de las tareas vinculadas al proyecto, o sea, los diferentes pedidos de un cliente para un determinado negocio.
Este circuito se realiza en dos partes:

* Primero el ejecutivo carga en el campo descripción el pedido específico de la tarea. Ingresa el nombre de la tarea en el campo "Material". Incorpora la cantidad, la unidad de duración (en general es "Hora") y fecha prometida (opcional).

* En un segundo paso el responsable de ejecutivos de cuentas (o quien cotiza) define el producto de las líneas. Cada producto posee un tarifario propio, el cual determina el precio del trabajo a realizar.

![Línea de Proyecto](/assets/img/docs/agency-management/agm-agency2.png)

### Proceso Generar Orden

Cuando cada línea de orden de trabajo posee su producto definido (así como el resto de sus datos obligatorios) el responsable de ejecutivos de cuentas (o quien realiza cotización) corre el proceso "Generar Orden" desde el cabezal de la orden de trabajo definiendo en el campo Sub tipo ov = Propuesta, y en el campo Tipo de Documento = Cotización de Venta.
Esto genera la orden de venta con la correspondiente cotización al cliente.
Es posible imprimir/exportar para envío y aprobación por parte del contacto de nuestro cliente.

![Generar Orden](/assets/img/docs/agency-management/agm-agency3.png)

### Convertir Cotización

Cuando el cliente notifica la aprobación de la cotización enviada, desde el proceso de menú "Convertir Cotización" es posible generar la Orden de Venta firme (definitiva).

Esto realiza en automático la marca de Aprobación por cliente = SI en la Orden de trabajo vinculada, así como la creación de tantas tareas como líneas posea la orden de trabajo (genera solicitudes). También genera el cierre de la Orden de Venta Cotización.

Las tareas pueden visualizarse desde los documentos relacionados o solapa Solicitudes en la misma orden de trabajo.

![Generar Orden](/assets/img/docs/agency-management/agm-agency4.png)

### Asignación de agentes de compañía a las diferentes tareas

Una vez generadas las tareas por cada línea de orden de trabajo, el paso posterior es asignar recurso a cada una de estas tareas (diseñadores) con el fin de dar seguimiento al status de cada trabajo.

La gestión de carga de horas y estado de las tareas se realiza desde Solicitudes (Asunto) y una vez que todas las tareas vinculadas a una orden de trabajo se encuentran finalizadas, la misma podrá ser facturada a cliente.

![Generar Orden](/assets/img/docs/agency-management/agm-agency5.png)

### Crear Marcas de Clientes

Ventana: **"Campaña"**

En la pestña de clientes se debe definir el cliente(s) para un correcto funcionamiento del link del campo, para que desde el Proyecto se muestren las marcas que posee cada cliente (una vez se defina el cliente en el proyecto).

![Generar Orden](/assets/img/docs/agency-management/agm-agency6.png)

![Generar Orden](/assets/img/docs/agency-management/agm-agency7.png)


### Generar Orden de Venta desde Solicitud de Cotización

Una vez generada la Solicitud de Cotización (RFQ-Request for Quotation), evaluadas las respuestas, y aceptado una Respuesta de Cotización por el Cliente, se deberá proceder a generar una Orden de Venta al Cliente para que la misma se pueda aprobar mediante el flujo de aprobación estándar de la Orden de Venta.

La Orden de Venta se podrá generar directo desde la Solicitud de Cotización desde el botón “Crear Orden de Venta”.

Seleccione el Tipo de Orden de Venta “Orden de Venta con Aprobación”. Esta se generará con las líneas de la Solicitud de Cotización en cuestión, tomando la Respuesta de Cotización seleccionada como “Ganador Seleccionado” para definir los campos *Precio* según el definido en el campo “Precio Factura” y como “Socio del Negocio de Entrega Directa” al Proveedor de la misma.

Luego de generarla desde el proceso ubicado en el botón “Crear Orden de Venta”. Se podrá navegar a la misma desde el campo “Orden de Venta” existente al lado del botón.

Al Completar la Orden de Venta luego de la aprobación del Cliente, automáticamente se generará la Orden de Compra Enlazada según Entrega Directa.

### Orden de Venta con Margen

En caso de contar con “% de Margen” (Mark-Up), el precio real enviado por la Cotización se definirá en la línea de la Orden de Compra. En caso de no existir “Mark-Up” los precios de la Orden de Venta y los precios de la Orden de Compra serán iguales.

### Nivel de Línea: Proyecto (Creativo Simple) / Primer Nivel

El Nivel Proyecto se deberá utilizar cuando la Campaña o Trabajo (Job) a realizar es simple. Esto quiere decir que el Proyecto tendrá directamente los “To-Do” a realizar, sin contar con ningún nivel o agrupación intermedia.

* Proyecto
  * “To-Do” (Solicitud)
  * “To-Do” (Solicitud)
  * “To-Do” (Solicitud)

### Nivel de Línea: Fase (Campaña Multimedia) / Segundo Nivel

La Fase es el segundo nivel del Proyecto. Se deberá utilizar en los siguientes casos:

Cuando una Campaña cuente con diferentes “Materiales” se deberá definir el nivel de Fases con el fin de contar con una Fase por cada Material de la Campaña (Proyecto).

* Proyecto
  * Material 1 (FASE)
    * Solicitud (“To-Do”)
    * Solicitud (“To-Do”)
    * Solicitud (“To-Do”)
  * Material 2 (FASE)
    * Solicitud (“To-Do”)

![Nivel Fase](/assets/img/docs/project-management/prm-project3.png)

### Nivel de Línea: Tarea (Producción o Campaña Multimedia) / Tercer Nivel

El Nivel de Proyecto hasta TAREA agrega un nivel adicional (3er Nivel) al Proyecto antes de llegar a la definición de Solicitudes (To-Do).

Este nivel se utilizará por ejemplo cuando existan Fases de Producción, donde se deba realizar Cotizaciones de Proveedores.

En este caso los niveles serán clasificados de la siguiente manera:

FASE: se clasificará el trabajo “Creativo” y “Producción” tendrá dentro las Solicitudes de Creatividad a realizar.

TAREAS: Dentro de cada Fase se crearán las diferentes TAREAS a realizar. En el caso de Producción, se deberá crear una Tarea por Cada Cotización a realizar.

* Proyecto (Tipo de Proyecto: Creativo)
  * Material 1 (FASE)
    * TAREA 1
      * Solicitud (“To-Do”)
      * Solicitud (“To-Do”)
      * Solicitud (“To-Do”)
    * TAREA 2
      * Solicitud (“To-Do”)
      * Solicitud (“To-Do”)
  * Material 2 (FASE)
    * TAREA 2
      * Solicitud (“To-Do”)
      * Solicitud (“To-Do”)
* Proyecto (Tipo de Proyecto: Cotización)
  * Producción (FASE)
    * TAREA 1 (Tema a Cotizar)
    * TAREA 2 (Tema a Cotizar)
    * TAREA 3 (Tema a Cotizar)

### Miembros del Proyecto

En cada Proyecto se podrá agregar Miembros. Los Miembros del Proyecto serán todos aquellos usuarios, internos como externos que estén involucrados con el Proyecto.

Estos pueden ser definidos manualmente desde el botón “Crear Desde” ubicado en el cabezal del Proyecto, como también automáticamente.

Al crearle un Proyecto a un Cliente, automáticamente se definirá como Miembros del Proyecto a todos los usuarios que que dicho Cliente tenga asignados a su Cuenta.

La asignación de Miembros de una Cuenta se definirá dentro de la Ventana *Socio del Negocio*, Pestaña *Miembros por Defecto*.

\*Pestaña “Miembros por Defecto” en Ventana Socio del Negocio.

### Solicitudes del Proyecto

Dentro de cada Proyecto se podrá crear diferentes Solicitudes asociadas al mismo. La ventaja de generar las Solicitudes desde un Proyecto, Fase o Tarea es que tomará del contexto toda la información que necesite, como Proyecto, Cliente, etc.

Desde la ventana Proyecto se podrá visualizar todas las Solicitudes relacionadas, tanto desde la Pestaña de Solicitudes correspondiente como desde la Barra de herramientas (Ver todas las solicitudes).

## Proyecto Pestaña Solicitudes de Fase

### Solicitud (To-Do)

Una Solicitud refiere a una Tarea específica (To-Do) que tiene determinado *Asunto*, *Descripción* y está *Asignado A* un Usuario con determinada *Fecha de Siguiente Acción* y *Fecha de Fin*.

Esta Solicitud a su vez, puede estar vinculada a diferentes documentos a lo largo del sistema, como por ejemplo un Proyecto, un Cliente, una Orden de Venta, una Factura, una Marca, un Sello, etc.

Dentro de una Solicitud se podrá agregar *Comentarios* y modificar el “*Asignado A”* o el *Estado* de la misma a medida que avanza el desarrollo de la misma. Cada Solicitud se podrá visualizar el histórico de Actualizaciones que la misma tuvo desde la pestaña de *“Actualizaciones”* detallando la Fecha-Hora, Usuario, Comentario así como demás cambios en los campos que fue realizando.

Cada Actualización que se realice sobre la Solicitud, el sistema estará enviando automáticamente notificaciones a cada usuario que esté vinculado a la misma. El tipo de Notificación a enviar dependerá de la Configuración de Notificaciones que cada usuario tenga definida (e-mail o aviso interno).

para ver más en detalle sobre las notificaciones ver “Notificaciones del Sistema”.

### Tipo de Proyecto

El sistema brinda diferentes “Plantillas” donde se puede definir una estructura Tipo en la cual basarse para crear un Proyecto. Esta puede utilizarse o no, según desee el usuario. La principal ventaja sería la creación automática de Fases o Tareas según el Tipo de Proyecto seleccionado ahorrando a uno crearlas manualmente. Principalmente es útil para los Proyectos donde existan cotizaciones.

Dentro de los diferentes Tipos de proyecto encontramos:

* **Creativo:** Estructura más simple, al seleccionarlo no se crean ninguna Fase ni Tarea por defecto. Simplemente define un conjunto de Estados de Proyecto así como también categoriza el proyecto en cuestión.
* **Creativo + Cotización:** Utilizado cuando existe Creatividad y Cotización. Crea una Fase para cada una. Se necesita nivel de Proyecto “Tarea”
* **Cotización:** Utilizado cuando es sólo para realizar una Cotización al Cliente. Crea una Fase de Cotización. Se necesita nivel de Proyecto “Tarea”

### Orden de Venta desde Proyecto

En cada Proyecto, cuando un trabajo deba ser facturado al Cliente, se deberá generar una Orden de Venta vinculada al mismo.

Para generar una Orden de Venta desde un Proyecto, se deberá definir en la Línea del Proyecto:

* el Producto/Servicio
* el Precio
* la Cantidad
* una Descripción

La ubicación de la Pestaña de “Línea” dependerá del *Nivel de Línea* seleccionado en el Proyecto, desplegando según corresponda Línea del Proyecto, Línea de la Fase o Línea de la Tarea.

Una vez definido el *Producto/Servicio* en la Línea que corresponda, se deberá generar una Orden de Venta desde el Botón “Generar Orden” ubicado en el Cabezal del Proyecto, en el Grupo de Campos “Acción”. La misma será generada tomando toda la información que se haya definido en las Líneas.

Las Órdenes de Venta generadas desde un Proyecto se pueden visualizar de diferentes maneras.

### Vista de la Orden de Venta desde la Pestaña del Proyecto

Una opción es desde la pestaña de “Orden de Venta” def