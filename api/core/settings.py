from pydantic_settings import BaseSettings, SettingsConfigDict


class settings(BaseSettings):
    mongo_host: str = "localhost"
    mongo_port: int = 27017
    mongo_url: str = f"mongodb://{mongo_host}:{mongo_port}/"

    db_name: str = "news"
    collection_name: str = "news-collection"

    model_config = SettingsConfigDict(env_file="./.env", env_file_encoding="utf-8")
