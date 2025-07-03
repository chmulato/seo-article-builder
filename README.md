# SEO Article Builder

[![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)](https://python.org)
[![Markdown](https://img.shields.io/badge/Markdown-HTML-green.svg)](https://markdown.org)
[![SEO](https://img.shields.io/badge/SEO-Optimized-orange.svg)](https://developers.google.com/search/docs)
[![License](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

## Sistema Automatizado de Conversão MD→HTML com SEO Otimizado

Aplicação Python profissional para converter artigos em formato Markdown para HTML responsivo com SEO otimizado

### 🚀 Início Rápido

```bash
# 1. Instalar dependências
pip install -r requirements.txt

# 2. Colocar artigos .md na pasta articles_md/

# 3. Executar conversão automática
python start.py
```

### ✨ Funcionalidades Principais

- **Conversão Automática**: Converte todos os arquivos `.md` de `articles_md/` para HTML
- **SEO Otimizado**: Meta tags, Open Graph, Schema.org, Twitter Cards
- **Design Responsivo**: Layout mobile-first com CSS moderno
- **Syntax Highlighting**: Realce de código com highlight.js
- **Performance**: Lazy loading, CSS inline, recursos otimizados
- **Logging Profissional**: Logs detalhados com timestamps
- **Gestão de Imagens**: Copia automaticamente imagens para output
- **Estrutura Semântica**: HTML5 com microdata para SEO

### 📂 Estrutura do Projeto

```text
seo-article-builder/
├── start.py                      # 🎯 ÚNICO PONTO DE ENTRADA
├── requirements.txt              # Dependências Python
├── README.md                     # Documentação
├── LICENSE                       # Licença MIT
│
├── articles_md/                  # 📝 Artigos em Markdown
│   ├── artigo1.md
│   ├── artigo2.md
│   └── images/                   # Imagens dos artigos
│       ├── diagrama1.png
│       └── screenshot.jpg
│
├── output/                       # 🌐 HTML gerados
│   ├── artigo1.html
│   ├── artigo2.html
│   └── images/                   # Imagens copiadas
│
├── logs/                         # 📊 Logs detalhados
│   └── YYYY_MM_DD_HH_MM_SS_seo_conversion.log
│
├── scripts/                      # 🔧 Scripts organizados
│   ├── format-html-seo.py       # Módulo principal de conversão
│   ├── html_config.py           # Configurações centralizadas
│   ├── demo.py                  # Demonstração
│   ├── run_conversion.py        # Conversão individual
│   ├── build_all.py             # Build completo
│   ├── build_single.py          # Build individual
│   ├── clean_output.py          # Limpeza
│   ├── conversion/              # Scripts de conversão específicos
│   ├── automation/              # Scripts de automação
│   └── demo/                    # Demonstrações
│
├── config/                       # ⚙️ Configurações
│   └── seo_config.py            # Configurações SEO
│
├── java_code/                    # ☕ Código Java dos exemplos
└── backup_removed_files/         # 🗃️ Backup automático
```

### 🎯 Como Usar

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

#### 2. Instalar Dependências

```bash
pip install -r requirements.txt
```

#### 3. Executar Conversão

```bash
python start.py
```

O sistema fará automaticamente:

- ✅ Busca todos os arquivos `.md` em `articles_md/`
- ✅ Converte cada um para HTML otimizado
- ✅ Salva na pasta `output/`
- ✅ Gera log detalhado em `logs/`
- ✅ Copia imagens para `output/images/`
- ✅ Para em caso de erro e registra no log

### 📊 Exemplo de Execução

```text
SEO Article Builder - Conversão Automatizada
============================================================
Cara Core Informática - www.caracore.com.br
Log salvo em: logs\2025_07_03_18_36_00_seo_conversion.log
============================================================

PREPARANDO AMBIENTE...
Pasta de saída preparada: output

BUSCANDO ARTIGOS PARA CONVERSÃO...
Encontrados 8 arquivo(s) .md na pasta articles_md/
  • artigo-seo-builder.md
  • exemplo_imagens.md
  • formatando_seo.md
  • futuro_programacao.md
  • parte1-fundamentos.md
  • parte2-java.md

INICIANDO CONVERSÕES...
--------------------------------------------------
Iniciando conversão de artigo-seo-builder.md
Arquivo de entrada: articles_md/artigo-seo-builder.md
Arquivo de saída: output/artigo-seo-builder.html
CONVERSÃO CONCLUÍDA: artigo-seo-builder.md → output/artigo-seo-builder.html

============================================================
RELATÓRIO FINAL
CONVERSÕES BEM-SUCEDIDAS: 8
CONVERSÕES FALHARAM: 0
ARQUIVOS HTML GERADOS EM: output/
TODAS AS CONVERSÕES FORAM CONCLUÍDAS COM SUCESSO!
PROCESSO COMPLETO FINALIZADO COM SUCESSO!
```

### 🔧 Conversão Individual

Para converter um artigo específico:

```bash
python scripts/format-html-seo.py articles_md/meu_artigo.md output/meu_artigo.html
```

### 🎨 Recursos SEO Incluídos

#### Meta Tags Otimizadas

- Title, Description, Keywords automáticos
- Author, Language, Robots
- Canonical URL

#### Redes Sociais

- Open Graph (Facebook, LinkedIn, WhatsApp)
- Twitter Cards
- Imagens otimizadas (1200x630px)

#### Performance

- Lazy loading para imagens
- CSS inline otimizado
- Syntax highlighting com highlight.js
- Recursos precarregados

#### Acessibilidade

- Estrutura semântica HTML5
- Alt text automático para imagens
- Navegação por teclado
- Contraste otimizado

### 🗂️ Logs Detalhados

Cada execução gera um log no formato:

```text
logs/YYYY_MM_DD_HH_MM_SS_seo_conversion.log
```

O log contém:

- Timestamp de cada operação
- Detalhes de cada conversão
- Título, descrição e keywords extraídas
- Erros com stack trace completo
- Relatório final de sucesso/falha

### ⚙️ Configurações

Edite `config/seo_config.py` para personalizar:

```python
# Configurações globais padrão
DEFAULT_CONFIG = {
    'author': 'Christian V. Mulato',
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
        'reading_time': '5 min'
    }
}
```

### 📝 Artigos de Exemplo Incluídos

O projeto inclui artigos de exemplo sobre Apache Kafka e programação:

- **[Artigo SEO Builder](articles_md/artigo-seo-builder.md)** - Sobre o próprio projeto
- **[Futuro da Programação](articles_md/futuro_programacao.md)** - IA e desenvolvimento
- **[Parte I: Fundamentos do Kafka](articles_md/parte1-fundamentos.md)** - Introdução
- **[Parte II: Java com Kafka](articles_md/parte2-java.md)** - Implementação
- **[Parte Final: Kafka Avançado](articles_md/parte-final-avancado.md)** - Produção

### 🚀 Próximos Passos

1. **Visualizar**: Abrir arquivos HTML no navegador
2. **Testar**: Verificar responsividade mobile
3. **Validar**: Usar ferramentas de SEO online
4. **Publicar**: Fazer upload para servidor web
5. **Compartilhar**: Postar nas redes sociais

### 🛠️ Requisitos

- Python 3.8+
- Dependências: `markdown`, `beautifulsoup4`, `Pygments`
- Opcional: JDK 11+ e Maven para exemplos Java

### 📈 Benefícios

✅ **Automação Total**: Uma única execução converte todos os artigos
✅ **SEO Profissional**: Meta tags, Schema.org, Open Graph
✅ **Design Moderno**: Layout responsivo e atrativo
✅ **Performance**: Otimizado para Core Web Vitals
✅ **Logs Detalhados**: Rastreamento completo de execução
✅ **Estrutura Organizada**: Apenas `start.py` na raiz
✅ **Backup Automático**: Preserva arquivos importantes

### 👨‍💻 Autor

Christian V. Mulato

- Website: [christian-mulato.dev](https://christian-mulato.dev)
- Desenvolvedor Java Sênior
- Especialista em Apache Kafka
- Cara Core Informática

### 📄 Licença

Este projeto está sob a licença MIT. Veja o arquivo [LICENSE](LICENSE) para mais detalhes.

---

**Sistema automatizado para formatação profissional de artigos Markdown em HTML responsivo com SEO otimizado.**
