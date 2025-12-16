---
title: Esquema Contable
category: Documentation
star: 9
sticky: 9
article: false
---

Un Esquema Contable es una combinación de un estándar contable nacional (ej. GAAP Internacional), un método de costeo (ej. estándar) y una moneda. 
Solop ERP le permite definir múltiples esquemas contables de tal manera que usted puede mantener en paralelo libros para reportes financieros y datos para tomar decisiones.
También elimina las tareas laboriosas de conversión, transformación y consolidación de subsidiarias extranjeras y permite la fácil separación de reportes legales y administrativos.

Usted no necesita preocuparse acerca de qué elementos introducir con cada transacción ya que Solop ERP genera todas las transacciones contables por usted automáticamente, derivando los valores de los elementos de la transacción o documento

La ventana Esquema Contable le permite definir el Método Contable y los Elementos que definirán la estructura contable. Mientras que las Cuentas y las Organizaciones son requeridas, otros elementos tales como Socios del Negocio, Producto, Proyecto y Campaña pueden incluirse para proporcionar un seguimiento y reporte más detallado. 

De entrada al Nombre y a la Descripción para este  Esquema Contable  y seleccione el cuadro de verificación Activo. Seleccione un GAAP (Principio de Contabilidad  Generalmente Aceptado), un Método de Costeo y una Moneda. 
Seleccione un Tipo de Compromiso, elija Ninguno, Compromiso y Reservación o Sólo Compromiso. Generalmente seleccionará Ninguno a menos que realice Encumbrance Accounting. Si seleccionó la aplicación de ciertos documentos (Ej. Ordenes  de Compra) generará transacciones a los Tipos de Aplicación Compromiso y/o Reservaciones. 
Seleccione el cuadro de verificación Acumulado si emplea la contabilidad basada en Acumulado. De no seleccionar este  cuadro indicará que la contabilidad está basada en Efectivo. Cuando selecciona Contabilidad Basada en Efectivo. Entradas y Gastos no son Contabilizados hasta que el Pago ha sido realizado. Al seleccionar el cuadro de verificación Acumulado, las Entradas y Gastos son contabilizados al momento de ser Facturados.
Para más información acerca de Transacciones generadas mediante un Documento, refiérase por favor al capítulo apropiado en el cuál se discuten los Documentos en Detalle.
Seleccione Método de Costeo de PEPS, UEPS. Facturación Promedio, Último Precio OC, Última Factura o Costeo Estándar

Seleccione Nivel de Costeo: Compañía, Organización o Lote.
Seleccione Moneda para este Esquema Contable.
Seleccione el cuadro de verificación Control de Período Automático si desea que los períodos contables sean abiertos automáticamente. Cuando se seleccione se desplegarán campos adicionales. Días de Historia define el número de días anteriores a la fecha actual en que usted puede hacer aplicaciones contables y Días a Futuro define el número de días posteriores de la fecha actual en que usted puede hacer aplicaciones contables. La fecha actual está basada en la fecha del sistema. Si por ejemplo la fecha del sistema es 10 de mayo y los Días de Historia es puesta a 20 y Días a Futuro se pone a 30, la aplicación puede ocurrir para transacciones fechadas entre el 20 de abril y el 9 de junio. Si se deja sin seleccionar, cada período debe ser abierto manualmente para los tipos de documento apropiados.

Separador de Elementos deseado para ser mostrado cuando se despliegue una combinación de cuenta.


Uso de Alias en Cuentas si quiere definir alias para sus combinaciones de cuenta. Los alias proporcionan un método fácil de búsqueda y selección de combinaciones de cuenta.
Aplicar Descuento Comercial si quiere que los descuentos comerciales sean aplicados a una cuenta explícita. Si no se selecciona, los descuentos comerciales serán deducidos del ingreso del producto.
Corregir Impuesto para Descuento/Cargos para indicar que el impuesto debe basarse en importe descontado en oposición al importe original.
Aplicación de Servicios por Separado si desea emplear una cuenta separada al aplicar Documentos que contengan Servicios o Tipos Recurso de Producto.

### Contabilidad General

Cada Esquema Contable define varios parámetros para procesar la Contabilidad, estos incluyen el tipo de manejo de error y el método de balanceo de moneda a ser usados. Adicionalmente, están definidas las cuentas usadas para Resultados acumulados, Inter-Compañía y Balanceo.

Clic en la pestaña Contabilidad General para introducir las Combinaciones de Cuenta que se usarán para registrar algunas entradas específicas a la contabilidad. 
Seleccione el cuadro de verificación Activo.
Seleccione el cuadro de verificación Usar Balance Suspendido si desea forzar la aplicación contable de importes fuera-de-balance en una póliza. El importe fuera-de-balance se registrará a la cuenta Puente de Balanceo introducida. Note que la Cuenta Puente de Balanceo aparece solamente si se selecciona el cuadro de verificación.
Seleccione el cuadro de verificación Usar Error en Suspenso si desea forzar la aplicación contable de importes con error en una póliza.  El importe en error se registrará a la cuenta Puente de Error  introducida. Note que la Cuenta Puente de Error  aparece solamente si se selecciona el cuadro de verificación.
Seleccione el cuadro de verificación Usar Balanceo de Moneda si desea forzar la aplicación contable de importes fuera-de-balance por moneda en un asiento. Una condición de fuera-de-balance por moneda puede ocurrir debido a redondeos al convertir moneda. El importe fuera de balance  se registrará a la cuenta Balanceo de Moneda introducida. Note que la  cuenta Balanceo de Moneda  aparece solamente si se selecciona el cuadro de verificación.
Clic en el icono de Cuenta para dar entrada o cambiar la cuenta de Utilidades Retenidas, cuenta Ingresos Acumulados, cuenta Intercompañía Débito A, cuenta  Inter-compañía Débito Desde y cuenta Compensación VPC (Variación Precio de Compra).
Los campos Utilidades Retenidas e Ingresos Acumulados son empleados al aplicar sus entradas de fin de año.
Las  cuentas Inter-compañía Débito A e Inter-compañía Débito Desde son empleados al aplicar transacciones entre Organizaciones. Estas cuentas deben ser definidas aun si usted no tiene planeado este tipo de transacciones.

La cuenta Compensación VPC es empleada para guardar la Variación de los Precios de Compra.

La cuenta Compensación de Compromiso es empleada para guardar Compromisos o Transacciones de Reservado. Estas podrían ser generadas si un Tipo de Compromiso o  de Compromiso o Reservación han sido seleccionados en la pestaña anterior. 

### Esquema Contable Múltiple

Puede haber ocasiones en que usted necesita más de un Esquema Contable para una compañía. Esto puede ser porque usted requiere transacciones contables a ser aplicadas en más de una unidad monetaria, o puede estar empleando una cartera diferente de cuentas o diferentes GAAP. 

En este ejemplo asumimos que nuestro Esquema Contable Principal está en Dólares Americanos y no seguimos el proyecto. Como sea, para nuestra subsidiaria en el Reino Unido debemos reportar en Libras  y necesitamos diferentes cuentas.

Para definir Esquemas Contables Adicionales primeramente debemos determinar si necesita definir nuevos Elementos (si está usted empleando Diferentes Cartera de Cuentas o  diferentes códigos de proyecto). Si determina que esto es necesario primeramente debe definir un Árbol.

### Cuentas Predeterminadas

El Esquema Contable también define las cuentas predeterminadas a ser usadas para las transacciones generadas por el sistema (por ej. Contabilizar las facturas de CxC). 
Para asegurar que todas las cuentas requeridas estén disponibles, las cuentas predeterminadas se definen en el nivel del Esquema Contable. Éstas son las cuentas que se importan como parte de la Configuración Inicial de la Compañía.

::: note
El objetivo es generar todas las entradas de asientos contables que correspondan a las transacciones realizadas por la empresa.
:::

Estas cuentas se usan como valores predeterminados para Socios del Negocio, Productos, almacenes, Proyectos, Bancos, Impuestos y Libros de Efectivo. Todos estos se pueden sobrescribir individualmente pero teniendo los valores predeterminados se asegura que cada transacción sea adecuadamente contabilizada.
El objetivo es generar todas las entradas de transacciones contables. Consecuentemente, todas las cuentas necesarias estas predefinidas. Por ejemplo, si usted vende un producto, la Cuenta de Ingresos definida para este Producto es usada. Esto le permite definir la cuenta en un momento simple y entonces usted no tiene que preocuparse por las consecuencias contables cuando introduce los documentos.

Si ha actualizado las cuentas predeterminadas para un Esquema Contable existente, esto debió ser realizado con precaución. Si ha borrado cuentas específicas de las cuentas predeterminadas (por ejemplo un Producto Específico o Socio del Negocio), estas se volverán a escribir mediante este Proceso y usted deberá aplicar las actualizaciones anteriores.
Clic en el botón OK para definir los parámetros del Proceso.
Seleccione el Esquema Contable que desea emplear como Fuente para este proceso.
Seleccione el cuadro de verificación Sobrescribir Copia si desea copiar los valores nuevos predeterminados a los registros existentes.