from datetime import datetime
import os
import re
import window
import pathlib
import json


# Get the config path and config file
def get_config_paths():
    config_base_path = str(pathlib.Path(__file__).absolute().parent.parent)
    config_path = os.path.join(config_base_path, r"config")
    
    config_file = "config.json"
    config_file_path = os.path.join(config_path, config_file)
    
    return (config_path, config_file_path)

# Create or update the screenshot base save path in config/config.json
def create_or_update_base_directory_path(base_screenshot_dir_path):
    # If the config folder does not exist, create it
    if (not os.path.exists(get_config_paths()[0])):
        try:
            os.mkdir(get_config_paths()[0])
            
        except OSError as e:
            print(e)
    
    # Create or update the screenshot base save path
    with open(get_config_paths()[1], "w") as config_file:
        json.dump({"savePath": f"{base_screenshot_dir_path}"}, config_file, indent=4)
    
    get_save_directory_path()
            
        
# Read the base screenshot save path
def get_save_directory_path():
    if (os.path.exists(get_config_paths()[1])):
        with open(get_config_paths()[1], "r") as config_file:
            config_data = json.load(config_file)
            
        if (isinstance(config_data, dict)):
            return config_data.get("savePath")
    else:
        return None


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
    
    if (get_save_directory_path() != None):
        full_path = os.path.join(get_save_directory_path(), directory_name)
        path = return_or_create_path(full_path)
        return (directory_name, path)
    else:
        print("Save path is none")
        pass


# Get save sub-directory
def get_subdirectory():
    parent_directory = get_parent_directory()[1]
    
    active_foreground_window = window.get_active_foreground_window()
    subdirectory_name = cleanup_name(active_foreground_window, 0)
    
    if (get_save_directory_path() != None):
        if (get_parent_directory()[0] == subdirectory_name):
            full_path = os.path.join(get_save_directory_path(), subdirectory_name)
            path = return_or_create_path(full_path)
            
            return path
            
        elif (get_parent_directory()[0] != subdirectory_name):
            full_path = os.path.join(parent_directory, subdirectory_name)
            path = return_or_create_path(full_path)
        
            return path
    else:
        print("Save path is none")
        pass
    
    
# Create the file name for the screenshot
def create_filename():
    timestamp = datetime.now().strftime("%d%m%Y_%H%M%S")
    
    active_foreground_window = window.get_active_foreground_window()
    window_string = cleanup_name(active_foreground_window, 0)
    
    filename = f"{timestamp}__{window_string}.png"
    
    return filename