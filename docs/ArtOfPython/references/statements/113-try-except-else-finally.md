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

...

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