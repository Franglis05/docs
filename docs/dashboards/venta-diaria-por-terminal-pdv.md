---
title: Venta Diaria por Terminal PDV
category: Documentation
star: 9
sticky: 9
article: false
---

# Venta Diaria por Terminal PDV

## Descripción

El dashboard **Venta Diaria por Terminal PDV** presenta el monto de venta neta de cada día, desglosado por terminal de punto de venta (PDV). Los valores se expresan en la moneda de reporte de la organización.

Este dashboard permite visualizar el comportamiento diario de las ventas en cada terminal PDV, identificando los terminales con mayor actividad y los patrones de venta a lo largo del tiempo.

## ¿Cuándo se utiliza?

Se utiliza cuando la gerencia comercial necesita:
- Analizar el comportamiento diario de ventas por terminal PDV.
- Comparar el volumen de ventas entre los diferentes terminales.
- Identificar picos y caídas en la actividad de cada terminal.
- Evaluar el rendimiento de cada punto de venta a lo largo del tiempo.

## Acceso

Dashboards → Ventas → Venta Diaria por Terminal PDV

**Rol requerido:** Gerente de Ventas

## Vista general

El dashboard muestra un indicador numérico con el total acumulado de ventas del período y un gráfico de líneas donde cada línea representa un terminal PDV diferente, mostrando la evolución diaria de sus ventas.

![Dashboard de Venta Diaria por Terminal PDV en vista de línea](/assets/img/docs/dashboards/venta-diaria-por-terminal-pdv-linea.png)

En la parte superior se presenta:
- **Título:** Venta Diaria por Terminal PDV
- **Subtítulo:** Venta diaria por terminal PDV
- **Indicador principal:** valor total acumulado del período consultado (ej. $5,342,279)
- **Leyenda:** listado de terminales PDV con su color asignado

En la esquina superior derecha se encuentran las opciones para cambiar la vista:
- Vista de tabla
- Selector de tipo de gráfica (Línea por defecto)

En la esquina superior izquierda se encuentra el [filtro de fechas](./#filtro-de-fechas) que permite definir el rango de consulta. Este filtro es común a todos los dashboards. Se recomienda **filtrar por un rango de fechas reducido** (por ejemplo, últimos 7 o 14 días) para obtener una mejor visualización de los datos diarios.

## Tipo de gráfica

- **Tipo:** Línea
- **Eje Y:** Importe en moneda de reporte ($)
- **Eje X:** Fecha (día)
- **Colores:** cada terminal PDV se representa con un color y una línea diferente

## Datos de ejemplo

La siguiente tabla muestra el total acumulado de ventas por terminal PDV en el período consultado (7 días):

| Terminal PDV | Ventas Netas ($) |
|-------------|-----------------:|
| Sin Terminal | 3,496,416.44 |
| Sucursal C Caja 1 | 725,741.98 |
| Sucursal E Caja 1 | 478,753.69 |
| Sucursal D Caja 1 | 255,849.96 |
| Sucursal A Caja 1 | 232,639.93 |
| Sucursal B Caja 1 | 152,876.67 |
| **Total** | **$5,342,278.67** |

En este ejemplo se observa que **Sin Terminal** concentra el 65% de las ventas, correspondiente a la facturación que no está asociada a un terminal PDV específico. Entre los terminales identificados, **Sucursal C Caja 1** lidera con $726K, seguido por **Sucursal E Caja 1** con $479K.

## Consideraciones importantes

- Los valores se expresan siempre en la **moneda de reporte** de la organización.
- Las **notas de crédito** se descuentan del total diario de cada terminal.
- Se recomienda utilizar un **rango de fechas reducido** en el filtro para obtener una mejor visibilidad de los datos. Al seleccionar períodos largos, la cantidad de puntos en el eje X puede dificultar la lectura del gráfico.
- Las facturas que no están asociadas a un terminal PDV aparecen agrupadas bajo la etiqueta **"Sin Terminal"**.
