# Strings Concatenation

Strings can be concatented using `+` operator:

```py
>>> "hello " + "world"
'hello world'
>>> 
```

Two or more *string literal* next to each other are automatically concatenated:

```py
>>> "hello " "world"
'hello world'
>>> 
```

Next feature is use full when you want to break long strings:

```py
>>> text = ('Put several strings within parentheses '
...         'to have them joined together.')
>>> text
'Put several strings within parentheses to have them joined together.'
```


If you want to concatenate variables or a variable and a literal, use `+`:

```py
>>> # variable h
>>> h = "hello "
>>> 
>>> # concatenating variable and literal
>>> h + 'world'
'hello world'
>>> 
```