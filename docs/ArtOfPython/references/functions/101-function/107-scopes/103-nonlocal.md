# The nonlocal Statement

The **nonlocal** statement is similar in both form and role to **global**. Like **global**, **nonlocal** declares that a name will be changed in an enclosing scope. Unlike **global**, though, **nonlocal** applies to a name in an enclosing function's scope, not the **global** module scope outside all **defs**. Also unlike **global**, **nonlocal** names must already exist in the enclosing function's scope when declared--then can exist only in enclosing functions and cannot be created by a first assignment in a nestef **def**.

**nonlocal** both allows assignment to names in enclosing function scopes and limits scope lookups for such names to enclosing **defs**.

### nonlocal Basics

```py
def func():
    nonlocal name1, name2, ...              # Ok here

>>> nonlocal X
SyntaxError: nonlocal declaration not allowed at module level
```

This statement allows a nest function to change one or more names defined in a syntactically enclosing function's scope.

### nonlocal in Action

```py
>>> 
>>> def tester(start):
...     state = start                       # Referencing nonlocals works normally
...     def nested(label):
...             print(label, state)         # Remembers state in enclosing scope
...     return nested
... 
>>> F = tester(0)
>>> F("spam")
spam 0
>>> F("ham")
ham 0
>>> 
```

### Using nonlocal for changes

If we declare **state** in the **tester** scope as **nonlocal** within **nested**, we got get change it inside the nested function, too. This words even though **tester** has returned and exited by the time we call the returned **nested** function throught the name F:

```py
>>> 
>>> def tester(start):
...     state = start                       # Each call gets it own state
...     def nested(label):
...             nonlocal state              # Remembers state in enclosing scope
...             print(label, state)
...             state += 1                  # Allowed to change it if nonlocal
...     return nested
... 
>>> F = tester(0)
>>> 
>>> F("spam")                               # Increments state on each call
spam 0
>>> F("ham")
ham 1
>>> F("eggs")
```


- We can call the **tester** factory (closure) function multiple times to get multiple times to get mulitple copies of its state in memory. The **state** object in the enclosing scope is essentially attached to the **nested** function object returned; each call makes a new, distinct **state** object, such that updating one function's state won't impact the other.

```py
>>> G = tester(42)          # Make a new tester that starts at 42
>>> G("spam")
spam 42
>>> G('eggs')               # My state information updated to 43
eggs 43
>>> F('bacon')              # But f's is where it left off: at 3
bacon 3                     # Each call has different state information
>>> 
```

### Boundary cases

nonlocals come with some subtleties to be aware of:

1. unlike the **global** statement, **nonlocal** names realy *must* have previously been assigned in an enclosing **def**'s when a **nonlocal** is evaluated, or else you'll get an error--you cannot create then dynamically by assigning then a new in the enclosing scope. If fact, they are checked at function definition time before  with an enclosing or nested function is called:


```py
>>> 
>>> def tester(start):
...     def nested(label):
...             nonlocal state              # Nonlocals must already exist in enclosing def!
...             state = 0
...             print(label, state)
...     return nested
... 
  File "<stdin>", line 3
SyntaxError: no binding for nonlocal 'state' found
>>> 
```

```py
>>> 
>>> def tester(start):
...     def nested(label):
...             global state            # Global don't have to exist yet when declared
...             state = 0               # This creates the name in the module now
...             print(label, state)
...     return nested
... 
>>> F = tester(0)
>>> F('abc')
abc 0
>>> state
0
>>> 
```


2. **nonlocal** restricts the scope lookup to just enclosing defs; nonlocals are not looked up in the enclosign module's global scope or the built-in scope outside all **def**s, even if they are already here:

```py
>>> spam = 99
>>> def tester():
...     def nested():
...             nonlocal spam               # Must be in a def, not the module!
...             print("Current=", spam)
...             spam += 1
...     return nested
... 
  File "<stdin>", line 3
SyntaxError: no binding for nonlocal 'spam' found
>>> 
```