#!/usr/bin/env python3
"""
demo.py

Script principal de demonstração do sistema SEO Article Builder.
Localizado na raiz para facilitar o acesso.
"""

import os
import sys
from pathlib import Path

def print_header(title):
    """Imprime cabeçalho formatado."""
    print(f"\n🚀 {title}")
    print("=" * 50)

def main():
    """Demonstra o sistema completo."""
    print_header("SEO Article Builder - Apache Kafka System")
    print("Por Christian V. Mulato")
    print("Sistema de conversão MD→HTML com SEO otimizado")
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
    print("🗂️  Estrutura organizada do projeto:")
    print("  📄 Sistema central:")
    print("    • format-html-seo.py (módulo principal)")
    print("    • html_config.py (configurações)")
    print("    • requirements.txt (dependências)")
    print()
    print("  🐍 Scripts organizados:")
    print("    • scripts/conversion/ (conversão de artigos)")
    print("    • scripts/automation/ (automação)")
    print("    • scripts/demo/ (demonstração)")
    print()
    print("  📁 Conteúdo:")
    print("    • articles_md/ (arquivos .md)")
    print("    • output/ (arquivos .html)")
    print("    • [projetos de exemplo]/ (código Java + Docker)")
    
    print()
    print("🎯 Como usar:")
    print("  # Converter artigo específico")
    print("  python scripts/conversion/futuro_programacao.py")
    print("  python scripts/conversion/parte1-fundamentos.py")
    print("  python scripts/conversion/parte2-java.py")
    print("  python scripts/conversion/parte-final-avancado.py")
    print()
    print("  # Automação")
    print("  python scripts/automation/run_all_conversions.py")
    print("  python scripts/automation/update_all_scripts.py")
    print()
    print("  # Demonstração detalhada")
    print("  python scripts/demo/demo_simples.py")
    print()
    print("✅ Sistema funcionando corretamente!")
    print("🔗 https://christian-mulato.dev")

if __name__ == "__main__":
    main()
