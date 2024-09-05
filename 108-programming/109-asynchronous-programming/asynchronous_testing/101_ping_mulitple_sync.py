import requests
import asyncio
from functools import partial

from settings import MAX

def ping(url: str, id: int):
    res = requests.get(url)
    return f"id: {id}, response: {res.status_code}"

def main():
    task_ping = partial(ping, "https://google.com")
    for i in range(MAX):
        res = task_ping(i)
        print(res)
    
if __name__ == "__main__":
    main()
        