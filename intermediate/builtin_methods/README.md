# Built-in Methods in Python

## Introduction
Built-in methods are functions provided by Python’s data types, such as lists or strings. They’re useful for non-developers to manipulate data efficiently.

## Key Concepts
- **String Methods**: `upper()`, `lower()`, `strip()`, `split()`.
- **List Methods**: `append()`, `pop()`, `sort()`, `reverse()`.
- **Dictionary Methods**: `get()`, `update()`, `pop()`.
- **Set Methods**: `add()`, `union()`, `intersection()`.

## Examples
```python
# String methods
text = "  Hello World  "
print(text.strip())  # Output: Hello World
print(text.upper())  # Output:   HELLO WORLD  

# List methods
numbers = [3, 1, 2]
numbers.sort()
print(numbers)  # Output: [1, 2, 3]
```

## Resources
- [Python Official Documentation - Built-in Types](https://docs.python.org/3/library/stdtypes.html)
- [W3 Schools - Python Methods](https://www.w3schools.com/python/python_ref_list.asp)

## Exercises
In `exercises.py`, try the following:
1. Use a string method to convert text to lowercase.
2. Sort a list of numbers in descending order.
3. Use a dictionary method to retrieve a value safely with `get()`.

## Project
In `project.py`, create a program that processes a list of user inputs, using string methods to clean the input and list methods to organize it.

## Contact
For questions, open an issue in the repository or email [your email].
