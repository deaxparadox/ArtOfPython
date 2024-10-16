# nested `lambda` function


Like nested function definitions, lambda functions can reference variables from the containing scopes:

```python
>>> def make_incrementor(n):
...     return lambda x: x + n
... 
>>> f = make_incrementor(42)
>>> f(0)
42
>>> f(1)
43
```

**lambda** also has access to the names in any enclosing **lambda**.

```py
>>> action = (lambda x: (lambda y: x + y))
>>> 
>>> act = action(99)
>>> act
<function <lambda>.<locals>.<lambda> at 0x7f59feca51b0>
>>> act(3)
102
>>> act(3)
102
>>> ((lambda x: (lambda y: x + y))(99))(4)
103
>>> 
```