# Overloading class creation calls with metaclasses

Since they participate in normal OOP mechanics, it's also possible for metaclasses to catch the creation call at the end of a **class** statement directly, by redefining the **type** object's `__call__`. The redefinitions of both `__new__` and `__call__` must be carefull to call back to their defaults in *type* it they mean to make a class in the end, and `__call__` must invoke `type` to kick off the other two here:

```py
# Classes can catch calls to (but built-ins look in metas, not super!)

class SuperMeta(type):
    def __call__(meta, classname, supers, classdict):
        print("In SuperMeta.call: ", classname, supers, classdict, sep='\n', end="\n\n")
        return type.__call__(meta, classname, supers, classdict)
    
    def __init__(Class, classname, supers, classdict):
        print("In SuperMeta init: ", classname, supers, classdict, sep="\n...", end="\n\n")
        print("...init class object: ", list(Class.__dict__.keys()))

print("Making metaclass")
class SubMeta(type, metaclass=SuperMeta):
    def __new__(meta, classname, supers, classdict):
        print("In SubMeta.new: ", classname, supers, classdict, sep="\n...", end="\n\n")
        return type.__new__(meta, classname, supers, classdict)
    
    def __init__(Class, classname, supers, classdict):
        print("In Submeta init:", classname, supers, classdict, sep="\n...", end="\n\n")
        print("...init class object:", list(Class.__dict__.keys()))


class Eggs:
    pass 

print("Making class")
class Spam(Eggs, metaclass=SubMeta):          # Invoke SubMeta, instance via SuperMeta.__call__
    data = 1                                
    def meta(self, arg):
        return self.data + arg
    
print("Making instance")
X = Spam()
print("data:", X.data, X.meta(2))
```

This code has some oddities I'll explain in a moment. When run, though, all three redefined methods run in turn for **Spam**. This is again essentially what the **type** object does by default, but there's an additional metaclass call for the metaclass subclass (*metasubclass?*):


```bash
$ python metaclass5.py 
Making metaclass
In SuperMeta init: 
...SubMeta
...(<class 'type'>,)
...{'__module__': '__main__', '__qualname__': 'SubMeta', '__new__': <function SubMeta.__new__ at 0x7fb9ae5fa0e0>, '__init__': <function SubMeta.__init__ at 0x7fb9ae5fa170>}

...init class object:  ['__module__', '__new__', '__init__', '__doc__']
Making class
In SuperMeta.call: 
Spam
(<class '__main__.Eggs'>,)
{'__module__': '__main__', '__qualname__': 'Spam', 'data': 1, 'meta': <function Spam.meta at 0x7fb9ae5fa200>}

In SubMeta.new: 
...Spam
...(<class '__main__.Eggs'>,)
...{'__module__': '__main__', '__qualname__': 'Spam', 'data': 1, 'meta': <function Spam.meta at 0x7fb9ae5fa200>}

In Submeta init:
...Spam
...(<class '__main__.Eggs'>,)
...{'__module__': '__main__', '__qualname__': 'Spam', 'data': 1, 'meta': <function Spam.meta at 0x7fb9ae5fa200>}

...init class object: ['__module__', 'data', 'meta', '__doc__']
Making instance
data: 1 3
```

This example is complicated by the fact that it overrides a methods invoked by a *built-in* operation--in this case, the call run automatically to create a class. Metaclasses are used to create class objects, but only generate instances of themselves when callled in a metaclass role. Because of this, name lookup with metaclasses may be somewhat different than what we ar accustomed to. The `__call__` method, for example, is looked up by built-ins in the class (a.k.a. type) of an object; for metaclasses, this means that metaclass of a metaclass!

Metaclasses also *inherit* names from other metaclasses normally, but as for normal classes, this seems to apply to *explicit* name fetches only, not to the *implicit* lookup of names for built-in operations such as calls. The latter appears to look in the metaclass's *class*, available in its `__class__` link--which is either the default **type** or a metaclass. This is the same built-ins routing issue we've seen so often in this book for normal class instances. The **metaclass** in **SubMeta** is required to set this link though this also kicks off a metaclass construction step for the metaclass itself.

Trace the invocations in the output. **SuperMeta**'s `__call__` method is not run for the call to **SuperMeta** when making **SubMeta** (this goes to type instead), but is run for the **SubMeta** call when making **Spam**. Inheriting normally from **SuperMeta** does not suffice to catch **SubMeta** calls, and for reasons  we'll see later is actually the wrong thing to do for operator overloading methods: **SuperMeta**'s `__call__` is then acquired by **Spam**, causing **Spam** instance creation calls to fail before by instance is every created.

Here's an illustration of the issue in simple terms--a normal superclass is skipped for built-ins, but not for *explicit* fetches and callls, the latter relying on normal attribute name inheirtence:

```py
class SuperMeta(type):
    def __call__(meta, classname, supers, classdict):           # By name, not built-in
        print("In SuperMeta.calll: ", classname)
        return type.__call__(meta, classname, supers, classdict)
    
class SubMeta(SuperMeta):                                   # Created by type default
    def __init__(Class, classname, supers, classdict):      # Overrides type.__init__
        print("In SubMeta init: ", classname)

print(SubMeta.__class__)
print([n.__name__ for n in SubMeta.__mro__])
print()
print(SubMeta.__call__)              # Not a class descriptor if found by name
print()
SubMeta.__call__(SubMeta, "xxx", (), {})    # Explicit calls work: class inheirtence
print()
SubMeta("yyy", (), {})          # But implicit built-in calls do not: type
```

```bash
$ python metaclass5b.py 
<class 'type'>
['SubMeta', 'SuperMeta', 'type', 'object']

<function SuperMeta.__call__ at 0x7fe3c6d35ea0>

In SuperMeta.calll:  xxx
In SubMeta init:  xxx

In SubMeta init:  yyy
```

Of course, this specific example is a special case: catching a built-in run on a metaclass, a likely rare usage related to `__call__` here. But it underscores a core asymmetry and apparent inconsistency: *normal attribute inheritence is not fully used for built-in dispatch*--for both instnaces and classes.