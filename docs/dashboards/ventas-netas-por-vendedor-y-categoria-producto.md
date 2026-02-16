---
title: Ventas Netas por Vendedor y Categoría de Producto
category: Documentation
star: 9
sticky: 9
article: false
---

# Ventas Netas por Vendedor y Categoría de Producto

## Descripción

El dashboard **Ventas Netas por Vendedor y Categoría de Producto** presenta el importe total de ventas facturadas considerando las devoluciones (notas de crédito) como negativas, desglosado simultáneamente por vendedor y por categoría de producto. Los valores se expresan en la moneda de reporte de la organización.

Este dashboard permite analizar el mix de productos que vende cada vendedor, identificando la especialización comercial de cada agente y las categorías que predominan en su cartera.

## ¿Cuándo se utiliza?

Se utiliza cuando la gerencia comercial necesita:
- Analizar qué categorías de producto vende cada vendedor.
- Identificar la especialización comercial de cada agente de ventas.
- Comparar el mix de productos entre vendedores.
- Detectar oportunidades para diversificar las ventas por categoría en determinados vendedores.

## Acceso

Dashboards → Ventas → Ventas Netas por Vendedor y Cat. Prod.

**Rol requerido:** Gerente de Ventas

## Vista general

El dashboard muestra un indicador numérico con el total acumulado de ventas netas y un gráfico de barras agrupadas por vendedor, donde cada color representa una categoría de producto diferente.

![Dashboard de Ventas Netas por Vendedor y Categoría de Producto en vista de barras](/assets/img/docs/dashboards/ventas-netas-por-vendedor-y-categoria-producto-barras.png)

En la parte superior se presenta:
- **Título:** Ventas Netas por Vendedor y Cat. Prod.
- **Subtítulo:** Ventas netas por vendedor y cat. prod.
- **Indicador principal:** valor total acumulado del período consultado (ej. $44,427,914)
- **Leyenda:** listado de categorías de producto con su color asignado

En la esquina superior derecha se encuentran las opciones para cambiar la vista:
- Vista de tabla
- Selector de tipo de gráfica (Barras por defecto)

En la esquina superior izquierda se encuentra el [filtro de fechas](./#filtro-de-fechas) que permite definir el rango de consulta. Este filtro es común a todos los dashboards.

## Tipo de gráfica

- **Tipo:** Barras agrupadas
- **Eje Y:** Importe en moneda de reporte ($)
- **Eje X:** Vendedor
- **Colores:** cada categoría de producto se representa con un color distinto en la leyenda

## Datos de ejemplo

La siguiente tabla muestra los 10 vendedores con mayor volumen de ventas netas:

| Vendedor | Ventas Netas ($) |
|---------|-----------------:|
| Vendedor_84 | 9,704,173.34 |
| Vendedor_103 | 7,631,441.69 |
| Vendedor_1820 | 3,435,461.57 |
| Vendedor_129 | 3,118,203.95 |
| Vendedor_100 | 2,781,330.94 |
| Vendedor_1805 | 1,510,538.55 |
| Vendedor_10 | 1,313,901.73 |
| Vendedor_109 | 1,304,017.96 |
| Vendedor_1804 | 1,185,877.19 |
| Vendedor_1803 | 993,422.41 |
| Otros (33 vendedores) | 11,449,545.14 |
| **Total** | **$44,427,914.47** |

En este ejemplo se observa que **Vendedor_84** lidera con $9.7M, concentrados principalmente en ELECTRODOMESTICOS ($8.2M). **Vendedor_103** ocupa el segundo lugar con $7.6M, también dominado por ELECTRODOMESTICOS ($7.1M). En contraste, **Vendedor_100** se especializa en JUGUETES ($2.3M de sus $2.8M totales). En total, el dashboard desglosa las ventas de **43 vendedores**.

## Consideraciones importantes

- Los valores se expresan siempre en la **moneda de reporte** de la organización.
- Las **notas de crédito** se descuentan del total de cada combinación vendedor-categoría.
- Se recomienda utilizar la **vista de tabla** para analizar los datos con mayor detalle.
- Este dashboard es una variante de [Ventas Netas](./ventas-netas) desglosada por las dimensiones **Vendedor** y **Categoría de Producto**.
