# Primer

### Simple Example: A descriptor that returns a contant

The Ten class is a descriptor who `__get__()` method always returns the constant `10`:

```py
In [1]: class Ten:
   ...:     def __get__(self, obj, objtype=None):
   ...:         return 10
   ...: 
```

- To use the descriptor, it must be stored as a class variable in another class:

```py
In [2]: class A:
   ...:     x = 5                   # Regular class attribute
   ...:     y = Ten()               # Descriptor instance
   ...: 
```

- An interactive session shows the difference between normal attribute lookup and descriptor lookup:

```py
In [3]: a = A()                 # Make an instance of class A

In [4]: a.x                     # Normal attribute lookup
Out[4]: 5

In [5]: a.y                     # Descriptor lookup
Out[5]: 10

```


In the `a.x` attribute lookup, the dot operator finds `'x': 5` in the class dictionary. In the `a.y` lookup, the dot operator finds a descriptor instance, recognized by its `__get__` method. Calling that method returns `10`.

Note that the value `10` is not stored in either the class dictionary or the instance dictionary. Instead, the value `10` is computed on demand.

This example shows how a simple descriptor works, but it isn’t very useful. For retrieving constants, normal attribute lookup would be better.