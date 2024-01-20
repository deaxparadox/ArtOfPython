# break and continue Statements, and else Clauses on Loops

## `break` statements

The `break` statement, breaks out of the innermost enclosing `for` or `while` loop.

```python
for n in range(2, 10):
    for x in range(2, n):
        if n % x == 0:
            print(n, 'equals', x, '*', n//x)
            break 
    print(n, 'is a prime number')

# output
2 is a prime number
3 is a prime number
4 equals 2 * 2
4 is a prime number
5 is a prime number
6 equals 2 * 3
6 is a prime number
7 is a prime number
8 equals 2 * 4
8 is a prime number
9 equals 3 * 3
9 is a prime number
```

## `continue` statement

The `continue` statement, continues with the next iteration of the loop.

```python
for num in range(2, 10):
    if num % 2 == 0:
        print("Found an even number:", num)
        continue
    print("Found an odd number", num)

# output
Found an even number: 2
Found an odd number 3
Found an even number: 4
Found an odd number 5
Found an even number: 6
Found an odd number 7
Found an even number: 8
Found an odd number 9    
```

## `else` clauses

Loop statements may have an `else` clause, it is executed when the loop terminates through exhaustion of the iterable (with `for`) or when the condition becomes false (with `while`), but not when loop is terminated by a `break` statement.

```python
for n in range(2, 10):
    for x in range(2, n):
        if n % x == 0:
            print(n, 'equals', x, '*', n//x)
            break 
    else:
        print(n, 'is a prime number')

# output
2 is a prime number
3 is a prime number
4 equals 2 * 2
5 is a prime number
6 equals 2 * 3
7 is a prime number
8 equals 2 * 4
9 equals 3 * 3
```