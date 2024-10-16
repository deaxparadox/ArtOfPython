

## Control with `continue`

Now if i want to skip, any specific range while iterating, i can do that with continue statement. Now i am going to skip values from 3-8, including end elements:

```py
for i in range(10):
    if i >= 3 and i <=8:
        continue
    print(i)
```

```output
0
1
2
9
```