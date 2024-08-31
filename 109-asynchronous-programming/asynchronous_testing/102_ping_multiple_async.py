import requests
import asyncio
from functools import partial
from concurrent.futures import ThreadPoolExecutor, Future

URLS = list(enumerate(['https://google.com'] * 100))

async def ping(id: int, url: str):
    res = requests.get(url)
    print(f"id: {id}, response: {res.status_code}")

async def main():
        loop = asyncio.get_event_loop()
        loop.run_until_complete(
            asyncio.gather(*[
                ping(x, y) for x, y in URLS
            ])
        )

if __name__ == "__main__":
    asyncio.run(main())
        