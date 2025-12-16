---
title: Carga de Contratos Masiva (Educación)
category: Documentation
star: 9
sticky: 9
tag:
  - Educación
article: false
---

## Carga Masiva de Alumno-Contrato (Educación)

Esta funcionalidad permite crear registros de nuevos alumnos realizando la carga de sus entidades relacionadas en una misma importación.

Desde una planilla con datos concatenados se importan las siguientes entidades: Alumno (y su localización), familiares (padre, madre, hasta tres parientes), la entidad familia (con sus miembros) y el Contrato de Servicio vinculado al alumno.

### 1. Formato de Importación de Datos

Este circuito se inicia creando el formato de importación de datos correspondiente a Contratos.

![Formato de importación](/assets/img/docs/basic-rules/bid-format.png)

Dentro de este formato se configuran los campos correspondientes para asegurar la correcta carga de los datos al generar la importación.

![Campos de Fomato](/assets/img/docs/basic-rules/bid-fields.png)

Estos datos estarán separados por secciones: Socio del Negocio Estudiante (y su localización), Socio de Negocio responsable de pago (padre, madre, etc.), entidad Familia, entidad Contrato y Contactos (hasta tres contactos, siendo el contacto número uno el responsable de pago por defecto).

### 2. Cargador de Archivo

Una vez seteado el formato de importación con los campos necesarios para realizar la carga masiva, desde la ventana Cargador de Archivo se realizará la subida de la planilla generada (con los datos concatenados en forma cronológica y de acuerdo al formato de importación creado.

Se debe seleccionar formato de importación: Importar Contratos. Luego elegir set de caracteres UTF-8 o UTF-16.

Desde el botón de acción "Seleccionar Archivo a Cargar" se habilitará una ventana emergente con la opción de "choose file" para seleccionar el archivo (planilla) a cargar y luego la opción de "Cargar Archivo (upload)". 

![Ventana emergente](/assets/img/docs/basic-rules/bid-upload2.png)

Esto permitirá en el visor de esa ventana validar los datos de la planilla cargada, y utilizando las flechas del extremo superior derecho se podrá verificar que cada dato se encuentre en el campo que corresponda (de acuerdo al formato definido).

![Cargador de Archivo](/assets/img/docs/basic-rules/bid-upload.png)

Al dar Ok, se procesará el archivo y quedará pendiente de importar (cargado en el sistema).

### 3. Importar Contrato

Esta ventana nos permite visualizar el archivo previamente cargado (desde Cargador de Archivos). Para agilizar la consulta del registro, desde búsqueda avanzada es posible ubicarlo con el filtro Importado = NO.

Permite realizar una segunda validación de los datos respecto al campo donde están ubicados.

Luego desde el botón de procesos al hacer click en "Importación de Contrato" se generan en sistema todas las entidades de acuerdo a los datos extraidos del archivo cargado e importado.

![Importar Contrato](/assets/img/docs/basic-rules/bid-import1.png)

### 4. Consejos útiles

Es válido mencionar que si se importan los datos de un estudiante que ya existe en la base de datos, el registro no se procesará (no se importará) y se informará de esta situación en el campo "Mensaje Error Importación".

![Mensajes de Error](/assets/img/docs/basic-rules/bid-import-error-message.png)

A su vez, en el caso de importar una familia que ya exista en la base de datos, los registros de estudiante, responsable de pago y contrato se sumarán a esa familia previamente creada.

Esta función se habilitó a los fines de permitir sumar estudiantes (hermanos) o nuevos contactos a una familia previamente creada.

### 5. Ejemplo de Carga de Archivo Alumno-Contrato

![Ejemplo Carga de Archivo](/assets/img/docs/basic-rules/bid-import-upload.mp4)