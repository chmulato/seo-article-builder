#!/usr/bin/env python3
"""
html_config.py

Configurações para conversão de MD para HTML com SEO.
Centralize todas as configurações específicas de cada artigo aqui.
"""

from typing import Dict, Any

# Configurações globais padrão
DEFAULT_CONFIG = {
    'author': 'Christian V. Mulato',
    'url': 'https://christian-mulato.dev',
    'language': 'pt-BR',
    'theme_color': '#667eea',
    'social_image_size': {
        'width': 1200,
        'height': 630
    }
}

# Configurações específicas para cada arquivo
ARTICLE_CONFIGS = {
    'futuro_programacao.md': {
        'author': 'Christian V. Mulato',
        'url': 'https://christian-mulato.dev',
        'keywords': 'inteligência artificial, programação, AutoCAD, desenvolvimento de software, IA, futuro da programação, Christian V. Mulato, prancheta, prompt',
        'description': 'Reflexão sobre como a inteligência artificial está transformando o desenvolvimento de software, comparando com a revolução do AutoCAD na engenharia civil. Da prancheta ao prompt.',
        'category': 'Technology',
        'tags': ['IA', 'Programação', 'AutoCAD', 'Desenvolvimento', 'Futuro'],
        'reading_time': '8 min',
        'social_image': 'futuro_programacao.png'
    },
    
    'parte1-fundamentos.md': {
        'author': 'Christian V. Mulato',
        'url': 'https://christian-mulato.dev',
        'keywords': 'Apache Kafka, Java, fundamentos, streaming, produção, consumo, programação, microservices, event-driven',
        'description': 'Guia completo sobre os fundamentos do Apache Kafka com Java, incluindo produtores e consumidores. Aprenda streaming de dados e arquitetura event-driven.',
        'category': 'Programming',
        'tags': ['Kafka', 'Java', 'Streaming', 'Microservices', 'Event-Driven'],
        'reading_time': '15 min',
        'social_image': 'kafka-java-parte1.png'
    },
    
    'parte2-java.md': {
        'author': 'Christian V. Mulato',
        'url': 'https://christian-mulato.dev',
        'keywords': 'Apache Kafka, Java, avançado, serialização, particionamento, streaming, performance, configuração',
        'description': 'Curso avançado de Apache Kafka com Java, cobrindo tópicos como serialização, particionamento e configurações avançadas para alta performance.',
        'category': 'Programming',
        'tags': ['Kafka', 'Java', 'Avançado', 'Serialização', 'Performance'],
        'reading_time': '20 min',
        'social_image': 'kafka-java-parte2.png'
    },
    
    'parte-final-avancado.md': {
        'author': 'Christian V. Mulato',
        'url': 'https://christian-mulato.dev',
        'keywords': 'Apache Kafka, produção, monitoramento, segurança, performance, DevOps, Docker, Kubernetes',
        'description': 'Guia completo para uso do Apache Kafka em produção, incluindo monitoramento, segurança e otimização de performance com Docker e Kubernetes.',
        'category': 'DevOps',
        'tags': ['Kafka', 'Produção', 'Monitoramento', 'Segurança', 'DevOps'],
        'reading_time': '25 min',
        'social_image': 'kafka-java-parte-final.png'
    },
    
    'guia-completo.md': {
        'author': 'Christian V. Mulato',
        'url': 'https://christian-mulato.dev',
        'keywords': 'Apache Kafka, Java, guia completo, tutorial, streaming, microservices, event-driven architecture',
        'description': 'Guia completo de Apache Kafka com Java - do básico ao avançado. Aprenda streaming de dados, microservices e arquitetura event-driven.',
        'category': 'Tutorial',
        'tags': ['Kafka', 'Java', 'Tutorial', 'Completo', 'Streaming'],
        'reading_time': '45 min',
        'social_image': 'kafka-java-completo.png'
    }
}

def get_config_for_file(filename: str) -> Dict[str, Any]:
    """Retorna configuração específica para um arquivo ou configuração padrão."""
    config = DEFAULT_CONFIG.copy()
    
    if filename in ARTICLE_CONFIGS:
        config.update(ARTICLE_CONFIGS[filename])
    else:
        # Gera configuração padrão baseada no nome do arquivo
        file_stem = filename.replace('.md', '').replace('-', ' ').title()
        config.update({
            'keywords': f'{filename.replace(".md", "").replace("-", ", ")}, programação, tecnologia, Christian V. Mulato',
            'description': f'Artigo sobre {file_stem} - Programação e tecnologia por Christian V. Mulato',
            'category': 'Technology',
            'tags': [file_stem, 'Programação', 'Tecnologia'],
            'reading_time': '10 min',
            'social_image': f'{filename.replace(".md", "")}.png'
        })
    
    return config

def get_all_configs() -> Dict[str, Dict[str, Any]]:
    """Retorna todas as configurações disponíveis."""
    return ARTICLE_CONFIGS

def update_config(filename: str, new_config: Dict[str, Any]):
    """Atualiza configuração para um arquivo específico."""
    if filename not in ARTICLE_CONFIGS:
        ARTICLE_CONFIGS[filename] = DEFAULT_CONFIG.copy()
    
    ARTICLE_CONFIGS[filename].update(new_config)

# Configurações de estilo CSS customizadas
CSS_THEMES = {
    'default': {
        'primary_color': '#667eea',
        'secondary_color': '#764ba2',
        'background_gradient': 'linear-gradient(135deg, #f5f7fa 0%, #c3cfe2 100%)',
        'font_family': "'Inter', 'Segoe UI', system-ui, -apple-system, sans-serif"
    },
    
    'dark': {
        'primary_color': '#4f46e5',
        'secondary_color': '#7c3aed',
        'background_gradient': 'linear-gradient(135deg, #1e1e2e 0%, #2d2d44 100%)',
        'font_family': "'Inter', 'Segoe UI', system-ui, -apple-system, sans-serif"
    },
    
    'tech': {
        'primary_color': '#00d4aa',
        'secondary_color': '#0ea5e9',
        'background_gradient': 'linear-gradient(135deg, #f0f9ff 0%, #e0f2fe 100%)',
        'font_family': "'Fira Code', 'Consolas', monospace"
    }
}

def get_css_theme(theme_name: str = 'default') -> Dict[str, str]:
    """Retorna tema CSS específico."""
    return CSS_THEMES.get(theme_name, CSS_THEMES['default'])

# Configurações de SEO avançadas
SEO_SETTINGS = {
    'enable_sitemap': True,
    'enable_robots_txt': True,
    'enable_amp': False,
    'enable_pwa': False,
    'google_analytics_id': '',
    'google_search_console_id': '',
    'facebook_app_id': '',
    'twitter_site': '@christianmulato',
    'linkedin_profile': 'https://linkedin.com/in/chmulato',
    'github_profile': 'https://github.com/chmulato'
}

def get_seo_settings() -> Dict[str, Any]:
    """Retorna configurações de SEO."""
    return SEO_SETTINGS

if __name__ == "__main__":
    # Exemplo de uso
    print("[CONFIG] Configurações disponíveis:")
    print(f"Arquivos configurados: {len(ARTICLE_CONFIGS)}")
    for filename in ARTICLE_CONFIGS:
        config = get_config_for_file(filename)
        print(f"  • {filename}: {config['description'][:50]}...")
    
    print(f"\n🎨 Temas CSS disponíveis: {list(CSS_THEMES.keys())}")
    print(f"[INFO] SEO configurado: {SEO_SETTINGS['enable_sitemap']}")
