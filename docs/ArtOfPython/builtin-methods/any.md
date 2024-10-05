# `any()` function


- Return `True` if any element of the *iterable* is true. 

```py
a = [True, False]

status = any(a)
print(status)
```

```output
True
```

- If the iterator is empty, return `False`

```py
a = []

status = any(a)
print(status)
```

```output
False
```

## Examples

- You can also supply expression inside an iterable

Example 1:

```py
a = [1 == 2, False]

status = any(a)
print(status)

# output
# False
```

Example 2:

```py
a = [1 == 1, False]

status = any(a)
print(status)

# output
# True
```