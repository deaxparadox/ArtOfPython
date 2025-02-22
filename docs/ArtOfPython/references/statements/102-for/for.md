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



# *for* Loop

Python *for* loop is used  for sequential traversal i.e. It is used for iteration over an iterable like `string`, `list`, `tuple` and `dict`

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



### `for-else` Usage

The *else* clause can e applied to *for* loop. When we apply the *else* to for loop, the *else* condition is executed if *for* loop is exhausted, it means if the *for* loop is breaked in between the execution, the *else* block will not be executed. But, if *for* loop is not terminated, and passes all the conditions happily passing all cases, then *else* block will not be executed.

The following example demonstrate, that all the condition are passed, the *else* block will be executed:

```py
In [11]: for i in range(10):
    ...:     print(i, end=" ")
    ...: else:
    ...:     print("\nElse loop is exhaunted")
0 1 2 3 4 5 6 7 8 9 
Else loop is exhaunted
```

The following example demonstrate, that the *else* block will be terminated if certain condition is matched, and *else* block will not be executed:

```py
In [15]: for i in range(13):
    ...:     print(i, end=" ")
    ...:     if i == 11:
    ...:         break
    ...: else:
    ...:     print("\nElse loop is exhaunted")
    ...: 
0 1 2 3 4 5 6 7 8 9 10 11 
```