# Sorting Algorithms in Python

## Introduction
Sorting algorithms arrange data in a specific order, like ascending or descending. For non-developers, understanding basic algorithms like bubble sort can improve data handling.

## Key Concepts
- **Bubble Sort**: Repeatedly swaps adjacent elements if they’re in the wrong order.
- **Selection Sort**: Selects the smallest element and places it in the correct position.
- **Python’s Built-in Sort**: Use `list.sort()` or `sorted()` for efficiency.

## Examples
```python
# Bubble sort
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

numbers = [64, 34, 25, 12]
print(bubble_sort(numbers))  # Output: [12, 25, 34, 64]

# Built-in sort
numbers = [64, 34, 25, 12]
print(sorted(numbers))  # Output: [12, 25, 34, 64]
```

## Resources
- [GeeksforGeeks - Sorting Algorithms](https://www.geeksforgeeks.org/sorting-algorithms/)
- [Real Python - Sorting](https://realpython.com/sorting-algorithms-python/)

## Exercises
In `exercises.py`, try the following:
1. Implement bubble sort for a list of numbers.
2. Use selection sort to sort a list.
3. Compare the results of `sorted()` with a custom sorting function.

## Project
In `project.py`, create a program that sorts a list of user-entered names alphabetically using a sorting algorithm.

## Contact
For questions, open an issue in the repository or email [your email].
