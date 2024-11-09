import win32gui
import win32process
import psutil


# Get active window text in the foreground
def get_active_foreground_window():
    active_HWND_text = win32gui.GetWindowText(win32gui.GetForegroundWindow())
        
    return active_HWND_text


# Get the active window application name with process ID
def get_active_app_name():
    active_HWND = win32gui.GetForegroundWindow()
    active_pid = win32process.GetWindowThreadProcessId(active_HWND)

    p_name = psutil.Process(active_pid[-1]).name()
    
    return p_name
    