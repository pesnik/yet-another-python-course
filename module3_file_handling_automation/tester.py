import tkinter as tk

# Create the main window
root = tk.Tk()
root.title("Simple Tkinter Window")

# Create a label widget
label = tk.Label(root, text="Hello, Tkinter!")
label.pack()

# Create a button widget
button = tk.Button(root, text="Click Me!")
button.pack()

# Run the main loop
root.mainloop()
