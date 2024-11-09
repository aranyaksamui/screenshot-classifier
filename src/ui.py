import tkinter as tk
from tkinter import filedialog
from tkinter import ttk
import keyboard
import file_handler
import screenshot


# class UI:
#     def __init__(self):
#         self.root = tk.Tk()
#         self.root.geometry("350x200")
#         self.root.title("Screenshot Classifier")
#         self.is_open = False

#         # Initialize UI components
#         self.init_ui()

#     def init_ui(self):
#         self.save_label_text = tk.StringVar()
#         self.browse_button = ttk.Button(self.root, text="Browse", command=self.select_dir)
#         self.browse_button.pack()

#         self.base_save_path = ttk.Label(self.root, textvariable=self.save_label_text)
#         self.base_save_path.pack()

#         self.close_button = ttk.Button(self.root, text="Close", command=self.on_close)
#         self.close_button.pack()

#     def select_dir(self):
#         directory_selected = filedialog.askdirectory()
#         file_handler.create_or_update_base_directory_path(directory_selected)
#         self.save_label_text.set(file_handler.get_save_directory_path())

#     def on_close(self):
#         self.unregister_hotkey()
#         self.root.destroy()

#     def register_hotkey(self):
#         if file_handler.get_save_directory_path():
#             print("You can now use the hotkey")
#             self.hotkey_id = keyboard.add_hotkey("windows+shift+insert", self.screenshot_callback)
#         else:
#             print("Save path is not set.")

#     def unregister_hotkey(self):
#         if hasattr(self, 'hotkey_id'):
#             keyboard.unhook(self.hotkey_id)

#     def screenshot_callback(self):
#         if self.is_open:
#             screenshot.capture_screenshot()

#     def run(self):
#         self.register_hotkey()
#         self.is_open = True
#         self.root.mainloop()
#         self.is_open = False

# # Usage
# if __name__ == "__main__":
#     ui = UI()
#     ui.run()












root = tk.Tk()

def draw_ui():
    # Main window
    root.geometry("350x200")
    root.title("Screenshot Classifier")

    ttk.Style().configure("TButton", padding=2, relief="flat")

    # A heading label
    label = ttk.Label(root, text="Extra organize your screenshots!", font=("Helvetica", 14)).pack()

    save_label_text = tk.StringVar()

    # Open folder FileDialog
    def select_dir():
        directory_selected = filedialog.askdirectory()
        file_handler.create_or_update_base_directory_path(directory_selected)
        save_label_text.set(file_handler.get_save_directory_path())
        
        
    info = ttk.Label(root, text="Select screenshot directory:", font=("Helvetica", 11)).pack()
    browse_button = ttk.Button(root, text="Browse", command=select_dir).pack()

    # Base save path label
    if (file_handler.get_save_directory_path() == None):
        save_label_text.set(f"Please select a base save path for screenshots")
        ttk.Label(root, textvariable=save_label_text).pack()
    else:
        save_label_text.set(file_handler.get_save_directory_path())
        base_save_path = ttk.Label(root, textvariable=save_label_text).pack()
        
    root.mainloop()
    
def destroy_ui():
    root.destroy()