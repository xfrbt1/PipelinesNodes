from pydantic_settings import BaseSettings, SettingsConfigDict


class settings(BaseSettings):
    celery_broker_url: str | None = "redis://localhost:6379"
    redis_host: str | None = "redis"
    redis_port: str | None = "6379"

    kafka_host: str | None = "kafka:9092"
    kafka_topic: str | None = "test-topic"

    model_config = SettingsConfigDict(env_file="./.env", env_file_encoding="utf-8")
