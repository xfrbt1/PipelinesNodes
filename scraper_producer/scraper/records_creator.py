import logging
from typing import Callable, Coroutine

from scraper_producer.core.config import (CHESS_TITLE, CHESS_URL, HABR_TITLE,
                                          HABR_URL, HEADERS, ONLINER_TITLE,
                                          ONLINER_URL)
from scraper_producer.scraper.payload_creator import create_payload
from scraper_producer.scraper.processing_soup_data import (
    chess_news_scraper, habr_news_scraper, onliner_news_scraper)
from scraper_producer.scraper.records_factory import records_factory
from scraper_producer.scraper.soup_response import soup_response

logger = logging.getLogger(__name__)


def records_creator() -> list[Callable | Coroutine]:
    try:
        parser_objects_kwargs = [
            (habr_news_scraper, HABR_URL, HABR_TITLE),
            (onliner_news_scraper, ONLINER_URL, ONLINER_TITLE),
            (chess_news_scraper, CHESS_URL, CHESS_TITLE),
        ]
        return [
            records_factory(
                response_content=soup_response,
                scraper=po[0],
                picker=create_payload,
                url=po[1],
                headers=HEADERS,
            )
            for po in parser_objects_kwargs
        ]
    except Exception as ex:
        logger.exception(ex)
