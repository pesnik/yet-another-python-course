# Iterators in Python

## Introduction
Iterators allow you to traverse through data structures like lists or custom objects. They’re useful for non-developers to process data efficiently.

## Key Concepts
- **Iterator Protocol**: Objects with `__iter__()` and `__next__()` methods.
- **For Loops**: Automatically use iterators to traverse iterables.
- **Creating Iterators**: Define custom iterators using classes.

## Examples
```python
# Using a for loop with an iterator
numbers = [1, 2, 3]
iterator = iter(numbers)
print(next(iterator))  # Output: 1
print(next(iterator))  # Output: 2

# Custom iterator
class Counter:
    def __init__(self, max):
        self.max = max
        self.current = 0
    def __iter__(self):
        return self
    def __next__(self):
        if self.current < self.max:
            self.current += 1
            return self.current
        raise StopIteration

counter = Counter(3)
for num in counter:
    print(num)  # Output: 1, 2, 3
```

## Resources
- [Python Official Documentation - Iterators](https://docs.python.org/3/tutorial/classes.html#iterators)
- [Real Python - Iterators](https://realpython.com/python-iterators/)

## Exercises
In `exercises.py`, try the following:
1. Create an iterator for a list and use `next()` to print items.
2. Write a custom iterator that yields even numbers up to a limit.
3. Use a for loop to iterate over a custom iterator.

## Project
In `project.py`, create a custom iterator that generates Fibonacci numbers up to a user-specified limit.

## Contact
For questions, open an issue in the repository or email [your email].
