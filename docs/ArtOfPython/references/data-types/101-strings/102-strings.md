# Strings

Python String are regular text strings, which can be expressed in several ways. They can be enclosed in singles quotes (`'...'`) or doubles quotes (`"..."`).

```python
>>> # single quotes
>>> 'spam eggs'
'spam eggs'
>>> 
```


### r"" raw string

- `r''`, If you don't want characters prefaced by `\` to be interpreted as special characters, you can use *raw strings* by adding an `r` before the first quote:

```python
>>> print('\some\name')  # here \n means newline!
\some
ame
>>> print(r'\some\name')  # note the r before the quote
\some\name
```

## Multple line string `"""..."""` and `'''...'''`.

```py
>>> mls = """line1
... line2
... line3"""
>>> 
>>> mls
'line1\nline2\nline3'
>>> 
>>> print(mls)
line1
line2
line3
>>> 
```

## Conacatenation `+`

```python
>>> s = 'un' + 'ium'
>>> s
'unium'
>>> print(s)
unium
>>> 
```

- Two or more *string literals* (i.e. the ones enclosed between quotes) next to each other automatically concatenated:

```python
>>> 
>>> 'every' 'where' 'linux'
'everywherelinux'
>>> 
```

- You can also put several strings within parentheses to have them joined together:

```python
>>> text = ('Put several strings within parentheses '
...     'to have them joined together.')
>>> text
'Put several strings within parentheses to have them joined together.'
```

- This only works with two literals though, not with variables or expressions:

```python
prefix = 'Py'
prefix 'thon'  # can't concatenate a variable and a string literal
  File "<stdin>", line 1
    prefix 'thon'
           ^^^^^^
SyntaxError: invalid syntax
('un' * 3) 'ium'
  File "<stdin>", line 1
    ('un' * 3) 'ium'
               ^^^^^
SyntaxError: invalid syntax
```

- If you want to concatenated variables or variables and a litrals, use `+`:

```python
>>> prefix = "Py"
>>> prefix + "thon"
'Python'
```

## Repetition `*`

```python
>>> 2 * s
'uniumunium'
>>> 3 * s
'uniumuniumunium'
>>> 
```