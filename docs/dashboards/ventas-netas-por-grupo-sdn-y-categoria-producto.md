---
title: Ventas Netas por Grupo de SDN y Categoría de Producto
category: Documentation
star: 9
sticky: 9
article: false
---

# Ventas Netas por Grupo de SDN y Categoría de Producto

## Descripción

El dashboard **Ventas Netas por Grupo de SDN y Categoría de Producto** presenta el importe total de ventas facturadas considerando las devoluciones (notas de crédito) como negativas, desglosado simultáneamente por grupo de socio del negocio (SDN) y por categoría de producto. Los valores se expresan en la moneda de reporte de la organización.

Este dashboard permite analizar el mix de categorías de producto que compra cada grupo de clientes, identificando las preferencias y el perfil de consumo de cada segmento comercial.

## ¿Cuándo se utiliza?

Se utiliza cuando la gerencia comercial necesita:
- Analizar qué categorías de producto compra cada grupo de clientes.
- Identificar el perfil de consumo de cada segmento comercial.
- Detectar oportunidades de venta cruzada entre grupos de clientes y categorías de producto.
- Comparar la composición de ventas entre los diferentes segmentos de clientes.

## Acceso

Dashboards → Ventas → Ventas Netas por Grupo SDN y Cat. Prod.

**Rol requerido:** Gerente de Ventas

## Vista general

El dashboard muestra un indicador numérico con el total acumulado de ventas netas y un gráfico de barras agrupadas por grupo de SDN, donde cada color representa una categoría de producto diferente.

![Dashboard de Ventas Netas por Grupo de SDN y Categoría de Producto en vista de barras](/assets/img/docs/dashboards/ventas-netas-por-grupo-sdn-y-categoria-producto-barras.png)

En la parte superior se presenta:
- **Título:** Ventas Netas por Grupo SDN y Cat. Prod.
- **Subtítulo:** Ventas netas por grupo SDN y cat. prod.
- **Indicador principal:** valor total acumulado del período consultado (ej. $44,427,914)
- **Leyenda:** listado de categorías de producto con su color asignado

En la esquina superior derecha se encuentran las opciones para cambiar la vista:
- Vista de tabla
- Selector de tipo de gráfica (Barras por defecto)

En la esquina superior izquierda se encuentra el [filtro de fechas](./#filtro-de-fechas) que permite definir el rango de consulta. Este filtro es común a todos los dashboards.

## Tipo de gráfica

- **Tipo:** Barras agrupadas
- **Eje Y:** Importe en moneda de reporte ($)
- **Eje X:** Grupo de SDN
- **Colores:** cada categoría de producto se representa con un color distinto en la leyenda

## Datos de ejemplo

La siguiente tabla muestra las ventas netas por grupo de SDN, destacando las categorías principales:

| Grupo de SDN | ELECTRODOMESTICOS | JUGUETES | Otras categorías | Total |
|-------------|------------------:|---------:|-----------------:|------:|
| General | 1,611,282.92 | 11,022,105.11 | 4,429,771.42 | 17,063,159.45 |
| EMPRESA NO DEFINIDA | 11,375,713.80 | 1,062,865.70 | 776,128.93 | 13,214,708.43 |
| SUPERMERCADOS | 4,678,092.28 | 0.00 | 178,512.81 | 4,856,605.09 |
| Clientes | 2,502,408.73 | 153,491.25 | 694,107.35 | 3,350,007.33 |
| Proveedores | 0.00 | 2,258,102.88 | 0.00 | 2,258,102.88 |
| WEB | 90,272.74 | 479,289.98 | 442,013.33 | 1,011,576.05 |
| CASA ELECTRODOMESTICOS | 763,851.08 | 0.00 | 14,902.45 | 778,753.53 |
| MUEBLERIA Y ELECTRODOMESTICOS | 450,442.78 | 0.00 | 51,301.17 | 501,743.96 |
| Otros (12 grupos) | 945,796.31 | 236,899.98 | 210,561.45 | 1,393,257.75 |
| **Total** | **22,417,860.64** | **15,212,754.90** | **6,797,298.91** | **$44,427,914.47** |

En este ejemplo se observa que el grupo **General** lidera con $17M, concentrando la mayor parte de las ventas de JUGUETES ($11M). **EMPRESA NO DEFINIDA** ocupa el segundo lugar con $13.2M, dominado por ELECTRODOMESTICOS ($11.4M). **SUPERMERCADOS** presenta un perfil casi exclusivamente de ELECTRODOMESTICOS ($4.7M).

## Consideraciones importantes

- Los valores se expresan siempre en la **moneda de reporte** de la organización.
- Las **notas de crédito** se descuentan del total de cada combinación grupo-categoría. Un grupo puede presentar un saldo negativo en alguna categoría si las devoluciones superan las ventas.
- Este dashboard muestra la misma información que [Ventas Netas por Categoría de Producto y Grupo de SDN](./ventas-netas-por-categoria-producto-y-grupo-sdn) pero con las dimensiones invertidas: aquí el grupo de SDN está en el eje X y la categoría de producto se representa con colores.
- Se recomienda utilizar la **vista de tabla** para analizar los datos con mayor detalle dado la cantidad de grupos y categorías.
- Este dashboard es una variante de [Ventas Netas](./ventas-netas) desglosada por las dimensiones **Grupo de SDN** y **Categoría de Producto**.
