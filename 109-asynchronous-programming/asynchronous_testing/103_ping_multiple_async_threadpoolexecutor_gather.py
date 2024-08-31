import requests
import asyncio
from functools import partial
from concurrent.futures import ThreadPoolExecutor, Future

URLS = list(enumerate(['https://google.com'] * 100))

def ping(id: int, url: str, ):
    res = requests.get(url)
    print(f"id: {id}, response: {res.status_code}")


# def ping():
#     res = requests.get('https://google.com')
#     print(f"id: 0, response: {res.status_code}")


async def main():
    tasks = [partial(ping, x, y) for x, y in URLS]
    loop = asyncio.get_event_loop()
    with ThreadPoolExecutor() as executor:
        asyncio.gather(
            *[loop.run_in_executor(executor, task) for task in tasks]
        )
        
        

if __name__ == "__main__":
    asyncio.run(main())
        