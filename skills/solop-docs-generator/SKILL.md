---
name: solop-docs-generator
description: >
  Agente experto en generación de documentación funcional para Solop ERP basado en VitePress.
  Usar cuando se necesite: (1) Crear documentación de nuevas funcionalidades desde un directorio 
  con recursos (videos, imágenes, transcripciones, SQL, código), (2) Analizar y sintetizar 
  información de múltiples fuentes para generar docs, (3) Agregar documentación al proyecto 
  VitePress siguiendo la estructura existente, (4) Validar que el proyecto compile correctamente.
  Triggers: "documentar funcionalidad", "crear documentación", "agregar docs", "documentar entrega",
  "generar manual de usuario", "documentar feature", "crear guía de usuario".
---

# Solop Docs Generator

Agente especializado en generar documentación funcional para Solop ERP.

## Flujo de Interacción

```
USUARIO: "Documenta lo que está en /entregas/bonificaciones/"
   │
   ▼
AGENTE: Escanea el directorio, detecta recursos
   │
   ▼
AGENTE: "¿Cómo se llama este feature?"
   │
   ▼
USUARIO: "Gestión de Bonificaciones"
   │
   ▼
AGENTE: Analiza transcripciones, imágenes, SQL...
        Deduce tipo, menú, campos, flujo...
   │
   ▼
AGENTE: "Detecté que es una ventana de Gestión de Ventas → Comisiones.
         ¿Es correcto ubicarla en sales-management/commissions?"
   │
   ▼
USUARIO: "Sí" / "No, ponla en..."
   │
   ▼
AGENTE: Genera documentación, copia imágenes, actualiza index, valida build
```

## Qué Pregunta el Agente

| Pregunta | Cuándo |
|----------|--------|
| ¿Cómo se llama este feature? | **Siempre** (único dato requerido) |
| ¿Es correcto que sea tipo [ventana/proceso/etc]? | Si no está 100% seguro |
| ¿Ubicarlo en [módulo/subcarpeta]? | Para confirmar antes de crear |
| ¿Esta descripción es correcta? | Opcional, para validar síntesis |

## Qué Deduce Automáticamente

| Elemento | Lo deduce de... |
|----------|-----------------|
| Tipo (ventana/proceso/reporte) | Transcripciones + capturas |
| Menú de acceso | Transcripciones ("vamos a Gestión de Ventas...") |
| Nombre del archivo .md | Nombre del feature → kebab-case |
| Ubicación (módulo/subcarpeta) | Palabras clave + menú detectado |
| Descripción | Síntesis de transcripciones |
| Campos y propósito | Análisis de transcripciones + imágenes |
| Flujo de uso | Pasos en demos/videos |
| Casos de prueba/ejemplos | Ejemplos en transcripciones |
| Formato del documento | Según tipo detectado |

## 1. Estructura del Directorio de Entrega

No se requiere ningún archivo especial. Solo los recursos:

```
/entrega-mi-feature/
├── *.txt, *.vtt           # Transcripciones de Loom
├── *.png, *.jpg           # Capturas de pantalla
├── *.sql                  # Queries (opcional)
├── *.java, *.vue, etc     # Código (opcional)
├── *.pdf, *.docx          # Docs adicionales (opcional)
└── links.txt              # URLs de Loom (opcional)
```

El agente escanea **todo el directorio recursivamente**.

## 2. Proceso de Generación

```
PASO 1: ESCANEAR
├── Ejecutar scripts/scan_resources.py
├── Detectar links de Loom en archivos
└── Listar transcripciones, imágenes, SQL, código

PASO 2: PREGUNTAR NOMBRE
└── "¿Cómo se llama este feature?"

PASO 3: ANALIZAR
├── Procesar transcripciones (scripts/process_transcript.py)
├── Anonimizar datos sensibles (scripts/anonymize_data.py)
├── Analizar imágenes (visión)
├── Revisar SQL para entender cambios
└── Consultar references/project-structure.md para mapeo

PASO 4: DEDUCIR Y CONFIRMAR
├── Tipo de funcionalidad → preguntar si hay duda
├── Menú de acceso → extraído de transcripciones
├── Módulo y subcarpeta → preguntar para confirmar
└── Nombre del archivo .md → kebab-case del nombre

PASO 5: GENERAR
├── Crear documento .md con estructura de references/doc-template.md
├── Incluir: descripción, campos, flujo, ejemplos
├── Copiar imágenes a carpeta correspondiente
├── Actualizar index.md del módulo
└── Validar build con pnpm docs:build
```

## 3. Qué Extraer del Análisis

### De las transcripciones:
- **Tipo**: buscar "ventana", "proceso", "reporte", "navegador"
- **Menú**: buscar "vamos a...", "accedemos desde...", "en el menú..."
- **Campos**: buscar "el campo X es para...", "seleccionamos...", "ingresamos..."
- **Flujo**: buscar "primero...", "luego...", "después...", "finalmente..."
- **Consideraciones**: buscar "importante", "tener en cuenta", "cuidado con..."

### De las imágenes:
- **Tipo de pantalla**: formulario, grilla, reporte, diálogo
- **Campos visibles**: labels en la UI
- **Navegación**: breadcrumbs, menús
- **Estados**: botones disponibles

### Del SQL:
- **Tablas**: AD_Window (ventana), AD_Process (proceso), AD_Browse (browser)
- **Tipo de cambio**: INSERT = nuevo, UPDATE = modificación

## 4. Mapeo de Contenido a Módulo

Ver `references/project-structure.md` para la guía completa de palabras clave.

Resumen rápido:
- "venta", "factura cliente", "pedido" → `sales-management`
- "compra", "proveedor", "recepción" → `purchase-management`
- "inventario", "almacén", "stock" → `material-management`
- "contabilidad", "asiento", "cuenta" → `accounting-management`
- "banco", "pago", "cobro" → `financial-management`
- "producción", "manufactura", "BOM" → `production-management`

## 5. Estructura del Documento Generado

Ver `references/doc-template.md` para el template completo.

```markdown
---
title: [Nombre del Feature]
category: Documentation
star: 9
sticky: 9
article: false
---

# [Nombre del Feature]

## Descripción
[Síntesis extraída del análisis]

## ¿Cuándo se utiliza?
[Casos de uso identificados]

## Acceso
[Menú extraído de transcripciones]

## Campos principales
[Campos identificados con sus descripciones]

## Acciones disponibles
[Botones y acciones detectadas]

## Flujo del proceso
[Pasos extraídos de las demos]

## Consideraciones importantes
[Puntos mencionados como importantes]

## Ejemplo de uso
[Caso de prueba extraído]
```

## 6. Scripts Disponibles

| Script | Propósito |
|--------|-----------|
| `scan_resources.py` | Detectar todos los recursos del directorio |
| `process_transcript.py` | Limpiar y procesar transcripciones |
| `anonymize_data.py` | Reemplazar datos de clientes por datos Solop |
| `validate_entry.py` | Validar que el directorio tenga recursos |
| `generate_doc.py` | Generar estructura base del documento |

## 7. Checklist Final

- [ ] Nombre del feature obtenido del usuario
- [ ] Recursos escaneados del directorio
- [ ] Transcripciones procesadas y anonimizadas
- [ ] Tipo de funcionalidad deducido/confirmado
- [ ] Ubicación confirmada con el usuario
- [ ] Documento .md generado
- [ ] Imágenes copiadas a carpeta correcta
- [ ] index.md actualizado
- [ ] `pnpm docs:build` exitoso

## 2. Estructura VitePress

```
docs/
├── .vitepress/config.mts       # NO MODIFICAR automáticamente
├── public/                     # Assets globales
├── [modulo]/
│   ├── index.md                # Índice con links
│   └── [subcarpeta]/
│       ├── index.md
│       ├── feature.md
│       └── feature/            # Carpeta de imágenes
│           └── *.png
```

## 3. Formato de Documentos

### Frontmatter

```yaml
---
title: Título del Documento
category: Documentation
star: 9
sticky: 9
article: false
---
```

### Estructura Contenido

Ver `references/doc-template.md` para template completo.

Secciones principales:
1. **Descripción** - Qué es y para qué sirve
2. **¿Cuándo se utiliza?** - Casos de uso
3. **Acceso** - Ruta de menú
4. **Campos principales** - Por pestaña/sección
5. **Acciones disponibles** - Botones y acciones
6. **Flujo del proceso** - Si aplica
7. **Consideraciones importantes** - Puntos clave
8. **Ejemplo de uso** - Caso típico

### Imágenes

Carpeta con mismo nombre del .md:
```markdown
![Descripción](./nombre-archivo/imagen.png)
```

## 4. Proceso de Generación

1. **Leer contexto.yaml** - Validar campos requeridos
2. **Recopilar información** - Transcripciones, imágenes, SQL, URLs externas
3. **Anonimizar datos** - Reemplazar datos sensibles de clientes por datos Solop
4. **Sintetizar** - Generar contenido estructurado
5. **Crear archivos** - .md + carpeta de imágenes
6. **Actualizar index.md** - Agregar link al nuevo doc
7. **Validar build** - `pnpm docs:build`

## 5. Anonimización de Datos Sensibles

**IMPORTANTE**: Toda documentación generada de ambientes de clientes debe ser anonimizada.

### Datos que se reemplazan automáticamente

| Tipo | Ejemplo Original | Reemplazo Solop |
|------|------------------|-----------------|
| RIF (Venezuela) | J-40215985-7 | J-12345678-9 |
| RUC (Perú) | 20456789012 | 20123456789 |
| CUIT (Argentina) | 30-71234567-9 | 30-12345678-9 |
| NIT (Colombia) | 900.456.789-1 | 900.123.456-7 |
| RUT (Chile) | 76.543.210-K | 12.345.678-9 |
| Cédula | V-18.456.789 | V-12.345.678 |
| Email | cliente@empresa.com | contacto@solopsoftware.com |
| Teléfono | +58 414-555-1234 | +58 212-555-1234 |
| Dirección | Av. Libertador, Torre XYZ | Av. Principal, Edificio Solop |
| Cuenta Bancaria | 0134-1234-5678-9012 | 0000-1234-5678-9012 |

### Uso del script de anonimización

```bash
# Anonimizar un archivo
python scripts/anonymize_data.py /ruta/transcripcion.txt

# Anonimizar todo un directorio
python scripts/anonymize_data.py /ruta/entrega/ --verbose

# Anonimizar texto directo
python scripts/anonymize_data.py --text "Cliente: Empresa ABC, RIF: J-40215985-7"
```

### Datos de reemplazo (Solop ERP)

```yaml
empresa: "Solop Software C.A."
rif: "J-12345678-9"
direccion: "Av. Principal, Edificio Solop, Piso 5, Oficina 501"
email: "contacto@solopsoftware.com"
telefono: "+58 212-555-1234"

# Personas de ejemplo para documentación
personas:
  - nombre: "Juan Pérez"
    cargo: "Gerente de Ventas"
  - nombre: "María García"
    cargo: "Supervisor de Compras"
  - nombre: "Carlos Rodríguez"
    cargo: "Contador"
```

### Flujo con anonimización

1. El equipo graba video en ambiente de cliente
2. Descarga transcripción de Loom
3. Coloca archivos en directorio de entrega
4. **Claude ejecuta anonimización automáticamente** antes de generar docs
5. La documentación final NO contiene datos reales de clientes

## 5. Reglas

1. NO modificar config.mts automáticamente
2. Usar kebab-case para archivos/carpetas
3. Imágenes en carpeta dedicada
4. Validar build antes de finalizar
5. Frontmatter obligatorio
6. Idioma español
7. Links relativos
8. Actualizar index.md correspondiente

## 6. Scripts Disponibles

- `scripts/scan_resources.py` - **Escanea directorio y detecta recursos automáticamente**
- `scripts/validate_entry.py` - Valida directorio de entrada
- `scripts/process_transcript.py` - Procesa transcripciones .vtt/.txt
- `scripts/anonymize_data.py` - Anonimiza datos sensibles de clientes
- `scripts/generate_doc.py` - Genera estructura base del .md

### Uso de scan_resources.py

```bash
# Ver todos los recursos detectados
python scripts/scan_resources.py /ruta/entrega/

# Salida JSON para procesamiento
python scripts/scan_resources.py /ruta/entrega/ --json
```

Detecta automáticamente:
- Links de Loom en archivos .txt, .md, links.txt
- Transcripciones, imágenes, SQL, código
- Documentos adicionales

## 7. Checklist

- [ ] contexto.yaml validado
- [ ] Fuentes recopiladas
- [ ] **Datos sensibles anonimizados**
- [ ] .md creado con formato correcto
- [ ] Imágenes copiadas
- [ ] index.md actualizado
- [ ] `pnpm docs:build` exitoso
