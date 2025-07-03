#!/usr/bin/env python3
"""
parte1-fundamentos.py

Script para converter parte1-fundamentos.md em HTML com SEO otimizado.
Gerado automaticamente pelo create_html_scripts.py
"""

import sys
import subprocess
from pathlib import Path

def main():
    """Converte parte1-fundamentos.md para HTML com SEO."""
    
    # Configurações específicas para este artigo
    config = {
        'md_file': 'articles_md/parte1-fundamentos.md',
        'html_file': 'output/parte1-fundamentos.html',
        'author': 'Christian V. Mulato',
        'url': 'https://christian-mulato.dev',
        'keywords': 'Apache Kafka, Java, fundamentos, streaming, produção, consumo, programação',
        'description': 'Guia completo sobre os fundamentos do Apache Kafka com Java, incluindo produtores e consumidores.'
    }
    
    try:
        # Verifica se o arquivo MD existe
        if not Path(config['md_file']).exists():
            print(f"[ERROR] Arquivo não encontrado: {config['md_file']}")
            return 1
        
        # Executa o script format-html-seo.py
        cmd = [
            sys.executable, 'scripts/format-html-seo.py',
            config['md_file'], config['html_file'],
            '--author', config['author'],
            '--url', config['url']
        ]
        
        print(f"[PROCESS] Convertendo {config['md_file']} para HTML...")
        result = subprocess.run(cmd, capture_output=True, text=True)
        
        if result.returncode == 0:
            print(result.stdout)
            print(f"[SUCCESS] Conversão concluída com sucesso!")
            print(f"📁 Arquivo: {config['html_file']}")
            print(f"[WEB] URL: {config['url']}/parte1-fundamentos.html")
            print(f"[MOBILE] Otimizado para SEO e redes sociais")
            
            # Informações adicionais
            print("\n[DATA] Recursos incluídos:")
            print("• Meta tags otimizadas")
            print("• Open Graph para redes sociais") 
            print("• Schema.org structured data")
            print("• Design responsivo")
            print("• Syntax highlighting")
            print("• Lazy loading para imagens")
            
        else:
            print(f"[ERROR] Erro na conversão:")
            print(result.stderr)
            return 1
            
        return 0
        
    except Exception as e:
        print(f"[ERROR] Erro: {e}")
        return 1

if __name__ == "__main__":
    sys.exit(main())
