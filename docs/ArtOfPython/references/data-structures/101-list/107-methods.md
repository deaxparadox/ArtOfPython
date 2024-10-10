# list methods


- **list.append()**
    Add an item to the end of the list.
- **list.extend()**: Extend the list by appending all the items from the iterable.
- **list.insert(i, x)**: Insert an item at a given position. The first argument is the index of the element before which, to insert, so `a.insert(0, x)` inserts at the front of the list, and `a.insert(len(a), x)` is equivalent to `a.append(x)`.
- **list.remove(x)**: Remove the first item from the list whose value is equal to x. It raise a `ValueError` if there is no such item.
- **list.pop([i])**: Remove the item at the given position in the list, and return it. If not index is specified, `a.pop()` removes and returns the last item of the list.
- **list.clear()**: Remove all items from the list. Equivalent to `del a[:]`.
- **list.index(x[, start[,end]])**: Return zero-based index in the list of the  first item whose value is equal to x. Raise a **ValueError** if there is no such item.
- **list.count(x)**: Return the number of items x appears in the list.
- **list.sort(*, key=None, reverse=False)**: Sort the items of the list in place (the arguments can be used for sort customization, see **sorted()** for their explanation).
- **list.reverse()**: Reverse the elements of the list in place.
- **list.copy()**: Return a shallow copy of the list. 

```python
>>> fruits = ['orange', 'apple', 'pear', 'banana', 'kiwi', 'apple', 'banana']
>>> fruits.count('apple')
2
>>> fruits.count('tangerine')
0
>>> fruits.index('banana')
3
>>> fruits.index('banana', 4)  # Find next banana starting at position 4
6
>>> fruits.reverse()
>>> fruits
['banana', 'apple', 'kiwi', 'banana', 'pear', 'apple', 'orange']
>>> fruits.append('grape')
>>> fruits
['banana', 'apple', 'kiwi', 'banana', 'pear', 'apple', 'orange', 'grape']
>>> fruits.sort()
>>> fruits
['apple', 'apple', 'banana', 'banana', 'grape', 'kiwi', 'orange', 'pear']
>>> fruits.pop()
'pear'
```