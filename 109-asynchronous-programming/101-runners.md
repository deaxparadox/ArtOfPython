# Runners

- high level asyncio primitives to run asyncio code.
- The are built on top of an event loop with the aim to simplify async code usage for wide-spread scenarios.


### Running an asyncio Program

```
asyncio.run(coro, *, debug=None, loop_factory=None)¶
```

Execute the coroutine *coro* and return the result


```py
async def main():
    await asyncio.sleep(1)
    print('hello')

asyncio.run(main())
```

### Runner context manager

```
class asyncio.Runner(*, debug=None, loop_factory=None)¶
```

A context manager that simplifies *multiple* async function calls in the same context.

```python
import asyncio 

async def main():
    await asyncio.sleep(1)
    print("hello")
    
    
with asyncio.Runner() as runner:
    runner.run(main())
    runner.close()
```