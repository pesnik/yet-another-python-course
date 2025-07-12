import tkinter as tk
from tkinter import filedialog, messagebox, scrolledtext
import pandas as pd
import os

class CSVLoader:
    def __init__(self, root):
        self.root = root
        self.root.title("CSV File Loader")
        self.root.geometry("800x600")
        
        # Variables
        self.df = None
        self.file_path = None
        
        # Create GUI elements
        self.create_widgets()
        
    def create_widgets(self):
        # Main frame
        main_frame = tk.Frame(self.root, padx=20, pady=20)
        main_frame.pack(fill=tk.BOTH, expand=True)
        
        # File selection frame
        file_frame = tk.Frame(main_frame)
        file_frame.pack(fill=tk.X, pady=(0, 20))
        
        # File selection button
        select_btn = tk.Button(file_frame, text="Select CSV File", 
                              command=self.select_file, bg="#4CAF50", 
                              fg="white", font=("Arial", 10, "bold"))
        select_btn.pack(side=tk.LEFT, padx=(0, 10))
        
        # Selected file label
        self.file_label = tk.Label(file_frame, text="No file selected", 
                                  fg="gray", font=("Arial", 9))
        self.file_label.pack(side=tk.LEFT)
        
        # Load button
        self.load_btn = tk.Button(file_frame, text="Load & Show Head", 
                                 command=self.load_and_show_head, 
                                 bg="#2196F3", fg="white", 
                                 font=("Arial", 10, "bold"), state=tk.DISABLED)
        self.load_btn.pack(side=tk.RIGHT)
        
        # Info frame
        info_frame = tk.Frame(main_frame)
        info_frame.pack(fill=tk.X, pady=(0, 10))
        
        self.info_label = tk.Label(info_frame, text="", 
                                  font=("Arial", 9), fg="blue")
        self.info_label.pack(side=tk.LEFT)
        
        # Text area for displaying data
        self.text_area = scrolledtext.ScrolledText(main_frame, 
                                                  wrap=tk.NONE, 
                                                  font=("Consolas", 9))
        self.text_area.pack(fill=tk.BOTH, expand=True)
        
        # Status bar
        self.status_bar = tk.Label(self.root, text="Ready", 
                                  relief=tk.SUNKEN, anchor=tk.W)
        self.status_bar.pack(side=tk.BOTTOM, fill=tk.X)
        
    def select_file(self):
        """Open file dialog to select CSV file"""
        file_path = filedialog.askopenfilename(
            title="Select CSV File",
            filetypes=[("CSV files", "*.csv"), ("All files", "*.*")]
        )
        
        if file_path:
            self.file_path = file_path
            filename = os.path.basename(file_path)
            self.file_label.config(text=f"Selected: {filename}", fg="black")
            self.load_btn.config(state=tk.NORMAL)
            self.status_bar.config(text=f"File selected: {filename}")
            
    def load_and_show_head(self):
        """Load CSV file into pandas DataFrame and display head"""
        if not self.file_path:
            messagebox.showerror("Error", "Please select a CSV file first")
            return
            
        try:
            # Update status
            self.status_bar.config(text="Loading CSV file...")
            self.root.update()
            
            # Load CSV into pandas DataFrame
            self.df = pd.read_csv(self.file_path, skiprows=11)
            
            # Clear text area
            self.text_area.delete(1.0, tk.END)
            
            # Display basic info
            info_text = f"Shape: {self.df.shape} | Columns: {len(self.df.columns)} | Rows: {len(self.df)}\n"
            info_text += f"Memory usage: {self.df.memory_usage(deep=True).sum() / 1024:.1f} KB\n"
            info_text += "-" * 80 + "\n"
            
            self.text_area.insert(tk.END, info_text)
            
            # Display column info
            self.text_area.insert(tk.END, "COLUMNS:\n")
            for i, col in enumerate(self.df.columns):
                dtype = str(self.df[col].dtype)
                null_count = self.df[col].isnull().sum()
                col_info = f"{i+1:2d}. {col:<25} | {dtype:<10} | {null_count} nulls\n"
                self.text_area.insert(tk.END, col_info)
            
            self.text_area.insert(tk.END, "\n" + "="*80 + "\n")
            self.text_area.insert(tk.END, "FIRST 5 ROWS:\n")
            self.text_area.insert(tk.END, "="*80 + "\n\n")
            
            # Display head of DataFrame
            head_str = self.df.head().to_string()
            self.text_area.insert(tk.END, head_str)
            
            # Print to console as well
            print(f"\nLoaded CSV: {os.path.basename(self.file_path)}")
            print(f"Shape: {self.df.shape}")
            print("\nDataFrame Head:")
            print(self.df.head())
            
            # Update info label and status
            self.info_label.config(text=f"Loaded successfully! Shape: {self.df.shape}")
            self.status_bar.config(text="CSV loaded successfully")
            
        except Exception as e:
            error_msg = f"Error loading CSV: {str(e)}"
            messagebox.showerror("Error", error_msg)
            self.status_bar.config(text="Error loading file")
            print(f"Error: {error_msg}")

def main():
    root = tk.Tk()
    app = CSVLoader(root)
    root.mainloop()

if __name__ == "__main__":
    main()