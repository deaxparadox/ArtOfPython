# Variables


[<<< Topics](README.md) | [Variables >>>](102-variables.md)

----------

The equal sign (`=`) is used to assign a value to a variable. Afterwards, no result is displayed before the next interactive prompt:

```py
>>> width = 20
>>> height = 5 * 9
>>> width * height
900
>>> 
```

If a variable is not "defined" (assigned a value), trying to use it will give you an error:

```py
>>> n  # try to access an undefined variable
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'n' is not defined
```