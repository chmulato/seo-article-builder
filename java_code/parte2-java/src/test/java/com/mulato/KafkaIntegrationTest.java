package com.mulato;
/**
 * KafkaIntegrationTest
 *
 * Teste de integração real entre Producer e Consumer usando um broker Kafka rodando em localhost:9092.
 *
 * Instruções para execução:
 * 1. Abra um terminal na pasta parte2-java.
 * 2. Suba o ambiente Kafka e Zookeeper com: docker-compose up -d
 * 3. Certifique-se de que o tópico "pedidos" existe. Se necessário, crie-o:
 *    docker exec -it <nome_do_container_kafka> kafka-topics --bootstrap-server localhost:9092 --create --topic pedidos --partitions 1 --replication-factor 1
 *    (Use `docker ps` para descobrir o nome do container Kafka.)
 * 4. Execute este teste com Maven: mvn test
 * 5. Ao terminar, pare os containers: docker-compose down
 *
 * O teste envia uma mensagem para o tópico e verifica se ela é consumida corretamente.
 */
import org.apache.kafka.clients.consumer.*;
import org.apache.kafka.clients.producer.*;
import org.apache.kafka.common.serialization.StringDeserializer;
import org.apache.kafka.common.serialization.StringSerializer;
import org.junit.jupiter.api.*;

import java.time.Duration;
import java.util.*;

import static org.junit.jupiter.api.Assertions.*;

class KafkaIntegrationTest {

    private static final String TOPIC = "pedidos";
    private static final String BOOTSTRAP_SERVERS = "localhost:9092";

    @Test
    void producerAndConsumerIntegration() {
        // Producer envia mensagem
        Properties producerProps = new Properties();
        producerProps.put(ProducerConfig.BOOTSTRAP_SERVERS_CONFIG, BOOTSTRAP_SERVERS);
        producerProps.put(ProducerConfig.KEY_SERIALIZER_CLASS_CONFIG, StringSerializer.class.getName());
        producerProps.put(ProducerConfig.VALUE_SERIALIZER_CLASS_CONFIG, StringSerializer.class.getName());
        try (KafkaProducer<String, String> producer = new KafkaProducer<>(producerProps)) {
            producer.send(new ProducerRecord<>(TOPIC, "1", "Pedido #1"));
            producer.flush();
        }

        // Consumer lê mensagem
        Properties consumerProps = new Properties();
        consumerProps.put(ConsumerConfig.BOOTSTRAP_SERVERS_CONFIG, BOOTSTRAP_SERVERS);
        consumerProps.put(ConsumerConfig.GROUP_ID_CONFIG, "test-group");
        consumerProps.put(ConsumerConfig.KEY_DESERIALIZER_CLASS_CONFIG, StringDeserializer.class.getName());
        consumerProps.put(ConsumerConfig.VALUE_DESERIALIZER_CLASS_CONFIG, StringDeserializer.class.getName());
        consumerProps.put(ConsumerConfig.AUTO_OFFSET_RESET_CONFIG, "earliest");

        try (KafkaConsumer<String, String> consumer = new KafkaConsumer<>(consumerProps)) {
            consumer.subscribe(Collections.singletonList(TOPIC));
            boolean found = false;
            long end = System.currentTimeMillis() + 5000; // espera até 5s
            while (System.currentTimeMillis() < end && !found) {
                ConsumerRecords<String, String> records = consumer.poll(Duration.ofMillis(500));
                for (ConsumerRecord<String, String> record : records) {
                    if ("Pedido #1".equals(record.value())) {
                        found = true;
                        break;
                    }
                }
            }
            assertTrue(found, "Mensagem não encontrada no tópico!");
        }
    }
}