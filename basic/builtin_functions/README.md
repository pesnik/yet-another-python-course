# Built-in Functions in Python

## Introduction
Python provides built-in functions that perform common tasks, such as manipulating data or getting input. These are perfect for non-developers to quickly add functionality.

## Key Concepts
- **Common Built-in Functions**:
  - `len()`: Returns the length of an object.
  - `input()`: Gets user input as a string.
  - `type()`: Returns the type of an object.
  - `str()`, `int()`, `float()`: Convert data types.

## Examples
```python
# Length of a string
text = "Hello"
print(len(text))  # Output: 5

# User input
name = input("Enter your name: ")
print(f"Hi, {name}!")

# Type conversion
num = "123"
num_int = int(num)
print(num_int + 1)  # Output: 124
```

## Resources
- [Python Official Documentation - Built-in Functions](https://docs.python.org/3/library/functions.html)
- [W3Schools - Built-in Functions](https://www.w3schools.com/python/python_ref_functions.asp)

## Exercises
In `exercises.py`, try the following:
1. Use `len()` to find the length of a string.
2. Use `input()` to get a number and convert it to an integer.
3. Use `type()` to check the type of a variable after conversion.

## Project
In `project.py`, create a program that asks for a user’s name and a number, then prints the name repeated that number of times using `input()` and `str()`.

## Contact
For questions, open an issue in the repository or email [your email].
