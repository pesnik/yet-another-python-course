# Generator Expressions in Python

## Introduction
Generator expressions create iterators in a memory-efficient way, ideal for non-developers handling large datasets in automation tasks.

## Key Concepts
- **Syntax**: Similar to list comprehensions but with parentheses, e.g., `(x**2 for x in range(5))`.
- **Memory Efficiency**: Generates values one at a time, unlike lists.
- **Use Cases**: Feed data to functions like `sum()` or loops.

## Examples
```python
# Generator expression
squares = (x**2 for x in range(5))
print(next(squares))  # Output: 0
print(next(squares))  # Output: 1

# Using with sum
total = sum(x**2 for x in range(5))
print(total)  # Output: 30
```

## Resources
- [Python Official Documentation - Generator Expressions](https://docs.python.org/3/tutorial/classes.html#generator-expressions)
- [Real Python - Generators](https://realpython.com/introduction-to-python-generators/)

## Exercises
In `exercises.py`, try the following:
1. Create a generator expression to yield even numbers.
2. Use a generator expression with `sum()` to calculate the sum of squares.
3. Compare memory usage of a list comprehension vs. a generator expression.

## Project
In `project.py`, create a program that uses a generator expression to process a large dataset (e.g., filter numbers from a file) without loading it all into memory.

## Contact
For questions, open an issue in the repository or email [your email].
