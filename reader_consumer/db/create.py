from pymongo import InsertOne


def bulk_create(collection, documents: list[dict]):
    try:

        operations = [InsertOne(document) for document in documents]
        result = collection.bulk_write(operations, ordered=False)
        print("docs: {}".format(len(documents)))
        print("inserted: {}".format(result.inserted_count))

    except Exception as e:
        print("error bulk creating: ", e)
