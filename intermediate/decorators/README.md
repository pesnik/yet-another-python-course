# Decorators in Python

## Introduction
Decorators modify the behavior of functions or methods, adding functionality like logging or timing. They’re useful for non-developers to enhance automation scripts.

## Key Concepts
- **Function Decorators**: Functions that wrap other functions.
- **Syntax**: Use `@decorator_name` above a function definition.
- **Creating Decorators**: Define a wrapper function inside a decorator.

## Examples
```python
# Simple decorator
def my_decorator(func):
    def wrapper():
        print("Something before")
        func()
        print("Something after")
    return wrapper

@my_decorator
def say_hello():
    print("Hello!")

say_hello()
# Output:
# Something before
# Hello!
# Something after
```

## Resources
- [Python Official Documentation - Decorators](https://docs.python.org/3/glossary.html#term-decorator)
- [Real Python - Decorators](https://realpython.com/primer-on-python-decorators/)

## Exercises
In `exercises.py`, try the following:
1. Create a decorator that prints the execution time of a function.
2. Write a decorator that logs function calls to a file.
3. Apply a decorator to a function that calculates a square.

## Project
In `project.py`, create a decorator that logs the input and output of a function, and apply it to a program that processes user input.

## Contact
For questions, open an issue in the repository or email [your email].
