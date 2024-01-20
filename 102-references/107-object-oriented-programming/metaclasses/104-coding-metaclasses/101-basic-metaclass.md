# A Basic Metaclass

The simplest metaclass can be coded is simply by subclassing **type** with a `__new__` method that creates the class object by running the default version in the **type**. A metaclass `__new__` like this is run by the `__call__` method inherited from **type**; it typically performs whatever customization is required and calls the **type** superclass's `__new__` method to create and return the new class object:

```py
In [6]: class Meta(type):
   ...:     def __new__(meta, classname, supers, classdict):
   ...:         # Run by inherited type.__call__
   ...:         return type.__new__(meta, classname, supers, classdict)
   ...: 

```

This metaclass doesn't really do anything, but it demonstrates the way a metaclass taps into the metaclass hook to customize--because the metaclass is called at the end ofthe class statement, and because the type object's `__call__` dispatches to the `__new__` and `__init__` methods, code we provide in these methods can manage all the classes created from the metaclass.

Here's is an example in action again, with prints added to the metaclass and the file at large to trace:

```py
class MetaOne(type):
    def __new__(meta, classname, supers, classdict):
        print("In MetaOne.new", meta, classname, supers, classname, classdict, end="\n")
        return type.__new__(meta, classname, supers, classdict)
    
class Eggs:
    pass 

print("making class")
class Spam(Eggs, metaclass=MetaOne):            # Inherits from Eggs, instance of MetaOne
    data = 1                                    # Class data attribute
    def meta(self, arg):                        # Class method attribute
        return self.data + arg
    
print("making instance")
X = Spam()
print('data:', X.data, X.meta(2))
```

Here, **Spam** inherits from **Eggs** and is an instance of **MetaOne**, but X is an instance of and inehrits from **Spam**. When this code is run with Python 3.X, notice how the metaclass is invoked at the *end* of the **class** statement, before we every make an instance--metaclasses are for processing *classes*, and classes are not processing normal *instances*:

```bash
$ python -m metaclass1
making class
In MetaOne.new
<class '__main__.MetaOne'>
Spam
(<class '__main__.Eggs'>,)
Spam
{'__module__': '__main__', '__qualname__': 'Spam', 'data': 1, 'meta': <function Spam.meta at 0x7f634ca04310>}
making instance
data: 1 3
```