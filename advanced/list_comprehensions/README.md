# List Comprehensions in Python

## Introduction
List comprehensions provide a concise way to create lists, useful for non-developers to process data efficiently in automation scripts.

## Key Concepts
- **Syntax**: `[expression for item in iterable if condition]`
- **Use Cases**: Transform or filter data in a single line.
- **Nested Comprehensions**: Create complex lists, like matrices.

## Examples
```python
# Basic list comprehension
squares = [x**2 for x in range(5)]
print(squares)  # Output: [0, 1, 4, 9, 16]

# With condition
evens = [x for x in range(10) if x % 2 == 0]
print(evens)  # Output: [0, 2, 4, 6, 8]
```

## Resources
- [Python Official Documentation - List Comprehensions](https://docs.python.org/3/tutorial/datastructures.html#list-comprehensions)
- [Real Python - List Comprehensions](https://realpython.com/list-comprehension-python/)

## Exercises
In `exercises.py`, try the following:
1. Create a list comprehension to generate cubes of numbers.
2. Use a condition to filter out odd numbers from a list.
3. Write a nested list comprehension to create a 3x3 matrix.

## Project
In `project.py`, create a program that uses list comprehensions to process a list of user inputs and filter specific values (e.g., words longer than 5 characters).

## Contact
For questions, open an issue in the repository or email [your email].
