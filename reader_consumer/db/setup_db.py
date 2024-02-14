from pymongo import MongoClient


def get_client(settings):
    mongo_host = settings.mongo_host
    mongo_port = settings.mongo_port
    client = MongoClient(host=mongo_host, port=mongo_port)
    return client


def get_db_collection(client, settings):
    db = client[settings.db_name]
    collection = db[settings.collection_name]
    return collection


def create_index_(collection, field: str, index_type, **kwargs):
    collection.create_index((field, index_type), **kwargs)


def return_setup(settings):
    client = get_client(settings)
    collection = get_db_collection(client, settings)
    create_index_(collection, "title", "text", unique=True)
    return collection
