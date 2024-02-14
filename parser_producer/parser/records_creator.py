from parser_producer.parser.parse_soup_data import (
    bbc_news_parser,
    habr_news_parser,
    onliner_news_parser,
    chess_news_parser,
)
from parser_producer.parser.records_factory import records_factory
from parser_producer.parser.soup_response import soup_response
from parser_producer.parser.payload_creator import create_payload
from parser_producer.core.config import (
    HEADERS,
    HABR_URL,
    BBC_URL,
    ONLINER_URL,
    CHESS_URL,
    BBC_TITLE,
    HABR_TITLE,
    ONLINER_TITLE,
    CHESS_TITLE,
)

import asyncio


async def records_creator() -> tuple[list]:
    try:
        parser_objects_kwargs = [
            (bbc_news_parser, BBC_URL, BBC_TITLE),
            (habr_news_parser, HABR_URL, HABR_TITLE),
            (onliner_news_parser, ONLINER_URL, ONLINER_TITLE),
            (chess_news_parser, CHESS_URL, CHESS_TITLE),
        ]
        tasks = [
            records_factory(
                soup_resp=soup_response,
                picker=create_payload,
                parser=po[0],
                url=po[1],
                headers=HEADERS,
            )
            for po in parser_objects_kwargs
        ]
        return await asyncio.gather(*tasks)
    except Exception as e:
        print("error (response_parse_pick): ", e)
