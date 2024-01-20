# Managing Functions and Classes Directly

Decorators work by running new functions and classes through decorator code, they can also be manage function and class object themselves, not just later calls made to them.

```py
from __future__ import print_function
import os
import sys



registry = {}
def register(obj):                      # Both class and func decorator
    registry[obj.__name__] = obj        # Add to registry
    return obj                          # Return obj itself, not a wrapper


@register
def spam(x):
    return x ** 2                       # spam = register(spam)

@register
def ham(x):
    return x ** 3

@register
class Eggs:                             # Eggs = register(Eggs)
    def __init__(self, x):
        self.data = x ** 4 
    def __str__(self) -> str:
        return str(self.data)

print("Registry:")
for name in registry:
    print(name, "=>", registry[name], type(registry[name]))

print("\nManual calls:")                                    # Invoke objects mannually
print(spam(2))                                              # Later calls not intercepted
print(ham(2))
X = Eggs(2)
print(X)

print("\nRegistry calls:")
for name in registry:
    print(name, "=>", registry[name](2))                    # Invoke from registry
 
sys.exit(0)
```

When this code is run the decorated objects are added to the registry by name, but they still work as originally coded when they's called later, without being routed through a wrapper layer.

If fact, our objects can be run both mannually form inside the registry table:

```bash

Registry:
spam => <function spam at 0x7fb671a68ae0> <class 'function'>
ham => <function ham at 0x7fb671a68b80> <class 'function'>
Eggs => <class '__main__.Eggs'> <class 'type'>

Manual calls:
4
8
16

Registry calls:
spam => 4
ham => 8
Eggs => 16
```

----------

Consider the following function decorators--they assign function attributes to record information for later use by an API, but they do not insert a wrapper layer to intercept later calls:

```py
>>> 
>>> def decorate(func):
...     func.marked = True
...     return func
... 
>>> 
>>> @decorate
... def spam(a, b):
...     return a + b
... 
>>> 
>>> spam.marked
True
>>> 
>>> 
>>> def annotate(text):
...     def decorate(func):
...             func.label = text
...             return func 
...     return decorate
... 
>>> 
>>> @annotate('spam data')
... def spam(a, b):
...     return a + b
... 
>>> spam(1, 2), spam.label
(3, 'spam data')
>>> 
```

Such decorators augments functions and classes directly, without catching later calls to them.