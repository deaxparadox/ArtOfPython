# Immutability

Tuples are immutable:

- It means they doesn't support item assignment 

```python
>>> # Tuples are immutable:
>>> t[0] = 88888
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: 'tuple' object does not support item assignment
```

- They doesn't support item deleting;

```python
>>> del t[0]
---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)
Cell In[3], line 1
----> 1 del a[0]

TypeError: 'tuple' object doesn't support item deletion
```

But tuples can contian mutable object:

```python
>>> # but they can contain mutable objects:
>>> v = ([1, 2, 3], [3, 2, 1])
>>> v
([1, 2, 3], [3, 2, 1])
```