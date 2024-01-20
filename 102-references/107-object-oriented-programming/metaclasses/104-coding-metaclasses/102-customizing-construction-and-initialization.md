# Customizring Construction and Initializatoin

Metaclasses can also tap into the `__init__` protocol invoked by the type object's `__call__`. In genera, `__new__` creates and returns the class object, and `__init__` initializes the already created class passed in as an argument. Metaclasses can use either or both hooks to manage the class at creation time:

```py
class MetaTwo(type):
    def __new__(meta, classname, supers, classdict):
        print("In MetaTwo.new", classname, supers, classdict, sep="\n")
        return type.__new__(meta, classname, supers, classdict)
    
    def __init__(Class, classname, supers, classdict):
        print("In MetaTwo.init", Class, classname, supers, classdict, sep="\n")
        print("...init class object:", list(Class.__dict__.keys()))

class Eggs:
    pass 

print("makeing class")
class Spam(Eggs, metaclass=MetaTwo):        # Inherits from Egs, instance of MetaTwo
    data = 1                                # Class data attribute
    def meth(self, arg):                   # Class method attribute
        return self.data + arg
    
print("making instance")
X = Spam()
print("data:", X.data, X.meth(2))
```

In this case, the class initialization method is run after the class construction method, but both run at the end of the **class** statement before any instances are made. Conversely, an `__init__` is Spam would run at *instance* creation time, and is not affected or run by the metaclass's `__init__`:

```bash
$ python metaclass2.py 
makeing class
In MetaTwo.new
Spam
(<class '__main__.Eggs'>,)
{'__module__': '__main__', '__qualname__': 'Spam', 'data': 1, 'meth': <function Spam.meth at 0x7f8d375da170>}
In MetaTwo.init
<class '__main__.Spam'>
Spam
(<class '__main__.Eggs'>,)
{'__module__': '__main__', '__qualname__': 'Spam', 'data': 1, 'meth': <function Spam.meth at 0x7f8d375da170>}
...init class object: ['__module__', 'data', 'meth', '__doc__']
making instance
data: 1 3
```