# `lambda` as argument

Another use is to pass a small function as an argument:

```python
>>> pairs = [(1, 'one'), (2, 'two'), (3, 'three'), (4, 'four')]
>>> pairs.sort(key=lambda pair: pair[1])
>>> pairs
[(4, 'four'), (1, 'one'), (3, 'three'), (2, 'two')]
```


## lamda as function call arguments

```py

>>> def f1(x = lambda: print("This is Mr. Lambda")): x()
... 
>>> 
>>> f1()
This is Mr. Lambda
>>> 
```