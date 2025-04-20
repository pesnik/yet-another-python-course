# Dictionaries in Python

## Introduction
Dictionaries store key-value pairs, making them perfect for organizing data like a phonebook. They’re intuitive for non-developers to manage structured data.

## Key Concepts
- **Creating Dictionaries**: Use curly braces, e.g., `my_dict = {"name": "Alice", "age": 30}`.
- **Accessing Values**: Use keys, e.g., `my_dict["name"]`.
- **Modifying Dictionaries**: Add or update key-value pairs with assignment.
- **Dictionary Methods**: `keys()`, `values()`, `items()`.

## Examples
```python
# Creating a dictionary
person = {"name": "Alice", "age": 30}
print(person["name"])  # Output: Alice

# Modifying a dictionary
person["city"] = "New York"
print(person)  # Output: {'name': 'Alice', 'age': 30, 'city': 'New York'}

# Dictionary methods
print(person.keys())  # Output: dict_keys(['name', 'age', 'city'])
```

## Resources
- [Python Official Documentation - Dictionaries](https://docs.python.org/3/tutorial/datastructures.html#dictionaries)
- [Real Python - Dictionaries](https://realpython.com/python-dicts/)

## Exercises
In `exercises.py`, try the following:
1. Create a dictionary with three key-value pairs and print one value.
2. Add a new key-value pair to a dictionary.
3. Use `items()` to loop through a dictionary and print each key-value pair.

## Project
In `project.py`, create a contact manager that stores names and phone numbers in a dictionary, allowing users to add and display contacts.

## Contact
For questions, open an issue in the repository or email [your email].
