import tkinter as tk
from tkinter import ttk, filedialog, messagebox, scrolledtext
import pandas as pd
import os

# Global variables
current_app_frame = None
main_content_frame = None
df = None
file_path = None

def clear_content():
    """Clear the main content area"""
    global current_app_frame
    if current_app_frame:
        current_app_frame.destroy()
        current_app_frame = None

def create_csv_loader_app():
    """Create the CSV Loader application"""
    global current_app_frame, main_content_frame, df, file_path
    
    clear_content()
    current_app_frame = ttk.Frame(main_content_frame)
    current_app_frame.pack(fill=tk.BOTH, expand=True)
    
    # Header
    header_frame = ttk.Frame(current_app_frame)
    header_frame.pack(fill=tk.X, padx=20, pady=20)
    
    ttk.Label(header_frame, text="📊 CSV Data Loader", 
             font=("Arial", 16, "bold")).pack(anchor=tk.W)
    ttk.Label(header_frame, text="Load and analyze CSV files", 
             font=("Arial", 10), foreground="gray").pack(anchor=tk.W)
    
    # File selection section
    file_section = ttk.LabelFrame(current_app_frame, text="File Selection", padding=15)
    file_section.pack(fill=tk.X, padx=20, pady=10)
    
    file_frame = ttk.Frame(file_section)
    file_frame.pack(fill=tk.X)
    
    ttk.Button(file_frame, text="Browse Files", 
              command=select_csv_file).pack(side=tk.LEFT, padx=(0, 10))
    
    # Create file label as global so we can update it
    global file_label, load_button
    file_label = ttk.Label(file_frame, text="No file selected", foreground="gray")
    file_label.pack(side=tk.LEFT, fill=tk.X, expand=True)
    
    load_button = ttk.Button(file_frame, text="Load Data", 
                            command=load_csv_data, state=tk.DISABLED)
    load_button.pack(side=tk.RIGHT)
    
    # Data display section
    data_section = ttk.LabelFrame(current_app_frame, text="Data Preview", padding=15)
    data_section.pack(fill=tk.BOTH, expand=True, padx=20, pady=10)
    
    # Info frame
    global info_frame, text_area
    info_frame = ttk.Frame(data_section)
    info_frame.pack(fill=tk.X, pady=(0, 10))
    
    # Text area for data
    text_area = scrolledtext.ScrolledText(data_section, 
                                         font=("Consolas", 9),
                                         wrap=tk.NONE)
    text_area.pack(fill=tk.BOTH, expand=True)

def select_csv_file():
    """Handle CSV file selection"""
    global file_path, file_label, load_button
    
    selected_file = filedialog.askopenfilename(
        title="Select CSV File",
        filetypes=[("CSV files", "*.csv"), ("All files", "*.*")]
    )
    
    if selected_file:
        file_path = selected_file
        filename = os.path.basename(selected_file)
        file_label.config(text=filename)
        load_button.config(state=tk.NORMAL)

def load_csv_data():
    """Load and display CSV data"""
    global df, file_path, info_frame, text_area
    
    if not file_path:
        messagebox.showerror("Error", "Please select a CSV file first")
        return
    
    try:
        # Load CSV
        df = pd.read_csv(file_path)
        
        # Clear previous info
        for widget in info_frame.winfo_children():
            widget.destroy()
        
        # Display file info
        info_text = f"Shape: {df.shape} | Memory: {df.memory_usage(deep=True).sum() / 1024:.1f} KB"
        ttk.Label(info_frame, text=info_text, font=("Arial", 9)).pack(anchor=tk.W)
        
        # Clear and populate text area
        text_area.delete(1.0, tk.END)
        text_area.insert(tk.END, "COLUMNS:\n")
        text_area.insert(tk.END, "-" * 50 + "\n")
        
        # Show column info
        for i, col in enumerate(df.columns):
            dtype = str(df[col].dtype)
            null_count = df[col].isnull().sum()
            col_info = f"{i+1:2d}. {col:<20} | {dtype:<10} | {null_count} nulls\n"
            text_area.insert(tk.END, col_info)
        
        # Show data preview
        text_area.insert(tk.END, "\n" + "="*60 + "\n")
        text_area.insert(tk.END, "FIRST 5 ROWS:\n")
        text_area.insert(tk.END, "="*60 + "\n\n")
        text_area.insert(tk.END, df.head().to_string())
        
        # Print to console
        print(f"\nLoaded: {os.path.basename(file_path)}")
        print(df.head())
        
    except Exception as e:
        messagebox.showerror("Error", f"Error loading CSV: {str(e)}")

def create_kpi_app():
    """Create the KPI Dashboard application"""
    global current_app_frame, main_content_frame
    
    clear_content()
    current_app_frame = ttk.Frame(main_content_frame)
    current_app_frame.pack(fill=tk.BOTH, expand=True)
    
    # Header
    header_frame = ttk.Frame(current_app_frame)
    header_frame.pack(fill=tk.X, padx=20, pady=20)
    
    ttk.Label(header_frame, text="📈 KPI Dashboard", 
             font=("Arial", 16, "bold")).pack(anchor=tk.W)
    ttk.Label(header_frame, text="Track and analyze key performance indicators", 
             font=("Arial", 10), foreground="gray").pack(anchor=tk.W)
    
    # Content
    content_frame = ttk.LabelFrame(current_app_frame, text="KPI Metrics", padding=20)
    content_frame.pack(fill=tk.BOTH, expand=True, padx=20, pady=10)
    
    ttk.Label(content_frame, text="🚧 KPI Dashboard Coming Soon!", 
             font=("Arial", 14)).pack(pady=50)
    
    features_text = """Features will include:
• Real-time KPI monitoring
• Data visualization
• Performance analytics
• Custom metrics"""
    
    ttk.Label(content_frame, text=features_text, 
             font=("Arial", 10), justify=tk.LEFT).pack()

def create_excel_automation_app():
    """Create the Excel Automation application"""
    global current_app_frame, main_content_frame
    
    clear_content()
    current_app_frame = ttk.Frame(main_content_frame)
    current_app_frame.pack(fill=tk.BOTH, expand=True)
    
    # Header
    header_frame = ttk.Frame(current_app_frame)
    header_frame.pack(fill=tk.X, padx=20, pady=20)
    
    ttk.Label(header_frame, text="📋 Excel Automation", 
             font=("Arial", 16, "bold")).pack(anchor=tk.W)
    ttk.Label(header_frame, text="Automate Excel tasks and workflows", 
             font=("Arial", 10), foreground="gray").pack(anchor=tk.W)
    
    # Content
    content_frame = ttk.LabelFrame(current_app_frame, text="Automation Tools", padding=20)
    content_frame.pack(fill=tk.BOTH, expand=True, padx=20, pady=10)
    
    ttk.Label(content_frame, text="🚧 Excel Automation Coming Soon!", 
             font=("Arial", 14)).pack(pady=50)
    
    features_text = """Features will include:
• Bulk file processing
• Template generation
• Data transformation
• Report automation"""
    
    ttk.Label(content_frame, text=features_text, 
             font=("Arial", 10), justify=tk.LEFT).pack()

def create_sidebar(parent):
    """Create the sidebar navigation"""
    # Sidebar frame
    sidebar = ttk.Frame(parent, width=250)
    sidebar.pack(side=tk.LEFT, fill=tk.Y, padx=(0, 2))
    sidebar.pack_propagate(False)
    
    # Header
    header_frame = ttk.Frame(sidebar)
    header_frame.pack(fill=tk.X, padx=15, pady=20)
    
    ttk.Label(header_frame, text="📊 Analytics Hub", 
             font=("Arial", 14, "bold")).pack(anchor=tk.W)
    ttk.Label(header_frame, text="Business Intelligence Tools", 
             font=("Arial", 8), foreground="gray").pack(anchor=tk.W)
    
    # Separator
    ttk.Separator(sidebar, orient=tk.HORIZONTAL).pack(fill=tk.X, padx=15, pady=10)
    
    # Navigation buttons
    nav_frame = ttk.Frame(sidebar)
    nav_frame.pack(fill=tk.BOTH, expand=True, padx=15)
    
    # App buttons
    apps = [
        ("📊 CSV Loader", create_csv_loader_app),
        ("📈 KPI Dashboard", create_kpi_app),
        ("📋 Excel Automation", create_excel_automation_app)
    ]
    
    for app_name, app_function in apps:
        ttk.Button(nav_frame, text=app_name, 
                  command=app_function).pack(fill=tk.X, pady=2)
    
    # Footer
    footer_frame = ttk.Frame(sidebar)
    footer_frame.pack(fill=tk.X, padx=15, pady=20)
    
    ttk.Label(footer_frame, text="v1.0.0", 
             font=("Arial", 8), foreground="gray").pack(anchor=tk.W)

def add_new_app(name, icon, create_function):
    """
    Helper function to add new apps easily
    Usage: add_new_app("My App", "🔧", create_my_app)
    """
    # You can call this function to add new apps dynamically
    # For now, it's just a template for future use
    pass

def create_main_window():
    """Create the main application window"""
    global main_content_frame
    
    # Main window
    root = tk.Tk()
    root.title("Business Analytics Platform")
    root.geometry("1200x800")
    root.minsize(1000, 600)
    
    # Configure style
    style = ttk.Style()
    style.theme_use('clam')
    
    # Main container
    main_container = ttk.Frame(root)
    main_container.pack(fill=tk.BOTH, expand=True)
    
    # Create sidebar
    create_sidebar(main_container)
    
    # Content area
    main_content_frame = ttk.Frame(main_container)
    main_content_frame.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)
    
    # Show default app
    create_csv_loader_app()
    
    return root

def main():
    """Main function to run the application"""
    root = create_main_window()
    root.mainloop()

# How to add a new app:
# 1. Create a function like create_my_new_app()
# 2. Add it to the apps list in create_sidebar()
# 3. That's it!

if __name__ == "__main__":
    main()