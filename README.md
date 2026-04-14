# ScreenTranslator

A powerful real-time screen translation tool written in Python. Originally designed with visual novels like *Danganronpa* in mind, this application allows you to select any region on your screen and automatically translates the text contained within that region from English to Vietnamese.

## 🌟 Features

* **Region Selection:** Manually draw a bounding box around the dialogue or text you want to track on your screen.
* **Auto Translate Loop:** The application automatically scans the selected region every 1.5 seconds. If new text appears, it uses OCR to read the text and translates it instantly without any manual input!
* **Smart Memory:** It remembers the last translated sentence to prevent redundant translations and save bandwidth.
* **Transparent Overlay:** Translated Vietnamese text is displayed dynamically in a sleek, non-intrusive transparent overlay window at the bottom of the screen.
* **Manual Trigger:** Press `F9` at any time to force a re-translation of the current screen region.

## 🚀 Installation & Requirements

Ensure you have **Python 3.8+** installed.

1. **Clone the repository:**
   ```bash
   git clone https://github.com/tridpt/ScreenTranslator.git
   cd ScreenTranslator
   ```

2. **Run the Script:**
   You can run the script via command line:
   ```bash
   python main.py
   ```
   *Or simply double-click the `run.bat` file if you are on Windows.*

## 🎮 How to Use

1. Start the application. The screen will slightly dim.
2. Click and drag your mouse to create a rectangular selection box over the text area (e.g., the game's dialogue box).
3. The translation overlay will appear at the bottom.
4. Play your game! The script runs silently in the background and will auto-translate text whenever it detects an update in the selected region.
5. Press `F9` if you need to manually force a translation.
6. Hold `Esc` to safely exit the application.

## 👨‍💻 Developer Notes

Developed by **Trần Đức Trí**.
Leverages Python `ctypes` for DPI awareness, `keyboard` for global hotkeys, and multi-threading to ensure the game performance is unaffected during OCR scanning.
