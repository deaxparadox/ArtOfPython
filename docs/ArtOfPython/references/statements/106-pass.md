# `pass` statements

The `pass` statement does nothing. It an be used when a statement is required syntactically but the program requires no action.

```python
>>> while True:
...     pass  # Busy-wait for keyboard interrupt (Ctrl+C)
... 
```

- This is commonly used for createing minimal classes:

```python
>>> class MyEmptyClass:
...     pass
```

- Another place `pass` can be used is as a place-holder for a function or conditional body when you are working on new code:

```python
>>> def initlog(*args):
...     pass   # Remember to implement this!
```