from kafka import KafkaProducer


def write_records_collection(
    collection: list[bytes],
    kafka_host: str | list[str],
    kafka_topic: str
):
    try:

        producer = KafkaProducer(bootstrap_servers=kafka_host)
        print("\nproducer connected: ", producer.bootstrap_connected())
        for record in collection:
            producer.send(topic=kafka_topic, value=record)
        print("\nproducer send messages: ", len(collection))
        producer.close(1)
        print("\nclosed, producer connection : ", producer.bootstrap_connected())

    except Exception as e:
        print("\nwrite exc: ", e)
