@echo off
echo Building Windows Executable with PyInstaller...
pip install pyinstaller
pyinstaller --noconfirm --onedir --windowed --name "Zenith Auto Clicker" ^
    --icon "build_scripts\icon.ico" ^
    --add-data "gui\style.qss;gui" ^
    "zenith.py"

echo Executable generated in 'dist\' directory.
echo Starting Inno Setup to create the Installer...
"C:\Program Files (x86)\Inno Setup 6\ISCC.exe" "build_scripts\zenith_windows.iss"
echo Done! Check the output folder for the Setup file.
pause
