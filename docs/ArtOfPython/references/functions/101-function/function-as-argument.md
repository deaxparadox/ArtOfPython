# Function as argument

We can take a function as argument in Python. Let's see an example of it, in  the following example we will be creating a function `world()`, it will be taken as argument function while declaring the `hello()` function, and it will be saved in the `call` argument.

```py
>>> def world():
...     return " World!"
... 
>>> def hello(call = world):
...     print("Hello" + call())
... 
>>> hello()
Hello World!
>>> 
```

In this case, we are excepting the function as argument without calling the argument. 

But what if you don't need to execute the *world* function inside *hello* function, and only required the value returned by the *world* function, in that case, we can directly directly execute the *world* function, at the time of *hello* declaration, and the returned value will be stored in the *hello* function *call* argument:

```py
>>> def world():
...     return " World!"
... 
>>> def hello(call = world()):
...     print("Hello" + call)
... 
>>> hello()
Hello World!
>>> 
```