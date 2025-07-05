import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.geometry("600x500")


# Commands
def submit_filepath():
    print(filepath.get())
    f = open(filepath.get())

    lines = f.readlines()
    label = tk.Label(text=f"total{len(lines)}")


# Widgets
filepath = tk.StringVar()
column_name = ttk.Entry(root, textvariable=filepath)
submit_button = ttk.Button(root, command=submit_filepath, text="Submit")

# Layouts
column_name.pack()
submit_button.pack()

root.mainloop()
