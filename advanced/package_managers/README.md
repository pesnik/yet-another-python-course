# Package Managers in Python

## Introduction
Package managers like pip and conda install and manage Python libraries, enabling non-developers to use powerful tools for automation or data analysis.

## Key Concepts
- **pip**: Installs packages from PyPI, e.g., `pip install requests`.
- **conda**: Manages packages and environments, e.g., `conda install numpy`.
- **Virtual Environments**: Isolate project dependencies using `venv` or `conda`.
- **Requirements File**: List dependencies in a `requirements.txt` for easy installation.

## Examples
```python
# Using pip in a terminal
# pip install requests

# Using a virtual environment
import os
os.system("python -m venv myenv")
# Activate: source myenv/bin/activate (Linux/Mac) or myenv\Scripts\activate (Windows)

# Installing from requirements.txt
# pip install -r requirements.txt
```

## Resources
- [Python Official Documentation - pip](https://pip.pypa.io/en/stable/)
- [Conda Documentation](https://docs.conda.io/en/latest/)

## Exercises
In `exercises.py`, try the following:
1. Create a virtual environment and install a package like `requests`.
2. Write a script that uses an installed package (e.g., fetch data with `requests`). 
3. Generate a `requirements.txt` file for your project.

## Project
In `project.py`, create a program that uses the `requests` library to fetch and display data from a public API, managing dependencies in a virtual environment.

## Contact
For questions, open an issue in the repository or email [your email].
