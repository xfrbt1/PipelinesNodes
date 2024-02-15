def create_payload(data: list[dict], **kwargs) -> list[dict]:
    n = kwargs.get("n")
    result = [{"title": block[0], "url": block[1]} for block in data][:n]
    print(len(result))
    return result
