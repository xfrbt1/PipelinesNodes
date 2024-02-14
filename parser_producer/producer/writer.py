from kafka import KafkaProducer


def write_records(
    collection: list[bytes], kafka_host: str | list[str], kafka_topic: str
):
    try:

        producer = KafkaProducer(bootstrap_servers=kafka_host)
        print("producer connected: ", producer.bootstrap_connected())
        for record in collection:
            producer.send(topic=kafka_topic, value=record)
        print("producer send messages: ", len(collection))

    except Exception as e:
        print("\nwrite exc: ", e)
