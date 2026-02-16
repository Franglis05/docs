---
title: Ventas Netas por Cliente y Categoría de Producto
category: Documentation
star: 9
sticky: 9
article: false
---

# Ventas Netas por Cliente y Categoría de Producto

## Descripción

El dashboard **Ventas Netas por Cliente y Categoría de Producto** presenta el importe total de ventas facturadas considerando las devoluciones (notas de crédito) como negativas, desglosado simultáneamente por cliente y por categoría de producto. Los valores se expresan en la moneda de reporte de la organización.

Este dashboard permite analizar el mix de productos que compra cada cliente, identificando las preferencias de consumo y la concentración de ventas por categoría en cada socio del negocio.

## ¿Cuándo se utiliza?

Se utiliza cuando la gerencia comercial necesita:
- Analizar qué categorías de producto compra cada cliente.
- Identificar el perfil de consumo de los principales clientes.
- Detectar oportunidades de venta cruzada ofreciendo nuevas categorías a clientes existentes.
- Evaluar la concentración de ventas por categoría en clientes específicos.

## Acceso

Dashboards → Ventas → Ventas Netas por Cliente y Cat. Prod.

**Rol requerido:** Gerente de Ventas

## Vista general

El dashboard muestra un indicador numérico con el total acumulado de ventas netas y un gráfico de barras agrupadas por cliente, donde cada color representa una categoría de producto diferente.

![Dashboard de Ventas Netas por Cliente y Categoría de Producto en vista de barras](/assets/img/docs/dashboards/ventas-netas-por-cliente-y-categoria-producto-barras.png)

En la parte superior se presenta:
- **Título:** Ventas Netas por Cliente y Cat. Prod.
- **Subtítulo:** Ventas netas por cliente y cat. prod.
- **Indicador principal:** valor total acumulado del período consultado (ej. $44,427,914)
- **Leyenda:** listado de categorías de producto con su color asignado

En la esquina superior derecha se encuentran las opciones para cambiar la vista:
- Vista de tabla
- Selector de tipo de gráfica (Barras por defecto)

En la esquina superior izquierda se encuentra el [filtro de fechas](./#filtro-de-fechas) que permite definir el rango de consulta. Este filtro es común a todos los dashboards.

## Tipo de gráfica

- **Tipo:** Barras agrupadas
- **Eje Y:** Importe en moneda de reporte ($)
- **Eje X:** Cliente
- **Colores:** cada categoría de producto se representa con un color distinto en la leyenda

## Datos de ejemplo

La siguiente tabla muestra los 10 clientes con mayor volumen de ventas netas:

| Cliente | Ventas Netas ($) |
|--------|-----------------:|
| SOCIO_22 | 15,239,173.61 |
| SOCIO_4426 | 2,258,102.88 |
| SOCIO_2602 | 1,443,091.39 |
| SOCIO_117 | 1,437,496.50 |
| SOCIO_2652 | 1,378,942.38 |
| SOCIO_4564 | 1,113,509.18 |
| SOCIO_24 | 1,066,963.93 |
| SOCIO_2410 | 1,056,662.19 |
| SOCIO_2409 | 1,018,826.41 |
| SOCIO_4411 | 1,003,725.26 |
| Otros (377 clientes) | 17,411,420.74 |
| **Total** | **$44,427,914.47** |

En este ejemplo se observa que **SOCIO_22** concentra el 34% de las ventas totales ($15.2M), con un perfil diversificado que incluye JUGUETES ($10.7M), PUERICULTURA ($1.6M), RODADOS ($1M) y DEPORTES ($636K), entre otras categorías. **SOCIO_4426** se especializa exclusivamente en JUGUETES ($2.3M). En total, el dashboard desglosa las ventas de **387 clientes**.

## Consideraciones importantes

- Los valores se expresan siempre en la **moneda de reporte** de la organización.
- Las **notas de crédito** se descuentan del total de cada combinación cliente-categoría.
- Dado que este dashboard presenta una gran cantidad de clientes (387 en el ejemplo), se recomienda utilizar la **vista de tabla** para analizar los datos con mayor detalle.
- Este dashboard es una variante de [Ventas Netas](./ventas-netas) desglosada por las dimensiones **Cliente** y **Categoría de Producto**.
