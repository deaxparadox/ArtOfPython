# Dictionary Operations

## Adding Values

```python
>>> tel = {'jack': 4098, 'sape': 4139}
>>> 
>>> # Added key-value
>>> tel['guido'] = 4127
>>> print(tel)
{'jack': 4098, 'sape': 4139, 'guido': 4127}
```

## Accessing Values

```python
>>> tel['jack']
4098
```

## Deleting Values

```python
>>> del tel['sape']
>>> tel['irv'] = 4127
>>> tel
{'jack': 4098, 'guido': 4127, 'irv': 4127}
```

## Converting dictionary to items

```python
>>> list(tel)
['jack', 'guido', 'irv']
```

- only key are exported to `list` function, and a new is formed of keys.

## Sorting 

```python
>>> sorted(tel)
['guido', 'irv', 'jack']
```

## Membership operation

```python
>>> 'guido' in tel
True
>>> 'jack' not in tel
False
```