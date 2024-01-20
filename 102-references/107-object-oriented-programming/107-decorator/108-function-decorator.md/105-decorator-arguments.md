# Adding Decorator Arguments

Decorator also support arguments, which are use full for configuration options that can vary for each decorated function. A label, for instance, might be added as follows:

```py
def timer(label=""):
    def decorator(func):
        def onCall(*args):          # Multilevel state retention
            ...                     # args passed to function
            func(*args)             # func retained in enclosing scope
            print(label, ...)       # label retained in enclosing scope
        return onCall
    return decorator                # Returns the actual decorator

@timer("==>")                   # Like listcomp = timer("==>")(listcomp)
def listcomp(N): ...            # listcomp is rebound to new onCall

listcomp(...)                   # Really calls onCall
```

```
==> Ellipsis
```

- this code adds an enclosing scope to retain a decorator argument for use on a later actual call.

Python realy invokes **decorator** the reuslt of **timer**, run before decoration actually occurs--with the label value available in its enclosing scope. That is, **timer** **returns** the decorator, which remembers both the decorator argument and the original function, and returns the callable **onCall**, which ultimately invokes the original function. *Because this structure creates new **decorator** and **onCall** functions, their enclosing scopes are per-decoration state retention.*

----------

We can put this structure to use in our timer to allow a label and a trace control flag to be passed in at decoration time.


```py
import time, sys 
force = list if sys.version_info[0] == 3 else (lambda X: X)

def timer(label="", trace=True):                            # On decorator args: retain args
    class Timer:
        def __init__(self, func):                           # On @: retain decorated func
            self.func = func 
            self.alltime = 0
        def __call__(self, *args, **kwargs):                # On calls: call original
            start = time.time()
            result = self.func(*args, **kwargs)
            elapsed = time.time() - start 
            self.alltime += elapsed
            if trace:
                format = "%s %s: %.5f, %.5f"
                values = (label, self.func.__name__, elapsed, self.alltime)
                print(format % values)
            return result
    return Timer
    
@timer(label="[CCC]==>")
def listcomp(N):
    return [x * x for x in range(N)]

@timer(trace=True, label="[MMM]==>")
def mapcall(N):
    return force(map((lambda x: x * 2), range(N)))

result = listcomp(5)            # Time for this call, alls, return value
listcomp(50000)
listcomp(500000)
listcomp(1000000)
print(result)
print("allTime = %s" % listcomp.alltime)        # Total time for all listcomp calls                


print("")
result = mapcall(5)
mapcall(50000)
mapcall(500000)
mapcall(1000000)
print(result)
print('allTime = %s' % mapcall.alltime)         # Total time for all mapcall calls

print("\n**map/comp = %s" % round(mapcall.alltime / listcomp.alltime, 3))
```

```bash
$ time python timerdeco2.py 
[CCC]==> listcomp: 0.00001, 0.00001
[CCC]==> listcomp: 0.00861, 0.00863
[CCC]==> listcomp: 0.04982, 0.05845
[CCC]==> listcomp: 0.08682, 0.14527
[0, 1, 4, 9, 16]
allTime = 0.14526653289794922

[MMM]==> mapcall: 0.00001, 0.00001
[MMM]==> mapcall: 0.01061, 0.01062
[MMM]==> mapcall: 0.06863, 0.07925
[MMM]==> mapcall: 0.13081, 0.21006
[0, 2, 4, 6, 8]
allTime = 0.21006202697753906

**map/comp = 1.446

real    0m0.517s
user    0m0.418s
sys     0m0.080s
```

We can also test interactively to see how the decorator's configuration arguments come into play:

```py
>>> from timerdeco2 import timer
>>> @timer(trace=False)
    # No tracing, collect total time
... def listcomp(N):
...
 return [x * 2 for x in range(N)]
...
>>> x = listcomp(5000)
>>> x = listcomp(5000)
>>> x = listcomp(5000)
>>> listcomp.alltime
0.0037191417530599152
>>> listcomp
<timerdeco2.timer.<locals>.Timer object at 0x02957518>
```