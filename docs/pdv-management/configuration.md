---
title: Configuración del Punto de Venta
category: Documentation
star: 9
sticky: 9
article: false
---

Este módulo permite configurar las terminales del Punto de Venta (PDV) en Solop ERP, estableciendo reglas de operación, control de caja, dispositivos asociados y condiciones comerciales. Asegura un comportamiento correcto del sistema durante las ventas, cobranzas y devoluciones.

---

## Terminal PDV

### Acceso

Desde el menú de Solop ERP:  
**Gestión de Ventas > Órdenes de Venta > Punto de Venta > Terminal PDV**

La ventana **Terminal PDV** permite configurar cajas, taquillas o autoservicios donde se gestionarán órdenes, facturación y cobro.

### Campos Principales

- **Organización**: Define a qué entidad pertenece el terminal.
- **Nombre / Descripción**: Identificación del PDV.
- **Agente Comercial**: Vendedor asignado.
- **Retraso de Cierre Automático**: Tiempo de inactividad antes del cierre de sesión.
- **Lista de Precios**: Lista utilizada para las ventas.
- **Modificación de Precio**: Permite cambios de precio con autorización.
- **Caja Menor**: Caja asociada para pagos en efectivo.
- **Plantilla de Socio del Negocio**: Cliente genérico para registrar ventas rápidas.
- **Cuenta Bancaria**: Cuenta vinculada a las operaciones de cobro.
- **Transferencia a Banco**: Cuenta destino para transferencias.

### Documentos y Reglas

- **Tipo de Documento**: Para ventas, devoluciones, cobros, etc.
- **Reglas de Facturación / Entrega**: Definen cómo se generan y gestionan los documentos.

### Parámetros de Dispositivos

- **Impresora Fiscal**
- **Registradora / Balanzas**
- **PIN POS Requerido**
- **Teclado en Pantalla**: Habilita entrada por pantalla táctil.

### Checks y Configuraciones Adicionales

- **POS Compartido**
- **Permitir Crear Cliente Nuevo**
- **Límites de Reembolso y Descuento**
- **Vendedores Asignados**

---

## Pestañas de Configuración Específica

- **Almacenes**: Definen desde dónde se realiza la entrega.
- **Formas de Pago**: Métodos disponibles y reglas de cambio.
- **Listas de Precios / Tipos de Documento**
- **Esquemas de Descuento**
- **Vendedores Asignados**: Usuarios habilitados para operar en ese PDV.

Para más información sobre precios:  
[Lista de Precios](../sales-management/comercial-rules/price-list)

---

## Operaciones en el PDV

### Documentos por Defecto

Tipos predefinidos para apertura, retiro de caja, cobros y devoluciones.

### Productos Favoritos

Desde la pestaña **Llave PDV**, se pueden asignar productos destacados, imágenes y categorías.

### Cajas del Punto de Venta

Definición de caja asociada a la terminal, socio del negocio y cargo contable predeterminado.

---

## Definir SDN con RUT o Cédula

### Objetivo

Permitir la creación rápida de socios de negocio (clientes) en el PDV usando plantillas según si es empresa (RUT) o persona física (Cédula).

### Pasos

1. Acceder a la ventana de **Terminal PDV**.
2. Ir a la pestaña **Business Partner Template**.
3. Dejar activos solo dos templates:  
   - RUT Template  
   - Cédula Template
4. Verificar en cada plantilla:
   - Grupo de Impuestos correcto.
   - Activo en todos los clientes.
   - Tipo de impuesto correspondiente.

Una vez guardado, el sistema podrá crear automáticamente socios desde el PDV.

---

## Cambio en Otra Moneda

### Configuración en Terminal PDV

- Si se define una moneda específica: **No** se puede cambiar la moneda al cobrar ni al entregar cambio.
- Si no se define: el sistema **permite seleccionar otra moneda**.

Para que un método de pago pueda usarse como cambio:  
* Marcar **Is Allowed To Refund**

Podés usar un método existente (ej. efectivo) o crear uno específico llamado “Cambio”.

### Funcionamiento

Si un producto **no tiene precio** en la lista principal, el sistema busca en una **lista de referencia**, aunque esté en otra moneda.

> Convierte automáticamente el precio usando la **tasa de cambio del día**.

Esto permite vender productos con precios en distintas monedas sin duplicar listas.

### Observaciones Clave

- La **lista principal** es la configurada en el terminal.
- Si no hay precio allí, consulta la lista secundaria.
- El precio se convierte automáticamente.

---

## Beneficios

- ✔️ Configuración completa por terminal.
- ✔️ Flexibilidad en el uso de múltiples monedas.
- ✔️ Automatización para creación de clientes.
- ✔️ Integración con dispositivos físicos.
- ✔️ Control por permisos, reglas y límites.
