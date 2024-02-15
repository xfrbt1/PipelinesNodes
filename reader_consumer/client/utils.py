import json


def transform_data(data: list[bytes]) -> list[dict]:
    data_dict_list: list[list[dict]] = [json.loads(bs.decode()) for bs in data]
    documents = [document for batch in data_dict_list for document in batch]
    return documents
