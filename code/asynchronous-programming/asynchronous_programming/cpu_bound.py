def fibonacci_main(x: int) -> int:
    if x <= 0:
        return 0
    if x == 1:
        return 1
    return fibonacci_main(x-1) + fibonacci_main(x-2)


def fibonacci(x: int) -> int:
    value = fibonacci_main(x)
    print(f"Fibonacci of {x} is: {value}")
    return value
