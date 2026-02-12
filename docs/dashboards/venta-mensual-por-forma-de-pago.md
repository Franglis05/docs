---
title: Venta Mensual por Forma de Pago
category: Documentation
star: 9
sticky: 9
article: false
---

# Venta Mensual por Forma de Pago

## Descripción

El dashboard **Venta Mensual por Forma de Pago** presenta el monto de venta neta **sin impuestos** agrupado por mes, desglosado por la forma de pago utilizada en cada transacción. Los valores se expresan en la moneda de reporte de la organización.

Este dashboard permite analizar la evolución mensual de las ventas según el método de pago, proporcionando una vista consolidada de la composición de pagos a lo largo del tiempo.

## ¿Cuándo se utiliza?

Se utiliza cuando la gerencia comercial necesita:
- Analizar la distribución mensual de ventas por forma de pago.
- Comparar la evolución de los diferentes métodos de pago entre meses.
- Evaluar tendencias de adopción de medios de pago a lo largo del tiempo.
- Identificar la proporción de ventas por cada método de pago en el consolidado mensual.

## Acceso

Dashboards → Ventas → Venta Mensual por Forma de Pago

**Rol requerido:** Gerente de Ventas

## Vista general

El dashboard muestra un indicador numérico con el total acumulado de ventas del período y un gráfico de barras agrupadas por mes, donde cada color representa una forma de pago diferente.

![Dashboard de Venta Mensual por Forma de Pago en vista de barras](/assets/img/docs/dashboards/venta-mensual-por-forma-de-pago-barras.png)

En la parte superior se presenta:
- **Título:** Venta Mensual por Forma de Pago
- **Subtítulo:** Ventas sin imp. mensual por forma de pago
- **Indicador principal:** valor total acumulado del período consultado (ej. $54,625,683)
- **Leyenda:** listado de formas de pago con su color asignado

En la esquina superior derecha se encuentran las opciones para cambiar la vista:
- Vista de tabla
- Selector de tipo de gráfica (Barras por defecto)

En la esquina superior izquierda se encuentra el [filtro de fechas](./#filtro-de-fechas) que permite definir el rango de consulta. Este filtro es común a todos los dashboards.

## Tipo de gráfica

- **Tipo:** Barras agrupadas
- **Eje Y:** Importe sin impuestos en moneda de reporte ($)
- **Eje X:** Período temporal (meses)
- **Colores:** cada forma de pago se representa con un color distinto en la leyenda

## Datos de ejemplo

La siguiente tabla muestra el total acumulado de ventas por forma de pago en el período consultado:

| Forma de Pago | Ventas ($) |
|--------------|-----------:|
| Sin Forma Pago | 36,680,445.28 |
| Pleni1 SmartMVD | 5,478,680.63 |
| Efectivo | 3,564,523.48 |
| Pleni1 Ositos XXX | 3,139,979.10 |
| Pleni1 OsitosMVD | 2,167,414.23 |
| Pleni1 T00005 Ositos LP | 1,690,280.57 |
| Fiserv | 640,379.91 |
| Nota de Crédito (Devolución) | 384,090.83 |
| Transferencia Bancaria / Giro - BROU | 286,988.90 |
| Pleni1 Puerto Arenal | 250,234.47 |
| Devolución PSIG | 236,354.78 |
| Otros (10 formas de pago) | 106,311.31 |
| **Total** | **$54,625,683.49** |

En este ejemplo se observa que **Sin Forma Pago** concentra el 67% de las ventas. Entre los métodos identificados, las plataformas **Pleni1** en sus diferentes terminales representan el medio de pago principal ($12.7M en total, 23% de las ventas), seguido por **Efectivo** con $3.6M (7%) y **Fiserv** con $640K.

## Consideraciones importantes

- Los valores se expresan siempre en la **moneda de reporte** de la organización.
- Este dashboard muestra los montos **sin impuestos** (neto de línea), a diferencia de otros dashboards de ventas netas que incluyen el total facturado.
- Las facturas que no tienen un pago asociado con forma de pago específica aparecen agrupadas bajo **"Sin Forma Pago"**.
- Dado que este dashboard puede presentar una gran cantidad de formas de pago, se recomienda utilizar la **vista de tabla** para analizar los datos con mayor detalle.
