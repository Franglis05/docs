---
title: Venta Diaria por Categoría de Producto
category: Documentation
star: 9
sticky: 9
article: false
---

# Venta Diaria por Categoría de Producto

## Descripción

El dashboard **Venta Diaria por Categoría de Producto** presenta el monto de venta neta de cada día, desglosado por categoría de producto. Los valores se expresan en la moneda de reporte de la organización.

Este dashboard permite visualizar el comportamiento diario de las ventas por categoría, identificando las líneas de producto con mayor actividad y los patrones de consumo a lo largo del tiempo.

## ¿Cuándo se utiliza?

Se utiliza cuando la gerencia comercial necesita:
- Analizar el comportamiento diario de ventas por categoría de producto.
- Identificar picos de demanda en categorías específicas.
- Comparar el ritmo de ventas entre las diferentes líneas de producto día a día.
- Detectar tendencias estacionales o patrones de consumo por categoría.

## Acceso

Dashboards → Ventas → Venta Diaria por Cat. Producto

**Rol requerido:** Gerente de Ventas

## Vista general

El dashboard muestra un indicador numérico con el total acumulado de ventas del período y un gráfico de líneas donde cada línea representa una categoría de producto diferente, mostrando la evolución diaria de sus ventas.

![Dashboard de Venta Diaria por Categoría de Producto en vista de línea](/assets/img/docs/dashboards/venta-diaria-por-categoria-producto-linea.png)

En la parte superior se presenta:
- **Título:** Venta Diaria por Cat. Producto
- **Subtítulo:** Venta diaria por cat. producto
- **Indicador principal:** valor total acumulado del período consultado (ej. $44,447,914)
- **Leyenda:** listado de categorías de producto con su color asignado

En la esquina superior derecha se encuentran las opciones para cambiar la vista:
- Vista de tabla
- Selector de tipo de gráfica (Línea por defecto)

En la esquina superior izquierda se encuentra el [filtro de fechas](./#filtro-de-fechas) que permite definir el rango de consulta. Este filtro es común a todos los dashboards. Se recomienda **filtrar por un rango de fechas reducido** (por ejemplo, últimos 7 o 14 días) para obtener una mejor visualización de los datos diarios.

## Tipo de gráfica

- **Tipo:** Línea
- **Eje Y:** Importe en moneda de reporte ($)
- **Eje X:** Fecha (día)
- **Colores:** cada categoría de producto se representa con un color y una línea diferente

## Datos de ejemplo

La siguiente tabla muestra el total acumulado de ventas por categoría de producto en el período consultado (63 días):

| Categoría de Producto | Ventas Netas ($) |
|----------------------|-----------------:|
| ELECTRODOMESTICOS | 22,417,860.64 |
| JUGUETES | 15,212,754.90 |
| RODADOS | 2,099,331.21 |
| PUERICULTURA | 1,947,570.51 |
| DEPORTES | 1,787,445.20 |
| BAZAR | 448,725.57 |
| PAPELERIA | 259,013.99 |
| LIBROS | 258,057.22 |
| REPUESTO | 207,045.87 |
| ESCOLARES | 98,656.37 |
| INSUMOS | 95,784.77 |
| MATERIAL DIDACTICO | 42,668.22 |
| SERVICIO | -427,000.00 |
| **Total** | **$44,447,914.47** |

En este ejemplo se observa que **ELECTRODOMESTICOS** presenta los picos diarios más altos y la mayor variabilidad, con días que superan $1M y otros por debajo de $100K. **JUGUETES** muestra un comportamiento más regular con un pico notable el 16 de octubre ($2.4M). Las demás categorías mantienen valores diarios relativamente bajos y estables.

## Consideraciones importantes

- Los valores se expresan siempre en la **moneda de reporte** de la organización.
- Las **notas de crédito** se descuentan del total diario de cada categoría. Una categoría puede presentar un valor negativo en un día si las devoluciones superan las ventas.
- Se recomienda utilizar un **rango de fechas reducido** en el filtro para obtener una mejor visibilidad de los datos. Al seleccionar períodos largos, la cantidad de puntos en el eje X puede dificultar la lectura del gráfico.
