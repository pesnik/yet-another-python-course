# Variables and Data Types in Python

## Introduction
Variables store data in Python, and data types define the kind of data they hold. This topic is essential for non-developers to understand how to manage information in programs.

## Key Concepts
- **Variables**: Assigned using `=`, e.g., `x = 5`. No need to declare types.
- **Data Types**:
  - **Integers**: Whole numbers (e.g., `5`, `-3`)
  - **Floats**: Decimal numbers (e.g., `3.14`, `-0.08`)
  - **Strings**: Text (e.g., `"Hello"`, `'World'`)
  - **Booleans**: `True` or `False`
  - **None**: Represents no value

## Examples
```python
# Variables and data types
x = 5  # Integer
y = 3.14  # Float
name = "Alice"  # String
is_student = True  # Boolean
z = None  # NoneType

print(type(x))  # Output: <class 'int'>
print(type(name))  # Output: <class 'str'>
```

## Resources
- [Python Official Documentation - Built-in Types](https://docs.python.org/3/library/stdtypes.html)
- [Real Python - Data Types](https://realpython.com/python-data-types/)

## Exercises
In `exercises.py`, try the following:
1. Create variables for different data types and print their types.
2. Convert a string to an integer using `int()` and print the result.
3. Use `isinstance()` to check if a variable is a string.

## Project
In `project.py`, write a program that takes user input for name (string), age (integer), and height (float), then prints a summary, e.g., "Name: Alice, Age: 30, Height: 1.75m".

## Contact
For questions, open an issue in the repository or email [your email].
