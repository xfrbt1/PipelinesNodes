import uvicorn
from starlette.applications import Starlette
from starlette.routing import Route

from api.api_handlers.news import search_titles

if __name__ == "__main__":
    uvicorn.run(
        Starlette(
            routes=[
                Route("/search-titles", search_titles),
            ]
        ),
        host="0.0.0.0",
        port=8800
    )
