# Retaining Enclosing Scope State with Defaults

```py
>>> def f1():
...     x = 88
...     def f2(x=x):
...             print(x)
...     f2()
... 
>>> f1()
88
>>> 
```

- The syntax **arg=value** in a **def** header means that the argument **arg** will default to the value **val** if no real value is passed to **arg** in a call. This syntax is used here to explicitly assign enclosing scope state to be retained.

- Specifically, in the modified **f2** here, the **x=x** means that the argument **x** will default to the value of **x** in the enclosing scope--because the second **x** is evaluated before Python steps into the nested **def**, it still referes to the **x** in **f1**. In effect, the default argument remembers what **x** was in **f1**: the object 88.

The following in equivalent of the prior example that avoids nesting altogether.

- Code inside a def in nevar evaluated until the function is actually called:

```py
>>> def f1():
...     x = 88
...     f2(x)
... 
>>> def f2(x):
...     print(x)
... 
>>> f1()
88
>>> 
``` 


## Nested scopes, defaults, and lambdas

A **lambda** expression also introduces a new local scope for the function it creates.

```py
>>> 
>>> def func():
...     x = 4
...     action = (lambda n: x ** n)     # x remembered from enclosing def
...     return action
... 
>>> x = func()
>>> print(x(2))                         # Prints 16, 4 ** 2
16
>>> 
```


To use defaults to pass values from an enclosing scope into **lambda**s, just as for **def**s.

```py
>>> def func():
...     x = 4
...     action = (lambda n, x=x: x ** n)            # Pass x in manually
...     return action
... 
>>> func()
<function func.<locals>.<lambda> at 0x7f59feca5750>
>>> 
>>> func()(2)
16
>>> 
```

## Loop variables may require defaults, not scopes

if a **lambda** or **def** defined within a function is nested inside a loop, and the nested function references an enclosing scope variable that is changed by that loop, all functions generated within the loop will have the same value--the value the references has in the *last* loop iteration.

The following attempts to build up a list of functions that each remember the current variable **i** from the enclosing scope:

```py
>>> def makeActions():
...     acts = []
...     for i in range(5):                          # Tries to remember each i
...             acts.append(lambda x: i ** x)       # But all remember same last i!
...     return acts 
... 
>>> acts = makeActions()
>>> 
>>> acts[0]
<function makeActions.<locals>.<lambda> at 0x7f59feca5900>
>>> 
>>> acts[0](2)                      # All are 4 ** 2, 4=value of last i
16
>>> acts[1](2)                      # This should be 1 ** 2 (1)
16
>>> acts[2](2)                      # This should be 2 ** 2 (4)
16
>>> acts[3](2)                      # Only this should be 4 ** 2 (16)
16
>>> acts[4](2)
16
>>> 
```

This is the one case where we still have to explicitly retain enclosing scope values with default arguments, rather than enclosing scope references. That is, to make this sort of code work, we must pass in the *current* value of the enclosing scope's variable with a default.

Because defaults are evaluated when the nested function is *created*, each remembers its own value for **i**:

```py
>>> 
>>> def makeActions():
...     acts = []
...     for i in range(5):
...             acts.append(lambda x, i=i: i ** x)
...     return acts
... 
>>> acts = makeActions()
>>> 
>>> acts[0](2)
0
>>> acts[1](2)
1
>>> 
>>> acts[2](2)
4
>>> acts[4](2)
16
>>> 
```


## Artitrary scope nesting 

Scopes my nest arbitrarily, but only enclosing function **def** statements are searched when names are referenced:

```py
>>> 
>>> def f1():
...     x = 99
...     def f2():
...             def f3():
...                     print(x)        # Found in f1's local scope!
...             f3()
...     f2()
... 
>>> f1()
99
>>> 
```