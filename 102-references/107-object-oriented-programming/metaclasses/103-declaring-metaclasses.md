# Declaring Metaclasses

The classes are created by the **type** class by default. To tell Python to create a class with a custom metaclass instead, you simply need to declare a metaclass to intercept the normal instance creation call in a user-defined class.

### In 3.X

It list the desired metaclass as a *keyword* argument in the **class** header:

```py
class Spam(metaclass=Meta)          # 3.X version (only)
```

Inheritence superclasses can be listed in the header as well. In the following, for exaple, the new class **Spam** inherits from superclass **Eggs**, but is also an instance of and is created by metaclass **Meta**:

```py
class Spam(Eggs, metaclass=Meta):           # Normal supers OK: must list first
```

In this form, superclasses must be listed before the metaclass; in effect, the ordering rules used for keyword arguments in function calls apply here.

### Metaclass Dispatch in Both 3.X

When a specific metaclass in declared per the prior section's syntax, the call to create the **class** object run at the end of the **class** statement in modified to invoke the *metaclass* instead of the **type** default:

```py
class = Meta(classname, superclasses, attributedict)
```

and because the metaclass is a subclass of **type**, the **type** class's `__call__` delegates the calls to create and initialize the new **class** object to the metaclass, it it defines custom  versions of the methods:

```py
Meta.__new__(Meta, classname, superclasses attributedict)
Meta.__init__(class, classname, superclasses, attributedict)
```

To demonstrate:

```py
class Spam(Eggs, metaclass=Meta):               # Inherits from Eggs, instance of Meta
    data = 1                                    # Class data attribute
    def meth(self, arg):                        # Class method attribute
        return self.data + arg
```

At the end of this **class** statement, Python internally runs the following to create the **class** object--again, a call you could make manually too, but automatically run by Python's class machinery:

```py
Spam = Meta("Spam", (Eggs,), {"data": 1, "meth": meth, "__module__": "__main__"})
```

If the metaclass defines its own versions of `__new__` or `__init__`, they will be invoked in turn during this call by the inherited **type** class's `__call__` method, to create and initialize the new class. The new effect is to automatically  run methods the metaclass provides, as part of the class construction process.