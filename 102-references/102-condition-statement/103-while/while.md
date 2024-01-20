# `while` Statements

The `while` is usefull for cases where you want to iterate over some code, until some condition meet, or infinitely.

- Infinite loop:

```python
>>> while True:
...     print("Hello EveryWhereLinux!")
... 
Hello EveryWhereLinux!
Hello EveryWhereLinux!
^CTraceback (most recent call last):
  File "<stdin>", line 2, in <module>
KeyboardInterrupt
Hello EveryWhereLinux!>>> 
>>> 
```

- Conditiona based while loop:

```python
count = 0
while count <=5:
    print(count)
    count += 1

# output
0
1
2
3
4
5
```

## `break` Statement

```python
count = 0
while count <= 5:
    if count == 3:
        break 
    print(count)
    count += 1

# output
0
1
2
```

## `continue` Statement

```python
count = 0
while count <= 5:
    if count == 3:
        count += 1
        continue
    print(count)
    count += 1
```


## `else` clauses

- `else` clause in while loop is executed when condition become False.

```python
count = 0
breaker = True
while breaker:
    if count >= 5:
        breaker = False
    print(count)
    count += 1
else:
    print("Counter is greator than 5")
```