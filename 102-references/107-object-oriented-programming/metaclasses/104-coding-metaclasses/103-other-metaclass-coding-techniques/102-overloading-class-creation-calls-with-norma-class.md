# Overloading class creation calls with normal classes

Because the normal class instances can respond to call operations with operator overloading, they can serve in some metaclasses roles too. The output of the following is similar to the prior class-based version, but it's based on a simple class-one that doesn't inherit from **type** at all, and provides a `__call__` for its instances that catches the metaclass call using normal operator overloading. Note that `__new__` and `__init__` must have different names here, or else they will run when the **Meta** instance is *created*, not when it is later called inthe role of metaclass:

```py
# A normal class instance can serve as a metaclass to.

class MetaObj:
    def __call__(self, classname, supers, classdict):
        print("In MetaObj.call: ", classname, supers, classdict, sep="\n", end="\n\n")
        Class = self.__New__(classname, supers, classdict)
        self.__Init__(Class, classname, supers, classdict)
        return Class 
    
    def __New__(self, classname, supers, classdict):
        print("In MetaObj.new: ", classname, supers, classdict, sep="\n", end="\n\n")
        return type(classname, supers, classdict)
    
    def __Init__(self, Class, classname, supers, classdict):
        print("In MetaObj.init: ", classname, supers, classdict, sep='\n', end="\n\n")
        print("...init class object: ", list(Class.__dict__.keys()))

class Eggs:
    pass 

print("Making class")
class Spam(Eggs, metaclass=MetaObj()):          # Metaobj is normal class instance
    data = 1                                    # Called at end of statement
    def meta(self, arg):
        return self.data + arg
    
print("Making instance")
X = Spam()
print("data:", X.data, X.meta(2))
```

When run, the three methods are dispatched via the normal instance's `__call__` inheirtence from its normal class, but without any dependence on **type** dispatch mechanics or sem

```bash
$ python metaclass4.py 
Making class
In MetaObj.call: 
Spam
(<class '__main__.Eggs'>,)
{'__module__': '__main__', '__qualname__': 'Spam', 'data': 1, 'meta': <function Spam.meta at 0x7f2663086200>}

In MetaObj.new: 
Spam
(<class '__main__.Eggs'>,)
{'__module__': '__main__', '__qualname__': 'Spam', 'data': 1, 'meta': <function Spam.meta at 0x7f2663086200>}

In MetaObj.init: 
Spam
(<class '__main__.Eggs'>,)
{'__module__': '__main__', '__qualname__': 'Spam', 'data': 1, 'meta': <function Spam.meta at 0x7f2663086200>}

...init class object:  ['__module__', 'data', 'meta', '__doc__']
Making instance
data: 1 3
```

In fact, we can use normal superclass inheritence to acquire the call interpretor in this coding model--the superclass here is serving essentially the same role as **type**, at least in terms of metaclass dispatch:

```py
# Instances inherit from classes and their supers normally

class SuperMetaObj:
    def __call__(self, classname, supers, classdict):
        print("In SuperMetaObj.call: ", classname, supers, classdict, sep="\n", end="\n\n")
        Class = self.__New__(classname, supers, classdict)
        self.__Init__(Class, classname, supers, classdict)
        return Class

class SubMetaObj(SuperMetaObj):        
    def __New__(self, classname, supers, classdict):
        print("In SubMetaObj.new: ", classname, supers, classdict, sep="\n", end="\n\n")
        return type(classname, supers, classdict)
    
    def __Init__(self, Class, classname, supers, classdict):
        print("In SubMetaObj.init: ", classname, supers, classdict, sep='\n', end="\n\n")
        print("...init class object: ", list(Class.__dict__.keys()))



class Eggs:
    pass 

print("Making class")
class Spam(Eggs, metaclass=SubMetaObj()):          # Invoke Sub instance via Super.__call__
    data = 1                                
    def meta(self, arg):
        return self.data + arg
    
print("Making instance")
X = Spam()
print("data:", X.data, X.meta(2))
```

```bash
$ python metaclass4-super.py 
Making class
In SuperMetaObj.call: 
Spam
(<class '__main__.Eggs'>,)
{'__module__': '__main__', '__qualname__': 'Spam', 'data': 1, 'meta': <function Spam.meta at 0x7f56ca86e050>}

In SubMetaObj.new: 
Spam
(<class '__main__.Eggs'>,)
{'__module__': '__main__', '__qualname__': 'Spam', 'data': 1, 'meta': <function Spam.meta at 0x7f56ca86e050>}

In SubMetaObj.init: 
Spam
(<class '__main__.Eggs'>,)
{'__module__': '__main__', '__qualname__': 'Spam', 'data': 1, 'meta': <function Spam.meta at 0x7f56ca86e050>}

...init class object:  ['__module__', 'data', 'meta', '__doc__']
Making instance
data: 1 3
```

Although such alternative forms work, most metaclasses get their work done by redifining the **type** superclass's `__new__` and `__init__`; in practice, this is usually as much control as is required, and it's often simple than other schemes. Moreover, metaclasses have access to additional tools, such as class *methods*, which can influence clas behavior more directly than some other schemes.