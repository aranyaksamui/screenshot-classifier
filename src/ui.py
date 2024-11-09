import tkinter as tk
from tkinter import filedialog
from tkinter import ttk


root = tk.Tk()

# Main window
root.geometry("350x200")
root.title("Screenshot Classifier")

ttk.Style().configure("TButton", padding=2, relief="flat")

# A heading label
label = ttk.Label(root, text="Extra organize your screenshots!", font=("Helvetica", 14)).pack()

# Open folder FileDialog
def select_dir():
    directory_selected = filedialog.askdirectory()
    create_or_get_base_directory()
    
info = ttk.Label(root, text="Select screenshot directory:", font=("Helvetica", 11)).pack()
browse_button = ttk.Button(root, text="Browse", command=select_dir).pack()


root.mainloop()