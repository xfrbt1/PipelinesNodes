from typing import Iterable

from parser_producer.core.settings import settings
from kafka import KafkaProducer


class kafka_produce_topic:
    def __init__(
        self,
        topic: str = settings().kafka_topic,
        host_string: str = settings().kafka_host_string,
        timeout: int | None = None,
    ):

        self.producer = KafkaProducer(bootstrap_servers=host_string)
        self.topic = topic
        self.producer.close(timeout) if timeout else ...

    def send(self, value: bytes, key: str | None = None, partition: str | None = None):

        self.producer.send(topic=self.topic, key=key, value=value, partition=partition)

    def send_iterable(self, collection: Iterable[bytes]):

        for record in collection:
            self.send(value=record)
            print("message_send >>> ", record[:10])

    def metrics(self):
        print("METRICS: ", self.producer.metrics())
