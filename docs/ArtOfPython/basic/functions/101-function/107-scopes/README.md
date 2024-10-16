# Scopes

When you use a name in a program, Python creates, changes, or looks up the name in what is known as a `namespace--a place where names live`. When we talk about the search for a name's value in relation to code, the term `scope` refers to a namespace: that is, the location of a name's assignment in your source code determines the scope of the name's visibility to your code.

Names in Python come into existence when they are first assigned values, and they must be assigned before they are used. Because names are not declared ahead of time, Python uses the location of the assignment of a name to associate it with a particular namespace.

In other words, the place where you assign a name in your source code determines the namespace it will live in, and hence its scope of visibility.

*By default, all names assigned inside a function are associated with that function's namespace and no other*. This rule means that:

- Names assigned inside a **def** can only be seen by the code within the **def**. You cannot even refer to such names from outside the function.
- Names assigned inside a **def** do not clash with variables outside the **def**, even if the same names are used everywhere. A name **X** assigned outside a given **def** is a completely different variable from a name **X** assigned inside the **def**.

In all cases, the scope of a variable is always determined by where it is assigned in your source code and has nothing to do with which functions call which. Variables may be assigned in three different places corresponding to three different scopes:

- If a variables is assigned inside a **def**, it is *local* to that function.
- If a variables is assigned in an enclosing **def**, it is *nonlocal* to nested function.
- If a variables is assigned outside all **def**s, it is **global** to the entire file.

We call this *Lexical scoping* because variable scopes are determined entirely by the locations of the variables in the source code of your program files, not by function calls.


For example, in the following module file, the **X=99** assignment creates a **global** variable name **X** (visible everywhere in this file), but the **X=88** assignment creates *local* variable **X** (visible only within the **def** statement).

```py
X = 99              # Global (modules) Scope X

def func():
    X = 88          # Local (function) scope X: a different variable
```

## Scope Details

Functions defines a *local scope* and modules define a *global scope* with the folllowing properties:

- The enclosing module is a global scope.
- The global scope spans a single file only.
- Assigned names are local unless declared global or nonlocal
- All other names are enclosing function locals, globals or built-ins.
- Each call to a function creates a new local scope.


## Comprehensive variables

The variable **X** used to refer to the current iteration item in a comprehensive expression such as **[X for X in I]**, such variable are local to the expression itself in all comprehensive forms: generator, list, set ,and dictionary.


## Exception variables

The variable X used to reference the raised exception in a try statement handler clause such as except E as X. Such variable in local to the except block.