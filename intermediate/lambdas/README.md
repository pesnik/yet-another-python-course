# Lambda Functions in Python

## Introduction
Lambda functions are small, anonymous functions defined with the `lambda` keyword. They’re handy for non-developers to write concise code for simple tasks.

## Key Concepts
- **Syntax**: `lambda arguments: expression`
- **Use Cases**: Often used with `map()`, `filter()`, or sorting.
- **Limitations**: Single expression, no statements.

## Examples
```python
# Lambda function
square = lambda x: x * x
print(square(5))  # Output: 25

# Using with map
numbers = [1, 2, 3]
squares = list(map(lambda x: x * x, numbers))
print(squares)  # Output: [1, 4, 9]
```

## Resources
- [Python Official Documentation - Lambda](https://docs.python.org/3/tutorial/controlflow.html#lambda-expressions)
- [GeeksforGeeks - Lambda](https://www.geeksforgeeks.org/python-lambda/)

## Exercises
In `exercises.py`, try the following:
1. Write a lambda function to double a number.
2. Use `map()` with a lambda to cube a list of numbers.
3. Use `filter()` with a lambda to get even numbers from a list.

## Project
In `project.py`, create a program that uses lambda functions to process a list of user inputs (e.g., convert strings to uppercase).

## Contact
For questions, open an issue in the repository or email [your email].
