import keyboard
import screenshot
import file_handler


# Create a hotkey to take screenshot
class Hotkey:
    def __init__(self, ui):
        self.ui = ui
    
    def hotkey_action(self):
        if not file_handler.get_base_save_directory_path():
            self.ui.save_dir_reminder()
        else:
            screenshot.capture_screenshot()
    
    # Initialize the hotkey
    def initialize_hotkey(self):
        try:
            keyboard.add_hotkey("windows+shift+insert", self.hotkey_action)
        except Exception as e:
            print(e)