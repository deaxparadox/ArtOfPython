import asyncio

async def after(delay: int) -> None:
    await asyncio.sleep(delay)
    print(f"After -> {delay}")
    
    
async def main():
    background_tasks = set()

    for i in range(10):
        task = asyncio.create_task(after(i))

        # Add task to the set. This creates a strong reference.
        background_tasks.add(task)
        
        await task

        # To prevent keeping references to finished tasks forever,
        # make each task remove its own reference from the set after
        # completion:
        task.add_done_callback(background_tasks.discard)
        
if __name__ == "__main__":
    asyncio.run(main())