from httpx import AsyncClient
from bs4 import BeautifulSoup


async def soup_response(**kwargs):
    url = kwargs.get("url")
    headers = kwargs.get("headers")
    async with AsyncClient() as client:
        response = await client.get(url=url, headers=headers)
    soup = BeautifulSoup(response.content, "lxml")
    return soup
