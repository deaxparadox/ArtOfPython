import requests
import asyncio
from functools import partial
from concurrent.futures import ProcessPoolExecutor, Future

URLS = list(enumerate(['https://google.com'] * 10))

def ping(id: int, url: str, ):
    res = requests.get(url)
    return {"id": id, "response_code": res.status_code}


# def ping():
#     res = requests.get('https://google.com')
#     print(f"id: 0, response: {res.status_code}")
async def say_hello(message):
    return message


"""
`asyncio.as_completed` block the event event loop,
until all the task are completed in executor.

But, in `as_completed` result are return as soon as task
is completed in executor, and the following task can be used to 
futher processing.
"""
async def main_as_completed():
    # first task
    old_task = asyncio.create_task(say_hello("first task"))
    
    # last task
    last_task = asyncio.create_task(say_hello("last task done."))
    
    tasks = [partial(ping, x, y) for x, y in URLS]
    
    loop = asyncio.get_event_loop()
    
    with ProcessPoolExecutor() as executor:
        
        print(await old_task)
        
        future_tasks = [
            loop.run_in_executor(executor, task) 
            for task in tasks
        ]
        
        for f in asyncio.as_completed(future_tasks):
            code = await f
            if code['response_code'] == 200:
                print("Request", code['id'], "completed successfully.")
            
        print(await last_task)
        
        

if __name__ == "__main__":
    asyncio.run(main_as_completed())
        