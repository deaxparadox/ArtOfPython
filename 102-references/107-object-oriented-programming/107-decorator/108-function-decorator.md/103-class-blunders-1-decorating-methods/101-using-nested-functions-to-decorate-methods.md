# Using nested functions to decorate methods

If you want function decorators to work on *both* simple functions and class-level methods, the most straightforward solution lies in using one of the state retention, coded you function decorator as nested **defs**, so that you don't depened on a single **self** instance argument to be both the wrapper class instance and the subject class instance.

The following alternatives applies this fix using **nonlocal**. Because decorated methods are rebounded to simple functions instead of instance objects, Python correctly passes the **Person** object as the first argument, and the decorator propagates it on in the first item of `*args` to the **self** argument of the real, decorated methods:

```py
# A call tracer decorator for both functions and methods.

def tracer(func):                       # Use function, not class with __call__
    calls = 0                           # Else "self" is decorator instance only!
    def onCall(*args, **kwargs):
        nonlocal calls
        calls += 1
        print("call %s to %s" % (calls, func.__name__))
        return func(*args, **kwargs)
    return onCall

if __name__ == "__main__":

    # Applies to simple functions
    @tracer
    def spam(a, b, c):                      # spam = tracer(spam)
        print(a + b + c)                    # onCall remembers spam

    @tracer
    def eggs(N):
        return 2 ** N
    
    spam(1, 2, 3)
    spam(a=4, b=5, c=6)

    # Applie sto class-level method functions to

    class Person:
        def __init__(self, name, pay):
            self.name = name 
            self.pay = pay 
        
        @tracer
        def giveRaise(self, percent):           # giveRaise = tracer(giveRaise)
            self.pay *= (1.0 + percent)         # onCall remembers giveRaise

        @tracer 
        def lastName(self):                     # lastName = tracer(lastName)
            return self.name.split()[-1]
        
    print("methods...")
    bob = Person("Bob Smith", 50000)
    sue = Person("Sue Jones", 100000)
    print(bob.name, sue.name)
    sue.giveRaise(.10)                          # Runs onCall(sue, .10)
    print(int(sue.pay))
    print(bob.lastName(), sue.lastName())       # Runs onCall(bob), lastName in scopes
```

```bash
$ python decorator7.py 
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