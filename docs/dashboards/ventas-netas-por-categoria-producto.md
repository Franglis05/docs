---
title: Ventas Netas por Categoría de Producto
category: Documentation
star: 9
sticky: 9
article: false
---

# Ventas Netas por Categoría de Producto

## Descripción

El dashboard **Ventas Netas por Categoría de Producto** presenta el importe total de ventas facturadas considerando las devoluciones (notas de crédito) como negativas, desglosado por cada categoría de producto. Los valores se expresan en la moneda de reporte de la organización.

Este dashboard permite identificar cuáles categorías de producto concentran el mayor volumen de ventas y cómo se distribuyen a lo largo del tiempo.

## ¿Cuándo se utiliza?

Se utiliza cuando la gerencia comercial necesita:
- Evaluar el desempeño de ventas por línea o categoría de producto.
- Identificar las categorías con mayor y menor contribución a las ventas totales.
- Analizar la evolución mensual de ventas por categoría.
- Detectar categorías con saldo negativo por devoluciones o ajustes que superan las ventas.

## Acceso

Dashboards → Ventas → Ventas Netas por Categoría de Producto

**Rol requerido:** Gerente de Ventas

## Vista general

El dashboard muestra un indicador numérico con el total acumulado de ventas netas y un gráfico de barras agrupadas por mes, donde cada color representa una categoría de producto diferente. En la parte superior del gráfico se presenta una leyenda con el nombre de cada categoría y su color correspondiente.

![Dashboard de Ventas Netas por Categoría de Producto en vista de barras](/assets/img/docs/dashboards/ventas-netas-por-categoria-producto-barras.png)

En la parte superior se presenta:
- **Título:** Ventas Netas por Cat. Producto
- **Subtítulo:** Ventas netas por cat. producto mon. reporte
- **Indicador principal:** valor total acumulado del período consultado (ej. $44,427,914)
- **Leyenda:** listado de categorías de producto con su color asignado

En la esquina superior derecha se encuentran las opciones para cambiar la vista:
- Vista de tabla
- Selector de tipo de gráfica (Barras por defecto)

En la esquina superior izquierda se encuentra el [filtro de fechas](./#filtro-de-fechas) que permite definir el rango de consulta. Este filtro es común a todos los dashboards.

## Tipo de gráfica

- **Tipo:** Barras agrupadas
- **Eje Y:** Importe en moneda de reporte ($)
- **Eje X:** Período temporal (meses)
- **Colores:** cada categoría de producto se representa con un color distinto en la leyenda

## Datos de ejemplo

La siguiente tabla muestra el resumen de ventas netas por categoría de producto en el período consultado:

| Categoría | Ventas Netas ($) |
|-----------|-----------------|
| ELECTRODOMESTICOS | 22,417,860.64 |
| JUGUETES | 15,212,754.90 |
| RODADOS | 2,099,331.21 |
| PUERICULTURA | 1,947,570.51 |
| DEPORTES | 1,787,445.20 |
| BAZAR | 448,725.57 |
| PAPELERIA | 259,013.99 |
| LIBROS | 258,057.22 |
| REPUESTO | 207,045.87 |
| ESCOLARES | 98,656.37 |
| INSUMOS | 75,784.77 |
| MATERIAL DIDACTICO | 42,668.22 |
| SERVICIO | -427,000.00 |
| **Total** | **44,427,914.47** |

El desglose mensual por categoría es el siguiente:

| Categoría | 2025-10 | 2025-11 | 2025-12 |
|-----------|---------|---------|---------|
| ELECTRODOMESTICOS | 12,049,139.89 | 9,926,952.52 | 441,768.23 |
| JUGUETES | 8,217,455.58 | 6,747,154.38 | 248,144.94 |
| RODADOS | 775,748.82 | 1,217,382.67 | 106,199.72 |
| PUERICULTURA | 984,029.46 | 947,426.52 | 16,114.53 |
| DEPORTES | 667,955.52 | 1,090,428.64 | 29,061.04 |

En este ejemplo se observa que las categorías **ELECTRODOMESTICOS** y **JUGUETES** representan la mayor parte de las ventas, concentrando juntas más del 84% del total. La categoría **SERVICIO** presenta un saldo negativo de -$427,000 debido a notas de crédito que superaron la facturación en el período.

## Consideraciones importantes

- Los valores se expresan siempre en la **moneda de reporte** de la organización.
- Las **notas de crédito** se descuentan del total de cada categoría. Una categoría puede presentar un saldo negativo si las devoluciones o ajustes superan las ventas en el período consultado.
- La leyenda de colores permite identificar visualmente la contribución de cada categoría en las barras del gráfico.
- Este dashboard es una variante de [Ventas Netas](./ventas-netas) desglosada por la dimensión **Categoría de Producto**.
