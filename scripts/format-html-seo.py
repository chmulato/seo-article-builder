"""
format-html-seo.py

Script universal para converter arquivos Markdown (.md) em HTML responsivo, moderno e otimizado para SEO.
Versão profissional para o sistema automatizado SEO Article Builder.

Uso:
    python format-html-seo.py <arquivo_markdown.md> [arquivo_saida.html] [--author="Nome do Autor"] [--url="https://exemplo.com"]

- Gera um HTML com layout profissional, pronto para publicação ou visualização local.
- Suporta realce de código, tabelas, imagens e links responsivos.
- Otimizado para SEO com meta tags, Open Graph e Schema.org.
- Geração automática de meta description baseada no conteúdo.
- Estrutura semântica para melhor indexação pelos motores de busca.

Requisitos:
    pip install markdown beautifulsoup4

Exemplo:
    python format-html-seo.py parte1-fundamentos.md
    python format-html-seo.py parte2-java.md parte2-java.html --author="Christian V. Mulato" --url="https://meusite.com"
"""

import markdown
from pathlib import Path
import sys
import re
import json
from datetime import datetime
from bs4 import BeautifulSoup
import argparse
import logging


def extract_meta_info(md_content, md_path):
    """Extrai informações meta do conteúdo Markdown para SEO."""
    lines = md_content.split('\n')
    
    # Busca pelo primeiro h1 como título
    title = md_path.stem.replace('-', ' ').title()
    for line in lines:
        if line.startswith('# '):
            title = line[2:].strip()
            break
    
    # Gera descrição baseada no primeiro parágrafo
    description = ""
    for line in lines:
        line = line.strip()
        if line and not line.startswith('#') and not line.startswith('*') and not line.startswith('-'):
            # Remove markdown básico
            description = re.sub(r'\*\*(.*?)\*\*', r'\1', line)
            description = re.sub(r'\*(.*?)\*', r'\1', description)
            description = re.sub(r'\[(.*?)\]\(.*?\)', r'\1', description)
            description = description[:160]  # Limita a 160 caracteres
            break
    
    # Extrai keywords baseadas nos cabeçalhos
    keywords = []
    for line in lines:
        if line.startswith('## ') or line.startswith('### '):
            keyword = line.replace('#', '').strip().lower()
            keywords.append(keyword)
    
    # Adiciona palavras-chave baseadas no nome do arquivo
    file_keywords = md_path.stem.replace('-', ' ').split()
    keywords.extend(file_keywords)
    
    return {
        'title': title,
        'description': description if description else f"Artigo sobre {title}",
        'keywords': ', '.join(list(set(keywords))[:10])  # Máximo 10 keywords únicas
    }


def generate_structured_data(meta_info, author, url, md_path):
    """Gera dados estruturados Schema.org."""
    structured_data = {
        "@context": "https://schema.org",
        "@type": "Article",
        "headline": meta_info['title'],
        "description": meta_info['description'],
        "author": {
            "@type": "Person",
            "name": author
        },
        "datePublished": datetime.now().isoformat(),
        "dateModified": datetime.now().isoformat(),
        "publisher": {
            "@type": "Organization",
            "name": author,
            "logo": {
                "@type": "ImageObject",
                "url": f"{url}/img/logo.png" if url else ""
            }
        },
        "mainEntityOfPage": {
            "@type": "WebPage",
            "@id": f"{url}/{md_path.stem}.html" if url else ""
        }
    }
    return json.dumps(structured_data, indent=2)


def generate_meta_tags(meta_info, author, url, md_path):
    """Gera tags meta para SEO."""
    canonical_url = f"{url}/{md_path.stem}.html" if url else ""
    
    meta_tags = f"""
    <!-- SEO Meta Tags -->
    <meta name="description" content="{meta_info['description']}">
    <meta name="keywords" content="{meta_info['keywords']}">
    <meta name="author" content="{author}">
    <meta name="robots" content="index, follow">
    <meta name="language" content="pt-BR">
    <meta name="revisit-after" content="7 days">
    <meta name="distribution" content="global">
    <meta name="rating" content="general">
    
    <!-- Open Graph Tags -->
    <meta property="og:title" content="{meta_info['title']}">
    <meta property="og:description" content="{meta_info['description']}">
    <meta property="og:type" content="article">
    <meta property="og:url" content="{canonical_url}">
    <meta property="og:site_name" content="{author}">
    <meta property="og:locale" content="pt_BR">
    <meta property="og:image" content="{url}/img/{md_path.stem}.png" if url else "">
    <meta property="og:image:width" content="1200">
    <meta property="og:image:height" content="630">
    
    <!-- Twitter Cards -->
    <meta name="twitter:card" content="summary_large_image">
    <meta name="twitter:title" content="{meta_info['title']}">
    <meta name="twitter:description" content="{meta_info['description']}">
    <meta name="twitter:image" content="{url}/img/{md_path.stem}.png" if url else "">
    
    <!-- Canonical URL -->
    <link rel="canonical" href="{canonical_url}">
    
    <!-- Preload Critical Resources -->
    <link rel="preload" href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&display=swap" as="style">
    <link rel="preload" href="https://cdnjs.cloudflare.com/ajax/libs/highlight.js/11.9.0/styles/github-dark.min.css" as="style">
    """
    
    return meta_tags


def convert_md_to_html(md_file, output_file=None, author="Christian V. Mulato", url="", lang="pt-BR"):
    """
    Função principal para converter Markdown para HTML com SEO otimizado.
    
    Args:
        md_file (str): Caminho para o arquivo Markdown
        output_file (str): Caminho para o arquivo HTML de saída (opcional)
        author (str): Nome do autor
        url (str): URL base do site
        lang (str): Idioma do conteúdo
    
    Returns:
        tuple: (success: bool, output_path: str, error_message: str)
    """
    try:
        md_path = Path(md_file)
        if not md_path.exists():
            return False, "", f"Arquivo markdown não encontrado: {md_path}"
        
        html_path = Path(output_file) if output_file else md_path.with_suffix('.html')
        url = url.rstrip('/') if url else ''
        
        # Lê o conteúdo do arquivo Markdown
        with md_path.open(encoding='utf-8') as f:
            md_content = f.read()
        
        # Extrai informações meta
        meta_info = extract_meta_info(md_content, md_path)
        
        # Converte Markdown para HTML
        html_body = markdown.markdown(md_content, extensions=['extra', 'toc', 'codehilite', 'tables', 'fenced_code'])
        
        # Processa o HTML para melhorar SEO
        soup = BeautifulSoup(html_body, 'html.parser')
        
        # Adiciona atributos alt às imagens sem alt
        for img in soup.find_all('img'):
            if not img.get('alt'):
                img['alt'] = f"Imagem relacionada a {meta_info['title']}"
            img['loading'] = 'lazy'  # Lazy loading para performance
        
        # Adiciona rel="noopener" para links externos
        for link in soup.find_all('a', href=True):
            if link['href'].startswith('http') and not link['href'].startswith(url):
                link['rel'] = 'noopener noreferrer'
                link['target'] = '_blank'
        
        # Adiciona estrutura semântica
        html_body = str(soup)
        
        # Gera tags meta e dados estruturados
        meta_tags = generate_meta_tags(meta_info, author, url, md_path)
        structured_data = generate_structured_data(meta_info, author, url, md_path)
        
        html_template = f"""<!DOCTYPE html>
<html lang="{lang}" itemscope itemtype="https://schema.org/Article">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <title>{meta_info['title']}</title>
    {meta_tags}
    
    <!-- Fonts -->
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&display=swap" rel="stylesheet">
    
    <!-- Syntax Highlighting -->
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/highlight.js/11.9.0/styles/github-dark.min.css">
    
    <!-- Structured Data -->
    <script type="application/ld+json">
    {structured_data}
    </script>
    
    <style>
        /* CSS Reset e Base */
        * {{ margin: 0; padding: 0; box-sizing: border-box; }}
        
        html {{ scroll-behavior: smooth; }}
        
        body {{ 
            font-family: 'Inter', 'Segoe UI', system-ui, -apple-system, sans-serif; 
            background: linear-gradient(135deg, #f5f7fa 0%, #c3cfe2 100%);
            color: #2d3748; 
            line-height: 1.7;
            margin: 0;
            padding: 0;
        }}
        
        /* Container Principal */
        .container {{ 
            max-width: 900px; 
            margin: 2rem auto; 
            background: #fff; 
            border-radius: 16px; 
            box-shadow: 0 4px 25px rgba(0,0,0,0.08);
            padding: 3rem 2.5rem;
            position: relative;
            overflow: hidden;
        }}
        
        .container::before {{
            content: '';
            position: absolute;
            top: 0;
            left: 0;
            right: 0;
            height: 4px;
            background: linear-gradient(90deg, #667eea 0%, #764ba2 100%);
        }}
        
        /* Typography */
        h1, h2, h3, h4, h5, h6 {{ 
            color: #1a202c;
            font-weight: 600;
            margin-bottom: 1rem;
            margin-top: 2rem;
        }}
        
        h1 {{ 
            font-size: 2.5rem; 
            font-weight: 700;
            margin-top: 0;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            background-clip: text;
        }}
        
        h2 {{ 
            font-size: 2rem; 
            border-bottom: 2px solid #e2e8f0;
            padding-bottom: 0.5rem;
        }}
        
        h3 {{ font-size: 1.5rem; }}
        h4 {{ font-size: 1.25rem; }}
        
        p {{ 
            margin-bottom: 1.5rem; 
            text-align: justify;
        }}
        
        /* Code Blocks */
        pre, code {{ 
            font-family: 'Fira Code', 'Consolas', 'Monaco', monospace;
        }}
        
        pre {{ 
            background: #1a202c;
            color: #e2e8f0;
            border-radius: 8px;
            padding: 1.5rem;
            overflow-x: auto;
            margin: 1.5rem 0;
            position: relative;
            box-shadow: 0 2px 10px rgba(0,0,0,0.1);
        }}
        
        code {{ 
            background: #edf2f7;
            color: #2d3748;
            padding: 0.2rem 0.4rem;
            border-radius: 4px;
            font-size: 0.9em;
        }}
        
        pre code {{ 
            background: none;
            color: inherit;
            padding: 0;
        }}
        
        /* Links */
        a {{ 
            color: #667eea;
            text-decoration: none;
            font-weight: 500;
            transition: color 0.3s ease;
        }}
        
        a:hover {{ 
            color: #764ba2;
            text-decoration: underline;
        }}
        
        /* Tables */
        table {{ 
            border-collapse: collapse; 
            width: 100%; 
            margin: 2rem 0;
            border-radius: 8px;
            overflow: hidden;
            box-shadow: 0 2px 10px rgba(0,0,0,0.1);
        }}
        
        th, td {{ 
            padding: 1rem;
            text-align: left;
            border-bottom: 1px solid #e2e8f0;
        }}
        
        th {{ 
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            color: white;
            font-weight: 600;
        }}
        
        tr:hover {{ 
            background: #f7fafc;
        }}
        
        /* Images */
        img {{ 
            max-width: 100%; 
            height: auto;
            border-radius: 8px; 
            box-shadow: 0 4px 15px rgba(0,0,0,0.1);
            margin: 1rem 0;
        }}
        
        /* Lists */
        ul, ol {{ 
            margin: 1rem 0;
            padding-left: 2rem;
        }}
        
        li {{ 
            margin: 0.5rem 0;
        }}
        
        /* Blockquotes */
        blockquote {{ 
            border-left: 4px solid #667eea;
            padding-left: 1rem;
            margin: 1.5rem 0;
            font-style: italic;
            color: #4a5568;
        }}
        
        /* Responsividade */
        @media (max-width: 768px) {{
            .container {{ 
                margin: 1rem;
                padding: 2rem 1.5rem;
                border-radius: 12px;
            }}
            
            h1 {{ font-size: 2rem; }}
            h2 {{ font-size: 1.5rem; }}
            h3 {{ font-size: 1.25rem; }}
            
            pre {{ 
                padding: 1rem;
                margin: 1rem 0;
            }}
            
            table {{ 
                font-size: 0.9rem;
            }}
            
            th, td {{ 
                padding: 0.75rem 0.5rem;
            }}
        }}
        
        @media (max-width: 480px) {{
            .container {{ 
                margin: 0.5rem;
                padding: 1.5rem 1rem;
            }}
            
            h1 {{ font-size: 1.75rem; }}
            
            pre {{ 
                padding: 0.75rem;
                font-size: 0.85rem;
            }}
        }}
        
        /* Print Styles */
        @media print {{
            body {{ 
                background: white;
                color: black;
            }}
            
            .container {{ 
                box-shadow: none;
                margin: 0;
                padding: 1rem;
            }}
            
            a {{ 
                color: black;
                text-decoration: underline;
            }}
            
            pre {{ 
                background: #f8f9fa;
                color: black;
                border: 1px solid #dee2e6;
            }}
        }}
    </style>
</head>
<body>
    <main class="container" role="main">
        <article itemscope itemtype="https://schema.org/Article">
            <meta itemprop="author" content="{author}">
            <meta itemprop="datePublished" content="{datetime.now().isoformat()}">
            <div itemprop="articleBody">
                {html_body}
            </div>
        </article>
    </main>
    
    <!-- Scripts -->
    <script src="https://cdnjs.cloudflare.com/ajax/libs/highlight.js/11.9.0/highlight.min.js"></script>
    <script>
        // Inicializa highlight.js
        hljs.highlightAll();
        
        // Adiciona smooth scrolling para links internos
        document.querySelectorAll('a[href^="#"]').forEach(anchor => {{
            anchor.addEventListener('click', function (e) {{
                e.preventDefault();
                const target = document.querySelector(this.getAttribute('href'));
                if (target) {{
                    target.scrollIntoView({{
                        behavior: 'smooth',
                        block: 'start'
                    }});
                }}
            }});
        }});
        
        // Lazy loading para imagens (fallback para navegadores antigos)
        if ('IntersectionObserver' in window) {{
            const imageObserver = new IntersectionObserver((entries, observer) => {{
                entries.forEach(entry => {{
                    if (entry.isIntersecting) {{
                        const img = entry.target;
                        if (img.dataset.src) {{
                            img.src = img.dataset.src;
                            img.removeAttribute('data-src');
                        }}
                        observer.unobserve(img);
                    }}
                }});
            }});
            
            document.querySelectorAll('img[data-src]').forEach(img => {{
                imageObserver.observe(img);
            }});
        }}
    </script>
</body>
</html>"""
        
        # Salva o arquivo HTML
        with html_path.open('w', encoding='utf-8') as f:
            f.write(html_template)
        
        logging.info(f"Arquivo HTML com SEO otimizado gerado: {html_path.resolve()}")
        logging.info(f"Título: {meta_info['title']}")
        logging.info(f"Descrição: {meta_info['description']}")
        logging.info(f"Keywords: {meta_info['keywords']}")
        logging.info(f"Autor: {author}")
        
        if url:
            logging.info(f"URL: {url}/{md_path.stem}.html")
        
        return True, str(html_path.resolve()), ""
        
    except Exception as e:
        error_msg = f"Erro ao converter {md_file}: {str(e)}"
        logging.error(error_msg)
        return False, "", error_msg


def main():
    """Função principal para uso como script independente."""
    # Configuração de argumentos
    parser = argparse.ArgumentParser(description='Converter Markdown para HTML otimizado para SEO')
    parser.add_argument('markdown_file', help='Arquivo Markdown de entrada')
    parser.add_argument('html_file', nargs='?', help='Arquivo HTML de saída (opcional)')
    parser.add_argument('--author', default='Christian V. Mulato', help='Nome do autor')
    parser.add_argument('--url', default='', help='URL base do site')
    parser.add_argument('--lang', default='pt-BR', help='Idioma do conteúdo')
    
    # Compatibilidade com modo simples
    if len(sys.argv) >= 2 and not sys.argv[1].startswith('-'):
        # Modo compatibilidade
        if len(sys.argv) < 2:
            print('Uso: python format-html-seo.py <arquivo_markdown.md> [arquivo_saida.html]')
            sys.exit(1)
        
        md_file = sys.argv[1]
        html_file = sys.argv[2] if len(sys.argv) > 2 else None
        author = 'Christian V. Mulato'
        url = ''
        lang = 'pt-BR'
    else:
        # Modo com argumentos avançados
        args = parser.parse_args()
        md_file = args.markdown_file
        html_file = args.html_file
        author = args.author
        url = args.url
        lang = args.lang
    
    # Executa conversão
    success, output_path, error_msg = convert_md_to_html(md_file, html_file, author, url, lang)
    
    if success:
        print(f"SUCCESS: Arquivo HTML gerado em: {output_path}")
    else:
        print(f"ERROR: {error_msg}")
        sys.exit(1)


if __name__ == '__main__':
    main()
