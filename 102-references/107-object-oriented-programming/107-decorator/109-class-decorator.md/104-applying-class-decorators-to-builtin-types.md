# Applying class Decorators to built-in types

Previously used decorator:

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
```



We can also use the decorator to wrap up a built-in type such as a list, as long as we either subclass to allow decoration or perform the decoration manually--decorator syntax requires a **class** statement for the @ line. 

In the following, **x** is really a **Wrapper** againg due to the indrection of decoration:

```py
>>> from interfacetracer import Tracer
>>> @Tracer
... class MyList(list): pass            # MyList = Tracer(MyList)
... 
>>> x = MyList([1, 2, 3])               # Triggers Wrapper(0)
>>> x.append(4)                         # Triggers __getattr__, append
Trace: append
>>> x.wrapped
[1, 2, 3, 4]
>>> 
>>> 
>>> WrapList = Tracer(list)             # Or perform decoration manually
>>> x = WrapList([4, 5, 6])             # Else subclass statement required
>>> x.append(7)
Trace: append
>>> x.wrapped
[4, 5, 6, 7]
```

The decorator approach allows us to move instance creation into the decorator itself, instead of requiring a premade ojbect to be passed in.