
## Iteration: iter(), next(), while loop, try-except statement

Now we are goint to iterate over tuple using builtin function:

```py
a = (0, 1, 2)


i = iter(a)

print(next(i))
print(next(i))
print(next(i))
print(next(i))
```

```output
0
1
2
Traceback (most recent call last):
  File "/home/creator/Documents/Paradox/Github/ArtOfPython/Examples/examples.py", line 16, in <module>
    print(next(i))
StopIteration
```

You can see if try to print after 3 element it's raise `StopIteration` error. Here are writing `next` multiple time to get the value from `iter`. We an automate this process using *while* loop.

```py
a = (0, 1, 2)

i = iter(a)

while True:
    print(next(i))
```

```output
0
1
2
Traceback (most recent call last):
  File "/home/creator/Documents/Paradox/Github/ArtOfPython/Examples/examples.py", line 7, in <module>
    print(next(i))
StopIteration
```

As you can see we are not printing tuple using while loop. But, one thing is that we are still getting *StopIteration* error whenever we try to access empty, after all the value from the tuple are taken out. There must be a way to suppres this error.

We can suppress this error using `try-except` block, inside the while loop.

```py
a = (0, 1, 2)

i = iter(a)

while True:
    try:
        print(next(i))
    except:
        break
```

```output
0
1
2
```

Here, whenevery *StopIteration* error is raise, *block* supressing the error and control is given to *except block*, which then break the loop.


