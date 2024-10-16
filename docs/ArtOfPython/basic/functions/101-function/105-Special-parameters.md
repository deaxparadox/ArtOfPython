# Special parameters

By default, arguments may be passed to a Python function either by a position or explicitly by keyword. For readability and performance, it make sense to restrict the way arguments can be passed so that a developer need only look at the function definition to determine if items are passed by position, by position or keyword, or by keyword.

### Syntax 

```py
def f(pos1, pos2, /, pos_or_kwd, *, kwd1, kwd2):
      -----------    ----------     ----------
        |             |                  |
        |        Positional or keyword   |
        |                                - Keyword only
         -- Positional only
```

- where `/` and `*` are optional. It used, these symbols indicate the kind of parameter by how th arguments may be passed to the function: positoinal-onl, positional-or-keyword, and keyword-only. Keyword parameters are also referred to as named parameters.


### Stadard arguments

```python
>>> def standard_arg(arg):
...     print(arg)
```

```python
def standard_args(arg):
    print(arg)

standard_args(1)
standard_args(arg=3)

# output 
1
3
```


### positional arguments

```python 
>>> def pos_only_arg(arg, /):
...     print(arg)
```

```python
def pos_only_arg(arg, /):
    print(arg)

pos_only_arg(1)

# output
1
```

- If you write:

```python
pos_only_arg(arg=1)

# you will get TypeError
---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)
Cell In[12], line 5
      2     print(arg)
      4 pos_only_arg(1)
----> 5 pos_only_arg(arg=1)

TypeError: pos_only_arg() got some positional-only arguments passed as keyword arguments: 'arg'

```

## Keyword only argument

```python
>>> def kwd_only_arg(*, arg):
...     print(arg)
... 
```

```python
kwd_only_arg(arg=1)

# output
1

kwd_only_arg(1)         # you will get TypeError
```

- if you try to use it as keyword argument you will `TypeError`.


## Combined

```python
>>> def combined_example(pos_only, /, standard, *, kwd_only):
...     print(pos_only, standard, kwd_only)
```

```python
combined_example(1, standard=2, kwd_only=3)

# output
1 2 3
```


Finally, consider this function definition which has a potential collision between the positional argument `name` and `**kwds` which has `name` as a key:

```py
def foo(name, **kwds):
    return 'name' in kwds
```

- There is no possible call that will make it return `True` as the keyword `'name'` will always bind to the first parameter. For example:

```py
>>> foo(1, **{'name': 2})
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: foo() got multiple values for argument 'name'
>>> 
```

- But using `/` (positional only arguments), it is possible since it allows name as a positional argument and `'name'` as a key in the keyword arguments:

```py
def foo(name, /, **kwds):
    return 'name' in kwds
>>> foo(1, **{'name': 2})
True
```