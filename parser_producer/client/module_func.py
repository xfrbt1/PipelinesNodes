import asyncio
import json
import logging
from time import sleep

from parser_producer.producer.writer import write_records
from parser_producer.scraper.records_creator import records_creator

logger = logging.getLogger(__name__)


async def write_func(settings) -> None:

    while True:
        scraping_result = await asyncio.gather(*records_creator())

        if scraping_result is None:
            continue

        logger.info(f"Get {len(scraping_result)} row from sources")
        print(f"Get {len(scraping_result)} row from sources")
        logger.info(scraping_result)
        print(scraping_result)

        records: list[bytes] = [
            json.dumps(record).encode() for record in scraping_result
        ]
        write_records(records, settings.kafka_host, settings.kafka_topic)
        sleep(settings.delay)
