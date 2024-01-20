# Implementing Private Attributes

```py
"""
File access1.py (3.X + 2.X)

Privacy for attributes fetched from class instances.
See self-test code at end of file for a usage example.

Decorator same as: Doubler = Private('data', 'size')(Doubler).
Private returns onDecorator, onDecorator returns onInstance,
and each onInstance instance embeds a Doubler instance.
"""

traceMe = False

def trace(*args):
    if traceMe:
        print("[" + " ".join(map(str, args)) + "]")
        
def Private(*privates):
    def onDecorate(aClass):
        class onInstance:
            def __init__(self, *args, **kwargs):
                self.wrapped = aClass(*args, **kwargs)
            
            def __getattr__(self, attr):
                trace("get:", attr)
                if attr in privates:
                    raise TypeError("private attribute fetch: ", + attr)
                else:
                    return getattr(self.wrapped, attr)
                
            def __setattr__(self, attr, value):
                trace("set:", attr, value)
                if attr == "wrapped":
                    self.__dict__[attr] = value 
                elif attr in privates:
                    raise TypeError("private attribute change: " + attr)
                else:
                    setattr(self.wrapped, attr, value)
        return onInstance
    return onDecorate

if __name__ == "__main__":
    traceMe = True
    
    @Private('data', 'size')
    class Doubler:
        def __init__(self, label, start) -> None:
            self.label = label
            self.data = start
        def size(self):
            return len(self.data)
        def double(self):
            for i in range(self.size()):
                self.data[i] = self.data[i] * 2
        def display(self):
            print("%s => %s" % (self.label, self.data))
        
    X = Doubler("Y is", [1, 2, 3])
    Y = Doubler("Y is", [-10, -20, -30])
    
    # The following all succeed
    print(X.label)
    X.display()
    X.double()
    X.display()
    print(Y.label)
    Y.display()
    Y.double()
    Y.label = 'Spam'
    Y.display()
    
    # The following all fail properly
    """
    print(X.size())
    print(X.data)
    X.data = [1, 1, 1]
    X.size = lambda S: 0
    print(Y.data)
    print(Y.size())
    """
```

When `traceMe` is `True`, the module file's self-test code produces the following output. Notice how the decorator catches and validates both attributes fetches and assignments run *outside* of the wrapped class, but does not catch attribute accesses *inside* the class itself:

```bash
[set: wrapped <__main__.Doubler object at 0x7f6e699af7d0>]
[set: wrapped <__main__.Doubler object at 0x7f6e699af800>]
[get: label]
Y is
[get: display]
Y is => [1, 2, 3]
[get: double]
[get: display]
Y is => [2, 4, 6]
[get: label]
Y is
[get: display]
Y is => [-10, -20, -30]
[get: double]
[set: label Spam]
[get: display]
Spam => [-20, -40, -60]
```