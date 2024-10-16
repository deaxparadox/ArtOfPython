# Dictionary Unpacking

We can unpack dictionary in another dictionay or function argument. To unpack a dictionary we have to use `**` preceeding dictionary.

## Unpacking in dictionary

```py
>>> d
{'voltage': 'four million', 'state': "bleedin' demised", 'action': 'VOOM'}
>>> 
>>> # unpacking in dictionary
>>> {**d}
{'voltage': 'four million', 'state': "bleedin' demised", 'action': 'VOOM'}
>>> 
>>> # if try to unpack in global environment
>>> # will get error
>>> **d
  File "<stdin>", line 1
    **d
    ^^
SyntaxError: invalid syntax
>>> 
```

## Unpacking as function argument

```py
>>> def func(**kwargs):
...     print(kwargs)
... 
>>> 
>>> # unpacking as function arguments
>>> func(**d)
{'voltage': 'four million', 'state': "bleedin' demised", 'action': 'VOOM'}
>>> 
```

## Updaing dictionary: using unpacking

```py
>>> 
>>> d
{'voltage': 'four million', 'state': "bleedin' demised", 'action': 'VOOM'}
>>> 
>>> # another dictionary
>>> a = {}
>>> 
>>> # updating dictionary `a`
>>> a.update({**d})
>>> 
>>> a
{'voltage': 'four million', 'state': "bleedin' demised", 'action': 'VOOM'}
>>> a.update()
>>> 
>>> # again updating another value to dictionary
>>> a.update({'a':1})
>>> a
{'voltage': 'four million', 'state': "bleedin' demised", 'action': 'VOOM', 'a': 1}
>>> 
```