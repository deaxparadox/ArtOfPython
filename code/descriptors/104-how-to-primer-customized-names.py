"""# Customized names

When a class uses descriptors, it can inform 
each descriptor about which variable name was used.

In this example, the Person class has two descriptor 
instances, name and age. When the Person class is defined, 
it makes a callback to `__set_name__()` in LoggedAccess so
that the field names can be recorded, giving each descriptor 
its own `public_name` and `private_name`:
"""

import logging 

logging.basicConfig(level=logging.INFO)

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
    
    # First descriptor instance
    name = LoggedAgeAccess()
    # Second descriptor instance
    age = LoggedAgeAccess()
    
    
    def __init__(self, name, age):
        # Calls the first descritor
        self.name = name
        # Calls the second descriptor
        self.age = age
        
    def birthday(self):
        self.age += 1
        
if __name__ == "__main__":
    # Calling `vars()` to lookup the descriptor without 
    # triggering it
    
    print(vars(vars(Person)['name']))
    print(vars(vars(Person)['age']))
    
    
    # The new class now logs access to both `name` and `age`.
    pete = Person('Peter P', 10)
    kate = Person('Catherine C', 20)
    
    # The two `Person` instances contain only the private names
    print(vars(pete))
    print(vars(kate))