from bs4 import BeautifulSoup
from httpx import AsyncClient


async def soup_response(**kwargs):
    url: str = kwargs.get("url")
    headers: dict = kwargs.get("headers")

    async with AsyncClient() as client:
        response = await client.get(url=url, headers=headers)

    return BeautifulSoup(response.content, "lxml")
