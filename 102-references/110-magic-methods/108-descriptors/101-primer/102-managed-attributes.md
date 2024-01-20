# Managed attributes

A popular use for descriptors is managing access to instance data. The descriptor is assigned to a public attribute in the class dictionary while the actual data is stored as a private attribute in the instance dictionary. The descriptor’s `__get__()` and `__set__()` methods are triggered when the public attribute is accessed.

In the following example, age is the public attribute and _age is the private attribute. When the public attribute is accessed, the descriptor logs the lookup or update:

```py
import logging 

logging.basicConfig(
    level=logging.INFO
)

class LoggedAgeAccess:
    def __get__(self, obj, objtype=None):
        value = obj._age 
        logging.info("Accessing %r giving %r", "age", value)
        return value 
    def __set__(self, obj, value):
        logging.info("Updating %r to %r", "age", value)
        obj._age = value 

class Person:
    age = LoggedAgeAccess()                         # Descriptor instance

    def __init__(self, name, age) -> None:
        self.name = name                            # Regular instance attribute
        self.age = age                              # Calls __set__()
    
    def birthday(self):
        self.age += 1                               # Calls both __get__() and __set__()
```

An interactive session shows that all access to the managed attribute *age* is logged, but that the regular attribute *name* is not logged:



```py
In [28]: mary = Person('Mary M', 30)                # The initial age update is logged
INFO:root:Updating 'age' to 30

In [29]: dave = Person('David D', 40)
INFO:root:Updating 'age' to 40

In [30]: vars(mary)                                 # The acutal data is in a private attribute
Out[30]: {'name': 'Mary M', '_age': 30}

In [31]: vars(dave)
Out[31]: {'name': 'David D', '_age': 40}

In [33]: mary.age                                   # Access the data and log the lookup
INFO:root:Accessing 'age' giving 30
Out[33]: 30

In [34]: dave.age
INFO:root:Accessing 'age' giving 40
Out[34]: 40

In [35]: mary.birthday()                            # Updates are logged as well
INFO:root:Accessing 'age' giving 30
INFO:root:Updating 'age' to 31

In [36]: dave.name                                  # Regular attribute lookup isn't logged
Out[36]: 'David D'

In [37]: dave.age                                   # Only the managed attribute is good
INFO:root:Accessing 'age' giving 40
Out[37]: 40

In [38]: dave.age += 1
INFO:root:Accessing 'age' giving 40
INFO:root:Updating 'age' to 41

In [39]: 
```

One major issue with this example is that the private name _age is hardwired in the LoggedAgeAccess class. That means that each instance can only have one logged attribute and that its name is unchangeable.