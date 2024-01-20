# Dynamic lookups

Interesting descriptors typically run computations instead of returning constants:

```py
import os 

class DirectorySize:
    def __get__(self, obj, objtype=None):
        return len(os.listdir(obj.dirname))
    
    
class Directory:
    size = DirectorySize()                  # Descriptor instance

    def __init__(self, dirname) -> None:
        self.dirname = dirname              # Regular instance attribute
```


An interactive session shows that the lookup is dynamic — it computes different, updated answers each time:



```py
In [15]: a = Directory("../")

In [16]: a.size             # previous directory has 27 files
Out[16]: 27

In [17]: g = Directory("../decorators")

In [18]: g.size             # another folder in previous directory has 5 file
Out[18]: 5

In [19]: 

In [19]: import os

In [20]: os.remove("../lists.ipynb")        # removed a file in previous directory

In [21]: a.size         # size is calculate again on run time.
Out[21]: 26

In [22]: 
```


Besides showing how descriptors can run computations, this example also reveals the purpose of the parameters to `__get__()`. The `self` parameter is `size`, an instance of `DirectorySize`. The `obj` parameter is either `g` or `s`, an instance of `Directory`. It is the `obj` parameter that lets the `__get__()` method learn the target directory. The `objtype` parameter is the class `Directory`.