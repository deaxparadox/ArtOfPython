import os
from multiprocessing import Pool

# get total cpu available
CPU_COUNT = os.cpu_count()

def __calculate_factorial(x: int) -> int:
    if x == 1:
        return 1
    return x * __calculate_factorial(x-1)  

def factorial(x: int) -> None:
    _value = __calculate_factorial(x)
    print(f"Value of {x} is {_value}")
    return _value



def f(x):
    return x * x

if __name__ == "__main__":
    with Pool(CPU_COUNT) as p:
        print(p.map(factorial, [x+40 for x in [1, 2, 3]]))
        
        # pool must be closed after using
        p.close()