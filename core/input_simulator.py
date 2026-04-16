import sys
import time
import threading

class InputSimulator:
    def __init__(self, target_window_id=None, button='left'):
        self.target_window_id = target_window_id
        if button == 'left':
            self.button_code = 1
        elif button == 'right':
            self.button_code = 3
        elif button == 'middle':
            self.button_code = 2
        else:
            self.button_code = 1
            
        self.mouse = None
        self.buttons = None
        
        # Setup cross-platform global mouse for non-targeted
        try:
            from pynput.mouse import Controller, Button
            self.mouse = Controller()
            self.buttons = {
                'left': Button.left,
                'right': Button.right,
                'middle': Button.middle
            }
            self.button_enum = self.buttons.get(button, Button.left)
        except ImportError:
            pass
            
    def click(self, hold_time=0.0):
        if self.target_window_id:
            # Targeted Click
            if sys.platform == "win32":
                self._click_windows_targeted(hold_time)
            elif sys.platform.startswith("linux"):
                self._click_linux_targeted(hold_time)
        else:
            # Global Click
            if self.mouse:
                self.mouse.press(self.button_enum)
                if hold_time > 0:
                    time.sleep(hold_time)
                self.mouse.release(self.button_enum)

    def _click_windows_targeted(self, hold_time):
        try:
            import win32api
            import win32con
            hwnd = int(self.target_window_id)
            
            # Map button
            if self.button_code == 1:
                msg_down = win32con.WM_LBUTTONDOWN
                msg_up = win32con.WM_LBUTTONUP
            elif self.button_code == 3:
                msg_down = win32con.WM_RBUTTONDOWN
                msg_up = win32con.WM_RBUTTONUP
            else:
                msg_down = win32con.WM_MBUTTONDOWN
                msg_up = win32con.WM_MBUTTONUP
                
            win32api.PostMessage(hwnd, msg_down, 1, 0)
            if hold_time > 0:
                time.sleep(hold_time)
            win32api.PostMessage(hwnd, msg_up, 0, 0)
        except Exception as e:
            print(f"Windows targeted click error: {e}")

    def _click_linux_targeted(self, hold_time):
        try:
            import subprocess
            wid = str(self.target_window_id)
            # Send xdotool command in a background thread or process without blocking if delay is large
            # We are already in a thread, so blocking here is fine
            if hold_time > 0:
                subprocess.run(['xdotool', 'mousedown', '--window', wid, str(self.button_code)])
                time.sleep(hold_time)
                subprocess.run(['xdotool', 'mouseup', '--window', wid, str(self.button_code)])
            else:
                subprocess.run(['xdotool', 'click', '--window', wid, str(self.button_code)])
        except Exception as e:
            print(f"Linux targeted click error: {e}")
