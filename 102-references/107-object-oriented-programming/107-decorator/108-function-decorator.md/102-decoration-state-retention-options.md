# Decorator State Retention Options

Function decorations have a variety of options for retaining state information provided at decoration time, for use during the actual function call. They generally need to support multiple decorated objects and multiple calls, but there are a number of ways to implement these goals: instance attributes, global variables, nonlocal closure variables, and function attributes can all be used for retaining state.

### Class instance attributes

For example, this adds support for *keyword* arguments with `**` syntax, and *returns* the wrapped function's result to support more use cases.

```py
class tracer:
    def __init__(self, func):
        self.calls = 0
        self.func = func 
    def __call__(self, *args, **kwargs):
        self.calls += 1
        print("call %s to %s" % (self.calls, self.func.__name__))
        return self.func(*args, **kwargs)
    

@tracer
def spam(a, b, c):
    print(a + b + c)


@tracer
def eggs(x, y):
    print(x ** y)

spam(1, 2, 3)
spam(a=3, b=5, c=6)

eggs(2, 16)
eggs(4, y=4) 
```

- this uses *class instance attributes* to save state explicitly.

- Both the wrapped function and the calls coounter are *per-instance* information--each decoration gets it own copy. 

- The **spam** and **eggs** functions each have their own calls counter, because each decoration creates a new class instance.

```bash
$ python decorator2.py 
call 1 to spam
6
call 2 to spam
14
call 1 to eggs
65536
call 2 to eggs
256
```

- while usefull for decorating functions, this coding scheme still has issues when applied to methods.


### Enclosing scopes and globals

**Closure functions--**with enclosing **def** scope references and nested **def**s--can often achieve the same effect, especially for static data like the decorated original function.

In this example, though, we would also needd a counter in the enclosing scope that *changes* on each call.

Moving state variables out to the *global scope* with declarations in one candidate.

```py
calls = 0
def tracer(func):                                           # State via enclosing scope and global
    def wrapper(*args, **kwargs):                           # Instead of class atributes
        global calls                                        # calls is global, not per-function
        calls += 1
        print("call %s to %s" % (calls, func.__name__))
        return func(*args, **kwargs)    
    return wrapper

@tracer
def spam(a, b, c):                      # Same as: spam = tracer(spam)
    print(a + b + c)

@tracer
def eggs(x, y):                         # Same as: eggs = tracer(eggs)
    print(x ** y)


spam(1, 2, 3)                           # Really calls wrapper, assigned to spam
spam(a=4, b=5, c=6)                     # wrapper calls spam

eggs(2, 16)                             # Really calls wrapper, assigned to eggs
eggs(4, y=14)                           # Global calls is not per-decoration here!
```

```bash
$ python decorator3.py 
call 1 to spam
6
call 2 to spam
15
call 3 to eggs
65536
call 4 to eggs
268435456
```

### Enclosing scopes and nonlocals

Shared global state may be what we want in some cases. 

If we really want a *per-function* counter, though, we can either use classes, or make use of *closure* (a.k.a. *factory*) functions and the **nonlocal** statement in Python **3.X**. Becuase this new statement allows enclosing function scope variables to changed, they can serve as per-decoration and changeable data.

```py
def tracer(func):                               # State via enclosing scope and nonlocal
    calls = 0                                   # Instead of class atts and global
    def wrapper(*args, **kwargs):               # calls is per-function, not global
        nonlocal calls 
        calls += 1
        print("call %s to %s" % (calls, func.__name__))
        return func(*args, **kwargs)
    return wrapper 

@tracer
def spam(a, b, c):                      # Same as: spam = tracer(spam)
    print(a + b + c)

@tracer
def eggs(x, y):                         # Same as: eggs = tracer(eggs)
    print(x ** y)

spam(1, 2, 3)                           # Really calls wrapper, bound to func
spam(a=4, b=5, c=6)                     # wrapper calls spam

eggs(2, 16)                             # Really calls wrapper, bound to eggs
eggs(4, y=14)                           # Nonlocal calls is per-decoration here!

```

Now, because enclosing scope variables are not cross-programm globals, each wrapped function get its won counter again, just as for classes and attributes.


```bash
$ python decorator4.py 
call 1 to spam
6
call 2 to spam
15
call 1 to eggs
65536
call 2 to eggs
268435456
```


### Function attributes

To avoid globals and classes by making use of *function atributes* for some changeable state instead.

We can assign arbitrary attributes to functions to attach them, with **func.attr=value**. Because a factory function makes a new function on each call, its attributes become per-call state.

Moreoever, you need to use this technique only for state variables that must *change*; enclosing scope references are still retained and work normally.

In our example, we can simple use **wrapper.calls** for state. The following works the same as **nonlocal** version because the counter is again per-decoratored function:

```py
def tracer(func):                           # State via enclosing scope and func attr
    def wrapper(*args, **kwargs):           # calls is per-function, not global
        wrapper.calls += 1
        print("call %s to %s" % (wrapper.calls, func.__name__))
        return func(*args, **kwargs)
    
    wrapper.calls = 0
    return wrapper


@tracer
def spam(a, b, c):                      # Same as: spam = tracer(spam)
    print(a + b + c)

@tracer
def eggs(x, y):                         # Same as: eggs = tracer(eggs)
    print(x ** y)

spam(1, 2, 3)                           # Really calls wrapper, assigned to spam
spam(a=4, b=5, c=6)                     # wrapper calls spam

eggs(2, 16)                             # Really calls wrapper, assigned to eggs
eggs(4, y=14)                           # Nonlocal calls is per-decoration here!

```

- this works only because the name **wrapper** is retained in the enclosing **tracer** function's scope. When we later increment **wrapper.calls**, we are not changing the name **wrapper** itself, so no nonlocal declaration is required.

```bash
$ python decorator5.py 
call 1 to spam
6
call 2 to spam
15
call 1 to eggs
65536
call 2 to eggs
268435456
```

----------


Function attributes also have substantial advantages.

- For one, they allow access to the saved state from *outside* the decorator's code; nonlocals can only be seen inside the nested function itself, but function attributes have wider visibility.
- Another, they are far more *portable*, this scheme also works in 2.X, making it version-neutal.

Function attributes are equivalent to enclosing scope nonlocals.

Because decorators often imply multiple levels of callables, you can combine functions with enclosing scopes, classes with attributes, and function attributes to achieve a variety of coding structure. This sometimes may subtle then you expect--each decorated function should have its won state, and each decorated class may require state both itself and for each generated instance.