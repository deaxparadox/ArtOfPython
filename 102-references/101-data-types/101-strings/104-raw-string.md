# Raw Strings

If you dont' want characters prefaced by `\` to be interpreted as special characters. you can use *raw string* by adding an `r` before the first quote:

```py
>>> print('C:\some\name')  # here \n means newline!
C:\some
ame
>>> print(r'C:\some\name')  # note the r before the quote
C:\some\name
```

Raw string are used with the string which shouldn't be formated:

```python
>>> r"this string should not be formated\n"
'this string should not be formated\\n'

```