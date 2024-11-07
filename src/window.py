from win32gui import *

# Get active window text in the foreground
def get_active_foreground_window():
    active_HWND_text = GetWindowText(GetForegroundWindow())\
        
    return active_HWND_text

