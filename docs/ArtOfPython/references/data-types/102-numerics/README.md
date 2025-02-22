# Numeric Types

Python's clore objects set includes the usual: 

- *Integers*: that have not fractional part
- *Floating-Points*: number that contain fractional part
- *Complex* numbers with imaginary parts
- *Decimals* with fixed precision
- *Rationals* with numerator and denominator
- *Sets* collections with numeric operations
- *Booleans*: `true` and `false`
- Built-in functions and modules: **round**, **math**, **random**, etc.
- Expressions; unlimited integer precision, bitwise operations; hex, octal, and binary formats
- Third party extensions: vectors, libraries, visualization, plotting, etc.

Numbers in Python support the normal mathematical operations. For instance the plus sign (+) performs addition, a star (*) is used for multiplication, and two star (**) are used for exponentiation:

```py
>>> 123 + 222               # Integer addition
345
>>> 1.5 * 4                 # Floating-point multiplication
4.5
>>> 2 ** 100                # 2 to the power 100, again
1267650600228229401496703205376
>>>
```


### Built-in Numeric Tools

Python provides a set of tools for processing number objects:

*Expression operators*

```
+, -, *, /, >>, **, &, etc.
```

*Built-in mathematical functions*

```
pow, abs, round, int, hex, bin, etc.
```

*Utility modules*

```
random, math, etc
```

### Python Expression Operators

*Expression*: a combination of numbers (or other objects) and operators that computers a value when executed by Python.

For instace, to add two number **X** and **Y** you would say **X + Y**, which tell Python to apply the **+** operator to the values named by **X** and **Y**. The result of the expression is the sum of **X** an **Y**, another number object.

![Python expression operators and precedence](/assets/images/python-expression-operator-and-precedence.png)


### Mixed operators follow operator precidence.

When you write an expression with more than one operator, Python groups its part according to what are called *precedence rules*, and this grouping determines the order in which the expression's part are computed:

From above table:

- Operators lower in the table have higher precendence, and so bind more tightly in mixed expressions.
- Operators in the same row generally group from left to right when combined (except for exponentiation, which groups right to left, and comparisons, which chain left to right).

For example, if you write **X + Y * Z**, Python evaluates the multiple first (**Y * Z**), then adds the result to **X** because * have higher precedence (is lower in the table) then **+**.


### Parentheses operators follow operator precedence

You can forget about precedence completely if you's careful to group parts of expressions with parentheses. When you enclose subexpressions in parentheses, you override Python's precendence rules; Python always evaluates expressions in parentheses first before using their results in the enclosing expressions.

For instance, instead of coding **X + Y * Z**, you could write one of the following to force Python to evaluate the expression in the desired order:

```
(X + Y) * Z
X + (Y * Z)
```

In the first case, **+** is applied to **X** and **Y** first, becuase this subexpression is wrapped in parentheses.

In the second case, the * is performed first.

Adding parentheses in large expressions is good.


### Mixed types are converted up