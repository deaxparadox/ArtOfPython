# `__name__` class attributes

The `__name__` attribute holds the name of the class, function, method, description or generator instance.

### class `__name__` attribute

The `__name__` attribute hold the name of the class. Let's create a simple class, perform operation on this attributes.

```py
In [3]: class A:
   ...:     pass
   ...: 

In [4]: A.__name__
Out[4]: 'A'

In [5]: 
```

As you can see, Python automatically create the `__name__` attribute for you. You can also check the name of this attribute by instance of the following class.

For fetching the name of class via instance, there is additional attribute that you need to reference in between `a` and `__name__`, that attribute is `__class__`. Let's see an example of it:

```py
In [31]: a = A()

In [32]: a.__class__.__name__
Out[32]: 'A'

In [33]: 
```

### Method `__name__` attribute

The method of class also assigned name attribute.

```py
In [35]: class A:
    ...:     def hello(self):
    ...:         pass
    ...: 

In [36]: 

In [36]: A.hello
Out[36]: <function __main__.A.hello(self)>

In [37]: A.hello.__name__
Out[37]: 'hello'
```

or

```py
In [38]: a = A()

In [39]: a.hello.__name__
Out[39]: 'hello'

In [40]: 
```


### Function `__name__` attribute

Similar to class name attribute, when we declare a function, the function is also assign a name while declaration. Let's see an example of it.

```py
In [33]: def hello():
    ...:     pass
    ...: 

In [34]: hello.__name__
Out[34]: 'hello'

In [35]: 
```

### Generator `__name__` attribute

Generator also assigned `__name__` attribute.

```py
In [40]: def hello():
    ...:     yield 1
    ...: 

In [41]: h = hello()

In [42]: h.__name__
Out[42]: 'hello'

In [43]: type(h)
Out[43]: generator

In [44]: 
```

### Descriptor `__name__` attribute

```py

In [56]: class Descriptor:
    ...:     def __get__(self, obj, objtype=None):
    ...:         return "Hello"
    ...: 

In [57]: class A:
    ...:     h = Descriptor()
    ...: 

In [58]: a = A()

In [59]: a
Out[59]: <__main__.A at 0x7fadeaba09e0>

In [60]: a.h
Out[60]: 'Hello'

In [63]: a.h.__class__.__name__
Out[63]: 'str'

In [64]: 
```