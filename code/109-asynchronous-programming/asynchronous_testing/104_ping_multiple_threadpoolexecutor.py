import requests
import asyncio
from functools import partial
from concurrent.futures import ThreadPoolExecutor, Future

def ping(url: str, id: int):
    res = requests.get(url)
    return f"id: {id}, response: {res.status_code}"

def main():
    task_ping = partial(ping, "https://google.com")
    with ThreadPoolExecutor() as executor:
        for res in executor.map(task_ping, range(100)):
            print(res)

if __name__ == "__main__":
    main()
        