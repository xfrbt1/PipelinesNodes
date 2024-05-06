from starlette.responses import JSONResponse
from starlette.requests import Request

from api.db.get_collection import get_collection


async def search_titles(request: Request) -> JSONResponse:
    collection = await get_collection()
    if title := request.query_params.get("title"):
        projection = {"_id": 0, "score": {"$meta": "textScore"}}
        cursor = collection.find({"$text": {"$search": title}}, projection=projection)
        documents = await cursor.to_list(length=None)
        return JSONResponse(documents, status_code=200)
    return JSONResponse(None, status_code=204)


async def all_titles(request: Request) -> JSONResponse:
    collection = await get_collection()
    cursor = collection.find()
    documents = await cursor.to_list(length=None)
    return JSONResponse(documents, status_code=200)
