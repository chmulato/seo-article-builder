/**
 * SimpleProducer
 *
 * Exemplo didático de Producer Kafka em Java para a Parte I (Fundamentos).
 * Envia uma mensagem simples para o tópico "meu-topico".
 *
 * Requisitos:
 * - Kafka rodando em localhost:9092
 * - Tópico "meu-topico" criado previamente
 */
import org.apache.kafka.clients.producer.KafkaProducer;
import org.apache.kafka.clients.producer.ProducerRecord;
import java.util.Properties;

public class SimpleProducer {
    public static void main(String[] args) {
        Properties props = new Properties();
        props.put("bootstrap.servers", "localhost:9092");
        props.put("key.serializer", "org.apache.kafka.common.serialization.StringSerializer");
        props.put("value.serializer", "org.apache.kafka.common.serialization.StringSerializer");

        try (KafkaProducer<String, String> producer = new KafkaProducer<>(props)) {
            producer.send(new ProducerRecord<>("meu-topico", "mensagem de exemplo"));
            System.out.println("Mensagem enviada!");
        }
    }
}
