# Membership operation


## Membership oeration in `list`

Using *membership operation* we can check wheather a obect (list, tuple, string, character, ...) is present in list.

Support we have a numeric list:

```py
>>> a = list(range(10))
>>> a
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
```

Let's try to find object in it, for this we use `in` operation, if object is present in `list` it return `True`, if not it return `False`,

```py
>>> 
>>> 1 in a
True
>>> 
>>> 9 in a
True
>>> 
>>> 
>>> 100 in a
False
>>> 
```

Not let's try membership on list of string:

```py
>>> ls = ['hello', 'world']
>>> 
>>> 
>>> 'hello' in ls
True
>>> 
>>> 'normal' in ls
False
>>> 
```

Now let's try memberhsip on list of class instance:

```py

>>> class A:
...     pass 
... 
>>> class B:
...     pass
... 
>>> class C: pass 
... 
>>> 
>>> a = A()
>>> b = B()
>>> d = [a, b]
>>> d
[<__main__.A object at 0x7f03d330a200>, <__main__.B object at 0x7f03d330a020>]
>>> 
>>> c in d
False
>>> a in d
True
>>> 
```


## Membership Operation in Tuples

```py
>>> a = tuple(range(10))
>>> a
(0, 1, 2, 3, 4, 5, 6, 7, 8, 9)
>>> 
>>> 
>>> 1 in a
True
>>> 2 in a
True
>>> 99 in 
  File "<stdin>", line 1
    99 in 
          ^
SyntaxError: invalid syntax
>>> 99 in a
False
>>> 
```

## Membership Operation in Dictionary