<!-- syntax -->
<!-- variable -->
<!-- Some example of list creation -->
<!-- length of -->
<!-- iteration: using for loop -->
<!-- concatenation -->
<!-- repetition -->
<!-- indexing -->
<!-- change value in list -->
<!-- deleting value in list -->
<!-- slicing -->


<!-- Advance -->
<!-- iteration: using for while, try-except -->
<!-- unpacking list in variables -->
<!-- unpacking with `*list` -->


<!-- listmethods -->
<!-- append() -->
<!-- pop() -->
<!-- insert() -->
<!--  -->

# `list` Python

## Syntax 

`list` are created using the `[]` square bracket, and inbetween square bracket we put our comma-separated object. 

- I'm using term object here because everything in python is object.

```py
[...]
```

## Variable

We know the syntax, now we are going to created variable of *list*. Varaible is way to hold the *list* so we can use it in program for storing data at runtime.

Let's dive into, and create a empty list `a`:

```py
a = []

print(a)
```

```output
[]
```

So we have, created a empty list.


## Examples

Example 1: We are going to created a list of integer, range from 0-9:

```py
a = [0,1,2,3,4,5,6,7,8,9]
print(a)
```

```output
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
```

Example 2: We are going to created a list of integer, range from 0-9, using `range` function:

```py
a = list(range(10))
print(a)
```

```output
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
```

- Basicallly `list()` function is an builtin function, it except an *iterable* and create a list from it, and return that *list*.


Example 3:

- We can also create list using *list comprehension*:

```py
a = [x for x in range(10)]
print(a)
```

```output
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
```

## Length of list

We can find the length of list, using `len()` builtin function:

```py
a = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# length of list
print(len(a))
```

```output
10
```


# Iteration: for loop

We can iterate over the list using `for` loop:

```py
a = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

for i in a:
    print(i, end=" ")
```

```output
0 1 2 3 4 5 6 7 8 9
```

## Concatenation

Just like string we can concatenatie, or simply add two list:


```py
a = [0,1,2]
b = [3,4,5]

c = a + b
# c = [*a] + [*b]
# c = [0,1,2] + [3,4,5]

print(c)
```

```output
[0, 1, 2, 3, 4, 5]
```
