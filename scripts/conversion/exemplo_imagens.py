#!/usr/bin/env python3
"""
exemplo_imagens.py

Script para converter exemplo_imagens.md em HTML com SEO otimizado.
Demonstra o uso de imagens no sistema.
"""

import sys
import subprocess
from pathlib import Path
import json
import os

# Importa configurações se disponível
try:
    sys.path.append(str(Path(__file__).parent.parent.parent))
    from html_config import ARTICLE_CONFIGS, DEFAULT_CONFIG
    CONFIG_AVAILABLE = True
except ImportError:
    CONFIG_AVAILABLE = False
    print("[WARNING] Configurações não encontradas, usando valores padrão")

def main():
    """Converte o artigo exemplo_imagens.md para HTML."""
    
    print('[INFO] SEO Article Builder - Exemplo de Imagens')
    print('==================================================')
    print('[CONFIG] Configurações:')
    print('  • Arquivo MD: articles_md/exemplo_imagens.md')
    print('  • Arquivo HTML: output/exemplo_imagens.html')
    print('  • Autor: Christian V. Mulato')
    print('  • URL: https://christian-mulato.dev')
    print('  • Categoria: Tutorial')
    print('  • Tempo de leitura: 5 min')
    
    try:
        print('[PROCESS] Iniciando conversão...')
        print('[FILE] Processando: articles_md/exemplo_imagens.md')
        
        # Caminho para o script principal
        script_path = Path(__file__).parent.parent.parent / 'format-html-seo.py'
        
        # Executa o script principal
        result = subprocess.run([
            sys.executable, str(script_path),
            'articles_md/exemplo_imagens.md',
            'output/exemplo_imagens.html',
            '--author', 'Christian V. Mulato',
            '--url', 'https://christian-mulato.dev'
        ], capture_output=True, text=True, cwd=str(script_path.parent))
        
        if result.returncode == 0:
            print('[SUCCESS] Conversão concluída com sucesso!')
            print(result.stdout)
            
            # Estatísticas do arquivo
            md_path = Path('articles_md/exemplo_imagens.md')
            html_path = Path('output/exemplo_imagens.html')
            
            if md_path.exists() and html_path.exists():
                md_size = md_path.stat().st_size
                html_size = html_path.stat().st_size
                
                print('[DATA] Arquivo gerado:')
                print(f'  📁 Local: {html_path}')
                print('[WEB] URL: https://christian-mulato.dev/exemplo_imagens.html')
                print('[MOBILE] Otimizado para SEO e redes sociais')
                print('[STATS] Estatísticas:')
                print(f'[MD] Arquivo MD: {md_size:,} bytes')
                print(f'[WEB] Arquivo HTML: {html_size:,} bytes')
                print(f'[SPEED] Tempo de carregamento estimado: {html_size/50000:.2f}s')
                
                print('[SEO] Recursos SEO incluídos:')
                print('   1. Meta tags otimizadas (title, description, keywords)')
                print('   2. Open Graph para redes sociais (Facebook, LinkedIn, WhatsApp)')
                print('   3. Twitter Cards para compartilhamento')
                print('   4. Schema.org structured data (JSON-LD)')
                print('   5. Design responsivo mobile-first')
                print('   6. Syntax highlighting para código')
                print('   7. Lazy loading para imagens')
                print('   8. Links externos seguros')
                print('   9. Estrutura semântica HTML5')
                print('  10. Performance otimizada')
                
                print('[PROCESS] Próximos passos:')
                print('  1. Abrir output/exemplo_imagens.html no navegador')
                print('  2. Testar responsividade em dispositivos móveis')
                print('  3. Validar SEO com ferramentas online')
                print('  4. Publicar no servidor web')
                print('  5. Compartilhar nas redes sociais')
                
                print('[DEV] Recursos do conteúdo:')
                print('  1. Demonstração de uso de imagens')
                print('  2. Exemplos práticos de referências')
                print('  3. Otimizações automáticas')
                print('  4. Gestão inteligente de assets')
        else:
            print(f'[ERROR] Erro na conversão: {result.stderr}')
            return 1
        
    except Exception as e:
        print(f'[ERROR] Erro na conversão: {e}')
        return 1
    
    return 0

if __name__ == '__main__':
    sys.exit(main())
