from starlette.responses import JSONResponse

from api.db.get_collection import get_collection


async def search_titles(request):
    title = request.query_params.get("title")
    projection = {"_id": 0}
    collection = await get_collection()

    if title:
        projection["score"] = {"$meta": "textScore"}
        cursor = collection.find({"$text": {"$search": title}}, projection=projection)
    else:
        cursor = collection.find(projection=projection)

    documents = await cursor.to_list(length=None)

    return JSONResponse({"result": documents}, status_code=200)


async def all_titles(request): ...
