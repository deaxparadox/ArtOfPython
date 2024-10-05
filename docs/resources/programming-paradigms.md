Python supports multiple programming paradigms, making it a flexible and versatile language. The key paradigms supported by Python include:

1. **Procedural Programming**:
   - **Definition**: A programming paradigm based on the concept of procedure calls, where the program is a sequence of instructions or statements.
   - **Example**: Writing functions to perform tasks and calling them in a sequence.

   ```python
   def add(a, b):
       return a + b

   def main():
       result = add(5, 3)
       print(result)

   if __name__ == "__main__":
       main()
   ```

2. **Object-Oriented Programming (OOP)**:
   - **Definition**: A paradigm based on the concept of "objects," which can contain data and code to manipulate the data. It emphasizes the principles of encapsulation, inheritance, and polymorphism.
   - **Example**: Defining classes and creating objects.

   ```python
   class Dog:
       def __init__(self, name, age):
           self.name = name
           self.age = age

       def bark(self):
           print(f"{self.name} says woof!")

   my_dog = Dog("Buddy", 5)
   my_dog.bark()
   ```

3. **Functional Programming**:
   - **Definition**: A paradigm where programs are constructed by applying and composing functions. It emphasizes the use of pure functions, immutability, and higher-order functions.
   - **Example**: Using functions as first-class citizens, avoiding side effects.

   ```python
   def add(a, b):
       return a + b

   def apply_function(func, a, b):
       return func(a, b)

   result = apply_function(add, 10, 20)
   print(result)
   ```

4. **Imperative Programming**:
   - **Definition**: A paradigm where the program describes a sequence of steps that change the state of the system. It focuses on how to achieve a certain task.
   - **Example**: Using loops and conditional statements to control the flow of the program.

   ```python
   total = 0
   for i in range(1, 6):
       total += i
   print(total)
   ```

5. **Aspect-Oriented Programming (AOP)**:
   - **Definition**: A paradigm that aims to increase modularity by allowing the separation of cross-cutting concerns. This is often implemented through decorators in Python.
   - **Example**: Using decorators to add functionality to existing code.

   ```python
   def logger(func):
       def wrapper(*args, **kwargs):
           print(f"Function {func.__name__} called with {args} {kwargs}")
           return func(*args, **kwargs)
       return wrapper

   @logger
   def greet(name):
       print(f"Hello, {name}!")

   greet("Alice")
   ```

6. **Metaprogramming**:
   - **Definition**: A programming technique where programs have the ability to treat other programs as their data. It allows the creation of code that manipulates code.
   - **Example**: Using metaclasses to dynamically modify classes.

   ```python
   class Meta(type):
       def __new__(cls, name, bases, dct):
           dct['greet'] = lambda self: f"Hello from {self.name}"
           return super().__new__(cls, name, bases, dct)

   class Person(metaclass=Meta):
       def __init__(self, name):
           self.name = name

   p = Person("Alice")
   print(p.greet())
   ```

Python's support for these diverse paradigms allows developers to choose the most appropriate style for their specific needs, leading to more efficient and maintainable code.