<!-- Syntax -->
<!-- iterating with range -->
<!-- control with break -->
<!-- control with continue -->
<!-- iterating over list -->
<!-- iterating over tuple -->
<!-- iterationg over dictionary -->
<!-- iterationg over string -->
<!-- iterating over a matric -->
<!-- iterating next with while loop -->
<!-- Synchronous Iterator using OOPs __iter__ and __next__ -->
<!-- Asynchronous Iterator using OOPs, __aiter__ and __anext__ -->
<!-- Generator examples -->


# `for` Loop

Python `for` loop is used  for sequential traversal i.e. It is used for iteration over an iterable like `string`, `list`, `tuple` and `dict`

Syntax:

```py
for var in iterable:
    # code block
```

Each element of iterable is assign to *var*, and for each assignment to *var*, *code block* is execute once.

Simple Example:

```py
for i in range(10):
    print(i)
```

```output
0
1
2
3
4
5
6
7
8
9
```

- `range()` function is a Sequence type, which returns an iterable.






