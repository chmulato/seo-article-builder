/**
 * PedidoConsumer
 *
 * Exemplo simples de consumidor Kafka em Java.
 * Consome mensagens do tópico "pedidos" e imprime no console.
 * 
 * - Grupo de consumidores: "grupo-pedidos"
 * - Deserialização de chave e valor como String
 * - Uso didático para demonstração de consumo básico com Apache Kafka
 *
 * Requisitos:
 * - Broker Kafka rodando em localhost:9092
 * - Tópico "pedidos" criado previamente
 */
package com.mulato;

import org.apache.kafka.clients.consumer.ConsumerRecord;
import org.apache.kafka.clients.consumer.ConsumerRecords;
import org.apache.kafka.clients.consumer.KafkaConsumer;
import java.time.Duration;
import java.util.Collections;
import java.util.Properties;

public class PedidoConsumer {
    public static void main(String[] args) {
        Properties props = new Properties();
        props.put("bootstrap.servers", "localhost:9092");
        props.put("group.id", "grupo-pedidos");
        props.put("key.deserializer", "org.apache.kafka.common.serialization.StringDeserializer");
        props.put("value.deserializer", "org.apache.kafka.common.serialization.StringDeserializer");

        KafkaConsumer<String, String> consumer = new KafkaConsumer<>(props);
        consumer.subscribe(Collections.singletonList("pedidos"));

        System.out.println("Aguardando pedidos...");
        while (true) {
            ConsumerRecords<String, String> records = consumer.poll(Duration.ofMillis(500));
            for (ConsumerRecord<String, String> record : records) {
                System.out.printf("Recebido: offset=%d, chave=%s, valor=%s%n", record.offset(), record.key(), record.value());
            }
        }
    }
}
