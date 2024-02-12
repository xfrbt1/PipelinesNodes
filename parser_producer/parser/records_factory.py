from typing import Callable


async def records_factory(soup_resp: Callable, parser: Callable, **kwargs):
    try:
        response_result = await soup_resp(kwargs.get("url"), kwargs.get("headers"))
        parse_result = parser(soup=response_result, **kwargs)
        return parse_result
    except Exception as e:
        print("Error create record: ", e)
