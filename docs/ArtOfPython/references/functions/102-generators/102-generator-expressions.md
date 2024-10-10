# Generator Expressions: Iterables Meet Comprehensions

- notions of iterables and list comprehensions are combined in a new tool: *generator expressions*.

```python
>>> a = (x ** 2 for x in range(4))
>>> type(a)
<class 'generator'>
>>> print(a)
<generator object <genexpr> at 0x7fda47040ba0>
>>> 
>>> for i in a:
...     print(i)
... 
0
1
4
9
>>> 
```

- Generator expressions are very different: instead of building the result list in memory, they return a *generator object* automatically created iterable.
- This iteragble object in trun supports the *iteration protocol* to yield on piece of the reult list at a time in any iteration context. 
- The iterable object also retains generator state while active -- the varaible x i nthe preceding expressions, along with the generator's code location.

```python
>>> G = (x ** 2 for x in range(4))
>>> iter(G) is G      # iter(G) optional: __iter__ returns self
True
>>> next(G)           # Generator objects: automatic methods
0
>>> next(G)
1
>>> next(G)
4
>>> next(G)
9
>>> next(G)
Traceback (most recent call last):
File "<stdin>", line 1, in <module>
StopIteration
>>> G
<generator object <genexpr> at 0x00000000029A8318>
```