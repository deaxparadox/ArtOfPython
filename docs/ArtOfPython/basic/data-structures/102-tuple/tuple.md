<!-- syntax -->
<!-- variable -->
<!-- Some example of tuple creation -->
<!-- length of -->
<!-- iteration: using for loop -->
<!-- concatenation -->
<!-- indexing -->
<!-- slicing -->


<!-- Advance -->
<!-- iteration: using for while, try-except -->
<!-- unpacking with `*tuple` -->


# `tuple` Python

## Syntax 

`tuple` are created using the `()` square bracket, and inbetween square bracket we put our comma-separated object. 

- I'm using term object here because everything in python is object.

```py
(...)
```

## Variable

We know the syntax, now we are going to created variable of *tuple*. Varaible is way to hold the *tuple* so we can use it in program for storing data at runtime.

Let's dive into, and create a empty tuple `a`:

```py
a = ()

print(a)
```

```output
()
```

So we have, created a empty tuple.


## Examples

Example 1: We are going to created a tuple of integer, range from 0-9:

```py
a = (0,1,2,3,4,5,6,7,8,9)
print(a)
```

```output
(0, 1, 2, 3, 4, 5, 6, 7, 8, 9)
```

Example 2: We are going to created a tuple of integer, range from 0-9, using `range` function:

```py
a = tuple(range(10))
print(a)
```

```output
(0, 1, 2, 3, 4, 5, 6, 7, 8, 9)
```

- Basicallly `tuple()` function is an builtin function, it except an *iterable* and create a tuple from it, and return that *tuple*.

```

```output
(0, 1, 2, 3, 4, 5, 6, 7, 8, 9)
```

## Length of tuple

We can find the length of tuple, using `len()` builtin function:

```py
a = (0, 1, 2, 3, 4, 5, 6, 7, 8, 9)

# length of tuple
print(len(a))
```

```output
10
```


# Iteration: for loop

We can iterate over the tuple using `for` loop:

```py
a = (0, 1, 2, 3, 4, 5, 6, 7, 8, 9)

for i in a:
    print(i, end=" ")
```

```output
0 1 2 3 4 5 6 7 8 9
```

## Concatenation

Just like string we can concatenation, or simply add two tuple:


```py
a = (0,1,2)
b = (3,4,5)

c = a + b
# c = (0,1,2) + (3,4,5)

print(c)
```

```output
(0, 1, 2, 3, 4, 5)
```


## Indexing

Indexing is technique of accessing individual element from the tuple. By default indexing start from 0.

Let's dive into examples, and see how we can access the first element from the tuple.


```py
a = tuple(range(1, 10))
print(a)

# accessing the first element from the tuple, using index 0
print(a(0))
```

```output
1
```

`<tuple>(index)` is called indexing.

To access fifth element from the tuple, we have to use the *index 4*.

```py
a(4)
```

```output
5
```

So, if you want to access *7th* element from the tuple, to calculate the index, we do *7 - 1 = 6*, wich is the index position of *7th* element. 
Generally, the way to calculate the index is, if you want to access *nth* element from the tuple, then index of *nth* element is *n - 1*.

You can also use the negative indexing to access elements from the end, to access last element:

```py
a = tuple(range(1, 10))
print(a)

# accessing last element
print(a(-1))
```

```output
(1, 2, 3, 4, 5, 6, 7, 8, 9)
9
```

now, to access second last element:

```py
a = tuple(range(1, 10))
print(a)

# accessing second last element
print(a(-2))
```

```output
(1, 2, 3, 4, 5, 6, 7, 8, 9)
8
```



<!-- ADVANCE -->
