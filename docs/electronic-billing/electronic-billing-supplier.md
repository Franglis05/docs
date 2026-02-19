---
title: Invoicy - Plataforma Facturación Electrónica
category: Documentation
star: 9
sticky: 9
article: false
---

La plataforma InvoiCy permite visualizar, validar y gestionar los comprobantes fiscales electrónicos (CFE) generados desde Solop ERP. También centraliza el seguimiento de envíos, la reimpresión, las notificaciones y la administración de CAEs. Esta guía describe los procesos clave de validación, control de estados, gestión de reportes y anulación de comprobantes vencidos.

---

## Requisitos Previos

- Haber emitido un CFE desde Solop ERP (e-Ticket, e-Factura, etc.).
- Tener acceso a InvoiCy con credenciales proporcionadas por Solop.
- Haber cargado correctamente el CAE vigente en InvoiCy.

---

## 1. Validación de CFE

Luego de completar un documento en Solop ERP, se puede consultar su estado en:

*URL:* [https://solopuy.migrate.info/InvoiCy](https://solopuy.migrate.info/InvoiCy)

### Funcionalidades disponibles:

- Visualización de todos los CFE emitidos hasta la fecha.
- Revisión de detalles de cada documento en pestañas organizadas.
- Icono de impresora para generar versiones en A4 o rollo 80mm.
- Acciones al pie de página para interactuar con cada CFE.

---

## 2. Estado del CFE

Cada documento muestra un campo de *Estado*.

- Si un CFE fue *rechazado*, se puede editar haciendo clic en el ícono de lápiz para reenviarlo.
- Recomendación: contactar al soporte antes de realizar modificaciones.

::: tip 
Cuando el cliente también usa InvoiCy, el sistema envía copias del documento a su email registrado y a la DGI.
:::

---

## 3. Envío CFE a Clientes

Existen dos métodos para definir el envío por email, que dependen como esté definida la *Dirección*:

### 3.1 Definida en DGI
- En este caso, el envío lo realiza directamente InvoiCy.
- No depende de Solop ERP.

### 3.2 Definida por el proveedor
- Permite enviar una copia adicional al área de pagos del cliente.
- Se configura en Solop ERP: pestaña **Localización** del **Socio del Negocio** en el campo `EMail Address`.

> Se pueden incluir múltiples correos, separados por coma, sin espacios.

### Validación del envío:
- Ingresar en InvoiCy, consultar el comprobante emitido.
- En la pestaña **Receptor**, verificar el campo **E-mail receptor**.

::: tip 
Para deshabilitar el envío automático desde Solop ERP, solicitar al soporte que configure la opción interna "Deshabilitar Envío de mail a BP" en la ventana *Luy Sender*.
:::

---

## 4. Consulta de Documentos

Desde la pantalla **Inicio** en InvoiCy se pueden aplicar filtros por:

- Tipo de CFE  
- Número (inicial y final)  
- Período de tiempo  
- Estado  
- Serie  

> Al hacer clic en una fila, se abre el documento completo organizado por pestañas.

---

## 5. Reportes de CFE

La plataforma de Invoicy permite generar reportes considerados necesarios (u obligatorios) por la entidad fiscal del país correspondiente. 
Se tratan de listados con información que completan el control y fiscalización por parte de cada organismo gubernamental.

### Generar Reporte Diario

1. Ir a la sección **Reportes** > botón **Reporte Diario**.
2. Filtrar por estado, fechas, tipo de CFE, etc.
3. Clic en **Generar Reporte Diario**.
4. Especificar la fecha deseada.
5. Clic en **Generar**.

### Acciones disponibles:

- Editar  
- Actualizar  
- Eliminar  
- Enviar a DGI  
- Descargar  

::: tip
Si el reporte diario fue rechazado, primero validar los CFE emitidos antes de editar o reenviar el reporte. Contactar a soporte si es necesario.
:::

---

## 6. CFE Recibidos

La pantalla de **CFE Recibidos** muestra todos los comprobantes emitidos al RUT de la empresa.

### Filtros disponibles:

- Tipo CFE  
- Serie  
- Número  
- Fecha (emisión, firma o importación)  
- RUT del emisor  
- Estado del sobre y respuesta  
- Número secuencial único  

* Hacer clic en un registro para ver los detalles y realizar acciones como:

- Descargar XML  
- Imprimir copia  
- Reenviar email de acuse o aceptación  

---

## 7. Gestión de Empresas/Sucursales

En la parte superior del sistema se muestra una lista desplegable con las empresas/sucursales disponibles.

- La empresa activa aparece primero.  
- Se puede buscar por nombre.  
- Clic en "Mostrar todos los registros" para ampliar la vista.

---

## 8. Notificaciones

InvoiCy muestra notificaciones relacionadas a eventos del sistema:

- El ícono se encuentra en el encabezado.
- Una marca indica que hay nuevas notificaciones.
- Al pasar el mouse, se despliegan agrupadas por tipo.
- Clic en una notificación abre la pantalla correspondiente.

### Acciones disponibles:

- Marcar como leída  
- Ir a la pantalla para corregir el problema  
- Ver todas las notificaciones con estado, categoría y fecha

---

## 9. Aviso Límite de CAE

El aviso por límite de CAE se configura desde:

**Panel de Control > Datos de la Sucursal**  
**Panel de Control > Configuración de Notificaciones**

Se puede definir el **modo de notificación** (email o ícono dentro de InvoiCy).

---

## 10. Carga de CAE

La Constancia de Autorización de Emisión (CAE). Es un archivo digital que la Dirección General Impositiva (DGI) emite para autorizar a las empresas a emitir Comprobantes Fiscales Electrónicos (CFE), como facturas electrónicas, entre un rango de numeración específico. La CAE es necesaria para validar la emisión de estos comprobantes electrónicamente. 

Posee una validez en dos dimensiones:

* Cuenta con una fecha de vigencia. Al alcanzar esa fecha de vencimiento debe solicitarse y cargarse nuevo CAE para el tipo de documento que corresponda.

* Tiene un número predeterminado de CFE (numeración). Al alcanzar el límite de numeración de CFE también debe solicitarse y cargarse nuevo CAE para el tipo de documento que corresponda.

### 1. Descargar CAE de DGI

- Ingresar a **Servicios en Línea DGI** > "eFactura - CAE - Consulta Autorizaciones Emitidas".
- Descargar el XML del CAE autorizado.

### 2. Importar CAE

1. Ir a **Panel de Control > CAE > Importar CAE**.
2. Hacer clic en **Elegir archivo** y seleccionar el XML descargado.
3. Seleccionar una de las opciones de asignación:
   - Asignar a una única sucursal
   - Asignar a múltiples sucursales con rangos

4. Confirmar selección y método de emisión (ej.: web service).
5. El sistema mostrará el rango y cantidad de CFE disponibles.

---

## 11. Vencimiento de CAE

Cuando un CAE vence, deben anularse los números no utilizados:

### Procedimiento:

1. Ingresar a **Configuraciones > Anular rango de CFE**.
2. Buscar el último número emitido del CAE vencido.
3. Determinar el rango no utilizado.
4. Completar:
   - Tipo de CFE
   - Modo: Anulación por rango
   - Seleccionar CAE vencido
   - Número inicial y final

> InvoiCy permite anular hasta 5000 comprobantes por vez. Si el rango es mayor, dividir en tramos.

### Resultado:

El lote de CFE será anulado correctamente y no podrá ser utilizado.

