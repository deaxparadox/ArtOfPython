# Pool Object

The Pool object which offers a convenient means of parallelizing the execution of a function across multiple input values, distributing the input data across processes (data parallelism).

The following example demonstrates the common practice of defining such functions in a module so that child processes can successfully import that module. This basic example of data parallelism using Pool,

```python
from multiprocessing import Pool


def f(x):
    return x * x

if __name__ == "__main__":
    with Pool(5) as p:
        print(p.map(f, [1, 2, 3]))
```

will print to standard output:

```bash
[1, 4, 9]
```

Code file: [>>>](code/101-simple.py)


----------


### Pool class

One can create a pool of process which will carry out tasks submitted to it with the `Pool` class

syntax:

```
class multiprocessing.pool.Pool([processes[, initializer[, initargs[, maxtasksperchild[, context]]]]])
```

A process pool object which controls a pool of worker processes to which jobs can be submitted. It supports asynchronous results with timeouts and callbacks and has a parallel map implementation.

#### Arguments

***processes***:  is the number of worker to use. If *processes* is `None` then the number returned by `os.cpu_count()` is used.



***initializer***: If initializer is not None then each worker process will call initializer(*initargs) when it starts.


***maxtasksperchild*** is the number of tasks a worker process can complete before it will exit and be replaced with a fresh worker process, to enable unused resources to be freed. The default *maxtasksperchild* is `None`, which means worker processes will live as long as the pool.

