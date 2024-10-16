# Type checking 

To check of type of object, you can use the builtin `type()`  function.

For example, let's have a variable `a`, binded to `1`, we have to find the type of this variable.

```py
>>> a = 1
>>> type(a)
<class 'int'>
>>> 
```

We get type as `int`. Therefore, like this you can check type of any variable (or object).

### Typecasting

*Type-Casting* refers to converting a object from a type to another. Let's have a variable binded to the `'234'`, we are going to convert this to `int`, using `int()` function:

```py
>>> 
>>> n = '234'
>>> type(n)
<class 'str'>
>>> 
>>> n = int(n)
>>> type(n)
<class 'int'>
>>> 
```