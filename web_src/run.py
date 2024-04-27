import uvicorn
from starlette.applications import Starlette
from starlette.routing import Route

from web_src.api_handlers.news import search_titles

if __name__ == "__main__":
    routes = [Route("/search-titles", search_titles)]
    app = Starlette(routes=routes)
    uvicorn.run(app, host="0.0.0.0", port=8800)
