# The global Statement

The **global** statement tells Python that a function plans to change one or more global names--that is, names that live in the enclosing module's scope (namespace).

## Global names are variables assigned at the top level of the enclosing module file.

Suppose we have a file `mod_1.py` and at top we define a variable `x = 1`, this `x` in global variable, it's defined outside any enclosing scope.

```py
x = 1
```

- Global names must be declared only if they are assigned within a function.
- Global names may be referenced within a function without being declared.

`global` allows us to *change* names that live outside of a def at the top level of the module.


Accessing a global variable:

```py
X = 88                  # Global X

def func():
    global X
    X = 99              # Global X: outside def

func()
print(X)                # Prints 99
```

Setting a variable global:

```py
y, x = 1, 2             # Global variable in module
def all_global():
    global x            # Declare globals assigned
    x = y + x           # No need to declare y, x: LEGB
```