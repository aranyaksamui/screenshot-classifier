import keyboard
import screenshot


# Application start
def main():
    try:
        print("1. Press ctrl + shift + prtsc to capture a screenshot.\n2. Press shift + esc to close")
        keyboard.add_hotkey("windows+shift+insert", screenshot.capture_screenshot)
        keyboard.wait("shift+esc")
        
    except Exception as e:
        print(e)
        
if __name__ == "__main__":
    main()