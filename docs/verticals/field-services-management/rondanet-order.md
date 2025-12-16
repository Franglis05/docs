---
title: Carga de Órdenes Rondanet (Services)
category: Documentation
star: 9
sticky: 9
article: false
---

## 📦 Cómo cargar órdenes de compra desde Rondanet

Esta guía explica cómo realizar la carga de órdenes de compra exportadas desde Rondanet al sistema, utilizando el módulo de Carga Rondanet.

### 🎯 Objetivo

Importar múltiples órdenes de compra de forma masiva desde un archivo generado en Rondanet, optimizando el proceso de carga y minimizando errores manuales.

### 🛠️ Pasos para realizar la carga

1️⃣ Exportar las órdenes desde Rondanet

* Ingresá a tu cuenta de Rondanet.

* Seleccioná las órdenes que querés exportar (por ejemplo, del 11 de marzo).

* Asegurate de que estén en estado abierto.

* Presioná Exportar ➜ Seleccioná el formato Excel en un solo archivo.

📁 Esto generará un archivo descargable en formato Excel con todas las órdenes seleccionadas.

### 🧹 2. Limpiar y guardar el archivo

a. Abrí el archivo Excel descargado.

b. Eliminá las dos primeras columnas (opcional, pero recomendable para evitar errores en la importación).

* Guardá el archivo en formato:

✅ CSV delimitado por comas, o

✅ CSV delimitado por tabulador.

* Asegurate de que esté en codificación UTF-8.

💡 Este archivo es el que vamos a usar para la carga masiva desde el sistema.

### 📤 3. Importar el archivo en el sistema

a. Ingresá a la ventana Cargador de Archivos.

b. Seleccioná la opción: Importar Órdenes.

Luego, elegí Carga Rondanet.

* Asegurate de seleccionar el formato UTF-8 antes de continuar.

* Cargá el archivo CSV desde tu equipo.

📊 El sistema mostrará una vista previa con todas las columnas y valores importados.

### 🔎 4. Verificar los datos importados

Revisá las columnas importadas:

* Código del producto.

* Cantidad.

* Código del cliente (GLN del punto de entrega).

* Usá las barras de desplazamiento para visualizar el contenido completo del archivo.

✅ Verificá que los datos coincidan con los solicitados por el cliente y que estén correctamente ubicados en cada columna.

### 🚚 5. Generar la importación

* Hacé clic en Siguiente y luego en Generar.

* El sistema te indicará la cantidad de líneas importadas (por ejemplo: 26 líneas).

A continuación, accedé a la ventana Importar Órdenes.

🧾 Esta ventana muestra las líneas cargadas en una tabla intermedia. Todavía no se han generado las órdenes de venta.

### 📌 6. Revisar la tabla intermedia de importación

Verificá las órdenes importadas:

a. Podés visualizar las ya procesadas (aparecen con su número de orden de venta).

b. Las no procesadas figuran como pendientes de importación.

Para mayor claridad:

* Podés filtrar por el campo "Importado".

* O bien, eliminar registros de prueba anteriores para evitar confusión.

🗑️ Por ejemplo, podés borrar líneas antiguas que quedaron de pruebas anteriores.

### 📦 7. Crear las órdenes de venta

Con las líneas validadas, desde esta misma ventana podés iniciar el proceso para crear las órdenes de venta automáticamente.

* Verificá cada número de orden y desplazate hacia la derecha para ver los detalles.

* Confirmá que todas las líneas estén listas y ejecutá el proceso de creación.

✅ Resultado esperado
Las órdenes de compra exportadas desde Rondanet se cargan en el sistema como órdenes de venta completas, evitando el ingreso manual y asegurando la consistencia de los datos.

## 🛠️ Crear Órdenes desde la Ventana "Importar Órdenes"

Este instructivo detalla cómo transformar líneas importadas desde Rondanet en órdenes de venta dentro del sistema.

### 🔎 1. Verificar datos importados

* Accedé a la ventana Importar Órdenes.

* Filtrá por aquellas cuyo campo "Importado" sea distinto de “Sí” para ver lo pendiente.

🧾 Asegurate de tener:

a. La organización y almacén correctos.

b. El GLN correspondiente cargado para cada sucursal en la localización del socio de negocio (🗺️).

### 🏢 2. Validar ubicaciones (GLN)

* Desde la ventana de Socio de Negocio, buscá el cliente (ej: Disco único general).

* Refrescá las localizaciones para ver las sucursales disponibles.

📍 Verificá que cada sucursal tenga su GLN correctamente definido.

Este dato debe coincidir con el que figura en la columna I del archivo importado.

### ⚙️ 3. Ejecutar proceso de creación de órdenes

a. Volvé a la ventana Importar Órdenes.

b. Seleccioná las líneas que deseás importar.

Hacé clic en el botón de proceso (🧩).

Completá:

* Organización

* Acción: Preparar (📝) o Completar (✅)

* Lista de precios (📦). Asegurate de tener una lista general con todos los productos para evitar errores.

### 🧹 4. Manejar errores de productos

Si algún producto muestra error (Invalid Product 🚫), es probable que no esté definido en la lista de precios.

Eliminá esas líneas erróneas:

* Seleccionalas (puede ser de forma masiva).

* Usá la opción Eliminar (🗑️).

* Repetí el proceso de importación con las líneas válidas restantes.

### 📋 5. Confirmar las órdenes generadas

a. Una vez importadas correctamente, limpiá los filtros (🧼).

b. Buscá por la fecha de la orden (por ej. 11 de marzo).

Deberías ver las líneas cargadas con su número de orden de venta generado.

Podés hacer clic en cada número para navegar al detalle (🔍).

### 🧾 6. Verificar desde "Órdenes de Venta"

Abrí la ventana de Órdenes de Venta.

Filtrá por:

* Fecha de la orden

* Tipo de documento (Orden de Venta – POS Order 📦)

Validá los datos:

a. Productos cargados

b. Lista de precios asignada

c. Cantidades

Completá manualmente las órdenes si fueron creadas en estado Preparar (📝).

✅ ¡Listo!
Ahora las órdenes están generadas y listas para coordinar su correspondiente entrega. 🛒📦