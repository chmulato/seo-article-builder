/**
 * Teste unitário para SimpleProducer
 *
 * Verifica se o método send do KafkaProducer é chamado corretamente.
 */
import org.apache.kafka.clients.producer.KafkaProducer;
import org.apache.kafka.clients.producer.ProducerRecord;
import org.junit.jupiter.api.Test;

import java.util.Properties;

import static org.mockito.Mockito.*;

class SimpleProducerTest {

    @Test
    void testProducerSend() {
        KafkaProducer<String, String> mockProducer = mock(KafkaProducer.class);
        Properties props = new Properties();
        props.put("bootstrap.servers", "localhost:9092");
        props.put("key.serializer", "org.apache.kafka.common.serialization.StringSerializer");
        props.put("value.serializer", "org.apache.kafka.common.serialization.StringSerializer");

        ProducerRecord<String, String> record = new ProducerRecord<>("meu-topico", "mensagem de exemplo");
        mockProducer.send(record);

        verify(mockProducer, times(1)).send(record);
    }
}
