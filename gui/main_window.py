import sys
from PyQt6.QtWidgets import (
    QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, 
    QGroupBox, QLabel, QLineEdit, QComboBox, QSpinBox, 
    QPushButton, QRadioButton, QButtonGroup, QMessageBox
)
from PyQt6.QtCore import Qt, pyqtSlot
from core.window_manager import get_windows
from core.clicker import ClickerThread
from pynput import keyboard

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Zenith Auto Clicker")
        self.resize(500, 600)
        
        self.clicker_thread = None
        self.hotkey_listener = None
        
        self.start_hotkey = '<f6>'
        
        self._init_ui()
        self._setup_hotkeys()

    def _init_ui(self):
        main_widget = QWidget()
        self.setCentralWidget(main_widget)
        
        layout = QVBoxLayout(main_widget)
        layout.setContentsMargins(20, 20, 20, 20)
        layout.setSpacing(15)
        
        # Header
        header = QLabel("ZENITH AUTO CLICKER")
        header.setAlignment(Qt.AlignmentFlag.AlignCenter)
        header.setStyleSheet("font-size: 24px; font-weight: bold; color: #00E5FF; letter-spacing: 2px;")
        layout.addWidget(header)
        
        # Target Selection Group
        self.target_group_widget = QGroupBox("Target Selection")
        target_layout = QVBoxLayout()
        
        mode_layout = QHBoxLayout()
        self.radio_global = QRadioButton("Global (Cursor Pos)")
        self.radio_global.setChecked(True)
        self.radio_window = QRadioButton("Targeted Window")
        
        self.mode_group = QButtonGroup(self)
        self.mode_group.addButton(self.radio_global)
        self.mode_group.addButton(self.radio_window)
        
        mode_layout.addWidget(self.radio_global)
        mode_layout.addWidget(self.radio_window)
        target_layout.addLayout(mode_layout)

        window_layout = QHBoxLayout()
        self.window_combo = QComboBox()
        self.window_combo.setEnabled(False)
        self.refresh_btn = QPushButton("Refresh")
        self.refresh_btn.setEnabled(False)
        self.refresh_btn.clicked.connect(self._refresh_windows)
        
        window_layout.addWidget(self.window_combo, stretch=1)
        window_layout.addWidget(self.refresh_btn)
        target_layout.addLayout(window_layout)
        
        self.target_group_widget.setLayout(target_layout)
        layout.addWidget(self.target_group_widget)
        
        self.radio_global.toggled.connect(self._on_mode_change)
        
        # Click Configuration Group
        self.click_group_widget = QGroupBox("Click Configuration")
        click_layout = QVBoxLayout()
        
        grid1 = QHBoxLayout()
        grid1.addWidget(QLabel("Button:"))
        self.button_combo = QComboBox()
        self.button_combo.addItems(["Left", "Right", "Middle"])
        grid1.addWidget(self.button_combo)
        
        grid1.addSpacing(20)
        
        grid1.addWidget(QLabel("Delay (ms):"))
        self.delay_spin = QSpinBox()
        self.delay_spin.setRange(1, 100000)
        self.delay_spin.setValue(100)
        grid1.addWidget(self.delay_spin)
        click_layout.addLayout(grid1)
        
        grid2 = QHBoxLayout()
        grid2.addWidget(QLabel("Random Variance (ms):"))
        self.variance_spin = QSpinBox()
        self.variance_spin.setRange(0, 10000)
        self.variance_spin.setValue(20)
        grid2.addWidget(self.variance_spin)
        
        grid2.addSpacing(20)
        
        grid2.addWidget(QLabel("Hold (ms):"))
        self.hold_spin = QSpinBox()
        self.hold_spin.setRange(0, 50000)
        self.hold_spin.setValue(0)
        grid2.addWidget(self.hold_spin)
        click_layout.addLayout(grid2)
        
        self.click_group_widget.setLayout(click_layout)
        layout.addWidget(self.click_group_widget)
        
        # Hotkey Configuration
        hotkey_group = QGroupBox("Hotkeys")
        hotkey_layout = QHBoxLayout()
        hotkey_layout.addWidget(QLabel("Start/Stop Hotkey (Global):"))
        self.hotkey_input = QLineEdit(self.start_hotkey)
        self.hotkey_input.setReadOnly(True)
        hotkey_layout.addWidget(self.hotkey_input)
        hotkey_group.setLayout(hotkey_layout)
        layout.addWidget(hotkey_group)
        
        info_label = QLabel("Toggle auto clicker using the configured hotkey (e.g. <f6>).")
        info_label.setObjectName("secondaryText")
        layout.addWidget(info_label)
        
        # Controls
        control_layout = QHBoxLayout()
        self.start_btn = QPushButton("START")
        self.start_btn.setObjectName("startBtn")
        self.start_btn.clicked.connect(self._toggle_clicker)
        
        self.stop_btn = QPushButton("STOP")
        self.stop_btn.setObjectName("stopBtn")
        self.stop_btn.setEnabled(False)
        self.stop_btn.clicked.connect(self._toggle_clicker)
        
        control_layout.addWidget(self.start_btn)
        control_layout.addWidget(self.stop_btn)
        layout.addLayout(control_layout)
        
    def _refresh_windows(self):
        self.window_combo.clear()
        windows = get_windows()
        for wid, title in windows:
            self.window_combo.addItem(f"{title} ({wid})", wid)
            
    def _on_mode_change(self):
        is_targeted = self.radio_window.isChecked()
        self.window_combo.setEnabled(is_targeted)
        self.refresh_btn.setEnabled(is_targeted)
        if is_targeted and self.window_combo.count() == 0:
            self._refresh_windows()

    def _setup_hotkeys(self):
        self.hotkey_listener = keyboard.GlobalHotKeys({
            self.start_hotkey: self._on_hotkey
        })
        self.hotkey_listener.start()

    def _on_hotkey(self):
        from PyQt6.QtCore import QMetaObject, Qt
        QMetaObject.invokeMethod(self, "_toggle_clicker", Qt.ConnectionType.QueuedConnection)

    @pyqtSlot()
    def _toggle_clicker(self):
        if self.clicker_thread and self.clicker_thread.isRunning():
            self.clicker_thread.stop()
            self._set_ui_running(False)
        else:
            mode = 'global' if self.radio_global.isChecked() else 'targeted'
            window_id = None
            if mode == 'targeted':
                if self.window_combo.count() == 0:
                    QMessageBox.warning(self, "Error", "No window selected!")
                    return
                window_id = self.window_combo.currentData()
                
            button = self.button_combo.currentText().lower()
            delay = self.delay_spin.value()
            variance = self.variance_spin.value()
            hold = self.hold_spin.value()
            
            self.clicker_thread = ClickerThread(
                mode=mode, 
                window_id=window_id, 
                button=button, 
                delay_ms=delay, 
                variance_ms=variance, 
                hold_ms=hold
            )
            self.clicker_thread.finished_signal.connect(lambda: self._set_ui_running(False))
            self.clicker_thread.start()
            self._set_ui_running(True)
            
    def _set_ui_running(self, running):
        self.start_btn.setEnabled(not running)
        self.stop_btn.setEnabled(running)
        if hasattr(self, 'target_group_widget'):
            self.target_group_widget.setEnabled(not running)
        if hasattr(self, 'click_group_widget'):
            self.click_group_widget.setEnabled(not running)

    def closeEvent(self, event):
        if self.clicker_thread and self.clicker_thread.isRunning():
            self.clicker_thread.stop()
            self.clicker_thread.wait()
        if self.hotkey_listener:
            self.hotkey_listener.stop()
        event.accept()
