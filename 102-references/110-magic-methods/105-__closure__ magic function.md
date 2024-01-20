# __closure__ magic function in Python

Almost everything in Python is an **object**, similary **function** is an object to and all the function object have a `__closure__` attribute.__closure in a `dunder/magic function` i.e. methods having two underscores as prefix and suffix is a magic method name.

A `closure` is a function object that remembers values in enclosing scopes even if they are not present in memory. They __closure__ attribute of a closure function returns a type of cell objects. This cell object also has an attribute called cell_contents, which returns the content of the cell.

## Syntax 

```py
closure_function.__closure__
```

## Examples

```py
# this is a nested function
def gfg(raise_power_to):
  
    def power(number):
       return number ** raise_power_to
    return power
 
raise_power_to_3 = gfg(3)
print(raise_power_to_3.__closure__)
 
print(raise_power_to_3.__closure__[0].cell_contents)
```

```output
(<cell at 0x7f34ba2725e0: int object at 0x7f34bde02720>,)

3
```
