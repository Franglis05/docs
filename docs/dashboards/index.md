---
title: Dashboards
category: Documentation
star: 9
sticky: 9
article: false
---

# Dashboards

## Descripcion

Los **Dashboards** de Solop ERP proporcionan una vista consolidada de indicadores clave de gestión mediante gráficas interactivas, métricas numéricas y tablas comparativas. Permiten a los diferentes roles de la organización monitorear el desempeño operativo y financiero en tiempo real, facilitando la toma de decisiones basada en datos.

Cada dashboard presenta información relevante según el **área funcional** y el **rol del usuario**, asegurando que cada perfil acceda a los indicadores que le corresponden.

## Áreas disponibles

Los dashboards se organizan en las siguientes áreas funcionales:

### Ventas

Dashboards orientados al seguimiento de la actividad comercial, incluyendo ventas netas, márgenes, devoluciones, órdenes de venta y comparaciones entre períodos.

- [Ventas Netas](./ventas-netas)
- [Ventas Netas por Vendedor](./ventas-netas-por-vendedor)
- [Ventas Netas por Categoría de Producto](./ventas-netas-por-categoria-producto)
- [Ventas Netas por Grupo de Producto](./ventas-netas-por-grupo-producto)
- [Ventas Netas por Clase de Producto](./ventas-netas-por-clase-producto)
- [Ventas Netas por Cliente](./ventas-netas-por-cliente)
- [Ventas Netas por Proyecto](./ventas-netas-por-proyecto)
- [Ventas Netas por Contrato](./ventas-netas-por-contrato)
- [Ventas Netas por Región de Ventas](./ventas-netas-por-region-ventas)
- [Ventas Netas por Terminal PDV](./ventas-netas-por-terminal-pdv)
- [Ventas Netas por Origen de Orden](./ventas-netas-por-origen-orden)
- [Ventas Netas por Campaña](./ventas-netas-por-campana)
- [Ventas Netas por Organización](./ventas-netas-por-organizacion)
- [Ventas Netas por Categoría de Producto y Grupo de SDN](./ventas-netas-por-categoria-producto-y-grupo-sdn)
- [Ventas Netas por Categoría de Producto y Organización](./ventas-netas-por-categoria-producto-y-organizacion)
- [Ventas Netas por Vendedor y Cliente](./ventas-netas-por-vendedor-y-cliente)
- [Ventas Netas por Organización y Categoría de Producto](./ventas-netas-por-organizacion-y-categoria-producto)
- [Ventas Netas por Categoría de Producto y Origen de Orden](./ventas-netas-por-categoria-producto-y-origen)
- [Ventas Netas por Grupo de SDN y Categoría de Producto](./ventas-netas-por-grupo-sdn-y-categoria-producto)
- [Venta Diaria por Organización](./venta-diaria-por-organizacion)
- [Venta Diaria por Hora](./venta-diaria-por-hora)
- [Ventas Netas por Vendedor y Categoría de Producto](./ventas-netas-por-vendedor-y-categoria-producto)
- [Ventas Netas por Cliente y Categoría de Producto](./ventas-netas-por-cliente-y-categoria-producto)
- [Venta Diaria por Terminal PDV](./venta-diaria-por-terminal-pdv)
- [Venta Diaria por Categoría de Producto](./venta-diaria-por-categoria-producto)
- [Venta Diaria por Forma de Pago](./venta-diaria-por-forma-de-pago)
- [Venta Mensual por Forma de Pago](./venta-mensual-por-forma-de-pago)
- [Venta Diaria por Proveedor](./venta-diaria-por-proveedor)

**Roles con acceso:**

- **Gerente de Ventas:** acceso completo a indicadores de ventas netas en valor y unidades, márgenes brutos, rankings de clientes y productos, comparaciones mes a mes y año a año, devoluciones, órdenes de venta vencidas, forecast y métricas de servicios.
- **Operativos:** indicadores operativos de órdenes de venta, facturación, entregas pendientes y OTIF.

**Indicadores principales:**

| Indicador | Tipo | Descripción |
|-----------|------|-------------|
| Ventas Netas | Barras | Importe total de ventas facturadas considerando devoluciones (NC) como negativas |
| Ventas Netas por Vendedor | Barras | Ventas netas desglosadas por agente comercial |
| Ventas Netas por Categoría de Producto | Barras | Ventas netas agrupadas por categoría de producto |
| Ventas Netas por Cliente | Barras | Ventas netas agrupadas por socio del negocio |
| Venta Diaria por Organización | Línea | Monto de venta neta de cada día en moneda de reporte |
| Venta Total | Torta | Distribución de ventas en un mismo período entre diferentes criterios |
| Comparación de Ventas Mes con Mes anterior | Comparación | Ventas del mes actual vs. mes anterior |
| Comparación de Ventas YTD Actual vs YTD Año Anterior | Comparación | Ventas acumuladas del año contra el mismo período del año anterior |
| Ranking de Clientes | Planilla | Ranking de mayores ventas netas por cliente en moneda de reporte |
| Ranking de Productos | Planilla | Ranking de mayores ventas netas por producto en moneda de reporte |
| Gross Profit mensual | Comparación | Margen bruto mensual: ventas menos costo de ventas |
| Devoluciones por mes | Barra | Valor total de devoluciones de clientes en los meses seleccionados |
| Net Sales Units | Número | Cantidad facturada menos cantidad de notas de crédito del mes actual |
| Net Sales Amount | Número | Valor facturado menos valor de notas de crédito convertido a moneda de reporte |
| Customer count (active) | Número | Cantidad de clientes activos |

---

### Logística e Inventario

Dashboards orientados a la gestión de almacenes, entregas, recepciones y control de inventario.

**Roles con acceso:**

- **Gerente de Logística:** indicadores de recepciones, entregas OTIF, demoras, días de inventario, rotación de inventario y valorización de stock.
- **Gerente de Almacén:** indicadores operativos de recepciones pendientes.

**Indicadores principales:**

| Indicador | Tipo | Descripción |
|-----------|------|-------------|
| Cantidad entregas realizadas | Número | Total de entregas a clientes completadas |
| Entregas en tiempo y fuera de tiempo | Barra coloreada | OTIF de entregas: a tiempo vs. con retraso |
| Días demora entre entrega y orden de venta | Barra/Línea | Promedio ponderado en valor de los días de retraso por pedido |
| Total Inventory | Número | Valor total del inventario en todos los almacenes |
| Inventario por Almacén y categorías | Barra | Inventario de cada almacén coloreado por categoría |
| Días de Stock | Número | Unidades en inventario divididas entre el COGS del período |
| Rotación de Inventario | Planilla | Cantidad entregada neta dividida entre cantidad en inventario |
| Top 20 Alta/Baja Rotación | Planilla | Productos con mayor y menor rotación de inventario |
| Recepciones en tiempo y fuera de tiempo | Barra coloreada | Recepciones de proveedores a tiempo vs. con retraso |

---

### Requisiciones y Compras

Dashboards orientados al seguimiento de órdenes de compra, recepciones de proveedores y gastos de compras.

**Rol con acceso:**

- **Gerente de Compras:** indicadores de órdenes de compra abiertas, vencidas, recepciones completas e incompletas, compras COGS y gastos.

**Indicadores principales:**

| Indicador | Tipo | Descripción |
|-----------|------|-------------|
| OC recepcionadas completas y no completas | Barra | Cantidad de OC recepcionadas, diferenciando completas de parciales |
| OC vencidas no recepcionadas | Número | Órdenes de compra con fecha vencida sin recepción |
| OC Abiertas totales | Número | Cantidad y valor de OC abiertas por mes |
| Compras COGS mensuales | Barra | Valor de compras al costo por mes |
| Compras COGS por categoría | Barra | Costo de compras agrupado por categoría de producto |
| Compras COGS por Proveedor | Barra | Costo de compras agrupado por proveedor |

---

### Manufactura

Dashboards orientados al control de órdenes de producción y costos de manufactura.

**Rol con acceso:**

- **Gerente de Producción:** indicadores de órdenes de producción abiertas, en proceso, costos estimados vs. reales y cantidades producidas.

**Indicadores principales:**

| Indicador | Tipo | Descripción |
|-----------|------|-------------|
| OP no completas | Número | Órdenes de producción pendientes de completar |
| OP Abiertas | Número | Órdenes de producción abiertas |
| Producción artículos (cantidades) | Número | Cantidad de artículos producidos |
| Diferencia de producción plan/real (costos) | Comparación | Desvío entre costos planificados y costos reales |

---

### Financiero

Dashboards orientados a la gestión financiera: cuentas por pagar, cuentas por cobrar, tesorería, flujo de efectivo, gastos y proyectos.

**Roles con acceso:**

- **Gerente Financiero:** flujo de efectivo, ratios de liquidez, ciclo de conversión de efectivo.
- **Gerente de AP (Cuentas por Pagar):** antigüedad de deudas con proveedores, facturas pendientes de pago, necesidades de caja.
- **Gerente de AR (Cuentas por Cobrar):** antigüedad de deudas de clientes, atrasos de cobro, DSO, top deuda clientes.
- **Tesorería / Bancos:** saldos bancarios, pagos pendientes, posición de caja y flujos esperados.
- **Gastos:** gastos por departamento, composición del gasto y comparaciones con presupuesto.
- **Finanzas:** posición de caja, costos por proyecto, rentabilidad estimada por proyecto.
- **Project Manager:** proyectos activos, tareas vencidas, gastos vs. presupuesto.

**Indicadores principales:**

| Indicador | Tipo | Descripción |
|-----------|------|-------------|
| Flujo de efectivo neto | Línea | Flujo de efectivo neto de los últimos 6 meses |
| Antigüedad de Deudas Proveedores | Barras | Deudas por pagar agrupadas por rango de antigüedad |
| Antigüedad de Deudas Clientes | Barras | Deudas por cobrar agrupadas por rango de antigüedad y vendedor/grupo |
| Total saldo Cuentas Bancarias | Número | Saldo consolidado de todas las cuentas bancarias |
| Posición de caja | Gráfica | Posición de caja a lo largo del tiempo |
| Gastos por departamento | Barra | Gastos definidos por el usuario agrupados por departamento |
| Costos por proyecto | Grilla | Estimación de costos, costos a la fecha, OC y porcentaje faltante |
| Days Payable Outstanding (DPO) | Número | Días promedio de compra pendientes de pago |
| Days Sales Outstanding (DSO) | Número | Días de venta pendientes de cobro |

---

### Recursos Humanos

Dashboards orientados a la gestión de empleados, nómina, productividad y CRM.

**Roles con acceso:**

- **Recursos Humanos:** headcount, composición de empleados por tipo de contratación.
- **CRM:** leads, forecast, nuevas oportunidades, nuevos clientes.
- **Tiempo y Facturación:** revenue, profit, expenses, receivables, payables comparados entre períodos.

**Indicadores principales:**

| Indicador | Tipo | Descripción |
|-----------|------|-------------|
| Cantidad empleados Activos | Número | Total de empleados activos en la organización |
| Empleados por departamento | Número | Distribución de empleados activos por departamento |
| Gasto salarios por departamento | Barra | Total de gasto en salarios agrupado por departamento |
| Facturación por empleado directo | Ratio | Ingresos divididos entre empleados directos activos |
| Profit por empleado activo | Ratio | Ganancia dividida entre empleados activos |
| New Leads | Número | Nuevos leads ingresados al CRM |

---

## Tipos de gráficas

Los dashboards utilizan diferentes tipos de visualización según la naturaleza del indicador. Cada dashboard tiene un tipo de gráfica asignado por defecto, pero es posible cambiarlo utilizando el **selector de tipo de gráfica** ubicado en la esquina superior derecha de cada dashboard.

Al hacer clic sobre el selector se despliega un menú con los tipos de gráfica disponibles:

![Selector de tipo de gráfica con las opciones disponibles](/assets/img/docs/dashboards/selector-tipo-grafica.png)

Los tipos de gráfica disponibles son:

- **Línea:** gráfico de líneas para visualizar tendencias a lo largo del tiempo.
- **Barras:** gráfico de barras verticales para comparar valores entre categorías o períodos temporales.
- **Circular:** gráfico circular para mostrar la composición porcentual de un total.
- **Medidor:** indicador visual tipo velocímetro para representar un valor respecto a un rango.
- **Estadísticas:** valor numérico destacado, utilizado para KPIs de un solo valor (ej. ventas netas del mes, cantidad de clientes activos).
- **Cascada:** gráfico de cascada para visualizar cómo un valor inicial se ve afectado por incrementos y decrementos sucesivos.
- **Mapa de calor:** representación visual mediante colores para identificar concentraciones o patrones en los datos.
- **Burbujas:** gráfico de burbujas para representar tres dimensiones de datos (posición X, posición Y y tamaño de la burbuja).

La selección del tipo de gráfica se indica con una marca de verificación (✓) junto al tipo activo. El cambio de tipo de gráfica es temporal y aplica solo a la sesión actual del usuario.

Además del selector de tipo de gráfica, en la esquina superior derecha de cada dashboard se encuentran los botones para:
- **Descargar** los datos del dashboard.
- **Vista de tabla:** cambiar a una vista tabular de los datos.
- **Configuración adicional** del dashboard.

## Filtro de fechas

Todos los dashboards cuentan con un filtro de **rango de fechas** ubicado en la esquina superior izquierda de la pantalla. Este filtro permite definir el período de consulta para los datos presentados en el dashboard.

![Filtro de fecha en la barra superior del dashboard](/assets/img/docs/dashboards/filtro-de-fecha.png)

Al hacer clic sobre el selector de fechas, se despliega un calendario con dos meses visibles y opciones de rangos predefinidos en el lado izquierdo:

![Filtro de fecha expandido con calendario y rangos predefinidos](/assets/img/docs/dashboards/filtro-de-fecha-expandido.png)

Las opciones de rango predefinido disponibles son:

- **Últimos 7 días**
- **Últimos 14 días**
- **Últimos 30 días**
- **Últimos 3 meses**
- **Últimos 6 meses**
- **Último año**

También es posible seleccionar un rango personalizado haciendo clic en las fechas de inicio y fin directamente en el calendario.

La granularidad temporal en la que se presenta la información (diario, mensual, etc.) viene determinada por la definición de cada dashboard y no se modifica desde este filtro.
