#!/usr/bin/env python3
"""
build_single.py

Script para converter um artigo individual de MD para HTML com SEO otimizado.
Usa a nova estrutura de pastas organizada.

Uso:
    python scripts/build_single.py content/artigo.md
    python scripts/build_single.py content/artigo.md --output custom_output.html
"""

import sys
import os
import importlib.util
from pathlib import Path
import argparse

# Adicionar o diretório raiz ao path
sys.path.insert(0, str(Path(__file__).parent.parent))

# Importar o módulo de conversão
try:
    # Importar usando importlib para lidar com hífens no nome
    import importlib.util
    spec = importlib.util.spec_from_file_location("format_html_seo", Path(__file__).parent.parent / "format-html-seo.py")
    format_html_seo = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(format_html_seo)
    MarkdownToHtmlSEO = format_html_seo.MarkdownToHtmlSEO
except Exception as e:
    print("❌ Erro: Não foi possível importar o módulo de conversão")
    print(f"   Erro: {e}")
    print("   Certifique-se de que o arquivo 'format-html-seo.py' existe no diretório raiz")
    sys.exit(1)

def setup_paths():
    """Configura os caminhos base do projeto."""
    base_dir = Path(__file__).parent.parent
    return {
        'base': base_dir,
        'content': base_dir / 'content',
        'assets': base_dir / 'assets',
        'output': base_dir / 'output',
        'config': base_dir / 'config'
    }

def validate_paths(paths):
    """Valida se as pastas necessárias existem."""
    required_dirs = ['content', 'assets', 'output']
    for dir_name in required_dirs:
        if not paths[dir_name].exists():
            print(f"❌ Erro: Pasta '{dir_name}' não encontrada")
            print(f"   Esperado em: {paths[dir_name]}")
            return False
    return True

def build_article(md_file, output_file=None, author="Christian V. Mulato", base_url="https://christian-mulato.dev"):
    """Constrói um artigo individual."""
    paths = setup_paths()
    
    if not validate_paths(paths):
        return False
    
    # Converter para Path objects
    md_path = Path(md_file)
    
    # Verificar se o arquivo MD existe
    if not md_path.exists():
        print(f"❌ Erro: Arquivo '{md_file}' não encontrado")
        return False
    
    # Determinar arquivo de saída
    if output_file is None:
        output_file = paths['output'] / f"{md_path.stem}.html"
    else:
        output_file = Path(output_file)
        if not output_file.is_absolute():
            output_file = paths['output'] / output_file
    
    # Criar pasta de saída se não existir
    output_file.parent.mkdir(parents=True, exist_ok=True)
    
    print(f"🚀 SEO Article Builder - Conversão Individual")
    print(f"={'=' * 50}")
    print(f"📄 Entrada: {md_path}")
    print(f"🌐 Saída: {output_file}")
    print(f"👤 Autor: {author}")
    print(f"🔗 URL: {base_url}")
    print()
    
    try:
        # Criar o conversor
        converter = MarkdownToHtmlSEO(author=author, base_url=base_url)
        
        # Converter o arquivo
        result = converter.convert_md_to_html(
            md_file=str(md_path),
            html_file=str(output_file)
        )
        
        # Estatísticas
        md_size = md_path.stat().st_size
        html_size = output_file.stat().st_size
        
        print(f"✅ Conversão concluída com sucesso!")
        print(f"📊 Estatísticas:")
        print(f"   • Arquivo MD: {md_size:,} bytes")
        print(f"   • Arquivo HTML: {html_size:,} bytes")
        print(f"   • Arquivo gerado: {output_file}")
        print()
        print(f"🎯 Próximos passos:")
        print(f"   1. Abrir {output_file.name} no navegador")
        print(f"   2. Validar SEO e responsividade")
        print(f"   3. Publicar no servidor web")
        
        return True
        
    except Exception as e:
        print(f"❌ Erro na conversão: {e}")
        return False

def main():
    """Função principal."""
    parser = argparse.ArgumentParser(description='Converte artigo MD para HTML com SEO')
    parser.add_argument('md_file', help='Arquivo Markdown de entrada')
    parser.add_argument('--output', '-o', help='Arquivo HTML de saída (opcional)')
    parser.add_argument('--author', '-a', default='Christian V. Mulato', help='Nome do autor')
    parser.add_argument('--url', '-u', default='https://christian-mulato.dev', help='URL base do site')
    
    args = parser.parse_args()
    
    success = build_article(
        md_file=args.md_file,
        output_file=args.output,
        author=args.author,
        base_url=args.url
    )
    
    sys.exit(0 if success else 1)

if __name__ == "__main__":
    main()
