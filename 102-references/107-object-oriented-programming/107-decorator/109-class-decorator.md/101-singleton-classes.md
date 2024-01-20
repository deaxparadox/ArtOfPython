# Singleton Classes

Becuase class decorators may intercept instance createion calls, they may be used to either manage al lthe instances of a class, or augment the interfaces of those instances.

To demonstrate, here's a first class decorator example that does the former--managing all instances of a class. This code implements the classic *singleton* coding pattern, where at most one instance of a class ever exists. Its **singleton** function defines and returns a function for managing instances, and the @ syntax automatically wraps up a subject class in this function:

```py
instances = {}

def singleton(aClass):                  # On @ decoration
    def onCall(*args, **kwargs):        # On instance creation
        if aClass not in instances:     # One dict entry per class
            instances[aClass] = aClass(*args, **kwargs)
        return instances[aClass]
    return onCall
```

To use this, decorate the classes for which you want to enforce a single-instance model:

```py
@singleton                                              # Person = singleton(Person)
class Person:                                           # Rebinds Person to onCall
    def __init__(self, name, hours, rate) -> None:      # onCall remembers Person
        self.name = name 
        self.hours = hours
        self.rate = rate
    def pay(self):
        return self.hours * self.rate
    
@singleton                          # Spam = singleton(Spam)
class Spam:                         # Rebinds Spam to onCall
    def __init__(self, val):        # onCall remembers Spam
        self.attr = val

bob = Person("Bob", 40, 10)         # Really calls onCall
print(bob.name, bob.pay())

sue = Person("Sue", 50, 20)         # Same, single object
print(sue.name, sue.pay())

X = Spam(val=42)                    # One Person, one Spam
Y = Spam(99)
print(X.attr, Y.attr)
```

Now, when the **Person** and **Spam** class is later used to create an instance, the wrapping logic layer provided by the decorator routes instances construction calls to **onCall**, which in turn ensures a single instances per class, regardless of how may construction calls are made.

```bash
Bob 400
Bob 400
42 42
```

### Coding Alternatives

You can code a more self-contained solution here if you're able to use the **nonlocal** statement to change scope names. The following alternative achieves an indentical effect, by using one *enclosing scope* per class, instead of one global table entry per class. It works the same, but it does not depend on names  in the global scope outside the decorator:

```py

def singleton(aClass):                  # On @ decoration
    instance = None
    def onCall(*args, **kwargs):        # On instance creation
        nonlocal instance              # 3.X and later nonloca
        print(instance)
        if instance == None:     
            instance = aClass(*args, **kwargs)     # One scope per class
        return instance
    return onCall
```


----------

```py
def singleton(aClass):                                  # On @ decoration
    def onCall(*args, **kwargs):                        # On instance creation
        if onCall.instance == None:
            onCall.instance = aClass(*args, **kwargs)   # One function per class
        return onCall.instance
    onCall.instance = None
    return onCall
```

----------

```py

class singleton:                    
    def __init__(self, aClass):                             # On @ decoration
        self.aClass = aClass
        self.instance = None
    def __call__(self, *args, **kwargs):                    # On instance creation
        if self.instance == None:   
            self.instance = self.aClass(*args, **kwargs)    # One instance per class
        return self.instance
```

To make this decorator a fully general-purpose tool, choose one, store it in an import module file, and indent the self-test code under a **__name__**

[<<<](README.md) ... [Tracing Object Interfaces >>>](102-tracing-object-interfaces.md)