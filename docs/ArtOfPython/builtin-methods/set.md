# `set`

```python
>>> class set([iterable])
```

Return a new set or frozenset object whose elements are taken from *iterable*. 

- The elements of a set must be `hashable`.
- To represent sets of sets, the inner sets must be `frozenset` objects.
- If *iterable* is not specified, a new empty set is returned.

Sets can be created by several means:

- Use a comma-separated list of elements within braces: `{'jack', 'sjoerd'}`

Use a set comprehension: `{c for c in 'abracadabra' if c not in 'abc'}`

Use the type constructor: `set()`, `set('foobar')`, `set(['a', 'b', 'foo'])`