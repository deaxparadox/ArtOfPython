import argparse
import concurrent.futures
import asyncio
from functools import partial, wraps
import time


def timeit(message: str = None):
    def wrapper(func):
        @wraps
        def inner(*args, **kwargs):
            start = time.time()
            result = func(*args, **kwargs)
            end = time.time()
            if message:
                print(f"{message}, {end-start}")
            print(end-start)
            return result
        return inner
    return wrapper

def arg_paraser() -> argparse.Namespace:
    arguments = argparse.ArgumentParser()
    arguments.add_argument(
        '-n', "--number",
        help="Enter the number.",
        type=int
    )
    arguments.add_argument(
        '-w', "--workers",
        help="Enter the number.",
        type=int,
        default=1
    )
    arguments.add_argument(
        "-v",
        "--verbose",
        default=True,
        action="store_true",
        help="increase output verbosity",
    )
    return arguments.parse_args()



# @timeit("Timeing")
def fibonacci(num: int) -> int:
    if num == 0:
        return 0
    if num == 1:
        return 1
    return fibonacci(num-2) + fibonacci(num-1)

def fibonacci_handler(num: int) -> None:
    result = fibonacci(num)
    # print(result)
    return result
    
    
async def main():
    args = arg_paraser()
    
    workers = args.workers
    number = args.number
    
    loop = asyncio.get_running_loop()
    
    if workers > 1:
        with concurrent.futures.ProcessPoolExecutor(workers) as pool:
            # pool.map(fibonacci_handler, [number for _ in range(workers)])
            numbers = [number for _ in range(workers)]
            
            calls = [partial(fibonacci_handler, n) for n in numbers]
            call_cors = [
                loop.run_in_executor(pool, f) for f in calls
            ]
            
            results = await asyncio.gather(*call_cors)
            for r in results:
                print(r)
    else:
        await fibonacci_handler(number)
    
    
if __name__ == "__main__":
    asyncio.run(main())