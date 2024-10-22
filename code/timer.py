from functools import wraps
import typing
import time


def timer(reg_message: str|None = None, run_message: str|None = None) -> typing.Callable:
    if reg_message:
        print(reg_message)
    def inner(func):
        def wrapper(*args, **kwargs) -> typing.Any:
            if run_message:
                print(run_message)
            start = time.time()
            result = func(*args, **kwargs)
            end = time.time()
            print(f"Elapsed: {end-start}")
            return result
        return wrapper
    return inner

@timer("Registring count_10", "Running timer function")
def count_10() -> None:
    for i in range(10):
        print(i, end='\t')
        # time.sleep(.1)
    print()
    return


@timer("Registring class Count10", "Creating a instance")
class Count10:
    def __init__(self) -> None:
        self.__max = 10
    @timer("Registring count attribute of Count10`", "Running method")
    def count(self) -> None:
        for i in range(self.__max):
            print(i, end='\t')
            # time.sleep(.1)
        print()
        return
    

count_10()
print()
c = Count10()
c.count()