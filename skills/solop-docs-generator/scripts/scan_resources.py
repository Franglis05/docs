#!/usr/bin/env python3
"""
Escanea un directorio de entrega y detecta automáticamente:
- Links de Loom (en archivos .txt, .md, .url)
- Transcripciones
- Imágenes/capturas
- Archivos SQL
- Código fuente
- Otros documentos

Uso:
    python scan_resources.py /ruta/directorio/entrega
"""

import sys
import re
from pathlib import Path
from typing import Dict, List
import json

# Patrones para detectar URLs
PATTERN_LOOM = re.compile(r'https?://(?:www\.)?loom\.com/share/[a-zA-Z0-9]+')
PATTERN_YOUTUBE = re.compile(r'https?://(?:www\.)?(?:youtube\.com/watch\?v=|youtu\.be/)[a-zA-Z0-9_-]+')
PATTERN_URL = re.compile(r'https?://[^\s<>"\']+')


def scan_for_links(file_path: Path) -> Dict[str, List[str]]:
    """Escanea un archivo buscando links de video y otros URLs."""
    links = {
        "loom": [],
        "youtube": [],
        "otros": []
    }
    
    try:
        content = file_path.read_text(encoding='utf-8', errors='ignore')
        
        # Buscar links de Loom
        loom_matches = PATTERN_LOOM.findall(content)
        links["loom"].extend(loom_matches)
        
        # Buscar links de YouTube
        youtube_matches = PATTERN_YOUTUBE.findall(content)
        links["youtube"].extend(youtube_matches)
        
        # Buscar otros URLs (excluyendo los ya encontrados)
        all_urls = PATTERN_URL.findall(content)
        for url in all_urls:
            if url not in links["loom"] and url not in links["youtube"]:
                # Filtrar URLs comunes que no son relevantes
                if not any(skip in url for skip in ['github.com', 'localhost', '127.0.0.1', 'example.com']):
                    links["otros"].append(url)
    except Exception:
        pass
    
    return links


def scan_directory(dir_path: Path) -> Dict:
    """
    Escanea un directorio completo y retorna todos los recursos encontrados.
    """
    result = {
        "directorio": str(dir_path),
        "contexto_yaml": None,
        "links": {
            "loom": [],
            "youtube": [],
            "otros": []
        },
        "transcripciones": [],
        "imagenes": [],
        "sql": [],
        "codigo": [],
        "documentos": [],
        "otros_archivos": []
    }
    
    # Extensiones por categoría
    EXT_TRANSCRIPCIONES = {'.txt', '.vtt', '.srt'}
    EXT_IMAGENES = {'.png', '.jpg', '.jpeg', '.gif', '.webp', '.bmp'}
    EXT_SQL = {'.sql'}
    EXT_CODIGO = {'.java', '.js', '.ts', '.vue', '.py', '.xml', '.json', '.jsx', '.tsx'}
    EXT_DOCUMENTOS = {'.pdf', '.doc', '.docx', '.xls', '.xlsx', '.ppt', '.pptx', '.md'}
    EXT_LINKS = {'.url', '.webloc', '.desktop'}
    
    # Archivos donde buscar links
    EXT_BUSCAR_LINKS = {'.txt', '.md', '.html', '.url', '.webloc'}
    
    for file_path in dir_path.rglob('*'):
        if file_path.is_dir():
            continue
            
        # Ignorar archivos ocultos y de sistema
        if file_path.name.startswith('.'):
            continue
            
        suffix = file_path.suffix.lower()
        rel_path = str(file_path.relative_to(dir_path))
        
        # Detectar contexto.yaml
        if file_path.name in ['contexto.yaml', 'contexto.yml']:
            result["contexto_yaml"] = rel_path
            continue
        
        # Buscar links en archivos de texto
        if suffix in EXT_BUSCAR_LINKS or file_path.name == 'links.txt':
            links = scan_for_links(file_path)
            result["links"]["loom"].extend(links["loom"])
            result["links"]["youtube"].extend(links["youtube"])
            result["links"]["otros"].extend(links["otros"])
        
        # Categorizar archivo
        if suffix in EXT_TRANSCRIPCIONES:
            # No agregar como transcripción si es el archivo de links
            if 'link' not in file_path.name.lower():
                result["transcripciones"].append(rel_path)
        elif suffix in EXT_IMAGENES:
            result["imagenes"].append(rel_path)
        elif suffix in EXT_SQL:
            result["sql"].append(rel_path)
        elif suffix in EXT_CODIGO:
            result["codigo"].append(rel_path)
        elif suffix in EXT_DOCUMENTOS:
            result["documentos"].append(rel_path)
        elif suffix in EXT_LINKS:
            pass  # Ya procesado para links
        else:
            result["otros_archivos"].append(rel_path)
    
    # Eliminar duplicados de links
    result["links"]["loom"] = list(set(result["links"]["loom"]))
    result["links"]["youtube"] = list(set(result["links"]["youtube"]))
    result["links"]["otros"] = list(set(result["links"]["otros"]))
    
    return result


def print_report(result: Dict):
    """Imprime un reporte legible de los recursos encontrados."""
    
    print("\n" + "="*60)
    print("RECURSOS DETECTADOS EN EL DIRECTORIO")
    print("="*60)
    print(f"\n📁 Directorio: {result['directorio']}\n")
    
    # Contexto
    if result["contexto_yaml"]:
        print(f"✅ contexto.yaml: {result['contexto_yaml']}")
    else:
        print("⚠️  contexto.yaml: NO ENCONTRADO (requerido)")
    
    print()
    
    # Links de video
    print("🎥 VIDEOS DETECTADOS:")
    if result["links"]["loom"]:
        print(f"   Loom ({len(result['links']['loom'])}):")
        for link in result["links"]["loom"]:
            print(f"      • {link}")
    else:
        print("   Loom: ninguno")
        
    if result["links"]["youtube"]:
        print(f"   YouTube ({len(result['links']['youtube'])}):")
        for link in result["links"]["youtube"]:
            print(f"      • {link}")
    
    print()
    
    # Transcripciones
    print(f"📝 TRANSCRIPCIONES ({len(result['transcripciones'])}):")
    for t in result["transcripciones"][:10]:
        print(f"   • {t}")
    if len(result["transcripciones"]) > 10:
        print(f"   ... y {len(result['transcripciones'])-10} más")
    
    print()
    
    # Imágenes
    print(f"🖼️  IMÁGENES ({len(result['imagenes'])}):")
    for img in result["imagenes"][:10]:
        print(f"   • {img}")
    if len(result["imagenes"]) > 10:
        print(f"   ... y {len(result['imagenes'])-10} más")
    
    print()
    
    # SQL
    if result["sql"]:
        print(f"🗄️  SQL ({len(result['sql'])}):")
        for sql in result["sql"]:
            print(f"   • {sql}")
        print()
    
    # Código
    if result["codigo"]:
        print(f"💻 CÓDIGO ({len(result['codigo'])}):")
        for code in result["codigo"][:5]:
            print(f"   • {code}")
        if len(result["codigo"]) > 5:
            print(f"   ... y {len(result['codigo'])-5} más")
        print()
    
    # Documentos
    if result["documentos"]:
        print(f"📄 DOCUMENTOS ({len(result['documentos'])}):")
        for doc in result["documentos"]:
            print(f"   • {doc}")
        print()
    
    # Otros links
    if result["links"]["otros"]:
        print(f"🔗 OTROS LINKS ({len(result['links']['otros'])}):")
        for link in result["links"]["otros"][:5]:
            print(f"   • {link[:60]}...")
        print()
    
    print("="*60)


def main():
    if len(sys.argv) < 2:
        print("Uso: python scan_resources.py /ruta/directorio")
        print("     python scan_resources.py /ruta/directorio --json")
        sys.exit(1)
    
    dir_path = Path(sys.argv[1])
    
    if not dir_path.exists():
        print(f"Error: {dir_path} no existe")
        sys.exit(1)
    
    if not dir_path.is_dir():
        print(f"Error: {dir_path} no es un directorio")
        sys.exit(1)
    
    result = scan_directory(dir_path)
    
    # Output JSON si se solicita
    if '--json' in sys.argv:
        print(json.dumps(result, indent=2, ensure_ascii=False))
    else:
        print_report(result)


if __name__ == "__main__":
    main()
