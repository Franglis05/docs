---
title: Componentes
category: Documentation
star: 9
sticky: 9
article: false
---

Los Componentes en Solop ERP son aquellos que representan carpetas, ventanas, reportes, procesos y navegadores. A continuación se definen y visualizan cada uno de ellos.

## Ventanas

Las ventanas se encuentran representadas por el Icono de una Ventana en el menú de Solop ERP. De igual manera, cada ventana que contempla Solop ERP, representa la interfaz de usuario, mostrando la salida y permitiendo la entrada de datos para uno o varios procesos que se ejecutan.

**Para más información sobre Campos de Ventanas:** - [Interfaz de Usuario](user-interface)


![Ejemplo de una Ventana](/assets/img/docs/basic-rules/bar-icons-windows1.png)

**Las Ventanas poseen dos formas de visualización:**

Una visual de grilla o multi registro que permite visualizar una cantidad determinada de documentos (según la paginación seleccionada) con sus diferentes campos ordenados tipo columna (las mismas pueden agregarse, ocultarse o cambiar su orden).

![Ejemplo de una Ventana](/assets/img/docs/basic-rules/bar-icons-windows2.png)

Una visual de documento individual o mono registro que posibilita consultar un documento específico con sus diferentes datos o campos (los cuales se pueden agregar, ocultar o cambiar su orden en la ventana).

A su vez, esta forma de visualización permite navegar entre las diferentes pestañas del registro (cada pestaña con sus campos correspondientes y con la misma variantes de mono registro o multi registro).

![Ejemplo de una Ventana](/assets/img/docs/basic-rules/bar-icons-windows3.png)

::: info 
Para realizar el cambio de visualización utilizamos el botón Multi registro o mono registro (dependiendo de la visual actual de la ventana) del extremo superior izquierdo.
:::

### Barra de Herramientas

En Solop ERP contamos con una barra de herramientas la cual contiene una serie de opciones que realizan determinadas funciones. La barra de herramientas que a continuación será definida se encuentra ubicada en la ventana estándar de Solop ERP.

Uno de los navegadores inteligentes que contempla Solop ERP es el siguiente:

![Barra de Herramientas de Solop ERP en Ventana Estándar](/assets/img/docs/basic-rules/bar-tools1.png)

Imagen 1. Barra de Herramientas de Solop ERP en Ventana Estándar

A continuación se define la operatividad de dicha barra de herramientas.

* Multiregistro: permite visualizar múltiples registros de acuerdo a la paginación (en pie de ventana) y la opción de "Cambiar a Mono", que hace posible visualizar mono registro.

* Flechas (ascendente y descendente): permite navegar entre los diferentes registros (cuando se encuentra en mono registro).

* Nuevo: Habilita a generar un nuevo registro con sus dos variantes (desplegables desde la flecha del botón): Nuevo Registro o Copiar Registro.

* Refrescar: actualiza la ventana en la que se encuentra.

* Anular: Es un cotrol que permite el cambio de estado del documento consultado. Su nombre irá cambiando dependiendo del estado actual del documento (mostrando la próxima posible acción). Por ejemplo, cuando se encuentra el documento en estado borrador, mostrará el botón el nombre "Completo". En este caso al estar Completo, muestra el nombre Anular.

* Completo: este botón describe el estado del documento y al presionarlo es posible visualizar los diferentes estados que ha transitado el registro.

### Búsqueda de Registros

Cada ventana cuenta con funciones y accesos directos para una interacción y navegabilidad óptima:

![Búsqueda](/assets/img/docs/basic-rules/bar-icons-windows4.png)

**Búsqueda Individual**

* Buscar Registros: es un campo de búsqueda que permite ubicar un registro por alguna de sus características (por número, nombre, etc.). 

### Consulta Avanzada

A su vez permite abrir la búsqueda avanzada por diferentes filtros.
Esta búsqueda avanzada posee diferentes métodos de búsqueda por cada filtro (igual a, diferente a, no incluye, etc.) para lograr ubicar un registro determinado de manera ágil y eficiente.
La consulta avanzada presenta un campo que despliega en combo los diferentes filtros para agregarse u ocultarse de la búsqueda.
Cada filtro posee las siguientes opciones de búsqueda por cada entidad:

#### Igual a: 

Realizará la búsqueda que sea identico/s al dato ingresado.

#### Diferente a:

Realizará la búsqueda sobre registros que sean diferente al ingresado.

#### Tiene un valor:

Mostrará aquellos registros que posean un valor en el campo seleccionado.

#### No tiene un valor:

Mostrará aquellos registros que no posean un valor en el campo seleccionado.

#### Contiene: 

Mostrará aquellos registros que posean el valor ingresado (aunque sea una parte del registro, pueden ser letras o números).

#### No contiene:

Mostrará registros que no contengan el valor ingresado (aunque sea parte del registro, en letras o números).

![Ejemplo de una Ventana](/assets/img/docs/basic-rules/bar-icons-windows5.png)

Desde el botón con icono de "lupa" es posible desplegar la búsqueda avanzada. Dentro de la ventana emergente de búsqueda avanzada, el visor de filtros permite desplegar todos los filtros y agregar o quitar los que correspondan:

![Ejemplo de una Ventana](/assets/img/docs/basic-rules/bar-icons-windows100.png)

## Procesos desde Ventana

Este botón abre los diferentes procesos a ejecutar en el registro consultado (en este caso por ejemplo: Asignar pago cobro, enviar por mail, Impresión de CFE, exportar, compartir, etc.)

![Ejemplo de una Ventana](/assets/img/docs/basic-rules/bar-icons-windows7.png)

## Formato de Visualización

Este botón permite cambiar el formato de visualización de la ventana (por ejemplo: minimalista, mostrar campos por defecto, mostrar todos los campos, etc.).

![Ejemplo de una Ventana](/assets/img/docs/basic-rules/bar-icons-windows8.png)

#### Control de Campos

Es un elemento que permite agregar y quitar datos (campos) de la ventana. Cada campo/dato de la ventana se despliega en combo/lista y al tildar o destildarlos, los hace visible o los oculta.

![Control de Campos](/assets/img/docs/basic-rules/bar-icons-windows6.png)

## Pestañas Laterales

Este botón ubicado en el lateral derecho permite visualizar pestañas relacionadas con el registro (por ejemplo: histórico de cambios. documentos relacionados, adjuntos, notas, solicitudes, información contable, etc.).

**Información de Solapas**

#### Histórico de cambios: 

Permite visualizar la auditoría de cambios en el registro, con datos de fecha y hora, el usuario que realizó el cambio, así como el valor anterior y el valor nuevo.

![Elementos Relacionados](/assets/img/docs/basic-rules/bar-icons-windows9.png)

#### Documentos Relacionados: 

En esta pestaña se pueden consultar las diferentes entidades relacionadas al registro y navegar hacia ellas.

![Elementos Relacionados](/assets/img/docs/basic-rules/bar-icons-windows101.png)

#### Adjuntos: 

Permite consultar y descargar los diferentes archivos adjuntos al registro.

![Elementos Relacionados](/assets/img/docs/basic-rules/bar-icons-windows102.png)

#### Notas: 

En esta pestaña se pueden visualizar las notas generadas para el registro.

![Elementos Relacionados](/assets/img/docs/basic-rules/bar-icons-windows103.png)

#### Solicitudes: 

Es posible crear solicitudes o consultar solicitudes vinculadas al registro.

![Elementos Relacionados](/assets/img/docs/basic-rules/bar-icons-windows104.png)

#### Histórico de Flujo de Trabajo: 

Permite visualizar los diferentes estados que ha transitado el registro.

![Elementos Relacionados](/assets/img/docs/basic-rules/bar-icons-windows105.png)

#### Información Contable

Esta solapa permite visualizar el asiento que corresponde a la transacción del documento consultado, así como las cuentas intervinientes e importes.

#### Panel de Control

Esta solapa permite visualizar gráficas del registro consultado.

## Reportes

Los reportes se encuentran representados por el icono Icono de un Reporte en el menú de Solop ERP. Así mismo, permiten visualizar informes acerca de algún documento en específico, transacciones y procesos previamente ejecutados.
Los mismos cuentan con diferentes parámetros y criterios de búsqueda para obtener informes detallados y eficientes.

Uno de los reportes que permite generar Solop ERP es el siguiente:

![Ejemplo de un Reporte](/assets/img/docs/basic-rules/bar-icons-reports1.png)

### Procesos desde Reporte

Es posible ejecutar procesos desde el reporte generado:

![Ejemplo de un Reporte](/assets/img/docs/basic-rules/bar-icons-reports100.png)

**Opciones de Procesos**

* Generar: Permite generar archivo del reporte con extensión por defecto.
* Generar Como: Permite cambiar la extensión del archivo a generar.
* Cambiar Parámetros: Permite modificar los patrones de búsqueda del reporte.
* Limpiar Parámetros: Limpia los parámetros previamente seteados.
* Compartir Enlace: Comparte la ruta en el porta papeles.

### Configuración del Reporte

Esta solapa permite modificar tanto las Preferencias, como los parámetros del reporte (por ejemplo: en tipo de reporte permite modificar la extensión por defecto).

![Ejemplo de un Reporte](/assets/img/docs/basic-rules/bar-icons-reports101.png)

## Procesos

Los procesos se encuentran representados por el Icono de un Proceso en el menú de Solop ERP. Se le llama proceso al conjunto de operaciones al que se somete un documento para ser elaborado.
Los mismos cuentan con diferentes parámetros y criterios de búsqueda para ejecutar determinados procesos masivos sobre una determinada fracción de entidades.

Uno de los procesos que contempla Solop ERP es el siguiente:

![Ejemplo de un Proceso](/assets/img/docs/basic-rules/bar-icons-process1.png)

Desde el campo superior derecho se despliegan los diferentes filtros. Desde allí es posible habilitarlos u ocultarlos según corresponda de acuerdo a los parámetros que requieran aplicarse para obtener el resultado deseado en el proceso a generar:

![Ejemplo de un Proceso](/assets/img/docs/basic-rules/bar-icons-process100.png)

Una vez seteados los parámetros correspondientes, al seleccionar "Ejecutar" se genera el proceso (botón superior derecho). Posteriormente se muestran las entidades creadas.

![Ejemplo de un Proceso](/assets/img/docs/basic-rules/bar-icons-process101.png)

Imagen 4. Ejemplo de un Proceso

## Navegadores

Los navegadores se encuentran representados por el Icono de una Ventana en el menú de Solop ERP. Adicional a ello, permite realizar una búsqueda a partir de ciertos parámetros.

Uno de los navegadores que contempla Solop ERP es el siguiente:

![Ejemplo de un Navegador](/assets/img/docs/basic-rules/bar-icons-navigators1.png)

Imagen 5. Ejemplo de un Navegador

Desde el campo superior derecho se despliegan los diferentes filtros. Desde allí es posible habilitarlos u ocultarlos según corresponda de acuerdo a los parámetros que requieran aplicarse para obtener el resultado deseado:

![Ejemplo de un Navegador](/assets/img/docs/basic-rules/bar-icons-navigators100.png)

Una vez seteados los parámetros correspondientes, es posible seleccionar (de acuerdo a los parámetros fijados) un registro, varios o todos para de esta forma realizar la ejecución en forma individual (de cada registro) o masiva. 
Al seleccionar "Anular Conceptos" se genera el proceso (botón superior derecho). Posteriormente se muestran las entidades creadas.

![Ejemplo de un Navegador](/assets/img/docs/basic-rules/bar-icons-navigators101.png)
