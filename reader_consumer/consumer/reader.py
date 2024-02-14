from kafka import KafkaConsumer


def read_records(kafka_host: str | list[str], kafka_topic: str) -> list[bytes | str]:
    try:

        consumer = KafkaConsumer(
            kafka_topic,
            bootstrap_servers=kafka_host,
            consumer_timeout_ms=5000
        )
        print("consumer connected: ", consumer.bootstrap_connected())
        records = [record.value for record in consumer]
        print("consumer receive messages: ", len(records))
        return records

    except Exception as e:
        print("read exc: ", e)
