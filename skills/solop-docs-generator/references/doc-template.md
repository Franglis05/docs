# Template de Documentación Solop ERP

## Frontmatter

```yaml
---
title: [Título del Documento]
category: Documentation
star: 9
sticky: 9
article: false
---
```

## Estructura Completa

```markdown
# [Título Principal]

## Descripción

La ventana/proceso/reporte **[Nombre]** permite [descripción de la funcionalidad principal]. 
[Explicación adicional del propósito y beneficios].

## ¿Cuándo se utiliza?

Se utiliza cuando [descripción del caso de uso principal].

Casos típicos:
- [Caso 1]
- [Caso 2]
- [Caso 3]

## Acceso

[Módulo Principal] → [Submenú] → [Nombre de la Opción]

## Campos principales

### Pestaña [Nombre de Pestaña]

- **[Nombre del Campo]**  
  [Descripción del campo y su propósito].

- **[Nombre del Campo]**  
  [Descripción del campo y su propósito].

### Pestaña [Otra Pestaña] (si aplica)

- **[Nombre del Campo]**  
  [Descripción del campo y su propósito].

## Acciones disponibles

- **[Nombre de Acción]**  
  [Descripción de qué hace esta acción].

- **[Nombre de Acción]**  
  [Descripción de qué hace esta acción].

## Flujo del proceso

### 1. [Nombre del paso]

[Descripción detallada del paso].

![Descripción de imagen](./nombre-archivo/paso1.png)

### 2. [Nombre del paso]

[Descripción detallada del paso].

### 3. [Nombre del paso]

[Descripción detallada del paso].

## Consideraciones importantes

- [Punto importante 1]
- [Punto importante 2]
- [Punto importante 3]

## Ejemplo de uso

[Descripción de un escenario típico de uso, desde el inicio hasta el resultado esperado].
```

## Guía de Estilo

### Títulos
- H1 (#): Solo el título principal del documento
- H2 (##): Secciones principales
- H3 (###): Subsecciones (pestañas, pasos)

### Campos
Usar formato:
```markdown
- **Nombre del Campo**  
  Descripción del campo.
```

Nota: Dos espacios al final de la línea del nombre para forzar salto de línea.

### Imágenes
- **IMPORTANTE**: Ubicar en `docs/public/assets/img/docs/[modulo]/`
- Usar nombres descriptivos en inglés con kebab-case
- Alt text descriptivo en español
- **Usar ruta absoluta `/assets/img/docs/[modulo]/imagen.png`**

```markdown
# ❌ NO HACER (rutas relativas):
![Vista principal de la ventana](./nombre-feature/vista-principal.png)

# ✅ CORRECTO (ruta absoluta):
![Vista principal de la ventana](/assets/img/docs/modulo/01-vista-principal.png)
```

**Ejemplo real:**
```markdown
# Documento: docs/electronic-billing/electronic-billing-versioning.md
# Imagen: docs/public/assets/img/docs/electronic-billing/01-screenshot.png

![Verificación del Soporte](/assets/img/docs/electronic-billing/01-screenshot.png)
```

### Links Internos
Usar rutas relativas:
```markdown
[Ver documento relacionado](./otro-documento)
[Ver en otro módulo](../otro-modulo/documento)
```

### Listas
- Para campos y acciones: lista con guiones y negrita
- Para consideraciones: lista simple con guiones
- Para pasos numerados: usar ### con número

### Tablas con montos
- Las columnas que contienen valores monetarios o numéricos **siempre van alineadas a la derecha**
- Usar `---:` en el separador de la columna para alinear a la derecha

```markdown
# ✅ CORRECTO:
| Categoría | Ventas Netas ($) |
|-----------|-----------------:|
| Producto A | 1,234,567.89 |

# ❌ INCORRECTO:
| Categoría | Ventas Netas ($) |
|-----------|-----------------|
| Producto A | 1,234,567.89 |
```

### Tono
- Formal pero accesible
- Tercera persona o impersonal
- Verbos en presente indicativo
- Evitar jerga técnica innecesaria
