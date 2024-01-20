# Retaining Multiple Instances

The decorator function in this example can *almost* be coded as a class instead of a function, with the proper operator overloading protocol. The following slightly simplified alternative works similarly becuase its `__init__` is triggered when the @decorator is applied to the class, and its `__call__` is triggered when a subject class instance is created. Our objects are really instance of **Tracer** this time, and we essentiallly just trade an enclosing scope of reference for an instance attribute here:

```py


class Tracer:
    def __init__(self, aClass):                     # On @decorator
        self.aClass = aClass                        # Use instance attribute
    def __call__(self, *args):                      # On instance creation
        self.wrapped = self.aClass(*args)           # ONE (LAST) INSTANCE PER CLASS!
        return self
    def __getattr__(self, attrname):
        print("Trace:" + attrname)
        return getattr(self.wrapped, attrname)
    
@Tracer                                 # Triggers __init__
class Spam:                             # Like: Spam = Tracer(Spam)
    def display(self):
        print("Spam!" * 8)

food = Spam()                           # Triggers __call__
food.display()                          # Triggers __getattr__
```

This class-only alternative handles multiple *classes* as before, but it wont quite work for *multiple instances* of a given class: each instance construction call triggers `__call__`, which overwrites the prior instance. The net effect is that **Tracer** saves just one instance--the last one created.

```py

@Tracer
class Person:                           # Person = Tracer(Person)
    def __init__(self, name):           # Wrapper bound to Person
        self.name = name

bob = Person("Bob")                     # bob is really a Wrapper
print(bob.name)                         # Wrapper embeds a Person
sue = Person("Sue")
print(sue.name)                         # sue overwrites bob
print(bob.name)                         # OOPS: now bob's name is 'Sue'!
```

This code's output follows--because this tracer only has a single shared instance, the second overwrites the first:

```
Trace:display
Spam!Spam!Spam!Spam!Spam!Spam!Spam!Spam!
Trace:name
Bob
Trace:name
Sue
Trace:name
Sue
```

----------

The function-based **Tracer** version does work for mutlple instances, because each instance construction call make a new **Wrapper** instance, instead of overwritting the state of a single shared **Tracer** instance; the original non decorator version handles multiple instnaces correctly for the same reason.