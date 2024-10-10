# Multiple Lines Strings

To span strings to multiple lines. One is to use triple quotes `"""..."""` or `'''...'''`. End of lines is automatically included in the string.

```py
>>> # Multple line string: using triple quotes
>>> s = """line 1           
... line 2
... line 3"""
>>>
>>> # end of line is automatically added after 1, 2, and 3
>>> s
'line 1\nline 2\nline 3'
>>>
>>> # using print funciton to format the string.
>>> print(s)
line 1
line 2
line 3
>>> 
```

Suppose you to write a long string in python for project and you cannot use *triple quotes* because it will add *end of line*, so how do you do it.

- For this case you use `\` for preventing quotes (*single* or *double*, or *triple*) from adding *end of line*.

```py
>>> # single quote
>>> s = 'line 1\
... line 2\
... line 3'
>>> s
'line 1line 2line 3'
>>> 
>>> print(s)
line 1line 2line 3
>>> 
>>> # double quote
>>> s = "line 1\
... line 2\
... line 3"
>>> 
>>> print(s)
line 1line 2line 3
>>> 
>>> # similarly for triple quotes
```