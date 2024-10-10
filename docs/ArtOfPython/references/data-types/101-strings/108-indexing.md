# Indexing
 

This techinque is used to accessing individual character from the string, syntax for indexing are square bracket `[index]`, where index is the position of character which we want to fetch. By default indexing start from `0`, from first character.

let's have a simple string literal *hello world*, we are going to store it in variable *s*:

```py
>>> s = 'hello world'
```

To access the first character `h` from the string:

```py
>>> s[0]
'h'
>>> 
```

Similarly we can access `e` index `1`, first `l` index `2`, and so on. 

```py
>>> s[1]
'e'
>>> s[2]
'l'
>>> 
```

What if we want to access the last character from string, we don't known the index of the last character. For calculating the index of last character , we should known the length of the string.

## Length of string

To calculate the length of the string, we can use the *built-in* function *len(string)*:

```py
>>> s = 'hello world'
>>> 
>>> len(s)
11
>>> 
```

## Accessing last character

Now we can find the index of last character in string, we have string and its length from above, to calculate the index, we can use formula: ***length of string - 1***

```py
>>> s = 'hello world'
>>> 
>>> len(s)
11
>>> 
>>> s[len(s) -1]
'd'
>>> # or 
>>> s[11 -1]
'd'
>>> 
>>> # or
>>> 11 - 1
10
>>> s[10]
'd'
>>> 
```

we are able to access last character `d`.


## Negative Indexing

We can also use negative indexing. It start from last character with negative index `-1` till first character with negative index `-length` (-1 * length of string), let's see examples:

```py
>>> 
>>> s[-1]
'd'
>>> s[-2]
'l'
>>> 
>>> s[-11]
'h'
>>> 
```

## Out of range index

If our try to access imaginary character with imagnary index, you will get `IndexError`:


```py
>>> s[99]
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
IndexError: string index out of range
>>> 
```