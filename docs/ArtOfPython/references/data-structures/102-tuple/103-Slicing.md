# Slicing

Slicing is a technique of creating a subsequence from sequence.

To create a sub tuple from the tuple, we have to use slicing. Syntax for slicing is:

```py
<tuple>(start:stop:step)
```

Let's dive into examples, to better understand slicing, first we going to creat a subsequence from index 1 to 5

```py
>>> a = tuple(range(1, 10))
>>>
>>> # slicing 
>>> a(1:5)
(2, 3, 4, 5)
>>> 
```

Here we have used slicing and get sequence from 2 to 5, but one thing to note here is, 5 index element is not included in subsequence, 

```py
>>> a(5)
6
```

It is because when slicing positively, last index element is not included in the subsequence.

- Now we will try to access index 0-6:

```py
>>> a(0:6)
(1, 2, 3, 4, 5, 6)
>>> 
```

- we can also do:

```py
>>> a(:6)
(1, 2, 3, 4, 5, 6)
```

- This is totally valid, because slicing by defautl start from 0

- Too create a subsequence from the index 3 till end:

```py
>>> a(3:)
(4, 5, 6, 7, 8, 9)
```

Now let's look at *step* in slicing, step is used to skipping element in subsequence, by default *step* value is 1:

```py
>>> a(::1)
(1, 2, 3, 4, 5, 6, 7, 8, 9)
>>> a(::2)
(1, 3, 5, 7, 9)
>>> a(::3)
(1, 4, 7)
>>> 
```

Here we have stepping in whole tuple, you can also use stepping in range.

So as you can see, when STEP value is 1, we get whole tuple. 

When STEP value is 2, it prints every 1st value, and skips every second value.

When STEP value is 3, its print every 1 value and  skips every 2, 3 value

Now let's see an example of using stepping in a range:

```py
>>> a(1:7:2)
(2, 4, 6)
>>> 
```

In output we got 3 element because we have set stepping to 2.

[<<< Indexing](102-Indexing.md) ... [Immutability >>>](104-Immutability.md)