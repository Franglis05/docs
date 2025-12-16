---
title: Dar de Baja CxC/CxP
category: Documentation
star: 9
sticky: 9
article: false
---

## Dar de Baja CxC/CxP

Esta ventana brinda la posibilidad de marcar facturas (documentos por cobrar y/o pagar) como pagadas y dar de baja sus totales abiertos por medio de la selección de diferentes criterios (filtros).

Criterios existentes en la ventana para establecer el grupo de facturas que se marcarán como pagadas:

* **Organización**: por defecto se mostrará la organización con la cual se ingresó al sistema (y en el caso de contar con varias organizaciones se podrá elegir entre ellas)
* **Moneda**: Es un dato mandatorio (está relacionado con el filtro de ajuste máximo por factura, ya que es un valor a ser ajustado en la moneda de la factura).
* **Socio del Negocio**: Es posible seleccionar un determinado Socio del Negocio (opcional)
* **Grupo de Socio del Negocio**: Es posible filtrar por grupo de socio del Negocio (opcional)
* **Factura**: En el caso de requerir ajustar un determinado documento (en este caso el filtro moneda queda sin funcionalidad)
* **Estado de Cartera**: Es el estado de cobranza de la factura y puede filtrarse por sus criterios (ejemplo: cartera, emitido, entregado, etc.)
* **Nivel de Morosidad**: Es el estado de mora y puede filtrarse por sus diferentes opciones como estado de cuenta, deuda atrasada, etc.
* **Ajuste Máximo por Factura**: Es un valor numérico que establece hasta que importe se ajustarán los diferentes comprobantes que ingresen en la búsqueda (determinada por los demás criterios). Los comprobantes que tengan saldo pendiente por encima de ese valor tope no serán ajustados, y por el contrario, los comprobantes que se encuentren por debajo de ese importe se marcarán como pagadas (es un valor a ser ajustado en la moneda de la factura)
* **CP-CC**: permite filtrar entre ajustar solo Cuentas por Pagar, solo Cuentas por Cobrar o ambos.
* Fecha de Facturación: Es un rango fecha desde/hasta, por defecto estará seteado en el día de la fecha. Permite seleccionar un rango en el cual se ajustarán los comprobantes.
* **Simulado**: es un control tipo check (tildado por defecto) que al encontrarse tildado permite simular el ajuste para determinar los comprobantes que ingresan en la búsqueda de acuerdo a los criterios seleccionados. Esto no genera el ajuste de las facturas. Para ajustar efectivamente los comprobantes debe luego destildarse este control de SIMULADO y volver a ejecutar el proceso.

![Filtros](/assets/img/docs/balance-management/bam-balance-image412.png)

### Resultado

Al finalizar la ejecución del proceso, el sistema muestra un log con aquellos comprobantes ajustados y la cantidad de documentos que se han marcado como pagados.

![Resultado](/assets/img/docs/balance-management/bam-balance-image413.png)

### **Consejos Útiles**

* Es importante para que se **ejecute el proceso correctamente** destildar el check de **Simulado**. ya que esta opción tal como lo indica el nombre solo genera en forma de prueba el proceso. Para que se ejecute la acción de ajustar los saldos pendientes (abiertos) de las facturas se deberá correr nuevamente con el check destildado.

#### Ejecución con check Simulado destildado:

![Filtros](/assets/img/docs/balance-management/bam-assignment-image3.png)

#### Log de Resultado del proceso ejecutado:

![Log de Resultado](/assets/img/docs/balance-management/bam-assignment-image4.png)

