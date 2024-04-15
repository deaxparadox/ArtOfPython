# local scope

The local scope is defined in the enclosed block:

- Inside a function.
- private variable of class which can only accessed inside the class.
- A variable defined in a module, this variable is local to that module.

### Function

A variable defined in the function is local variable, and it can't be access outside the function.

Let's define a variable `a` inside a function, which can only be accessed inside a function.

```py
def func():
    a = "a local variable"
    print(a)
```

If one try to acess the variable `a` outside the function, will get `NameError: name 'a'a is not defined`.


### Private class variable

A private variable defined in the class, which can only be accessed inside the class is a local variable. This are variables is local to the enclosing class block.