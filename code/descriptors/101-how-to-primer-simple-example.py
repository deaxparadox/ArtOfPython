# Simple example: A descriptor that returns a constant

class Ten:
    # The `Ten` class is a discriptor whose `__get__()` method
    # always returns the contsnt `10`;
    def __get__(self, obj, objtype=None):
        return 10
class A:
    # Regular class attribute
    x = 5
    
    # Descriptor instance
    y = Ten()
    
if __name__ == "__main__":
    # Make an instance of class A
    a = A()
    
    # Normal attribute loopup
    # 
    # The dot operator finds 'x':5 in the class dictionary.
    print(a.x)
    
    # Descriptor lookup
    # 
    # The dot operator finds a descriptor instance, recognized 
    # by its `__get__` method. Calling that method returns `10`.
    print(a.y)
    # The value `10` is not stored in either the class dictionary 
    # or the instance dictionary. Instead the value `10` is computed 
    # on demand.