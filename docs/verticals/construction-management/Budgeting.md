---
title: 1. Presupuestación
category: Documentation
star: 9
sticky: 9
article: false
---

La presupuestación desde un proyecto de Constructora es una herramienta clave para gestionar y planificar los recursos financieros, materiales, y humanos necesarios para la ejecución de un proyecto de construcción. El objetivo principal de esta función es proporcionar un control exhaustivo sobre los costos asociados al proyecto, garantizando que se mantengan dentro del presupuesto previsto y facilitando la toma de decisiones informadas durante todo el proceso.

La presupuestación es el proceso de estimar los costos que se esperan durante las diversas etapas de un proyecto de construcción. Dentro de un sistema ERP, la presupuestación permite:

* Definir y asignar recursos (materiales, mano de obra, equipos) y estimar sus costos.
* Establecer los límites financieros para cada fase o tarea del proyecto.
* Llevar un control y seguimiento continuo de las desviaciones entre el presupuesto inicial y los costos reales durante la ejecución.

## Generar Proyecto de Constructora

El proyecto de constructora es un módulo o conjunto de funcionalidades diseñado específicamente para gestionar y controlar todos los aspectos de un proyecto de construcción.

Integra múltiples áreas clave como la planificación, presupuestación, recursos humanos, inventario, compras, ventas, y finanzas, todo relacionado con el ciclo de vida de un proyecto de construcción.

Es la representación detallada de todos los elementos y actividades necesarias para llevar a cabo un proyecto de construcción, desde su planificación inicial hasta su ejecución y cierre. El ERP permite centralizar la información de cada proyecto en un solo sistema, permitiendo la gestión y seguimiento de aspectos como:

* Presupuesto del proyecto.
* Planificación de recursos (materiales, mano de obra, maquinaria).
* Control de costos y flujo de caja.
* Cronogramas y plazos.
* Inventario y aprovisionamiento de materiales.
* Facturación y cobros.
* El ERP organiza y almacena toda la información relevante del proyecto y la hace accesible en tiempo real a las diferentes áreas involucradas (ingeniería, compras, finanzas, logística, etc.).

El Proyecto de Constructora es, en la práctica, una presupuestación sobre un determinado plan de obra que puede contener diversas "Fases", donde case estará compuesta por un determinado universo de productos.

Se trata de una unidad de gestión que agrupa un conjunto de entidades que le dan forma y describen un determinado Servicio.

El primer paso para la creación de un Proyecto de Constructora es ingresar en la ventana el nombre del cliente (Socio del negocio del cual hereda la dirección, lista de precio y el almacén), la fecha de inicio del servicio a realizar y seleccionar una categoría de Proyecto (y la unidad o departamento). En este paso solo se genera el evento (no se asignan recursos o productos).

![Proyecto](/assets/img/docs/construction-management/com-image1.png)

### Generar Fase y Líneas de fase de proyecto

A partir del proyecto (cabezal) creado se generan las diferentes Fases del proyecto.

Las fases se dividen de acuerdo a los distintos segmentos (o universos) de productos que son determinadas características que poseen los productos .

En las fases se crean las líneas de proyecto listando los productos necesarios por cada fase con sus correspondientes cantidades.

Para lograr un circuito óptimo y eficiente de selección de productos en las líneas, es posible utilizar un proceso denominado "**Agregar Productos a Fase de Proyecto**". Este SB permite seleccionar los productos a través de parámetros para agilizar la selección y definición en las fases.

El Navegador *Agregar Productos a Fase de Proyecto* se ejecuta desde el cabezal del proyecto, y permite seleccionar productos (sólo productos "Activos"), y para cada uno definir una cantidad.

Al procesar, se debe seleccionar la Fase, y se crea una línea de fase de proyecto por cada línea de producto seleccionada en el SB, donde cada línea tendrá los datos siguientes:

* Producto
* Cantidad Planeada
* Precio Planeado (si se encontró precio en la versión lista de precios del proyecto)

![Agregar Productos a Fase de Proyecto](/assets/img/docs/construction-management/com-image8.png)

Cada producto tiene definido un determinado "Tipo de costo" (ejemplo: tipo de costo Herramientas).

Este tipo de costo define un costo para el producto en particular y ese costo multiplicado por la cantidad que se encuentre definido en la línea de la fase del proyecto será el que se muestre como importe costo de la línea del proyecto.

![Fase y línea](/assets/img/docs/construction-management/com-image2.png)

### Dimensionar Mano de Obra

En el producto es posible definir los parámetros de Unidad de duración y duración.

Determinando estas dos entidades y de acuerdo a la unidad de medida (y cantidad) es posible establecer la cantidad de mano de obra estimada que se necesitará por cada línea (y fase).

Esta función propone un cálculo eficiente (aproximado) de la cantidad de recursos (mano de obra) necesaria para un determinado proyecto).

Cuando el producto no tiene definida una lista de materiales (LDM), estos campos (Duración y Unidad de Duración) se pueden modificar manualmente.

Cuando el producto tiene definida una LDM (check 'Lista de Materiales' está marcado), estos campos se muestran como sólo lectura y no se pueden modificar manualmente. En este caso se van a definir automáticamente, según la sumatoria de las duraciones de los productos que estén definidos en las lineas de la LDM.

El sistema dispara las verificaciones para actualizar la duración de los productos que contengan al producto modificado en su LDM.

Estas verificaciones se ejecutan cuando se realizan las acciones siguientes:

* Se crea un producto o se modifica uno existente
* Se crea o se borra una línea de la lista de materiales de un producto