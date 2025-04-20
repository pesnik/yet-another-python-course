# Lists in Python

## Introduction
Lists are versatile data structures in Python that store ordered collections of items. They’re great for non-developers to manage multiple pieces of data.

## Key Concepts
- **Creating Lists**: Use square brackets, e.g., `my_list = [1, 2, 3]`.
- **Accessing Items**: Use indices, starting at 0, e.g., `my_list[0]`.
- **Modifying Lists**: Add items with `append()`, remove with `remove()`.
- **List Operations**: Slicing, concatenation, and length with `len()`.

## Examples
```python
# Creating a list
fruits = ["apple", "banana", "orange"]
print(fruits[1])  # Output: banana

# Modifying a list
fruits.append("grape")
print(fruits)  # Output: ['apple', 'banana', 'orange', 'grape']

# Slicing
print(fruits[1:3])  # Output: ['banana', 'orange']
```

## Resources
- [Python Official Documentation - Lists](https://docs.python.org/3/tutorial/introduction.html#lists)
- [GeeksforGeeks - Python Lists](https://www.geeksforgeeks.org/python-list/)

## Exercises
In `exercises.py`, try the following:
1. Create a list of numbers and print the first and last items.
2. Add an item to a list and remove another.
3. Slice a list to get a subset of items.

## Project
In `project.py`, create a to-do list program that allows users to add tasks, remove tasks, and display the current list.

## Contact
For questions, open an issue in the repository or email [your email].
