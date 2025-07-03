"""
format-html-seo.py

Módulo Python para converter arquivos Markdown em HTML com SEO otimizado.
Este módulo é chamado por outros scripts Python para automatizar a conversão.

Uso como módulo:
    from format_html_seo import convert_md_to_html
    
    convert_md_to_html(
        md_file="arquivo.md",
        html_file="arquivo.html",
        author="Nome do Autor",
        url="https://site.com",
        custom_meta={}
    )

Uso como script:
    python format-html-seo.py arquivo.md [saida.html] [--author="Nome"] [--url="https://site.com"]
"""

import markdown
from pathlib import Path
import sys
import re
import json
import shutil
from datetime import datetime
from bs4 import BeautifulSoup
import argparse
from typing import Dict, Optional, List


class MarkdownToHtmlSEO:
    """Classe para converter Markdown em HTML com SEO otimizado."""
    
    def __init__(self, author: str = "Christian V. Mulato", base_url: str = "", language: str = "pt-BR"):
        self.author = author
        self.base_url = base_url.rstrip('/')
        self.language = language
        self.meta_info = {}
        
    def extract_meta_info(self, md_content: str, md_path: Path) -> Dict[str, str]:
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
        
        # Extrai autor do conteúdo se disponível
        author = self.author
        for line in lines:
            if 'por:' in line.lower() or 'author:' in line.lower() or 'autor:' in line.lower():
                author_match = re.search(r'(?:por|author|autor):\s*(.+)', line, re.IGNORECASE)
                if author_match:
                    author = author_match.group(1).strip()
                    break
        
        self.meta_info = {
            'title': title,
            'description': description if description else f"Artigo sobre {title}",
            'keywords': ', '.join(list(set(keywords))[:10]),  # Máximo 10 keywords únicas
            'author': author,
            'date': datetime.now().isoformat(),
            'slug': md_path.stem
        }
        
        return self.meta_info

    def generate_structured_data(self, meta_info: Dict[str, str]) -> str:
        """Gera dados estruturados Schema.org."""
        canonical_url = f"{self.base_url}/{meta_info['slug']}.html" if self.base_url else ""
        
        structured_data = {
            "@context": "https://schema.org",
            "@type": "Article",
            "headline": meta_info['title'],
            "description": meta_info['description'],
            "author": {
                "@type": "Person",
                "name": meta_info['author']
            },
            "datePublished": meta_info['date'],
            "dateModified": meta_info['date'],
            "publisher": {
                "@type": "Organization",
                "name": meta_info['author'],
                "logo": {
                    "@type": "ImageObject",
                    "url": f"{self.base_url}/img/logo.png" if self.base_url else ""
                }
            },
            "mainEntityOfPage": {
                "@type": "WebPage",
                "@id": canonical_url
            },
            "image": f"{self.base_url}/img/{meta_info['slug']}.png" if self.base_url else "",
            "wordCount": len(meta_info.get('content', '').split()),
            "articleSection": "Technology",
            "inLanguage": self.language
        }
        return json.dumps(structured_data, indent=2, ensure_ascii=False)

    def generate_meta_tags(self, meta_info: Dict[str, str]) -> str:
        """Gera tags meta para SEO."""
        canonical_url = f"{self.base_url}/{meta_info['slug']}.html" if self.base_url else ""
        image_url = f"{self.base_url}/img/{meta_info['slug']}.png" if self.base_url else ""
        
        meta_tags = f"""
    <!-- SEO Meta Tags -->
    <meta name="description" content="{meta_info['description']}">
    <meta name="keywords" content="{meta_info['keywords']}">
    <meta name="author" content="{meta_info['author']}">
    <meta name="robots" content="index, follow">
    <meta name="language" content="{self.language}">
    <meta name="revisit-after" content="7 days">
    <meta name="distribution" content="global">
    <meta name="rating" content="general">
    
    <!-- Open Graph Tags -->
    <meta property="og:title" content="{meta_info['title']}">
    <meta property="og:description" content="{meta_info['description']}">
    <meta property="og:type" content="article">
    <meta property="og:url" content="{canonical_url}">
    <meta property="og:site_name" content="{meta_info['author']}">
    <meta property="og:locale" content="{self.language.replace('-', '_')}">
    <meta property="og:image" content="{image_url}">
    <meta property="og:image:width" content="1200">
    <meta property="og:image:height" content="630">
    <meta property="article:author" content="{meta_info['author']}">
    <meta property="article:published_time" content="{meta_info['date']}">
    
    <!-- Twitter Cards -->
    <meta name="twitter:card" content="summary_large_image">
    <meta name="twitter:title" content="{meta_info['title']}">
    <meta name="twitter:description" content="{meta_info['description']}">
    <meta name="twitter:image" content="{image_url}">
    <meta name="twitter:creator" content="@{meta_info['author'].replace(' ', '').lower()}">
    
    <!-- Additional Meta Tags -->
    <meta name="theme-color" content="#667eea">
    <meta name="msapplication-navbutton-color" content="#667eea">
    <meta name="apple-mobile-web-app-status-bar-style" content="#667eea">"""
        
        if canonical_url:
            meta_tags += f'\n    <link rel="canonical" href="{canonical_url}">'
            
        return meta_tags

    def process_html_content(self, html_content: str) -> str:
        """Processa o HTML para melhorar SEO e acessibilidade."""
        soup = BeautifulSoup(html_content, 'html.parser')
        
        # Adiciona atributos alt às imagens sem alt
        for img in soup.find_all('img'):
            if not img.get('alt'):
                img['alt'] = f"Imagem relacionada a {self.meta_info['title']}"
            img['loading'] = 'lazy'  # Lazy loading para performance
            
        # Adiciona rel="noopener" para links externos
        for link in soup.find_all('a', href=True):
            if link['href'].startswith('http') and not link['href'].startswith(self.base_url):
                link['rel'] = 'noopener noreferrer'
                link['target'] = '_blank'
        
        # Adiciona IDs aos cabeçalhos para navegação
        for heading in soup.find_all(['h1', 'h2', 'h3', 'h4', 'h5', 'h6']):
            if not heading.get('id'):
                heading_text = heading.get_text().lower()
                heading_id = re.sub(r'[^a-z0-9\s-]', '', heading_text)
                heading_id = re.sub(r'\s+', '-', heading_id.strip())
                heading['id'] = heading_id
                
        return str(soup)

    def generate_html_template(self, meta_info: Dict[str, str], html_body: str, structured_data: str, meta_tags: str) -> str:
        """Gera o template HTML completo."""
        return f"""<!DOCTYPE html>
<html lang="{self.language}" itemscope itemtype="https://schema.org/Article">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <title>{meta_info['title']}</title>
    {meta_tags}
    
    <!-- Preload Critical Resources -->
    <link rel="preload" href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&display=swap" as="style">
    <link rel="preload" href="https://cdnjs.cloudflare.com/ajax/libs/highlight.js/11.9.0/styles/github-dark.min.css" as="style">
    
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
            <meta itemprop="author" content="{meta_info['author']}">
            <meta itemprop="datePublished" content="{meta_info['date']}">
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
        
        // Adiciona botão "Voltar ao topo"
        const backToTopBtn = document.createElement('button');
        backToTopBtn.innerHTML = '↑';
        backToTopBtn.style.cssText = `
            position: fixed;
            bottom: 20px;
            right: 20px;
            background: #667eea;
            color: white;
            border: none;
            border-radius: 50%;
            width: 50px;
            height: 50px;
            font-size: 20px;
            cursor: pointer;
            box-shadow: 0 2px 10px rgba(0,0,0,0.2);
            transition: all 0.3s ease;
            opacity: 0;
            visibility: hidden;
        `;
        document.body.appendChild(backToTopBtn);
        
        window.addEventListener('scroll', () => {{
            if (window.scrollY > 300) {{
                backToTopBtn.style.opacity = '1';
                backToTopBtn.style.visibility = 'visible';
            }} else {{
                backToTopBtn.style.opacity = '0';
                backToTopBtn.style.visibility = 'hidden';
            }}
        }});
        
        backToTopBtn.addEventListener('click', () => {{
            window.scrollTo({{ top: 0, behavior: 'smooth' }});
        }});
    </script>
</body>
</html>"""

    def convert_md_to_html(self, md_file: str, html_file: Optional[str] = None, custom_meta: Optional[Dict] = None) -> str:
        """Converte arquivo Markdown para HTML com SEO otimizado."""
        md_path = Path(md_file)
        if not md_path.exists():
            raise FileNotFoundError(f'Arquivo markdown não encontrado: {md_path}')
        
        # Define arquivo de saída
        if html_file:
            html_path = Path(html_file)
        else:
            html_path = md_path.with_suffix('.html')
        
        # Lê o conteúdo do arquivo Markdown
        with md_path.open(encoding='utf-8') as f:
            md_content = f.read()
        
        # Extrai informações meta
        meta_info = self.extract_meta_info(md_content, md_path)
        
        # Aplica meta customizadas se fornecidas
        if custom_meta:
            meta_info.update(custom_meta)
        
        # Converte Markdown para HTML
        html_body = markdown.markdown(
            md_content, 
            extensions=['extra', 'toc', 'codehilite', 'tables', 'fenced_code', 'footnotes']
        )
        
        # Processa o HTML para melhorar SEO
        html_body = self.process_html_content(html_body)
        
        # Processa caminhos das imagens
        html_body = self.process_image_paths(html_body)
        
        # Copia imagens para pasta de saída
        self.copy_images(str(md_path), str(html_path))
        
        # Gera componentes SEO
        structured_data = self.generate_structured_data(meta_info)
        meta_tags = self.generate_meta_tags(meta_info)
        
        # Gera HTML final
        html_template = self.generate_html_template(meta_info, html_body, structured_data, meta_tags)
        
        # Salva o arquivo HTML
        with html_path.open('w', encoding='utf-8') as f:
            f.write(html_template)
        
        # Copia imagens se existirem
        self.copy_images(md_file, html_file)
        
        return str(html_path.resolve())

    def copy_images(self, md_file: str, html_file: str) -> None:
        """Copia imagens de articles_md/images/ para output/images/."""
        md_path = Path(md_file)
        html_path = Path(html_file)
        
        # Pastas de origem e destino das imagens
        source_images_dir = md_path.parent / "images"
        dest_images_dir = html_path.parent / "images"
        
        # Verifica se existe pasta de imagens na origem
        if source_images_dir.exists() and source_images_dir.is_dir():
            # Cria pasta de destino se não existir
            dest_images_dir.mkdir(parents=True, exist_ok=True)
            
            # Copia todas as imagens (somente se não existir ou for mais recente)
            for image_file in source_images_dir.glob("*"):
                if image_file.is_file():
                    dest_file = dest_images_dir / image_file.name
                    
                    # Verifica se precisa copiar
                    if not dest_file.exists() or image_file.stat().st_mtime > dest_file.stat().st_mtime:
                        shutil.copy2(image_file, dest_file)
                        print(f'[IMAGE] Copiada: {image_file.name} → {dest_file}')
                    else:
                        print(f'[IMAGE] Skipped: {image_file.name} (já existe)')
    
    def process_image_paths(self, html_content: str) -> str:
        """Processa caminhos das imagens no HTML para apontar para output/images/."""
        # Substitui referencias de images/ por images/ (já está correto)
        # Substitui referencias de articles_md/images/ por images/
        html_content = re.sub(r'src="articles_md/images/', 'src="images/', html_content)
        html_content = re.sub(r'src="\.\.\/articles_md\/images\/', 'src="images/', html_content)
        
        # Substitui referencias de /assets/images/ por images/
        html_content = re.sub(r'src="/assets/images/', 'src="images/', html_content)
        html_content = re.sub(r'src="assets/images/', 'src="images/', html_content)
        
        return html_content


def convert_md_to_html(md_file: str, html_file: Optional[str] = None, 
                       author: str = "Christian V. Mulato", url: str = "", 
                       custom_meta: Optional[Dict] = None) -> str:
    """Função de conveniência para converter MD para HTML com SEO."""
    converter = MarkdownToHtmlSEO(author=author, base_url=url)
    return converter.convert_md_to_html(md_file, html_file, custom_meta)


def main():
    """Função principal para uso como script."""
    parser = argparse.ArgumentParser(description='Converter Markdown para HTML otimizado para SEO')
    parser.add_argument('markdown_file', help='Arquivo Markdown de entrada')
    parser.add_argument('html_file', nargs='?', help='Arquivo HTML de saída (opcional)')
    parser.add_argument('--author', default='Christian V. Mulato', help='Nome do autor')
    parser.add_argument('--url', default='', help='URL base do site')
    parser.add_argument('--lang', default='pt-BR', help='Idioma do conteúdo')
    
    args = parser.parse_args()
    
    try:
        converter = MarkdownToHtmlSEO(author=args.author, base_url=args.url, language=args.lang)
        output_file = converter.convert_md_to_html(args.markdown_file, args.html_file)
        
        print('[OK] Arquivo HTML com SEO otimizado gerado em: ' + output_file)
        print('[INFO] Titulo: ' + converter.meta_info["title"])
        print('[INFO] Descricao: ' + converter.meta_info["description"])
        print('[INFO] Keywords: ' + converter.meta_info["keywords"])
        print('[INFO] Autor: ' + converter.meta_info["author"])
        if args.url:
            print('[INFO] URL: ' + args.url + '/' + converter.meta_info["slug"] + '.html')
            
    except Exception as e:
        print('[ERROR] Erro: ' + str(e))
        return 1
    
    return 0


if __name__ == "__main__":
    sys.exit(main())
