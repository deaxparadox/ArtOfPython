from multiprocessing import Pool

def __calculate_fibonacci(x: int) -> int:
    if x == 0:
        return 0
    if x == 1:
        return 1
    return __calculate_fibonacci(x-1) + __calculate_fibonacci(x-2)  

def fibonacci(x: int) -> None:
    _value = __calculate_fibonacci(x)
    print(f"Value of {x} is {_value}")
    return _value



def f(x):
    return x * x

if __name__ == "__main__":
    with Pool(5) as p:
        print(p.map(fibonacci, [x+40 for x in [1, 2, 3]]))