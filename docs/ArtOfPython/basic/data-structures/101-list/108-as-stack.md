# `list` as Stacks

- The list methods make it very easy to use a list as a stack, where the last element added is the first element retreived ("last-in", "first-out"). To add an item to the top of the stakc use, `append()`. 

- To retrieve an item from the top of the stack, use `pop()` without an explicit index.

```python
>>> stack = [3, 4, 5]
>>> stack.append(6)
>>> stack.append(7)
>>> stack
[3, 4, 5, 6, 7]
>>> stack.pop()
7
>>> stack
[3, 4, 5, 6]
>>> stack.pop()
6
>>> stack.pop()
5
>>> stack
[3, 4]
```