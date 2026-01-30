#!/usr/bin/env python3
"""
Anonimiza datos sensibles en textos y documentación.
Reemplaza información de clientes reales por datos genéricos de Solop ERP.

Uso:
    python anonymize_data.py /ruta/archivo.txt
    python anonymize_data.py /ruta/directorio/
    python anonymize_data.py --text "Texto con datos sensibles"
"""

import sys
import re
import argparse
from pathlib import Path
from typing import Dict, List, Tuple

# =============================================================================
# DATOS DE REEMPLAZO - SOLOP ERP
# =============================================================================

SOLOP_DATA = {
    # Empresa
    "empresa": "Solop Software C.A.",
    "empresa_corta": "Solop",
    
    # Identificaciones fiscales
    "rif": "J-12345678-9",
    "ruc": "20123456789",
    "cuit": "30-12345678-9",
    "nit": "900.123.456-7",
    "rut": "12.345.678-9",
    "cedula": "V-12.345.678",
    "dni": "12.345.678",
    
    # Direcciones
    "direccion": "Av. Principal, Edificio Solop, Piso 5, Oficina 501",
    "ciudad": "Caracas",
    "estado": "Distrito Capital",
    "pais": "Venezuela",
    "codigo_postal": "1010",
    
    # Contacto
    "telefono": "+58 212-555-1234",
    "email": "contacto@solopsoftware.com",
    "web": "www.solopsoftware.com",
    
    # Personas de ejemplo
    "personas": [
        {"nombre": "Juan Pérez", "cargo": "Gerente de Ventas", "email": "juan.perez@solop.com"},
        {"nombre": "María García", "cargo": "Supervisor de Compras", "email": "maria.garcia@solop.com"},
        {"nombre": "Carlos Rodríguez", "cargo": "Contador", "email": "carlos.rodriguez@solop.com"},
        {"nombre": "Ana Martínez", "cargo": "Vendedor", "email": "ana.martinez@solop.com"},
    ],
    
    # Productos de ejemplo
    "productos": [
        "Producto Demo A",
        "Producto Demo B", 
        "Servicio Ejemplo 1",
        "Servicio Ejemplo 2",
    ],
    
    # Bancos
    "banco": "Banco Demo",
    "cuenta_bancaria": "0000-1234-5678-9012",
}

# =============================================================================
# PATRONES DE DETECCIÓN
# =============================================================================

# RIF Venezuela: J-12345678-9, G-12345678-9, V-12345678-9
PATTERN_RIF = re.compile(
    r'\b[JGVEP]-?\d{8}-?\d\b',
    re.IGNORECASE
)

# RUC Perú: 20123456789 (11 dígitos empezando con 10, 15, 17, 20)
PATTERN_RUC = re.compile(
    r'\b(10|15|17|20)\d{9}\b'
)

# CUIT/CUIL Argentina: 20-12345678-9, 27-12345678-9, 30-12345678-9
PATTERN_CUIT = re.compile(
    r'\b(20|23|24|27|30|33|34)-?\d{8}-?\d\b'
)

# NIT Colombia: 900.123.456-7
PATTERN_NIT = re.compile(
    r'\b\d{3}\.?\d{3}\.?\d{3}-?\d\b'
)

# RUT Chile: 12.345.678-9 (con puntos obligatorios)
PATTERN_RUT_CHILE = re.compile(
    r'\b\d{1,2}\.\d{3}\.\d{3}-[\dkK]\b'
)

# Cédula Venezuela: V-12.345.678, E-12.345.678
PATTERN_CEDULA = re.compile(
    r'\b[VE]-?\d{1,2}\.?\d{3}\.?\d{3}\b',
    re.IGNORECASE
)

# DNI genérico: 12.345.678 o 12345678 (8 dígitos)
PATTERN_DNI = re.compile(
    r'\b\d{1,2}\.?\d{3}\.?\d{3}\b'
)

# Teléfonos (formatos Latam con código de país)
PATTERN_TELEFONO = re.compile(
    r'\+\d{1,3}\s\d{3}-\d{3}-\d{4}'
)

# Email
PATTERN_EMAIL = re.compile(
    r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
)

# Direcciones (heurística: palabras clave + texto)
PATTERN_DIRECCION = re.compile(
    r'(Av\.?|Avenida|Calle|Carrera|Urbanización|Urb\.?|Edificio|Edif\.?|Torre|Piso|Local|Oficina|Of\.?|Centro Comercial|C\.C\.)[^,\n]{5,50}',
    re.IGNORECASE
)

# Números de cuenta bancaria (4 grupos de 4 dígitos con guión)
PATTERN_CUENTA = re.compile(
    r'\b\d{4}-\d{4}-\d{4}-\d{4}\b'
)

# =============================================================================
# FUNCIONES DE ANONIMIZACIÓN
# =============================================================================

def anonymize_text(text: str, verbose: bool = False) -> Tuple[str, List[Dict]]:
    """
    Anonimiza datos sensibles en un texto.
    
    Returns:
        Tuple de (texto_anonimizado, lista_de_reemplazos)
    """
    replacements = []
    result = text
    
    # Función helper para registrar y reemplazar
    def replace_and_log(pattern, replacement, category):
        nonlocal result
        matches = pattern.findall(result)
        for match in set(matches):
            if isinstance(match, tuple):
                match = match[0] if match[0] else match[1] if len(match) > 1 else str(match)
            if match and len(str(match)) > 3:  # Evitar falsos positivos muy cortos
                replacements.append({
                    "original": str(match),
                    "reemplazo": replacement,
                    "categoria": category
                })
        result = pattern.sub(replacement, result)
    
    # Aplicar reemplazos en orden de especificidad (más específico primero)
    
    # 1. Emails (muy específico)
    replace_and_log(PATTERN_EMAIL, SOLOP_DATA["email"], "email")
    
    # 2. Cuentas bancarias (antes de teléfonos para evitar conflictos)
    replace_and_log(PATTERN_CUENTA, SOLOP_DATA["cuenta_bancaria"], "Cuenta Bancaria")
    
    # 3. Identificaciones fiscales
    replace_and_log(PATTERN_RIF, SOLOP_DATA["rif"], "RIF")
    replace_and_log(PATTERN_RUC, SOLOP_DATA["ruc"], "RUC")
    replace_and_log(PATTERN_CUIT, SOLOP_DATA["cuit"], "CUIT")
    replace_and_log(PATTERN_NIT, SOLOP_DATA["nit"], "NIT")
    replace_and_log(PATTERN_RUT_CHILE, SOLOP_DATA["rut"], "RUT")
    replace_and_log(PATTERN_CEDULA, SOLOP_DATA["cedula"], "Cédula")
    
    # 4. Teléfonos
    replace_and_log(PATTERN_TELEFONO, SOLOP_DATA["telefono"], "Teléfono")
    
    # 5. Direcciones (heurística, puede tener falsos positivos)
    # Solo reemplazar si parece una dirección completa
    direcciones = PATTERN_DIRECCION.findall(result)
    for dir_match in set(direcciones):
        if len(dir_match) > 15:  # Dirección razonablemente larga
            replacements.append({
                "original": dir_match,
                "reemplazo": SOLOP_DATA["direccion"],
                "categoria": "Dirección"
            })
            result = result.replace(dir_match, SOLOP_DATA["direccion"])
    
    return result, replacements


def anonymize_file(file_path: Path, output_path: Path = None, verbose: bool = False) -> Dict:
    """
    Anonimiza un archivo de texto.
    
    Returns:
        Dict con estadísticas de reemplazos
    """
    content = file_path.read_text(encoding='utf-8', errors='ignore')
    
    anonymized, replacements = anonymize_text(content, verbose)
    
    # Guardar resultado
    if output_path is None:
        output_path = file_path.with_suffix('.anonymized' + file_path.suffix)
    
    output_path.write_text(anonymized, encoding='utf-8')
    
    return {
        "archivo": str(file_path),
        "salida": str(output_path),
        "reemplazos": len(replacements),
        "detalle": replacements if verbose else []
    }


def anonymize_directory(dir_path: Path, verbose: bool = False) -> List[Dict]:
    """
    Anonimiza todos los archivos de texto en un directorio.
    """
    results = []
    
    extensions = ['*.txt', '*.vtt', '*.srt', '*.md', '*.csv']
    
    for ext in extensions:
        for file_path in dir_path.rglob(ext):
            # Saltar archivos ya anonimizados
            if '.anonymized' in file_path.name:
                continue
            # Saltar archivos de configuración
            if file_path.name in ['contexto.yaml', 'contexto.yml', 'config.yaml']:
                continue
                
            result = anonymize_file(file_path, verbose=verbose)
            results.append(result)
    
    return results


def print_report(results: List[Dict], verbose: bool = False):
    """Imprime reporte de anonimización."""
    
    print("\n" + "="*60)
    print("REPORTE DE ANONIMIZACIÓN")
    print("="*60)
    
    total_reemplazos = sum(r["reemplazos"] for r in results)
    
    print(f"\nArchivos procesados: {len(results)}")
    print(f"Total de reemplazos: {total_reemplazos}")
    
    print("\nDetalle por archivo:")
    for r in results:
        status = "✅" if r["reemplazos"] > 0 else "⚪"
        print(f"  {status} {Path(r['archivo']).name}: {r['reemplazos']} reemplazos")
        
        if verbose and r["detalle"]:
            for d in r["detalle"][:5]:  # Mostrar máximo 5
                print(f"      [{d['categoria']}] {d['original'][:30]}... → {d['reemplazo'][:30]}...")
            if len(r["detalle"]) > 5:
                print(f"      ... y {len(r['detalle'])-5} más")
    
    print("\n" + "="*60)
    print("DATOS DE REEMPLAZO UTILIZADOS (Solop ERP)")
    print("="*60)
    print(f"  Empresa: {SOLOP_DATA['empresa']}")
    print(f"  RIF: {SOLOP_DATA['rif']}")
    print(f"  Dirección: {SOLOP_DATA['direccion']}")
    print(f"  Email: {SOLOP_DATA['email']}")
    print("="*60 + "\n")


# =============================================================================
# MAIN
# =============================================================================

def main():
    parser = argparse.ArgumentParser(
        description='Anonimiza datos sensibles reemplazándolos por datos de Solop ERP'
    )
    parser.add_argument('path', nargs='?', help='Archivo o directorio a procesar')
    parser.add_argument('--text', '-t', help='Texto directo a anonimizar')
    parser.add_argument('--verbose', '-v', action='store_true', help='Mostrar detalle de reemplazos')
    parser.add_argument('--output', '-o', help='Archivo de salida (solo para archivo único)')
    
    args = parser.parse_args()
    
    if args.text:
        # Procesar texto directo
        anonymized, replacements = anonymize_text(args.text, args.verbose)
        print("\n--- TEXTO ORIGINAL ---")
        print(args.text)
        print("\n--- TEXTO ANONIMIZADO ---")
        print(anonymized)
        if args.verbose and replacements:
            print("\n--- REEMPLAZOS ---")
            for r in replacements:
                print(f"  [{r['categoria']}] {r['original']} → {r['reemplazo']}")
        return
    
    if not args.path:
        parser.print_help()
        sys.exit(1)
    
    path = Path(args.path)
    
    if not path.exists():
        print(f"Error: {path} no existe")
        sys.exit(1)
    
    if path.is_file():
        output = Path(args.output) if args.output else None
        result = anonymize_file(path, output, args.verbose)
        print_report([result], args.verbose)
    else:
        results = anonymize_directory(path, args.verbose)
        if not results:
            print("No se encontraron archivos para procesar")
            sys.exit(1)
        print_report(results, args.verbose)


if __name__ == "__main__":
    main()
