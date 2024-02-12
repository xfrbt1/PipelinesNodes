from functools import lru_cache

from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    celery_broker_url: str | None = "redis://localhost:6379"
    redis_host: str | None = "redis"
    redis_port: str | None = "6379"

    kafka_host_string: str | None = "kafka_b:9092"
    kafka_topic: str | None = "test-topic"

    model_config = SettingsConfigDict(env_file="./.env", env_file_encoding="utf-8")


@lru_cache()
def settings():
    return Settings()
