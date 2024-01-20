

# Asynchronous Iterator using `__aiter__()` and `__anext__()`

In this example i am building `Asynchronous` Iteration, for this, you should have kownlege of OOPs and `asyncio`:

```py
import asyncio

async def func():
    return 1

class aFor():
    def __init__(self, stop = 0):
        self.__count = 0
        self.__stop = stop

    def __aiter__(self):
        return self
    
    async def __anext__(self):
        val = self.__count
        if self.__count == self.__stop:
            raise StopAsyncIteration
        self.__count += 1
        return val
    

async def main():
    af = aFor(10)

    async for i in af:
        print(i)

asyncio.run(main())

```

```ouptut
0
1
2
3
4
5
6
7
8
9
```