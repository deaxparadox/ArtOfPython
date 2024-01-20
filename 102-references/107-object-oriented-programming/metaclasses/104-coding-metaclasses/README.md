# Coding Metaclasses

Python routes class creation calls to a metaclass, if one is specified and provided. 

Metaclasses are coded with normal Python **class** statements and semantics. By definition, they are simply classes that inherit from **type**. Their only substantial distinctions are that Python calls them *automatically* at the end of the **class** statement, and that they must adhere to the *interface* expected by the **type** superclass.