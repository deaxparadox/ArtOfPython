# Nested functions

Function in python can be nested. Let's see an example of the nested function.


```py
>>> def hello():
...     def world():
...         print("Hello world")
...     world()
... 
>>> hello()
Hello world
>>> 
```

Here we have nested the `world()` function in inside of `hello()` function, and to execute the world function, we need to call the world function inside the hello function, because the world function in visible in hello scope.

We can also return the world function without executing, and save it in the instance, in that way we can execute the nested function outside of the hello scope.

```py
>>> def hello():
...     def world():
...         print("Hello world")
...     return world
... 
>>> world = hello()
>>> world()
Hello world
>>> 
```
