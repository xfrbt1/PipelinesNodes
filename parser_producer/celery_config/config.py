from celery import Celery
from celery.schedules import crontab
from parser_producer.core.settings import settings as s

settings = s()


app = Celery("app")
app.conf.broker_url = settings.celery_broker_url
app.conf.result_backend = settings.celery_broker_url
app.conf.broker_connection_retry_on_startup = True


app.conf.beat_schedule = {
    "hc-task": {
        "task": "parser_producer.celery_config.tasks.hc_func_task",
        "schedule": crontab(minute="*/1"),
    },
    "write-func": {
        "task": "parser_producer.celery_config.tasks.write_func_task",
        "schedule": crontab(minute="*/1"),
    },
}
