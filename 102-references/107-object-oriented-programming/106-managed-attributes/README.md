# Manages Attributes


Object attributes are central to most Python programs--they are where we often store information about the entities our scripts process.

```py
person.name                      # Fetch attribute value
person.name = value             # Change atribute value
```



### Inserting Code to Run on Attribute Access

- The `__getattr__` and `__setattr__` methods, for routing and undefined attribute fetches and all attribute assignments to generic handler methods.
- The `__getattribute__` method, for routing all attribute fetches to a generic handler method.
- The `property` built-in, for routing specific attributes access to get and set handler functions.
- The *descriptor protocol*, for routing specific attribute accesses to instances of classes with arbitrary get and set handler methods, and the basis for other tools such as properties and slots.


[Properties >>>](101-properties/README.md)