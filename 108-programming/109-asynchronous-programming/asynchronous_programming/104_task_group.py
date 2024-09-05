import asyncio
import time


async def say_after(delay: int, what: str) -> None:
    await asyncio.sleep(delay)
    print(what)
    return 

async def main():
    async with asyncio.TaskGroup() as tg:
        task1 = tg.create_task(say_after(1, "hello"))
        task2 = tg.create_task(say_after(2, "world"))
        
        print(f"started at {time.strftime('%X')}")
    
    # The await is implicit when the context manager exits.
    
    print(f"started at {time.strftime('%X')}")
    
    
    
if __name__ == "__main__":
    asyncio.run(main())