import argparse


def arg_paraser() -> argparse.Namespace:
    arguments = argparse.ArgumentParser()
    arguments.add_argument(
        'NUMBER',
        help="Enter the number.",
        type=int
    )
    arguments.add_argument(
        "-v",
        "--verbose",
        default=True,
        action="store_true",
        help="increase output verbosity",
    )
    return arguments.parse_args()


def factrial(num: int) -> int:
    if num == 1:
        return 1
    return num * factrial(num-1)

def factorial_handler(num: int) -> None:
    result = factrial(num)
    print(result)
    
    
def main():
    args = arg_paraser()
    factorial_handler(args.NUMBER)
    
    
if __name__ == "__main__":
    main()