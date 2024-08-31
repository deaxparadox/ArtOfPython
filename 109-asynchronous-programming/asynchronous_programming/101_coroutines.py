import asyncio


async def example_1():
    
    print("hello")
    await asyncio.sleep(1)
    print("world")
    
    
if __name__ == "__main__":
    asyncio.run(example_1())