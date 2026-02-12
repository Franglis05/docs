---
title: Ventas Netas por Organización y Categoría de Producto
category: Documentation
star: 9
sticky: 9
article: false
---

# Ventas Netas por Organización y Categoría de Producto

## Descripción

El dashboard **Ventas Netas por Organización y Categoría de Producto** presenta el importe total de ventas facturadas considerando las devoluciones (notas de crédito) como negativas, desglosado simultáneamente por organización y por categoría de producto. Los valores se expresan en la moneda de reporte de la organización.

Este dashboard permite analizar el mix de productos vendidos en cada organización, identificando qué categorías predominan en cada sucursal o centro de distribución.

## ¿Cuándo se utiliza?

Se utiliza cuando la gerencia comercial necesita:
- Analizar qué categorías de producto predominan en cada organización.
- Comparar el mix de productos entre las diferentes sucursales o centros de distribución.
- Identificar oportunidades para diversificar la oferta de productos en determinadas organizaciones.
- Evaluar la especialización comercial de cada organización.

## Acceso

Dashboards → Ventas → Ventas Netas por Org. y Cat. Producto

**Rol requerido:** Gerente de Ventas

## Vista general

El dashboard muestra un indicador numérico con el total acumulado de ventas netas y un gráfico de barras agrupadas por organización, donde cada color representa una categoría de producto diferente.

![Dashboard de Ventas Netas por Organización y Categoría de Producto en vista de barras](/assets/img/docs/dashboards/ventas-netas-por-organizacion-y-categoria-producto-barras.png)

En la parte superior se presenta:
- **Título:** Ventas Netas por Org. y Cat. Producto
- **Subtítulo:** Ventas netas por org. y cat. producto
- **Indicador principal:** valor total acumulado del período consultado (ej. $44,427,914)
- **Leyenda:** listado de categorías de producto con su color asignado

En la esquina superior derecha se encuentran las opciones para cambiar la vista:
- Vista de tabla
- Selector de tipo de gráfica (Barras por defecto)

En la esquina superior izquierda se encuentra el [filtro de fechas](./#filtro-de-fechas) que permite definir el rango de consulta. Este filtro es común a todos los dashboards.

## Tipo de gráfica

- **Tipo:** Barras agrupadas
- **Eje Y:** Importe en moneda de reporte ($)
- **Eje X:** Organización
- **Colores:** cada categoría de producto se representa con un color distinto en la leyenda

## Datos de ejemplo

La siguiente tabla muestra las ventas netas por organización, destacando las categorías principales:

| Organización | ELECTRODOMESTICOS | JUGUETES | Otras categorías | Total |
|-------------|------------------:|---------:|-----------------:|------:|
| Distribución Central | 16,393,249.51 | 3,345,631.46 | 1,817,719.08 | 21,556,600.05 |
| Tienda MVD Shopping | 42,666.92 | 6,297,256.77 | 2,162,264.92 | 8,502,188.61 |
| Tienda Mayorista | 5,847,541.20 | 706,928.39 | 662,060.66 | 7,216,530.25 |
| Tienda Tres Cruces | 17,312.00 | 2,883,096.83 | 886,393.27 | 3,786,802.10 |
| Tienda Las Piedras | 19,110.80 | 1,499,844.71 | 826,847.67 | 2,345,803.18 |
| Administración Retail | 97,980.21 | 479,996.74 | 442,013.33 | 1,019,990.28 |
| **Total** | **22,417,860.64** | **15,212,754.90** | **6,797,298.93** | **$44,427,914.47** |

En este ejemplo se observa que **Distribución Central** concentra las ventas de ELECTRODOMESTICOS ($16.4M), mientras que **Tienda MVD Shopping** lidera en JUGUETES ($6.3M). Cada organización muestra un perfil de ventas diferente según su orientación comercial.

## Consideraciones importantes

- Los valores se expresan siempre en la **moneda de reporte** de la organización.
- Las **notas de crédito** se descuentan del total de cada combinación organización-categoría.
- Este dashboard muestra la misma información que [Ventas Netas por Categoría de Producto y Organización](./ventas-netas-por-categoria-producto-y-organizacion) pero con las dimensiones invertidas: aquí la organización está en el eje X y la categoría de producto se representa con colores.
- Este dashboard es una variante de [Ventas Netas](./ventas-netas) desglosada por las dimensiones **Organización** y **Categoría de Producto**.
