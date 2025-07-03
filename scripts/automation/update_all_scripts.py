#!/usr/bin/env python3
"""
update_all_scripts.py

Script para atualizar todos os scripts de conversão MD → HTML com as novas funcionalidades.
Usa o template avançado baseado no parte1-fundamentos.py atualizado.
"""

import os
import sys
from pathlib import Path
from typing import Dict, List

def get_md_files() -> List[Path]:
    """Retorna lista de arquivos Markdown no diretório atual."""
    return [f for f in Path('.').glob('*.md') if f.name != 'README.md']

def get_article_specific_config(md_file: Path) -> Dict[str, str]:
    """Retorna configurações específicas para cada artigo."""
    
    configs = {
        'futuro_programacao.md': {
            'title': 'Kafka Java Mastery - Futuro da Programação',
            'category': 'Technology',
            'reading_time': '8 min',
            'description_detail': 'Reflexão sobre como a inteligência artificial está transformando o desenvolvimento de software, comparando com a revolução do AutoCAD na engenharia civil.',
            'dev_features': [
                'Comparação entre AutoCAD e IA na programação',
                'Reflexões sobre o futuro do desenvolvimento',
                'Experiências práticas com IA e código',
                'Perspectivas de um desenvolvedor sênior'
            ]
        },
        
        'parte1-fundamentos.md': {
            'title': 'Kafka Java Mastery - Parte 1: Fundamentos',
            'category': 'Programming',
            'reading_time': '15 min',
            'description_detail': 'Guia completo sobre os fundamentos do Apache Kafka com Java, incluindo produtores e consumidores. Aprenda streaming de dados e arquitetura event-driven.',
            'dev_features': [
                'Código Java/Kafka com syntax highlighting',
                'Exemplos práticos de produtores e consumidores',
                'Configurações de ambiente Docker',
                'Exercícios práticos incluídos'
            ]
        },
        
        'parte2-java.md': {
            'title': 'Kafka Java Mastery - Parte 2: Java Avançado',
            'category': 'Programming',
            'reading_time': '20 min',
            'description_detail': 'Curso avançado de Apache Kafka com Java, cobrindo tópicos como serialização, particionamento e configurações avançadas para alta performance.',
            'dev_features': [
                'Serialização avançada e custom serializers',
                'Particionamento e balanceamento de carga',
                'Configurações de performance e tuning',
                'Exemplos avançados de streaming'
            ]
        },
        
        'parte-final-avancado.md': {
            'title': 'Kafka Java Mastery - Parte Final: Produção',
            'category': 'DevOps',
            'reading_time': '25 min',
            'description_detail': 'Guia completo para uso do Apache Kafka em produção, incluindo monitoramento, segurança e otimização de performance com Docker e Kubernetes.',
            'dev_features': [
                'Configurações de produção e monitoramento',
                'Segurança e autenticação',
                'Docker e Kubernetes para Kafka',
                'Backup e disaster recovery'
            ]
        },
        
        'guia-completo.md': {
            'title': 'Kafka Java Mastery - Guia Completo',
            'category': 'Tutorial',
            'reading_time': '45 min',
            'description_detail': 'Guia completo de Apache Kafka com Java - do básico ao avançado. Aprenda streaming de dados, microservices e arquitetura event-driven.',
            'dev_features': [
                'Tutorial completo do básico ao avançado',
                'Arquitetura de microservices com Kafka',
                'Padrões de design event-driven',
                'Projeto prático completo'
            ]
        }
    }
    
    # Configuração padrão para arquivos não mapeados
    file_stem = md_file.stem.replace('-', ' ').title()
    return configs.get(md_file.name, {
        'title': f'Kafka Java Mastery - {file_stem}',
        'category': 'Technology',
        'reading_time': '10 min',
        'description_detail': f'Artigo sobre {file_stem} - Programação e tecnologia por Christian V. Mulato.',
        'dev_features': [
            f'Conteúdo técnico sobre {file_stem}',
            'Exemplos práticos e código',
            'Configurações e boas práticas',
            'Exercícios e projetos práticos'
        ]
    })

def generate_advanced_script(md_file: Path) -> str:
    """Gera script Python avançado para um arquivo MD específico."""
    
    config = get_article_specific_config(md_file)
    script_name = md_file.stem
    
    # Gera lista de recursos para desenvolvedores
    dev_features_str = '\n'.join([f'                "{feature}",' for feature in config['dev_features']])
    
    script_content = f'''#!/usr/bin/env python3
"""
{script_name}.py

Script para converter {md_file.name} em HTML com SEO otimizado.
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
        config = get_config_for_file('{md_file.name}')
        # Adiciona campos necessários que podem não estar no config
        config.update({{
            'md_file': '{md_file.name}',
            'html_file': '{script_name}.html'
        }})
        return config
    else:
        # Configurações padrão se não houver arquivo de config
        return {{
            'md_file': '{md_file.name}',
            'html_file': '{script_name}.html',
            'author': 'Christian V. Mulato',
            'url': 'https://christian-mulato.dev',
            'keywords': '{script_name.replace("-", ", ")}, programação, tecnologia, Christian V. Mulato',
            'description': '{config["description_detail"]}',
            'category': '{config["category"]}',
            'reading_time': '{config["reading_time"]}',
            'social_image': '{script_name}.png',
            'language': 'pt-BR'
        }}

def validate_environment():
    """Valida se o ambiente está configurado corretamente."""
    issues = []
    
    # Verifica se o arquivo MD existe
    if not Path('{md_file.name}').exists():
        issues.append("[ERROR] Arquivo {md_file.name} não encontrado")
    
    # Verifica se o script format-html-seo.py existe
    if not Path('format-html-seo.py').exists():
        issues.append("[ERROR] Script format-html-seo.py não encontrado")
    
    # Verifica dependências
    try:
        import markdown
        from bs4 import BeautifulSoup
    except ImportError as e:
        issues.append(f"[ERROR] Dependência faltando: {{e}}")
    
    return issues

def print_conversion_stats(config):
    """Exibe estatísticas sobre a conversão."""
    md_file = Path(config['md_file'])
    html_file = Path(config['html_file'])
    
    if md_file.exists():
        md_size = md_file.stat().st_size
        print(f"[MD] Arquivo MD: {{md_size:,}} bytes")
    
    if html_file.exists():
        html_size = html_file.stat().st_size
        print(f"[WEB] Arquivo HTML: {{html_size:,}} bytes")
        
        # Calcula estatísticas aproximadas
        estimated_load_time = html_size / (1024 * 50)  # ~50KB/s estimado
        print(f"[SPEED] Tempo de carregamento estimado: {{estimated_load_time:.2f}}s")

def main():
    """Converte {md_file.name} para HTML com SEO."""
    
    print("[INFO] {config['title']}")
    print("=" * 50)
    
    # Obtém configurações
    config = get_article_config()
    
    # Valida ambiente
    issues = validate_environment()
    if issues:
        print("⚠️  Problemas encontrados:")
        for issue in issues:
            print(f"  {{issue}}")
        return 1
    
    try:
        print(f"[CONFIG] Configurações:")
        print(f"  • Arquivo MD: {{config['md_file']}}")
        print(f"  • Arquivo HTML: {{config['html_file']}}")
        print(f"  • Autor: {{config['author']}}")
        print(f"  • URL: {{config['url']}}")
        print(f"  • Categoria: {{config.get('category', 'N/A')}}")
        print(f"  • Tempo de leitura: {{config.get('reading_time', 'N/A')}}")
        
        # Prepara comando de conversão
        cmd = [
            sys.executable, 'format-html-seo.py',
            config['md_file'], config['html_file'],
            '--author', config['author'],
            '--url', config['url'],
            '--lang', config.get('language', 'pt-BR')
        ]
        
        print(f"\\n[PROCESS] Iniciando conversão...")
        print(f"[FILE] Processando: {{config['md_file']}}")
        
        # Executa conversão
        result = subprocess.run(cmd, capture_output=True, text=True)
        
        if result.returncode == 0:
            print(f"\\n[SUCCESS] Conversão concluída com sucesso!")
            print(result.stdout)
            
            # Informações do arquivo gerado
            print(f"\\n[DATA] Arquivo gerado:")
            print(f"  📁 Local: {{config['html_file']}}")
            print(f"  [WEB] URL: {{config['url']}}/{{Path(config['html_file']).stem}}.html")
            print(f"  [MOBILE] Otimizado para SEO e redes sociais")
            
            # Estatísticas
            print(f"\\n[STATS] Estatísticas:")
            print_conversion_stats(config)
            
            # Recursos SEO incluídos
            print(f"\\n[SEO] Recursos SEO incluídos:")
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
                print(f"  {{i:2d}}. {{feature}}")
            
            # Próximos passos
            print(f"\\n[PROCESS] Próximos passos:")
            print(f"  1. Abrir {{config['html_file']}} no navegador")
            print(f"  2. Testar responsividade em dispositivos móveis")
            print(f"  3. Validar SEO com ferramentas online")
            print(f"  4. Publicar no servidor web")
            print(f"  5. Compartilhar nas redes sociais")
            
            # Informações específicas do conteúdo
            print(f"\\n[DEV] Recursos do conteúdo:")
            dev_features = [
{dev_features_str}
            ]
            
            for i, feature in enumerate(dev_features, 1):
                print(f"  {{i}}. {{feature}}")
            
        else:
            print(f"[ERROR] Erro na conversão:")
            print(result.stderr)
            return 1
            
        return 0
        
    except Exception as e:
        print(f"[ERROR] Erro inesperado: {{e}}")
        return 1

if __name__ == "__main__":
    sys.exit(main())
'''
    
    return script_content

def update_scripts():
    """Atualiza todos os scripts de conversão com a nova funcionalidade."""
    md_files = get_md_files()
    
    if not md_files:
        print("[ERROR] Nenhum arquivo Markdown encontrado no diretório atual.")
        return
    
    print(f"[PROCESS] Atualizando {len(md_files)} scripts com nova funcionalidade:")
    print("=" * 60)
    
    updated_count = 0
    
    for md_file in md_files:
        print(f"  [MD] Processando {md_file.name}...")
        
        # Gera o script atualizado
        script_name = f"{md_file.stem}.py"
        script_content = generate_advanced_script(md_file)
        
        # Salva o script atualizado
        with open(script_name, 'w', encoding='utf-8') as f:
            f.write(script_content)
        
        print(f"    [SUCCESS] Script atualizado: {script_name}")
        updated_count += 1
    
    print(f"\\n🎉 {updated_count} scripts atualizados com sucesso!")
    print("\\n[INFO] Novos recursos incluídos:")
    print("  • Integração com sistema de configurações")
    print("  • Validação de ambiente")
    print("  • Estatísticas de conversão")
    print("  • Informações específicas por tipo de conteúdo")
    print("  • Recursos SEO detalhados")
    print("  • Próximos passos sugeridos")
    
    print("\\n[CONFIG] Como usar:")
    print("  python nome_do_script.py     # Executa script específico")
    print("  python run_all_conversions.py # Executa todos os scripts")

def main():
    """Função principal."""
    print("[INFO] Atualizador de Scripts MD → HTML com SEO")
    print("Versão avançada com novas funcionalidades")
    print("Desenvolvido por Christian V. Mulato")
    print()
    
    update_scripts()

if __name__ == "__main__":
    main()
