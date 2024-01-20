# Timing Calls


The decorator is applied to two functions, in order to compare the relative speed  of list comprehensions and the **map** built-in call:


```py
import time, sys 
force = list if sys.version_info[0] == 3 else (lambda X: X)

class timer:
    def __init__(self, func):
        self.func = func 
        self.alltime = 0
    def __call__(self, *args, **kwargs):
        start = time.time()
        result = self.func(*args, **kwargs)
        elapsed = time.time() - start 
        self.alltime += elapsed
        print("%s: %.5f, %.5f" % (self.func.__name__, elapsed, self.alltime))
        return result
    
@timer
def listcomp(N):
    return [x * x for x in range(N)]

@timer
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
$ time python timerdeco1.py 
listcomp: 0.00001, 0.00001
listcomp: 0.00651, 0.00652
listcomp: 0.04624, 0.05276
listcomp: 0.08369, 0.13645
[0, 1, 4, 9, 16]
allTime = 0.13644623756408691

mapcall: 0.00001, 0.00001
mapcall: 0.01207, 0.01209
mapcall: 0.07405, 0.08613
mapcall: 0.12529, 0.21142
[0, 2, 4, 6, 8]
allTime = 0.21142196655273438

**map/comp = 1.549

real    0m0.522s
user    0m0.402s
sys     0m0.097s
```