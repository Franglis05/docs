---
title: Venta Diaria por Proveedor
category: Documentation
star: 9
sticky: 9
article: false
---

# Venta Diaria por Proveedor

## Descripción

El dashboard **Venta Diaria por Proveedor** presenta el monto de venta neta **sin impuestos** de cada día, desglosado por el proveedor del producto vendido. Los valores se expresan en la moneda de reporte de la organización.

Este dashboard permite analizar las ventas diarias agrupadas por el proveedor que suministra cada producto, identificando qué proveedores tienen mayor presencia en las ventas de la organización. El proveedor corresponde al proveedor actual registrado en la ficha del producto.

## ¿Cuándo se utiliza?

Se utiliza cuando la gerencia comercial necesita:
- Analizar las ventas diarias agrupadas por proveedor del producto.
- Identificar los proveedores cuyos productos generan mayor volumen de ventas.
- Evaluar la dependencia de las ventas respecto a proveedores específicos.
- Detectar la proporción de productos vendidos sin proveedor asignado.

## Acceso

Dashboards → Ventas → Venta Diaria por Proveedor

**Rol requerido:** Gerente de Ventas

## Vista general

El dashboard muestra un indicador numérico con el total acumulado de ventas del período y un gráfico de barras agrupadas por día, donde cada color representa un proveedor diferente.

![Dashboard de Venta Diaria por Proveedor en vista de barras](/assets/img/docs/dashboards/venta-diaria-por-proveedor-barras.png)

En la parte superior se presenta:
- **Título:** Venta Diaria por Proveedor
- **Subtítulo:** Ventas sin imp. diarias por proveedor
- **Indicador principal:** valor total acumulado del período consultado (ej. $1,428,898)
- **Leyenda:** listado de proveedores con su color asignado

En la esquina superior derecha se encuentran las opciones para cambiar la vista:
- Vista de tabla
- Selector de tipo de gráfica (Barras por defecto)

En la esquina superior izquierda se encuentra el [filtro de fechas](./#filtro-de-fechas) que permite definir el rango de consulta. Este filtro es común a todos los dashboards. Se recomienda **filtrar por un rango de fechas reducido** (por ejemplo, últimos 7 o 14 días) para obtener una mejor visualización de los datos diarios.

## Tipo de gráfica

- **Tipo:** Barras agrupadas
- **Eje Y:** Importe sin impuestos en moneda de reporte ($)
- **Eje X:** Fecha (día)
- **Colores:** cada proveedor se representa con un color distinto en la leyenda

## Datos de ejemplo

La siguiente tabla muestra el total acumulado de ventas por proveedor en el período consultado (3 días):

| Proveedor | Ventas ($) |
|----------|-----------:|
| SOCIO_23 | 1,201,813.49 |
| SOCIO_1860 | 42,343.25 |
| SOCIO_1951 | 31,193.95 |
| Sin Proveedor | 28,924.35 |
| SOCIO_180 | 17,763.48 |
| SOCIO_185 | 17,269.25 |
| SOCIO_4612 | 14,304.35 |
| SOCIO_218 | 12,906.50 |
| SOCIO_2340 | 11,420.00 |
| SOCIO_2302 | 8,223.50 |
| Otros (14 proveedores) | 42,735.79 |
| **Total** | **$1,428,897.91** |

En este ejemplo se observa que **SOCIO_23** concentra el 84% de las ventas del período ($1.2M), indicando que los productos de este proveedor dominan ampliamente la facturación. **Sin Proveedor** agrupa las ventas de productos que no tienen un proveedor actual asignado en su ficha.

## Consideraciones importantes

- Los valores se expresan siempre en la **moneda de reporte** de la organización.
- Este dashboard muestra los montos **sin impuestos** (neto de línea), a diferencia de otros dashboards de ventas netas que incluyen el total facturado.
- El proveedor corresponde al **proveedor actual** registrado en la ficha del producto, no al proveedor de una orden de compra específica.
- Los productos que no tienen un proveedor asignado aparecen agrupados bajo **"Sin Proveedor"**.
- Se recomienda utilizar un **rango de fechas reducido** en el filtro para obtener una mejor visibilidad de los datos diarios.
