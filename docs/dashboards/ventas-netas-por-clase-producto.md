---
title: Ventas Netas por Clase de Producto
category: Documentation
star: 9
sticky: 9
article: false
---

# Ventas Netas por Clase de Producto

## Descripción

El dashboard **Ventas Netas por Clase de Producto** presenta el importe total de ventas facturadas considerando las devoluciones (notas de crédito) como negativas, desglosado por cada clase de producto (marca o línea comercial). Los valores se expresan en la moneda de reporte de la organización.

Este dashboard permite analizar las ventas según la clasificación comercial de los productos, identificando qué marcas o clases concentran el mayor volumen de ventas. Los productos que no tienen una clase asignada se agrupan bajo la etiqueta "Sin Clase".

## ¿Cuándo se utiliza?

Se utiliza cuando la gerencia comercial necesita:
- Evaluar el desempeño de ventas por marca o clase de producto.
- Identificar las clases con mayor y menor contribución a las ventas totales.
- Detectar la proporción de productos sin clase asignada en las ventas.
- Comparar la evolución mensual de ventas entre las diferentes clases.

## Acceso

Dashboards → Ventas → Ventas Netas por Clase de Producto

**Rol requerido:** Gerente de Ventas

## Vista general

El dashboard muestra un indicador numérico con el total acumulado de ventas netas y un gráfico de barras agrupadas por mes, donde cada color representa una clase de producto diferente. En la parte superior del gráfico se presenta una leyenda con el nombre de cada clase y su color correspondiente.

![Dashboard de Ventas Netas por Clase de Producto en vista de barras](/assets/img/docs/dashboards/ventas-netas-por-clase-producto-barras.png)

En la parte superior se presenta:
- **Título:** Ventas Netas por Clase de Producto
- **Subtítulo:** Ventas netas por clase producto mon. reporte
- **Indicador principal:** valor total acumulado del período consultado (ej. $44,427,914)
- **Leyenda:** listado de clases de producto con su color asignado

En la esquina superior derecha se encuentran las opciones para cambiar la vista:
- Vista de tabla
- Selector de tipo de gráfica (Barras por defecto)

En la esquina superior izquierda se encuentra el [filtro de fechas](./#filtro-de-fechas) que permite definir el rango de consulta. Este filtro es común a todos los dashboards.

## Tipo de gráfica

- **Tipo:** Barras agrupadas
- **Eje Y:** Importe en moneda de reporte ($)
- **Eje X:** Período temporal (meses)
- **Colores:** cada clase de producto se representa con un color distinto en la leyenda

## Datos de ejemplo

La siguiente tabla muestra el resumen de ventas netas por clase de producto en el período consultado:

| Clase de Producto | Ventas Netas ($) |
|-------------------|-----------------|
| Sin Clase | 24,656,234.38 |
| MARCA PROPIA | 15,973,132.23 |
| NATHOR | 817,698.42 |
| MOLTEN | 773,739.64 |
| HUANGER | 717,653.86 |
| Classic World | 582,143.85 |
| Janod | 230,667.57 |
| KIDDIELAND | 195,486.72 |
| MAJORETTE | 106,864.40 |
| INFANTI | 83,467.48 |
| PLAYMOBIL | 79,138.65 |
| FISHER PRICE | 53,509.62 |
| Otras (14 clases) | 158,177.65 |
| **Total** | **44,427,914.47** |

El desglose mensual de las principales clases es el siguiente:

| Clase | 2025-10 | 2025-11 | 2025-12 |
|-------|---------|---------|---------|
| Sin Clase | 13,661,086.04 | 10,558,824.97 | 436,323.37 |
| MARCA PROPIA | 8,371,475.11 | 7,285,160.00 | 316,497.12 |
| NATHOR | 153,717.73 | 588,070.55 | 75,910.14 |
| MOLTEN | 62,295.00 | 709,182.89 | 2,261.75 |
| HUANGER | 348,960.76 | 359,557.04 | 9,136.06 |

En este ejemplo se observa que **Sin Clase** y **MARCA PROPIA** dominan ampliamente las ventas, representando juntas más del 91% del total. Esto indica que la mayoría de los productos vendidos no tienen una clase (marca) asignada o corresponden a productos de marca propia. En total, el dashboard desglosa las ventas en **26 clases** diferentes.

## Consideraciones importantes

- Los valores se expresan siempre en la **moneda de reporte** de la organización.
- Las **notas de crédito** se descuentan del total de cada clase. Una clase puede presentar un saldo negativo si las devoluciones superan las ventas en el período consultado.
- Los productos que no tienen una clase asignada aparecen agrupados bajo la etiqueta **"Sin Clase"**.
- Este dashboard es una variante de [Ventas Netas](./ventas-netas) desglosada por la dimensión **Clase de Producto**.
