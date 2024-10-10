
# Escaping

## Escaping single quotes

If you want to include the *single quote* in our string. It can be done using `\` backslash character.

```py
# escaping single quotes
>>> 'Isn\'t they said'
"Isn't they said"
```

- If you don't escape the single in quote in between your string, you will the get syntax. Because python think you are trying to end the string after `Isn`. 


```python
# not escaping quotes
>>> 'Isn't they said'
  File "<stdin>", line 1
    'Isn't they said'
         ^
SyntaxError: invalid syntax
>>> 
>>> 'Isn\'t they said'
"Isn't they said"
>>> 
```


- So you can escape the single quote.


Another way to add single quote in between your string is, you can used *double quotes* to create string.

```py
>>> "Isn't they said"
"Isn't they said"
>>> 
```

## Escape characters.

### `\n`:newline

- `\n` add a newline to the string.

```python
>>> s = 'First line.\nSecone line'
>>>
>>> print(s)
First line.
Secone line
>>> 
```


### `\t`: tab

`\t` adds tab space between strings.

```py
>>> s = "First line\tSecond line"
>>> s
'First line\tSecond line'
>>> print(s)
First line      Second line
>>> 
```

- to format the *escape character*, you have to use **print()** function.


