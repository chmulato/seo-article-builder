# Exemplo de Artigo com Imagens

Este é um exemplo de como usar o sistema de conversão com imagens.

## Como Usar Imagens

### 1. Colocar Imagens na Pasta Correta

Coloque suas imagens em `articles_md/images/`:

- `articles_md/images/diagrama.png`
- `articles_md/images/screenshot.jpg`
- `articles_md/images/logo.svg`

### 2. Referenciar Imagens no Markdown

Use as seguintes sintaxes:

```markdown
![Descrição da imagem](images/diagrama.png)
![Screenshot](images/screenshot.jpg)
![Logo](images/logo.svg)
```

Ou se você preferir paths absolutos:

```markdown
![Descrição da imagem](/assets/images/diagrama.png)
![Screenshot](/assets/images/screenshot.jpg)
![Logo](/assets/images/logo.svg)
```

### 3. Resultado Após Conversão

- As imagens serão automaticamente copiadas para `output/images/`
- Os paths no HTML serão ajustados para `src="images/nome_da_imagem.ext"`
- Lazy loading será aplicado automaticamente
- Alt text será preservado para acessibilidade

## Exemplo de Imagem

![Desenvolvimento de Software](images/software.png)

Esta imagem será automaticamente copiada e referenciada corretamente no HTML final.

## Tipos de Imagem Suportados

- PNG
- JPG/JPEG
- SVG
- GIF
- WebP

## Otimizações Automáticas

1. **Lazy Loading**: Carregamento sob demanda
2. **Alt Text**: Preservação para acessibilidade
3. **Responsive**: Adapta ao tamanho da tela
4. **Performance**: Otimizações de carregamento

---

**Sistema SEO Article Builder** - Conversão inteligente de MD para HTML com gestão automática de imagens.
