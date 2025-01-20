# Managed attributes
# 
# A popular use for descriptors is managing access to instance data. 
# The descriptor is assigned to a public attribute in the class 
# dictionary while the actual data is stored as a private attribute 
# in the instance dictionary. The descriptor’s __get__() and __set__()
# methods are triggered when the public attribute is accessed.

import logging 

logging.basicConfig(level=logging.INFO)

class LoggedAgeAccess:
    def __get__(self, obj, objtype=None):
        value = obj._age
        logging.info("Accessing %r giving %r", "age", value)
        return value
    def __set__(self, obj, value):
        logging.info("Updating %r to %r", "age", value)
        obj._age = value
        
class Person:
    
    # Descriptor instance
    age = LoggedAgeAccess()
    
    def __init__(self, name, age):
        # Regular instance attribute
        self.name = name
        # Calls __set__()
        self.age = age
        
    def birthday(self):
        # Calls both __get__() and __set__()
        self.age += 1
        
if __name__ == "__main__":
    mary = Person('Mary M', 30)         # The initial age update is logged

    dave = Person('David D', 40)


    vars(mary)                          # The actual data is in a private attribute

    vars(dave)


    mary.age                            # Access the data and log the lookup


    mary.birthday()                     # Updates are logged as well



    dave.name                           # Regular attribute lookup isn't logged

    dave.age                            # Only the managed attribute is logged


"""
One major issue with this example is that the private name _age is 
hardwired in the LoggedAgeAccess class. That means that each instance 
can only have one logged attribute and that its name is unchangeable.
In the next example, we’ll fix that problem.
"""