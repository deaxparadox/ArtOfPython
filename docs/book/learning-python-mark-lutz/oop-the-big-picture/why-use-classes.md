# Why use classes?

In simple terms, classes are just a way to define new sorts of stuff, reflecting real objects in a program's domain.

For instance, suppose we decide to implement hypothetical pizza-makking robot. Implement it using classes. Two aspects of OOP prove useful here:

- *Inheritence*: Pizza-making robots are kinds of robots, so they posses the usual robot-y properties. In OOP terms, we say they "inherit" properties from the general category of all robots. These common properties need to be implemented only once for the general case and can be reused in part or in full by all types of robots we may build in the future.
- *Composition*: Pizza-making robots are really collections of components that work together as a team. For instance, for our robot to be successful, it might need arms to rool dough, motors to maneuer to the even, and so on. In OOP parlance, our robot is an example of composition; it contains other objects that it activates to do its bidding. Each component might be codded as a class, which defines its own behavior and relationships.

Classes are Python program units, just like functions and modules; they are another compartment for packing logic and data. In fact, classes also define new namespaces, much like modules. But, compared to other program units, classes have three critical distinctions that make them more useful when it comes to building new objects:

- *Mulitple instances*: Classes are essentially factories for generating one or more objects. Every time we call a class, we generate a new object with a distinct namespace. Each object generated from a class has access to the class's attributes *and* gets a namespace of its own for data that varies per object.
- *Customization via inheritance*: Classes also support the OOP notion of inheritance; we can extend a class by redefining its attributes outside the class ifself in new software components coded as subclasses. More generally, classes can build up namespace hierarchies, which define names to be used by objects created from classes in the hierarchy. This supports multiple customizable behaviors more directly than other tools.
- *Operator overloading*: By providing special protocol methods, classes can define objects that respond to the sorts of operations we saw at work on built-in types. For instance, objects made with classes can be sliced, concatenated, indexed, and so on. Python provides hooks that classes can use to intercept and implement any built-in type operation.

### Attribute Inheritence Search

OOP story in Python boils down to this expression:

```
object.attribute
```

This expression is used to access module attributes, call methods of objects, and so on. When we say this to an object that is derived from a **class** statement, however, the expression kicks off a search in Python--it searches a tree of linked object,s looking for the first appearance of ***attribute*** that it can find.

The term *inheritance* is applied because objects lower in a tree inherit attached to objects higher in that tree. As the search proceeds from the bottom up, in  a sense, the objects linked into a tree are the union of all the attributes defined in all their tree parents, all the way up the tree.

In Python, this is all very literal: we really do build up trees of linked objects with code, and Python really does climb this tree at runtime searching for attributes every time we use the ***object.attribute*** expression.

----------

![Class](/assets/images/learning-python-1.png)

A class tree, with two instances at the bottom (I1 and I2), a class above them (C1), and two superclasses at the top (C2 and C3). All of these objects are namespaces (packages of variables), and the inheritance search is simply a search of the tree from bottom to top looking for the lowest occurence of an attribute name. Code implies the shape of such trees.