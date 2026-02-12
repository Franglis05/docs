---
title: Ventas Netas por Vendedor y Cliente
category: Documentation
star: 9
sticky: 9
article: false
---

# Ventas Netas por Vendedor y Cliente

## Descripción

El dashboard **Ventas Netas por Vendedor y Cliente** presenta el importe total de ventas facturadas considerando las devoluciones (notas de crédito) como negativas, desglosado simultáneamente por vendedor y por cliente. Los valores se expresan en la moneda de reporte de la organización.

Este dashboard permite analizar la relación entre vendedores y clientes, identificando qué clientes gestiona cada vendedor y cómo se distribuye el volumen de ventas en cada combinación vendedor-cliente.

## ¿Cuándo se utiliza?

Se utiliza cuando la gerencia comercial necesita:
- Analizar la cartera de clientes de cada vendedor.
- Identificar la concentración de ventas por vendedor y por cliente.
- Detectar dependencias comerciales entre vendedores específicos y sus clientes principales.
- Evaluar la distribución de la fuerza de ventas respecto a la base de clientes.

## Acceso

Dashboards → Ventas → Ventas Netas por Vendedor y Cliente

**Rol requerido:** Gerente de Ventas

## Vista general

El dashboard muestra un indicador numérico con el total acumulado de ventas netas y un gráfico agrupado por vendedor, donde cada color representa un cliente diferente. Dado que este dashboard cruza 46 vendedores con 402 clientes, la leyenda de colores es muy extensa.

![Dashboard de Ventas Netas por Vendedor y Cliente en vista de línea](/assets/img/docs/dashboards/ventas-netas-por-vendedor-y-cliente-linea.png)

En la parte superior se presenta:
- **Título:** Ventas Netas por Vendedor y Cliente
- **Subtítulo:** Ventas netas por vendedor y cliente
- **Indicador principal:** valor total acumulado del período consultado (ej. $57,500,727)
- **Leyenda:** listado de clientes con su color asignado

En la esquina superior derecha se encuentran las opciones para cambiar la vista:
- Vista de tabla
- Selector de tipo de gráfica (Línea por defecto)

En la esquina superior izquierda se encuentra el [filtro de fechas](./#filtro-de-fechas) que permite definir el rango de consulta. Este filtro es común a todos los dashboards.

## Tipo de gráfica

- **Tipo:** Línea (recomendada) / Barras agrupadas
- **Eje Y:** Importe en moneda de reporte ($)
- **Eje X:** Vendedor
- **Colores:** cada cliente se representa con un color distinto en la leyenda

Debido a la gran cantidad de clientes (402 en el ejemplo), la gráfica de barras puede resultar difícil de interpretar visualmente. Se recomienda utilizar la **vista de línea** para obtener una mejor representación de los datos.

## Datos de ejemplo

La siguiente tabla muestra el resumen de los 10 vendedores con mayor volumen de ventas netas:

| Vendedor | Ventas Netas ($) |
|---------|-----------------:|
| Vendedor_84 | 10,597,401.24 |
| Vendedor_103 | 9,218,392.65 |
| Vendedor_104 | 8,337,271.78 |
| Vendedor_1820 | 4,191,263.55 |
| Vendedor_129 | 3,803,219.29 |
| Vendedor_100 | 3,378,174.09 |
| Vendedor_10 | 1,715,298.25 |
| Vendedor_1805 | 1,510,538.59 |
| Vendedor_109 | 1,306,035.58 |
| Vendedor_1804 | 1,185,877.00 |
| Otros (36 vendedores) | 12,257,255.41 |
| **Total** | **$57,500,727.43** |

En este ejemplo se observa que los 3 principales vendedores (**Vendedor_84**, **Vendedor_103** y **Vendedor_104**) concentran el 49% de las ventas totales, gestionando entre los tres aproximadamente $28M. En total, el dashboard cruza **46 vendedores** con **402 clientes**.

## Consideraciones importantes

- Los valores se expresan siempre en la **moneda de reporte** de la organización.
- Las **notas de crédito** se descuentan del total de cada combinación vendedor-cliente.
- Dado que este dashboard cruza dos dimensiones con gran cantidad de valores (46 vendedores × 402 clientes), la leyenda de colores es muy extensa. Se recomienda utilizar la **vista de tabla** para analizar los datos con mayor detalle, o cambiar a la **vista de línea** para una mejor representación gráfica.
- Este dashboard es una variante de [Ventas Netas](./ventas-netas) desglosada por las dimensiones **Vendedor** y **Cliente**.
