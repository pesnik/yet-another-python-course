# Asynchronous Programming in Python

## Introduction
Asynchronous programming allows tasks to run concurrently, useful for non-developers to handle I/O-bound tasks like API calls. This is an optional topic due to its complexity.

## Key Concepts
- **Async/Await**: Use `async def` for functions and `await` for pauses.
- **Libraries**: `asyncio` for basic async, `aiohttp` for async HTTP requests.
- **Event Loop**: Manages async tasks.

## Examples
```python
import asyncio

async def say_hello():
    print("Hello")
    await asyncio.sleep(1)
    print("World")

async def main():
    await asyncio.gather(say_hello(), say_hello())

asyncio.run(main())
# Output (with delay):
# Hello
# Hello
# World
# World
```

## Resources
- [Python Official Documentation - asyncio](https://docs.python.org/3/library/asyncio.html)
- [Real Python - Async IO](https://realpython.com/async-io-python/)

## Exercises
In `exercises.py`, try the following:
1. Write an async function that simulates a delay with `asyncio.sleep()`.
2. Use `asyncio.gather()` to run multiple async tasks.
3. Experiment with `aiohttp` to fetch data asynchronously (requires installation).

## Project
In `project.py`, create a program that uses `aiohttp` to fetch data from multiple APIs concurrently and prints the results.

## Contact
For questions, open an issue in the repository or email [your email].
