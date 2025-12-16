---
title: Socio del Negocio para Educación
category: Documentation
star: 9
sticky: 9
tag: 
  - Educación
article: false
---

## Estudiantes

### Socio del Negocio

Un Socio del Negocio corresponde a una entidad con la que se hacen negocios. Hay tres tipos diferentes de Socios del Negocio:

* Proveedores
* Clientes
* Empleados

En la vertical de Educación tanto el Estudiante como su Responsable de Pago son considerados Socios del Negocio.

![Socio del Negocio](/assets/img/docs/master-data/mad-education4.png)

Grupo de Socio del Negocio (Campo)

Al Estudiante se recomienda definirlo en el campo Grupo de Socio del Negocio: “Estudiantes” así como en los Familiares definir el Grupo de Socio del Negocio “Familiares”.

**NOTA: En el caso de los familiares Responsables de pago que realicen el pago completo de la Anualidad por adelantado, se les deberá definir el Grupo de Socio del Negocio “Familiar Anualidad”.**

Los **Grupos de Socios del Negocio** usados más frecuentemente son:

* General
* Estudiantes
* Familiar
* Familiar Anualidad
* Proveedores

Ejemplo de relleno de cabezal para un Estudiante:

* Código: No. de Cédula de Identidad
* Grupo de Impuestos: Cédula
* Grupo de Socio del Negocio: Estudiante
* Lista de Precios: Venta pesos para Estudiantes
* Es Cliente: SI

::: note
 Por configurador del sistema es posible indicar si al guardar un Socio del Negocio se debe asignar su número de identificación al código del Socio del Negocio.
:::

### **Pestaña Localización**

Es obligatorio ingresar la localización (domicilio) en un Socio de Negocio. Ingrese dónde está marcado.

## Familia

La Familia se crea como una agrupación donde dentro de la misma se podrán encontrar sus correspondientes miembros junto con el vínculo que los define (Padre, Madre, Hijo, Tutor).

Los Vínculos podrán ser parametrizados según sea necesario.

![Familia](/assets/img/docs/master-data/mad-education5.png)

**Responsable de Pago:**

Es a quien se le emitirá las facturas de servicios.

Dentro de cada uno de los Miembros de la familia también se deberá definir el check de “Responsable de Pago”. Sólo los Miembros que sean Responsable de Pago podrán ser definidos como “Socio de Negocio Facturar a” en el Contrato de Servicios de los alumnos. Por defecto se definirá en una familia el check de Responsable de Pago al miembro que se defina con el vínculo “Padre”. Esto podrá ser modificado.

Para poder ser definido como “Responsable de Pago” éste se deberá definir como Socio del Negocio y también como Usuario. Usuario es el contacto del Socio del Negocio, y un Socio del Negocio puede tener uno o varios contactos usuarios.

El Responsable de Pago y los Alumnos deben ser Socio del Negocio, pues solo ellos tendrán vínculos comerciales con la institución.

El esposo/a del Responsable de Pago no es necesario que sea Socio del Negocio.

Código Familia: Número

Nombre de Familia: 2 Apellidos de la Familia

Descripción Familia: Si se desea

### Miembros (Pestaña)

Los Miembros de la Familia del Tipo de Vínculo Estudiante y el Responsable de Pago deben estar previamente ingresados como Socio del Negocio.

Para crear una nueva Familia se deberá seleccionar:

* Socio del Negocio
* Usuario
* Vínculo: cómo se vincula a la Familia
  * Hijo
  * Padre
  * Madre

Puede ingresar también los Miembros de la Familia desde el Contrato de Servicios, posicionándose en Alumno, haciendo click derecho y seleccionando Registro nuevo.

![Miembros](/assets/img/docs/master-data/mad-education6.png)

 ### **Definir la cantidad de Hermanos en la Familia:**

Al momento de guardar un Socio del Negocio como Miembro de la Familia el sistema verificará que el mismo sea de Tipo de Relación = “Hijo” y que tenga un Contrato de Servicio creado en el sistema.

En ese momento se actualizará automáticamente en la Ventana Familia el Campo “Hermanos”.

### **Orden de Creación de Contratos Recomendado:**

* Nombre Familia
* Contrato
  * Producto, Actividad
* Desde Contrato se define:
  * Socio del Negocio
    * Nombre
    * Cédula de Identidad
    * Contacto
  * Familia
* Miembros de Familia

## **Documentos compartidos entre Organizaciones**

Cuando un Documento deba ser compartido entre diferentes Organizaciones se deberán crear con Organización “ * ”

Los Productos en la Vertical de Educación normalmente son comunes entre todas las Organizaciones, por lo que se deben definir en la organización \* .

Los Estudiantes sin embargo normalmente no son compartidos entre las organizaciones así que los Socios del Negocio de Estudiantes así como sus Contrato de Servicios deberán ser creados siempre con la Organización que corresponda.

Los Proveedores y Empleados que puedan ser Compartidos entre las Organizaciones si podrían ser creados con la Organización “ * ” en caso que se deseen compartir entre todas las Organizaciones.