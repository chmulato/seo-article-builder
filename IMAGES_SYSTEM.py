#!/usr/bin/env python3
"""
IMAGES_SYSTEM.py

Script para converter IMAGES_SYSTEM.md em HTML com SEO otimizado.
Gerado automaticamente pelo create_html_scripts.py
"""

import sys
import subprocess
from pathlib import Path

def main():
    """Converte IMAGES_SYSTEM.md para HTML com SEO."""
    
    # Configurações específicas para este artigo
    config = {
        'md_file': 'IMAGES_SYSTEM.md',
        'html_file': 'IMAGES_SYSTEM.html',
        'author': 'Christian V. Mulato',
        'url': 'https://christian-mulato.dev',
        'keywords': 'IMAGES_SYSTEM, programação, tecnologia',
        'description': 'Artigo sobre Images_System'
    }
    
    try:
        # Verifica se o arquivo MD existe
        if not Path(config['md_file']).exists():
            print(f"[ERROR] Arquivo não encontrado: {config['md_file']}")
            return 1
        
        # Executa o script format-html-seo.py
        cmd = [
            sys.executable, 'format-html-seo.py',
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
            print(f"[WEB] URL: {config['url']}/IMAGES_SYSTEM.html")
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
