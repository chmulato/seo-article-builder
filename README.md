# SEO Article Builder

[![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)](https://python.org)
[![Markdown](https://img.shields.io/badge/Markdown-HTML-green.svg)](https://markdown.org)
[![SEO](https://img.shields.io/badge/SEO-Optimized-orange.svg)](https://developers.google.com/search/docs)
[![License](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

## Sistema de Conversão de Artigos MD→HTML com SEO Otimizado

**Aplicação Python para converter artigos em formato Markdown para HTML responsivo com SEO otimizado**

### Funcionalidades Principais

- Conversão automática de Markdown para HTML
- SEO otimizado com meta tags, Open Graph e Schema.org
- Design responsivo mobile-first
- Syntax highlighting para código
- Lazy loading e performance otimizada
- Configurações centralizadas e customizáveis
- **Gestão automática de imagens**: Copia automaticamente imagens de `articles_md/images/` para `output/images/`

### Artigos de Exemplo

- **[Futuro da Programação com IA](articles_md/futuro_programacao.md)** → [HTML](output/futuro_programacao.html)
- **[Parte I: Fundamentos do Kafka](articles_md/parte1-fundamentos.md)** → [HTML](output/parte1-fundamentos.html)
- **[Parte II: Java com Kafka](articles_md/parte2-java.md)** → [HTML](output/parte2-java.html)
- **[Parte Final: Kafka Avançado](articles_md/parte-final-avancado.md)** → [HTML](output/parte-final-avancado.html)

### Estrutura do Projeto

```text
seo-article-builder/
├── Sistema Central
│   ├── format-html-seo.py        # Módulo principal de conversão
│   ├── html_config.py            # Configurações centralizadas
│   ├── requirements.txt          # Dependências Python
│   └── README.md                 # Documentação
│
├── Scripts Organizados
│   └── scripts/
│       ├── conversion/           # Scripts de conversão
│       │   ├── futuro_programacao.py
│       │   ├── parte1-fundamentos.py
│       │   ├── parte2-java.py
│       │   └── parte-final-avancado.py
│       ├── automation/           # Scripts de automação
│       │   ├── update_all_scripts.py
│       │   ├── run_all_conversions.py
│       │   └── create_html_scripts.py
│       └── demo/                 # Scripts de demonstração
│           └── demo_simples.py
│
├── Facilitadores (Raiz)
│   ├── demo.py                   # Demonstração principal
│   └── run_conversion.py         # Menu de conversões
│
├── Artigos e Saída
│   ├── articles_md/              # Artigos em formato Markdown
│   └── output/                   # Artigos HTML gerados
│
└── Projetos de Exemplo
    ├── parte1-fundamentos/       # Exemplo: Projeto Java básico
    ├── parte2-java/              # Exemplo: Projeto Java avançado
    └── parte-final-avancado/     # Exemplo: Configurações de produção
```

### Como Usar

#### 1. Preparar Artigos

Coloque seus artigos em formato Markdown na pasta `articles_md/`:

```text
articles_md/
├── meu_artigo.md
├── tutorial_python.md
├── guia_react.md
└── images/                       # Imagens dos artigos
    ├── diagrama1.png
    ├── screenshot.jpg
    └── logo.svg
```

**Importante**: As imagens devem estar em `articles_md/images/` e serão automaticamente copiadas para `output/images/` durante a conversão.

#### 2. Instalar Dependências

```bash
pip install -r requirements.txt
```

#### 3. Configurar Artigos

Edite `html_config.py` para adicionar configurações específicas:

```python
ARTICLE_CONFIGS = {
    'meu_artigo.md': {
        'author': 'Seu Nome',
        'keywords': 'python, tutorial, programação',
        'description': 'Descrição do seu artigo',
        'category': 'Technology',
        'reading_time': '10 min'
    }
}
```

#### 4. Converter Artigos

##### Método 1: Menu Interativo (Recomendado)

```bash
python run_conversion.py
```

##### Método 2: Demonstração Rápida

```bash
python demo.py
```

##### Método 3: Scripts Diretos

```bash
# Converter artigo específico
python scripts/conversion/nome_do_artigo.py

# Ou usar o módulo principal diretamente
python format-html-seo.py articles_md/meu_artigo.md output/meu_artigo.html
```

#### 5. Automação

```bash
# Converter todos os artigos
python scripts/automation/run_all_conversions.py

# Gerar scripts para novos artigos
python scripts/automation/create_html_scripts.py
```

### Recursos SEO Incluídos

#### Meta Tags Otimizadas

- Title, Description, Keywords
- Author, Language, Robots
- Canonical URL

#### Redes Sociais

- Open Graph (Facebook, LinkedIn, WhatsApp)
- Twitter Cards
- Imagens otimizadas (1200x630px)

#### Performance

- Lazy loading para imagens
- CSS inline otimizado
- Syntax highlighting
- Minificação automática

#### Acessibilidade

- Estrutura semântica HTML5
- Alt text para imagens
- Navegação por teclado

### Estatísticas

| Artigo | Tamanho MD | Tamanho HTML | Load Time |
|--------|------------|--------------|-----------|
| Futuro da Programação | 4,219 bytes | 17,967 bytes | 0.35s |
| Parte I: Fundamentos | 6,914 bytes | 29,924 bytes | 0.58s |
| Parte II: Java | 8,521 bytes | 35,867 bytes | 0.70s |
| Parte Final: Avançado | 4,008 bytes | 17,583 bytes | 0.34s |

### Configurações

Edite `html_config.py` para personalizar configurações globais e específicas por artigo:

```python
# Configurações globais padrão
DEFAULT_CONFIG = {
    'author': 'Seu Nome',
    'url': 'https://seu-site.com',
    'language': 'pt-BR',
    'theme_color': '#667eea'
}

# Configurações específicas por artigo
ARTICLE_CONFIGS = {
    'meu_artigo.md': {
        'author': 'Nome do Autor',
        'keywords': 'palavras, chave, artigo',
        'description': 'Descrição do artigo para SEO',
        'category': 'Technology',
        'reading_time': '5 min',
        'social_image': 'imagem_social.png'
    }
}
```

### Exemplos de Uso

Este projeto inclui artigos de exemplo sobre Apache Kafka que demonstram as capacidades do sistema:

1. **Artigos Técnicos**: Tutoriais sobre programação e tecnologia
2. **Projetos Práticos**: Exemplos com código e configurações
3. **Documentação**: Guias e manuais técnicos

**Os exemplos incluídos:**

- Futuro da Programação com IA
- Fundamentos do Apache Kafka
- Integração Java com Kafka
- Configurações de Produção

### Requisitos

- Python 3.8+
- Dependências: `markdown`, `beautifulsoup4`, `Pygments`
- Opcional: JDK 11+ e Maven para exemplos Java

### Adicionando Novos Artigos

1. **Criar arquivo MD**: Adicione seu artigo em `articles_md/`
2. **Configurar**: Adicione configurações em `html_config.py`
3. **Gerar script**: Execute `python scripts/automation/create_html_scripts.py`
4. **Converter**: Use o script gerado ou o módulo principal

### Próximos Passos

1. **Visualizar**: Abrir arquivos HTML no navegador
2. **Testar**: Verificar responsividade mobile
3. **Validar**: Usar ferramentas de SEO online
4. **Publicar**: Fazer upload para servidor web
5. **Compartilhar**: Postar nas redes sociais

### Autor

Christian V. Mulato

- Website: [christian-mulato.dev](https://christian-mulato.dev)
- Desenvolvedor Java Sênior
- Especialista em Apache Kafka

### Licença

Este projeto está sob a licença MIT. Veja o arquivo [LICENSE](LICENSE) para mais detalhes.

---

**Aplicação Python para formatação profissional de artigos Markdown em HTML responsivo com SEO otimizado.**
