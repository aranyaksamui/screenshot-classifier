from PIL import ImageGrab
import os
import file_save

# Capture the screenshot and save it
def capture_screenshot():
    try:
        #Capture screenshot
        screenshot = ImageGrab.grab()
        
        # Create a filepath
        filepath = os.path.join(file_save.get_directory(), file_save.create_filename())
        
        # Save the screenshot
        screenshot.save(filepath)
        print("Screenshot saved")
    except Exception as e:
        print(f"Something went wrong: {e}")