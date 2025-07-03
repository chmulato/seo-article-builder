#!/usr/bin/env python3
"""
seo_config.py

Configurações centralizadas para SEO e geração de HTML.
Todas as configurações específicas de cada artigo ficam aqui.
"""

from typing import Dict, Any

# Configurações globais padrão
DEFAULT_CONFIG = {
    'author': 'Christian V. Mulato',
    'base_url': 'https://christian-mulato.dev',
    'language': 'pt-BR',
    'theme_color': '#667eea',
    'site_name': 'Christian V. Mulato',
    'twitter_handle': '@christianv.mulato',
    'social_image_size': {
        'width': 1200,
        'height': 630
    },
    'default_category': 'Technology',
    'default_reading_time': '5 min'
}

# Configurações específicas para cada arquivo
ARTICLE_CONFIGS = {
    'futuro_programacao.md': {
        'title': 'Da Prancheta ao Prompt: O Futuro da Criação de Softwares com IA',
        'description': 'Reflexão sobre como a inteligência artificial está transformando o desenvolvimento de software, comparando com a revolução do AutoCAD na engenharia civil.',
        'keywords': 'inteligência artificial, programação, AutoCAD, desenvolvimento de software, IA, futuro da programação, prompt, prancheta',
        'category': 'Technology',
        'tags': ['IA', 'Programação', 'AutoCAD', 'Desenvolvimento', 'Futuro'],
        'reading_time': '8 min',
        'social_image': 'futuro_programacao.png',
        'custom_css': None
    },
    
    'parte1-fundamentos.md': {
        'title': 'Parte I: Fundamentos do Apache Kafka',
        'description': 'Guia completo sobre os fundamentos do Apache Kafka com Java, incluindo produtores e consumidores. Aprenda streaming de dados e arquitetura event-driven.',
        'keywords': 'Apache Kafka, Java, fundamentos, streaming, produção, consumo, programação, microservices, event-driven',
        'category': 'Programming',
        'tags': ['Kafka', 'Java', 'Streaming', 'Microservices', 'Event-Driven'],
        'reading_time': '15 min',
        'social_image': 'kafka-java-parte1.png',
        'custom_css': None
    },
    
    'parte2-java.md': {
        'title': 'Parte II: Java com Apache Kafka',
        'description': 'Aprenda Java avançado com Apache Kafka, incluindo serialização, particionamento, configurações de performance e práticas de produção.',
        'keywords': 'Apache Kafka, Java, avançado, serialização, particionamento, streaming, performance, configuração',
        'category': 'Programming',
        'tags': ['Kafka', 'Java', 'Avançado', 'Serialização', 'Performance'],
        'reading_time': '20 min',
        'social_image': 'kafka-java-parte2.png',
        'custom_css': None
    },
    
    'parte-final-avancado.md': {
        'title': 'Parte Final: Kafka Avançado e Produção',
        'description': 'Configurações avançadas do Apache Kafka para produção, incluindo monitoramento, segurança, Kafka Streams e boas práticas.',
        'keywords': 'Apache Kafka, produção, monitoramento, segurança, Kafka Streams, DevOps, observabilidade',
        'category': 'DevOps',
        'tags': ['Kafka', 'Produção', 'Monitoramento', 'Segurança', 'DevOps'],
        'reading_time': '25 min',
        'social_image': 'kafka-java-parte-final.png',
        'custom_css': None
    },
    
    'guia-completo.md': {
        'title': 'Guia Completo: Apache Kafka com Java',
        'description': 'Guia completo e abrangente sobre Apache Kafka com Java, desde fundamentos até configurações avançadas de produção.',
        'keywords': 'Apache Kafka, Java, guia completo, streaming, microservices, produção, desenvolvimento',
        'category': 'Programming',
        'tags': ['Kafka', 'Java', 'Guia', 'Streaming', 'Completo'],
        'reading_time': '30 min',
        'social_image': 'kafka-java-guia.png',
        'custom_css': None
    }
}

def get_config_for_file(filename: str) -> Dict[str, Any]:
    """
    Obtém a configuração completa para um arquivo específico.
    Combina configurações padrão com configurações específicas do arquivo.
    """
    # Começar com configurações padrão
    config = DEFAULT_CONFIG.copy()
    
    # Aplicar configurações específicas do arquivo se existirem
    if filename in ARTICLE_CONFIGS:
        file_config = ARTICLE_CONFIGS[filename]
        config.update(file_config)
    
    # Garantir que campos obrigatórios existam
    if 'title' not in config:
        config['title'] = filename.replace('.md', '').replace('-', ' ').title()
    
    if 'description' not in config:
        config['description'] = f"Artigo sobre {config['title']}"
    
    if 'keywords' not in config:
        config['keywords'] = config['title'].lower().replace(' ', ', ')
    
    # Construir URL completa
    if 'base_url' in config:
        html_filename = filename.replace('.md', '.html')
        config['canonical_url'] = f"{config['base_url'].rstrip('/')}/{html_filename}"
        
        # URL da imagem social
        if 'social_image' in config:
            config['social_image_url'] = f"{config['base_url'].rstrip('/')}/assets/images/{config['social_image']}"
    
    return config

def get_all_article_configs() -> Dict[str, Dict[str, Any]]:
    """
    Retorna configurações completas para todos os artigos.
    """
    configs = {}
    for filename in ARTICLE_CONFIGS.keys():
        configs[filename] = get_config_for_file(filename)
    return configs

def add_article_config(filename: str, config: Dict[str, Any]):
    """
    Adiciona configuração para um novo artigo.
    """
    ARTICLE_CONFIGS[filename] = config

def update_default_config(new_config: Dict[str, Any]):
    """
    Atualiza configurações padrão.
    """
    DEFAULT_CONFIG.update(new_config)

# Exemplo de uso
if __name__ == "__main__":
    # Testar configurações
    print("🔧 Testando Configurações de SEO")
    print("=" * 40)
    
    # Testar configuração de um arquivo específico
    config = get_config_for_file('futuro_programacao.md')
    print(f"Configuração para 'futuro_programacao.md':")
    for key, value in config.items():
        print(f"  {key}: {value}")
    
    print("\n" + "=" * 40)
    
    # Listar todos os artigos configurados
    print(f"Artigos configurados:")
    for filename in ARTICLE_CONFIGS.keys():
        print(f"  • {filename}")
    
    print(f"\nTotal: {len(ARTICLE_CONFIGS)} artigos configurados")
