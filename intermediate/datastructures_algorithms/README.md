# Data Structures and Algorithms in Python

## Introduction
Data structures organize data, and algorithms solve problems efficiently. For non-developers, understanding basic structures like stacks and queues can enhance automation tasks.

## Key Concepts
- **Data Structures**: Stacks (LIFO), Queues (FIFO), Linked Lists.
- **Algorithms**: Searching (linear, binary), Basic sorting (bubble sort).
- **Python Implementation**: Use lists for stacks/queues, custom classes for linked lists.

## Examples
```python
# Stack using a list
stack = []
stack.append(1)  # Push
stack.append(2)
print(stack.pop())  # Pop: 2

# Linear search
def linear_search(arr, target):
    for i, item in enumerate(arr):
        if item == target:
            return i
    return -1

print(linear_search([1, 3, 5], 3))  # Output: 1
```

## Resources
- [Python Official Documentation - Data Structures](https://docs.python.org/3/tutorial/datastructures.html)
- [GeeksforGeeks - DSA](https://www.geeksforgeeks.org/data-structures/)

## Exercises
In `exercises.py`, try the following:
1. Implement a stack using a list with push and pop operations.
2. Write a linear search function to find an item in a list.
3. Create a queue using a list with enqueue and dequeue operations.

## Project
In `project.py`, implement a simple task scheduler using a queue to manage tasks in order of submission.

## Contact
For questions, open an issue in the repository or email [your email].
