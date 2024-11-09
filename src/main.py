import keyboard
import screenshot
# from ui import UI
import ui
import file_handler

# Application start
def main():
    # ui = UI()
    # ui.run()
    
    print(file_handler.get_save_directory_path())
    try:
        if (file_handler.get_save_directory_path() != None):
            keyboard.add_hotkey("windows+shift+insert", screenshot.capture_screenshot)
        else:
            print("Save path is none from main.py")
        
    except Exception as e:
        print(e)
    ui.draw_ui()
        
        
if __name__ == "__main__":
    main()