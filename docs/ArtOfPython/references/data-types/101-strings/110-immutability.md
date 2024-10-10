# Immutablity

Python strings cannot be changed--they are immutable. Therefore, assigning to an indexed position in the string results in an error:

```py
>>> s[0] = 't'
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: 'str' object does not support item assignment
>>> 
```

Therefore cannot delete character from string.