# Numbers


[<<< Topics](README.md) | [Variables >>>](102-variables.md)

----------



- [Numeric Types](#numeric-types)
- [Operation on Integers](#operation-on-integers)
    - [Addition](#1-addition)
    - [Subtraction](#2-subtraction)
    - [Multiplication](#3-mutliplication)
    - [Division](#4-division)
    - [Remainder](#5-remainder)
- [Using Parentheses](#using-parentheses)
- [Calculating Power](#calculating-power)




The intepretor acts as a simple calculator: you can type an expression at it and it will write the value.

Expression syntax is straightforward, following operations using their operators can be performed:

- `+` Addition
- `-` Subtraction
- `*` Multiplication
- `/` Division
- `%` Remainder

Parentheses `()` can be used for grouping operations.


### Numeric Types

The numbers are of two basic types: 

1. `int()` integers, such as -1, 0, 1, 2, etc
2. `float()` floats: fractional part integer, such as -2.0, 0.0, 2.23, etc.


### Operation on integers

#### 1. Addition

Here, addition (or sum) will be performed between two numbers.

```py
>>> 2 + 2
4
>>> -1 + 4
3
>>> 
```

#### 2. Subtraction

We are going to performed subtract operation.


```py
>>> 2 - 2
0
>>> 10 - 3
7
>>> -1 - 15
-16
>>> 
```

#### 3. Mutliplication

We are going to perform multiplication operation.

```py
>>> 5 * 6
30
>>> -9 * 12
-108
>>> 
```

#### 4. Division

We are going to look divion operation.

```py
>>> 8 / 5
1.6
>>> 
```

By default division always returns a *floating point number*. This type of division is called `classic division`. 

To get a integer return value, we have to use `floor division` using `//` operator. Let's look at the example of `floor division`:

```py
>>> 8 // 5
1
>>> 
```

**Floor division are useful when you want to divide an array using length, which required a integer value**.

#### 5. Remainder

To find the remainder, we use the `%` operator:

```py
>>> 12 % 7
5
>>> 9  % 2
1
>>> 
```


### Using Parentheses

Parenthese are used for grouping numeric operations.

```py
>>> # If we don't used the parentheses
>>> 2 * 3 + 3
9
>>> 
>>> # If we use parentheses
>>> 2 * (3 + 3)
12
>>> 
```


### Calculating power

The `**` operator are used to calculate powers. 

```py
>>> 2 ** 7      # 2 to the power of 7
128
>>> 
>>> 
>>> 5 ** 2      # 5 squared
25
>>> 
```

----------



There is full support for floating point; operators with mixed operands convert the integer operand to floaing point:

```py
>>> 4 * 3.75 - 1
14.0
```

[Text >>>](103-text.md)

[<<< Topics](README.md) | [Variables >>>](102-variables.md)