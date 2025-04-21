# Object-Oriented Programming (OOP) in Python

## Introduction
Object-Oriented Programming (OOP) organizes code using classes and objects, making it easier to model real-world entities. For non-developers, OOP is useful for structuring automation scripts or managing complex data.

## Key Concepts
- **Classes and Objects**: A class is a blueprint, and an object is an instance of a class.
- **Attributes**: Variables that belong to a class or object.
- **Methods**: Functions defined within a class.
- **Inheritance**: A class can inherit attributes and methods from another class.
- **Encapsulation**: Restricting access to certain attributes using private variables (e.g., `_variable`).

## Examples
```python
# Defining a class
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def introduce(self):
        return f"Hi, I'm {self.name} and I'm {self.age} years old."

# Creating an object
alice = Person("Alice", 30)
print(alice.introduce())  # Output: Hi, I'm Alice and I'm 30 years old.

# Inheritance
class Student(Person):
    def __init__(self, name, age, student_id):
        super().__init__(name, age)
        self.student_id = student_id

bob = Student("Bob", 20, "S123")
print(bob.introduce())  # Output: Hi, I'm Bob and I'm 20 years old.
```

## Resources
- [Python Official Documentation - Classes](https://docs.python.org/3/tutorial/classes.html)
- [Real Python - OOP](https://realpython.com/python3-object-oriented-programming/)

## Exercises
In `exercises.py`, try the following:
1. Create a class with two attributes and a method to display them.
2. Implement inheritance by creating a subclass that extends a base class.
3. Use encapsulation to restrict access to an attribute.

## Project
In `project.py`, create a program that models a simple library system with classes for books and users, allowing users to borrow and return books.

## Contact
For questions, open an issue in the repository or email [your email].
