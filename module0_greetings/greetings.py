#!/usr/bin/env python3
import random

# Welcome message
print("Welcome to Yet Another Python Course!")
print("Let's get to know you a bit. Please answer the following questions.")

name = input("Enter your name: ").strip()
if not name:
    name = "Anonymous"

job_title = input("Enter your job title: ").strip()
if not job_title:
    job_title = "Professional"

fun_fact = input("Enter a fun fact about yourself: ").strip()
if not fun_fact:
    fun_fact = "being awesome"

templates = [
    "Meet {name}, the {job_title} who {fun_fact}. Clearly, they're here to conquer the world of Python!",
    "{name}, a {job_title} by day, and someone who {fun_fact} by night. Watch out, Python world!",
    "Introducing {name}, the {job_title} known for {fun_fact}. Python better watch its back!"
]

selected_template = random.choice(templates)

message = selected_template.format(name=name, job_title=job_title, fun_fact=fun_fact)

print(message)

print("Thanks for sharing! Get ready to dive into the world of Python.")
