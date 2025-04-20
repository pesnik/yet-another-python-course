# Regular Expressions (RegEx) in Python

## Introduction
Regular expressions (RegEx) are patterns used to match and manipulate text. They’re useful for non-developers to validate or extract data, like emails or phone numbers.

## Key Concepts
- **Importing re**: Use `import re` to access RegEx functions.
- **Common Patterns**: `.` (any character), `\*` (zero or more), `+` (one or more).
- **Functions**: `re.match()`, `re.search()`, `re.findall()`.

## Examples
```python
import re

# Find an email
text = "Contact: alice@example.com"
email = re.search(r'\w+@\w+\.\w+', text)
print(email.group())  # Output: alice@example.com

# Validate a phone number
phone = "123-456-7890"
if re.match(r'\d{3}-\d{3}-\d{4}', phone):
    print("Valid phone number")  # Output: Valid phone number
```

## Resources
- [Python Official Documentation - re Module](https://docs.python.org/3/library/re.html)
- [Real Python - Regular Expressions](https://realpython.com/regex-python/)

## Exercises
In `exercises.py`, try the following:
1. Use `re.search()` to find a word in a string.
2. Write a RegEx to match a date format (e.g., MM/DD/YYYY).
3. Use `re.findall()` to extract all numbers from a string.

## Project
In `project.py`, create a program that extracts all email addresses from a given text and prints them.

## Contact
For questions, open an issue in the repository or email [your email].
