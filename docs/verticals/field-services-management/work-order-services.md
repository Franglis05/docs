---
title: 1b. Órdenes de Trabajo Services
category: Documentation
star: 9
sticky: 9
article: false
---

## 🔧 Circuito de Gestión de Orden de Trabajo (Productos de Service)

Este circuito permite registrar de forma completa la recepción de productos de service traídos por un cliente, generando automáticamente una orden de trabajo con todos los datos necesarios para su seguimiento.

### 📝 Paso 1: Creación de Orden de Trabajo

Desde la ventana Orden de Trabajo, se inicia el flujo creando un nuevo registro.

Se utiliza este formulario cuando llega un cliente con un producto para reparar.

En esta instancia puede:

* Buscar un Socio del Negocio existente.

* O crear uno nuevo desde el mismo campo.

### 👤 Paso 2: Registro del Socio del Negocio (si es necesario)

Si el cliente no está registrado previamente, se puede crear en el momento:

* Completar el campo Tipo de documento (Ej: Cédula).

* Ingresar nombre (Ej: Pablo Pérez Demo).

* Agregar dirección si se desea, especialmente útil para la facturación.

* Confirmar para generar el nuevo Socio del Negocio.

###v📦 Paso 3: Datos del Producto Recibido

Una vez definido el Socio del Negocio, se completan los datos del producto:

* Fecha de recepción.

* Descripción del problema según lo informado por el cliente (Ej: “Sale humo del motor”).

* Producto: puede buscarse por código o nombre. Para facilitar la búsqueda:

1. Usar filtros por categoría (Ej: Electrodomésticos).

2. Número de factura: si no lo tiene, indicar “No tiene”.

3. Categoría del proyecto o tipo de trabajo (opcional).

Guardar los datos una vez completados.

### 🧾 Paso 4: Información adicional

Lista de precios: será necesaria más adelante al definir los valores de la venta. (Se detalla en el siguiente módulo).

“Atendido por”: permite dejar registro del usuario que realizó la atención.

Seleccionar la dirección del Socio del Negocio (si aplica).

### 📋 Paso 5: Constancia de Recepción

Con los datos anteriores ya definidos, se puede generar la constancia de recepción del producto.

Ingresar comentarios u observaciones si se desea.

Definir cantidad (por defecto es 1).

Revisar la fecha y el nombre del usuario que recepcionó el producto (se toma automáticamente el usuario activo).

### ✅ Resultado

Al finalizar estos pasos se genera correctamente una orden de trabajo con su constancia de recepción, quedando lista para su gestión técnica y posterior facturación.

## 🔍 Seguimiento y Análisis de la Orden de Trabajo

Luego de la recepción del producto, se puede avanzar en el circuito para realizar el análisis técnico, generar cotización y crear tareas o solicitudes internas para gestionar la reparación.

### 🧭 Estado de la Orden de Trabajo

Las órdenes de trabajo pueden pasar por distintos estados según el avance del proceso:

* Recibido

* En reparación

* En análisis o cotización

* En autorización

* Pronto para retirar

📌 Estos estados son editables por la empresa y pueden adaptarse a su lógica de trabajo.

### 🧰 Análisis técnico y cotización

Una vez que el producto fue recibido:

* Cambiar el estado a “En análisis” o “En cotización” (según preferencia).

* Se puede agregar una línea de orden de trabajo con el producto o servicio a realizar.

* Alternativamente, se puede gestionar como una tarea desde la pestaña “Solicitudes y Reparación”:

#### Crear una nueva solicitud de trabajo.

1. Indicar el producto asociado.

2. Asignar la tarea a un técnico o usuario responsable.

3. Definir una fecha de finalización estimada.

Esta solicitud puede luego visualizarse desde la agenda del usuario asignado, facilitando la gestión del tiempo y el trabajo.

### 🧾 Consulta de la Lista de Materiales (BOM)

Para conocer los componentes del producto:

* Ir a la ventana Lista de Materiales.

* Buscar el producto por código (ej: 72690).

Desde allí se puede visualizar:

El producto padre (encabezado).

Los componentes necesarios para su armado o reparación.

Las versiones disponibles de la lista de materiales.

También es posible consultar la lista desde la ficha del producto, aunque se recomienda acceder directamente desde la ventana específica de materiales para mayor claridad.

### 💲 Agregado de Servicios o Repuestos

Desde la orden de trabajo, se pueden agregar líneas con los productos o servicios involucrados en la reparación:

* Seleccionar los repuestos desde la lista de precios de venta de servicios (ejemplo: Venta a Service).

* Buscar por código los productos requeridos (por ejemplo, el repuesto 72690).

* Ingresar cantidad a utilizar.

* Ingresar el precio manualmente o tomarlo desde la lista de precios asociada.

Ejemplo: Precio planeado: 300 | Precio final: 700

También se pueden agregar otros ítems como mano de obra si se encuentran en la lista de precios correspondiente.

### 🛠️ Finalización de la cotización

Una vez que se han definido todos los ítems y costos:

1. Cambiar el estado a “En cotización”.

2. Revisar toda la información cargada.

Si está todo validado, hacer clic en “Generar Orden” para continuar el proceso.