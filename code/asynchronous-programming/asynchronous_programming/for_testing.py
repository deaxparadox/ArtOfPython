import typing
import asyncio

def sleep_until(delay):
    asyncio.sleep(delay)


class Task:
    def __init__(self, delay: int = 1):
        self.delay = delay
        self._running = False
        self._completed = False
    
    
    async def running(self):
        return f"Running with delay {self.delay}"
    
    async def completed(self):
        return f'Competed with delay {self.delay}'
        
    async def run(self):
        self._running = True
        await asyncio.sleep(self.delay)
        self._completed = True
        self._running = False
    
class Iterator:
    def __init__(self, task: Task | None = None):
        self.tasks = []
        if callable(task):
            self.tasks.append(task)
        self.index = 0
        self.length = len(self.tasks)
        
    async def add(self, task: Task):
        self.tasks.append(task)
        self.length+=1
    
    def __aiter__(self, *args, **kwargs):
        return self
    
    async def __anext__(self, *args, **kwargs):
        if self.index == len(self.tasks): self.index = 0
        if len(self.tasks) == 0:
            raise RuntimeError("No task found")
        coroutine: Task = self.tasks[self.index]
        self.index += 1
        return coroutine
    
    async def check(self, coroutine):
        if coroutine._running:
            print(await coroutine.running())
        if coroutine._completed:
            print(await coroutine.completed())
        
       
        
async def main():
    iterator = Iterator()
    await iterator.add(Task(1))
    await iterator.add(Task(2))
    await iterator.add(Task(3))
    async for i in iterator:
        await iterator.check(i)
            
            
            
if __name__ == "__main__":
    asyncio.run(main())