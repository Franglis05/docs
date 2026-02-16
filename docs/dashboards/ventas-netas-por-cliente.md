---
title: Ventas Netas por Cliente
category: Documentation
star: 9
sticky: 9
article: false
---

# Ventas Netas por Cliente

## Descripción

El dashboard **Ventas Netas por Cliente** presenta el importe total de ventas facturadas considerando las devoluciones (notas de crédito) como negativas, desglosado por cada socio del negocio (cliente). Los valores se expresan en la moneda de reporte de la organización.

Este dashboard permite identificar los clientes con mayor volumen de compras, analizar la concentración de ventas y detectar la dependencia comercial respecto a clientes específicos.

## ¿Cuándo se utiliza?

Se utiliza cuando la gerencia comercial necesita:
- Evaluar el volumen de ventas por cliente en un período determinado.
- Identificar los clientes más relevantes para la organización.
- Analizar la concentración de ventas y la dependencia de clientes principales.
- Detectar clientes con saldo negativo por devoluciones que superan las ventas.

## Acceso

Dashboards → Ventas → Ventas Netas por Cliente

**Rol requerido:** Gerente de Ventas

## Vista general

El dashboard muestra un indicador numérico con el total acumulado de ventas netas y un gráfico de barras agrupadas por mes, donde cada color representa un cliente diferente. En la parte superior del gráfico se presenta una leyenda con el nombre de cada cliente y su color correspondiente.

![Dashboard de Ventas Netas por Cliente en vista de barras](/assets/img/docs/dashboards/ventas-netas-por-cliente-barras.png)

En la parte superior se presenta:
- **Título:** Ventas Netas por Cliente
- **Subtítulo:** Ventas netas por cliente mon. reporte
- **Indicador principal:** valor total acumulado del período consultado (ej. $57,525,127)
- **Leyenda:** listado de clientes con su color asignado

En la esquina superior derecha se encuentran las opciones para cambiar la vista:
- Vista de tabla
- Selector de tipo de gráfica (Barras por defecto)

En la esquina superior izquierda se encuentra el [filtro de fechas](./#filtro-de-fechas) que permite definir el rango de consulta. Este filtro es común a todos los dashboards.

## Tipo de gráfica

- **Tipo:** Barras agrupadas
- **Eje Y:** Importe en moneda de reporte ($)
- **Eje X:** Período temporal (meses)
- **Colores:** cada cliente se representa con un color distinto en la leyenda

## Datos de ejemplo

La siguiente tabla muestra el resumen de los 10 clientes con mayor volumen de ventas netas en el período consultado:

| Cliente | Ventas Netas ($) |
|---------|-----------------|
| SOCIO_22 | 15,308,954.38 |
| SOCIO_4467 | 8,319,612.63 |
| SOCIO_4426 | 2,754,885.52 |
| SOCIO_117 | 1,753,743.36 |
| SOCIO_2602 | 1,743,120.62 |
| SOCIO_2652 | 1,682,309.69 |
| SOCIO_4564 | 1,310,621.32 |
| SOCIO_24 | 1,291,347.98 |
| SOCIO_2410 | 1,229,262.47 |
| SOCIO_4411 | 1,221,268.36 |
| Otros (392 clientes) | 20,910,001.10 |
| **Total** | **57,525,127.43** |

En este ejemplo se observa que el top 10 de clientes concentra aproximadamente el 64% de las ventas totales. En total, el dashboard desglosa las ventas en **402 clientes** diferentes.

## Consideraciones importantes

- Los valores se expresan siempre en la **moneda de reporte** de la organización.
- Las **notas de crédito** se descuentan del total de cada cliente. Un cliente puede presentar un saldo negativo si las devoluciones superan las ventas en el período consultado.
- Dado que este dashboard puede presentar una gran cantidad de clientes (402 en el ejemplo), la leyenda de colores resulta muy extensa. Se recomienda utilizar la **vista de tabla** para analizar los datos con mayor detalle.
- Este dashboard es una variante de [Ventas Netas](./ventas-netas) desglosada por la dimensión **Socio del Negocio (Cliente)**.
