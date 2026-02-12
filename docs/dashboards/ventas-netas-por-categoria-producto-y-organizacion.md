---
title: Ventas Netas por Categoría de Producto y Organización
category: Documentation
star: 9
sticky: 9
article: false
---

# Ventas Netas por Categoría de Producto y Organización

## Descripción

El dashboard **Ventas Netas por Categoría de Producto y Organización** presenta el importe total de ventas facturadas considerando las devoluciones (notas de crédito) como negativas, desglosado simultáneamente por categoría de producto y por organización. Los valores se expresan en la moneda de reporte de la organización.

Este dashboard permite analizar cómo se distribuyen las ventas de cada categoría de producto entre las diferentes organizaciones de la empresa, identificando la especialización comercial de cada sucursal o centro de distribución.

## ¿Cuándo se utiliza?

Se utiliza cuando la gerencia comercial necesita:
- Analizar qué categorías de producto se venden más en cada organización.
- Identificar la especialización comercial de cada sucursal o centro de distribución.
- Comparar la participación de cada organización dentro de una misma categoría de producto.
- Detectar oportunidades para ampliar el mix de productos en determinadas organizaciones.

## Acceso

Dashboards → Ventas → Ventas Netas por Cat. Prod. y Org.

**Rol requerido:** Gerente de Ventas

## Vista general

El dashboard muestra un indicador numérico con el total acumulado de ventas netas y un gráfico de barras agrupadas por categoría de producto, donde cada color representa una organización diferente.

![Dashboard de Ventas Netas por Categoría de Producto y Organización en vista de barras](/assets/img/docs/dashboards/ventas-netas-por-categoria-producto-y-organizacion-barras.png)

En la parte superior se presenta:
- **Título:** Ventas Netas por Cat. Prod. y Org.
- **Subtítulo:** Ventas netas por cat. prod. y org.
- **Indicador principal:** valor total acumulado del período consultado (ej. $44,427,914)
- **Leyenda:** listado de organizaciones con su color asignado

En la esquina superior derecha se encuentran las opciones para cambiar la vista:
- Vista de tabla
- Selector de tipo de gráfica (Barras por defecto)

En la esquina superior izquierda se encuentra el [filtro de fechas](./#filtro-de-fechas) que permite definir el rango de consulta. Este filtro es común a todos los dashboards.

## Tipo de gráfica

- **Tipo:** Barras agrupadas
- **Eje Y:** Importe en moneda de reporte ($)
- **Eje X:** Categoría de producto
- **Colores:** cada organización se representa con un color distinto en la leyenda

## Datos de ejemplo

La siguiente tabla muestra las ventas netas por categoría de producto y organización:

| Categoría | Tienda Las Piedras | Tienda Tres Cruces | Tienda Mayorista | Distribución Central | Tienda MVD Shopping | Administración Retail | Total |
|-----------|-------------------:|-------------------:|-----------------:|---------------------:|--------------------:|----------------------:|------:|
| ELECTRODOMESTICOS | 19,110.80 | 17,312.00 | 5,847,541.20 | 16,393,249.51 | 42,666.92 | 97,980.21 | 22,417,860.64 |
| JUGUETES | 1,499,844.71 | 2,883,096.83 | 706,928.39 | 3,345,631.46 | 6,297,256.77 | 479,996.74 | 15,212,754.90 |
| RODADOS | 275,900.90 | 207,588.95 | 283,150.01 | 504,929.38 | 585,456.02 | 242,305.95 | 2,099,331.21 |
| PUERICULTURA | 421,339.71 | 405,281.82 | 84,768.70 | 101,754.64 | 822,381.56 | 112,044.08 | 1,947,570.51 |
| DEPORTES | 32,540.20 | 94,925.70 | 23,614.91 | 1,249,268.03 | 307,597.92 | 79,498.44 | 1,787,445.20 |
| Otras categorías | 97,066.86 | 178,597.00 | 234,527.00 | -213,232.97 | 447,900.58 | 3,093.51 | 747,952.01 |
| **Total** | **2,345,803.18** | **3,786,802.30** | **7,180,530.21** | **21,381,600.05** | **8,503,259.77** | **1,014,919.23** | **$44,427,914.47** |

En este ejemplo se observa que **ELECTRODOMESTICOS** se concentra principalmente en **Distribución Central** (73% de la categoría) y **Tienda Mayorista** (26%). En contraste, **JUGUETES** se distribuye más ampliamente, con **Tienda MVD Shopping** liderando con el 41% de la categoría.

## Consideraciones importantes

- Los valores se expresan siempre en la **moneda de reporte** de la organización.
- Las **notas de crédito** se descuentan del total de cada combinación categoría-organización.
- Dado que este dashboard cruza dos dimensiones, se recomienda utilizar la **vista de tabla** para analizar los datos con mayor detalle.
- Este dashboard es una variante de [Ventas Netas](./ventas-netas) desglosada por las dimensiones **Categoría de Producto** y **Organización**.
