# Functions in Python

## Introduction
Functions are reusable blocks of code that perform specific tasks, making your programs more organized and efficient. They’re great for non-developers to simplify repetitive tasks.

## Key Concepts
- **Defining Functions**: Use `def function_name(parameters):` to create a function.
- **Parameters**: Inputs to the function, optional or required.
- **Return Statement**: Outputs a value using `return`.
- **Calling Functions**: Execute the function with `function_name(arguments)`.

## Examples
```python
# Define a function
def greet(name):
    return f"Hello, {name}!"

# Call the function
print(greet("Alice"))  # Output: Hello, Alice!

# Function with multiple parameters
def add(a, b):
    return a + b

print(add(5, 3))  # Output: 8
```

## Resources
- [Python Official Documentation - Functions](https://docs.python.org/3/tutorial/controlflow.html#defining-functions)
- [GeeksforGeeks - Functions](https://www.geeksforgeeks.org/python-functions/)

## Exercises
In `exercises.py`, try the following:
1. Write a function that calculates the square of a number.
2. Create a function that checks if a number is positive.
3. Define a function that concatenates two strings.

## Project
In `project.py`, build a calculator function that takes two numbers and an operation (add, subtract, multiply, divide) and returns the result.

## Contact
For questions, open an issue in the repository or email [your email].
