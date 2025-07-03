/**
 * PedidoProducer
 *
 * Exemplo simples de producer Kafka em Java.
 * Envia mensagens simulando pedidos para o tópico "pedidos".
 * 
 * - Serialização de chave e valor como String
 * - Uso didático para demonstração de envio básico com Apache Kafka
 *
 * Requisitos:
 * - Broker Kafka rodando em localhost:9092
 * - Tópico "pedidos" criado previamente
 */
package com.mulato;

import org.apache.kafka.clients.producer.KafkaProducer;
import org.apache.kafka.clients.producer.ProducerRecord;
import java.util.Properties;

public class PedidoProducer {
    public static void main(String[] args) {
        Properties props = new Properties();
        props.put("bootstrap.servers", "localhost:9092");
        props.put("key.serializer", "org.apache.kafka.common.serialization.StringSerializer");
        props.put("value.serializer", "org.apache.kafka.common.serialization.StringSerializer");

        KafkaProducer<String, String> producer = new KafkaProducer<>(props);

        for (int i = 1; i <= 5; i++) {
            String pedido = "Pedido #" + i;
            producer.send(new ProducerRecord<>("pedidos", Integer.toString(i), pedido));
            System.out.println("Enviado: " + pedido);
        }

        producer.close();
    }
}
