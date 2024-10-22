import asyncio

async def nested():
    return 42

async def main():
    
    
    # schedule nested() to run soom concurrently
    # with "main()".
    task = asyncio.create_task(nested())
    
    # "task" can now be used to cancel "nested()", or
    # an simply be awaited to wait until it is complete:
    await task
    
    
if __name__ == "__main__":
    asyncio.run(main())