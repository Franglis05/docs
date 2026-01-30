#!/usr/bin/env python3
"""
Valida que un directorio tenga recursos suficientes para documentar.
No requiere ningún archivo especial, solo verifica que haya contenido útil.

Uso:
    python validate_entry.py /ruta/al/directorio/entrega
"""

import sys
from pathlib import Path

def validate_entry_directory(entry_path: str) -> dict:
    """
    Valida el directorio de entrada y retorna un resumen.
    """
    result = {
        "valid": True,
        "errors": [],
        "warnings": [],
        "resources": {
            "transcripciones": [],
            "imagenes": [],
            "sql": [],
            "codigo": [],
            "documentos": [],
            "links_files": []
        }
    }
    
    path = Path(entry_path)
    
    if not path.exists():
        result["valid"] = False
        result["errors"].append(f"El directorio no existe: {entry_path}")
        return result
    
    if not path.is_dir():
        result["valid"] = False
        result["errors"].append(f"La ruta no es un directorio: {entry_path}")
        return result
    
    # Extensiones por categoría
    EXT_TRANS = {'.txt', '.vtt', '.srt'}
    EXT_IMG = {'.png', '.jpg', '.jpeg', '.gif', '.webp'}
    EXT_SQL = {'.sql'}
    EXT_CODE = {'.java', '.js', '.ts', '.vue', '.py', '.xml', '.json'}
    EXT_DOCS = {'.pdf', '.doc', '.docx', '.md'}
    
    for file_path in path.rglob('*'):
        if file_path.is_dir() or file_path.name.startswith('.'):
            continue
            
        suffix = file_path.suffix.lower()
        rel_path = str(file_path.relative_to(path))
        
        if suffix in EXT_TRANS:
            result["resources"]["transcripciones"].append(rel_path)
        elif suffix in EXT_IMG:
            result["resources"]["imagenes"].append(rel_path)
        elif suffix in EXT_SQL:
            result["resources"]["sql"].append(rel_path)
        elif suffix in EXT_CODE:
            result["resources"]["codigo"].append(rel_path)
        elif suffix in EXT_DOCS:
            result["resources"]["documentos"].append(rel_path)
        
        # Detectar archivos que podrían tener links
        if 'link' in file_path.name.lower() or suffix in {'.txt', '.md', '.url'}:
            result["resources"]["links_files"].append(rel_path)
    
    # Validar que haya algo útil
    total = (len(result["resources"]["transcripciones"]) + 
             len(result["resources"]["imagenes"]) +
             len(result["resources"]["documentos"]))
    
    if total == 0:
        result["valid"] = False
        result["errors"].append("No se encontraron recursos útiles (transcripciones, imágenes o documentos)")
    
    if not result["resources"]["transcripciones"]:
        result["warnings"].append("No hay transcripciones - el análisis será limitado")
    
    if not result["resources"]["imagenes"]:
        result["warnings"].append("No hay imágenes - la documentación no tendrá capturas")
    
    return result


def print_report(result: dict):
    print("\n" + "="*60)
    print("VALIDACIÓN DEL DIRECTORIO DE ENTREGA")
    print("="*60)
    
    status = "✅ VÁLIDO" if result["valid"] else "❌ INVÁLIDO"
    print(f"\nEstado: {status}\n")
    
    if result["errors"]:
        print("ERRORES:")
        for err in result["errors"]:
            print(f"  ❌ {err}")
        print()
    
    if result["warnings"]:
        print("ADVERTENCIAS:")
        for warn in result["warnings"]:
            print(f"  ⚠️  {warn}")
        print()
    
    print("RECURSOS ENCONTRADOS:")
    res = result["resources"]
    print(f"  📝 Transcripciones: {len(res['transcripciones'])}")
    print(f"  🖼️  Imágenes: {len(res['imagenes'])}")
    print(f"  🗄️  SQL: {len(res['sql'])}")
    print(f"  💻 Código: {len(res['codigo'])}")
    print(f"  📄 Documentos: {len(res['documentos'])}")
    print("="*60)


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Uso: python validate_entry.py /ruta/directorio")
        sys.exit(1)
    
    result = validate_entry_directory(sys.argv[1])
    print_report(result)
    sys.exit(0 if result["valid"] else 1)
