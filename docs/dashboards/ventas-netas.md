---
title: Ventas Netas
category: Documentation
star: 9
sticky: 9
article: false
---

# Ventas Netas

## Descripción

El dashboard **Ventas Netas** presenta el importe total de ventas facturadas considerando las devoluciones (notas de crédito) como negativas. Los valores se expresan en la moneda de reporte de la organización, permitiendo una vista consolidada del desempeño comercial independientemente de la moneda original de cada transacción.

La fórmula de cálculo es:

**Ventas Netas = Valor Facturado - Valor Notas de Crédito**

## ¿Cuándo se utiliza?

Se utiliza cuando la gerencia comercial necesita:
- Evaluar el volumen total de ventas en un período determinado.
- Identificar tendencias de crecimiento o disminución en las ventas mes a mes.
- Comparar el desempeño de ventas entre diferentes períodos temporales.
- Obtener una cifra consolidada de ingresos netos que descuente las devoluciones.

## Acceso

Dashboards → Ventas → Ventas Netas

**Rol requerido:** Gerente de Ventas

## Vista general

El dashboard muestra un indicador numérico con el total acumulado de ventas netas y un gráfico de barras con el desglose temporal.

![Dashboard de Ventas Netas en vista de barras](/assets/img/docs/dashboards/ventas-netas-barras.png)

En la parte superior se presenta:
- **Título:** Ventas Netas
- **Subtítulo:** Ventas netas en moneda de reporte
- **Indicador principal:** valor total acumulado del período consultado (ej. $57,525,127)

## Tipo de gráfica

- **Tipo:** Barras
- **Eje Y:** Importe en moneda de reporte ($)
- **Eje X:** Período temporal (meses)

En la esquina superior derecha se encuentran las opciones para cambiar la vista:
- Vista de tabla
- Selector de tipo de gráfica (Barras por defecto)

En la esquina superior izquierda se encuentra el [filtro de fechas](./#filtro-de-fechas) que permite definir el rango de consulta. Este filtro es común a todos los dashboards.

## Datos de ejemplo

La siguiente tabla muestra los datos correspondientes al dashboard ilustrado:

| Período | Ventas Netas ($) |
|---------|-----------------:|
| 2025-09 | 0.00 |
| 2025-10 | 29,486,774.63 |
| 2025-11 | 26,890,382.10 |
| 2025-12 | 1,123,570.70 |
| 2026-01 | 24,400.00 |
| **Total** | **57,525,127.43** |

En este ejemplo se observa que los meses de octubre y noviembre de 2025 concentran la mayor parte de las ventas del período, mientras que diciembre muestra una caída significativa y enero de 2026 registra un valor mínimo correspondiente al inicio del mes.

## Variantes relacionadas

El indicador de Ventas Netas cuenta con múltiples variantes que permiten desglosar la información por diferentes dimensiones:

### Por una dimensión

| Dashboard | Dimensión |
|-----------|-----------|
| [Ventas Netas por Vendedor](./ventas-netas-por-vendedor) | Vendedor |
| [Ventas Netas por Categoría de Producto](./ventas-netas-por-categoria-producto) | Categoría de Producto |
| [Ventas Netas por Grupo de Producto](./ventas-netas-por-grupo-producto) | Grupo de Producto |
| [Ventas Netas por Clase de Producto](./ventas-netas-por-clase-producto) | Clase de Producto |
| [Ventas Netas por Cliente](./ventas-netas-por-cliente) | Socio del Negocio |
| [Ventas Netas por Proyecto](./ventas-netas-por-proyecto) | Proyecto |
| [Ventas Netas por Contrato](./ventas-netas-por-contrato) | Contrato de Servicio |
| [Ventas Netas por Región de Ventas](./ventas-netas-por-region-ventas) | Región de Venta |
| [Ventas Netas por Terminal PDV](./ventas-netas-por-terminal-pdv) | Terminal PDV |
| [Ventas Netas por Origen de Orden](./ventas-netas-por-origen-orden) | Origen de Orden |
| [Ventas Netas por Campaña](./ventas-netas-por-campana) | Campaña |
| [Ventas Netas por Organización](./ventas-netas-por-organizacion) | Organización |

### Por dos dimensiones

| Dashboard | Dimensiones |
|-----------|-------------|
| [Ventas Netas por Organización y Categoría de Producto](./ventas-netas-por-organizacion-y-categoria-producto) | Organización + Categoría |
| [Ventas Netas por Vendedor y Cliente](./ventas-netas-por-vendedor-y-cliente) | Vendedor + Cliente |
| [Ventas Netas por Categoría de Producto y Origen de Orden](./ventas-netas-por-categoria-producto-y-origen) | Categoría + Origen |
| [Ventas Netas por Grupo de SDN y Categoría de Producto](./ventas-netas-por-grupo-sdn-y-categoria-producto) | Grupo SDN + Categoría |
| [Ventas Netas por Categoría de Producto y Grupo de SDN](./ventas-netas-por-categoria-producto-y-grupo-sdn) | Categoría + Grupo SDN |
| [Ventas Netas por Categoría de Producto y Organización](./ventas-netas-por-categoria-producto-y-organizacion) | Categoría + Organización |
| [Ventas Netas por Vendedor y Categoría de Producto](./ventas-netas-por-vendedor-y-categoria-producto) | Vendedor + Categoría |
| [Ventas Netas por Cliente y Categoría de Producto](./ventas-netas-por-cliente-y-categoria-producto) | Cliente + Categoría |

### Ventas Netas Acumuladas

Las variantes acumuladas muestran el total progresivo a lo largo del tiempo:

- Ventas Netas Acumuladas
- Ventas Netas Acumuladas por Vendedor
- Ventas Netas Acumuladas por Categoría de Producto
- Ventas Netas Acumuladas por Cliente
- Ventas Netas Acumuladas por Cliente y Categoría de Producto

## Consideraciones importantes

- Los valores se expresan siempre en la **moneda de reporte** de la organización, independientemente de la moneda original de la factura.
- Las **notas de crédito** se descuentan del total, por lo que el dashboard refleja ventas netas reales.
- Un mes con valor **$0** indica que no hubo actividad de facturación en ese período o que las devoluciones anularon completamente las ventas.
- Los datos se actualizan conforme se completan las facturas y notas de crédito en el sistema.
