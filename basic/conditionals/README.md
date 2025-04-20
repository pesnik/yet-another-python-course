# Conditionals in Python

## Introduction
Conditionals allow your program to make decisions based on conditions, using `if`, `elif`, and `else`. They’re useful for non-developers to add logic to programs.

## Key Concepts
- **If Statement**: Executes code if a condition is true.
- **Elif Statement**: Checks additional conditions if the previous ones are false.
- **Else Statement**: Executes code if no conditions are true.
- **Comparison Operators**: `==`, `!=`, `>`, `<\", `>=`, `<=`.

## Examples
```python
# Simple if statement
age = 20
if age >= 18:
    print("You are an adult")  # Output: You are an adult

# If-elif-else
score = 85
if score >= 90:
    print("Grade: A")
elif score >= 80:
    print("Grade: B")  # Output: Grade: B
else:
    print("Grade: C")
```

## Resources
- [Python Official Documentation - Control Flow](https://docs.python.org/3/tutorial/controlflow.html)
- [Real Python - Conditionals](https://realpython.com/python-conditional-statements/)

## Exercises
In `exercises.py`, try the following:
1. Write an if statement to check if a number is positive.
2. Use elif to categorize a number as positive, negative, or zero.
3. Create a conditional that checks if a string is empty.

## Project
In `project.py`, write a program that takes a user’s score (0-100) and prints their letter grade (A, B, C, D, F) based on standard grading scales.

## Contact
For questions, open an issue in the repository or email [your email].
