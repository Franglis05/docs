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
- **Indicador principal:** valor total acumulado del período consultado (ej. $57,525,127)
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

La siguiente tabla muestra el total acumulado de ventas por terminal PDV en el período consultado (64 días):

| Terminal PDV | Ventas Netas ($) |
|-------------|-----------------:|
| Sin Terminal | 41,910,263.89 |
| Smart MSC Caja 1 | 6,055,190.20 |
| Ositos y Cia XXX Caja 1 | 3,744,898.84 |
| Ositos y Cia MSC Caja 1 | 2,403,780.55 |
| Ositos y Cia LP Caja 1 | 2,345,803.27 |
| Puerto Arenal Caja 1 | 985,715.68 |
| Punto de Venta Service | 79,475.00 |
| **Total** | **$57,525,127.43** |

En este ejemplo se observa que **Sin Terminal** concentra el 73% de las ventas, correspondiente a la facturación que no está asociada a un terminal PDV específico. Entre los terminales identificados, **Smart MSC Caja 1** lidera con $6.1M, seguido por **Ositos y Cia XXX Caja 1** con $3.7M.

## Consideraciones importantes

- Los valores se expresan siempre en la **moneda de reporte** de la organización.
- Las **notas de crédito** se descuentan del total diario de cada terminal.
- Se recomienda utilizar un **rango de fechas reducido** en el filtro para obtener una mejor visibilidad de los datos. Al seleccionar períodos largos, la cantidad de puntos en el eje X puede dificultar la lectura del gráfico.
- Las facturas que no están asociadas a un terminal PDV aparecen agrupadas bajo la etiqueta **"Sin Terminal"**.
