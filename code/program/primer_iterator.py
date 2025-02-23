import typing
from abc import abstractmethod, ABC
from functools import wraps

def single_instance(instance_num: int = 1):
    instances = []
    def callable(c):
        @wraps(c)
        def wrapper(*args, **kwargs):
            if len(instances) >= instance_num:
                raise RuntimeError("Maximum instance already created")
            instance = c(*args, **kwargs)
            instances.append(instance)
            return instance
        return wrapper
    return callable

class BasePrime(ABC):
    def __init__(self, inital, target):
        self.__initial = inital
        self.__target = target
        
    @property
    def value(self):
        return self.__initial
    
    @value.setter
    def value(self, value: int):
        self.__initial = value

    @abstractmethod
    def skip_value(self, func: typing.Callable):
        raise NotImplementedError("methods not implemented")
        
    def _check_prime(self):
        for i in range(2, self.__initial):
            if self.__initial % i == 0:
                return False
        return True
        
    def __increment(self):
        self.__initial+=1
        
    def __return_prime(self):
        while True:
            if self._check_prime():
                break
            self.__increment()
        return self.__initial

    def __return_wrapper(self):
        value = self.__return_prime()
        self.__increment()
        if value > self.__target:
            raise StopIteration
        return value

    def __iter__(self):
        return self
    
    def __next__(self):
        if self.__initial >= self.__target:
            raise StopIteration
        return self.__return_wrapper()
    
    def __enter__(self):
        return self
    
    def __exit__(self, obj_type, obj_value, obj_traceback):
        return

@single_instance()
class Primer(BasePrime):
    def __init__(self, inital: int = 1, target: int = 1000):
        if inital >= target:
            raise RuntimeError("Initial value must be smaller than target.")
        super().__init__(inital=inital, target=target)
        
    def skip_value(self, func):
        raise NotImplementedError("Method not implemented")

if __name__ == "__main__":
    with Primer(500, 550) as p:
        for i in p:
            print(p.value)
            