from PIL import ImageGrab
import os
import file_handler


# Capture the screenshot and save it
def capture_screenshot():
    try:
        #Capture screenshot
        screenshot = ImageGrab.grab()
        
        # Create a filepath
        filepath = os.path.join(file_handler.get_subdirectory(), file_handler.create_filename())
        
        # Save the screenshot
        screenshot.save(filepath)
        print("Screenshot saved")
        
    except Exception as e:
        print(f"Something went wrong: {e}")