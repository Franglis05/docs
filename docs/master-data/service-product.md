---
title: Producto de Servicio
category: Documentation
star: 9
sticky: 9
article: false
---

En Solop ERP, un producto de servicio es un tipo de producto que no implica gestión de stock, porque no es un bien tangible, sino una prestación o actividad que se factura al cliente o se contrata a un proveedor.

Todos los productos que se utilizarán deberán estar definidos en la ventana “Producto”. Los Productos pueden ser Servicios o Artículos.

**Al crear los Productos se debe definir los siguientes puntos:**

* **Categoría de Producto (Obligatorio):** Según la Categoría del Producto es que se definirá la Cuenta Contable a utilizar en los Documentos donde sea utilizado. También se podrá definir diversos descuentos de precio de venta según Categorías de Producto.
* **Grupo de Producto (Opcional):** Según el Grupo de Producto se podrá agrupar diferentes Productos según su Actividad o Centro de Costo. (En Cada Grupo de Producto también se definirá el Centro de Costo que corresponderá el Producto en cuestión).
* **Grupo de Impuesto:** Definir si el Producto tiene Tasa Exenta, Mínima o Básica.
* **Comprado:** Si el producto es comprado definir “Si”.
* **Vendido:** Si el producto es comprado definir “Si”.

![Productos de Servicios](/assets/img/docs/master-data/mad-serviceproduct1.png)

### Pestaña Precio

En esta pestaña se definirá la Versión de lista de precios que el producto tenga definida en la ventana Lista de Precios.

![Precio](/assets/img/docs/master-data/mad-serviceproduct2.png)

### Ventana Lista de Precios

Existen Listas de Precios de Venta y de Compra y a cada Socio del Negocio se le debe definir una.

A los Estudiantes, como son considerados Clientes se le debe definir en el cabezal del Socio de Negocio la Lista de Precios “Venta Pesos”.

### Versiones de Listas de Precios

A su vez existen versiones de una Lista de Precios, por ejemplo:

* Lista de Precios Venta Pesos
  * Versión de Lista de Precios Venta Pesos: Lista Venta 2020