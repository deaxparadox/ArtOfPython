# `assert` statement

Also known as Asesertion is used for testing, whenever a condition is test using *assert* statement, if a condition return True, *assert* let the code after it run and if a condition return False, it raise an `AssertionError`.

In first case we are going to see that the condition return True.

```py
a = 0

assert a == 0

print("Finished")
```

```output
Finished
```

In next we are getting `AssertionError` because condition return False, and print does not get executed:

```py
a = 0

assert a == 1

print("Finished")
```

```output
Traceback (most recent call last):
  File "/home/creator/Documents/Paradox/Github/ArtOfPython/Examples/main.py", line 3, in <module>
    assert a == 1
AssertionError
```