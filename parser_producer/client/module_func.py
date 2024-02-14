import asyncio
import json
from time import sleep
from parser_producer.parser.records_creator import records_creator
from parser_producer.producer.writer import write_records


def write_func(settings):
    while True:
        print("PRODUCE_")
        res = asyncio.run(records_creator())
        records: list[bytes] = [json.dumps(r).encode() for r in res]
        write_records(records, settings.kafka_host, settings.kafka_topic)
        sleep(settings.delay)
