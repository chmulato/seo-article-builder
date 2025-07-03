#!/usr/bin/env python3
"""
start.py

Sistema automatizado de conversão MD→HTML com SEO otimizado
Cara Core Informática - www.caracore.com.br
"""

import sys
import os
import shutil
import logging
from datetime import datetime
from pathlib import Path

# Adiciona a pasta scripts ao path
scripts_path = Path(__file__).parent / "scripts"
sys.path.insert(0, str(scripts_path))

def setup_logging():
    """Configura o sistema de logging."""
    # Cria pasta de logs se não existir
    log_dir = Path("logs")
    log_dir.mkdir(exist_ok=True)
    
    # Nome do arquivo de log com timestamp
    timestamp = datetime.now().strftime("%Y_%m_%d_%H_%M_%S")
    log_file = log_dir / f"{timestamp}_seo_conversion.log"
    
    # Configura o logging
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s - %(levelname)s - %(message)s',
        handlers=[
            logging.FileHandler(log_file, encoding='utf-8'),
            logging.StreamHandler(sys.stdout)
        ]
    )
    
    return log_file

def get_articles_list():
    """Retorna lista de artigos .md na pasta articles_md."""
    articles_dir = Path("articles_md")
    
    if not articles_dir.exists():
        logging.error(f"Pasta {articles_dir} não encontrada!")
        return []
    
    md_files = list(articles_dir.glob("*.md"))
    logging.info(f"Encontrados {len(md_files)} arquivo(s) .md na pasta articles_md/")
    
    for md_file in md_files:
        logging.info(f"  • {md_file.name}")
    
    return md_files

def convert_single_article(md_file):
    """Converte um artigo específico."""
    try:
        logging.info(f"Iniciando conversão de {md_file.name}")
        
        input_file = f"articles_md/{md_file.name}"
        output_file = f"output/{md_file.stem}.html"
        
        logging.info(f"Arquivo de entrada: {input_file}")
        logging.info(f"Arquivo de saída: {output_file}")
        
        # Importa o módulo de conversão
        import importlib.util
        spec = importlib.util.spec_from_file_location("format_html_seo", "scripts/format-html-seo.py")
        format_html_seo = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(format_html_seo)
        
        # Chama a função de conversão
        success, output_path, error_msg = format_html_seo.convert_md_to_html(input_file, output_file)
        
        if success:
            logging.info(f"CONVERSÃO CONCLUÍDA: {md_file.name} → {output_path}")
            return True
        else:
            logging.error(f"FALHA NA CONVERSÃO: {md_file.name} - {error_msg}")
            return False
            
    except ImportError as e:
        logging.error(f"ERRO DE IMPORTAÇÃO ao converter {md_file.name}: {e}")
        return False
    except Exception as e:
        logging.error(f"ERRO INESPERADO ao converter {md_file.name}: {e}")
        return False

def ensure_output_directory():
    """Garante que a pasta de saída existe."""
    output_dir = Path("output")
    output_dir.mkdir(exist_ok=True)
    
    # Cria subpasta de imagens se não existir
    images_dir = output_dir / "images"
    images_dir.mkdir(exist_ok=True)
    
    logging.info(f"Pasta de saída preparada: {output_dir}")

def cleanup_root_md_files():
    """Move arquivos .md da raiz para backup (mantém apenas README.md)."""
    try:
        root_path = Path(".")
        backup_path = Path("backup_removed_files")
        
        # Cria pasta de backup se não existir
        backup_path.mkdir(exist_ok=True)
        
        # Encontra arquivos .md na raiz (excluindo README.md)
        md_files = []
        for md_file in root_path.glob("*.md"):
            if md_file.name.upper() == "README.MD":
                continue
            md_files.append(md_file)
        
        if not md_files:
            logging.info("LIMPEZA: Nenhum arquivo .md encontrado na raiz para limpar")
            return True
        
        logging.info(f"LIMPEZA: Encontrados {len(md_files)} arquivo(s) .md na raiz:")
        for md_file in md_files:
            logging.info(f"  • {md_file.name}")
        
        # Move os arquivos
        moved_count = 0
        for md_file in md_files:
            try:
                destination = backup_path / md_file.name
                
                # Se arquivo já existe no backup, adiciona timestamp
                if destination.exists():
                    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
                    name_part = md_file.stem
                    ext_part = md_file.suffix
                    destination = backup_path / f"{name_part}_{timestamp}{ext_part}"
                
                shutil.move(str(md_file), str(destination))
                logging.info(f"MOVIDO: {md_file.name} → {destination}")
                moved_count += 1
                
            except Exception as e:
                logging.error(f"ERRO ao mover {md_file.name}: {e}")
        
        logging.info(f"LIMPEZA CONCLUÍDA: {moved_count} arquivo(s) movido(s)")
        return True
        
    except Exception as e:
        logging.error(f"ERRO na limpeza de arquivos .md: {e}")
        return False

def main():
    """Função principal - execução automatizada."""
    
    # Configura logging
    log_file = setup_logging()
    
    logging.info("SEO Article Builder - Conversão Automatizada")
    logging.info("=" * 60)
    logging.info("Cara Core Informática - www.caracore.com.br")
    logging.info(f"Log salvo em: {log_file}")
    logging.info("=" * 60)
    
    try:
        # Verifica e prepara ambiente
        logging.info("PREPARANDO AMBIENTE...")
        ensure_output_directory()
        
        # Busca artigos para conversão
        logging.info("BUSCANDO ARTIGOS PARA CONVERSÃO...")
        md_files = get_articles_list()
        
        if not md_files:
            logging.error("ERRO: Nenhum arquivo .md encontrado na pasta articles_md/")
            logging.error("EXECUÇÃO INTERROMPIDA - nada para converter")
            sys.exit(1)
        
        # Inicia conversões
        logging.info("INICIANDO CONVERSÕES...")
        success_count = 0
        error_count = 0
        
        for md_file in md_files:
            logging.info("-" * 50)
            
            success = convert_single_article(md_file)
            
            if success:
                success_count += 1
            else:
                error_count += 1
                logging.error(f"FALHA CRÍTICA na conversão de {md_file.name}")
                logging.error("EXECUÇÃO INTERROMPIDA devido a erro")
                sys.exit(1)
        
        # Relatório final
        logging.info("=" * 60)
        logging.info("RELATÓRIO FINAL")
        logging.info(f"CONVERSÕES BEM-SUCEDIDAS: {success_count}")
        logging.info(f"CONVERSÕES FALHARAM: {error_count}")
        logging.info(f"ARQUIVOS HTML GERADOS EM: output/")
        
        if success_count > 0:
            logging.info("TODAS AS CONVERSÕES FORAM CONCLUÍDAS COM SUCESSO!")
            
            # Executa limpeza automática
            logging.info("EXECUTANDO LIMPEZA AUTOMÁTICA...")
            cleanup_root_md_files()
            
            logging.info("PROCESSO COMPLETO FINALIZADO COM SUCESSO!")
        else:
            logging.error("ERRO: Nenhuma conversão foi bem-sucedida")
            sys.exit(1)
            
    except KeyboardInterrupt:
        logging.error("EXECUÇÃO INTERROMPIDA pelo usuário")
        sys.exit(1)
    except Exception as e:
        logging.error(f"ERRO CRÍTICO INESPERADO: {e}")
        logging.error("EXECUÇÃO INTERROMPIDA")
        sys.exit(1)

if __name__ == "__main__":
    main()
