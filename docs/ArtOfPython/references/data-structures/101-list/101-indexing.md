

## Indexing

Indexing is technique of accessing individual element from the list. By default indexing start from 0.

Let's dive into examples, and see how we can access the first element from the list.


```py
a = list(range(1, 10))
print(a)

# accessing the first element from the list, using index 0
print(a[0])
```

```output
1
```

`<list>[index]` is called indexing.

To access fifth element from the list, we have to use the *index 4*.

```py
a[4]
```

```output
5
```

So, if you want to access *7th* element from the list, to calculate the index, we do *7 - 1 = 6*, wich is the index position of *7th* element. 
Generally, the way to calculate the index is, if you want to access *nth* element from the list, then index of *nth* element is *n - 1*.

You can also use the negative indexing to access elements from the end, to access last element:

```py
a = list(range(1, 10))
print(a)

# accessing last element
print(a[-1])
```

```output
[1, 2, 3, 4, 5, 6, 7, 8, 9]
9
```

now, to access second last element:

```py
a = list(range(1, 10))
print(a)

# accessing second last element
print(a[-2])
```

```output
[1, 2, 3, 4, 5, 6, 7, 8, 9]
8
```