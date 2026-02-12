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
- **Indicador principal:** valor total acumulado del período consultado (ej. $7,985,900)
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

| Fecha | Tienda Las Piedras | Tienda Tres Cruces | Tienda Mayorista | Distribución Central | Tienda MVD Shopping | Administración Retail | Total |
|-------|-------------------:|-------------------:|-----------------:|---------------------:|--------------------:|----------------------:|------:|
| 2025-10-01 | 27,269.55 | 31,598.30 | 25,313.16 | 162,310.33 | 120,791.05 | 122,715.99 | 489,998.38 |
| 2025-10-02 | 26,052.50 | 70,212.55 | 34,650.63 | 372,249.18 | 118,406.13 | 8,249.99 | 629,820.98 |
| 2025-10-03 | 43,127.00 | 96,043.99 | 106,998.75 | 135,046.91 | 172,836.10 | 5,646.74 | 559,699.49 |
| 2025-10-04 | 63,538.79 | 93,851.10 | 54,801.59 | 0.00 | 178,285.80 | 304.08 | 390,781.36 |
| 2025-10-05 | 52,149.50 | 59,046.95 | 0.00 | 0.00 | 158,257.07 | 0.00 | 269,453.52 |
| 2025-10-06 | 16,916.56 | 53,510.50 | 108,866.12 | 1,234,575.56 | 91,773.06 | 7,047.69 | 1,512,689.49 |
| 2025-10-07 | 26,796.06 | 76,502.30 | 436,262.49 | 615,579.80 | 120,204.70 | 214,490.10 | 1,489,835.45 |
| 2025-10-08 | 23,135.50 | 43,399.55 | 263,842.70 | 740,115.92 | 126,271.98 | 36,819.00 | 1,233,584.65 |
| 2025-10-09 | 35,478.90 | 37,917.80 | 23,484.16 | 188,864.93 | 115,020.84 | 163,258.88 | 564,025.51 |
| 2025-10-10 | 19,828.15 | 69,170.25 | 180,268.01 | 382,457.16 | 166,503.62 | 27,784.33 | 846,011.52 |
| **Total** | **334,292.51** | **631,253.29** | **1,234,487.61** | **3,831,199.79** | **1,368,150.35** | **586,316.80** | **$7,985,900.35** |

En este ejemplo se observa que **Distribución Central** presenta la mayor variabilidad diaria, con picos superiores a $1.2M (6 de octubre) y días sin actividad (4 y 5 de octubre, correspondientes a fin de semana). Las tiendas físicas mantienen un flujo más estable, con **Tienda MVD Shopping** mostrando actividad consistente todos los días incluyendo fines de semana.

## Consideraciones importantes

- Los valores se expresan siempre en la **moneda de reporte** de la organización.
- Las **notas de crédito** se descuentan del total diario de cada organización.
- Se recomienda utilizar un **rango de fechas reducido** en el filtro para obtener una mejor visibilidad de los datos. Al seleccionar períodos largos, la cantidad de puntos en el eje X puede dificultar la lectura del gráfico.
- Los días con valor **$0** para una organización indican que no hubo actividad de facturación en esa organización durante ese día (ej. fines de semana o días no laborables).
