---
title: Ventas Netas por Vendedor
category: Documentation
star: 9
sticky: 9
article: false
---

# Ventas Netas por Vendedor

## Descripción

El dashboard **Ventas Netas por Vendedor** presenta el importe total de ventas facturadas considerando las devoluciones (notas de crédito) como negativas, desglosado por cada agente comercial o vendedor asignado. Los valores se expresan en la moneda de reporte de la organización.

Este dashboard permite identificar el aporte individual de cada vendedor al total de ventas netas, facilitando la evaluación de desempeño del equipo comercial.

## ¿Cuándo se utiliza?

Se utiliza cuando la gerencia comercial necesita:
- Evaluar el desempeño individual de cada vendedor en un período determinado.
- Comparar la contribución de ventas entre los diferentes agentes comerciales.
- Identificar los vendedores con mayor y menor volumen de ventas.
- Detectar vendedores con saldo negativo por devoluciones que superan las ventas.

## Acceso

Dashboards → Ventas → Ventas Netas por Vendedor

**Rol requerido:** Gerente de Ventas

## Vista general

El dashboard muestra un indicador numérico con el total acumulado de ventas netas y un gráfico de barras agrupadas por mes, donde cada color representa a un vendedor diferente. En la parte superior del gráfico se presenta una leyenda con el nombre de cada vendedor y su color correspondiente.

![Dashboard de Ventas Netas por Vendedor en vista de barras](/assets/img/docs/dashboards/ventas-netas-por-vendedor-barras.png)

En la parte superior se presenta:
- **Título:** Ventas Netas por Vendedor
- **Subtítulo:** Ventas netas por vendedor en moneda de reporte
- **Indicador principal:** valor total acumulado del período consultado (ej. $57,525,127)
- **Leyenda:** listado de vendedores con su color asignado

En la esquina superior derecha se encuentran las opciones para cambiar la vista:
- Vista de tabla
- Selector de tipo de gráfica (Barras por defecto)

En la esquina superior izquierda se encuentra el [filtro de fechas](./#filtro-de-fechas) que permite definir el rango de consulta. Este filtro es común a todos los dashboards.

## Tipo de gráfica

- **Tipo:** Barras agrupadas
- **Eje Y:** Importe en moneda de reporte ($)
- **Eje X:** Período temporal (meses)
- **Colores:** cada vendedor se representa con un color distinto en la leyenda

## Datos de ejemplo

La siguiente tabla muestra el resumen de los 10 vendedores con mayor volumen de ventas netas en el período consultado:

| Vendedor | Ventas Netas ($) |
|----------|-----------------|
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
| Otros (38 vendedores) | 13,281,655.41 |
| **Total** | **57,525,127.43** |

El desglose mensual de los principales vendedores es el siguiente:

| Vendedor | 2025-09 | 2025-10 | 2025-11 | 2025-12 | 2026-01 |
|----------|---------|---------|---------|---------|---------|
| Vendedor_84 | 0 | 5,665,929.38 | 4,720,545.83 | 210,926.03 | 0 |
| Vendedor_103 | 0 | 3,970,434.66 | 4,883,343.23 | 364,614.76 | 0 |
| Vendedor_104 | 0 | 3,414,540.32 | 4,758,333.90 | 164,397.56 | 0 |
| Vendedor_1820 | 0 | 2,716,471.33 | 1,420,563.57 | 54,228.65 | 0 |
| Vendedor_129 | 0 | 1,984,110.77 | 1,757,408.22 | 61,700.30 | 0 |
| Vendedor_100 | 0 | 3,032,911.95 | 345,262.14 | 0 | 0 |

En este ejemplo se observa que los meses de octubre y noviembre de 2025 concentran la actividad de ventas para todos los vendedores, mientras que septiembre no registra actividad y enero de 2026 presenta valores mínimos.

## Consideraciones importantes

- Los valores se expresan siempre en la **moneda de reporte** de la organización.
- Las **notas de crédito** se descuentan del total de cada vendedor. Un vendedor puede presentar un saldo negativo si las devoluciones superan las ventas en el período consultado.
- La leyenda de colores permite identificar visualmente la contribución de cada vendedor en las barras del gráfico.
- Este dashboard es una variante de [Ventas Netas](./ventas-netas) desglosada por la dimensión **Vendedor**.
