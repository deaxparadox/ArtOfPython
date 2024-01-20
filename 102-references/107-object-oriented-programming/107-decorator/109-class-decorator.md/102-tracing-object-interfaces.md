# Tracing Object Interfaces

Another common use case for class decorators augments the interface of *each* generated instance. Class decorators can essentially installl on instances a wrapper or "proxy" logic layer that manages access to their interfaces in some way.

`__getattr__` is run when an undefined name is fetched; we can used this hook to intercept methods call in a controller class and propagate them to an embedded object.

For reference, here's the original nondecorator delegation example, working on two built-in tpe objects.

```py
class Wrapper:
    def __init__(self, object):
        self.wrapped = object           # Save object
    def __getattr__(self, attrname):
        print("Trace:", attrname)               # Trace fetch
        return getattr(self.wrapped, attrname)  # Delegate fetch
```

```py
>>> x = Wrapper([1,2,3])            # Wrap a list
>>> x.append(4)                     # Delegate to list method
Trace: append
>>> x.wrapped                       # Print my member
[1, 2, 3, 4]
>>> 
>>> 
>>> x = Wrapper({"a": 1, "b": 2})   # Wrap a dictionary
>>> list(x.keys())                  # Delegate to dictionary method
Trace: keys                         # Use list() in 3.X
['a', 'b']
>>> 
```

In this code, the **Wrapper** class intercepts access to any of the wrapped object's method attributes, prints a trace message, and uses the **getattr** built-in to pass off the request to the wrapped object. Specifically, it traces attribute access made *outside* the wrapped object's class; accesses inside the wrapped object's methods are not caught and run normally by design. Theis *whole-interface* model differs from the behavior of function decorators, which wrap up just one specific method.

[<<< Singleton Classes](101-singleton-classes.md) ... [Tracing interfaces with class decorators >>>](103-tracing-interfaces-with-class-decorators.md)