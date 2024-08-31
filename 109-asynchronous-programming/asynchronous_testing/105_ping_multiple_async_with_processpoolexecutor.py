import requests
import asyncio
from functools import partial
from concurrent.futures import ProcessPoolExecutor, Future

URLS = list(enumerate(['https://google.com'] * 100))

def ping(id: int, url: str, ):
    res = requests.get(url)
    return f"id: {id}, response: {res.status_code}"


# def ping():
#     res = requests.get('https://google.com')
#     print(f"id: 0, response: {res.status_code}")
async def say_hello(message):
    return message


"""
`asyncio.gather` block the event event loop,
until all the task are completed in executor 
"""
async def main_gather():
    old_task = asyncio.create_task(say_hello())
    tasks = [partial(ping, x, y) for x, y in URLS]
    loop = asyncio.get_event_loop()
    with ProcessPoolExecutor() as executor:
        
        print(await old_task)
        
        results = await asyncio.gather(
            *[loop.run_in_executor(executor, task) for task in tasks]
        )
        
        for result in results:
            print(result)
            
            


if __name__ == "__main__":
    asyncio.run(main_gather())
        