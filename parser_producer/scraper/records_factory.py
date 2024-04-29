from typing import Awaitable, Callable


async def records_factory(
    response_content: Callable | Awaitable,
    scraper: Callable,
    picker: Callable,
    **kwargs,
) -> list:
    response = await response_content(**kwargs)
    parse_result: list = scraper(response, **kwargs)
    list_result: list = picker(parse_result, **kwargs)
    return list_result
