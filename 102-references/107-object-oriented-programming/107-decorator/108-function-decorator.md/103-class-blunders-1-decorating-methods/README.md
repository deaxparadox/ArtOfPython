# Class Blunders I: Decorating Methods

```py
class tracer:                                   # On @ decorator
    def __init__(self, func):                   # Save func for later call
        self.calls = 0
        self.func = func 
    def __call__(self, *args, **kwargs):        # On call to original function
        self.calls += 1
        print("calls %s to %s" % (self.calls, self.func.__name__))
        return self.func(*args, **kwargs)

```

----------

- decoration of simple functions:

```py
    
@tracer
def spam(a, b, c):                  # spam = tracer(spam)
    print(a + b + c)                # Triggers tracer.__init__



In [32]: spam(1, 2, 3)              # Runs tracer.__call__
calls 1 to spam
6

In [33]: spam(a=4, b=5, c=6)        # spam saved in an instance attribute
calls 2 to spam
15

```

----------

- decoration of class-level methods fails:

```py

class Person:
    def __init__(self, name, pay):
        self.name = name 
        self.pay = pay 
    
    @tracer
    def giveRaise(self, percent):           # giveRaise = tracer(giveRaise)
        self.pay *= (1.0 + percent)

    @tracer 
    def lastName(self):                     # lastName = tracer(lastName)
        return self.name.split()[-1]



In [34]: bob = Person("Bob Smith", 50000)       # tracer remembers method funcs

In [35]: bob.giveRaise(.25)                     # Runs tracer.__call__(???, .25)
calls 1 to giveRaise

TypeError: Person.giveRaise() missing 1 required positional argument: 'percent'

In [36]: print(bob.lastName())                  # Runs tracer.__call__(???)
calls 1 to lastName

TypeError: Person.lastName() missing 1 required positional argument: 'self'

In [37]:  
```

The root of the problem here is in the **self** argument of the tracer class's `__call__` method--is it a **tracer** instance or a **Person** instance?  We really need both as it’s coded: the **tracer** for decorator state, and the **Person** for routing on to the original method. Really, **self** *must* be the **tracer** object, to provide access to **tracer**’s state information (its calls and func); this is true whether decorating a simple function or a method.


Unfortunately, when our decorated method name is rebound to a class instance object
with a `__call__`, Python passes only the **tracer** *instance* to **self**; it doesn’t pass along the **Person** subject in the arguments list at all. Moreover, because the **tracer** knows nothing about the **Person** instance we are trying to process with method calls, there’s no way to create a bound method with an instance, and thus no way to correctly dispatch the call. This isn’t a bug, but it’s wildly subtle.
