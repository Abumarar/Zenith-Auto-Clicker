import sys

def get_windows():
    windows = []
    if sys.platform == "win32":
        try:
            import win32gui
            def callback(hwnd, extra):
                if win32gui.IsWindowVisible(hwnd) and win32gui.GetWindowText(hwnd):
                    windows.append((hwnd, win32gui.GetWindowText(hwnd)))
                return True
            win32gui.EnumWindows(callback, None)
        except ImportError:
            pass
    elif sys.platform.startswith("linux"):
        try:
            from Xlib import display
            d = display.Display()
            root = d.screen().root
            NET_CLIENT_LIST = d.intern_atom('_NET_CLIENT_LIST')
            prop = root.get_full_property(NET_CLIENT_LIST, 0)
            if prop:
                window_ids = prop.value
                NET_WM_NAME = d.intern_atom('_NET_WM_NAME')
                for wid in window_ids:
                    try:
                        w = d.create_resource_object('window', wid)
                        name_prop = w.get_full_property(NET_WM_NAME, 0)
                        if name_prop:
                            name = name_prop.value.decode('utf-8', errors='ignore')
                            if name:
                                windows.append((str(wid), name))
                    except Exception:
                        pass
        except ImportError:
            # Fallback to xdotool if Xlib is not available
            import subprocess
            try:
                output = subprocess.check_output(['xdotool', 'search', '--name', '.*']).decode('utf-8')
                for wid in output.strip().split():
                    try:
                        name = subprocess.check_output(['xdotool', 'getwindowname', wid]).decode('utf-8').strip()
                        if name:
                            windows.append((wid, name))
                    except subprocess.CalledProcessError:
                        continue
            except FileNotFoundError:
                pass
    return windows
