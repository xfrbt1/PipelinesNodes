from kafka import KafkaConsumer


def subscribe_consumer(kafka_host: str | list[str], kafka_topic: str) -> KafkaConsumer:
    try:
        consumer = KafkaConsumer(
            kafka_topic,
            bootstrap_servers=kafka_host,
            auto_offset_reset="earliest",
            group_id="test-group",
        )
        consumer.subscribe([kafka_topic])
        return consumer
    except Exception:
        ...
