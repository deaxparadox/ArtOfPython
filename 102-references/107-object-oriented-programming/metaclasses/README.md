# Metaclasses

In a sense, metaclasses simply extend the code-insertion model of decorators. Function and class decorators allow us to intercept and augment function calls and class creation calls. 

Similarly, metaclasses allow us to intercept and augment *class creation*--they provide an API for inserting extra logic to be run at the conclusion of the **class** statement. Metaclasses allow us to gain a high level of control over how a set of classes works.

- *class decorators* are often used to manage instances, they can also be used to manage classes instead, much like metaclasses.
- while *metaclasses* are designed to augment class construction, they can also insert proxies to manage instances instead, much like class decorators.

----------

The *class decorators* run after the decorated class has already been created. Thus, they are often used to add logic to be run at *instance* creation time.

The metaclasses, run *during* class creation to make and return the new client class. Therefore, they are often used for managing or augmenting *classes* themselves, and can even provide methods to process the classes that are created from them, via a direct instance relationship.

----------


To be able to insert some code to run automatically at the end of a class statement to augment the class, is exactly what *metaclasses* do, by declaring a metaclass, we tell Python to route the creation of the class object to another class we provide:


```py
def extra(self, arg):
    ...

class Extras(type):
    def __init__(Class, classname, superclasses, attributedict):
        if required():
            Class.extra = extra 

class Client1(metaclass=Extras): ...
class Client2(metaclass=Extras): ...
class Client2(metaclass=Extras): ...

X = Client1()
X.extra()
```

Because Python invokes the metaclass automatically at the end of the class statement when the new class is created, it can augment, register, or otherwise manage the class as needed. Moreover, the only requirement for the client class is that they declare the metaclass; every class that does so will automatically acquire whatever augmentation the metaclass provides.