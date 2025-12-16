---
title: Personalización de Reportes
category: Documentation
star: 9
sticky: 9
article: false
---

Los reportes cuentan con una forma de parametrizarlos de acuerdo a la necesidad. Cuentan con una amplia flexibilidad para realizar cambios de visibilidad de columnas, de secuencia de visualización de las mismas, así como su nomenclatura, ordenamiento (order by), sumarización, etc.

## Elementos

 Solop ERP le permite cambiar los siguientes elementos de cada Reporte:

* Orden de Despliegue
* Criterio de Ordenamiento
* Formato
    Campo, Imagen, Texto, Formato de Impresión
     % de Alineación Ancho/Alto
    Calcular: Suma – Promedio – Cuenta 
    Agrupado por (Requiere Orden por  Clasificación)

![Elementos](/assets/img/docs/basic-rules/bar-report1.png)

1- Formato del Reporte
PDF
HTML
XLSX
2- Nombre de la Vista del Reporte: Si es copiado el nombre antecedente será el de la Organización
3- Trial Balance: No Usar 
4- Engranaje: Personalización del Reporte
5- Lupa: Mediante la lupa se pueden aplicar nuevos filtros para obtener un nuevo reporte. 
6- Exportar datos
7- Importar un nuevo Reporte (ARXML)
8- Refresca
9- Navegar al Registro
10- Resumen: Muestra sólo Sub-totales

## Formato de Impresión

![Formato](/assets/img/docs/basic-rules/bar-report2.png)

1- Copia el Reporte para utilizarlo de base en otro
2- Click si es el Reporte Predeterminado (abre primero)
3- Si está Activo (disponible) el Reporte

### Pestaña “Orden de Despliegue”

![Orden de Despliegue](/assets/img/docs/basic-rules/bar-report3.png)

1- Campos Disponible
2- Campos Seleccionados. Secuencia Seleccionada

Mediante esta pestaña se podrá definir cuales campos estarán visibles en la Vista en cuestión (Sección "Secuencia") o si estarán ocultos (Sección "Selecciones Disponibles"). 

A su vez también se podrá definir el Orden de Despliegue según la secuencia que se definan en la sección 2.

### Pestaña “Criterio de Ordenamiento”

En esta pestaña se determinará el Ordenamiento de los Datos brindados por el reporte. 
Se podrá definir el orden por múltiples campos. 
Para modificar un Ordenamiento existente, deben borrarse los campos de ordenamiento y comenzar nuevamente agregando los campos de a uno (para setear el nuevo criterio de ordenamiento). 
Si no se desea modificar el reporte, se debe borrar caché o ir probando a medida que se va agregando campos de Ordenamiento.  

### Pestaña “Elemento de Formato”

![Elemento de Formato](/assets/img/docs/basic-rules/bar-report4.png)

**Campos**

Nombre
Nombre a ser Impreso
Activo
Mantenido Centralmente
Suprimir Nulos
Tipo de Formato
Columna
Patrón Formato
Tipo Código de Barras
Próxima Línea

![Cálculos](/assets/img/docs/basic-rules/bar-report5.png)

**Cálculos:** 

* Ordenar por (cuando los campos se definen como Criterio de Ordenamiento se definirá automáticamente el check en Y). Y viceversa, cuando se clickea Y se define como Criterio de Ordenamiento.
Solo cuando se define el campo “Ordenar Por”= Y aparecen los siguientes campos:

    * Descending: Para ordenar de manera descendente. Por defecto siempre ordena ascendentemente. 
    * Agrupar Por: Este campo es utilizado para poder realizar Sub-Totales dentro de los datos del reporte. Si se define en “Y” se realizará un corte cada vez que se cambie a un nuevo Registro en los datos presentados, dejando todos los que sean iguales “Agrupados”. Para lograr que se aplique la agrupación se deberá definir además al menos una columna como “Calcular Sumatoria”.
    * Corte de Página: este campo sirve para que además del corte que se realiza al cambiar el registro se definirá los siguientes en una Nueva Página quedando siempre 1 Registro por Hoja. 

* Calcular Sumatoria: El Cálculo de Sumatoria se aplica sobre toda “Agrupación” de Campos. Esta agrupación puede ser por el total de los Registros, o si se definió algún “Agrupar Por” también sumariza por dicha agrupación. 
* Calcular Conteo: El Cálculo de Conteo sumariza el número de elementos "no vacíos".
* Calcular mínimo: Calcula el "monto mínimo".
* Calcular Promedio: Calcula promedio de contenido numérico o longitud.
* Calcular Máximo: Calcula el "monto máximo".
* Calcular Varianza: Calcula varianza.
* Calcular Desviación: Calcula desviación.
