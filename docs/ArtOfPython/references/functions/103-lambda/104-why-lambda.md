# What Use lambda?

**lambda** comes in handy as a sort of function shorthand that allows you to embed a function's definition within the code that uses it.

**lambda** is also commonly used to code *jump tables*, which are lists or dictionaries of actions to be performed on demand. For example:

```py
>>> L = [lambda x: x ** 2,              # Inline function definitino
...     lambda x: x ** 3,
...     lambda x: x ** 4]               # A list of three callable functions
>>> 
>>> for f in L:
...     print(f(2))
... 
4
8
16
>>> 
>>> print(L[0](3))
9
>>> 
```

The equivalent def coding would require temporary function names and function definitions outside the context of intended use:

```py
>>> def f1(x): return x ** 2
... 
>>> def f2(x): return x ** 3
... 
>>> def f3(x): return x ** 4
... 
>>> l = [f1, f2, f3]
>>> 
>>> for f in L:
...     print(f(2))
... 
4
8
16
>>> print(L[0](3))
9
>>> 
```

## Multiway branch switches

```py
>>> 
>>> key = "got"
>>> {'already': (lambda: 2 + 2),
...     'got': (lambda: 2 * 4),
...     'one': (lambda: 2 ** 6)}[key]()
8
>>> 
```
