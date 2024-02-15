from celery import shared_task
from parser_producer.client.module_func import write_func
from parser_producer.core.settings import settings as s

settings = s()


@shared_task
def write_func_task():
    print("\n\nrun write task >>")
    write_func(settings)
