---
title: Venta Diaria por Hora
category: Documentation
star: 9
sticky: 9
article: false
---

# Venta Diaria por Hora

## Descripción

El dashboard **Venta Diaria por Hora** presenta el monto de venta neta agrupado por hora del día. Los valores se expresan en la moneda de reporte de la organización.

Este dashboard permite identificar las horas de mayor y menor actividad comercial durante el día, facilitando decisiones operativas relacionadas con dotación de personal, horarios de atención y estrategias de promoción.

## ¿Cuándo se utiliza?

Se utiliza cuando la gerencia comercial necesita:
- Identificar las horas pico de venta durante el día.
- Analizar la distribución horaria de la facturación.
- Optimizar la dotación de personal según las horas de mayor actividad.
- Planificar promociones o actividades comerciales en franjas horarias específicas.

## Acceso

Dashboards → Ventas → Venta Diaria por Hora

**Rol requerido:** Gerente de Ventas

## Vista general

El dashboard muestra un indicador numérico con el total de ventas del período y un gráfico de línea que representa el volumen de ventas en cada hora del día.

![Dashboard de Venta Diaria por Hora en vista de línea](/assets/img/docs/dashboards/venta-diaria-por-hora-linea.png)

En la parte superior se presenta:
- **Título:** Venta Diaria por Hora
- **Subtítulo:** Venta por hora del día
- **Indicador principal:** valor total del período consultado (ej. $489,998)

En la esquina superior derecha se encuentran las opciones para cambiar la vista:
- Vista de tabla
- Selector de tipo de gráfica (Línea por defecto)

En la esquina superior izquierda se encuentra el [filtro de fechas](./#filtro-de-fechas) que permite definir el rango de consulta. Este filtro es común a todos los dashboards. Se recomienda **filtrar por un solo día** para visualizar correctamente la distribución de ventas por hora de ese día específico.

## Tipo de gráfica

- **Tipo:** Línea
- **Eje Y:** Importe en moneda de reporte ($)
- **Eje X:** Hora del día (formato 24h)
- **Área:** el área bajo la curva se muestra sombreada para facilitar la visualización del volumen

## Datos de ejemplo

La siguiente tabla muestra las ventas por hora para un día específico:

| Hora | Ventas ($) |
|------|----------:|
| 08:00 | 310.00 |
| 09:00 | 1,076.50 |
| 10:00 | 6,713.00 |
| 11:00 | 9,055.95 |
| 12:00 | 19,991.63 |
| 13:00 | 22,830.05 |
| 14:00 | 160,817.25 |
| 15:00 | 31,264.31 |
| 16:00 | 30,827.85 |
| 17:00 | 147,462.74 |
| 18:00 | 26,451.50 |
| 19:00 | 9,608.10 |
| 20:00 | 15,535.00 |
| 21:00 | 8,054.50 |
| **Total** | **$489,998.38** |

En este ejemplo se observan dos picos de venta claramente diferenciados: uno a las **14:00** con $160,817 y otro a las **17:00** con $147,462. Juntos, estos dos picos representan el 63% de las ventas del día. La actividad comercial comienza a incrementarse a partir de las 12:00 y disminuye significativamente después de las 18:00.

## Consideraciones importantes

- Los valores se expresan siempre en la **moneda de reporte** de la organización.
- Se recomienda **filtrar por un solo día** en el selector de fechas para visualizar correctamente la distribución horaria de ventas. Al seleccionar múltiples días, los valores se acumulan por hora y el gráfico muestra el consolidado, lo cual puede dificultar la interpretación.
- Las horas sin actividad de facturación no aparecen en el gráfico.
- La hora indicada corresponde a la hora de creación de la factura en el sistema.
