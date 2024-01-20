# `raise` statement

The *raise* statement in Python is used to raise error, it cause to program in exit.

Create a file `main.py` and put the following code in it:

```py
# main.py

raise ValueError

print("I not going to be printed in terminal.")
```

When you run this file, you will get output:

```py
Traceback (most recent call last):
  File "/home/creator/Documents/Paradox/Github/ArtOfPython/Examples/main.py", line 1, in <module>
    raise ValueError
ValueError
```

your *print* hadn't ran yet, because before it can be executed error was raise which cause the program to stop.
