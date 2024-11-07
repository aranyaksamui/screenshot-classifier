from datetime import datetime
import os
import window

# Get save directory
def get_directory():
    base_dir = r"C:\Users\arany\Pictures\Screenshots"
    active_foreground_window = window.get_active_foreground_window()
    directory_name = active_foreground_window.replace(" ", "_").replace("-", "").replace(".", "")
    
    full_path = os.path.join(base_dir, directory_name)
    
    return base_dir
    

# Create the file name for the screenshot
def create_filename():
    timestamp = datetime.now().strftime("%d%m%Y_%H%M%S")
    
    active_foreground_window = window.get_active_foreground_window()
    window_string = active_foreground_window.replace(" ", "_").replace("-", "").replace(".", "")
    
    filename = f"{timestamp}__{window_string}.png"
    
    return filename