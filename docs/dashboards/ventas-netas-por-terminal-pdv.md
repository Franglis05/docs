---
title: Ventas Netas por Terminal PDV
category: Documentation
star: 9
sticky: 9
article: false
---

# Ventas Netas por Terminal PDV

## Descripción

El dashboard **Ventas Netas por Terminal PDV** presenta el importe total de ventas facturadas considerando las devoluciones (notas de crédito) como negativas, desglosado por cada terminal de punto de venta (PDV). Los valores se expresan en la moneda de reporte de la organización.

Este dashboard permite analizar el rendimiento de cada terminal de punto de venta, identificando cuáles generan mayor volumen de facturación. Las facturas que no se originaron desde un terminal PDV se agrupan bajo la etiqueta "Sin Terminal".

## ¿Cuándo se utiliza?

Se utiliza cuando la gerencia comercial necesita:
- Evaluar el rendimiento de cada terminal de punto de venta.
- Comparar el volumen de facturación entre las diferentes cajas o terminales.
- Identificar la proporción de ventas realizadas por PDV frente a otros canales.
- Analizar la evolución mensual de ventas por terminal.

## Acceso

Dashboards → Ventas → Ventas Netas por Terminal PDV

**Rol requerido:** Gerente de Ventas

## Vista general

El dashboard muestra un indicador numérico con el total acumulado de ventas netas y un gráfico de barras agrupadas por mes, donde cada color representa un terminal PDV diferente.

![Dashboard de Ventas Netas por Terminal PDV en vista de barras](/assets/img/docs/dashboards/ventas-netas-por-terminal-pdv-barras.png)

En la parte superior se presenta:
- **Título:** Ventas Netas por Terminal PDV
- **Subtítulo:** Ventas netas por terminal PDV mon. reporte
- **Indicador principal:** valor total acumulado del período consultado (ej. $17,862,033)
- **Leyenda:** listado de terminales con su color asignado

En la esquina superior derecha se encuentran las opciones para cambiar la vista:
- Vista de tabla
- Selector de tipo de gráfica (Barras por defecto)

En la esquina superior izquierda se encuentra el [filtro de fechas](./#filtro-de-fechas) que permite definir el rango de consulta. Este filtro es común a todos los dashboards.

## Tipo de gráfica

- **Tipo:** Barras agrupadas
- **Eje Y:** Importe en moneda de reporte ($)
- **Eje X:** Período temporal (meses)
- **Colores:** cada terminal PDV se representa con un color distinto en la leyenda

## Datos de ejemplo

| Terminal PDV | Ventas Netas ($) |
|-------------|-----------------:|
| Sin Terminal | 13,298,770.89 |
| Sucursal C Caja 1 | 1,811,771.30 |
| Sucursal E Caja 1 | 1,057,273.23 |
| Sucursal D Caja 1 | 719,018.06 |
| Sucursal A Caja 1 | 695,606.18 |
| Sucursal B Caja 1 | 254,842.85 |
| Punto de Venta Service | 24,750.00 |
| **Total** | **$17,862,032.51** |

En este ejemplo se observa que **Sin Terminal** concentra el 74% de las ventas, correspondiente a la facturación que no se realiza desde un punto de venta. Entre los terminales activos, **Sucursal C Caja 1** lidera con $1.8M, seguido por **Sucursal E Caja 1** con $1.1M.

## Consideraciones importantes

- Los valores se expresan siempre en la **moneda de reporte** de la organización.
- Las **notas de crédito** se descuentan del total de cada terminal.
- Las facturas que no se originaron desde un terminal PDV aparecen agrupadas bajo la etiqueta **"Sin Terminal"**.
- Este dashboard es una variante de [Ventas Netas](./ventas-netas) desglosada por la dimensión **Terminal PDV**.
