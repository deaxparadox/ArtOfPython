# Old style string Formatting

String objects have one unique built-in operation: the `%` operator (modulo). This is also known as the string *formatting* or *interpolation operator*. Given format % values (where *format* is a string), `%` conversion specifications in *format* are replaced with zero or more elements of *values*

Let's see a simple example:

```py
>>> "Hello %s" % "World"
'Hello World'
>>> 
```

- to format multiple values, we need to pass them in tuple.


```py
>>> "%s %s" % ("Hello", "World")
'Hello World'
>>> 
```

We can also format using dictonary mapping, in this case we have to use dictionary in place of tuple, and we have to use dictionary key to substibute values:


```py
>>> "%(first)s %(second)s" % {"first": "Hello", "second": "World"}
'Hello World'
>>> 
```