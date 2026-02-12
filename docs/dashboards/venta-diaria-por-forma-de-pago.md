---
title: Venta Diaria por Forma de Pago
category: Documentation
star: 9
sticky: 9
article: false
---

# Venta Diaria por Forma de Pago

## Descripción

El dashboard **Venta Diaria por Forma de Pago** presenta el monto de venta neta **sin impuestos** de cada día, desglosado por la forma de pago utilizada en cada transacción. Los valores se expresan en la moneda de reporte de la organización.

Este dashboard permite analizar cómo se distribuyen las ventas diarias entre los diferentes métodos de pago (efectivo, transferencias, plataformas digitales, etc.), identificando los medios de pago más utilizados y su evolución día a día.

## ¿Cuándo se utiliza?

Se utiliza cuando la gerencia comercial necesita:
- Analizar la distribución de ventas por forma de pago en cada día.
- Identificar los métodos de pago más utilizados por los clientes.
- Detectar tendencias en la adopción de medios de pago digitales.
- Evaluar la proporción de ventas sin forma de pago asignada.

## Acceso

Dashboards → Ventas → Venta Diaria por Forma de Pago

**Rol requerido:** Gerente de Ventas

## Vista general

El dashboard muestra un indicador numérico con el total acumulado de ventas del período y un gráfico de barras agrupadas por día, donde cada color representa una forma de pago diferente.

![Dashboard de Venta Diaria por Forma de Pago en vista de barras](/assets/img/docs/dashboards/venta-diaria-por-forma-de-pago-barras.png)

En la parte superior se presenta:
- **Título:** Venta Diaria por Forma de Pago
- **Subtítulo:** Ventas sin imp. diarias por forma de pago
- **Indicador principal:** valor total acumulado del período consultado (ej. $1,622,686)
- **Leyenda:** listado de formas de pago con su color asignado

En la esquina superior derecha se encuentran las opciones para cambiar la vista:
- Vista de tabla
- Selector de tipo de gráfica (Barras por defecto)

En la esquina superior izquierda se encuentra el [filtro de fechas](./#filtro-de-fechas) que permite definir el rango de consulta. Este filtro es común a todos los dashboards. Se recomienda **filtrar por un rango de fechas reducido** (por ejemplo, últimos 7 o 14 días) para obtener una mejor visualización de los datos diarios.

## Tipo de gráfica

- **Tipo:** Barras agrupadas
- **Eje Y:** Importe sin impuestos en moneda de reporte ($)
- **Eje X:** Fecha (día)
- **Colores:** cada forma de pago se representa con un color distinto en la leyenda

## Datos de ejemplo

La siguiente tabla muestra el total acumulado de ventas por forma de pago en el período consultado (3 días):

| Forma de Pago | Ventas ($) |
|--------------|-----------:|
| Sin Forma Pago | 812,921.65 |
| Pleni1 SmartMVD | 277,371.38 |
| Pleni1 Ositos XXX | 157,439.79 |
| Efectivo | 148,576.19 |
| Pleni1 OsitosMVD | 85,469.15 |
| Pleni1 T00005 Ositos LP | 71,467.55 |
| Fiserv | 36,755.65 |
| Devolución PSIG | 10,353.00 |
| Pleni1 Puerto Arenal | 8,980.00 |
| Soy Santander | 3,299.50 |
| Transferencia Bancaria / Giro - BROU | 3,171.66 |
| Fisrerv - Mastercard | 3,010.50 |
| Mercado Pago | 1,970.00 |
| Nota de Crédito (Devolución) | 1,900.00 |
| **Total** | **$1,622,686.02** |

En este ejemplo se observa que **Sin Forma Pago** concentra el 50% de las ventas, correspondiente a facturación que no tiene un pago asociado con forma de pago específica. Entre los métodos identificados, las plataformas **Pleni1** en sus diferentes terminales representan el medio de pago más utilizado, seguido por **Efectivo** con $148K.

## Consideraciones importantes

- Los valores se expresan siempre en la **moneda de reporte** de la organización.
- Este dashboard muestra los montos **sin impuestos** (neto de línea), a diferencia de otros dashboards de ventas netas que incluyen el total facturado.
- Las facturas que no tienen un pago asociado con forma de pago específica aparecen agrupadas bajo **"Sin Forma Pago"**.
- Se recomienda utilizar un **rango de fechas reducido** en el filtro para obtener una mejor visibilidad de los datos diarios.
