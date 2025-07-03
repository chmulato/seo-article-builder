package com.mulato;

import org.apache.kafka.clients.consumer.ConsumerRecord;
import org.apache.kafka.clients.consumer.ConsumerRecords;
import org.apache.kafka.clients.consumer.KafkaConsumer;
import org.junit.jupiter.api.Test;

import java.time.Duration;
import java.util.Collections;

import static org.mockito.Mockito.*;

class PedidoConsumerTest {

    @Test
    void testConsumerPoll() {
        KafkaConsumer<String, String> mockConsumer = mock(KafkaConsumer.class);

        ConsumerRecord<String, String> record =
                new ConsumerRecord<>("pedidos", 0, 0L, "1", "Pedido #1");
        ConsumerRecords<String, String> records =
                new ConsumerRecords<>(Collections.singletonMap(new org.apache.kafka.common.TopicPartition("pedidos", 0), Collections.singletonList(record)));

        when(mockConsumer.poll(Duration.ofMillis(500))).thenReturn(records);

        ConsumerRecords<String, String> polled = mockConsumer.poll(Duration.ofMillis(500));
        assert polled.count() == 1;
        assert polled.iterator().next().value().equals("Pedido #1");
    }
}
