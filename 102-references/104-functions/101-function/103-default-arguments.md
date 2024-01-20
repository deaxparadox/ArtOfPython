## Default Argument Values

The most usefulll is to specify a default value for one or more arguments. This creates a function that can be called with fewer arguments than it is defined to allow:

```python

def ask_ok(prompt, retries=4, reminder="Please try again!"):
    while True:
        ok = input(prompt)
        if ok in ("y", 'ye', "yes"):
            return True 
        if ok in ("n", 'no', 'nop', 'nope'):
            return False 
        retries = retries - 1
        if retries <= 0:
            raise ValueError("invalid user response")
        print(reminder)

ask_ok("Enter: ")
```

```bash
$ python functions.py 
Enter: 2
Please try again!
Enter: 3
Please try again!
Enter: y
```

- The default values are evaluated at the point of function definition in the *definition scope*, it mean the following example:

```python
i = 5
def f(arg=i):
    print('arg:', arg, 'i:', i)
i = 6
f()

# output
arg: 5 i: 6
```

**important warninig:** The defualt value is evaluated only once. This makes a difference when the default is a mutable object such as a list dictionary, or instances of most classes.

- For example, the following function accumulates the arguments passed to it on subsequent calls:

```python

def f(a, L=[]):
    L.append(a)
    return L 

print(f(1))
print(f(2))
print(f(3))

# output
[1]
[1, 2]
[1, 2, 3]
```

- If you don't want the default to be shared subsquent calls, you can write the function like this instead:

```python

def f(a, L=None):
    if L is None:
        L = []
    L.append(a)
    return L

print(f(1))
print(f(2))
print(f(3))

# output
[1]
[2]
[3]
```

[<<< return](102-return-Statement.md) ... [Keyword Argument >>>](104-keyword-arguments.md)