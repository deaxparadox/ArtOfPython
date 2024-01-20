# Generalizing for Public Declarations, Too


Class decorator with Private and Public attribute declarations. 

Controls external access to attributes stored on an instance, or Inherited by it from its classes. Private declares attribute names that cannot be fetched or assigned outside the decorated class, and Public declares all the name that can.

```py
from typing import Any


traceMe = False
def trace(*args):
    if traceMe: print("[" + "".join(map(str, args)) + "]")

def accessControl(failIf):
    def onDecorator(aClass):
        class onInstance:
            def __init__(self, *args, **kwargs):
                self.__wrapped = aClass(*args, **kwargs)
            def __getattr__(self, attr):
                trace("get: ", attr)
                if failIf(attr):
                    raise TypeError("private attribute fetched: " + attr)
                else:
                    return getattr(self.__wrapped, attr)
            def __setattr__(self, attr, value) -> None:
                trace('set:', attr, value)
                if attr == "_onInstance__wrapped":
                    self.__dict__[attr] = value
                elif failIf(attr):
                    raise TypeError("private attribute change: " + attr)
                else:
                    setattr(self.__wrapped, attr, value)
        return onInstance
    return onDecorator

def Private(*attributes):
    return accessControl(failIf=(lambda attr: attr in attributes))

def Public(*attributes):
    return accessControl(failIf=(lambda attr: attr not in attributes))

```

```py
In [2]: from access2 import Private, Public
```

```py
In [3]: @Private('age')
   ...: class Person:
   ...:     def __init__(self, name, age):
   ...:         self.name = name
   ...:         self.age = age
   ...: 

In [4]: X = Person("Bob", 40)

In [5]: X.name
Out[5]: 'Bob'

In [6]: X.name = "Sue"

In [7]: X.name
Out[7]: 'Sue'

In [8]: X.age
TypeError: private attribute fetched: age

In [9]: X.age = "Tom"
TypeError: private attribute change: age

```

```py
In [10]: @Public('name')
    ...: class Person:
    ...:     def __init__(self, name, age):
    ...:         self.name = name
    ...:         self.age = age
    ...: 

In [11]: X = Person("bob", 40)

In [12]: X.name
Out[12]: 'bob'

In [13]: X.name = "Sue"

In [14]: X.name
Out[14]: 'Sue'

In [15]: X.age
TypeError: private attribute fetched: age

In [16]: X.age = "Tom"
TypeError: private attribute change: age

In [17]: 
```