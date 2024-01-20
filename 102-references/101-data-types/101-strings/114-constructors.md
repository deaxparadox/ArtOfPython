# Constructor function

## str()

str() is used to create regular string or for converting a type string.

Creating string:

```py
>>> str("this is  a string")
'this is  a string'
>>> 
```

We can convert almost any object to string:

```py
>>> str([13123, 123])           # list to string
'[13123, 123]'
>>> 
>>> str((13123, 123))           # tuple to string
'(13123, 123)'
>>> str({13123, 123})           # dictionary to string
'{123, 13123}'
>>> 
>>> str(123)                    # number to string
'123'
>>> 
```

## You can overload this method in class

`str()` method maps to `__str__()` method in class.

Suppose you have class, it take a number a input, so we will over `__str__()` method, so it return that number as string:

```py
>>> class Stringer:
...     def __init__(self, num):
...             self.num = num
...     def __str__(self):
...             return str(self.num)
... 
>>> s = Stringer(12)
>>> str(s)
'12'
>>> 
```

- Adding a message to method:

```py
>>> class Stringer:
...     def __init__(self, num):
...             self.num = num
...     def __str__(self):
...             return f"Number to string: {str(self.num)}"
... 
>>> s = Stringer(13)
>>> str(s)
'Number to string: 13'
>>> 
```

## repr() function

Return a string containing a printable representation of an object. 

```py
>>> repr("this is  a string")
"'this is  a string'"
>>> 
```

We can convert almost any object to string:

```py
>>> str([13123, 123])           # list to string
'[13123, 123]'
>>> 
>>> str((13123, 123))           # tuple to string
'(13123, 123)'
>>> str({13123, 123})           # dictionary to string
'{123, 13123}'
>>> 
>>> str(123)                    # number to string
'123'
>>> 
```

Similar to constructor function `__str__()` we can implemente  `__repr__()` method for `repr()` function:

```py
class Stringer:
    def __init__(self, num):
        self.num = str(num) 
    def __repr__(self):
        return f"Stringable object: {self.num}"
    

s = Stringer(12)
print(repr(s))

# output 
Stringable object: 12
```