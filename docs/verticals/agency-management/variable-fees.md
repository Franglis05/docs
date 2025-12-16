---
title: Honorarios Variables
category: Documentation
star: 9
sticky: 9
tag: 
  - Agencia
article: false
---

## Cálculo de Honorarios variables

### ¿Cuándo se calculan los Honorarios?

Al momento de completar la Orden de Venta de Inversión se generarán tantos Cálculos de Comisiones como Tipos de Honorarios se tengan definidos. Según cada Tipo de Honorarios se verificará si los productos definidos en la línea de la Orden de Venta están definidos dentro de los Honorarios del Contrato de Servicio en cuestión. En caso de que se encuentre que un Producto está contemplado en los Honorarios del Contrato, el cálculo de comisiones considerará dicha línea y aplicará el % correspondiente. En el caso de que la Orden de Venta no tenga ningún producto que esté definido en los criterios de un Honorario específico este se creará con importe 0.

Podremos acceder a los cálculos de Comisión realizados mediante el botón de “Documentos Relacionados” desde la Barra de Herramientas.

### ¿Cómo se genera la Orden de Venta de Honorarios?

La Orden de Venta de Honorarios se generará automáticamente desde el Cálculo de Comisiones siempre y cuando éste tenga un importe mayor a 0.

Podremos acceder a la misma desde la ventana Cálculo de Comisiones mediante el ícono de documentos relacionados.

## Definición de Honorarios

### ¿Cómo se define el porcentaje de los Honorarios a utilizar?

El porcentaje de honorarios que será considerado para el cálculo de Honorarios será obtenido según el “Contrato de Servicio”, según la definición que exista en la pestaña Honorarios, aplicando los filtros definidos en estos registros.

Considerar que estas definiciones actúan como si fuese un Diagrama de Venn, definiendo tantos conjuntos como definiciones se realicen. A medida que se vayan definiendo conjuntos más complejos se debe tener la precaución de no dejar conjuntos que en algún momento puedan duplicar ciertos productos ya que un producto puede estar en diferentes conjuntos según como se definan los mismos. En este proceso se debe actuar en concordancia con la definición de los productos para que se logre una correcta definición de ellos y los Conjuntos que se desean definir. 

Según el Contrato de servicio se obtendrán sus correspondientes Honorarios variables, según la definición que exista en la pestaña Honorarios, es decir, según los filtros definidos en estos registros.

![Definición de Honorarios](/assets/img/docs/service-management/sem-agency3.png)

![Definición de Honorarios](/assets/img/docs/service-management/sem-agency13.png)

## Ventana Cálculo de Comisión

### Lógica del Cálculo de Comisión

Según los parámetros definidos en la línea de comisión (“Honorarios” en Contrato de Servicios o “Comisión” del Proveedor en Socio del Negocio), se realizará el control a ver si los Productos definidos en las líneas de la “Orden de Venta Inversión” entran en el conjunto definido en la línea de Comisión correspondiente. 

Si existe un producto que está definido según el criterio aplicado en los parámetros de los Honorarios, entonces el proceso obtendrá el Importe de la línea y lo definirá como “Importe Total” sobre el cuál aplicará el porcentaje correspondiente. 

**Cabezal**
Como dijimos, al momento de completar la Orden de venta se calcularán tantos Cálculos de comisiones como Tipos de honorarios tengan definidos en el sistema. 

En el caso de que la Orden de venta no tenga ningún producto que ingrese en los criterios de un Honorario específico este se creará con importe 0.

**Pestaña Total de Comisión**
En esta pestaña se generará un Registro por cada % de Comisión diferente que encuentre en la Orden. En el campo Porcentaje aparecerá el % a aplicar por la comisión en cuestión. En el campo “Total Convertido” aparecerá el total del importe a comisionar y lo multiplicará por el porcentaje para así definir el “Total de la Comisión” en el campo del mismo nombre.

**Pestaña Detalle de Comisión**
En la pestaña Detalle de Comisión tendremos cada una de las líneas de la Orden de venta que generó el cálculo, aplicando su correspondiente porcentaje a cada una. Aparecerá entonces en esta pestaña tantas líneas como líneas tenga la Orden de venta que haya ingresado en el Conjunto de la comisión definido.

## Actualización de Cálculo de Honorarios

Se deberán seguir los siguientes pasos:

### 1. Pestaña Honorarios

* Desde el Contrato de servicio, pestaña Honorarios modificaremos el campo “Multiplicador” al Honorario en cuestión que queramos modificar, indicando aquí el nuevo valor. Guardamos el registro.

### 2. Orden de Venta

* Luego desde la Orden de venta a la que se aplicaron los honorarios correremos el proceso “Actualizar Cálculo de Comisión de Orden”

### 3. Resultado

De esta manera los Cálculos de comisiones generados antes de aplicar este proceso serán Cerrados al igual que su Orden de venta Honorarios.

Se generarán los nuevos Cálculos de comisiones aplicando los nuevos porcentajes definidos y una nueva Orden de venta honorarios en estado Completo.

![Actualizar Cáculo Comisión de orden](/assets/img/docs/service-management/sem-agency6.png)