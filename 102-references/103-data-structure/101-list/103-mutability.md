# List: Item Assignment


## Changing the element of the list

Let's see an example, to change the value of *5th* element in the list:

```py
a = list(range(1, 10))
print("list:", a)

# accessing 5th element
print("fifth:", a[4])

# changing the value of 5th element in the list
a[4] = True

# changed list
print("changed list:", a)

# accessing new fifth element
print("new fifth:", a[4])
```

```output
list: [1, 2, 3, 4, 5, 6, 7, 8, 9]
fifth: 5
changed list: [1, 2, 3, 4, True, 6, 7, 8, 9]
new fifth: True
```

Similarly you can change value at inde 7:

```py
# Since we are change element at position 7,
# therefore index of 7th position is 6.

a = list(range(1, 10))
print("list:", a)

print("seventh:", a[6])

a[6] = "EveryWhereLinux"

print("changed list:", a)

print("new seventh:", a[6])
```

```output
list: [1, 2, 3, 4, 5, 6, 7, 8, 9]
seventh: 7
changed list: [1, 2, 3, 4, 5, 6, 'EveryWhereLinux', 8, 9]
new seventh: EveryWhereLinux
```

## Deleting element from the list

To delete an element from the list, we have to use `del` statement, and syntax of acessing element, ex: *del <list>[index]*.

Now we are going to delete, *5th* element from the list.

```py
# deleting 5th element from the list.
# therefore index of 5th element is 4.

a = list(range(1, 10))
print("list:", a)

del a[4]

print("list:", a)
```

```output
list: [1, 2, 3, 4, 5, 6, 7, 8, 9]
list: [1, 2, 3, 4, 6, 7, 8, 9]
```

we have deleted *5th* element, which is 5. Then print the list we can see *5* is gone from list.
