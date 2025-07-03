#!/bin/bash
# Script para backup da lista de tópicos Kafka

# Lista todos os tópicos e salva em um arquivo
kafka-topics --bootstrap-server localhost:9092 --list > topicos-backup.txt

echo "Backup dos tópicos realizado em topicos-backup.txt"