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
- **Indicador principal:** valor total acumulado del período consultado (ej. $16,802,396)
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

La siguiente tabla muestra el total acumulado de ventas por forma de pago en el período consultado (3 meses):

| Forma de Pago | Ventas ($) |
|--------------|-----------:|
| Sin Forma Pago | 11,597,660.71 |
| Terminal POS 8 | 1,736,236.67 |
| Efectivo | 995,743.32 |
| Terminal POS 10 | 887,898.18 |
| Terminal POS 7 | 637,124.18 |
| Terminal POS 9 | 519,772.00 |
| Nota de Crédito (Devolución) | 119,510.40 |
| Fiserv | 94,316.44 |
| Transferencia Bancaria / Giro - BROU | 84,700.50 |
| Terminal POS 6 | 63,241.84 |
| Devolución | 35,156.67 |
| Terminal POS 5 | 18,250.00 |
| Vale Obsequio | 7,987.00 |
| Mercado Pago | 4,798.00 |
| **Total** | **$16,802,395.91** |

En este ejemplo se observa que **Sin Forma Pago** concentra el 69% de las ventas. Entre los métodos identificados, las **Terminales POS** en sus diferentes configuraciones representan el medio de pago principal ($3.9M en total, 23% de las ventas), seguido por **Efectivo** con $996K (6%) y **Fiserv** con $94K.

## Consideraciones importantes

- Los valores se expresan siempre en la **moneda de reporte** de la organización.
- Este dashboard muestra los montos **sin impuestos** (neto de línea), a diferencia de otros dashboards de ventas netas que incluyen el total facturado.
- Las facturas que no tienen un pago asociado con forma de pago específica aparecen agrupadas bajo **"Sin Forma Pago"**.
- Dado que este dashboard puede presentar una gran cantidad de formas de pago, se recomienda utilizar la **vista de tabla** para analizar los datos con mayor detalle.
