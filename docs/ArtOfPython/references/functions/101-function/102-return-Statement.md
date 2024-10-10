
## return statements


It is simple to write a function that returns a list of the numbers of the fibonacci series, instead of printing it:

```python

def fib(n):
    # print a Fibonacci series up to n.
    result = []
    a = 0
    b = 1
    while a < n:
        result.append(a)
        a = b
        b = a + b 
    return result

print(fib(10))

# output
[0, 1, 2, 4, 8]
```

- The `return` statement returns witha value from a function. return without an expression argument returns None. Falling off the end of a function also returns None.

[<<< functions](101-functions.md) ... [Keyword Argument >>>](103-default-arguments.md)