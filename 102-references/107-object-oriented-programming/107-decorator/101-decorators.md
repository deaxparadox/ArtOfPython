# What's a Decorator?


Decoration is a way to specify management or augmentation code for functions and classes. Decorators themselves take the form of callable objects (e.g. functions) that process other  callable objects.

Python decorators come in two related flavours:

1. *Function decorators*
2. *Class decorators*

In short, decorators provide a way to insert *automatically run code* at the end of function and class definition statements--at the end of a **def** for function decorators, and at the end of a **class** for class decorators.

## Managing Calls and Instances

This automatically run code may be used to augment calls to functions and classes. It arranges this by installing *wrapper (a.k.a proxy)* objects to be invoked later:

- *Call proxies*: Function decorators install wrapper objects to intercept later *function calls* and process them as needed, usually passing the call on to the original function to run the managed action.
- *Interface proxies*: Class decorators install wrapper objects to intercept later *instance creation calls* and process them as required, usually passing the call on to the original class to create a managed instance.

Decorators achieve these effects by automatically rebinding function and class names to other callables, at the **def** and **class** statements. When later invoked, these callable can perform tack such as trancing and timing function calls, managing access to class instance attributes, and so on.


## Managing Functions and Classes

- *Function managers*: Function decorators can also be used to managed *function objects", instead of or in addition to later calls to them--to register a function to an API, for instance. Our primary focus here, though, will be on their more commonly used call wrapper application.
- *Class managers*: Class decorators can also be used to managed *class objects* directly, instead of or in addition to instance creation calls--to argument a class with new methods, for exmaple.


----------

Function decorators can be used to manage both function calls and function objects, and class decorators can be used to manage both class instances and classes themselves. By returning the decorated object itself instead of a wrapper, decorators become a simple post-creation step for functions and classes.


## Using and Defining Decorators

Functions decorators may be used to augment functions with code that adds call tracing or logging, performs argument validity testing during debugging, automatically acquires and releases thread locks, times calls made to functions for optimization, and so on.

Function decorators are designed to augment only a specific function or method call, not an entire *object interface*. 

Class decorators fill the latter role better because they can intercept instance creation calls, they can be used to implement arbitrary object interface augmentation or management tasks.
