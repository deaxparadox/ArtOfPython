# Tracing Calls

The following defines and applies a function decorator that counts the number of calls made to the decorated function and prints a trace message for each call:


```py
class tracer:
    def __init__(self, func):           # On @ decoration: save original function
        self.calls = 0
        self.func = func

    def __call__(self, *args):
        self.calls += 1
        print("call %s to %s" % (self.calls, self.func.__name__))
        self.func(*args)

@tracer
def spam(a, b, c):              # spam = tracer (spam)
    print(a + b + c)            # Wraps spam in a decorator object
```

- Each function decorated with this class will create a new instance, with its own saved function object and calls counter.
- The `*args` argument syntax is used to pack and unpack arbitrarily many passed-in arguments. This genrality enablese this decorator to be used to wrap any function with any number of positional arguments; this version doesn't yet work on keyword arguments or class-level methods.

```py
In [2]: spam(1, 2, 3)
call 1 to spam
6

In [3]: spam('a', 'b', 'c')
call 2 to spam
abc

In [4]: spam.calls
Out[4]: 2


In [16]: spam
Out[16]: <decorator1.tracer at 0x7fe9e1b1fdc0>
```

When run, the **tracer** class saves away the decorated function, and intercepts later calls to it, in order to add a layer of logic that counts and prints each call.

Notice how to total number of calls shows up as an attribute of the decorated function--**spam** is really an instance of the **tracer** class when decorated, a find that may have ramnifications for programs that do type checking, but is generally benign.

----------

For function calls, @ decoration syntax can be more convenient then modifyng each call to account for the extra logic level, and it avoids accidentally calling the original function directly. 

Consider a nondecorator equivalent such as the following:

```py
calls = 0
def tracer(func, *args):
    global calls
    calls += 1
    print("call %s to %s" % (calls, func.__name__))
    func(*args)

def spam(a, b, c):
    print(a, b, c)

In [18]: spam(1, 2,3)               # Normal nontraced call: accidental
1 2 3

In [21]: tracer(spam, 1, 2, 3)      # Special traced call without decorators
call 1 to spam
1 2 3

In [22]: 
```

This alternative can be used on any function without the special @ syntax, but unlike the decorator version, it requires extra syntax at every place where the function is called in your code.