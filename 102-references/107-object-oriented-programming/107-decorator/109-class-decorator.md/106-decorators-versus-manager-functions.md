# Decorators Versus Manager Functions

With the original non-decorator tracing example, we could simply code instance creation differently:

```py
class Spam:                             # Nondecorator version
    ...                                 # Any class will do
food = Wrapper(Spam())                  # Special creation syntax

@Tracer
class Spam:                             # Decorator verion
    ...                                 # Requires @ syntax at class
            
food = Spam()                           # Normal creation syntax      
```

Essentially, *class decorators* shift special syntax requirements from the instance creation call to the class statement itself.

Rather then decorating aclass and using normal instance creation calls, we could simply pass the class and its construction arguments into a manager function:

```py

instances = {}
def getInstances(aClass, *args, **kwargs):
    if aClass not in instances:
        instances[aClass] = aClass(*args, **kwargs)
    return instances(aClass)

bob = getInstances(Person, "Bob", 40, 10)               # Versus: bob = Person('Bob', 40, 10)
```

Alternatively, we could use Python's introspection facilities to fetch the class from an already created instance:

```py
instances = {}
def getInstance(object):
    aClass = object.__clas__
    if aClass not in instances:
        instances[aClass] = object
    return instances[aClass]

bob = getInstance(Person('Bob', 40, 10))
```

The same holds true for *function decorators*. Rather than decorating a functino with logic that intercepts later calls, we could simply pass the function and its arguments into a manager that dispatches the call:

```py

def func(x, y):                         # Nondecorator version
    ...                                 # def tracer(func, args): ... func(*args)
result = tracer(func, 1, 2)             # Special call syntax

@tracer
def func(x, y):                         # Decorator version
    ...                                 # Rebinds name: func = tracer(func)
result = func(1, 2)                     # Normal call syntax
```

Manager function approaches like this place the burden of using special syntax on *calls*, instead of expecting decoration syntax at function and class definitions, but also allow you to selectively apply augmentation on a call-by-call basis.