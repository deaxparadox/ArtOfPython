# String Slicing

This techique is used for accessing substring from the given string. Syntax for slicing is `[start:stop;step]`, where `start` represent starting index from where it should start accessing, `stop` represent stop index till where it should accessing, and `step` if you want to jump or skip between character which by default is `1`, it means no jump:

Let have a simple string:

```py
>>> s = "hello world"
```

Let access *hello* from this string:

- so for starting index we have `0` 
- for stoping index we can calculate it, length till `o` is 5, so index of `o` is `4`, but for accessing `o`, we have to provide the index of character after `o`, which is space character with index `5`, because last character is not included in slicing, and we will leave `step` for now.

```py
>>> s[0:5]
'hello'
>>> 
>>> # since we are slicing from start, 
>>> # it's not neccessary to provide starting index.
>>> s[:5]
'hello'
>>> 
```

Now let's use the `step` functionality.

```py
>>> # skip no character
>>> s[:5]
'hello'
>>>
>>> # skip no character
>>> s[:5:1]
'hello'
>>>
>>> # skip one character after accessing each character
>>> s[:5:2]
'hlo'
>>>
>>> # skip two character after accessing each character
>>> s[:5:3]
'hl'
>>> 
```

Let accessing remaining string:

```py
>>> s[5:]
' world'
>>> 
>>> s[5::]
' world'
>>> 
>>> s[5:len(s)]
' world'
>>> 
>>> s[5:len(s):1]
' world'
>>> 
>>> s[5:len(s):2]
' ol'
>>> s[5:len(s):3]
' r'
>>> 
```

Note how the start is always included, and the end always excluded. This makes sure that `s[:i] + s[i:]` is always equal to `s`:

```py
>>> 
>>> s[:5]
'hello'
>>> 
>>> s[5:]
' world'
>>> 
>>> s[:5] + s[5:]
'hello world'
>>> 
```

Since in this example we have been using `5` as index, but you can use any index of your choice.

To get the whole string:

```py
>>> 
>>> s[:]
'hello world'
>>> s[::]
'hello world'
>>>
```


## Out of range

Out of range slice indexes are handled gracefully when used for slicing:

```py
>>> s[:99]
'hello world'
>>> s[99:]
''
>>> s[3:99:]
'lo world'
>>> 
```
