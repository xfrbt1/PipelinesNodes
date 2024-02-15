from kafka import KafkaProducer


def write_records(
    collection: list[bytes], kafka_host: str | list[str], kafka_topic: str
):
    try:
        producer = KafkaProducer(bootstrap_servers=kafka_host)
        [producer.send(topic=kafka_topic, value=record) for record in collection]
        print("producer write: ", len(collection))
    except Exception as e:
        print("\nwrite exc: ", e)
