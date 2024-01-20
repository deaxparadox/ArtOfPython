# Tracing interfaces with class decorators


Class decorators provide an alternative convenient way to code this `__getattr__` technique to wrap an entire inteface.

```py
class Wrapper:
    def __init__(self, object):
        self.wrapped = object           # Save object
    def __getattr__(self, attrname):
        print("Trace:", attrname)               # Trace fetch
        return getattr(self.wrapped, attrname)  # Delegate fetch
```

The following **Wrapper** class can be coded as a class decorator that triggers wrapped instance creation, instead of passing a premade instance into the wrapper's constructor (also augmented here to support keyword augments with ****kwargs** and to count the number of accesses made to illustrate changeable state):

```py

def Tracer(aClass):                                 # On @ decorator
    class Wrapper:
        def __init__(self, *args, **kwargs):        # On instance creation
            self.fetches = 0
            self.wrapped = aClass(*args, **kwargs)  # Use enclosing scope name
        def __getattr__(self, attrname):
            print("Trace:", attrname)               # Catches  all but own attrs
            self.fetches += 1
            return getattr(self.wrapped, attrname)  # Delegate to wrapped obj
    return Wrapper

if __name__ == "__main__":
    @Tracer
    class Spam:                             # Spam = Tracer(Spam)
        def display(self):                  # Spam is reboud to Wrapper
            print("Spam!" * 8)
    
    @Tracer
    class Person:                                           # Person = Tracer(Person)
        def __init__(self, name, hours, rate) -> None:      # Wrapper remembers Person
            self.name = name 
            self.hours = hours
            self.rate = rate
        def pay(self):                          # Access outside class traced
            return self.hours * self.rate       # In-method access not traced
        
    food = Spam()                   # Triggers Wrapper
    food.display()                  # Triggers __getattr__
    print([food.fetches])

    bob = Person("Bob", 40, 50)         # bob is really a Wrapper
    print(bob.name)                     # Wrapper embeds a Person
    print(bob.pay())

    print("")
    sue = Person("Sue", rate=100, hours=60)     # sue is a different Wrapper
    print(sue.name)                             # with a different Person
    print(sue.pay())

    print(bob.name)                             # bob has different state
    print(bob.pay())
    print([bob.fetches, sue.fetches])           # Wrapper attrs not traced
```

In function decorators, we looked at decorators that enabled us to trace and time calls to a given function or method.

In contrast, by intercepting instance creation calls, the class decorators here allows us to trace an entire object interface--that is, accessed to nay of the instance's attributes.

```bash
$ python interfacetracer.py 
Trace: display
Spam!Spam!Spam!Spam!Spam!Spam!Spam!Spam!
[1]
Trace: name
Bob
Trace: pay
2000

Trace: name
Sue
Trace: pay
6000
Trace: name
Bob
Trace: pay
2000
[4, 2]
```

Notice how there is one **Wrapper** class with state retention per decoration, generate by the nested *class* statement in the Tracer function, and how each instance get its own fetches counter by virtue of generating a new **Wrapper** instance.

[<<< Tracing Object Interfaces](102-tracing-object-interfaces.md) ... [Applying class decorators to built-in types >>>](104-applying-class-decorators-to-builtin-types.md)