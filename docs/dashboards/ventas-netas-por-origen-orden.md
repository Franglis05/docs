---
title: Ventas Netas por Origen de Orden
category: Documentation
star: 9
sticky: 9
article: false
---

# Ventas Netas por Origen de Orden

## Descripción

El dashboard **Ventas Netas por Origen de Orden** presenta el importe total de ventas facturadas considerando las devoluciones (notas de crédito) como negativas, desglosado por el canal u origen desde el cual se generó la orden de venta. Los valores se expresan en la moneda de reporte de la organización.

Este dashboard permite analizar las ventas según el canal de origen, identificando la contribución de cada canal (tienda web, marketplace, punto de venta, etc.) a las ventas totales. Las facturas cuya orden no tiene un origen asignado se agrupan bajo la etiqueta "Sin Origen".

## ¿Cuándo se utiliza?

Se utiliza cuando la gerencia comercial necesita:
- Evaluar el desempeño de ventas por canal de origen.
- Comparar el volumen de ventas entre canales digitales, marketplaces y punto de venta.
- Identificar la proporción de ventas sin canal de origen asignado.
- Analizar la evolución mensual de ventas por canal.

## Acceso

Dashboards → Ventas → Ventas Netas por Origen de Orden

**Rol requerido:** Gerente de Ventas

## Vista general

El dashboard muestra un indicador numérico con el total acumulado de ventas netas y un gráfico de barras agrupadas por mes, donde cada color representa un origen de orden diferente.

![Dashboard de Ventas Netas por Origen de Orden en vista de barras](/assets/img/docs/dashboards/ventas-netas-por-origen-orden-barras.png)

En la parte superior se presenta:
- **Título:** Ventas Netas por Origen de Orden
- **Subtítulo:** Ventas netas por origen orden mon. reporte
- **Indicador principal:** valor total acumulado del período consultado (ej. $57,500,727)
- **Leyenda:** listado de orígenes de orden con su color asignado

En la esquina superior derecha se encuentran las opciones para cambiar la vista:
- Vista de tabla
- Selector de tipo de gráfica (Barras por defecto)

En la esquina superior izquierda se encuentra el [filtro de fechas](./#filtro-de-fechas) que permite definir el rango de consulta. Este filtro es común a todos los dashboards.

## Tipo de gráfica

- **Tipo:** Barras agrupadas
- **Eje Y:** Importe en moneda de reporte ($)
- **Eje X:** Período temporal (meses)
- **Colores:** cada origen de orden se representa con un color distinto en la leyenda

## Datos de ejemplo

| Origen de Orden | Ventas Netas ($) |
|----------------|-----------------:|
| Sin Origen | 56,403,002.18 |
| MercadoLibre | 355,926.79 |
| Web A | 314,929.38 |
| MercadoLibre_2 | 181,436.17 |
| Web B | 147,255.80 |
| Web D | 92,504.03 |
| Punto de Venta | 5,673.08 |
| **Total** | **$57,500,727.43** |

En este ejemplo se observa que **Sin Origen** concentra el 98% de las ventas, correspondiente a facturación cuya orden de venta no tiene un canal de origen asignado. Entre los canales identificados, los marketplaces de **MercadoLibre** y las tiendas **Web** representan los principales canales digitales.

## Consideraciones importantes

- Los valores se expresan siempre en la **moneda de reporte** de la organización.
- Las **notas de crédito** se descuentan del total de cada origen.
- Las facturas cuya orden de venta no tiene un origen asignado aparecen agrupadas bajo la etiqueta **"Sin Origen"**.
- Este dashboard resulta más útil cuando la organización registra el canal de origen en las órdenes de venta, permitiendo evaluar el rendimiento de cada canal comercial.
- Este dashboard es una variante de [Ventas Netas](./ventas-netas) desglosada por la dimensión **Origen de Orden**.
