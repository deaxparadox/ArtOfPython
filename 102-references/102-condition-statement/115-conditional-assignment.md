# Conditional assignment

We can use conditional variable assignment. If we are fetch data from some source in two variable or more, and suppose if we can get any of the variable which hold that data our program will word, in that case we can use condition assignment:

```py
>>> a = None
>>> 
>>> b = 'Important'
>>> 
>>> c = a or b           # if any of variable hold our data
>>> c
'Important'
>>> 
```