from parser_producer.parser.parse_soup_data import (
    bbc_news_parser,
    habr_news_parser,
    onliner_news_parser,
    chess_news_parser,
)
from parser_producer.parser.records_factory import records_factory
from parser_producer.parser.soup_response import soup_response
from parser_producer.core.config import (
    HEADERS,
    HABR_URL,
    BBC_URL,
    ONLINER_URL,
    CHESS_URL,
)

import asyncio


async def records_creator():
    parser_objects_kwargs = [
        (bbc_news_parser, BBC_URL),
        (habr_news_parser, HABR_URL),
        (onliner_news_parser, ONLINER_URL),
        (chess_news_parser, CHESS_URL),
    ]
    tasks = [
        records_factory(
            soup_resp=soup_response, parser=po[0], url=po[1], headers=HEADERS
        )
        for po in parser_objects_kwargs
    ]
    return await asyncio.gather(*tasks)
