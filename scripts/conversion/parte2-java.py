#!/usr/bin/env python3
"""
parte2-java.py

Script para converter parte2-java.md em HTML com SEO otimizado.
Versão avançada com integração ao sistema de configurações.
"""

import sys
import subprocess
from pathlib import Path
import json
import os

# Importa configurações se disponível
try:
    from html_config import get_config_for_file
    CONFIG_AVAILABLE = True
except ImportError:
    CONFIG_AVAILABLE = False

def get_article_config():
    """Obtém configurações específicas para este artigo."""
    if CONFIG_AVAILABLE:
        config = get_config_for_file('parte2-java.md')
        # Adiciona campos necessários que podem não estar no config
        config.update({
            'md_file': 'articles_md/parte2-java.md',
            'html_file': 'output/parte2-java.html'
        })
        return config
    else:
        # Configurações padrão se não houver arquivo de config
        return {
            'md_file': 'articles_md/parte2-java.md',
            'html_file': 'output/parte2-java.html',
            'author': 'Christian V. Mulato',
            'url': 'https://christian-mulato.dev',
            'keywords': 'parte2, java, programação, tecnologia, Christian V. Mulato',
            'description': 'Curso avançado de Apache Kafka com Java, cobrindo tópicos como serialização, particionamento e configurações avançadas para alta performance.',
            'category': 'Programming',
            'reading_time': '20 min',
            'social_image': 'parte2-java.png',
            'language': 'pt-BR'
        }

def validate_environment(config):
    """Valida se o ambiente está configurado corretamente."""
    issues = []
    
    # Verifica se o arquivo MD existe
    md_file = Path(config['md_file'])
    if not md_file.exists():
        issues.append(f"[ERROR] Arquivo {md_file} não encontrado")
    
    # Verifica se o script format-html-seo.py existe
    if not Path('format-html-seo.py').exists():
        issues.append("[ERROR] Script format-html-seo.py não encontrado")
    
    # Verifica dependências
    try:
        import markdown
        from bs4 import BeautifulSoup
    except ImportError as e:
        issues.append(f"[ERROR] Dependência faltando: {e}")
    
    return issues

def print_conversion_stats(config):
    """Exibe estatísticas sobre a conversão."""
    md_file = Path(config['md_file'])
    html_file = Path(config['html_file'])
    
    if md_file.exists():
        md_size = md_file.stat().st_size
        print(f"[MD] Arquivo MD: {md_size:,} bytes")
    
    if html_file.exists():
        html_size = html_file.stat().st_size
        print(f"[WEB] Arquivo HTML: {html_size:,} bytes")
        
        # Calcula estatísticas aproximadas
        estimated_load_time = html_size / (1024 * 50)  # ~50KB/s estimado
        print(f"[SPEED] Tempo de carregamento estimado: {estimated_load_time:.2f}s")

def main():
    """Converte parte2-java.md para HTML com SEO."""
    
    print("[INFO] Kafka Java Mastery - Parte 2: Java Avançado")
    print("=" * 50)
    
    # Obtém configurações
    config = get_article_config()
    
    # Valida ambiente
    issues = validate_environment(config)
    if issues:
        print("⚠️  Problemas encontrados:")
        for issue in issues:
            print(f"  {issue}")
        return 1
    
    try:
        print(f"[CONFIG] Configurações:")
        print(f"  • Arquivo MD: {config['md_file']}")
        print(f"  • Arquivo HTML: {config['html_file']}")
        print(f"  • Autor: {config['author']}")
        print(f"  • URL: {config['url']}")
        print(f"  • Categoria: {config.get('category', 'N/A')}")
        print(f"  • Tempo de leitura: {config.get('reading_time', 'N/A')}")
        
        # Prepara comando de conversão
        cmd = [
            sys.executable, 'format-html-seo.py',
            config['md_file'], config['html_file'],
            '--author', config['author'],
            '--url', config['url'],
            '--lang', config.get('language', 'pt-BR')
        ]
        
        print(f"\n[PROCESS] Iniciando conversão...")
        print(f"[FILE] Processando: {config['md_file']}")
        
        # Executa conversão
        result = subprocess.run(cmd, capture_output=True, text=True)
        
        if result.returncode == 0:
            print(f"\n[SUCCESS] Conversão concluída com sucesso!")
            print(result.stdout)
            
            # Informações do arquivo gerado
            print(f"\n[DATA] Arquivo gerado:")
            print(f"  📁 Local: {config['html_file']}")
            print(f"  [WEB] URL: {config['url']}/{Path(config['html_file']).stem}.html")
            print(f"  [MOBILE] Otimizado para SEO e redes sociais")
            
            # Estatísticas
            print(f"\n[STATS] Estatísticas:")
            print_conversion_stats(config)
            
            # Recursos SEO incluídos
            print(f"\n[SEO] Recursos SEO incluídos:")
            seo_features = [
                "Meta tags otimizadas (title, description, keywords)",
                "Open Graph para redes sociais (Facebook, LinkedIn, WhatsApp)",
                "Twitter Cards para compartilhamento",
                "Schema.org structured data (JSON-LD)",
                "Design responsivo mobile-first",
                "Syntax highlighting para código",
                "Lazy loading para imagens",
                "Links externos seguros",
                "Estrutura semântica HTML5",
                "Performance otimizada"
            ]
            
            for i, feature in enumerate(seo_features, 1):
                print(f"  {i:2d}. {feature}")
            
            # Próximos passos
            print(f"\n[PROCESS] Próximos passos:")
            print(f"  1. Abrir {config['html_file']} no navegador")
            print(f"  2. Testar responsividade em dispositivos móveis")
            print(f"  3. Validar SEO com ferramentas online")
            print(f"  4. Publicar no servidor web")
            print(f"  5. Compartilhar nas redes sociais")
            
            # Informações específicas do conteúdo
            print(f"\n[DEV] Recursos do conteúdo:")
            dev_features = [
                "Serialização avançada e custom serializers",
                "Particionamento e balanceamento de carga",
                "Configurações de performance e tuning",
                "Exemplos avançados de streaming",
            ]
            
            for i, feature in enumerate(dev_features, 1):
                print(f"  {i}. {feature}")
            
        else:
            print(f"[ERROR] Erro na conversão:")
            print(result.stderr)
            return 1
            
        return 0
        
    except Exception as e:
        print(f"[ERROR] Erro inesperado: {e}")
        return 1

if __name__ == "__main__":
    sys.exit(main())
