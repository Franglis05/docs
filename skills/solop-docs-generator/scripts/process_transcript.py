#!/usr/bin/env python3
"""
Procesa transcripciones de video (.vtt, .srt, .txt) y extrae el contenido limpio.
Útil para procesar transcripciones de Loom u otras fuentes.

Uso:
    python process_transcript.py /ruta/al/archivo.vtt
    python process_transcript.py /ruta/directorio/transcripciones/
"""

import sys
import re
from pathlib import Path
from typing import List, Tuple


def parse_vtt(content: str) -> str:
    """
    Parsea archivo VTT y extrae solo el texto.
    Elimina timestamps, índices y metadatos.
    """
    lines = content.split('\n')
    text_lines = []
    
    # Patrón para timestamps VTT: 00:00:00.000 --> 00:00:00.000
    timestamp_pattern = re.compile(r'\d{2}:\d{2}:\d{2}[.,]\d{3}\s*-->\s*\d{2}:\d{2}:\d{2}[.,]\d{3}')
    # Patrón para números de índice
    index_pattern = re.compile(r'^\d+$')
    
    skip_next = False
    for line in lines:
        line = line.strip()
        
        # Saltar líneas vacías
        if not line:
            continue
            
        # Saltar header WEBVTT
        if line.startswith('WEBVTT'):
            continue
            
        # Saltar timestamps
        if timestamp_pattern.match(line):
            continue
            
        # Saltar índices numéricos
        if index_pattern.match(line):
            continue
            
        # Saltar metadatos (líneas que empiezan con NOTE, STYLE, etc)
        if line.startswith(('NOTE', 'STYLE', 'REGION')):
            continue
        
        # Limpiar tags HTML/VTT
        line = re.sub(r'<[^>]+>', '', line)
        
        # Agregar línea de texto
        if line:
            text_lines.append(line)
    
    # Unir y limpiar duplicados consecutivos
    result = []
    prev_line = None
    for line in text_lines:
        if line != prev_line:
            result.append(line)
            prev_line = line
    
    return '\n'.join(result)


def parse_srt(content: str) -> str:
    """
    Parsea archivo SRT y extrae solo el texto.
    """
    lines = content.split('\n')
    text_lines = []
    
    # Patrón para timestamps SRT: 00:00:00,000 --> 00:00:00,000
    timestamp_pattern = re.compile(r'\d{2}:\d{2}:\d{2},\d{3}\s*-->\s*\d{2}:\d{2}:\d{2},\d{3}')
    index_pattern = re.compile(r'^\d+$')
    
    for line in lines:
        line = line.strip()
        
        if not line:
            continue
        if timestamp_pattern.match(line):
            continue
        if index_pattern.match(line):
            continue
            
        # Limpiar tags
        line = re.sub(r'<[^>]+>', '', line)
        line = re.sub(r'\{[^}]+\}', '', line)
        
        if line:
            text_lines.append(line)
    
    # Limpiar duplicados
    result = []
    prev_line = None
    for line in text_lines:
        if line != prev_line:
            result.append(line)
            prev_line = line
    
    return '\n'.join(result)


def parse_txt(content: str) -> str:
    """
    Procesa archivo de texto plano.
    Limpia líneas vacías excesivas y normaliza.
    """
    lines = content.split('\n')
    text_lines = []
    
    empty_count = 0
    for line in lines:
        line = line.strip()
        
        if not line:
            empty_count += 1
            if empty_count <= 1:  # Permitir máximo 1 línea vacía
                text_lines.append('')
        else:
            empty_count = 0
            text_lines.append(line)
    
    return '\n'.join(text_lines).strip()


def process_file(file_path: Path) -> Tuple[str, str]:
    """
    Procesa un archivo de transcripción.
    
    Returns:
        Tuple de (nombre_archivo, contenido_procesado)
    """
    content = file_path.read_text(encoding='utf-8', errors='ignore')
    
    suffix = file_path.suffix.lower()
    
    if suffix == '.vtt':
        processed = parse_vtt(content)
    elif suffix == '.srt':
        processed = parse_srt(content)
    else:  # .txt u otros
        processed = parse_txt(content)
    
    return (file_path.name, processed)


def process_directory(dir_path: Path) -> List[Tuple[str, str]]:
    """
    Procesa todos los archivos de transcripción en un directorio.
    """
    results = []
    
    for ext in ['*.vtt', '*.srt', '*.txt']:
        for file_path in dir_path.glob(ext):
            # Ignorar archivos que parecen ser de configuración
            if file_path.name in ['contexto.yaml', 'contexto.yml', 'config.yaml']:
                continue
            results.append(process_file(file_path))
    
    return results


def main():
    if len(sys.argv) < 2:
        print("Uso: python process_transcript.py <archivo_o_directorio>")
        sys.exit(1)
    
    path = Path(sys.argv[1])
    
    if path.is_file():
        name, content = process_file(path)
        print(f"=== {name} ===\n")
        print(content)
    elif path.is_dir():
        results = process_directory(path)
        if not results:
            print("No se encontraron archivos de transcripción (.vtt, .srt, .txt)")
            sys.exit(1)
        
        for name, content in results:
            print(f"\n{'='*60}")
            print(f"=== {name} ===")
            print('='*60)
            print(content)
            print()
    else:
        print(f"Error: {path} no existe")
        sys.exit(1)


if __name__ == "__main__":
    main()
