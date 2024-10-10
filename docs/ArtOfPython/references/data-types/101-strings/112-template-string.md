# Template Strings

Template strings provide simpler string substitutions.

Template strings support `$`-based substitutions, using the following rules:

- `$$` is an escape; it is replaced with a single `$`.
- `$identifier` names a substitution placeholder matching a mapping key of `"identifier"`
- `${identifier}` is equivalent to `$identifier`. It is required when valid identifier characters follow the placeholder but are not part of the placeholder, such as `"${noun}ification"`.


```py
>>> 
>>> from string import Template
>>> 
>>> s.substitute(who="tim", what="kung pao")
'tim likes kung pao'
>>> 
```

To substibute a dictionary object we have to use `.safe_substitue(d)` method:

```py
>>> Template('$who likes $what').safe_substitute(d)
'tim likes $what'
```