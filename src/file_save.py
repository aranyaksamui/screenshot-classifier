from datetime import datetime
import os
import window

# Get save directory
def get_directory():
    base_dir = r"C:\Users\arany\Pictures\Screenshots"
    active_foreground_window = window.get_active_foreground_window()
    directory_name = active_foreground_window.replace(" ", "_").replace("-", "").replace(".", "")
    
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
    window_string = active_foreground_window.replace(" ", "_").replace("-", "").replace(".", "")
    
    filename = f"{timestamp}__{window_string}.png"
    
    return filename