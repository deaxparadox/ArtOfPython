# try-except statement

`try-except` statement is used to testing a block of code. First, `try` execute a piece of code if not error is caused in it, then control flow continue after `try` statement, and if any kind of error occur in that piece of code, then `execept` get executed, and code flow continue after `except` block:

We will take example form `assert` code:


```py
a = 0

try:
    assert a == 0
    print("after assertion was successful")
except:
    print("assert condition failed!")

print("Finished")
```

```output
after assertion was successful
Finished
```

As you can see here assert condition return True therefore, try block ran successfully.

Now in assert condition replace 0 with 1:


```py
a = 0

try:
    assert a == 1
    print("after assertion was successful")
except:
    print("assert condition failed!")

print("Finished")
```

```output
assert condition failed!
Finished
```

Like this you test a piece of code in `try-except` statement.

### else clause

The `else` clause when used in `try-except`, in executed if `try` block is success. Let's understand with an example. First, we will code a *try-except-else* block, without defining a variable we want:

```py
In [38]: try:
    ...:     print(b)
    ...: except:
    ...:     print("`b` not found")
    ...: else:
    ...:     print("b found in try")
    ...: 
`b` not found

In [39]: 
```

As you can see, when we run the code, *print* statement in except block is executed. Now, we'll define and declare variable `b`, then run the code again.

```py
In [39]: b = 2

In [40]: try:
    ...:     print(b)
    ...: except:
    ...:     print("`b` not found")
    ...: else:
    ...:     print("b found in try")
    ...: 
2
b found in try

In [41]: 
```

This time we are getting *print* function executed in from *try* and *else*. Because, try block of success, therefore else block also executed.

### finally clause

The `finally` in `try-except` statement block used to cleaning or running the final code. Either of the block `try` or `except` runs, `finally` block will run in the end.

```py
a = 1
b = 2
d = 4


try: print(a)
except: print(b)
finally: print(d)

# output
# 1
# 4
```


```py
b = 2
d = 4


try: print(a)
except: print(b)
finally: print(d)

# output
# 2
# 4
```