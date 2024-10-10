# `dict` 

A pair of braces creates an empty dictionary: {}

- Placing a comma-separated list of key:value pairs within the braces adds initial key:value pairs to the dictionary; this is also the way dictionaries are written on output.

```python
>>> tel = {'jack': 4098, 'sape': 4139}
```

## `dict()` constructor

The `dict()` constructor builds dictionaries directly from sequences of key-value paris:

```python
>>> dict([('sape', 4139), ('guido', 4127), ('jack', 4098)])
{'sape': 4139, 'guido': 4127, 'jack': 4098}
```

We can also supply simple keyword argument to `dict()` constructor function to generate a dictionary:

```py
>>> 
>>> dict(a=1, b=2)
{'a': 1, 'b': 2}
>>> 
>>> dict(sape=4139, guido=4127, jack=4098)
{'sape': 4139, 'guido': 4127, 'jack': 4098}
```

## `dict` comprehensions

```python
>>> {x: x**2 for x in (2, 4, 6)}
{2: 4, 4: 16, 6: 36}
```
