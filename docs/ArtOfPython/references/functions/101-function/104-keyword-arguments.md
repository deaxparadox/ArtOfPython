# Keyword Arguments

Functions can also be called using `keyword arguments` of the form `kwarg=value`. For instance, the following function: 

### Keyword argument without default: 

```python

def add(a, b):
    return a + b
print(add(1,2))
print(add(a=1,b=2))
print(add(b=1,a=2))
print(add(a=2))
```

```bash
3
Traceback (most recent call last):
  File "/home/creator/Documents/Paradox/Github/ArtOfPython/Examples/functions.py", line 93, in <module>
    print(add(a=2))
TypeError: add() missing 1 required positional argument: 'b'
```

- If keyword are used to specify their values, then order doesn't matter.



### Keyword argument with defaults:

```python
def operation(a=1, b=13, operator="+"):
    match operator:
        case "-":
            return a - b
        case "*":
            return a * b
        case _:
            return a + b
        
print("Addition")
print(operation())
print(operation(a=12, b=12))
print(operation(a=12))
print(operation(b=12))

print("Subtraction")
print(operation(operator="-"))
print(operation(a=12, b=12, operator="-"))
print(operation(operator="-", a=12))
print(operation(b=12, operator="-"))
```

```bash
Addition
14
24
25
13
Subtraction
-12
0
-1
-11
```

## Combined Arguments

```python

def combine_argument(a, b, operator="+"):
    match operator:
        case "-":
            return a - b
        case "*":
            return a * b
        case _:
            return a + b

# use cases

print("Addition")
print(combine_argument(1,2))
print(combine_argument(a=1,b=2))
print(combine_argument(b=1,a=2))

print("Subraction")
print(combine_argument(1,2, operator="-"))
# print(combine_argument(operator="-", 1,2))      # error positional argument must be used before default argument
print(combine_argument(a=1,b=2))
print(combine_argument(b=1,a=2))
```

```bash
Addition
3
3
3
Subraction
-1
3
3
```



## `*name`

This type of parameter receives a typle containing the positional arguments beyond the formal parameter list.

```python
def func(*args):
    print(args)
    sum = 0
    for i in args:
        sum += i
    return 

print(func(1,2,3))

```output
(1, 2, 3)
6
```

## `**name` 

This type of parameter receives a dictionary containing all keyword arguments except for those corresponding to a formal parmeter.

```python
def func(**kwargs):
    print(kwargs)
    for k in kwargs:
        print(k, kwargs[k])
    return 

func(a=1, b=2, c=3)

# output
{'a': 1, 'b': 2, 'c': 3}
a 1
b 2
c 3
```

## Combining both args and kwargs

```python
def func(*args, **kwargs):
    print(args)
    print(kwargs)

func(1,2,3, a=4,b=5,c=6)

# output
(1, 2, 3)
{'a': 4, 'b': 5, 'c': 6}
```