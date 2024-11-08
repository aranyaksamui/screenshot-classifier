from datetime import datetime
import os
import re
import window


# Validate and sanitize directory and filename string
def cleanup_name(name_string):
    valid_chars = r"[^a-zA-Z0-9_]+"
    
    name_string = str(name_string)
    filename = name_string.replace(" ", "_") and re.sub(valid_chars, "", name_string)
    
    return filename


# Get save directory
def get_directory():
    base_dir = r"C:\Users\arany\Pictures\Screenshots"
    active_foreground_window = window.get_active_foreground_window()
    directory_name = cleanup_name(active_foreground_window)
    
    full_path = os.path.join(base_dir, directory_name)
    
    # If directory exists then return it's path else create a new directory and return it's path
    if (os.path.exists(full_path)):
        return full_path
    else:
        new_path = os.path.join(base_dir, directory_name)
        try:
            os.mkdir(new_path)
            return new_path
        
        except OSError as e:
            print(e)
    

# Create the file name for the screenshot
def create_filename():
    timestamp = datetime.now().strftime("%d%m%Y_%H%M%S")
    
    active_foreground_window = window.get_active_foreground_window()
    window_string = cleanup_name(active_foreground_window)
    
    filename = f"{timestamp}__{window_string}.png"
    
    return filename