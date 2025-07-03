#!/usr/bin/env python3
"""
futuro_programacao.py

Script para converter futuro_programacao.md em HTML com SEO otimizado.
Gerado automaticamente pelo create_html_scripts.py
"""

import sys
import subprocess
from pathlib import Path

def main():
    """Converte futuro_programacao.md para HTML com SEO."""
    
    # Configurações específicas para este artigo
    config = {
        'md_file': 'articles_md/futuro_programacao.md',
        'html_file': 'output/futuro_programacao.html',
        'author': 'Christian V. Mulato',
        'url': 'https://christian-mulato.dev',
        'keywords': 'inteligência artificial, programação, AutoCAD, desenvolvimento de software, IA, futuro da programação, Christian V. Mulato',
        'description': 'Reflexão sobre como a inteligência artificial está transformando o desenvolvimento de software, comparando com a revolução do AutoCAD na engenharia civil.'
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
            print(f"[WEB] URL: {config['url']}/futuro_programacao.html")
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
