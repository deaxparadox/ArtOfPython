# Python Scopes and Namespaces

A *namespace* is a mapping from names to objects.
- Most namespaces are currently implemented as Python dictionaries.
- Examples of namespaces are: the set of built-in names (containing function such as `abs()`, and built-in exception names); the global names in a modules; and the local names in a function invocation.
- The important thing to konwn about namespaces is that there is absolutely no relation between names in different namespaces; for instance, two different modules may both define a function `maximize` without confusion -- uses of the modules must perfix it with the module name.