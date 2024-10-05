# Range

The `range` type represents an immutable sequence of numbers and is commonly used for looping specific number of times in `for` loops.

```py
class ragne(stop)
class range(start, stop[,step])
```

The arguments to the range constructor must be integers (either buil-in `int` or any object that implement the `__index__()` special method). 

If the step argument is omitted, it defaults to `1`.

If the *start* argument is omitted, it default to `0`. 

If *step* is zero, **ValueError** is raised.

For a *positive step*, the contents of a range `r` are determined by the formula `r[i] = start + step * i`.

For a *negative step*, the contents of the range are still determined by the formuila `r[i] = start + step * i`, but the constraints are `i >= 0` and `r[i] > stop`.

A range object will be empty if `r[0]` does not meet the value constraint. Ranges do support negative indices, but these are interpreted as indexing from the end of the sequence determined by the positive indices.

```py
>>> list(range(10))
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
>>> list(range(1, 11))
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
>>> list(range(0, 30, 5))
[0, 5, 10, 15, 20, 25]
>>> list(range(0, 10, 3))
[0, 3, 6, 9]
>>> list(range(0, -10, -1))
[0, -1, -2, -3, -4, -5, -6, -7, -8, -9]
>>> list(range(0))
[]
>>> list(range(1, 0))
[]
```

Ranges implement all of the **common** sequence operations except concatenation and repetition (due to the fact that range object can only represent sequences that follow a strict patter and repetition and concatenation will usually voilates that pattern).

### start

- The value of the *start* parameter (or `0` if the parameter was not supplied)

### stop

The value of the *stop* parameter

### step

The value of the *step* parameter (or `1` if the parameter was not supplied). Step means jump.

### Advantage

A `range` object will alaways take the same (small) amount of memory, no matter the size of the range it represent.

Range objects implement the collections.abc.Sequence ABC, and provide features such as containment tests, element index lookup, slicing and support for negative indices (see `Sequence Types` — `list`, `tuple`, `range`):

```py
>>> r = range(0, 20, 2)
>>> r
range(0, 20, 2)
>>> 11 in r
False
>>> 10 in r
True
>>> r.index(10)
5
>>> r[5]
10
>>> r[:5]
range(0, 10, 2)
>>> r[-1]
18
```

We can also compare range objects with equality `==` and `!=` as sequences.

```py
>>> range(10) == range(10)
True
>>> range(10) == range(9)
False
>>> 
```


# Examples

example_1:

```py

In [37]: r = range(0, 10)

In [38]: a = iter(r)

In [39]: loop = True

In [40]: while loop:
    ...:     try:
    ...:         val = next(a)
    ...:         print(val)
    ...:     except:
    ...:         loop = False
    ...:         print("Closing loop")
    ...: 
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
Closing loop
```