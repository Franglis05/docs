---
title: Cierre de Caja del Punto de Venta
category: Documentation
star: 9
sticky: 9
article: false
---

El cierre de caja del Punto de Venta (PDV) permite consolidar y conciliar los ingresos registrados durante la jornada, asegurando el control de fondos, la detección de diferencias y su correspondiente gestión contable en Solop ERP.

---

## Flujo General

Cada operación en el PDV genera automáticamente registros vinculados al cierre de caja:

1. **Apertura de Caja**
2. **Ventas**
3. **Retiros de Fondos**
4. **Cierre**

Al ejecutar el proceso de cierre, el sistema genera un registro en **Estado Borrador**, que debe ser validado manualmente antes de ser completado.

---

## Proceso de Cierre

### Acceso a cierre de caja

1. Ir a la solapa **Opciones Rápidas del Punto de Ventas**.
2. Ingresar en la sección **Gestión de Caja**.
3. Seleccionar la opción **Cierre**.
4. Visualizar los ingresos y retiros registrados.
5. Confirmar para generar el **cierre del día en estado completo**.

---

## Consulta del Registro

Una vez generado el cierre, los detalles se visualizan en la pestaña:

> `Línea de Cierre de Caja`

### Datos visibles:

- **Apertura**: Registro de inicio de caja.
- **Cobros**: Documentos de cobro asociados.
- **Retiros de Fondos**: Egresos manuales registrados.

---

## Control de Diferencias

En caso de diferencias entre lo registrado y lo contado:

1. Verificar la columna `Diferencia Monto`.
2. Si se acepta la diferencia:
   - Tildar `Sobre/Sub Pago`.
   - Asignar un cargo (ej. `Pérdida por quebranto de caja`).
   - Registrar una descripción y la fecha de conciliación.

---

## Traspaso de Fondos a Banco

Dependiendo del método de cobro, se deberán realizar diferentes pasos antes del cierre:

### Solo pagos con tarjeta

- Ejecutar `Depósito de Caja`
- Luego realizar el `Cierre de Caja`.

### Pagos con transferencia bancaria

- Ejecutar `Transferencia Bancaria`
- Luego realizar el `Cierre de Caja`.

### Pagos mixtos

1. `Depósito de Caja`
2. `Transferencia Bancaria`
3. `Cierre de Caja`

---

## Retiro de Dinero desde PDV

Este paso se realiza *antes* del cierre del día.

1. Ir a `Opciones Rápidas del Punto de Ventas`.
2. Seleccionar **Retiro**.
3. Completar:
   - Monto
   - Moneda
   - Caja destino
   - Cargo asociado: `Retiro de Caja`
4. En caso de lotes de tarjetas, hacer un retiro por cada lote cerrado.

---

## Cierre Final de Caja

Al finalizar el proceso diario:

1. Seleccionar la **Caja a cerrar**.
2. Filtrar movimientos por:
   - `Cuenta Bancaria`
   - `Fecha de Estado de Cuenta`
3. Usar la opción **Crear a partir de Caja** para incluir los movimientos de:
   - Depósitos
   - Transferencias Bancarias
4. Confirmar haciendo clic en **OK**.

---

## Beneficios del Módulo

- ✔️ Control diario de caja y fondos por PDV  
- ✔️ Registro y trazabilidad de cobros, retiros y cierres  
- ✔️ Conciliación automática de diferencias  
- ✔️ Flujo integrado con módulos bancarios  
- ✔️ Información centralizada por punto de venta