---
title: Venta Diaria por Organización
category: Documentation
star: 9
sticky: 9
article: false
---

# Venta Diaria por Organización

## Descripción

El dashboard **Venta Diaria por Organización** presenta el monto de venta neta de cada día, desglosado por organización. Los valores se expresan en la moneda de reporte de la organización.

Este dashboard permite visualizar el comportamiento diario de las ventas en cada organización, identificando patrones de actividad comercial a lo largo de los días, picos de venta y días con menor actividad.

## ¿Cuándo se utiliza?

Se utiliza cuando la gerencia comercial necesita:
- Analizar el comportamiento diario de ventas por organización.
- Identificar patrones de actividad comercial (días de semana vs. fines de semana, por ejemplo).
- Detectar picos y caídas inusuales en la facturación diaria.
- Comparar el ritmo de ventas entre las diferentes organizaciones día a día.

## Acceso

Dashboards → Ventas → Venta Diaria por Organización

**Rol requerido:** Gerente de Ventas

## Vista general

El dashboard muestra un indicador numérico con el total acumulado de ventas del período y un gráfico de líneas donde cada línea representa una organización diferente, mostrando la evolución diaria de sus ventas.

![Dashboard de Venta Diaria por Organización en vista de línea](/assets/img/docs/dashboards/venta-diaria-por-organizacion-linea.png)

En la parte superior se presenta:
- **Título:** Venta Diaria por Organización
- **Subtítulo:** Venta neta diaria por organización
- **Indicador principal:** valor total acumulado del período consultado (ej. $17,862,033)
- **Leyenda:** listado de organizaciones con su color asignado

En la esquina superior derecha se encuentran las opciones para cambiar la vista:
- Vista de tabla
- Selector de tipo de gráfica (Línea por defecto)

En la esquina superior izquierda se encuentra el [filtro de fechas](./#filtro-de-fechas) que permite definir el rango de consulta. Este filtro es común a todos los dashboards. Se recomienda **filtrar por un rango de fechas reducido** (por ejemplo, últimos 7 o 14 días) para obtener una mejor visualización de los datos diarios.

## Tipo de gráfica

- **Tipo:** Línea
- **Eje Y:** Importe en moneda de reporte ($)
- **Eje X:** Fecha (día)
- **Colores:** cada organización se representa con un color y una línea diferente

## Datos de ejemplo

La siguiente tabla muestra las ventas diarias por organización para un período de 10 días:

| Fecha | Tienda Mayorista | Distribución Central | Tienda C | Administración Retail | Tienda B | Tienda A | Total |
|-------|-------------------:|-------------------:|-----------------:|---------------------:|--------------------:|----------------------:|------:|
| 2025-11-14 | 181,763.85 | 1,586,590.32 | 117,699.71 | 171,414.35 | 81,536.06 | 58,291.66 | 2,197,295.95 |
| 2025-11-15 | 17,667.14 | 0.00 | 185,298.77 | 241,220.74 | 46,896.23 | 86,124.47 | 577,207.35 |
| 2025-11-16 | 0.00 | 0.00 | 134,329.70 | 190,832.91 | 55,958.71 | 69,127.08 | 450,248.40 |
| 2025-11-17 | 212,364.60 | 763,209.31 | 102,927.38 | 168,972.36 | 14,036.58 | 49,531.95 | 1,311,042.18 |
| 2025-11-18 | 148,254.62 | 554,344.74 | 102,458.05 | 171,314.47 | 33,292.23 | 41,252.86 | 1,050,916.97 |
| 2025-11-19 | 85,863.08 | 598,967.44 | 85,630.51 | 153,590.52 | 35,653.50 | 57,658.14 | 1,017,363.19 |
| 2025-11-20 | 34,076.92 | 975,014.68 | 103,334.46 | 180,958.86 | 37,678.50 | 46,514.73 | 1,377,578.15 |
| 2025-11-21 | 270,033.08 | 299,657.60 | 142,490.14 | 324,399.92 | 39,224.34 | 56,103.50 | 1,131,908.58 |
| 2025-11-22 | 16,354.32 | 0.00 | 223,032.08 | 0.00 | 49,208.00 | 87,877.69 | 376,472.09 |
| 2025-11-23 | 0.00 | 0.00 | 126,629.39 | 171,604.04 | 53,018.49 | 52,032.75 | 403,284.67 |
| **Total** | **966,377.61** | **4,777,784.09** | **1,323,830.19** | **1,774,308.17** | **446,502.64** | **604,514.83** | **$9,893,317.53** |

En este ejemplo se observa que **Distribución Central** presenta la mayor variabilidad diaria, con picos superiores a $1.5M (14 de noviembre) y días sin actividad (15, 16, 22 y 23 de noviembre, correspondientes a fines de semana). Las tiendas físicas mantienen un flujo más estable, con **Tienda C** mostrando actividad consistente todos los días incluyendo fines de semana.

## Consideraciones importantes

- Los valores se expresan siempre en la **moneda de reporte** de la organización.
- Las **notas de crédito** se descuentan del total diario de cada organización.
- Se recomienda utilizar un **rango de fechas reducido** en el filtro para obtener una mejor visibilidad de los datos. Al seleccionar períodos largos, la cantidad de puntos en el eje X puede dificultar la lectura del gráfico.
- Los días con valor **$0** para una organización indican que no hubo actividad de facturación en esa organización durante ese día (ej. fines de semana o días no laborables).
