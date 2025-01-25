import asyncio

async def nested():
    return 42

async def main():
    
    
    # coroutine function must be awaited,
    # using await expression
    print(await nested())
    
    
if __name__ == "__main__":
    asyncio.run(main())