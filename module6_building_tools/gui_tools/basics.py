import tkinter as tk
from tkinter import messagebox
from tkinter import filedialog

window = tk.Tk()

window.title('Transmission Team')
window.geometry('400x300')
window.configure(bg='lightblue')


# Widgets

# button = tkinter.Button(window, text='Submit')
# button.pack(side='left')

# button1 = tkinter.Button(window, text='Click')
# button1.place(x=100, y=100)

# button2 = tkinter.Button(window, text='1x1')
# button2.grid(row=1, column=1)

# button2 = tkinter.Button(window, text='1x2')
# button2.grid(row=1, column=2)

# button2 = tkinter.Button(window, text='2x1')
# button2.grid(row=2, column=1, columnspan=2)

# entry = tkinter.Entry(window)
# entry.pack()

# Geometry Manager (Layout Management)
## Pack
# label = tk.Label(window, text='Username')
# label.pack(pady=20, side='left', padx=10)

# button = tk.Button(window, text='Submit')
# button.pack(pady=10, side='right', padx=10)

## Grid
# label = tk.Label(window, text='Username')
# label.grid(pady=20, row=1, column=1, padx=10)

# button = tk.Button(window, text='Submit')
# button.grid(pady=10, row=2, column=2, padx=10)

# Event
# button = tk.Button(window, text='Submit', command=lambda: messagebox.showinfo(message='Form Submitted'))
# button.grid(pady=10, row=2, column=2, padx=10)
file_path = None

def process_form_input():
    global file_path
    if file_path == None:
        messagebox.showerror('File Selection', message='Please select a file first')
    else:
        import pandas as pd
        excelsheet1 = pd.read_csv(file_path, skiprows=11)
        print(excelsheet1.head())

def file_selector():
    global file_path
    file_path = filedialog.askopenfilename(
        initialdir="/",
        title="Select a File",
        filetypes=(("CSV files", "*.csv"),)
    )
    if file_path:
        print(f"Selected file: {file_path}")

button = tk.Button(window, text='Submit', command=process_form_input)
button.grid(pady=10, row=2, column=2, padx=10)

input_btn = tk.Button(window, text='Select a CSV File', command=file_selector)
input_btn.grid(row=1, column=2)



window.mainloop()