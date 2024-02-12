import datetime
import json

from parser_producer.parser.main import main_parser
from parser_producer.producer.main import kafka_produce_topic


def healthcheck():
    print("HEALTHCHECK: ", datetime.datetime.now().time())


async def main_func():
    result = await main_parser()
    result = [json.dumps(record).encode("utf-8") for record in result]
    kafka_produce_topic().send_iterable(result)
