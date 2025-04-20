# Tuples in Python

## Introduction
Tuples are immutable, ordered collections of items, useful for storing fixed data. They’re helpful for non-developers to understand data that shouldn’t change.

## Key Concepts
- **Creating Tuples**: Use parentheses, e.g., `my_tuple = (1, 2, 3)`.
- **Accessing Items**: Use indices, e.g., `my_tuple[0]`.
- **Immutability**: Tuples cannot be modified after creation.
- **Tuple Operations**: Slicing and concatenation.

## Examples
```python
# Creating a tuple
coords = (10, 20)
print(coords[0])  # Output: 10

# Slicing
print(coords[0:2])  # Output: (10, 20)

# Concatenation
new_coords = coords + (30,)
print(new_coords)  # Output: (10, 20, 30)
```

## Resources
- [Python Official Documentation - Tuples](https://docs.python.org/3/tutorial/datastructures.html#tuples-and-sequences)
- [Real Python - Tuples](https://realpython.com/python-lists-tuples/)

## Exercises
In `exercises.py`, try the following:
1. Create a tuple with three items and print the second item.
2. Concatenate two tuples and print the result.
3. Try to modify a tuple (it will raise an error) and observe the result.

## Project
In `project.py`, create a program that stores coordinates (x, y) in a tuple and calculates the distance from (0, 0) using the Pythagorean theorem.

## Contact
For questions, open an issue in the repository or email [your email].
