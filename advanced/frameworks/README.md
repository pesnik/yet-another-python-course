# Python Frameworks

## Introduction
Frameworks like Flask and Django simplify web development, enabling non-developers to create simple web applications or APIs for automation tasks.

## Key Concepts
- **Flask**: Lightweight framework for small web apps, easy to learn.
- **Django**: Robust framework with built-in features like authentication.
- **Basic Setup**: Create routes, handle requests, and render templates.
- **REST APIs**: Build APIs to serve data.

## Examples
```python
# Simple Flask app
from flask import Flask
app = Flask(__name__)

@app.route('/')
def home():
    return "Welcome to my app!"

if __name__ == '__main__':
    app.run(debug=True)
# Run: python app.py, visit http://localhost:5000
```

## Resources
- [Flask Official Documentation](https://flask.palletsprojects.com/)
- [Django Official Documentation](https://www.djangoproject.com/)

## Exercises
In `exercises.py`, try the following:
1. Create a Flask route that displays a greeting.
2. Write a Flask app with multiple routes.
3. Experiment with Django’s admin interface (requires setup).

## Project
In `project.py`, build a simple Flask web app that allows users to submit a form and displays the submitted data.

## Contact
For questions, open an issue in the repository or email [your email].
