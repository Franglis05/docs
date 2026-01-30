# Estructura del Proyecto Solop Docs

## Módulos Disponibles

| Módulo | Carpeta | Descripción |
|--------|---------|-------------|
| Reglas Básicas | `basic-rules` | Configuraciones fundamentales del sistema |
| Datos Maestros | `master-data` | Socios de negocio, productos, listas de precios |
| Facturación Electrónica | `electronic-billing` | CFE, configuración fiscal |
| Gestión Contable | `accounting-management` | Plan de cuentas, asientos, reportes contables |
| Gestión de Compras | `purchase-management` | Órdenes de compra, recepciones, facturas proveedor |
| Gestión de Devoluciones | `return-management` | RMA, notas de crédito |
| Gestión de Distribución | `distribution-management` | Rutas, entregas, logística |
| Gestión de Materiales | `material-management` | Inventario, movimientos, ajustes |
| Gestión de Producción | `production-management` | Órdenes de producción, BOM |
| Gestión de PDV | `pdv-management` | Punto de venta, cajas, turnos |
| Gestión Humana | `human-management` | Empleados, nómina |
| Gestión de Relación con Clientes | `customer-relationship-management` | CRM, oportunidades |
| Gestión de Saldos Pendientes | `balance-management` | Cuentas por cobrar/pagar, cobranzas |
| Gestión de Ventas | `sales-management` | Órdenes de venta, facturas, entregas |
| Gestión Financiera | `financial-management` | Bancos, pagos, conciliaciones |
| Gestión de Activos | `asset-management` | Activos fijos, depreciación |
| Preguntas Frecuentes | `frequently-asked-questions` | FAQ por módulo |
| Verticales | `verticals` | Soluciones específicas por industria |
| Dispositivos | `devices` | Configuración de hardware |

## Guía de Mapeo: Contenido → Módulo

Para deducir el módulo correcto, buscar estas palabras clave en transcripciones:

### sales-management
- Palabras clave: venta, orden de venta, factura cliente, cotización, pedido, cliente, vendedor, comisión, bonificación, entrega cliente
- Menú: "Gestión de Ventas"

### purchase-management
- Palabras clave: compra, orden de compra, proveedor, recepción, factura proveedor, requisición
- Menú: "Gestión de Compras"

### material-management
- Palabras clave: inventario, almacén, movimiento, ajuste, transferencia, producto, stock
- Menú: "Gestión de Materiales"

### accounting-management
- Palabras clave: contabilidad, asiento, cuenta contable, diario, mayor, balance, plan de cuentas
- Menú: "Gestión Contable"

### financial-management
- Palabras clave: banco, pago, cobro, conciliación, caja, transferencia bancaria, cheque
- Menú: "Gestión Financiera"

### balance-management
- Palabras clave: saldo, cuenta por cobrar, cuenta por pagar, antigüedad, cobranza, morosidad
- Menú: "Gestión de Saldos"

### human-management
- Palabras clave: empleado, nómina, vacaciones, asistencia, contrato laboral
- Menú: "Gestión Humana"

### production-management
- Palabras clave: producción, orden de producción, BOM, lista de materiales, manufactura
- Menú: "Gestión de Producción"

### pdv-management
- Palabras clave: punto de venta, PDV, POS, caja, turno, arqueo
- Menú: "Gestión de PDV"

### electronic-billing
- Palabras clave: factura electrónica, CFE, DGI, comprobante fiscal, XML
- Menú: "Facturación Electrónica"

### master-data
- Palabras clave: socio de negocio, producto, lista de precios, categoría, configuración maestra
- Menú: "Datos Maestros"

## Guía de Mapeo: Contenido → Tipo

Para deducir el tipo de funcionalidad:

### ventana
- Indicadores: "ventana", "pestaña", "campo", "registro", "formulario"
- En capturas: formulario con campos, pestañas visibles

### proceso
- Indicadores: "proceso", "ejecutar", "generar", "parámetros", "corrida"
- En capturas: diálogo con parámetros, botón ejecutar

### reporte
- Indicadores: "reporte", "informe", "listado", "imprimir", "exportar"
- En capturas: visor de reportes, PDF, opciones de formato

### smart_browser
- Indicadores: "navegador", "browser", "búsqueda", "filtros", "selección múltiple"
- En capturas: grilla con checkboxes, filtros superiores

### configuracion
- Indicadores: "configuración", "parámetros del sistema", "setup"
- En capturas: pantalla de configuración

## Estructura de Carpetas Típica

```
docs/
├── [modulo]/
│   ├── index.md                    # Índice del módulo
│   ├── [subcarpeta]/               # Agrupación lógica
│   │   ├── index.md                # Índice de subcarpeta
│   │   ├── ventana.md              # Documentación de ventana
│   │   ├── ventana/                # Recursos de ventana
│   │   │   └── *.png
│   │   ├── proceso.md              # Documentación de proceso
│   │   └── proceso/
│   │       └── *.png
│   └── configuracion.md            # Docs sin subcarpeta
```

## Subcarpetas Comunes por Módulo

### sales-management
- `sales-orders/` - Órdenes de venta
- `documents-receivable/` - Facturas cliente
- `deliveries/` - Entregas

### purchase-management
- `purchase-orders/` - Órdenes de compra
- `documents-payable/` - Facturas proveedor
- `receipts/` - Recepciones

### material-management
- `inventory/` - Inventario
- `movements/` - Movimientos
- `physical-inventory/` - Inventario físico

### accounting-management
- `accounting-rules/` - Reglas contables
- `journal-entries/` - Asientos
- `reports/` - Reportes

### financial-management
- `banks/` - Bancos
- `payments/` - Pagos
- `collections/` - Cobros

## Tipos de Documentos

### Ventana
Documenta una ventana de ADempiere con sus pestañas y campos.

### Proceso
Documenta un proceso ejecutable desde menú o ventana.

### Reporte
Documenta un reporte con sus parámetros y salida.

### Smart Browser
Documenta un navegador inteligente con filtros y acciones.

### Integración
Documenta conexión con sistemas externos.

### Configuración
Documenta parámetros de configuración del sistema.

## Convenciones de Nombres

- Archivos: `kebab-case.md`
- Carpetas: `kebab-case/`
- Imágenes: `descripcion-corta.png`
- Sin espacios, sin caracteres especiales
- Todo en minúsculas
