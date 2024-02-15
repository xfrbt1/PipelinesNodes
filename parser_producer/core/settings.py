from pydantic_settings import BaseSettings, SettingsConfigDict


class settings(BaseSettings):

    celery_broker_url: str | None = "redis://redis:6379"
    redis_host: str | None = "redis"
    redis_port: str | None = "6379"

    kafka_host: str | None = "kafka_host:9092"
    kafka_topic: str | None = "test-topic"

    delay: int = 15

    model_config = SettingsConfigDict(env_file="./.env", env_file_encoding="utf-8")
