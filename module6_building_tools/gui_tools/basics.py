import tkinter as tk
from tkinter import messagebox, filedialog, ttk
import os
import pandas as pd

class CSVProcessorApp:
    def __init__(self, root):
        self.root = root
        self.file_path = None
        self.setup_window()
        self.create_widgets()
        
    def setup_window(self):
        self.root.title('CSV Data Processor - Transmission Team')
        self.root.geometry('600x450')
        self.root.configure(bg='#f0f0f0')
        self.root.resizable(True, True)
        
        # Configure grid weights for responsive design
        self.root.grid_rowconfigure(1, weight=1)
        self.root.grid_columnconfigure(0, weight=1)
        
    def create_widgets(self):
        # Header Frame
        header_frame = tk.Frame(self.root, bg='#2c3e50', height=60)
        header_frame.grid(row=0, column=0, sticky='ew', padx=0, pady=0)
        header_frame.grid_propagate(False)
        
        title_label = tk.Label(
            header_frame, 
            text='CSV Data Processor', 
            font=('Arial', 18, 'bold'),
            fg='white', 
            bg='#2c3e50'
        )
        title_label.pack(expand=True)
        
        # Main Content Frame
        main_frame = tk.Frame(self.root, bg='#f0f0f0', padx=30, pady=30)
        main_frame.grid(row=1, column=0, sticky='nsew')
        main_frame.grid_columnconfigure(0, weight=1)
        
        # File Selection Section
        file_section = tk.LabelFrame(
            main_frame, 
            text='File Selection', 
            font=('Arial', 12, 'bold'),
            bg='#f0f0f0',
            fg='#2c3e50',
            padx=20,
            pady=15
        )
        file_section.grid(row=0, column=0, sticky='ew', pady=(0, 20))
        file_section.grid_columnconfigure(0, weight=1)
        
        # File path display
        self.file_var = tk.StringVar(value="No file selected")
        self.file_label = tk.Label(
            file_section,
            textvariable=self.file_var,
            font=('Arial', 10),
            bg='white',
            fg='#7f8c8d',
            relief='sunken',
            anchor='w',
            padx=10,
            pady=8
        )
        self.file_label.grid(row=0, column=0, sticky='ew', pady=(0, 15))
        
        # Select file button
        self.select_btn = tk.Button(
            file_section,
            text='📁 Select CSV File',
            command=self.file_selector,
            font=('Arial', 11, 'bold'),
            bg='#3498db',
            fg='white',
            relief='flat',
            padx=20,
            pady=10,
            cursor='hand2'
        )
        self.select_btn.grid(row=1, column=0, pady=(0, 5))
        
        # Status indicator
        self.status_var = tk.StringVar(value="Ready to select file")
        self.status_label = tk.Label(
            file_section,
            textvariable=self.status_var,
            font=('Arial', 9),
            fg='#7f8c8d',
            bg='#f0f0f0'
        )
        self.status_label.grid(row=2, column=0, pady=(5, 0))
        
        # Processing Section
        process_section = tk.LabelFrame(
            main_frame,
            text='Data Processing',
            font=('Arial', 12, 'bold'),
            bg='#f0f0f0',
            fg='#2c3e50',
            padx=20,
            pady=15
        )
        process_section.grid(row=1, column=0, sticky='ew', pady=(0, 20))
        process_section.grid_columnconfigure(0, weight=1)
        
        # Skip rows option
        skip_frame = tk.Frame(process_section, bg='#f0f0f0')
        skip_frame.grid(row=0, column=0, sticky='ew', pady=(0, 15))
        
        tk.Label(
            skip_frame,
            text='Skip rows:',
            font=('Arial', 10),
            bg='#f0f0f0'
        ).pack(side='left')
        
        self.skip_var = tk.StringVar(value='11')
        self.skip_entry = tk.Entry(
            skip_frame,
            textvariable=self.skip_var,
            font=('Arial', 10),
            width=5,
            justify='center'
        )
        self.skip_entry.pack(side='left', padx=(10, 0))
        
        # Process button
        self.process_btn = tk.Button(
            process_section,
            text='🔄 Process Data',
            command=self.process_form_input,
            font=('Arial', 12, 'bold'),
            bg='#27ae60',
            fg='white',
            relief='flat',
            padx=30,
            pady=12,
            cursor='hand2',
            state='disabled'
        )
        self.process_btn.grid(row=1, column=0, pady=(0, 10))
        
        # Progress bar
        self.progress = ttk.Progressbar(
            process_section,
            mode='indeterminate',
            length=300
        )
        self.progress.grid(row=2, column=0, pady=(10, 0))
        
        # Results Section
        results_section = tk.LabelFrame(
            main_frame,
            text='Results',
            font=('Arial', 12, 'bold'),
            bg='#f0f0f0',
            fg='#2c3e50',
            padx=20,
            pady=15
        )
        results_section.grid(row=2, column=0, sticky='nsew', pady=(0, 0))
        results_section.grid_columnconfigure(0, weight=1)
        results_section.grid_rowconfigure(0, weight=1)
        main_frame.grid_rowconfigure(2, weight=1)
        
        # Results text area with scrollbar
        text_frame = tk.Frame(results_section, bg='#f0f0f0')
        text_frame.grid(row=0, column=0, sticky='nsew')
        text_frame.grid_columnconfigure(0, weight=1)
        text_frame.grid_rowconfigure(0, weight=1)
        
        self.results_text = tk.Text(
            text_frame,
            font=('Consolas', 9),
            bg='white',
            fg='#2c3e50',
            relief='sunken',
            padx=10,
            pady=10,
            wrap='none',
            state='disabled'
        )
        
        # Scrollbars
        v_scrollbar = tk.Scrollbar(text_frame, orient='vertical', command=self.results_text.yview)
        h_scrollbar = tk.Scrollbar(text_frame, orient='horizontal', command=self.results_text.xview)
        self.results_text.configure(yscrollcommand=v_scrollbar.set, xscrollcommand=h_scrollbar.set)
        
        self.results_text.grid(row=0, column=0, sticky='nsew')
        v_scrollbar.grid(row=0, column=1, sticky='ns')
        h_scrollbar.grid(row=1, column=0, sticky='ew')
        
        # Add hover effects
        self.add_button_hover_effects()
        
    def add_button_hover_effects(self):
        def on_enter(e, btn, color):
            btn.configure(bg=color)
            
        def on_leave(e, btn, color):
            btn.configure(bg=color)
        
        # Hover effects for buttons
        self.select_btn.bind("<Enter>", lambda e: on_enter(e, self.select_btn, '#2980b9'))
        self.select_btn.bind("<Leave>", lambda e: on_leave(e, self.select_btn, '#3498db'))
        
        self.process_btn.bind("<Enter>", lambda e: on_enter(e, self.process_btn, '#229954'))
        self.process_btn.bind("<Leave>", lambda e: on_leave(e, self.process_btn, '#27ae60'))
        
    def file_selector(self):
        file_path = filedialog.askopenfilename(
            title="Select a CSV File",
            filetypes=(
                ("CSV files", "*.csv"),
                ("All files", "*.*")
            ),
            initialdir=os.path.expanduser("~")
        )
        
        if file_path:
            self.file_path = file_path
            filename = os.path.basename(file_path)
            self.file_var.set(f"📄 {filename}")
            self.file_label.configure(fg='#2c3e50')
            self.status_var.set("✅ File selected successfully")
            self.process_btn.configure(state='normal')
            
            # Clear previous results
            self.update_results("File selected. Ready to process data.\n")
            
    def process_form_input(self):
        if not self.file_path:
            messagebox.showerror(
                'No File Selected', 
                'Please select a CSV file first before processing.'
            )
            return
            
        try:
            # Start progress bar
            self.progress.start(10)
            self.status_var.set("🔄 Processing data...")
            self.process_btn.configure(state='disabled', text='Processing...')
            self.root.update()
            
            # Get skip rows value
            try:
                skip_rows = int(self.skip_var.get()) if self.skip_var.get() else 0
            except ValueError:
                skip_rows = 0
                
            # Read CSV file
            df = pd.read_csv(self.file_path, skiprows=skip_rows)
            
            # Prepare results
            results = []
            results.append("=" * 50)
            results.append(f"FILE: {os.path.basename(self.file_path)}")
            results.append(f"ROWS SKIPPED: {skip_rows}")
            results.append(f"DATA SHAPE: {df.shape[0]} rows × {df.shape[1]} columns")
            results.append("=" * 50)
            results.append("\nFIRST 10 ROWS:")
            results.append("-" * 30)
            results.append(df.head(10).to_string())
            
            if df.shape[0] > 10:
                results.append(f"\n... and {df.shape[0] - 10} more rows")
                
            results.append(f"\nCOLUMNS:")
            results.append("-" * 30)
            for i, col in enumerate(df.columns, 1):
                results.append(f"{i:2d}. {col}")
                
            # Update results display
            self.update_results("\n".join(results))
            
            # Stop progress bar
            self.progress.stop()
            self.status_var.set("✅ Data processed successfully!")
            
            messagebox.showinfo(
                'Success', 
                f'Data processed successfully!\n\nFound {df.shape[0]} rows and {df.shape[1]} columns.'
            )
            
        except pd.errors.EmptyDataError:
            messagebox.showerror('Error', 'The selected file is empty or contains no valid data.')
            self.status_var.set("❌ Error: Empty file")
        except pd.errors.ParserError as e:
            messagebox.showerror('Error', f'Error parsing CSV file:\n{str(e)}')
            self.status_var.set("❌ Error: Parser error")
        except FileNotFoundError:
            messagebox.showerror('Error', 'The selected file was not found.')
            self.status_var.set("❌ Error: File not found")
        except Exception as e:
            messagebox.showerror('Error', f'An unexpected error occurred:\n{str(e)}')
            self.status_var.set("❌ Error occurred")
        finally:
            # Reset UI state
            self.progress.stop()
            self.process_btn.configure(state='normal', text='🔄 Process Data')
            
    def update_results(self, text):
        self.results_text.configure(state='normal')
        self.results_text.delete(1.0, tk.END)
        self.results_text.insert(1.0, text)
        self.results_text.configure(state='disabled')

# Create and run the application
if __name__ == "__main__":
    root = tk.Tk()
    app = CSVProcessorApp(root)
    root.mainloop()