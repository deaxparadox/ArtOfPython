import asyncio
import concurrent.futures
from functools import partial
from typing import List

def __calculate_factorial(num: int) -> int:
    if num == 1:
        return 1
    return num * __calculate_factorial(num-1)

def factorial(num: int) -> int:
    value = __calculate_factorial(num)
    return value


def __calculate_fibonaaci(num: int) -> int:
    if num == 0:
        return 0
    if num == 1:
        return 1
    return __calculate_fibonaaci(num-1) + __calculate_fibonaaci(num-2)

def fibonacci(num: int) -> int:
    value = __calculate_fibonaaci(num)
    return value



async def main() -> None:
    with concurrent.futures.ProcessPoolExecutor() as pool:
        
        loop: asyncio.AbstractEventLoop = asyncio.get_running_loop()
        nums = [40, 41, 42, 43, 44]
        calls: List[partial[int]] = [partial(fibonacci, num) for num in nums]
        call_coros = []
        
        for call in calls:
            call_coros.append(loop.run_in_executor(pool, call))

        results = await asyncio.gather(*call_coros)
        
        for result in results:
            print(result)

if __name__ == '__main__':
    asyncio.run(main())
