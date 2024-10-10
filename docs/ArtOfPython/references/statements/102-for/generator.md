

# Generator Examples

To convert any function into `generator` use yield statement

```py
def Gen():
    for i in range(10):
        yield i
    yield "Finished"

def main():
    for i in Gen():
        print(i)

main()
```

```output
0
1
2
3
4
5
6
7
8
9
```