#!/usr/bin/env python3
"""
clean_output.py

Script para limpar a pasta output, removendo todos os arquivos HTML gerados.
Útil para fazer uma limpeza antes de regenerar todos os artigos.

Uso:
    python scripts/clean_output.py
    python scripts/clean_output.py --confirm  # Não pede confirmação
"""

import sys
import os
from pathlib import Path
import argparse

def setup_paths():
    """Configura os caminhos base do projeto."""
    base_dir = Path(__file__).parent.parent
    return {
        'base': base_dir,
        'output': base_dir / 'output'
    }

def clean_output_folder(skip_confirm=False):
    """Limpa a pasta de saída."""
    paths = setup_paths()
    output_path = paths['output']
    
    if not output_path.exists():
        print(f"📁 Pasta output não existe: {output_path}")
        return True
    
    # Listar arquivos HTML
    html_files = list(output_path.glob('*.html'))
    
    if not html_files:
        print(f"📁 Pasta output já está limpa: {output_path}")
        return True
    
    print(f"🧹 Limpeza da Pasta Output")
    print(f"={'=' * 30}")
    print(f"📂 Pasta: {output_path}")
    print(f"📄 Arquivos HTML encontrados: {len(html_files)}")
    print()
    
    for html_file in html_files:
        size = html_file.stat().st_size
        print(f"   • {html_file.name} ({size:,} bytes)")
    
    print()
    
    # Confirmação
    if not skip_confirm:
        response = input("❓ Deseja remover todos esses arquivos? (s/N): ").lower().strip()
        if response not in ['s', 'sim', 'y', 'yes']:
            print("❌ Operação cancelada.")
            return False
    
    # Remover arquivos
    removed_count = 0
    total_size = 0
    
    for html_file in html_files:
        try:
            size = html_file.stat().st_size
            html_file.unlink()
            removed_count += 1
            total_size += size
            print(f"🗑️  Removido: {html_file.name}")
        except Exception as e:
            print(f"❌ Erro ao remover {html_file.name}: {e}")
    
    print()
    print(f"✅ Limpeza concluída!")
    print(f"📊 Estatísticas:")
    print(f"   • Arquivos removidos: {removed_count}")
    print(f"   • Espaço liberado: {total_size:,} bytes")
    print(f"   • Pasta: {output_path}")
    
    return True

def main():
    """Função principal."""
    parser = argparse.ArgumentParser(description='Limpa a pasta output removendo arquivos HTML')
    parser.add_argument('--confirm', '-c', action='store_true', help='Não pedir confirmação')
    
    args = parser.parse_args()
    
    success = clean_output_folder(skip_confirm=args.confirm)
    
    sys.exit(0 if success else 1)

if __name__ == "__main__":
    main()
