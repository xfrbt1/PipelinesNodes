import asyncio
from typing import Coroutine, Callable

from parser_producer.core.config import (BBC_TITLE, BBC_URL, CHESS_TITLE,
                                         CHESS_URL, HABR_TITLE, HABR_URL,
                                         HEADERS, ONLINER_TITLE, ONLINER_URL)
from parser_producer.parser.parse_soup_data import (bbc_news_parser,
                                                    chess_news_parser,
                                                    habr_news_parser,
                                                    onliner_news_parser)
from parser_producer.parser.payload_creator import create_payload
from parser_producer.parser.records_factory import records_factory
from parser_producer.parser.soup_response import soup_response

import logging

logger = logging.getLogger(__name__)


def records_creator() -> list[Callable | Coroutine]:
    try:
        parser_objects_kwargs = [
            (bbc_news_parser, BBC_URL, BBC_TITLE),
            (habr_news_parser, HABR_URL, HABR_TITLE),
            (onliner_news_parser, ONLINER_URL, ONLINER_TITLE),
            (chess_news_parser, CHESS_URL, CHESS_TITLE),
        ]
        return [
            records_factory(
                soup_resp=soup_response,
                parser=po[0],
                picker=create_payload,
                url=po[1],
                headers=HEADERS,
            )
            for po in parser_objects_kwargs
        ]
    except Exception as ex:
        logger.exception(ex)

