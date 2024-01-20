# Using simple factory functions

For example, metaclasses need for really be classes at all. The **class** statement issues a simple call to create a class at the conclusion of tis processing. Because of this, *any callable object* can in principle be used as a metaclass, provided it accepts the arguments passed and returns an object compatible with the intended class.

In fact, a simple ojbect factory function may serve just as well as a **type** subclass:

```py
# A Simple function can serve as a metaclass too

def MetaFunc(classname, supers, classdict):
    print("In MetaFunc: ", classname, supers, classdict, sep="\n...")
    return type(classname, supers, classdict)

class Eggs:
    pass 

print("making class")
class Spam(Eggs, metaclass=MetaFunc):       # Run simple function at end
    data = 1                                # Function returns class
    def meta(self, arg):
        return self.data + arg
    
print("Making instance")
X = Spam()
print("Data: ", X.data, X.meta(2))
```

When run, the function is called at the end of the declaring **class** statement, and it returns the expected new class object. The function is simply catching the call that the **type** object's `__call__` normally intercepts by default:

```bash
$ python metaclass3.py 
making class
In MetaFunc: 
...Spam
...(<class '__main__.Eggs'>,)
...{'__module__': '__main__', '__qualname__': 'Spam', 'data': 1, 'meta': <function Spam.meta at 0x7f0e1daf2050>}
Making instance
Data:  1 3
```