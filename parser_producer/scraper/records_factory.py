from typing import Callable


async def records_factory(
    soup_resp: Callable,
    parser: Callable,
    picker: Callable,
    **kwargs,
) -> list:
    response_result = await soup_resp(**kwargs)
    parse_result: list = parser(response_result, **kwargs)
    list_result: list = picker(parse_result, **kwargs)
    return list_result
