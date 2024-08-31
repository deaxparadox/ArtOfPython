import asyncio
import time 

async def wait(delay: int) -> str:
    await asyncio.sleep(delay)
    return f"Waited for: {delay}"


async def main():
    task = asyncio.create_task(wait(10))
    
    task.cancel()
    
    try:

        await task
    except asyncio.CancelledError as e:
        
        print(f"Task cancelled: {task.cancelled()}")
    
    
    
        
if __name__ == "__main__":
    asyncio.run(main())