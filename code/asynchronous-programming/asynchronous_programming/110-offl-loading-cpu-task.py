
import asyncio
import concurrent.futures
import time

from cpu_bound import fibonacci

async def main():
    loop = asyncio.get_running_loop()

    # Use ProcessPoolExecutor for CPU-bound task
    with concurrent.futures.ProcessPoolExecutor() as pool:
        future = loop.run_in_executor(pool, fibonacci, 40)

        print("Task is running in another process...")

        while not future.done():
            print("Task is still running...")
            await asyncio.sleep(1)  # Checking periodically

        # Once done, retrieve the result
        result = await future
        print(f"Task completed, result: {result}")
        
if __name__ == "__main__":
    asyncio.run(main())