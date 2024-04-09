from motor.motor_asyncio import AsyncIOMotorClient
from web_src.core.settings import settings as Settings


async def get_collection():
    settings = Settings()
    client = AsyncIOMotorClient(settings.mongo_url)
    database = client[settings.db_name]
    return database[settings.collection_name]
