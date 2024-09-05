import asyncio
import time

async def say_after(delay: int, what: str) -> None:
    await asyncio.sleep(delay)
    print(what)
    return 

async def example_1():
    print(f"started at {time.strftime('%X')}")

    await say_after(1, 'hello')
    await say_after(2, 'world')

    print(f"finished at {time.strftime('%X')}")

    
    
if __name__ == "__main__":
    asyncio.run(example_1())