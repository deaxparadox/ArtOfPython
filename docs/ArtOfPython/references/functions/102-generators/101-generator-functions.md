# Generator Functions: yield Versus return

- To write functions that may send back a value and leter be resumed, picking up where they left off. Such functions, are known as *generator functions* because they generate a sequence of values over time.
- Generator functions are like normal functions in most respects, and in fact are coded
with normal def statements.
- However, when created, they are compiled specially into an object that supports the iteration protocol.
- And when called, they don’t return a result: they return a result generator that can appear in any iteration context.

### State suspension: using yield

- difference between generator and normal functions is that a generator yields a value, rather than *returning* one—the **yield** statement suspends the function and sends a value back to the caller, but retains enough state to enable the function to resume from where it left off.
- When resumed, the function continues execution im-mediately after the last yield run.


### Generator functions in action

- The following code defines a generator function that can be used to generate the squares of a series of numbers over time:

```python
>>> def gen_squares(N):
...     for i in range(N):
...             yield i ** 2
... 
>>> 
>>> for i in gen_squares(5):
...     print(i, end=": ")
... 
0: 1: 4: 9: 16: >>> 
```

- If you really want to see what is going on inside the *for*, call the generator function directly:

```python
>>> 
>>> x = gen_squares(4)
>>> x
<generator object gen_squares at 0x7fd9208578b0>
>>> 
```

- You get back a *generator object* that supports the iteration protocol--the generator function was compiled to return this automatically.
- The returned generator object in trun has a **__next__** method that starts the function or resumes it from where it last yielded a value, raises a **StopIteration** exception when the end of the series of values is reached and the function returns.

```python
>>> 
>>> next(x)
0
>>> next(x)
1
>>> next(x)
4
>>> next(x)
9
>>> next(x)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
StopIteration
>>> next(x)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
StopIteration
>>> 
```

- generators returns themselves for **iter**, because they support **next** directly. 

```python
>>> y = gen_squares(5)
>>> iter(y) is y
True
>>> next(y)
0
>>> 
```

### Extended generator function protocol: send vs next

The **send** method advances to the next item in the series of results, just like **__next__**, but  also provides a way for to caller to communicate with the generator.


Techincally **yield** is now an expression form that returns the item passed to **send**, not a statement (though it can be called either way -- as yield X, or A = (yield X)).

- The expression must be enclosed the parentheses unless it's the only item on the right isde of the assignment statement.
- For example, **X = yield Y** is OK, as is **X = (yield Y) + 42**.


When this extra protocol is used, values are sent into a generator **G** by calling **G.send(value)**.
- The generator's code is them resumed, and the yield expression in the generator returns the value passed to **send**.