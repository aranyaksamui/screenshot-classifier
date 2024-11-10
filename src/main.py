from ui import UI
from hotkey import Hotkey


# Application start
def main():
    ui = UI()
    hotkey = Hotkey(ui)
    hotkey.initialize_hotkey()
    ui.run()
        
        
if __name__ == "__main__":
    main()