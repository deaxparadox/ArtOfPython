# Magic (Dunder) methods

Python provides a lot of class internal attribute for modifying the flow of the program accoding to your requirement. Such as you created your custom iterator, context manager, perform high level mathematical operation on class (or instance) attributes.

Below is the list of magic methods, all the listed attributes are used for class manipulation, but the list is categired for understanding purpose of the what that attributes used for.

- Class operations
    - [`__init__`](https://): After an instance is created.
    - [`__name__`](__name__.md): The name of the class.
    - [`__qualname__`](https://): The qualified name of the class.
    - [`__class__`](https://): Class of an instance.
    - [`__doc__`](https://): Class documentation string.
    - [`__annotations__`](https://): Dictionary of type annotations for class variables.
    - [`__module__`](https://): The module in which the class is defined.
    - [`__dict__`](https://): A dictionary containing the class's namespace (attributes and methods).
    - [`__bases__`](https://): A tuple containing the base classes (superclasses).
    - [`__mro__`](https://): A method resolution order (tuple of base classes in the order they are searched for methods).
    - [`__subclasses__()`](https://): A method that returns a list of the all known subclasses.
    - [`__call__()__`](https://): Allow instances of `type` (i.e., classes) to be called like functions to create new instances.
    - [`__len__()`](magic-method/__len__.ipynb)    
    - [`__str__()`](magic-method/__str__.ipynb)
    - [`__class_getitem__()`](/docs/ArtOfPython/references/magic-method/__class_getitem__.md)
    - [`___init_subclass___`](): Called when subclass is created.
    - [`__weakref__`](https://): List of weak references to the object (if any).
    - [`__sizeof__`](https://): Returns the memory size of the object.
    - [`__hash__`](https://): Returns the hash value of an object (used in sets, dict keys).
    - [`__instancecheck__`](https://): Used by `isintance(obj, Class)`.
    - [`__subclasscheck__`](https://): Used by `issubclass(SubClass, Class)`.
    - [`__reversed__`](https://): Defines behavior for `reversed(obj)`.
    - [`__slots__`](https://): Defines a fixed set of attributes, reducing memory usage.
    - [`__prepare__`](https://): Used in metaclasses to create a custom `namespace` (dictionary) before the class it created.
    - [`__new__`](https://): Before an instance is created.

- Copy operations
    - [`__copy__`](https://): Defines behaviour for `copy.copy(obj)`.
    - [`__deepcopy__`](): Defines behaviour for `copy.deepcopy(obj)`.

- String repsentation
    - [`__repr__`](https://): Returns a string representation of an instance (for developers).
    - [`__str__`](https://): Returns a human-readable string representation of an instance.
    - [`__bytes__`](https://): Converts the object to a byte representation.

- Format
    - [`__format__`](https://): Defines the how the object should be formatted.

- Comparison operations
    - [`__lt__`](https://): Implement for `<`.
    - [`__gt__`](https://): Implement for `>`.
    - [`__le__`](https://): Implement for `<`.
    - [`__ge__`](https://): Implement for `>=`.
    - [`__eq__`](https://): Implement for `=`.
    - [`__ne__`](https://): Implement for `!=`.
    - [`__bool__`](https://): Defines the truth value of an object (`True` or `False`).

- Membership operation
    - [`__contains__`](https://): Implements `in` operator (`value in obj`).

- Attributes operations
    - [`__getattr__`](https://): Called when an attributes is accessed but not round in `__dict__`.
    - [`__setattr__`](https://): Controls how attributes are set.
    - [`__delattr__`](https://): Controls how attributes are deleted.
    - [`__dir__`](): Called by `dir(obj)`, returns a list of attribute names.
    - [`__getattribute__`](https://): Called for every attribute access, even if it exists.


- Indexing operation
    - [`__getitem__()`](magic-method/__getitem__.ipynb)
    - [`__setitem__()`](magic-method/__setitem__.ipynb)
    - [`__delitem__()`](magic-method/__delitem__.ipynb)

- Iterator type
    - [`__iter__() and __next__()`](magic-method/__iter__next__.ipynb)
    - [`__aiter__() and __anext__()`](magic-method/__aiter__anext.ipynb)

- [Context Managers](https://)
    - [`__enter__() and __exit__()`](magic-method/__iter__next__.ipynb)
    - [`__aenter__() and __aexit__()`](magic-method/__aiter__anext.ipynb)


- Numeric operation
    - [`__add__()`](magic-method/__add__.md)
    - [`__sub__()`](/docs/ArtOfPython/references/magic-method/__sub__.md)

- Descriptions
    - [`__get__`](https://): Fetch attribute using descriptors.
    - [`__set__`](https://): Set attribute using descriptors.
    - [`__del__`](https://): Delete attribute using descriptors.