#!/usr/bin/env python3
"""
Descarga imágenes desde URLs encontradas en archivos del directorio de entrega.
Solo descarga imágenes públicas directas (PNG, JPG, GIF, WEBP) y screenshots de Loom.
NO descarga thumbnails de videos.

Soporta:
- URLs directas a imágenes: https://ejemplo.com/imagen.png
- Screenshots de Loom: https://loom.com/i/ID?workflows_screenshot=true

Uso:
    python download_images.py /ruta/directorio/entrega
    python download_images.py /ruta/directorio/entrega --output-dir /ruta/salida
"""

import sys
import re
import subprocess
from pathlib import Path
from typing import List, Set, Tuple
from urllib.parse import urlparse

# Patrones para detectar URLs de imágenes directas
IMAGE_URL_PATTERN = re.compile(
    r'https?://[^\s<>"\']+\.(?:png|jpg|jpeg|gif|webp|svg)',
    re.IGNORECASE
)

# Patrón para URLs de Loom screenshots (workflows_screenshot=true)
LOOM_SCREENSHOT_PATTERN = re.compile(
    r'https?://loom\.com/i/[a-f0-9]+\?workflows_screenshot=true',
    re.IGNORECASE
)

# Patrones de URLs a IGNORAR (thumbnails, previews, etc.)
IGNORED_PATTERNS = [
    r'loom\.com/.*thumbnails',
    r'youtube\.com/.*thumb',
    r'youtu\.be/.*thumb',
    r'/preview/',
    r'/thumbnail/',
]

# Extensiones de archivos a escanear
SCAN_EXTENSIONS = {'.txt', '.md', '.vtt', '.docx', '.pdf', '.html'}


def is_ignored_url(url: str) -> bool:
    """Verifica si la URL debe ser ignorada (thumbnails, previews, etc.)"""
    for pattern in IGNORED_PATTERNS:
        if re.search(pattern, url, re.IGNORECASE):
            return True
    return False


def is_loom_screenshot(url: str) -> bool:
    """Verifica si la URL es un screenshot de Loom"""
    return bool(LOOM_SCREENSHOT_PATTERN.match(url))


def is_public_image_url(url: str) -> bool:
    """Verifica si la URL es una imagen pública directa o un screenshot de Loom"""
    # Debe ser una URL válida
    try:
        parsed = urlparse(url)
        if not parsed.scheme in ['http', 'https']:
            return False
    except:
        return False

    # Puede ser un screenshot de Loom
    if is_loom_screenshot(url):
        return True

    # Debe tener extensión de imagen
    if not IMAGE_URL_PATTERN.match(url):
        return False

    # No debe estar en la lista de ignorados
    if is_ignored_url(url):
        return False

    return True


def extract_image_urls_from_file(file_path: Path) -> Set[str]:
    """Extrae URLs de imágenes de un archivo"""
    urls = set()

    try:
        # Para DOCX, primero convertir a texto si es necesario
        if file_path.suffix == '.docx':
            # Ya tenemos el contenido en .txt si fue procesado
            txt_path = file_path.with_suffix('.txt')
            if txt_path.exists():
                file_path = txt_path
            else:
                return urls

        with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
            content = f.read()

        # Buscar URLs de imágenes normales
        found_urls = IMAGE_URL_PATTERN.findall(content)

        # Buscar URLs de Loom screenshots
        loom_urls = LOOM_SCREENSHOT_PATTERN.findall(content)
        found_urls.extend(loom_urls)

        for url in found_urls:
            if is_public_image_url(url):
                urls.add(url)

    except Exception as e:
        print(f"  ⚠️  Error leyendo {file_path.name}: {e}")

    return urls


def scan_directory_for_images(directory: Path) -> Set[str]:
    """Escanea recursivamente el directorio buscando URLs de imágenes"""
    all_urls = set()

    print(f"\n🔍 Escaneando directorio: {directory}")

    for file_path in directory.rglob('*'):
        if file_path.is_file() and file_path.suffix in SCAN_EXTENSIONS:
            urls = extract_image_urls_from_file(file_path)
            if urls:
                print(f"  📄 {file_path.name}: {len(urls)} imagen(es) encontrada(s)")
                all_urls.update(urls)

    return all_urls


def download_image(url: str, output_dir: Path) -> Tuple[bool, str]:
    """
    Descarga una imagen desde una URL.
    Retorna (success, filename)
    """
    try:
        # Generar nombre de archivo desde URL
        parsed = urlparse(url)

        # Para URLs de Loom, extraer el ID y usar como nombre
        if is_loom_screenshot(url):
            # Extraer el ID del screenshot (formato: loom.com/i/ID?workflows_screenshot=true)
            match = re.search(r'/i/([a-f0-9]+)', url)
            if match:
                loom_id = match.group(1)
                filename = f"loom-screenshot-{loom_id}.png"
            else:
                filename = "loom-screenshot.png"
        else:
            filename = Path(parsed.path).name

            # Si el nombre es muy genérico, usar parte del host
            if filename in ['image.png', 'image.jpg', 'photo.png']:
                host_part = parsed.netloc.replace('.', '-')
                filename = f"{host_part}-{filename}"

        output_path = output_dir / filename

        # Evitar sobrescribir si ya existe
        if output_path.exists():
            print(f"  ⏭️  Ya existe: {filename}")
            return True, filename

        # Descargar con curl (silencioso pero muestra errores)
        result = subprocess.run(
            ['curl', '-sS', '-L', '-o', str(output_path), url],
            capture_output=True,
            text=True,
            timeout=30
        )

        if result.returncode == 0 and output_path.exists():
            size_kb = output_path.stat().st_size / 1024
            print(f"  ✅ Descargado: {filename} ({size_kb:.1f} KB)")
            return True, filename
        else:
            error_msg = result.stderr.strip() if result.stderr else "Error desconocido"
            print(f"  ❌ Error descargando {url}: {error_msg}")
            return False, ""

    except subprocess.TimeoutExpired:
        print(f"  ⏱️  Timeout descargando: {url}")
        return False, ""
    except Exception as e:
        print(f"  ❌ Error: {e}")
        return False, ""


def download_all_images(urls: Set[str], output_dir: Path) -> List[str]:
    """Descarga todas las imágenes encontradas"""
    output_dir.mkdir(parents=True, exist_ok=True)

    print(f"\n📥 Descargando {len(urls)} imagen(es) a: {output_dir}")

    downloaded = []

    for url in sorted(urls):
        success, filename = download_image(url, output_dir)
        if success and filename:
            downloaded.append(filename)

    return downloaded


def main():
    if len(sys.argv) < 2:
        print("Uso: python download_images.py <directorio> [--output-dir <salida>]")
        sys.exit(1)

    input_dir = Path(sys.argv[1])

    if not input_dir.exists() or not input_dir.is_dir():
        print(f"❌ Error: {input_dir} no es un directorio válido")
        sys.exit(1)

    # Directorio de salida (por defecto: <input_dir>/images)
    output_dir = input_dir / 'images'

    if '--output-dir' in sys.argv:
        idx = sys.argv.index('--output-dir')
        if idx + 1 < len(sys.argv):
            output_dir = Path(sys.argv[idx + 1])

    print("=" * 60)
    print("DESCARGA DE IMÁGENES DESDE URLs")
    print("=" * 60)

    # Escanear directorio
    image_urls = scan_directory_for_images(input_dir)

    if not image_urls:
        print("\n⚠️  No se encontraron URLs de imágenes públicas")
        print("\nNota: Se descargan:")
        print("      - URLs directas a imágenes (*.png, *.jpg, etc.)")
        print("      - Screenshots de Loom (loom.com/i/ID?workflows_screenshot=true)")
        print("      NO se descargan thumbnails de videos de Loom/YouTube")
        return

    print(f"\n✓ Total de URLs únicas encontradas: {len(image_urls)}")

    # Mostrar URLs que se van a descargar
    print("\n📋 URLs a descargar:")
    for url in sorted(image_urls):
        print(f"  • {url}")

    # Descargar
    downloaded = download_all_images(image_urls, output_dir)

    # Resumen
    print("\n" + "=" * 60)
    print(f"✅ Descarga completada: {len(downloaded)}/{len(image_urls)} imagen(es)")
    print("=" * 60)

    if downloaded:
        print(f"\n📁 Imágenes guardadas en: {output_dir}")
        print("\nArchivos descargados:")
        for filename in downloaded:
            print(f"  • {filename}")

    # Sugerencia para el siguiente paso
    if downloaded:
        print("\n💡 Siguiente paso:")
        print(f"   Copiar imágenes a la documentación:")
        print(f"   cp {output_dir}/*.{{png,jpg,jpeg,gif}} <ruta-docs>/")


if __name__ == '__main__':
    main()
