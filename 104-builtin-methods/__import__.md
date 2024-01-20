# __import__()

Syntax:

```python
__import__(name, globals=None, locals=None, fromlist=(), level=0)¶
```

This function is invoked by the `import` statement. It can be replaced (by importing the `builtins` module and assigning to `builtins.__import__`) in order to change sementtics of the import statement.

- The function imports the module *name*, potentiall using the given given *globals* and *locals* to determine how to interpret the name in a package contect. 
- The *fromlist* givens the names of objects or submodules that should be imported from the module given by name.
- The standard implementation does not use its *locals* argument at all and uses it *globals* only to determine the package contextof the import statement.

- *level* specifies whether to use absolute  or relative imports.
- `0` (the default) means only perform absolute imports. 
- Positive values for *level* indicate the number of parent directories to searh relative to the directory of the module calling **__import__()** .

- When the *name* variable is of the form `package.module`, normally, the top-level package (the name up till the first dot) is returned, `not` the module named by *name*. However, when a non-empty *fromlist* argument is given, the module name by `name` is returned.

For example, the statement import spam results in bytecode resembling the following code:

```python
spam = __import__('spam', globals(), locals(), [], 0)
```

The statement `import spam.ham` results in this call:

```python
spam = __import__('spam.ham', globals(), locals(), [], 0)
```

- Note how __import__() returns the toplevel module here because this is the object that is bound to a name by the `import` statement.

On the other hand, the statement `from spam.ham import eggs, sausage as saus` results in

```python
_temp = __import__('spam.ham', globals(), locals(), ['eggs', 'sausage'], 0)
eggs = _temp.eggs
saus = _temp.sausage
```


