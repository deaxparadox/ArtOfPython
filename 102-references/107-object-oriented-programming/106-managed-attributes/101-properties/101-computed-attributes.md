# Computed Attributes

Computing the value of an attribute dynamically when fetched,for example. The following example illustrates:

```py
class PropSquare:
    def __init__(self, start) -> None:
        self.value = start 
    def getX(self):                         # On attr fetch
        return self.value ** 2
    def setX(self, value):                  # On attr assign
        self.value = value 
    X = property(getX, setX)                # No delete or docs

def main():
    P = PropSquare(3)
    Q = PropSquare(32)

    print(P.X)          # 3 ** 2
    P.X = 4
    print(P.X)          # 4 ** 2
    print(Q.X)          # 32 ** 2 (1024)

if __name__ == "__main__":
    main()
``` 

This class defines an attribute **X** that is accessed as though it were static data, but really runs code to compute its value when fetched. The effect is much like an implicit method call. When the code is run, the value is stored in the instance as state information, but each time we fetch it via the managed attribute, its value is automatically squared:

```py
9
16
1024
```

Notice that we've made two different instances--because property methods automcatically receive a **self** argument, they have access to the state information stored in instances. In our case, this means computes the square of the subject instances' own data.