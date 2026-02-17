---
title: Ventas Netas por Contrato
category: Documentation
star: 9
sticky: 9
article: false
---

# Ventas Netas por Contrato

## Descripción

El dashboard **Ventas Netas por Contrato** presenta el importe total de ventas facturadas considerando las devoluciones (notas de crédito) como negativas, desglosado por cada contrato de servicio asociado a las facturas. Los valores se expresan en la moneda de reporte de la organización.

Este dashboard permite dar seguimiento a los ingresos vinculados a contratos de servicio específicos, facilitando el control de la facturación contractual. Las facturas que no tienen un contrato asignado se agrupan bajo la etiqueta "Sin Contrato".

## ¿Cuándo se utiliza?

Se utiliza cuando la gerencia comercial necesita:
- Evaluar los ingresos por ventas asociados a cada contrato de servicio.
- Comparar el volumen de facturación entre diferentes contratos.
- Identificar la proporción de ventas no vinculadas a ningún contrato.
- Dar seguimiento a la facturación contractual a lo largo del tiempo.

## Acceso

Dashboards → Ventas → Ventas Netas por Contrato

**Rol requerido:** Gerente de Ventas

## Vista general

El dashboard muestra un indicador numérico con el total acumulado de ventas netas y un gráfico de barras agrupadas por mes, donde cada color representa un contrato diferente. En la parte superior del gráfico se presenta una leyenda con el nombre de cada contrato y su color correspondiente.

![Dashboard de Ventas Netas por Contrato en vista de barras](/assets/img/docs/dashboards/ventas-netas-por-contrato-barras.png)

En la parte superior se presenta:
- **Título:** Ventas Netas por Contrato
- **Subtítulo:** Ventas netas por contrato mon. reporte
- **Indicador principal:** valor total acumulado del período consultado (ej. $57,500,727)
- **Leyenda:** listado de contratos con su color asignado

En la esquina superior derecha se encuentran las opciones para cambiar la vista:
- Vista de tabla
- Selector de tipo de gráfica (Barras por defecto)

En la esquina superior izquierda se encuentra el [filtro de fechas](./#filtro-de-fechas) que permite definir el rango de consulta. Este filtro es común a todos los dashboards.

## Tipo de gráfica

- **Tipo:** Barras agrupadas
- **Eje Y:** Importe en moneda de reporte ($)
- **Eje X:** Período temporal (meses)
- **Colores:** cada contrato se representa con un color distinto en la leyenda

## Datos de ejemplo

| Contrato | Ventas Netas ($) |
|----------|-----------------:|
| Sin Contrato | 57,500,727.43 |
| **Total** | **57,500,727.43** |

En este ejemplo se observa que la totalidad de las ventas se encuentran bajo **"Sin Contrato"**, lo cual indica que las facturas del período no tienen un contrato de servicio asignado. Cuando la organización asocie contratos a las facturas de venta, el dashboard mostrará barras coloreadas por cada contrato, permitiendo comparar su contribución al total.

## Consideraciones importantes

- Los valores se expresan siempre en la **moneda de reporte** de la organización.
- Las **notas de crédito** se descuentan del total de cada contrato.
- Las facturas que no tienen un contrato asignado aparecen agrupadas bajo la etiqueta **"Sin Contrato"**.
- Este dashboard resulta más útil en organizaciones que gestionan ventas mediante contratos de servicio, ya que permite vincular ingresos a acuerdos comerciales específicos.
- Este dashboard es una variante de [Ventas Netas](./ventas-netas) desglosada por la dimensión **Contrato de Servicio**.
