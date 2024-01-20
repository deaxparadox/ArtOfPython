# Inheritance and Instance

Because metaclasses are specified in similar ways to inheritance superclasses, they can be a bit confusing at first glance. A few key points should help summarize and clarify the model:

1. Metaclasses inherit from the **type** class (usually)
    
    - Although they have a special role, metaclasses are coded with **class** statements and follow the usual OOP model in Python. For example, as subclasses of **type**, they can redefine the type object's methods, overriding and customizing them as needed.
    - Metaclasses typically redefine the **type** class's `__new__` and `__init__` to customize class creation and initialization.
    - Although it's less common, they can also redefine `__call__` if they wish to catch the end-of-class creation call directly, and can even be simple functions or other callables that return arbitrary objects, instead of **type** subclasses.

2. Metaclass declarations are inherited by subclass

    - The **metaclass=M** declaration in a user-defined class is **inherited** by the class's normal subclasses, too, so the metaclass will run for the construction of each class that inherits this specification in a superclass inheritance chain.

3. Metaclass attributes are not inherited by class instances

    - Metaclass declarations specify an **instance** relationship, which is not the same as what we've called inheritance thus far. Because classes are instances of metaclasses, the behavior defined in a metaclass applies to the class, but not the class's later instances.
    - Instances obtain behavior from their classes and superclasses, but not from any metaclasses. Technically, attribute inheritance for normal instances usually searches on the `__dict__` dictionaries of the instance, its class, and all its superclasses; metaclasses are *not* included in inheritance lookup for normal instances.

4. Metaclass attributes are acquired by classes

    - By contrast, classes *do* acquire methods of their metaclasses by virtue of the instance relationship. This is a source of class behavior that processes classes themselves.
    - Technically, classes acquire metaclass attributes through the class's `__class__` link just as normal instances acquire names from their class, but inheritance via `__dict__` search is attempted first: when the same name is available to a class in *both* a metaclass and a superclass, the superclass (inheritance) version is used instead of that on a metaclass (instance).
    - The class's `__class__`, however, is not followed for its own instances: metaclass attributes are made available to their instances classes, but not to instances of those instances classes.

To illustrate all these points, consider the following example:


```py
class MetaOne(type):
    def __new__(meta, classname, supers, classdict):        # Redefine type method
        print("In MetaOne.new: ", classname)
        return type.__new__(meta, classname, supers, classdict)
    def toast(self):
        return "toast"
    
class Super(metaclass=MetaOne):         # Metaclass inherited by subs too
    def spam(self):                     # MetaOne run twice for two classe
        return "spam"
    
class Sub(Super):                   # Superclass: inheritence versus instance
    def eggs(self):                 # Classes inherit from superclasses
        return "eggs"               # But not from metaclasses
```

When this code is run (as a script or module), the metaclass handles construction of *both* client classes, and *instances* inherit class attributes but *not* metaclass attributes:

```py
In [26]: from metainstance import *     # Run class statements: metaclass run twice
In MetaOne.new:  Super
In MetaOne.new:  Sub

In [27]: X = Sub()              # normal instance of user-defined class

In [28]: X.eggs()               # Inherited from Sub
Out[28]: 'eggs'

In [29]: X.spam()               # Inherited from Super
Out[29]: 'spam'

In [30]: X.toast()              # Not inherited from metaclass
---------------------------------------------------------------------------
AttributeError                            Traceback (most recent call last)
Cell In[30], line 1
----> 1 X.toast()
```

By contrast, *classes* both inherit names from their superclasses, and acquire names from their metaclass (which in this example is *itself* inherited from superclass):

```py
In [32]: 

In [32]: Sub.eggs(X)            # Own method
Out[32]: 'eggs'

In [33]: Sub.spam(X)            # Inherited from Super
Out[33]: 'spam'

In [34]: Sub.toast()            # Acquired from metaclass
Out[34]: 'toast'

In [35]: Sub.toast(X)           # Not a normal class metho
---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)
Cell In[35], line 1
----> 1 Sub.toast(X)

TypeError: MetaOne.toast() takes 1 positional argument but 2 were given

In [36]: 
```

Notice how the last of the proceeding calls fails when we pass in an instance, because the name resolves to a metaclass method, not a normal class method. In fact, both the object you fetch a name from its source become crucial here. Methods acquired from metaclasses are bound to the subject *class*, while methods from normal classes are *unbound* it fetched through the class but *bound* when fetched through the instance:

```py
In [36]: Sub.toast()
Out[36]: 'toast'

In [37]: Sub.spam
Out[37]: <function metainstance.Super.spam(self)>

In [38]: Sub.toast
Out[38]: <bound method MetaOne.toast of <class 'metainstance.Sub'>>

In [39]: X.spam
Out[39]: <bound method Super.spam of <metainstance.Sub object at 0x7fb97a0169b0>>

In [40]: 
```