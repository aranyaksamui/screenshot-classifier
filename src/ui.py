import tkinter as tk
from tkinter import filedialog
from tkinter import ttk
import file_handler

# Create UI
class UI:
    def __init__(self):
        self.root = tk.Tk()
        self.root.geometry("350x200")
        self.root.title("Screenshot Classifier")
        self.is_open = False

        self.init_ui()

    # Initialize UI components
    def init_ui(self):
        ttk.Style().configure("TButton", padding=2, relief="flat")
        # A heading label
        label = ttk.Label(self.root, text="Extra organize your screenshots!", font=("Helvetica", 14)).pack()
        self.save_label_text = tk.StringVar()
        self.browse_button = ttk.Button(self.root, text="Browse", command=self.select_dir)
        self.browse_button.pack()

        if (file_handler.get_base_save_directory_path() == None):
            self.save_label_text.set(f"Please select a base save path for screenshots")
            ttk.Label(self.root, textvariable=self.save_label_text).pack()
            
        else:
            self.save_label_text.set(file_handler.get_base_save_directory_path())
            base_save_path = ttk.Label(self.root, textvariable=self.save_label_text).pack()
        
        shortcut_label = ttk.Label(self.root, text="Press 'shift + windows + insert' for screenshot", font=("Helvetica", 10)).pack()
    
    # Select base save directory dialog
    def select_dir(self):
        directory_selected = filedialog.askdirectory()
        file_handler.create_or_update_base_directory_path(directory_selected)
        self.save_label_text.set(file_handler.get_base_save_directory_path())
    
    # Base save directory reminder
    def save_dir_reminder(self):
        self.save_label_text.set(f"Something went wrong! Check if the save path is created")
        ttk.Label(self.root, textvariable=self.save_label_text).pack()
    
    # Run the UI
    def run(self):
        self.root.mainloop()
