from celery import shared_task
from parser_producer.client.module_func import hc_func, write_func
from parser_producer.core.settings import settings as s
settings = s()


@shared_task
def hc_func_task():
    print("\n\nrun hc task >>")
    hc_func()


@shared_task
def write_func_task():
    print("\n\nrun write task >>")
    write_func(settings)
