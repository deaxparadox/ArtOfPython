# `lambda` Expressions

Small anonymous functions can be created with the `lambda` keyword.

- This function returns the sum of its two arguments: `lambda a, b: a + b`.

```py
>>> square = lambda x: x*2
>>> 
>>> square(2)
4
>>> square(3)
6
>>> 
>>> for i in range(10):
...     print(square(i), end=" ")
... 
0 2 4 6 8 10 12 14 16 18 
>>> 
```

Defaults work on lambda arguments, just like in a def:

```py
>>> x = (lambda a="fee", b="fie", c="foe": a + b + c)
>>> 
>>> x()
'feefiefoe'
>>> 
>>> x('wee')
'weefiefoe'
>>> 
```

The code in a lambda body also follows the same scope lookup rules as code inside a **def**. **lambda** expression introduce a local scope must like nested **def**, which automatically sees names in enclosing functions, the module, and the build-in scope.

```py
>>> def knights():
...     title = 'Sir'
...     # Title in enclosing def scope
...     action = (lambda x: title + " " + x)
...     # Return a function object
...     return action
... 
>>> act = knights()
>>> 
>>> msg = act('robin')              # 'robin' passed to x
>>> msg
'Sir robin'
>>> 
>>> act                             # act: a function, not its result
<function knights.<locals>.<lambda> at 0x7f59feca5360>
>>> 
```
