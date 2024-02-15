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


def return_setup(settings):
    client = get_client(settings)
    collection = get_db_collection(client, settings)
    collection.create_index({"title": "text"})
    return collection
