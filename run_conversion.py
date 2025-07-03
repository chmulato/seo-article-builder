#!/usr/bin/env python3
"""
run_conversion.py

Script facilitador para executar conversões de artigos.
Permite executar scripts de conversão sem precisar navegar até a pasta.
"""

import subprocess
import sys
import os
from pathlib import Path

def print_header(title):
    """Imprime cabeçalho formatado."""
    print(f"\n🚀 {title}")
    print("=" * 50)

def run_script(script_path):
    """Executa um script de conversão."""
    try:
        result = subprocess.run([sys.executable, script_path], 
                              capture_output=False, 
                              text=True, 
                              cwd=Path.cwd())
        return result.returncode == 0
    except Exception as e:
        print(f"❌ Erro ao executar {script_path}: {e}")
        return False

def main():
    """Menu para executar conversões."""
    print_header("Conversor de Artigos Apache Kafka")
    print("Selecione qual artigo converter:")
    print()
    
    # Opções disponíveis
    options = {
        '1': ('scripts/conversion/futuro_programacao.py', 'Futuro da Programação com IA'),
        '2': ('scripts/conversion/parte1-fundamentos.py', 'Parte I: Fundamentos do Kafka'),
        '3': ('scripts/conversion/parte2-java.py', 'Parte II: Java com Kafka'),
        '4': ('scripts/conversion/parte-final-avancado.py', 'Parte Final: Kafka Avançado'),
        '5': ('scripts/automation/run_all_conversions.py', 'Converter TODOS os artigos'),
        '6': ('scripts/demo/demo_simples.py', 'Demonstração do sistema')
    }
    
    for key, (script, title) in options.items():
        print(f"  {key}. {title}")
    
    print()
    choice = input("Digite sua opção (1-6) ou 'q' para sair: ").strip()
    
    if choice.lower() == 'q':
        print("👋 Até logo!")
        return
    
    if choice in options:
        script_path, title = options[choice]
        print(f"\n📝 Executando: {title}")
        print("-" * 40)
        
        if run_script(script_path):
            print(f"\n✅ {title} executado com sucesso!")
        else:
            print(f"\n❌ Erro ao executar {title}")
    else:
        print("❌ Opção inválida!")

if __name__ == "__main__":
    main()
