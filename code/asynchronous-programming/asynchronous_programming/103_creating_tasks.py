import asyncio
import time


async def say_after(delay: int, what: str) -> None:
    await asyncio.sleep(delay)
    print(what)
    return 

async def main():
    task1 = asyncio.create_task(say_after(1, "hello"))
    task2 = asyncio.create_task(say_after(2, "world"))
    
    print(f"started at {time.strftime('%X')}")
    
    # wait until boths are completed (should 
    # take around 2 seconds)
    await task1
    await task2
    
    print(f"started at {time.strftime('%X')}")
    
if __name__ == "__main__":
    asyncio.run(main())