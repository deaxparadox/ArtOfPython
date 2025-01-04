import argparse
import multiprocessing
import concurrent.futures


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


def fibonacci(num: int) -> int:
    if num == 0:
        return 0
    if num == 1:
        return 1
    return fibonacci(num-2) + fibonacci(num-1)

def fibonacci_handler(num: int) -> None:
    result = fibonacci(num)
    print(result)
    
    
def main():
    args = arg_paraser()
    
    workers = args.workers
    number = args.number
    # fibonacci_handler(args.number)
    
    if workers > 1:
        with concurrent.futures.ProcessPoolExecutor(workers) as pool:
            pool.map(fibonacci_handler, [number for _ in range(workers)])
    else:
        fibonacci_handler(number)
    
    
if __name__ == "__main__":
    main()