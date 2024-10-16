# Factory Functions: Closures

The function object question remembers values in enclosing scopes regardless of whether those  scopes are still present in memory. In effect, have attached packets of memory (a.k.a *state retention*), which are local to each copy of the nested function created, and often provide a simple alternative to classes in the this role.

## A Simple function factory

Factory functions (a.k.a closures) are sometimes used by programs that need to generate event handlers on the fly in response to conditions at runtime.

For instance, imagine a GUI that must define actions according to user inputs that cannot be anticipated when the GUI is built. In such cases, we need a function that creates and returns another function, with information that may vary per function made.


```py
>>> def maker(N):
...     def action(X):
...             return X ** N
...     return action
... 
>>>
```

- This defines an outer function that simply generates and returns a nested function without calling it--**maker** makes **action**, but simply returns **action** without running it:

```py
>>> f  = maker(2)
>>> f
<function maker.<locals>.action at 0x7f59feca4820>
```

- what we get back is a reference to the generate nested function--the one created when the nested **def** runs. If we not call what we goot back from the outer function:

```py
>>> f(3)
9
>>> f(4)
16
>>> 
```

- we invoke the nested function--the one called **action** in **maker**. In other words we're calling the nested function that maker created and passed back.

The nested function *remembers* integer 2, the value of the variable **N** in maker, even though **maker** has returned and exited by the time we call **action**. *In effect, **N** from the enclosing local scope is retained as state information attacked to the generated **action**, which is why we get back its argument squared when it is later called*.

If we now call the outer function again, we get back a *new* nested function with *different* state information attached. That is, we get the argument cubed instead of squared when calling the new function, but the original still squares as before:

```py
>>> g = maker(3)
>>> g(4)
64
>>> # calling f instance, with same argument
>>> f(4)
16
>>> 
```

#### Using *lambda*

Enclosing scopes are often employed by the **lambda** function-creation expression:

```py
>>> def maker(N):
...     return lambda X: X ** N
... 
>>> h = maker(3)
>>> h(4)
64
>>> 
```