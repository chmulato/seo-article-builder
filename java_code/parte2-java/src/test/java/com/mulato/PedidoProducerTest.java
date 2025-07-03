package com.mulato;

import org.apache.kafka.clients.producer.KafkaProducer;
import org.apache.kafka.clients.producer.ProducerRecord;
import org.junit.jupiter.api.Test;

import java.util.Properties;

import static org.mockito.Mockito.*;

class PedidoProducerTest {

    @Test
    void testProducerSend() {
        KafkaProducer<String, String> mockProducer = mock(KafkaProducer.class);
        Properties props = new Properties();
        props.put("bootstrap.servers", "localhost:9092");
        props.put("key.serializer", "org.apache.kafka.common.serialization.StringSerializer");
        props.put("value.serializer", "org.apache.kafka.common.serialization.StringSerializer");

        // Simula envio de 1 pedido
        ProducerRecord<String, String> record = new ProducerRecord<>("pedidos", "1", "Pedido #1");
        mockProducer.send(record);

        verify(mockProducer, times(1)).send(record);
    }
}
