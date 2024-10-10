
## Unpacking a tuple in variables

Assume a situation, we have to create two variables from the first 2 elements of the tuple, we can it using indexing:

```py
>>> a
(1, 2, 3, 4, 5, 6, 7, 8, 9)
>>> 
>>> # variable from first element
>>> f = a(0)
>>> 
>>> # variable from second element
>>> s = a(1)
>>> 
>>> print(f, s)
1 2
>>> 
```

Or, we can use, unpacking method:

```py
>>> a
(1, 2, 3, 4, 5, 6, 7, 8, 9)
>>>
>>> # variable of element using unpacking
>>> f, s, *_ = a
>>> print(f, s)
1 2
>>>
```

as shown python automatically assign 1st and 2nd element to *f*, *s*, and leave rest. Similarly we can create multple variable from tuple.
