from pydantic_settings import BaseSettings, SettingsConfigDict


class settings(BaseSettings):
    kafka_host: str | None = "kafka_host:9092"
    kafka_topic: str | None = "test-topic"

    delay: int = 2

    mongo_host: str = "localhost"
    mongo_port: int = 27017

    db_name: str = "news"
    collection_name: str = "news-collection"

    model_config = SettingsConfigDict(env_file="./.env", env_file_encoding="utf-8")
