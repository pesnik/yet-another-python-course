# Testing in Python

## Introduction
Testing ensures your code works as expected, crucial for non-developers building reliable automation scripts. This topic covers unit testing frameworks like pytest.

## Key Concepts
- **Unit Testing**: Test individual functions or components.
- **Frameworks**: `pytest`, `unittest`, `doctest`, `nose`.
- **Assertions**: Check expected vs. actual results with `assert`.
- **Test Discovery**: Automatically find and run tests with pytest.

## Examples
```python
# Example test file (test_math.py)
def add(a, b):
    return a + b

import pytest

def test_add():
    assert add(2, 3) == 5
    assert add(-1, 1) == 0

# Run: pytest test_math.py
```

## Resources
- [Pytest Official Documentation](https://docs.pytest.org/en/stable/)
- [Python Official Documentation - unittest](https://docs.python.org/3/library/unittest.html)

## Exercises
In `exercises.py`, try the following:
1. Write a test for a function that calculates the square of a number.
2. Create a test case with multiple assertions.
3. Use pytest to run tests and generate a report.

## Project
In `project.py`, create a simple function (e.g., a calculator) and write a test suite using pytest to verify its functionality.

## Contact
For questions, open an issue in the repository or email [your email].
