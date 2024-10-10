
# Iterator

Let's manually create iterator using `while`, `iter()`, `next()` and `range()`:

```py
r = range(10)

a = iter(r)

loop = True 
while loop:
    try:
        val = next(a)
        print(val)
    except:
        loop = False
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

# Synchronous Iterator using `__iter__()` and `__next__()` methods

For understanding this example you should have knowledge of OOPs.

```py
# Creating an iterator which count from 0 to user input number
# It can only count positve increasing sequence

class For(object):
    def __init__(self, stop):
        self.__count = 0
        self.__stop = stop 
    def __iter__(self):
        return self 
    def __next__(self):
        val = self.__count
        if self.__count >= self.__stop:
            raise StopIteration
        self.__count += 1
        return val
        
```

Running iterator using `for` loop:

```py
f = For(20)

for i in f:
    print(i)
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
10
11
12
13
14
15
16
17
18
19
```
