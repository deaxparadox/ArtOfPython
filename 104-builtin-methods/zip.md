# zip() 

Syntax: 

```python
zip(*iterables, strict=false)
```

- Iterate over several iterables in parallel, producing tuples with an item from each one.

- Examples: 

```python
>>> for item in zip([1, 2, 3], ['sugar', 'spice', 'everything nice']):
...     print(item)
... 
(1, 'sugar')
(2, 'spice')
(3, 'everything nice')
```

- zip() returns an iterator of tupels, where the i-th tuples contains the i-th element from each of the argument iterables.

- Another way to think of zip() is that its turns rows in to columsn and columns in to rwos.

- `zip()` is lazy: The elements won't be processed untill the iterable is iterated on e.g. by a for loops of by wrapping in a `list`.


One thing to consider is that the iterables passed to zip() could have different lengths; sometimes by design, and sometimes because of a bug in the code that prepared these iterables. Python offers three different approaches to dealing with this issue:

- By default, zip() stops when the shortest iterable is exhausted. It will ignore the remaining items in the longer iterables, cutting off the result to the length of the shortest iterable:

```python
>>> list(zip(range(3), ['fee', 'fi', 'fo', 'fum']))
[(0, 'fee'), (1, 'fi'), (2, 'fo')]
```

- zip() is often used in cases where the iterables are assumed to be of equal length. In such cases, it’s recommended to use the `strict=True` option. Its output is the same as regular zip():

```python
>>> list(zip(('a', 'b', 'c'), (1, 2, 3), strict=True))
[('a', 1), ('b', 2), ('c', 3)]
```

- Unlike the default behavior, it raises a ValueError if one iterable is exhausted before the others;

```python
>>> for item in zip(range(3), ['fee', 'fi', 'fo', 'fum'], strict=True):  
...     print(item)
... 
(0, 'fee')
(1, 'fi')
(2, 'fo')
Traceback (most recent call last):
  ...
ValueError: zip() argument 2 is longer than argument 1
```