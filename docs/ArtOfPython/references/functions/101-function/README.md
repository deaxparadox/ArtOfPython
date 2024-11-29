# Functions

## Defining Functions

We can create a function that writes the Fibonacci series to an arbitrary boundary:


```python
def fib(n):
    # print a Fibonacci series up to n.
    a = 0
    b = 1
    while a < n:
        print(a, end=" ")
        a = b
        b = a + b 
    print()

# executing functions.
fib(10)

# output
0 1 2 4 8 
```

- The keyword `def` introduces a function *definition*. It must be followed by the function name and the parenteized list of romat parameters. The statements that form the body of the function start at the next line, and must be intended.


[<<< README.md](README.md) ... [Keyword Argument >>>](102-return-Statement.md)