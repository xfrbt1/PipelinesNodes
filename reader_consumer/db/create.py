import logging

logger = logging.getLogger(__name__)


def bulk_create(collection, documents: list[dict]):
    try:

        documents_to_insert = [
            doc
            for doc in documents
            if collection.count_documents({"title": doc["title"]}) == 0
        ]

        if documents_to_insert:
            collection.insert_many(documents_to_insert, ordered=False)

    except Exception as ex:
        logger.exception(ex)
