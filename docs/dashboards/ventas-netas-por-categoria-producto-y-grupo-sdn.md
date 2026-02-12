---
title: Ventas Netas por Categoría de Producto y Grupo de SDN
category: Documentation
star: 9
sticky: 9
article: false
---

# Ventas Netas por Categoría de Producto y Grupo de SDN

## Descripción

El dashboard **Ventas Netas por Categoría de Producto y Grupo de SDN** presenta el importe total de ventas facturadas considerando las devoluciones (notas de crédito) como negativas, desglosado simultáneamente por categoría de producto y por grupo de socio del negocio (SDN). Los valores se expresan en la moneda de reporte de la organización.

Este dashboard permite analizar cómo se distribuyen las ventas de cada categoría de producto entre los diferentes grupos de clientes, identificando qué tipo de cliente compra más en cada categoría.

## ¿Cuándo se utiliza?

Se utiliza cuando la gerencia comercial necesita:
- Analizar qué grupos de clientes generan mayor volumen de compras en cada categoría de producto.
- Identificar oportunidades comerciales cruzando categorías de producto con segmentos de clientes.
- Detectar concentración de ventas en combinaciones específicas de categoría y grupo de cliente.
- Evaluar la penetración de cada categoría de producto en los diferentes segmentos comerciales.

## Acceso

Dashboards → Ventas → Ventas Netas por Cat. Prod. y Grupo SDN

**Rol requerido:** Gerente de Ventas

## Vista general

El dashboard muestra un indicador numérico con el total acumulado de ventas netas y un gráfico de barras agrupadas por categoría de producto, donde cada color representa un grupo de socio del negocio diferente.

![Dashboard de Ventas Netas por Categoría de Producto y Grupo de SDN en vista de barras](/assets/img/docs/dashboards/ventas-netas-por-categoria-producto-y-grupo-sdn-barras.png)

En la parte superior se presenta:
- **Título:** Ventas Netas por Cat. Prod. y Grupo SDN
- **Subtítulo:** Ventas netas por cat. prod. y grupo SDN
- **Indicador principal:** valor total acumulado del período consultado (ej. $44,427,914)
- **Leyenda:** listado de grupos de SDN con su color asignado

En la esquina superior derecha se encuentran las opciones para cambiar la vista:
- Vista de tabla
- Selector de tipo de gráfica (Barras por defecto)

En la esquina superior izquierda se encuentra el [filtro de fechas](./#filtro-de-fechas) que permite definir el rango de consulta. Este filtro es común a todos los dashboards.

## Tipo de gráfica

- **Tipo:** Barras agrupadas
- **Eje Y:** Importe en moneda de reporte ($)
- **Eje X:** Categoría de producto
- **Colores:** cada grupo de SDN se representa con un color distinto en la leyenda

## Datos de ejemplo

La siguiente tabla muestra el total de ventas netas por categoría de producto:

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
| INSUMOS | 75,784.77 |
| MATERIAL DIDACTICO | 42,668.22 |
| SERVICIO | -427,000.00 |
| **Total** | **$44,427,914.47** |

Dentro de cada categoría, las ventas se desglosan por grupo de SDN. Los principales grupos que aparecen en el dashboard son: EMPRESA NO DEFINIDA, SUPERMERCADOS, BAZAR Y ELECTROS, CASA ELECTRODOMESTICOS, Clientes, Proveedores, General, WEB, entre otros.

En este ejemplo se observa que **ELECTRODOMESTICOS** y **JUGUETES** concentran el 85% de las ventas totales. La categoría **SERVICIO** presenta un valor negativo debido a notas de crédito que superan la facturación en el período.

## Consideraciones importantes

- Los valores se expresan siempre en la **moneda de reporte** de la organización.
- Las **notas de crédito** se descuentan del total de cada combinación categoría-grupo. Una categoría puede presentar un saldo negativo si las devoluciones superan las ventas.
- Dado que este dashboard cruza dos dimensiones, la leyenda de colores puede resultar extensa. Se recomienda utilizar la **vista de tabla** para analizar los datos con mayor detalle.
- Este dashboard es una variante de [Ventas Netas](./ventas-netas) desglosada por las dimensiones **Categoría de Producto** y **Grupo de SDN**.
