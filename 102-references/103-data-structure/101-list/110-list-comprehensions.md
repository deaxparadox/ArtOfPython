# List comprehensions

List comprehensions provide a concise way to create lists.

- Common applications are to make new lists where each element is the result of some operations applied to each member of another sequence or iterable, or to create a subsequence of those elements that satisfy a certain condition.

- For example, assume we want to create a list of squares, like:

```python
>>> squares = []
>>> for x in range(10):
...     squares.append(x**2)
... 
>>> squares
[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
```

- Note that this creates (or overwrites) a variable named x that still exists after the loop completes.

We can calculate the list of squares without any side effects using:

```python
>>> squares = list(map(lambda x: x **2, range(10)))
>>> squares
[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
>>> 
```

or `finally` the comprehensions ways.

```python
>>> squares = [x ** 2 for x in range(10)]
>>> squares
[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
>>> 
```

- A list comprehension consists of brackets containing an expression followed by a `for` clause, then zero or more `for` or `if` clauses. The result will be a new list resulting from evaluating the expression in the context of the for and if clauses which follow it.

- For example, this listcomp combines the elements of two lists if the are not equal:

```python
>>> [(x, y) for x in [1,2,3] for y in [3,1,4] if x != y]
[(1, 3), (1, 4), (2, 3), (2, 1), (2, 4), (3, 1), (3, 4)]
```

- and it's equivalent to:

```python
combs = []
for x in [1,2,3]:
    for y in [3,1,4]:
        if x != y:
            combs.append((x, y))

combs
```

Example: 

<pre><span></span><span class="gp">&gt;&gt;&gt; </span><span class="n">vec</span> <span class="o">=</span> <span class="p">[</span><span class="o">-</span><span class="mi">4</span><span class="p">,</span> <span class="o">-</span><span class="mi">2</span><span class="p">,</span> <span class="mi">0</span><span class="p">,</span> <span class="mi">2</span><span class="p">,</span> <span class="mi">4</span><span class="p">]</span>
<span class="gp">&gt;&gt;&gt; </span><span class="c1"># create a new list with the values doubled</span>
<span class="gp">&gt;&gt;&gt; </span><span class="p">[</span><span class="n">x</span><span class="o">*</span><span class="mi">2</span> <span class="k">for</span> <span class="n">x</span> <span class="ow">in</span> <span class="n">vec</span><span class="p">]</span>
<span class="go">[-8, -4, 0, 4, 8]</span>
<span class="gp">&gt;&gt;&gt; </span><span class="c1"># filter the list to exclude negative numbers</span>
<span class="gp">&gt;&gt;&gt; </span><span class="p">[</span><span class="n">x</span> <span class="k">for</span> <span class="n">x</span> <span class="ow">in</span> <span class="n">vec</span> <span class="k">if</span> <span class="n">x</span> <span class="o">&gt;=</span> <span class="mi">0</span><span class="p">]</span>
<span class="go">[0, 2, 4]</span>
<span class="gp">&gt;&gt;&gt; </span><span class="c1"># apply a function to all the elements</span>
<span class="gp">&gt;&gt;&gt; </span><span class="p">[</span><span class="nb">abs</span><span class="p">(</span><span class="n">x</span><span class="p">)</span> <span class="k">for</span> <span class="n">x</span> <span class="ow">in</span> <span class="n">vec</span><span class="p">]</span>
<span class="go">[4, 2, 0, 2, 4]</span>
<span class="gp">&gt;&gt;&gt; </span><span class="c1"># call a method on each element</span>
<span class="gp">&gt;&gt;&gt; </span><span class="n">freshfruit</span> <span class="o">=</span> <span class="p">[</span><span class="s1">'  banana'</span><span class="p">,</span> <span class="s1">'  loganberry '</span><span class="p">,</span> <span class="s1">'passion fruit  '</span><span class="p">]</span>
<span class="gp">&gt;&gt;&gt; </span><span class="p">[</span><span class="n">weapon</span><span class="o">.</span><span class="n">strip</span><span class="p">()</span> <span class="k">for</span> <span class="n">weapon</span> <span class="ow">in</span> <span class="n">freshfruit</span><span class="p">]</span>
<span class="go">['banana', 'loganberry', 'passion fruit']</span>
<span class="gp">&gt;&gt;&gt; </span><span class="c1"># create a list of 2-tuples like (number, square)</span>
<span class="gp">&gt;&gt;&gt; </span><span class="p">[(</span><span class="n">x</span><span class="p">,</span> <span class="n">x</span><span class="o">**</span><span class="mi">2</span><span class="p">)</span> <span class="k">for</span> <span class="n">x</span> <span class="ow">in</span> <span class="nb">range</span><span class="p">(</span><span class="mi">6</span><span class="p">)]</span>
<span class="go">[(0, 0), (1, 1), (2, 4), (3, 9), (4, 16), (5, 25)]</span>
<span class="gp">&gt;&gt;&gt; </span><span class="c1"># the tuple must be parenthesized, otherwise an error is raised</span>
<span class="gp">&gt;&gt;&gt; </span><span class="p">[</span><span class="n">x</span><span class="p">,</span> <span class="n">x</span><span class="o">**</span><span class="mi">2</span> <span class="k">for</span> <span class="n">x</span> <span class="ow">in</span> <span class="nb">range</span><span class="p">(</span><span class="mi">6</span><span class="p">)]</span>
  File <span class="nb">"&lt;stdin&gt;"</span>, line <span class="m">1</span>
    <span class="p">[</span><span class="n">x</span><span class="p">,</span> <span class="n">x</span><span class="o">**</span><span class="mi">2</span> <span class="k">for</span> <span class="n">x</span> <span class="ow">in</span> <span class="nb">range</span><span class="p">(</span><span class="mi">6</span><span class="p">)]</span>
     <span class="pm">^^^^^^^</span>
<span class="gr">SyntaxError</span>: <span class="n">did you forget parentheses around the comprehension target?</span>
<span class="gp">&gt;&gt;&gt; </span><span class="c1"># flatten a list using a listcomp with two 'for'</span>
<span class="gp">&gt;&gt;&gt; </span><span class="n">vec</span> <span class="o">=</span> <span class="p">[[</span><span class="mi">1</span><span class="p">,</span><span class="mi">2</span><span class="p">,</span><span class="mi">3</span><span class="p">],</span> <span class="p">[</span><span class="mi">4</span><span class="p">,</span><span class="mi">5</span><span class="p">,</span><span class="mi">6</span><span class="p">],</span> <span class="p">[</span><span class="mi">7</span><span class="p">,</span><span class="mi">8</span><span class="p">,</span><span class="mi">9</span><span class="p">]]</span>
<span class="gp">&gt;&gt;&gt; </span><span class="p">[</span><span class="n">num</span> <span class="k">for</span> <span class="n">elem</span> <span class="ow">in</span> <span class="n">vec</span> <span class="k">for</span> <span class="n">num</span> <span class="ow">in</span> <span class="n">elem</span><span class="p">]</span>
<span class="go">[1, 2, 3, 4, 5, 6, 7, 8, 9]</span>
</pre>


## Nested List comphensions

Consider the following example of a 3x4 matrix implemented as a list of 3 lists of length 4:

```python
matrix = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
]
```

The following list comprehension will transpose rows and columns:

```python
>>> [[row[i] for row in matrix] for i in range(4)]
[[1, 5, 9], [2, 6, 10], [3, 7, 11], [4, 8, 12]]
```

In the real world, you should prefer built-in functions to complex flow statements. The zip() function would do a great job for this use case:

```python
>>> list(zip(*matrix))
[(1, 5, 9), (2, 6, 10), (3, 7, 11), (4, 8, 12)]
```