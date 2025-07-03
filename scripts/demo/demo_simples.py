#!/usr/bin/env python3
"""
demo_simples.py

Demonstração simples do sistema Apache Kafka.
"""

import os
import sys
from pathlib import Path

def main():
    """Demonstra os artigos disponíveis."""
    print("🚀 Sistema de Conversão Apache Kafka MD→HTML")
    print("=" * 50)
    print("Por Christian V. Mulato")
    print()
    
    # Verifica os arquivos na pasta articles_md
    articles_dir = Path("articles_md")
    if articles_dir.exists():
        print("📚 Artigos disponíveis:")
        for md_file in articles_dir.glob("*.md"):
            print(f"  • {md_file.name}")
    else:
        print("❌ Pasta articles_md não encontrada")
        return
    
    print()
    
    # Verifica os arquivos na pasta output
    output_dir = Path("output")
    if output_dir.exists():
        print("🌐 Arquivos HTML gerados:")
        for html_file in output_dir.glob("*.html"):
            print(f"  • {html_file.name}")
    else:
        print("❌ Pasta output não encontrada")
        return
    
    print()
    print("🎯 Para converter um artigo específico:")
    print("  python futuro_programacao.py")
    print("  python parte1-fundamentos.py")
    print("  python parte2-java.py")
    print("  python parte-final-avancado.py")
    print()
    print("🔧 Sistema funcionando corretamente!")

if __name__ == "__main__":
    main()
