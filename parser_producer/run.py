import time

from parser_producer.client.module_func import write_func
from parser_producer.core.settings import settings as s


while True:
    settings = s()
    write_func(settings)
    time.sleep(settings.delay)
