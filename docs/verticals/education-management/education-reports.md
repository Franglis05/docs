---
title: Reportes Educación
category: Documentation
star: 9
sticky: 9
tag: 
  - Educación
article: false
---

## Reporte Miembros de Familia

Es un reporte que proporciona información detallada sobre los miembros de una familia asociados con un estudiante o varios estudiantes dentro de la institución educativa. Este tipo de reporte suele incluir datos como el nombre de los miembros de la familia, su relación con el estudiante (por ejemplo, padre, madre, tutor), información de contacto (como números telefónicos, direcciones de correo electrónico), y otra información relevante para la comunicación y gestión administrativa.

![Estados de cuenta educación](/assets/img/docs/master-data/mad-educationreports1.png)

#### Finalidad del reporte

El reporte "Miembros de Familia" es útil en un ERP educativo por varias razones:

* Comunicación efectiva: Permite a la institución educativa mantener una comunicación efectiva con los miembros de la familia relacionados con los estudiantes.

* Gestión de Contactos: Facilita la gestión de contactos al proporcionar una lista organizada y actualizada de los miembros de la familia asociados con cada estudiante. Esto es útil para el personal administrativo, que necesita comunicarse con las familias de manera regular.

* Registro de Información: Ayuda a mantener un registro completo y actualizado de la información de contacto de los miembros de la familia, lo cual es esencial para la gestión eficiente de la institución educativa.

* Personalización de la Experiencia Educativa: Permite personalizar la experiencia educativa al tener información sobre la estructura familiar de cada estudiante.

#### Vistas del Reporte:

* Miembros de Familia por Organización y Familia
* Miembros de Familia

#### Detalle de Columnas que integran el reporte

|         Columna        |              Descripción                   |                            Ayuda                                 |  
| ---------------------- | ------------------------------------------ | ---------------------------------------------------------------- |
|        Familia         |            Nombre de la Familia            |                Nombre que identifica a una familia               |
|   Socio del Negocio    |      Identifica un Socio del Negocio       | Persona con quien realiza transacciones. Cliente, proveedor, etc |
|        Grupo SDN       |    ID del Grupo de Socio del Negocio       |      Identifica con código único a un grupo de Socio del Negocio |
|       Contrato         |           Contrato de Servicios            |  Contrato de Servicios entre la Institucion educativa y alumno   |
|      Descuentos        |    	    Descuento en porcentaje           |     indica el descuento aplicado o tomado como un porcentaje     |
|    Tipo de Relación    |     Tipo de relación con el alumno         |     Indica el vínculo del familiar respecto al alumno            |
|     Es Responsable     |             Responsable de Pago            |     Identifica al familiar del alumno Responsable de Pago        |
|          Email         |        ID de Correo Electrónico            |      Indica la ID de correo electrónico para este usuario        |
|       Teléfono         |       Identifica un número telefónico      |         Identifica el número telefónico para este usuario        |
|           CI           |    Número de Identificación Tributaria     |      Número de Identificación gubernamental de esta entidad      |
|    Email Res. de Pago  | Correo Electrónico de Responsable de pago  |         ID de Correo electrónico del Responsable de Pago         |
|  CI Responsable Pago   | Número de Identificación Tributaria de RP  |  Número de Identificación gubernamental del responsable de pago  |
|          Nivel         | Nivel que se encuentra cursando el alumno  |            Identifica la actividad que cursa el alumno           |
|        Dirección       |        Domicilio real del registro         |           Identifica la dirección del familiar o alumno          |
|         Ciudad         |            Identifica una Ciudad           |        Identifica una ciudad única para este Paí­s o Región       |
|      Departamento      |           Nombre de esta región            | Nombre que se imprimirá cuando esta región se use en un documento|

## Estados de Cuenta Educación

Es un informe financiero específico para instituciones educativas, que detalla el estado de las cuentas de los estudiantes. Este reporte incluye información sobre matrículas, cuotas, pagos realizados, saldos pendientes, y cualquier otro cargo o crédito relacionado con la educación del estudiante. 

![Estados de cuenta educación](/assets/img/docs/master-data/mad-educationreports1.png)

#### Finalidad del reporte

* Transparencia Financiera: Proporciona una visión clara y detallada de las transacciones financieras entre la institución y los estudiantes, ayudando a mantener la transparencia en el manejo de los fondos.

* Gestión de Pagos: Facilita el seguimiento de los pagos realizados por los estudiantes, identificando rápidamente cualquier saldo pendiente y asegurando que las cuentas estén al día.

* Comunicación con Estudiantes y Familias: Ayuda a comunicar de manera efectiva a los estudiantes y sus familias sobre el estado de sus cuentas, proporcionando un registro claro de todas las transacciones y saldos actuales.

* Planificación Financiera: Asiste a los administradores de la institución educativa en la planificación y gestión de los ingresos y gastos, permitiendo una mejor previsión y control financiero.

* Cumplimiento y Auditoría: Asegura el cumplimiento con las normativas financieras y contables, proporcionando una documentación detallada que es esencial para auditorías internas y externas.

* Resolución de Disputas: Facilita la resolución de cualquier disputa relacionada con los pagos, al proporcionar un registro detallado y preciso de todas las transacciones.

* Informes Personalizados: Permite generar informes personalizados según las necesidades de la institución, como por ejemplo, resúmenes mensuales, estados de cuenta individuales, y reportes específicos para ciertos periodos académicos.

#### Vistas

* Estados de Cuenta Educación

#### Detalle de Columnas que integran el reporte

|         Columna        |              Descripción                   |                            Ayuda                                 |  
| ---------------------- | ------------------------------------------ | ---------------------------------------------------------------- |
|       F. Orden         |           Fecha de la orden                |             Indica la fecha en que se ordenó un artículo         |
|     Orden de Venta     |                Orden de Venta              |      La ID de la orden de ventas es un identificador único       |
|   Socio del Negocio    |      Identifica un Socio del Negocio       | Persona con quien realiza transacciones. Cliente, proveedor, etc |
|       Producto         |       Producto, Servicio, Artículo         |        Identifica un artículo que se compra o vende              |
|        Precio          |         Precio basado en la UM             | El precio ingresado convierte a precio real por conversión de UM |
|    Cantidad Ordenada   |             Cantidad Ordenada              |        Indica la cantidad de un producto que fue ordenada        |
|   Cantidad a Facturar  |             Cantidad Facturada             |     Indica la cantidad de un producto que ha sido facturado      |