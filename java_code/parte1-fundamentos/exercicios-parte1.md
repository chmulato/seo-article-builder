# Exercícios Práticos — Parte I: Fundamentos do Apache Kafka

Estes exercícios vão ajudar você a praticar os conceitos essenciais do Apache Kafka, desde a instalação até o uso dos principais comandos e a experimentação com tópicos, producers e consumers.

## 1. Suba o ambiente Kafka localmente

- Utilize o `docker-compose.yml` da pasta `parte1-fundamentos/`.
- Comando:

  ```sh
  docker-compose up -d
  ```

## 2. Crie tópicos com diferentes números de partições

- Crie um tópico chamado `meu-topico` com 3 partições:

  ```sh
  docker exec -it <nome_do_container_kafka> kafka-topics --bootstrap-server localhost:9092 --create --topic meu-topico --partitions 3 --replication-factor 1
  ```

- Liste os tópicos existentes:

  ```sh
  docker exec -it <nome_do_container_kafka> kafka-topics --bootstrap-server localhost:9092 --list
  ```

## 3. Produza e consuma mensagens usando o terminal

- Produza mensagens:

  ```sh
  docker exec -it <nome_do_container_kafka> kafka-console-producer --topic meu-topico --bootstrap-server localhost:9092
  ```

- Consuma mensagens:

  ```sh
  docker exec -it <nome_do_container_kafka> kafka-console-consumer --topic meu-topico --from-beginning --bootstrap-server localhost:9092
  ```

## 4. Experimente criar múltiplos consumidores em um mesmo grupo

- Abra dois terminais e execute o consumer em ambos, usando o mesmo `--group`:

  ```sh
  docker exec -it <nome_do_container_kafka> kafka-console-consumer --topic meu-topico --group grupo-exemplo --bootstrap-server localhost:9092
  ```

- Envie mensagens e observe como o Kafka distribui entre os consumidores.

## 5. (Opcional) Experimente os exemplos Java

- Compile e execute os exemplos `SimpleProducer` e `SimpleConsumer` conforme instruções na Parte I.

---

## Dicas Gerais

- Use `docker ps` para descobrir o nome do container Kafka.
- Consulte a documentação oficial do Kafka para mais comandos e opções.
- Personalize os nomes dos tópicos, grupos e mensagens conforme desejar.

## Espaço para Respostas

Anote abaixo suas observações, comandos utilizados e aprendizados. Exemplo de preenchimento:

```markdown
### 1. Ambiente Kafka iniciado com sucesso
- Comando: docker-compose up -d

### 2. Tópico criado
- Comando: kafka-topics --create ...
- Tópicos listados: meu-topico

### 3. Mensagens produzidas e consumidas
- Produzi: "Primeira mensagem"
- Consumi: "Primeira mensagem"

### 4. Teste com múltiplos consumidores
- Abri 2 terminais, ambos consumindo do mesmo grupo
- Kafka distribuiu as mensagens entre eles

### 5. Teste Java
- Compilei e executei SimpleProducer/SimpleConsumer
- Mensagens enviadas e recebidas com sucesso
```

Bons estudos!
