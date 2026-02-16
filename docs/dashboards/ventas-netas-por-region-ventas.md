---
title: Ventas Netas por Región de Ventas
category: Documentation
star: 9
sticky: 9
article: false
---

# Ventas Netas por Región de Ventas

## Descripción

El dashboard **Ventas Netas por Región de Ventas** presenta el importe total de ventas facturadas considerando las devoluciones (notas de crédito) como negativas, desglosado por cada región de ventas definida en la organización. Los valores se expresan en la moneda de reporte de la organización.

Este dashboard permite analizar la distribución geográfica de las ventas, identificando qué regiones concentran el mayor volumen comercial.

## ¿Cuándo se utiliza?

Se utiliza cuando la gerencia comercial necesita:
- Evaluar el desempeño de ventas por zona geográfica.
- Comparar el volumen de ventas entre las diferentes regiones.
- Identificar regiones con mayor potencial o bajo rendimiento.
- Analizar la evolución mensual de ventas por región.

## Acceso

Dashboards → Ventas → Ventas Netas por Región de Ventas

**Rol requerido:** Gerente de Ventas

## Vista general

El dashboard muestra un indicador numérico con el total acumulado de ventas netas y un gráfico de barras agrupadas por mes, donde cada color representa una región de ventas diferente.

![Dashboard de Ventas Netas por Región de Ventas en vista de barras](/assets/img/docs/dashboards/ventas-netas-por-region-ventas-barras.png)

En la parte superior se presenta:
- **Título:** Ventas Netas por Región de Ventas
- **Subtítulo:** Ventas netas por región ventas mon. reporte
- **Indicador principal:** valor total acumulado del período consultado (ej. $57,500,727)
- **Leyenda:** listado de regiones con su color asignado

En la esquina superior derecha se encuentran las opciones para cambiar la vista:
- Vista de tabla
- Selector de tipo de gráfica (Barras por defecto)

En la esquina superior izquierda se encuentra el [filtro de fechas](./#filtro-de-fechas) que permite definir el rango de consulta. Este filtro es común a todos los dashboards.

## Tipo de gráfica

- **Tipo:** Barras agrupadas
- **Eje Y:** Importe en moneda de reporte ($)
- **Eje X:** Período temporal (meses)
- **Colores:** cada región de ventas se representa con un color distinto en la leyenda

## Datos de ejemplo

| Región de Ventas | Ventas Netas ($) |
|------------------|-----------------|
| Estándar | 38,518,605.96 |
| Montevideo Este | 18,876,671.16 |
| Interior | 56,854.54 |
| Montevideo | 48,595.77 |
| **Total** | **57,500,727.43** |

En este ejemplo se observa que la región **Estándar** concentra el 67% de las ventas, seguida por **Montevideo Este** con el 33%. Las regiones **Interior** y **Montevideo** presentan un volumen marginal en comparación.

## Consideraciones importantes

- Los valores se expresan siempre en la **moneda de reporte** de la organización.
- Las **notas de crédito** se descuentan del total de cada región.
- Las facturas que no tienen una región de ventas asignada aparecen agrupadas bajo la etiqueta **"Sin Región"**.
- Este dashboard es una variante de [Ventas Netas](./ventas-netas) desglosada por la dimensión **Región de Venta**.
