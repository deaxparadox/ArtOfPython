# How to concatenate a dictionary


```py
import typing


class adict(dict):
    def __add__(self, other: dict):
        return {**self, **other}

a = adict(a=1, b=2)
b = adict(c=1, d=2)
d = a + b
print(d)
```

```output
{'a': 1, 'b': 2, 'x': 2, 'y': 4}
```