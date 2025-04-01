
import asyncio
import concurrent.futures
import time

from cpu_bound import fibonacci

def check_complete(future: asyncio.Future):
    result = future.done()
    print(f"Result of CPU is: {result}")
    return

async def main():
    loop = asyncio.get_running_loop()

    # Use ProcessPoolExecutor for CPU-bound task
    with concurrent.futures.ProcessPoolExecutor() as pool:
        future = loop.run_in_executor(pool, fibonacci, 40)
        future.add_done_callback(check_complete)

        print("Task is running in another process...")

        while not future.done():
            print("Task is still running...")
            await asyncio.sleep(1)  # Checking periodically
            
        print("All task completed")
        
if __name__ == "__main__":
    asyncio.run(main())