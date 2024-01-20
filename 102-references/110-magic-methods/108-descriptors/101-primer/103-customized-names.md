# Customized names

When a class uses descriptors, it can inform each descriptor about which variable name was used.

In this example, the `Person` class has two descriptor instances, `name` and `age`. When the `Person` class is defined, it makes a callback to `__set_name__()` in `LoggedAccess` so that the field names can be recorded, giving each descriptor its own *public_name* and *private_name*:

```py
import logging 

logging.basicConfig(
    level=logging.INFO
)

class LoggedAgeAccess:
    def __set_name__(self, owner, name):
        self.public_name = name
        self.private_name = "_" + name

    def __get__(self, obj, objtype=None):
        value = getattr(obj, self.private_name)
        logging.info("Accessing %r giving %r", self.public_name, value)
        return value 
    def __set__(self, obj, value):
        logging.info("Updating %r to %r", self.public_name, value)
        setattr(obj, self.private_name, value)

class Person:
    age = LoggedAgeAccess()                         # First descriptor instance
    name = LoggedAgeAccess()                         # Second descriptor instance

    def __init__(self, name, age) -> None:
        self.name = name                            # Calls the first descriptor
        self.age = age                              # Calls the second descriptor
    
    def birthday(self):
        self.age += 1                               # Calls both __get__() and __set__()
```

An interactive session shows that the `Person` class has called `__set_name__()` so that the field names would be recorded. Here we call `vars()` to look up the descriptor without triggering it:

```py
In [3]: vars(vars(Person)['name'])
Out[3]: {'public_name': 'name', 'private_name': '_name'}

In [4]: vars(vars(Person)['age'])
Out[4]: {'public_name': 'age', 'private_name': '_age'}

```

The new class now logs access to both *name* and *age*:

```py
In [5]: pete = Person('Peter P', 10)
INFO:root:Updating 'name' to 'Peter P'
INFO:root:Updating 'age' to 10

In [6]: kate = Person('Catherine C', 20)
INFO:root:Updating 'name' to 'Catherine C'
INFO:root:Updating 'age' to 20

In [7]: 
```

The two `Person` instances contain only the private names:

```py
In [7]: vars(pete)
   ...: 
Out[7]: {'_name': 'Peter P', '_age': 10}

In [8]: vars(kate)
Out[8]: {'_name': 'Catherine C', '_age': 20}

```