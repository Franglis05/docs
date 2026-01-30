#!/usr/bin/env python3
"""
Genera la estructura base del documento markdown a partir de contexto.yaml.
Este script crea el esqueleto que luego Claude completa con información.

Uso:
    python generate_doc.py /ruta/entrega/contexto.yaml [--output /ruta/salida.md]
"""

import sys
import argparse
from pathlib import Path
from datetime import datetime

try:
    import yaml
    HAS_YAML = True
except ImportError:
    HAS_YAML = False


def load_context(yaml_path: Path) -> dict:
    """Carga y valida el archivo contexto.yaml"""
    if not HAS_YAML:
        raise ImportError("PyYAML es requerido. Instalar con: pip install pyyaml")
    
    with open(yaml_path, 'r', encoding='utf-8') as f:
        return yaml.safe_load(f)


def generate_frontmatter(ctx: dict) -> str:
    """Genera el frontmatter YAML del documento."""
    nombre = ctx.get('feature', {}).get('nombre', 'Sin título')
    
    return f"""---
title: {nombre}
category: Documentation
star: 9
sticky: 9
article: false
---"""


def generate_skeleton(ctx: dict) -> str:
    """Genera el esqueleto del documento basado en el tipo."""
    feature = ctx.get('feature', {})
    ubicacion = ctx.get('ubicacion', {})
    contexto = ctx.get('contexto', {})
    
    nombre = feature.get('nombre', 'Sin título')
    tipo = feature.get('tipo', 'ventana')
    descripcion = contexto.get('descripcion_corta', '[Descripción pendiente]')
    menu_acceso = contexto.get('menu_acceso', '[Ruta de acceso pendiente]')
    usuario = contexto.get('usuario_destino', 'Usuario')
    
    # Frontmatter
    doc = generate_frontmatter(ctx)
    doc += f"\n\n# {nombre}\n\n"
    
    # Descripción
    doc += "## Descripción\n\n"
    doc += f"{descripcion}\n\n"
    
    # Cuándo se utiliza
    doc += "## ¿Cuándo se utiliza?\n\n"
    doc += f"[Describir casos de uso para {usuario}]\n\n"
    
    # Acceso
    doc += "## Acceso\n\n"
    doc += f"{menu_acceso}\n\n"
    
    # Secciones específicas por tipo
    if tipo == 'ventana':
        doc += generate_window_sections()
    elif tipo == 'proceso':
        doc += generate_process_sections()
    elif tipo == 'reporte':
        doc += generate_report_sections()
    elif tipo == 'smart_browser':
        doc += generate_browser_sections()
    elif tipo == 'integracion':
        doc += generate_integration_sections()
    elif tipo == 'configuracion':
        doc += generate_config_sections()
    else:
        doc += generate_generic_sections()
    
    # Secciones comunes al final
    doc += "## Consideraciones importantes\n\n"
    doc += "- [Punto importante 1]\n"
    doc += "- [Punto importante 2]\n\n"
    
    doc += "## Ejemplo de uso\n\n"
    doc += "[Describir un caso de uso típico paso a paso]\n"
    
    return doc


def generate_window_sections() -> str:
    """Secciones específicas para documentar una ventana."""
    return """## Campos principales

### Pestaña Principal

- **[Campo 1]**  
  [Descripción del campo].

- **[Campo 2]**  
  [Descripción del campo].

### Pestaña Secundaria (si aplica)

- **[Campo]**  
  [Descripción del campo].

## Acciones disponibles

- **Registro Nuevo**  
  Permite crear un nuevo registro.

- **Guardar Cambios**  
  Guarda la información ingresada.

- **Completar**  
  Finaliza el registro y habilita su procesamiento.

"""


def generate_process_sections() -> str:
    """Secciones específicas para documentar un proceso."""
    return """## Parámetros

- **[Parámetro 1]**  
  [Descripción y valores posibles].

- **[Parámetro 2]**  
  [Descripción y valores posibles].

## Flujo del proceso

### 1. Configuración inicial

[Descripción del paso].

### 2. Ejecución

[Descripción del paso].

### 3. Resultado

[Descripción de qué genera el proceso].

"""


def generate_report_sections() -> str:
    """Secciones específicas para documentar un reporte."""
    return """## Parámetros del reporte

- **[Parámetro 1]**  
  [Descripción].

- **[Parámetro 2]**  
  [Descripción].

## Contenido del reporte

El reporte muestra la siguiente información:

- [Columna/dato 1]
- [Columna/dato 2]
- [Columna/dato 3]

## Formatos de salida

- PDF
- Excel
- HTML

"""


def generate_browser_sections() -> str:
    """Secciones específicas para Smart Browser."""
    return """## Filtros de búsqueda

- **[Filtro 1]**  
  [Descripción].

- **[Filtro 2]**  
  [Descripción].

## Columnas mostradas

- [Columna 1]: [Descripción]
- [Columna 2]: [Descripción]

## Acciones disponibles

- **[Acción 1]**  
  [Descripción de qué hace].

- **[Acción 2]**  
  [Descripción de qué hace].

"""


def generate_integration_sections() -> str:
    """Secciones específicas para integraciones."""
    return """## Configuración

### Parámetros de conexión

- **[Parámetro 1]**  
  [Descripción].

- **[Parámetro 2]**  
  [Descripción].

## Flujo de datos

### Datos enviados

[Descripción de qué información se envía].

### Datos recibidos

[Descripción de qué información se recibe].

## Manejo de errores

[Descripción de cómo se manejan los errores].

"""


def generate_config_sections() -> str:
    """Secciones específicas para configuración."""
    return """## Parámetros de configuración

### Sección 1

- **[Parámetro]**  
  [Descripción y valores posibles].

### Sección 2

- **[Parámetro]**  
  [Descripción y valores posibles].

## Impacto en el sistema

[Describir cómo afecta esta configuración al comportamiento del sistema].

"""


def generate_generic_sections() -> str:
    """Secciones genéricas."""
    return """## Campos principales

- **[Campo 1]**  
  [Descripción].

- **[Campo 2]**  
  [Descripción].

## Acciones disponibles

- **[Acción 1]**  
  [Descripción].

"""


def main():
    parser = argparse.ArgumentParser(
        description='Genera estructura base de documento desde contexto.yaml'
    )
    parser.add_argument('yaml_path', help='Ruta al archivo contexto.yaml')
    parser.add_argument('--output', '-o', help='Ruta de salida para el .md')
    
    args = parser.parse_args()
    
    yaml_path = Path(args.yaml_path)
    
    if not yaml_path.exists():
        print(f"Error: {yaml_path} no existe")
        sys.exit(1)
    
    try:
        ctx = load_context(yaml_path)
    except Exception as e:
        print(f"Error al cargar {yaml_path}: {e}")
        sys.exit(1)
    
    doc = generate_skeleton(ctx)
    
    if args.output:
        output_path = Path(args.output)
        output_path.write_text(doc, encoding='utf-8')
        print(f"✅ Documento generado: {output_path}")
    else:
        print(doc)


if __name__ == "__main__":
    main()
