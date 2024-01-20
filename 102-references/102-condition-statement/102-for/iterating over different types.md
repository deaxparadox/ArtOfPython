

## Iterating over `list` type

This code uses a for loop to iterate over a list of strings, printing each item in the list on a new line. The loop assigns each item to the variable `i` and continues untill all items in the `list` have been processed.

```py
l = ['python', 'for', 'beginners']

for i in l:
    print(i)
```

```output
python
for
beginners
```

## Iterating over `tuple` type

This code uses a for loop to iterate over a tuple of strings, printing each item in the tuple on a new line. The loop assigns each item to the variable `i` and continues untill all items in the `tuple` have been processed.

```py
l = ('python', 'for', 'beginners')

for i in l:
    print(i)
```

```output
python
for
beginners
```

## Iterating over `dict` type

This code uses a for loop to iterate over a `dict` and print each key-value pair or a new line.

```py
d = {'a': 1, 'b': 2, 'c': 3}

for k in d:
    print(k, d[k])
```

```output
a 1
b 2
c 3
```

## Iterating over `string` type

Now i am going to iterate over `string`:

```py
s = "python for beginners"

for c in s:
    print(c)
```

```output
p
y
t
h
o
n
 
f
o
r
 
b
e
g
i
n
n
e
r
s
```

# Iterating over Matrix

In this example i am iterating over matrix and accessing single value at a time.

```py
a = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]

for sa in a:
    for i in sa:
        print(i)
```

```output
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

To access all values in list in a:

```py
a = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]

for a,b,c in a:
        print(a, b, c)
```

```output
1 2 3
4 5 6
7 8 9
```
