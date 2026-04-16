import time
import random
from PyQt6.QtCore import QThread, pyqtSignal
from .input_simulator import InputSimulator

class ClickerThread(QThread):
    finished_signal = pyqtSignal()
    
    def __init__(self, mode='global', window_id=None, button='left', 
                 delay_ms=100, variance_ms=20, hold_ms=0, coordinates=None):
        super().__init__()
        self.mode = mode
        self.window_id = window_id
        self.button = button
        self.delay_ms = delay_ms
        self.variance_ms = variance_ms
        self.hold_ms = hold_ms
        self.coordinates = coordinates
        self.running = False
        self.simulator = InputSimulator(
            target_window_id=window_id if mode == 'targeted' else None,
            button=button
        )
        
    def run(self):
        self.running = True
        
        while self.running:
            # Set cursor pos if global and coordinates matched
            # Move cursor only if we are in global mode and have coordinates
            if self.mode == 'global' and self.coordinates:
                # Need pynput mouse
                if self.simulator.mouse:
                    self.simulator.mouse.position = self.coordinates
            
            hold_sec = self.hold_ms / 1000.0
            
            self.simulator.click(hold_time=hold_sec)
            
            if not self.running:
                break
                
            # Apply delay with randomness
            delay = max(0, self.delay_ms / 1000.0)
            variance = random.uniform(0, self.variance_ms / 1000.0)
            
            time.sleep(delay + variance)
            
        self.finished_signal.emit()

    def stop(self):
        self.running = False
