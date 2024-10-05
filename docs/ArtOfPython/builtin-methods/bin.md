# `bin()` function

Syntax:

```py
bin(x)
```

Convert an integer number to a binary string prefixed with "0b". The result is a valid Python expression. If *x* is not a Python `int` object, it has to define an *__index__()* method that returns an integer. Some examples:

```py
>>> bin(3)
'0b11'
>>> bin(-10)
'-0b1010'
>>> 
```