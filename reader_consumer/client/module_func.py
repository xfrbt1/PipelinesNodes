from time import sleep
from reader_consumer.client.utils import transform_data
from reader_consumer.consumer.reader import read_records
from reader_consumer.db.create import bulk_create
from reader_consumer.db.setup_db import return_setup


def read_store_func(settings):
    while True:
        print("CONSUME_")
        data_bs: list[bytes] = read_records(settings.kafka_host, settings.kafka_topic)
        documents: list[dict] = transform_data(data_bs)
        collection = return_setup(settings)
        bulk_create(collection, documents)
        sleep(settings.delay)
