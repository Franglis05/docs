---
title: Elemento Contable
category: Documentation
star: 9
sticky: 9
article: false
---

El elemento contable le permite definir de forma sistemática una estructura de cuentas y los parámetros que serán utilizados en el Tipo de Aplicación contable.

Esta estructura actúa como el plan de cuentas contable, presentando una lista de cuentas contables en las cuales serán registrados los hechos contables generados desde los procesos administrativos de Solop ERP. Estos elementos generalmente son ordenados bajo una codificación que facilitan el reconocimiento de cada cuenta.

El método consiste en asignar un número decimal que nos permita asociar la clasificación de las cuentas:

Cuentas Reales: Son denominadas así las cuentas que mantienen saldo durante y posterior a un periodo contable y que son conservadas en el balances. Generalmente estas cuentas son útiles para Generar Informe Financiero, dentro de estas cuentas se encuentran:

Activos: Se refiere a los bienes de los que una empresa dispone y tiene derechos, sean tangibles o intangibles.

Pasivos: Se refiere a los compromisos u obligaciones que la empresa contrae con una entidad.

Patrimonio: Se refiere a los aportes realizados por accionistas de la empresa.

Cuentas Nominales: Son denominadas así las cuentas que son cerradas al finalizar el período contable, transfiriendo el saldo a las cuentas reales, y posteriormente iniciarán con saldo cero, con el objetivo de iniciar el balance con estas cuentas limpias, dentro de estas cuentas se encuentran:

Ingresos: Se refiere a la ganancia o dinero que ingresa a la empresa.

Costos: Se refiere al dinero que egresa de la empresa con la finalidad de generar un activo.

Gastos: Se refiere al dinero que egresa de la empresa que no genera activos.

Estas cuentas han sido estandarizadas a nivel mundial de la siguiente forma:

| Activos | Pasivos | Patrimonio | Ingresos | Costos | Gastos |
| ------- | ------- | ---------- | -------- | ------ | ------ |
| 1       | 2       | 3          | 4        | 5      | 6      |

En Solop ERP los códigos de las cuentas son conformados con números con la siguiente estructura:

![Campo](/assets/img/docs/accounting-management/acm-accounting-image464.png)

Imagen 1. Estructura de Cuentas Contables

Para este ejemplo podríamos establecer la siguiente figura:

| Activos | Corrientes | Disponibles | Banco | Cuenta Bancaria |
| ------- | ---------- | ----------- | ----- | --------------- |
| 1       | 1          | 1           | 0001  | 0001            |

El elemento contable es necesario para la definición del esquema contable, que a su vez define el óptimo funcionamiento de Solop ERP, esto es porque cada transacción administrativa generará un asiento contable y por ende son requeridas las cuentas contables.

En esta oportunidad Solop ERP ha diseñado para usted un material en el cual se define detalladamente esta ventana que frecuentemente será visitada por usted, que ha decidido incursionar en el uso de Solop ERP.

- Registro de Elemento Contable

## Registro de Elemento Contable

Ubique y seleccione en el menú de Solop ERP, la carpeta **Análisis de Desempeño**, luego seleccione la carpeta **Reglas Contables**, por último seleccione la ventana **Elemento Contable**.

![Campo](/assets/img/docs/accounting-management/acm-accounting-image646.png)

Imagen 1. Menú de Solop ERP

Podrá visualizar la ventana **Elemento Contable**, con los diferentes registros de elementos contables que posee la misma.

![Campo](/assets/img/docs/accounting-management/acm-accounting-image647.png)

Imagen 2. Ventana Elemento Contable

Seleccione la pestaña **Valor de Elemento**, para crear un nuevo registro de valor en el elemento contable.

![Campo](/assets/img/docs/accounting-management/acm-accounting-image648.png)

Imagen 3. Pestaña Valor de Elemento

Luego de ubicarse en el registro del valor del elemento, seleccione el icono **Registro Nuevo**, para crear un nuevo registro de valor del elemento.

Seleccione en el campo **Organización**, la organización para la cual esta realizando el registro.

![Campo](/assets/img/docs/accounting-management/acm-accounting-image649.png)

Imagen 5. Campo Organización de la Pestaña Valor de Elemento de la Ventana Elemento Contable

Introduzca en el campo **Código**, el código correspondiente al registro que esta realizando.

Introduzca en el campo **Cuenta Padre**, la cuenta padre correspondiente al registro que esta realizando.

Introduzca en el campo **Nombre**, el nombre correspondiente al registro que esta realizando.

Introduzca en el campo **Descripción**, la descripción correspondiente al registro que esta realizando.

Introduzca en el campo **Tipo de Cuenta**, el tipo de cuenta correspondiente al registro que esta realizando.

Introduzca en el campo **Naturaleza de Cuenta**, la naturaleza de la cuenta correspondiente al registro que esta realizando.

Seleccione el checklist **Cuenta Controlada**, para indicar que la cuenta en la cual será utilizado este registro, es una cuenta controlada.

Seleccione el checklist **Cuenta de Banco**, para indicar que la cuenta en la cual será utilizado este registro, es una cuenta de banco.

Al tildar el checklist **Cuenta de Banco**, es habilitado el campo **Cuenta Bancaria**.

Seleccione el checklist **Cuenta en Moneda Extranjera**, para indicar que la cuenta en la cual será utilizado este registro, es una cuenta en moneda extranjera.

Al tildar el checklist **Cuenta en Moneda Extranjera**, es habilitado el campo **Moneda**.

Seleccione el checklist **Entidad Acumulada**, para indicar que la cuenta en la cual será utilizado este registro, es una cuenta sumaria.

::: note
La selección de este checklist, oculta la visibilidad de los demas checklist que se encuentran en la pestaña **Valor de Elemento**.
:::

Seleccione el checklist **Aplicar Actuales**, para indicar que la cuenta en la cual será utilizado este registro, los valores acutales pueden ser contabilizados.

Seleccione el checklist **Aplicar Presupuesto**, para indicar que la cuenta en la cual será utilizado este registro, los valores del presupuesto pueden ser aplicados.

Seleccione el checklist **Aplicar Estadísticas**, para indicar que serán registradas las cantidades estadísticas en la cuenta en la cual sea utilizado este registro.

Seleccione el icono **Guardar Cambios**, ubicado en la barra de herramientas de Solop ERP, para guardar el registro de los campos de la pestaña **Valor de Elemento**.