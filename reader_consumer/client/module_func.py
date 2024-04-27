import json
import logging
from time import sleep

from reader_consumer.consumer.reader import subscribe_consumer
from reader_consumer.db.create import bulk_create
from reader_consumer.db.setup_db import return_setup

logger = logging.getLogger(__name__)


def read_store_func(settings):
    consumer = subscribe_consumer(settings.kafka_host, settings.kafka_topic)
    while True:
        try:
            for record in consumer:
                documents = json.loads(record.value.decode())
                sleep(settings.delay)
                collection = return_setup(settings)
                bulk_create(collection, documents)
        except Exception as ex:
            logger.exception(ex)

