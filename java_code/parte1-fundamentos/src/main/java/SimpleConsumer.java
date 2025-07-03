/**
 * SimpleConsumer
 *
 * Exemplo didático de Consumer Kafka em Java para a Parte I (Fundamentos).
 * Consome mensagens do tópico "meu-topico" e imprime no console.
 *
 * Requisitos:
 * - Kafka rodando em localhost:9092
 * - Tópico "meu-topico" criado previamente
 */
import org.apache.kafka.clients.consumer.ConsumerRecords;
import org.apache.kafka.clients.consumer.KafkaConsumer;
import org.apache.kafka.clients.consumer.ConsumerRecord;
import java.util.Collections;
import java.util.Properties;

public class SimpleConsumer {
    public static void main(String[] args) {
        Properties props = new Properties();
        props.put("bootstrap.servers", "localhost:9092");
        props.put("group.id", "grupo-exemplo");
        props.put("key.deserializer", "org.apache.kafka.common.serialization.StringDeserializer");
        props.put("value.deserializer", "org.apache.kafka.common.serialization.StringDeserializer");

        try (KafkaConsumer<String, String> consumer = new KafkaConsumer<>(props)) {
            consumer.subscribe(Collections.singletonList("meu-topico"));
            ConsumerRecords<String, String> records = consumer.poll(java.time.Duration.ofSeconds(5));
            for (ConsumerRecord<String, String> record : records) {
                System.out.printf("Recebido: %s%n", record.value());
            }
        }
    }
}
