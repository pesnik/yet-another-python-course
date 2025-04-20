# Sets in Python

## Introduction
Sets are unordered collections of unique items, ideal for tasks like removing duplicates. They’re useful for non-developers to manage distinct data.

## Key Concepts
- **Creating Sets**: Use curly braces or `set()`, e.g., `my_set = {1, 2, 3}`.
- **Set Operations**: Union (`|`), intersection (`&`), difference (`-`).
- **Adding/Removing Items**: Use `add()` and `remove()`.

## Examples
```python
# Creating a set
numbers = {1, 2, 2, 3}
print(numbers)  # Output: {1, 2, 3}

# Set operations
set1 = {1, 2, 3}
set2 = {2, 3, 4}
print(set1 & set2)  # Output: {2, 3}

# Adding an item
numbers.add(4)
print(numbers)  # Output: {1, 2, 3, 4}
```

## Resources
- [Python Official Documentation - Sets](https://docs.python.org/3/tutorial/datastructures.html#sets)
- [GeeksforGeeks - Python Sets](https://www.geeksforgeeks.org/python-sets/)

## Exercises
In `exercises.py`, try the following:
1. Create a set and add a new item.
2. Perform a union operation on two sets.
3. Remove an item from a set and handle the case where the item doesn’t exist.

## Project
In `project.py`, create a program that takes two lists of items, converts them to sets, and finds their common elements (intersection).

## Contact
For questions, open an issue in the repository or email [your email].
