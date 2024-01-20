# Using descriptors to decorate methods

A descriptor is normally a class attribute assigned to an object with a `__get__` method run automatically whenever that attribute is reference and fetched; new-style class **object** derivation is required for descriptors.

```py

In [37]: class Descriptor(object):
    ...:     def __get__(self, instance, owner):
    ...:         ...
    ...: 

In [38]: 

In [38]: class Subject:
    ...:     attr = Descriptor()
    ...: 

In [39]: X = Subject()

In [40]: X.attr             # Roughly runs Descriptor.__get__(Subject.attr, X, Subject)

In [41]: 
```

Descriptors may also have `__set__` and `__del__` access methods.

The descriptor's `__get__` method receives *both* the descriptor class instance and subject class instance when invoked, it's well suited for decorating methods when we need both the descriptor's state and the orginal class instance for disptaching calls.

Consider the following alternative tracing decorator, which also happens to be a descriptor when use for a class-level method:

```py
class tracer(object):                           # A decorator + descriptor
    def __init__(self, func):                   # On @ decorator
        self.calls = 0                          # Save func for later call
        self.func = func 
    def __call__(self, *args, **kwargs):        # On call to original func
        self.calls += 1
        print("call %s to %s" % (self.calls, self.func.__name__))
        return self.func(*args, **kwargs)
    def __get__(self, instance, owner):         # On method attribute fetch
        return wrapper(self, instance)
    
class wrapper:
    def __init__(self, desc, subj) -> None:     # Save both instances
        self.desc = desc                        # Route calls back to deco/desc
        self.subj = subj
    def __call__(self, *args, **kwargs):
        return self.desc(self.subj, *args, **kwargs)        # Runs tracer.__call__
    

@tracer
def spam(a, b, c):                  # spam = tracer(spam0)
    print(a + b + c)                # Uses __call__ only                    


class Person:
    def __init__(self, name, pay):
        self.name = name 
        self.pay = pay 
    
    @tracer
    def giveRaise(self, percent):           # giveRaise = tracer(giveRaise)
        self.pay *= (1.0 + percent)         # Makems giveRaise a descriptor

    @tracer 
    def lastName(self):                     # lastName = tracer(lastName)
        return self.name.split()[-1]
    

if __name__ == "__main__":
    
    spam(1, 2, 3)
    spam(a=4, b=5, c=6)

    print("\nmethods...")
    bob = Person("Bob Smith", 50000)
    sue = Person("Sue Jones", 100000)
    print(bob.name, sue.name)
    sue.giveRaise(.10)                          # Runs __get__ then __call__
    print(int(sue.pay))
    print(bob.lastName(), sue.lastName())       
```

```bash
$ python descriptor1.py 
call 1 to spam
6
call 2 to spam
15

methods...
Bob Smith Sue Jones
call 1 to giveRaise
110000
call 1 to lastName
call 2 to lastName
Smith Jones
```

This works the same as the nested function coding. Its operation varies by usage context:

- Decorated *functions* invoke only its `__call__`, and neven invoke it `__get__`.
- Decorated *methods* invoke its `__get__` first to resolve the method name fetch (on **I.method**); the object returned by `__get__` retains the subject class instance and is then invoked to complete the call expression, thereby trigerring the decorator's `__call__` (on ()).

For example, the test code's call to:

```py
sue.giveRaise(.10)              # Runs __get__and __call__
```

runs `tracer.__get__` first, because the **giveRaise** attribute in the **Person** class has been rebound to a descriptor by the method function decorator. The call expression then triggers the `__call__` method of the returned **wrapper** object, which in turn invokes `tracer.__call__`. In other words, decorated method calls trigger a four-stop process: `tracer.__get__`, followed by three call operation-- `wrapper.__call__`, `tracer.__call__`, and finally the original wrapped method.


The **wrapper** object retains both descriptor and subject instances, so it can route control back to the original decorator/descriptor class instance. In effect, the **wrapper** object saves the subject class instance available during method attribute fetch and adds it to the later call’s arguments list, which is passed to the decorator`__call__`. Routing the call back to the descriptor class instance this way is required in this application so that all calls to a wrapped method use the same **calls** counter state information in the descriptor instance object.


----------

Alternatively, we could use a nested function and enclosing scope references to achieve the same effect--the following version works the same as the preceding one, by swapping a class and object attributes for a nested function and scopes references. It requires noticeably less code, but follows the same four-step process on each decorated method call:

```py
class tracer(object):
    def __init__(self, func):                       # On @ decorator
        self.calls = 0                              # Save func for later call
        self.func = func 
    def __call__(self, *args, **kwargs):            # On call to original func
        self.calls += 1
        print("calls %s to %s" % (self.calls, self.func.__name__))
        return self.func(*args, **kwargs)
    def __get__(self, instance, owner):             # On method fetch
        def wrapper(*args, **kwargs):               # Retain both inst
            return self(instance, *args, **kwargs)  # Runs __call__
        return wrapper
    

@tracer
def spam(a, b, c):                  # spam = tracer(spam0)
    print(a + b + c)                # Uses __call__ only                    


class Person:
    def __init__(self, name, pay):
        self.name = name 
        self.pay = pay 
    
    @tracer
    def giveRaise(self, percent):           # giveRaise = tracer(giveRaise)
        self.pay *= (1.0 + percent)         # Makems giveRaise a descriptor

    @tracer 
    def lastName(self):                     # lastName = tracer(lastName)
        return self.name.split()[-1]
    

if __name__ == "__main__":
    
    spam(1, 2, 3)
    spam(a=4, b=5, c=6)

    print("\nmethods...")
    bob = Person("Bob Smith", 50000)
    sue = Person("Sue Jones", 100000)
    print(bob.name, sue.name)
    sue.giveRaise(.10)                          
    print(int(sue.pay))
    print(bob.lastName(), sue.lastName())       
```

```output
calls 1 to spam
6
calls 2 to spam
15

methods...
Bob Smith Sue Jones
calls 1 to giveRaise
110000
calls 1 to lastName
calls 2 to lastName
Smith Jones
```


----------

We might code this descriptor-based decorator more simply as follows, but it would then apply only to methods, not to simple functions--an intrinsic limitation of attribute descriptors:


```py
class tracer(object):                           # For methods, but not functions!
    def __init__(self, meth):                   # On @ decorator
        self.calls = 0
        self.meth = meth 
    def __get__(self, instance, owner):         # On method fetch
        def wrapper(*args, **kwargs):           # On method call: proxy with self+inst
            self.calls += 1
            print("call %s to %s" % (self.calls, self.meth.__name__))
            return self.meth(instance, *args, **kwargs)
        return wrapper
    
class Person:                               # Applies to class methods
    @tracer                                 # giveRaise = tracer(giveRaise)
    def giveRaise(self, percent):           # Makes giveRaise a descriptor
        ...

@tracer                         # But fails for simple functions 
def spam(a, b, c):              # spam = tracer(spam)
    ...                         # No attribute fetch occurs here
```