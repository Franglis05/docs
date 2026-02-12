---
title: Ventas Netas por Campaña
category: Documentation
star: 9
sticky: 9
article: false
---

# Ventas Netas por Campaña

## Descripción

El dashboard **Ventas Netas por Campaña** presenta el importe total de ventas facturadas considerando las devoluciones (notas de crédito) como negativas, desglosado por cada campaña comercial asociada a las facturas. Los valores se expresan en la moneda de reporte de la organización.

Este dashboard permite evaluar el impacto de cada campaña comercial en las ventas, identificando cuáles generan mayor volumen de facturación. Las facturas que no tienen una campaña asignada se agrupan bajo la etiqueta "Sin Campaña".

## ¿Cuándo se utiliza?

Se utiliza cuando la gerencia comercial necesita:
- Evaluar el rendimiento de cada campaña comercial en un período determinado.
- Comparar el volumen de ventas generado por las diferentes campañas.
- Identificar la proporción de ventas no vinculadas a ninguna campaña.
- Analizar la evolución mensual de ventas por campaña.

## Acceso

Dashboards → Ventas → Ventas Netas por Campaña

**Rol requerido:** Gerente de Ventas

## Vista general

El dashboard muestra un indicador numérico con el total acumulado de ventas netas y un gráfico de barras agrupadas por mes, donde cada color representa una campaña diferente.

![Dashboard de Ventas Netas por Campaña en vista de barras](/assets/img/docs/dashboards/ventas-netas-por-campana-barras.png)

En la parte superior se presenta:
- **Título:** Ventas Netas por Campaña
- **Subtítulo:** Ventas netas por campaña mon. reporte
- **Indicador principal:** valor total acumulado del período consultado (ej. $57,500,727)
- **Leyenda:** listado de campañas con su color asignado

En la esquina superior derecha se encuentran las opciones para cambiar la vista:
- Vista de tabla
- Selector de tipo de gráfica (Barras por defecto)

En la esquina superior izquierda se encuentra el [filtro de fechas](./#filtro-de-fechas) que permite definir el rango de consulta. Este filtro es común a todos los dashboards.

## Tipo de gráfica

- **Tipo:** Barras agrupadas
- **Eje Y:** Importe en moneda de reporte ($)
- **Eje X:** Período temporal (meses)
- **Colores:** cada campaña se representa con un color distinto en la leyenda

## Datos de ejemplo

| Campaña | Ventas Netas ($) |
|---------|-----------------|
| Sin Campaña | 41,967,444.29 |
| Estándar | 7,070,409.59 |
| Construcción | 6,054,544.20 |
| AGRO | 2,408,329.35 |
| **Total** | **57,500,727.43** |

En este ejemplo se observa que **Sin Campaña** concentra el 73% de las ventas, correspondiente a la facturación que no está asociada a una campaña comercial específica. Entre las campañas activas, **Estándar** lidera con $7M, seguida por **Construcción** con $6M y **AGRO** con $2.4M.

## Consideraciones importantes

- Los valores se expresan siempre en la **moneda de reporte** de la organización.
- Las **notas de crédito** se descuentan del total de cada campaña.
- Las facturas que no tienen una campaña asignada aparecen agrupadas bajo la etiqueta **"Sin Campaña"**.
- Este dashboard es una variante de [Ventas Netas](./ventas-netas) desglosada por la dimensión **Campaña**.
