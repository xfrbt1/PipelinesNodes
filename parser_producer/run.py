import asyncio

from parser_producer.client.module_func import write_func
from parser_producer.core.settings import settings as s

if __name__ == "__main__":
    settings = s()
    asyncio.run(write_func(settings))
