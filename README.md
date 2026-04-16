# Zenith Auto Clicker

![Zenith Logo](https://via.placeholder.com/128x128.png?text=Z)

A sophisticated, modern, and cross-platform graphical auto clicker, designed for precision, gaming evasion, and simple automation. Available on both Linux (X11/GTK/KDE) and Windows 11.

---

## 📖 The Story

While immersed in a particularly grindy session of **Minecraft**, trying to optimize a zombie spawner XP farm, I realized I was spending more time standing in one spot than actually playing. I wanted a simple tool that would click my mouse for me, collecting experience points automatically, so I could step away and, you know, **eat**.

I began searching for auto clickers, looking for a simple utility that offered a graphical interface and decent customization. But I quickly ran into issues: options were outdated, restricted to a single OS, or lacked the specific targeted-application locking I needed.

Frustrated by the friction, I thought: **"You know what? Why wouldn't I create one?"**

**Zenith Auto Clicker** is the result of that frustration—a lightweight, capable clicker that just works, exactly how you expect it to.

---

## 🚀 Features

* **Cross-Platform Support:** Runs natively on Windows 11 and Linux (tested on Ubuntu and Linux Mint/X11).
* **Graphical User Interface (GUI):** A clean, modern interface built with PyQt6. No terminal editing required.
* **Application Targeting:** Choose which opened application you want to start the auto-clicker on. *Lock the clicker to a single window (e.g., "Minecraft Java Edition") so it continues clicking even when you alt-tab away.* (Supports X11 on Linux).
* **Human Simulation & Game Evasion:**
    * **Click Randomization:** Set a minimum delay and a random variance (ms) to simulate natural clicking and bypass basic anti-cheat detection.
    * **Hold Duration:** Control exactly how long the simulated "finger" holds the mouse button down (important for games requiring block-breaking or channeled actions).
* **Target Specific Coordinates:** Choose between clicking at your current cursor position or locking the click to specific X/Y coordinates.
* **Multi-Button Support:** Left, Right, and Middle mouse button simulation.
* **Global Hotkeys:** Bind start/stop functions to custom keyboard shortcuts that work even when the GUI is minimized.

---

## 🎨 UI/UX Design Guidelines

To maintain visual consistency with the Zenith brand, the graphical interface should strictly adhere to the following design system, inspired by our logo.

### Color Palette
* **App Background (Deep Space Blue):** `#0F172A` - Used for the main application window background.
* **Panel/Card Background (Slate Gray):** `#1E293B` - Used for grouping settings like "Click Configuration" and "Target Selection."
* **Primary Accent (Electric Cyan):** `#00E5FF` - Used for active states, slider fills, the "START" button, and active text highlights. It should have a subtle drop-shadow or "glow" effect when active.
* **Secondary Accent (Steel Blue):** `#38BDF8` - Used for hover states on buttons or secondary active elements.
* **Text (Primary):** `#F8FAFC` (Off-White) - For high readability on headers and primary labels.
* **Text (Secondary):** `#94A3B8` (Muted Gray) - For placeholder text, minor labels, and the footer.
* **Destructive Action (Muted Crimson):** `#E11D48` - Strictly reserved for the "STOP" button or error states.

### Typography & Styling
* **Font Family:** A modern, clean sans-serif like *Inter*, *Roboto*, or *Segoe UI*.
* **Borders & Corners:** Keep elements sharp with very subtle rounding (e.g., a border radius of 4px). Avoid overly bubbly or pill-shaped buttons to match the angular "peak" aesthetic of the logo.
* **Component Feedback:** Inputs and dropdowns should feature an Electric Cyan border when focused.

---

## 🛠️ Installation & Requirements

### Prerequisites

You will need Python 3.8 or later installed on your system.

### Option 1: Running from Source (Recommended for Linux users)

1.  **Clone the repository:**
    ```bash
    git clone [https://github.com/abumarar/ZenithAutoClicker.git](https://github.com/abumarar/ZenithAutoClicker.git)
    cd ZenithAutoClicker
    ```

2.  **Install the dependencies:**
    * **On Windows:**
        ```bash
        pip install -r requirements_windows.txt
        ```
    * **On Linux (Debian/Mint/Ubuntu):**
        *(Ensure you have X11 utilities installed if you are targeting specific applications.)*
        ```bash
        sudo apt install xdotool python3-xlib
        pip install -r requirements_linux.txt
        ```

3.  **Run the application:**
    ```bash
    python zenith.py
    ```

### Option 2: Pre-compiled Binaries

We will soon offer standalone executables for Windows (`.exe`) and Linux AppImages. Check the [Releases](https://github.com/abumarar/ZenithAutoClicker/releases) tab for the latest versions.

---

## 🚧 Contributing

This project is in active development. If you are a developer with experience in PyQt6 or system-level input simulation (especially improving targeting support on Wayland), contributions are extremely welcome!

* Submit issue reports for bugs or feature requests.
* Feel free to fork the repository and submit pull requests. Ensure any UI contributions follow the design guidelines above.

---

## ⚖️ License & Copyright

All content, software code, design assets, and documentation for **Zenith Auto Clicker** are copyright (©) Mohammad Abumarar.

This project is open-source under the MIT License. You are free to modify and distribute it, provided that original copyright notices and this permission notice are included in all copies or substantial portions of the Software.

For inquiries, support, or to view more of my work, please visit my portfolio:

**[abumarar.github.io/portfolio/](https://abumarar.github.io/portfolio/)**
