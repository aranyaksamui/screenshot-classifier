from datetime import datetime
import os
import re
import window


base_dir = r"C:\Users\arany\Pictures\Screenshots"
def create_or_get_base_directory_path():
    pass


# Validate and sanitize directory and filename string
# Modes:
# 0 - Files and Sub-folders
# 1 - Parent folders
def cleanup_name(name_string, mode):
    name_string = str(name_string)
    if (mode == 0):
        valid_chars = r"[^a-zA-Z0-9_]+"
        
        name_string = name_string.replace(" ", "_")
        filename = re.sub(valid_chars, "", name_string)
    
        return filename
    
    elif (mode == 1):
        app_name = name_string.split(".")[0].capitalize()
        
        return app_name
    
    
# If directory exists then return it's path else create a new directory and return it's path
def return_or_create_path(full_path):
    if (os.path.exists(full_path)):
        return full_path
    
    else:
        try:
            os.mkdir(full_path)
            return full_path
        
        except OSError as e:
            print(e)
    
    
# Get save parent directory
def get_parent_directory():
    active_foreground_app = window.get_active_app_name()
    directory_name = cleanup_name(active_foreground_app, 1)
    
    full_path = os.path.join(base_dir, directory_name)
    path = return_or_create_path(full_path)
    
    return (directory_name, path)


# Get save sub-directory
def get_subdirectory():
    parent_directory = get_parent_directory()[1]
    
    active_foreground_window = window.get_active_foreground_window()
    subdirectory_name = cleanup_name(active_foreground_window, 0)
    
    if (get_parent_directory()[0] == subdirectory_name):
        full_path = os.path.join(base_dir, subdirectory_name)
        path = return_or_create_path(full_path)
        
        return path
        
    else:
        full_path = os.path.join(parent_directory, subdirectory_name)
        path = return_or_create_path(full_path)
    
        return path
    
    
# Create the file name for the screenshot
def create_filename():
    timestamp = datetime.now().strftime("%d%m%Y_%H%M%S")
    
    active_foreground_window = window.get_active_foreground_window()
    window_string = cleanup_name(active_foreground_window, 0)
    
    filename = f"{timestamp}__{window_string}.png"
    
    return filename