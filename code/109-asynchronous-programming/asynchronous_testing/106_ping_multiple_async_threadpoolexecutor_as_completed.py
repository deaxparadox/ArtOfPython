import requests
import asyncio
from functools import partial
from concurrent.futures import ThreadPoolExecutor, Future

URLS = list(enumerate(['https://google.com'] * 10))

def ping(id: int, url: str, /):
    res = requests.get(url)
    return {"id": id, "response_code": res.status_code}


# def ping():
#     res = requests.get('https://google.com')
#     print(f"id: 0, response: {res.status_code}")


async def main():
    
    
    loop = asyncio.get_event_loop()
    
    with ThreadPoolExecutor() as executor:
        future_tasks = [
            loop.run_in_executor(
                executor, 
                partial(ping, x, y)
            ) for x, y in URLS
        ]
    
        for f in asyncio.as_completed(future_tasks):
            code = await f
            if code["response_code"] == 200:
                print("Request", code['id'], "completed successfully")
        
        

if __name__ == "__main__":
    asyncio.run(main())
        