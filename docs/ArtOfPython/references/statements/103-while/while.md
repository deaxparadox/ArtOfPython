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

### `break` Statement

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

### `continue` Statement

```python
count = 0
while count <= 5:
    if count == 3:
        count += 1
        continue
    print(count)
    count += 1
```


### `else` clauses

- The *else* clause in while loop is executed when the while loop is exhausted.

```python
In [26]: 
    ...: count = 0
    ...: while count < 5:
    ...:     print(count)
    ...:     count += 1
    ...: else:
    ...:     print("Counter is greator than 5")
    ...: 
0
1
2
3
4
Counter is greator than 5
```

- In the following example, the *while* loop is terminated in between, therefore *else* block will not be executed.

```py
In [22]: counter = 0

In [23]: while counter<5:
    ...:     print(counter)
    ...:     if counter == 2:
    ...:         break
    ...:     counter+=1
    ...: else:
    ...:     print("Else block is executed")
    ...: 
0
1
2
```