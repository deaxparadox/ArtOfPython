# Formatted string literals

A formatted string literal or f-string is a string literal that is prefixed with `'f'` or `'F'`. These strings may contain replacement fields, which are expressions delimited by curly braces `{}`. While other string literals always have a constant value, formatted strings are really expressions evaluated at run time.

Simple Example, in this case we are going to format a variable *name*.

```py
>>> name = "Fred"
>>> f"He said his name is {name}."
'He said his name is Fred.'
>>> 
```

We can use constructor `str()` and `repr()`:


```py
>>> name = "Fred"
>>> 
>>> f"He said his name is {name!s}."            # !s is equivalent to str()
'He said his name is Fred.'
>>>
>>> f"He said his name is {str(name)}."         # !s is equivalent to str()
'He said his name is Fred.'
>>>
>>> f"He said his name is {name!r}."
"He said his name is 'Fred'."
>>>
>>> f"He said his name is {repr(name)}."  # repr() is equivalent to !r
"He said his name is 'Fred'."
>>>
```

Formatting decimal number:

```py
>>> width = 10
>>> precision = 4
>>> value = decimal.Decimal("12.34567")
>>> f"result: {value:{width}.{precision}}"  # nested fields
'result:      12.35'
>>>
```

To format date:

```py
>>> today = datetime(year=2017, month=1, day=27)
>>> f"{today:%B %d, %Y}"  # using date format specifier
'January 27, 2017'
>>> f"{today=:%B %d, %Y}" # using date format specifier and debugging
'today=January 27, 2017'
```

Other example: 

```py

>>> number = 1024
>>> f"{number:#0x}"  # using integer format specifier
'0x400'
>>> foo = "bar"
>>> f"{ foo = }" # preserves whitespace
" foo = 'bar'"
>>> line = "The mill's closed"
>>> f"{line = }"
'line = "The mill\'s closed"'
>>> f"{line = :20}"
"line = The mill's closed   "
>>> f"{line = !r:20}"
'line = "The mill\'s closed" 
```


A consequence of sharing the same syntax as regular string literals is that characters in the replacement fields must not conflict with the quoting used in the outer formatted string literal:

```py
f"abc {a["x"]} def"    # error: outer string literal ended prematurely
f"abc {a['x']} def"    # workaround: use different quoting
```

To include a value in which a backslash escape is required, create a temporary variable.

```py
>>> newline = ord('\n')
>>> f"newline: {newline}"
'newline: 10'
```