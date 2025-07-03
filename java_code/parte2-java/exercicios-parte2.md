# Exercícios Práticos — Parte II: Java com Apache Kafka

Estes exercícios vão ajudar você a fixar os conceitos de integração entre Java e Kafka, praticando desde a configuração do ambiente até a implementação de Producers e Consumers.

## 1. Crie um novo projeto Java com Maven

- Utilize o `pom.xml` de exemplo disponível em `artefatos-exercicios-parte2/pom.xml`.
- Garanta que a dependência `org.apache.kafka:kafka-clients` está presente.

## 2. Implemente um Producer que envia mensagens simulando pedidos

- Crie uma classe `ExemploProducer.java`.
- O Producer deve enviar mensagens para um tópico chamado `pedidos`.
- Cada mensagem pode ser um texto simples, como "Pedido #1", "Pedido #2", etc.
- Dica: Use o esqueleto disponível em `artefatos-exercicios-parte2/ExemploProducer.java`.

## 3. Implemente um Consumer que lê e imprime os pedidos

- Crie uma classe `ExemploConsumer.java`.
- O Consumer deve se inscrever no tópico `pedidos` e imprimir cada mensagem recebida.
- Dica: Use o esqueleto disponível em `artefatos-exercicios-parte2/ExemploConsumer.java`.

## 4. Experimente com Consumer Groups e múltiplas partições

- Altere o número de partições do tópico `pedidos` para 2 ou mais.
- Rode múltiplas instâncias do Consumer (em terminais diferentes) usando o mesmo `group.id`.
- Observe como o Kafka distribui as mensagens entre os Consumers.

## 5. (Opcional) Adicione testes automatizados

- Implemente um teste de integração semelhante ao `KafkaIntegrationTest.java` do projeto principal.
- Valide se o Producer envia e o Consumer consome corretamente.

---

## Dicas Gerais

- Use o `docker-compose.yml` da pasta `parte2-java/` para subir o ambiente Kafka local.
- Consulte a documentação oficial do Kafka para detalhes de configuração.
- Personalize as mensagens, tópicos e lógica conforme desejar.

## Espaço para Respostas

Anote abaixo suas observações, comandos utilizados e aprendizados:

Bons estudos!
