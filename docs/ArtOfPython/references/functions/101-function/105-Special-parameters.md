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

- where `/` and `*` are optional. It used, these symbols indicate the kind of parameter by how th arguments may be passed to the function: positoinal-only, positional-or-keyword, and keyword-only. Keyword parameters are also referred to as named parameters.



In Python argument can be passed to function (or method) in various ways, and you can limit the way in which python accept the argument, first and forement, we are going to see standard (or default) way in which we can pass the argument.

### Stadard arguments (position and keyword)

In standard way, we specify the *names* inside the function definition parentheses, and pass the argument as *position* and *key-word*. First, we argument we positional way to passing argument:


```python
>>> def standard_arg(arg):
...     print(arg)
...
>>> standard_args(1)
```

```bash
# output 
1
3
```

Next, we are going to key-word way passing the argument:

```python
>>> def standard_arg(arg):
...     print(arg)
...
>>> standard_args(arg=3)
```

```bash
# output 
1
3
```

### *N* position arguments

In Python we can pass *N* number of position argument.

```py
>>> def npos(*args):
...     print(args)
... 
>>> npos("Dr. Amit", 95, "Neuro")
('Dr. Amit', 95, 'Neuro')
>>> 
```

We specify the `*args as the argument. It store all the position argument in tuple, and we can access it by indexing.

### *N* keyword arguments

We can also pass *N* key-word argument, by specifing `**kwargs` as function argument. It store all the argument in `dict` form.

```py
>>> def nkw(**kargs):
...     print(kargs)
... 
>>> nkw(n=1, m=2, name='paradox')
{'n': 1, 'm': 2, 'name': 'paradox'}
>>> 
```


### Positional only arguments

We can limit the function to accept only the position argument with help of `/` parameter.

```python 
>>> def pos_only_arg(arg, /):
...     print(arg)
... 
>>> pos_only_arg("hi")
hi
>>> 
```

If you try to pass *keyword* argument here, we will get *TypeError`.


```python
>>> pos_only_arg(arg=12)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: pos_only_arg() got some positional-only arguments passed as keyword arguments: 'arg'
>>> 
```

Also, we can only pass one position argument here, we will try to pass more than one, we will get *TypeError*.

```py
>>> pos_only_arg("hi", 1)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: pos_only_arg() takes 1 positional argument but 2 were given
>>> 
```

### Keyword only argument

We can also limit the function accept only *keyword* as argument with the help of *** chracter:

```py
>>> def kwd_only_args(*, kwarg):
...     print(kwarg)
... 
>>> kwd_only_args(kwarg=12)
12
>>>  
```

If we try value as positional we will get *TypeError*.

```py
>>> kwd_only_args(12)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: kwd_only_args() takes 0 positional arguments but 1 was given
>>> 
```

This function type only accept, one *keyword* argument, else we get *TypeError*.

### Combined

We can also combined special character `*` and `/`, to define a definition the in which we want our function to accept the argument.

```python
>>> def combined_example(pos_only, /, standard, *, kwd_only):
...     print(pos_only, standard, kwd_only)
```

```python
combined_example(1, standard=2, kwd_only=3)

# output
1 2 3
```

### Function Argument collision

Consider this function definition which has a potential collision between the positional argument `name` and `**kwds` which has `name` as a key:

```py
def foo(name, **kwds):
    return 'name' in kwds
```

There is no possible call that will make it return `True` as the keyword `'name'` will always bind to the first parameter. For example:

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