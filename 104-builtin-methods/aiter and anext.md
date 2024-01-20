# `aiter()` and `anext()` function

## `aiter()`

Syntax

- aiter(async_iterable)

Returns an `asynchronous iterator` for an `asynchronous iterable`. Equivalent to calling `x.__aiter__()`.

### asynchronous iterable

An object, that can be used in an `async for` statement. Must return an `asynchronous iterator` from its `__aiter__()` method.


### asynchronous iterator

An object that implements the `__aiter__()` and `__anext__()` methods. `__anext__` must return an `awaitable` object object.

*async for* resolves the awaitables returned by an asynchronous iterator's `__anext__()` method until it raises a `StopAsyncIteration` exception.


# `anext()` 

Syntax 
    
- *awaitable* anext(async_iterator)
- *awaitable* anext(async_iterator, default)

When awaited, return the next item from the given `asynchronous iterator`, or default if given and the iterator is exhausted.

This is the async variable of the `next()` builtin, and behaves similarly.

This calls the `__next__()` method of async_iterator, returning an `awaitable`. Awaiting this returns the next value of the iterator. If *defaults* is given, it is returned if the iterator is exhausted, otherwise `StopAsyncIteration` is raised.

```py
import asyncio

r = range(10)

async def f():
    for i in range(10):
        yield i

async def main():
    a = aiter(f())

    breaker = True
    while breaker:
        try:
            print(await anext(a))
        except:
            breaker = False

asyncio.run(main())
```

```output
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