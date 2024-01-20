# List as `queues`

It is also possible to use a list as a queue, where the first element added is the first element retrieved (“first-in, first-out”);

-  While appends and pops from the end of list are fast, doing inserts or pops from the beginning of a list is slow (because all of the other elements have to be shifted by one).

```py
>>> 
>>> a = [1, 2, 3]           # list created
>>> 
>>> 
>>> a.insert(0, 0)          # inserting at index 0, value 0
>>> a
[0, 1, 2, 3]
>>> 
>>> # remove item at index 0
>>> a.pop(0)
0
>>> a
[1, 2, 3]
>>> 
>>> a.insert(0, 10)         # inserting at index 0, value 10
>>> a
[10, 1, 2, 3]
>>> 
```

We can also implement a queue using `collections.deque` which is designed to fast append and pop from both ends:

```py
>>> from collections import deque
>>> queue = deque(["Eric", "John", "Michael"])
>>> queue.append("Terry")           # Terry arrives
>>> queue.append("Graham")          # Graham arrives
>>> deque(['Eric', 'John', 'Michael', 'Terry', 'Graham'])
>>> queue.popleft()                 # The first to arrive now leaves
'Eric'
>>> queue.popleft()                 # The second to arrive now leaves
'John'
>>> queue                           # Remaining queue in order of arrival
deque(['Michael', 'Terry', 'Graham'])
>>> 
>>> queue.appendleft("Wright")      # Write arrvies late, but given first position
>>> queue
deque(['Wright', 'Michael', 'Terry', 'Graham'])
>>> 
```