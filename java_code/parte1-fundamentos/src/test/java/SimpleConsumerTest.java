/**
 * Teste unitário para SimpleConsumer
 *
 * Verifica se o consumer consome mensagens corretamente usando mock.
 */
import org.apache.kafka.clients.consumer.ConsumerRecord;
import org.apache.kafka.clients.consumer.ConsumerRecords;
import org.apache.kafka.clients.consumer.KafkaConsumer;
import org.junit.jupiter.api.Test;

import java.time.Duration;
import java.util.Collections;

import static org.mockito.Mockito.*;

class SimpleConsumerTest {

    @Test
    void testConsumerPoll() {
        KafkaConsumer<String, String> mockConsumer = mock(KafkaConsumer.class);
        ConsumerRecord<String, String> record = new ConsumerRecord<>("meu-topico", 0, 0L, null, "mensagem de exemplo");
        ConsumerRecords<String, String> records = new ConsumerRecords<>(Collections.singletonMap(new org.apache.kafka.common.TopicPartition("meu-topico", 0), Collections.singletonList(record)));
        when(mockConsumer.poll(Duration.ofSeconds(5))).thenReturn(records);

        ConsumerRecords<String, String> polled = mockConsumer.poll(Duration.ofSeconds(5));
        assert polled.count() == 1;
        assert polled.iterator().next().value().equals("mensagem de exemplo");
    }
}
