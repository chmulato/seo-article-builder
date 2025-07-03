# Exercícios Práticos — Parte Final: Kafka Avançado e Produção

Estes desafios vão ajudar você a experimentar cenários reais de produção, automação, monitoramento e segurança com Apache Kafka.

## 1. Configurar um cluster Kafka com múltiplos brokers

- Utilize o arquivo `artefatos-final/docker-compose-multibroker.yml` para subir um cluster distribuído.
- Teste a criação de tópicos com diferentes fatores de replicação.
- Simule a queda de um broker e observe o failover.

## 2. Implementar monitoramento com Prometheus e Grafana

- Use os exemplos em `artefatos-final/monitoramento/` para coletar métricas do Kafka.
- Importe o dashboard de exemplo no Grafana.
- Crie um alerta para lag de consumidores.

## 3. Configurar autenticação e autorização

- Ative SSL/SASL usando os arquivos em `artefatos-final/seguranca/`.
- Defina ACLs para restringir o acesso a tópicos.
- Teste permissões criando e consumindo mensagens com diferentes usuários.

## 4. Realizar testes de backup, restauração e failover

- Utilize o script de backup em `artefatos-final/backup-e-automacao/` para exportar dados dos tópicos.
- Simule a perda de dados e restaure a partir do backup.
- Documente o procedimento realizado.

## 5. Integrar Kafka com outros sistemas usando Kafka Connect

- Configure um conector JDBC ou outro de sua escolha usando os exemplos em `artefatos-final/kafka-connect/`.
- Importe dados de um banco relacional para um tópico Kafka.
- Exporte dados do Kafka para outro sistema.

---

## Dicas Gerais

- Consulte os exemplos e scripts prontos na pasta `artefatos-final/`.
- Use o checklist de produção em `artefatos-final/boas-praticas/checklist-producao.md` para validar seu ambiente.
- Personalize os cenários conforme sua necessidade.

## Espaço para Respostas

Anote abaixo suas observações, comandos utilizados e aprendizados. Exemplo de preenchimento:

```markdown
### 1. Cluster multi-broker
- Comando: docker-compose -f docker-compose-multibroker.yml up -d
- Brokers iniciados: kafka1, kafka2, kafka3
- Testei failover desligando kafka2, cluster continuou operando

### 2. Monitoramento
- Prometheus e Grafana configurados
- Dashboard importado, métricas visíveis
- Alerta de lag criado

### 3. Segurança
- SSL/SASL ativado, ACLs aplicadas
- Usuário sem permissão bloqueado

### 4. Backup e restauração
- Backup realizado com script
- Dados restaurados com sucesso após simulação de perda

### 5. Kafka Connect
- Conector JDBC configurado
- Dados importados do banco para o tópico
- Exportação para outro sistema testada
```

---

Bons estudos e sucesso em ambientes de produção!
