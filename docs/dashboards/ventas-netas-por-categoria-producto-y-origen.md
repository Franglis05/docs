---
title: Ventas Netas por Categoría de Producto y Origen de Orden
category: Documentation
star: 9
sticky: 9
article: false
---

# Ventas Netas por Categoría de Producto y Origen de Orden

## Descripción

El dashboard **Ventas Netas por Categoría de Producto y Origen de Orden** presenta el importe total de ventas facturadas considerando las devoluciones (notas de crédito) como negativas, desglosado simultáneamente por categoría de producto y por el canal u origen desde el cual se generó la orden de venta. Los valores se expresan en la moneda de reporte de la organización.

Este dashboard permite analizar qué categorías de producto se venden a través de cada canal comercial, identificando la participación de marketplaces, tiendas web y punto de venta en cada línea de producto.

## ¿Cuándo se utiliza?

Se utiliza cuando la gerencia comercial necesita:
- Analizar qué categorías de producto se venden más en cada canal de origen.
- Comparar la participación de los diferentes canales dentro de cada categoría.
- Identificar oportunidades para potenciar la venta de determinadas categorías en canales específicos.
- Evaluar la distribución de ventas por canal y categoría de producto.

## Acceso

Dashboards → Ventas → Ventas Netas por Cat. Prod. y Origen

**Rol requerido:** Gerente de Ventas

## Vista general

El dashboard muestra un indicador numérico con el total acumulado de ventas netas y un gráfico de barras agrupadas por categoría de producto, donde cada color representa un origen de orden diferente.

![Dashboard de Ventas Netas por Categoría de Producto y Origen de Orden en vista de barras](/assets/img/docs/dashboards/ventas-netas-por-categoria-producto-y-origen-barras.png)

En la parte superior se presenta:
- **Título:** Ventas Netas por Cat. Prod. y Origen
- **Subtítulo:** Ventas netas por cat. prod. y origen orden
- **Indicador principal:** valor total acumulado del período consultado (ej. $44,427,914)
- **Leyenda:** listado de orígenes de orden con su color asignado

En la esquina superior derecha se encuentran las opciones para cambiar la vista:
- Vista de tabla
- Selector de tipo de gráfica (Barras por defecto)

En la esquina superior izquierda se encuentra el [filtro de fechas](./#filtro-de-fechas) que permite definir el rango de consulta. Este filtro es común a todos los dashboards.

## Tipo de gráfica

- **Tipo:** Barras agrupadas
- **Eje Y:** Importe en moneda de reporte ($)
- **Eje X:** Categoría de producto
- **Colores:** cada origen de orden se representa con un color distinto en la leyenda

## Datos de ejemplo

La siguiente tabla muestra las ventas netas por categoría de producto, con el desglose por origen de orden:

| Categoría | Sin Origen | Canales digitales | Total |
|-----------|----------:|-----------------:|------:|
| ELECTRODOMESTICOS | 22,342,497.96 | 75,362.68 | 22,417,860.64 |
| JUGUETES | 14,766,107.73 | 446,647.17 | 15,212,754.90 |
| RODADOS | 1,887,074.43 | 212,256.78 | 2,099,331.21 |
| PUERICULTURA | 1,851,260.25 | 96,310.26 | 1,947,570.51 |
| DEPORTES | 1,713,719.66 | 73,725.54 | 1,787,445.20 |
| BAZAR | 446,553.98 | 2,171.59 | 448,725.57 |
| PAPELERIA | 259,013.99 | 0.00 | 259,013.99 |
| LIBROS | 258,057.22 | 0.00 | 258,057.22 |
| REPUESTO | 206,016.11 | 1,029.76 | 207,045.87 |
| ESCOLARES | 97,078.09 | 1,578.28 | 98,656.37 |
| INSUMOS | 75,784.77 | 0.00 | 75,784.77 |
| MATERIAL DIDACTICO | 40,791.18 | 1,877.04 | 42,668.22 |
| SERVICIO | -427,000.00 | 0.00 | -427,000.00 |
| **Total** | **43,516,955.37** | **910,959.10** | **$44,427,914.47** |

Los canales digitales identificados incluyen: **MercadoLibre** ($291,932), **Web A** ($265,911), **MercadoLibre_2** ($148,718), **Web B** ($123,925), **Web D** ($75,823) y **Punto de Venta** ($4,650).

En este ejemplo se observa que **Sin Origen** concentra el 98% de las ventas en todas las categorías. Entre los canales digitales, **JUGUETES** es la categoría con mayor participación en canales identificados ($446K).

## Consideraciones importantes

- Los valores se expresan siempre en la **moneda de reporte** de la organización.
- Las **notas de crédito** se descuentan del total de cada combinación categoría-origen.
- Las facturas cuya orden de venta no tiene un origen asignado aparecen agrupadas bajo **"Sin Origen"**.
- Este dashboard resulta más útil cuando la organización registra el canal de origen en las órdenes de venta.
- Se recomienda utilizar la **vista de tabla** para analizar los datos con mayor detalle.
- Este dashboard es una variante de [Ventas Netas](./ventas-netas) desglosada por las dimensiones **Categoría de Producto** y **Origen de Orden**.
