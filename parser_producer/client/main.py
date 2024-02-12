import json
import logging

from parser_producer.core.settings import settings as s
from parser_producer.parser.records_creator import records_creator
from parser_producer.producer.writer import write_records_collection

# logging.basicConfig(level=logging.ERROR, format="ERROR %(asctime)s : %(message)s : ")


def healthcheck():
    logging.info("healthcheck >> ")


async def main_func():
    settings = s()
    kafka_host = settings.kafka_host
    kafka_topic = settings.kafka_topic
    result = await records_creator()
    records = [json.dumps(record).encode("utf-8") for record in result]
    n_write = write_records_collection(records, kafka_host, kafka_topic)
    # logging.info("write: {}".format(n_write))
