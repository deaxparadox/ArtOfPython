# Metaclass Versus Superclass

In event simpler terms, watch what happends in the following: as an *instance* of the **A** metaclass type, class **B** acquires **A**'s attribute, but this attribute is not made available for inheritance by **B**'s own instances--the acquisition of namess by metaclass instances is *distinct* from the normal inheritance used for class instances:

```py
In [40]: class A(type): attr = 1

In [41]: class B(metaclass=A):
    ...:     pass
    ...: 

In [42]: B.attr
Out[42]: 1

In [44]: I = B()

In [45]: I.attr
---------------------------------------------------------------------------
AttributeError                            Traceback (most recent call last)
Cell In[45], line 1
----> 1 I.attr

AttributeError: 'B' object has no attribute 'attr'

In [46]: 'attr' in B.__dict__, 'attr' in A.__dict__
Out[46]: (False, True)

In [47]: 
```