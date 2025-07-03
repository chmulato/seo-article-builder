#!/usr/bin/env python3
"""
create_html_scripts.py

Gerador de scripts    # Configurações específicas para este artigo
    config = {
        'md_file': 'articles_md/{md_file.name}',
        'html_file': 'output/{md_file.stem}.html',
        'author': '{config['author']}',
        'url': '{config['url']}',
        'keywords': '{config['keywords']}',
        'description': '{config['description']}'
    }ara converter arquivos MD específicos em HTML com SEO.
Cria um script Python para cada arquivo Markdown encontrado no diretório.
"""

import os
from pathlib import Path
from typing import List, Dict

def get_md_files() -> List[Path]:
    """Retorna lista de arquivos Markdown na pasta articles_md/."""
    articles_dir = Path('articles_md')
    if not articles_dir.exists():
        return []
    return [f for f in articles_dir.glob('*.md') if f.name != 'README.md']

def generate_script_content(md_file: Path) -> str:
    """Gera o conteúdo do script Python para um arquivo MD específico."""
    
    # Configurações baseadas no nome do arquivo
    configs = {
        'futuro_programacao.md': {
            'author': 'Christian V. Mulato',
            'url': 'https://christian-mulato.dev',
            'keywords': 'inteligência artificial, programação, AutoCAD, desenvolvimento de software, IA, futuro da programação, Christian V. Mulato',
            'description': 'Reflexão sobre como a inteligência artificial está transformando o desenvolvimento de software, comparando com a revolução do AutoCAD na engenharia civil.'
        },
        'parte1-fundamentos.md': {
            'author': 'Christian V. Mulato',
            'url': 'https://christian-mulato.dev',
            'keywords': 'Apache Kafka, Java, fundamentos, streaming, produção, consumo, programação',
            'description': 'Guia completo sobre os fundamentos do Apache Kafka com Java, incluindo produtores e consumidores.'
        },
        'parte2-java.md': {
            'author': 'Christian V. Mulato',
            'url': 'https://christian-mulato.dev',
            'keywords': 'Apache Kafka, Java, avançado, serialização, particionamento, streaming',
            'description': 'Curso avançado de Apache Kafka com Java, cobrindo tópicos como serialização, particionamento e configurações avançadas.'
        },
        'parte-final-avancado.md': {
            'author': 'Christian V. Mulato',
            'url': 'https://christian-mulato.dev',
            'keywords': 'Apache Kafka, produção, monitoramento, segurança, performance, DevOps',
            'description': 'Guia completo para uso do Apache Kafka em produção, incluindo monitoramento, segurança e otimização de performance.'
        }
    }
    
    # Usa configuração específica ou padrão
    config = configs.get(md_file.name, {
        'author': 'Christian V. Mulato',
        'url': 'https://christian-mulato.dev',
        'keywords': f'{md_file.stem.replace("-", ", ")}, programação, tecnologia',
        'description': f'Artigo sobre {md_file.stem.replace("-", " ").title()}'
    })
    
    script_content = f'''#!/usr/bin/env python3
"""
{md_file.stem}.py

Script para converter {md_file.name} em HTML com SEO otimizado.
Gerado automaticamente pelo create_html_scripts.py
"""

import sys
import subprocess
from pathlib import Path

def main():
    """Converte {md_file.name} para HTML com SEO."""
    
    # Configurações específicas para este artigo
    config = {{
        'md_file': 'articles_md/{md_file.name}',
        'html_file': 'output/{md_file.stem}.html',
        'author': '{config['author']}',
        'url': '{config['url']}',
        'keywords': '{config['keywords']}',
        'description': '{config['description']}'
    }}
    
    try:
        # Verifica se o arquivo MD existe
        if not Path(config['md_file']).exists():
            print(f"[ERROR] Arquivo não encontrado: {{config['md_file']}}")
            return 1
        
        # Executa o script format-html-seo.py
        cmd = [
            sys.executable, 'scripts/format-html-seo.py',
            config['md_file'], config['html_file'],
            '--author', config['author'],
            '--url', config['url']
        ]
        
        print(f"[PROCESS] Convertendo {{config['md_file']}} para HTML...")
        result = subprocess.run(cmd, capture_output=True, text=True)
        
        if result.returncode == 0:
            print(result.stdout)
            print(f"[SUCCESS] Conversão concluída com sucesso!")
            print(f"📁 Arquivo: {{config['html_file']}}")
            print(f"[WEB] URL: {{config['url']}}/{md_file.stem}.html")
            print(f"[MOBILE] Otimizado para SEO e redes sociais")
            
            # Informações adicionais
            print("\\n[DATA] Recursos incluídos:")
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
        print(f"[ERROR] Erro: {{e}}")
        return 1

if __name__ == "__main__":
    sys.exit(main())
'''
    
    return script_content

def create_scripts():
    """Cria scripts Python para todos os arquivos MD encontrados."""
    md_files = get_md_files()
    
    if not md_files:
        print("[ERROR] Nenhum arquivo Markdown encontrado no diretório atual.")
        return
    
    print(f"📁 Encontrados {len(md_files)} arquivos Markdown:")
    
    for md_file in md_files:
        print(f"  • {md_file.name}")
        
        # Gera o script Python
        script_name = f"scripts/conversion/{md_file.stem}.py"
        script_content = generate_script_content(md_file)
        
        # Cria o diretório se não existir
        Path("scripts/conversion").mkdir(parents=True, exist_ok=True)
        
        # Salva o script
        with open(script_name, 'w', encoding='utf-8') as f:
            f.write(script_content)
        
        print(f"    [SUCCESS] Script criado: {script_name}")
    
    print(f"\\n🎉 {len(md_files)} scripts criados com sucesso!")
    print("\\n[CONFIG] Como usar:")
    print("1. Execute o script específico: python nome_do_arquivo.py")
    print("2. Ou execute todos: python run_all_conversions.py")

def main():
    """Função principal."""
    print("[INFO] Gerador de Scripts HTML com SEO")
    print("=" * 50)
    create_scripts()

if __name__ == "__main__":
    main()
