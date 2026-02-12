---
title: Ventas Netas por Grupo de Producto
category: Documentation
star: 9
sticky: 9
article: false
---

# Ventas Netas por Grupo de Producto

## Descripción

El dashboard **Ventas Netas por Grupo de Producto** presenta el importe total de ventas facturadas considerando las devoluciones (notas de crédito) como negativas, desglosado por cada grupo de producto. Los valores se expresan en la moneda de reporte de la organización.

Este dashboard permite analizar las ventas a un nivel de detalle intermedio entre la categoría de producto y el producto individual, identificando qué grupos concentran el mayor volumen comercial. Los productos que no tienen un grupo asignado se agrupan bajo la etiqueta "Sin Grupo".

## ¿Cuándo se utiliza?

Se utiliza cuando la gerencia comercial necesita:
- Analizar el desempeño de ventas a nivel de grupo de producto.
- Identificar los grupos con mayor y menor contribución a las ventas totales.
- Detectar la proporción de productos sin grupo asignado en las ventas.
- Comparar la evolución mensual de ventas entre los diferentes grupos.

## Acceso

Dashboards → Ventas → Ventas Netas por Grupo de Producto

**Rol requerido:** Gerente de Ventas

## Vista general

El dashboard muestra un indicador numérico con el total acumulado de ventas netas y un gráfico de barras agrupadas por mes, donde cada color representa un grupo de producto diferente. En la parte superior del gráfico se presenta una leyenda con el nombre de cada grupo y su color correspondiente.

![Dashboard de Ventas Netas por Grupo de Producto en vista de barras](/assets/img/docs/dashboards/ventas-netas-por-grupo-producto-barras.png)

En la parte superior se presenta:
- **Título:** Ventas Netas por Grupo de Producto
- **Subtítulo:** Ventas netas por grupo producto mon. reporte
- **Indicador principal:** valor total acumulado del período consultado (ej. $44,427,914)
- **Leyenda:** listado de grupos de producto con su color asignado

En la esquina superior derecha se encuentran las opciones para cambiar la vista:
- Vista de tabla
- Selector de tipo de gráfica (Barras por defecto)

En la esquina superior izquierda se encuentra el [filtro de fechas](./#filtro-de-fechas) que permite definir el rango de consulta. Este filtro es común a todos los dashboards.

## Tipo de gráfica

- **Tipo:** Barras agrupadas
- **Eje Y:** Importe en moneda de reporte ($)
- **Eje X:** Período temporal (meses)
- **Colores:** cada grupo de producto se representa con un color distinto en la leyenda

## Datos de ejemplo

La siguiente tabla muestra el resumen de los 15 grupos de producto con mayor volumen de ventas netas en el período consultado:

| Grupo de Producto | Ventas Netas ($) |
|-------------------|-----------------|
| Sin Grupo | 10,119,778.97 |
| FRIO | 3,253,706.99 |
| VENTILADOR DE TECHO | 2,722,784.54 |
| VENTILADORES DE PIE | 2,157,207.37 |
| LICUADORAS | 1,572,446.98 |
| OTROS VARIOS | 1,510,172.76 |
| VENTILADORES TURBO | 1,491,434.53 |
| CALENTADORES DE ALIMENTOS | 1,437,541.10 |
| JUEGOS VARIOS | 1,165,033.71 |
| CEPILLOS PARA CABELLOS | 937,497.12 |
| JUEGOS DE MESA EN CAJA | 887,419.61 |
| BICICLETAS | 867,822.95 |
| PROCESADORES DE ALIMENTOS | 833,737.50 |
| MUÑECAS, BELLEZA | 719,007.37 |
| MUÑECOS | 666,291.95 |
| Otros (74 grupos) | 14,086,031.02 |
| **Total** | **44,427,914.47** |

En este ejemplo se observa que el grupo **Sin Grupo** concentra la mayor proporción de ventas ($10.1M), lo cual indica que una parte significativa de los productos no tiene un grupo asignado. Los grupos de electrodomésticos (FRIO, VENTILADOR DE TECHO, VENTILADORES DE PIE, LICUADORAS) también representan un volumen importante. En total, el dashboard desglosa las ventas en **89 grupos de producto** diferentes.

## Consideraciones importantes

- Los valores se expresan siempre en la **moneda de reporte** de la organización.
- Las **notas de crédito** se descuentan del total de cada grupo.
- Los productos que no tienen un grupo asignado aparecen agrupados bajo la etiqueta **"Sin Grupo"**.
- Dado que este dashboard puede presentar una gran cantidad de grupos (89 en el ejemplo), la leyenda de colores puede resultar extensa. Se recomienda utilizar la vista de tabla para analizar los datos con mayor detalle.
- Este dashboard es una variante de [Ventas Netas](./ventas-netas) desglosada por la dimensión **Grupo de Producto**.
