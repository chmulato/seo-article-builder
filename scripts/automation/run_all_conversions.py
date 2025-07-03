#!/usr/bin/env python3
"""
run_all_conversions.py

Script para executar todas as conversões de MD para HTML com SEO.
Executa todos os scripts Python gerados pelo create_html_scripts.py
"""

import subprocess
import sys
from pathlib import Path
import time

def get_conversion_scripts():
    """Retorna lista de scripts de conversão no diretório atual."""
    # Busca por scripts Python que correspondem a arquivos MD
    scripts = []
    for md_file in Path('.').glob('*.md'):
        if md_file.name != 'README.md':
            script_file = Path(f"{md_file.stem}.py")
            if script_file.exists():
                scripts.append(script_file)
    return scripts

def run_script(script_path):
    """Executa um script Python e retorna o resultado."""
    try:
        print(f"[PROCESS] Executando {script_path.name}...")
        result = subprocess.run(
            [sys.executable, str(script_path)],
            capture_output=True,
            text=True,
            timeout=120  # Timeout de 2 minutos
        )
        
        if result.returncode == 0:
            print(f"[SUCCESS] {script_path.name} executado com sucesso!")
            return True, result.stdout
        else:
            print(f"[ERROR] Erro em {script_path.name}:")
            print(f"STDERR: {result.stderr}")
            print(f"STDOUT: {result.stdout}")
            return False, result.stderr
            
    except subprocess.TimeoutExpired:
        print(f"⏰ Timeout em {script_path.name}")
        return False, "Timeout"
    except Exception as e:
        print(f"[ERROR] Erro executando {script_path.name}: {e}")
        return False, str(e)

def main():
    """Função principal."""
    print("[INFO] Executando Todas as Conversões MD → HTML")
    print("=" * 50)
    
    # Encontra scripts de conversão
    scripts = get_conversion_scripts()
    
    if not scripts:
        print("[ERROR] Nenhum script de conversão encontrado.")
        print("💡 Execute primeiro: python create_html_scripts.py")
        return 1
    
    print(f"📁 Encontrados {len(scripts)} scripts de conversão:")
    for script in scripts:
        print(f"  • {script.name}")
    
    print(f"\n[PROCESS] Iniciando conversões...")
    
    # Executa todos os scripts
    successful = 0
    failed = 0
    start_time = time.time()
    
    for script in scripts:
        success, output = run_script(script)
        if success:
            successful += 1
        else:
            failed += 1
        print("-" * 30)
    
    # Resumo final
    end_time = time.time()
    duration = end_time - start_time
    
    print(f"\n[DATA] Resumo da Execução:")
    print(f"[SUCCESS] Sucessos: {successful}")
    print(f"[ERROR] Falhas: {failed}")
    print(f"[TIME]  Tempo total: {duration:.2f} segundos")
    
    if failed == 0:
        print(f"\n🎉 Todas as conversões foram concluídas com sucesso!")
        print(f"📁 Arquivos HTML gerados no diretório atual")
        print(f"[WEB] Todos otimizados para SEO e redes sociais")
        
        # Lista arquivos HTML gerados
        html_files = list(Path('.').glob('*.html'))
        if html_files:
            print(f"\n[CONFIG] Arquivos HTML gerados:")
            for html_file in html_files:
                print(f"  • {html_file.name}")
    else:
        print(f"\n⚠️  Algumas conversões falharam. Verifique os logs acima.")
    
    return 0 if failed == 0 else 1

if __name__ == "__main__":
    sys.exit(main())
