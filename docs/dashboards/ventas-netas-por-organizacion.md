---
title: Ventas Netas por Organización
category: Documentation
star: 9
sticky: 9
article: false
---

# Ventas Netas por Organización

## Descripción

El dashboard **Ventas Netas por Organización** presenta el importe total de ventas facturadas considerando las devoluciones (notas de crédito) como negativas, desglosado por cada organización de la empresa. Los valores se expresan en la moneda de reporte de la organización.

Este dashboard permite comparar el desempeño comercial entre las diferentes organizaciones (sucursales, tiendas, centros de distribución), identificando cuáles generan mayor volumen de facturación y cómo se distribuyen las ventas a lo largo del tiempo.

## ¿Cuándo se utiliza?

Se utiliza cuando la gerencia comercial necesita:
- Comparar el volumen de ventas entre las diferentes organizaciones de la empresa.
- Identificar las organizaciones con mayor y menor contribución a las ventas totales.
- Analizar la evolución mensual de ventas por organización.
- Evaluar la concentración de ventas en determinadas organizaciones.

## Acceso

Dashboards → Ventas → Ventas Netas por Organización

**Rol requerido:** Gerente de Ventas

## Vista general

El dashboard muestra un indicador numérico con el total acumulado de ventas netas y un gráfico de barras agrupadas por mes, donde cada color representa una organización diferente.

![Dashboard de Ventas Netas por Organización en vista de barras](/assets/img/docs/dashboards/ventas-netas-por-organizacion-barras.png)

En la parte superior se presenta:
- **Título:** Ventas Netas por Organización
- **Subtítulo:** Ventas netas por organización mon. reporte
- **Indicador principal:** valor total acumulado del período consultado (ej. $57,500,727)
- **Leyenda:** listado de organizaciones con su color asignado

En la esquina superior derecha se encuentran las opciones para cambiar la vista:
- Vista de tabla
- Selector de tipo de gráfica (Barras por defecto)

En la esquina superior izquierda se encuentra el [filtro de fechas](./#filtro-de-fechas) que permite definir el rango de consulta. Este filtro es común a todos los dashboards.

## Tipo de gráfica

- **Tipo:** Barras agrupadas
- **Eje Y:** Importe en moneda de reporte ($)
- **Eje X:** Período temporal (meses)
- **Colores:** cada organización se representa con un color distinto en la leyenda

## Datos de ejemplo

| Organización | Ventas Netas ($) |
|-------------|-----------------:|
| Distribución Central | 25,834,490.29 |
| Administración Retail | 9,759,834.38 |
| Tienda MVD Shopping | 8,502,259.77 |
| Tienda Mayorista | 7,271,537.41 |
| Tienda Tres Cruces | 3,786,802.31 |
| Tienda Las Piedras | 2,345,803.27 |
| **Total** | **57,500,727.43** |

En este ejemplo se observa que **Distribución Central** concentra el 45% de las ventas totales, seguida por **Administración Retail** con el 17% y **Tienda MVD Shopping** con el 15%. Las tiendas físicas (Las Piedras y Tres Cruces) representan una menor proporción del volumen total.

## Consideraciones importantes

- Los valores se expresan siempre en la **moneda de reporte** de la organización.
- Las **notas de crédito** se descuentan del total de cada organización.
- Este dashboard es una variante de [Ventas Netas](./ventas-netas) desglosada por la dimensión **Organización**.
