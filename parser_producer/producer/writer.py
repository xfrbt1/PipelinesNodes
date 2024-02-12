import logging
from kafka import KafkaProducer

# logging.basicConfig(level=logging.ERROR, format="%(asctime)s : %(message)s : ")


def write_records_collection(
    collection: list[bytes], kafka_host: str | list[str], kafka_topic: str
):
    try:
        producer = KafkaProducer(bootstrap_servers=kafka_host)
        count = 0
        for record in collection:
            producer.send(topic=kafka_topic, value=record)
            count += 1
        return count
    except Exception as e:
        print(e)
        # logging.error("write exc: {}".format(e))
