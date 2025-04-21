# Modules in Python

## Introduction
Modules are Python files containing reusable code, such as functions or classes. They help non-developers organize and share code for automation tasks.

## Key Concepts
- **Importing Modules**: Use `import module_name` to access module content.
- **Standard Library**: Python’s built-in modules like `math`, `os`, `datetime`.
- **Creating Modules**: Save a .py file and import it.
- **Packages**: Folders containing modules with an `__init__.py` file.

## Examples
```python
# Importing a standard module
import math
print(math.sqrt(16))  # Output: 4.0

# Creating and importing a custom module
# Assume my_module.py contains:
# def say_hello():
#     return "Hello from module!"
import my_module
print(my_module.say_hello())  # Output: Hello from module!
```

## Resources
- [Python Official Documentation - Modules](https://docs.python.org/3/tutorial/modules.html)
- [GeeksforGeeks - Modules](https://www.geeksforgeeks.org/python-modules/)

## Exercises
In `exercises.py`, try the following:
1. Import the `math` module and use a function like `sin()`.
2. Create a custom module with a function and import it.
3. Use the `datetime` module to print the current date.

## Project
In `project.py`, create a program that uses a custom module to handle file operations (e.g., reading a file) and calls its functions.

## Contact
For questions, open an issue in the repository or email [your email].
