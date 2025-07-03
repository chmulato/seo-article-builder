#!/usr/bin/env python3
"""
build_all.py

Script para converter todos os artigos de MD para HTML com SEO otimizado.
Processa todos os arquivos .md da pasta content/ e gera HTML na pasta output/.

Uso:
    python scripts/build_all.py
    python scripts/build_all.py --clean  # Limpa output antes de gerar
"""

import sys
import os
from pathlib import Path
import argparse
import time

# Adicionar o diretório raiz ao path
sys.path.insert(0, str(Path(__file__).parent.parent))

def setup_paths():
    """Configura os caminhos base do projeto."""
    base_dir = Path(__file__).parent.parent
    return {
        'base': base_dir,
        'content': base_dir / 'content',
        'assets': base_dir / 'assets',
        'output': base_dir / 'output',
        'scripts': base_dir / 'scripts'
    }

def clean_output_folder(output_path):
    """Limpa a pasta de saída."""
    if output_path.exists():
        for file in output_path.glob('*.html'):
            file.unlink()
        print(f"🧹 Pasta output limpa: {len(list(output_path.glob('*')))} arquivos removidos")

def get_markdown_files(content_path):
    """Obtém lista de arquivos Markdown na pasta content."""
    md_files = list(content_path.glob('*.md'))
    # Excluir arquivos de documentação
    exclude_files = {'README.md', 'CHANGELOG.md', 'TODO.md'}
    md_files = [f for f in md_files if f.name not in exclude_files]
    return sorted(md_files)

def build_all_articles(clean_first=False):
    """Constrói todos os artigos."""
    paths = setup_paths()
    
    # Criar pastas se não existirem
    paths['output'].mkdir(parents=True, exist_ok=True)
    
    print(f"🚀 SEO Article Builder - Conversão em Lote")
    print(f"={'=' * 50}")
    
    # Limpar output se solicitado
    if clean_first:
        clean_output_folder(paths['output'])
    
    # Obter arquivos MD
    md_files = get_markdown_files(paths['content'])
    
    if not md_files:
        print(f"❌ Nenhum arquivo .md encontrado em: {paths['content']}")
        return False
    
    print(f"📄 Encontrados {len(md_files)} arquivos para conversão:")
    for md_file in md_files:
        print(f"   • {md_file.name}")
    print()
    
    # Processar cada arquivo
    successful = 0
    failed = 0
    start_time = time.time()
    
    for md_file in md_files:
        try:
            print(f"🔄 Processando: {md_file.name}")
            
            # Importar e usar o script de conversão individual
            from build_single import build_article
            
            success = build_article(
                md_file=str(md_file),
                output_file=None,  # Usar nome automático
                author="Christian V. Mulato",
                base_url="https://christian-mulato.dev"
            )
            
            if success:
                successful += 1
                print(f"✅ {md_file.name} → {md_file.stem}.html")
            else:
                failed += 1
                print(f"❌ Falha em {md_file.name}")
                
        except Exception as e:
            failed += 1
            print(f"❌ Erro em {md_file.name}: {e}")
        
        print("-" * 30)
    
    # Resumo final
    end_time = time.time()
    total_time = end_time - start_time
    
    print(f"\n📊 Resumo da Conversão:")
    print(f"✅ Sucessos: {successful}")
    print(f"❌ Falhas: {failed}")
    print(f"📁 Total: {len(md_files)} arquivos")
    print(f"⏱️ Tempo: {total_time:.2f} segundos")
    print(f"📂 Saída: {paths['output']}")
    
    if successful > 0:
        print(f"\n🎯 Próximos passos:")
        print(f"   1. Verificar arquivos em: {paths['output']}")
        print(f"   2. Testar no navegador")
        print(f"   3. Validar SEO")
        print(f"   4. Publicar no servidor")
    
    return failed == 0

def main():
    """Função principal."""
    parser = argparse.ArgumentParser(description='Converte todos os artigos MD para HTML com SEO')
    parser.add_argument('--clean', '-c', action='store_true', help='Limpar pasta output antes de gerar')
    
    args = parser.parse_args()
    
    success = build_all_articles(clean_first=args.clean)
    
    sys.exit(0 if success else 1)

if __name__ == "__main__":
    main()
