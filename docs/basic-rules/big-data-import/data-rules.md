---
title: Reglas de Datos en Carga Socio del Negocio
category: Documentation
star: 9
sticky: 9
article: false
---

Esta guía detalla cómo deben enviarse los datos para realizar una carga masiva de Socios del Negocio (Clientes, Proveedores, Empleados) en el sistema. 
 
Todos los campos marcados como obligatorios deben completarse correctamente. En caso contrario, los datos faltantes deberán ser cargados manualmente luego de la importación. 

## Fases

La importación de datos al sistema tiene un mismo circuito para cualquier registro que esté importando (Socio del Negocio, Producto, Inventario, Documentos por Pagar, etc.) que deben cumplirse cronológicamente para lograr una efectiva carga de datos.

### Cargador de Archivo

Siempre partimos de un **formato de importación de datos**, en esa ventana generamos el formato para la tabla correspondiente al tipo de datos que deseamos cargar (Socio del Negocio en este caso). Una vez creado el formato con las columnas de datos a validar, se crea una planilla con los datos a importar respetando el orden de columna/dato del formato generado.

Por último, desde **Cargador de Archivo** seleccionando el formato que corresponda podremos cargar la planilla. Esto guarda los datos en una tabla intermedia.

### Importación de Datos

Desde la ventana **Importar Socio del Negocio** (o el importador que se corresponda con el dato a importar) es posible realizar una búsqueda de los registros cargados y aun no importados seleccionando **Importado** = NO. 
Ejecutando el botón **Importar Socios del Negocio** se cargarán a tabla definitiva todos los registros cargados que se encuentren sin importar.

### Campos a completar en la planilla 

|        Campo          |                         Descripción                                        | Obligatorio | 
| --------------------- | -------------------------------------------------------------------------- | ----------- |
|    Organización       | Será definido por el equipo de Solop. No requiere acción del usuario.      |    SI       |
|   Value (Código)      | Código único del SDN. Asignado por el cliente o dejar por valor default    |    SI       |
|   Nombre Fantasía     | Nombre comercial o visible del SDN. Ej.: 'Distribuidora Sur'               |    SI       |
|    Razón Social       | Nombre legal. Coincide o no con dato anterior. Ej.: 'Empresa del Sur S.A.' |    SI       |
|  Cliente/Empl/Prov    | Indicar 'Y' (Sí) o 'N' (No) por columna. Un SDN puede tener múltiple rol   |    SI       |
|  Dirección 1/Dir 2    | Dirección física del SDN. Usar Dir 2 si se requiere espacio adicional      |    SI       |
|       Ciudad          | Escribir mayúscula inicial y el resto en minúscula. Ej.: 'Montevideo'      |    SI       |
|        País           | Código ISO de 2 letras. Ejemplo: Uruguay = 'UY', Argentina = 'AR'          |    SI       |
|      Teléfono         | Número de contacto. Si no se conoce, puede dejarse vacío.                  |  Opcional   |
| Núm de Identificación | Número de RUT o Cédula. Según tipo de entidad (jurídica o natural) y país  |    SI       |
|       Región          | Aplica en país con regiones. Ej.: Buenos Aires/Jalisco                     |    SI       |
|     Grupo SDN         | Categoría del SDN. Ej.: “Clientes”, “Proveedores”, “Empleados”             |    SI       |
|     Contacto          | Nombre de contacto. Si se define, se crea un “Usuario” vinculado.          |  Opcional   |
|    Regla de Pago      | Valor constante para todos o por registro. Ej.: 'Contado', '30 días'.      |    SI       |
|  Grupo de Impuesto    | Identifica si el SDN se rige por RUT o Cédula. Completar según país.       |    SI       |

### Recomendaciones clave 

**Formato exacto:** Algunos campos (como Ciudad o Región) deben coincidir exactamente con lo que ya existe en el sistema. Revisá ortografía, tildes y uso de mayúsculas **(Primera letra Mayúscula y el resto Minúscula)** 

* Ejemplos no aceptados: Bsas, BA, BSAS, b.Aires.  

* Caso aceptado: Buenos Aires 

**Carga incompleta:** Si se omiten campos obligatorios, la información deberá cargarse manualmente después. 

**Grupos SDN:** Si necesitás crear nuevos grupos (por ejemplo, “Distribuidores”), deben ser dados de alta previamente por el equipo técnico. 

::: tip
 En caso de que existan datos que no cumplan con la lógica definida por el sistema, la   planilla será devuelta al cliente para su corrección. 
 Si se desea continuar con la carga pese a estos errores, la corrección de los mismos implicará costos adicionales que no están contemplados en el alcance inicial de la carga masiva. 
:::