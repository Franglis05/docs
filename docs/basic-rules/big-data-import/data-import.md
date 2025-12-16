---
title: Carga Masiva de Datos
category: Documentation
star: 9
sticky: 9
article: false
---

La Carga Masiva de Datos es una funcionalidad que permite importar al sistema lotes de registros en simultáneo, partiendo desde un formato de importación de datos donde se definen las columnas/datos. En base a ese formato se crea una planilla con el mismo orden de los datos concatenados definidos en el formato. Un cargador de archivo mediante el cual se suben los registros al sistema en una tabla intermedia y finalmente un importador que guarda en tabla definitiva los registros importados.

## Carga Masiva: Presupuesto Contable

La aplicación gestiona diferentes tipos de contabilidad:

* La contabilidad actual (legal) de reportes fiscales.
* La contabilidad presupuestal con características de la contabilidad actual pero a nivel de presupuesto.
* Y la contabilidad de compromiso que se gestiona en las órdenes tanto de venta como de compra.

Se trata de los compromisos que se van adquiriendo en el transcurrir del tiempo con diferentes socios del negocio.

Esta última contabilidad genera controles a través del ordenado brindando información de la operatoria de la organización ayudando en la toma de decisiones.

La contabilidad de compromiso no es parte aún de nuestra contabilidad actual, sino que se encuentra en expectativa. Aún así, nos brinda alertas para poder visualizar desvíos entre lo comprometido y lo presupuestado por ejemplo.

### Primer paso: Definir Formato de importación

La contabilidad presupuestal se carga desde un formato de importación predeterminado seguido de una carga de archivo.

El formato se define en la opción **formato de importación de datos**.

Se configura campo por campo la condición y tipo de dato de cada variable con un orden cronológico que se corresponde con la secuencia de datos concatenados del archivo a importar.

Datos importantes a mencionar son la actividad (o centro costos), socio de negocio, producto, agente comercial, edificio (o campaña) y una cuenta contable sobre la cual se carga el presupuesto.

Luego de esos primeros datos en el formato del archivo se pueden visualizar los importes mes por mes.

Una vez definidas todas las variables se guarda archivo en formato CVS.

Posteriormente en la aplicación se procede a generar la carga desde la opción cargador de archivos.

### Segundo Paso: Cargar Archivo en Ventana Cargador de Archivo

Seleccionamos importar presupuesto (en formato de importación),  configuramos UTF-8 como formato de codificación de caracteres. Elegimos cargar el archivo y a partir de ese momento podremos visualizar los datos de los registros. Esto permite controlar que cada dato se visualice en el campo correcto antes de realizar la importación.

![Ventana Cargador de Archivo](/assets/img/docs/basic-rules/bar-data-import1.png)

El presupuesto genera un asiento que balancea con una cuenta presupuestal (no afecta la contabilidad actual ni de compromiso).

### Tercer Paso: Importar Presupuesto

En la opción de importar presupuesto se procederá a la importación del archivo cargado previamente (permite buscar por filtro importado = No).

Se elige el lote y por defecto se poblará el esquema de cuentas (se definen los datos de la carga).

En la ventana emergente de importación de presupuesto se debe setear la fecha contable (en el caso de ser una carga anual seleccionamos el 1 de enero). Luego ingresamos el número de periodos (anual=12 meses), seteamos la organización, una descripción para el lote de ingreso manual y estado en el cual deseamos crear el Lote (borrador).

![Ventana Importación de Presupuesto](/assets/img/docs/basic-rules/bar-data-import2.png)

Al confirmar importación podremos visualizar un lote de nota contable que se refleja en el diario contable.

### Cuarto Paso: Consultar Asiento 

En la opción de asiento de presupuesto podremos identificar el presupuesto importado en 12 asientos (uno por cada mes) y cada asiento a su vez presentará tantas líneas como cuentas contables posea con su respectivo movimiento (positivo o negativo).

Los asientos de presupuesto por una cuestión interna de la aplicación quedarán generados únicamente al tipo de documento "gl journal" (el asiento en lote).

Una vez cargado el presupuesto en la contabilidad, nos habilita la posibilidad de generar informes financieros (opción informe financiero) seleccionando por periodos.

Esto genera un reporte (informe) constituyendo diferentes columnas: actual (contabilidad), una columna de presupuesto y otra columna que realiza una resta entre ambas columnas (actual y presupuesto) determinando cuánto se ha consumido en la contabilidad actual de lo presupuestado (columna: disponible).

Es una herramienta útil de control para identificar desvíos entre lo presupuestado y la realidad.

![Ventana Cargador de Archivo](/assets/img/docs/basic-rules/bar-data-import3.mp4)

## Carga Masiva: Asiento Diario

El asiento diario se carga desde un formato de importación predeterminado seguido de una carga de archivo.

El formato se define en la opción formato de importación de datos.

Se configura campo por campo la condición y tipo de dato de cada variable con un orden cronológico que se corresponde con la secuencia de datos concatenados del archivo a importar.

En la aplicación se procede a generar la carga desde la opción cargador de archivos.

Seleccionamos importar asiento diario (en formato de importación),  configuramos UTF-8 como formato de codificación de caracteres. Elegimos cargar el archivo y a partir de ese momento podremos visualizar los datos de los registros. Esto permite controlar que cada dato se visualice en el campo correcto antes de realizar la importación.

En la opción de importar diario contable se procederá a la importación del archivo cargado previamente (permite buscar por filtro importado = No).

Se podrá visualizar el asiento diario en lote cargado (desde cargador de archivo). Pueden validarse los datos cargados de cada registro antes de realizar importación.

En el extremo inferior derecho se selecciona el botón de acción Importar diario contable.

Esto abre una ventana emergente donde se deberán ingresar datos básicos como Organización, Compañía, Esquema Contable, fecha contable y cuenta con tres opciones tipo check para seleccionar según lo que se requiera hacer: solo validar datos, solo importar si no hay errores y borrar viejos registros importados.

Una vez importado desde la opción Diario contable es posible visualizar el asiento importado en lote y sus líneas con la posibilidad de completar el asiento.