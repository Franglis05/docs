---
title: Ventas Netas por Proyecto
category: Documentation
star: 9
sticky: 9
article: false
---

# Ventas Netas por Proyecto

## Descripción

El dashboard **Ventas Netas por Proyecto** presenta el importe total de ventas facturadas considerando las devoluciones (notas de crédito) como negativas, desglosado por cada proyecto asociado a las facturas. Los valores se expresan en la moneda de reporte de la organización.

Este dashboard permite analizar las ventas vinculadas a proyectos específicos, facilitando el seguimiento de ingresos por proyecto. Las facturas que no tienen un proyecto asignado se agrupan bajo la etiqueta "Sin Proyecto".

## ¿Cuándo se utiliza?

Se utiliza cuando la gerencia comercial necesita:
- Evaluar los ingresos por ventas asociados a cada proyecto.
- Comparar el volumen de ventas entre diferentes proyectos.
- Identificar la proporción de ventas no vinculadas a ningún proyecto.
- Dar seguimiento a la facturación de proyectos específicos a lo largo del tiempo.

## Acceso

Dashboards → Ventas → Ventas Netas por Proyecto

**Rol requerido:** Gerente de Ventas

## Vista general

El dashboard muestra un indicador numérico con el total acumulado de ventas netas y un gráfico de barras agrupadas por mes, donde cada color representa un proyecto diferente. En la parte superior del gráfico se presenta una leyenda con el nombre de cada proyecto y su color correspondiente.

![Dashboard de Ventas Netas por Proyecto en vista de barras](/assets/img/docs/dashboards/ventas-netas-por-proyecto-barras.png)

En la parte superior se presenta:
- **Título:** Ventas Netas por Proyecto
- **Subtítulo:** Ventas netas por proyecto mon. reporte
- **Indicador principal:** valor total acumulado del período consultado (ej. $57,500,727)
- **Leyenda:** listado de proyectos con su color asignado

En la esquina superior derecha se encuentran las opciones para cambiar la vista:
- Vista de tabla
- Selector de tipo de gráfica (Barras por defecto)

En la esquina superior izquierda se encuentra el [filtro de fechas](./#filtro-de-fechas) que permite definir el rango de consulta. Este filtro es común a todos los dashboards.

## Tipo de gráfica

- **Tipo:** Barras agrupadas
- **Eje Y:** Importe en moneda de reporte ($)
- **Eje X:** Período temporal (meses)
- **Colores:** cada proyecto se representa con un color distinto en la leyenda

## Datos de ejemplo

| Proyecto | Ventas Netas ($) |
|----------|-----------------:|
| Sin Proyecto | 57,500,727.43 |
| **Total** | **57,500,727.43** |

En este ejemplo se observa que la totalidad de las ventas se encuentran bajo **"Sin Proyecto"**, lo cual indica que las facturas del período no tienen un proyecto asignado. Cuando la organización asocie proyectos a las facturas de venta, el dashboard mostrará barras coloreadas por cada proyecto, permitiendo comparar su contribución al total.

## Consideraciones importantes

- Los valores se expresan siempre en la **moneda de reporte** de la organización.
- Las **notas de crédito** se descuentan del total de cada proyecto.
- Las facturas que no tienen un proyecto asignado aparecen agrupadas bajo la etiqueta **"Sin Proyecto"**.
- Este dashboard resulta más útil en organizaciones que gestionan ventas por proyecto, ya que permite vincular ingresos a iniciativas comerciales específicas.
- Este dashboard es una variante de [Ventas Netas](./ventas-netas) desglosada por la dimensión **Proyecto**.
