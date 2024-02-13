import asyncio
import json

from parser_producer.parser.records_creator import records_creator
from parser_producer.producer.writer import write_records_collection


def hc_func():
    print("| HEALTHCHECK |")


def write_func(settings):
    result = asyncio.run(records_creator())
    records = [json.dumps(record).encode("utf-8") for record in result]
    kafka_host = settings.kafka_host
    kafka_topic = settings.kafka_topic
    write_records_collection(records, kafka_host, kafka_topic)
