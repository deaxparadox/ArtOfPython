# Functions Annotations

Function Annotations are completely optional metadata information about the types used by user-defined functions 

- Annotations are stored in the `__annotations__` attribute of the function as a dictionary and have no effect on any other part of the function. 

- Parameter annotations are defined by a colon after the parameter name, followed by an expression evaluating to the value of the annotation.

- Return annotations are defined by a literal `->`, followed by an expression, between the parameter list and colon denoting the end of the `def statement:

```python
>>> def f(ham: str, eggs: str = 'eggs') -> str:
...     print("Annotations:", f.__annotations__)
...     print("Arguments:", ham, eggs)
...     return ham + ' and ' + eggs

>>> f('spam')
Annotations: {'ham': <class 'str'>, 'return': <class 'str'>, 'eggs': <class 'str'>}
Arguments: spam eggs
'spam and eggs'
```