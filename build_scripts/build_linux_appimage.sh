#!/bin/bash
set -e

echo "Installing required packaging libraries and project dependencies..."
pip install pyinstaller Pillow
pip install -r requirements_linux.txt

echo "Generating generic app icons..."
python build_scripts/create_icon.py

echo "Building Linux Executable with PyInstaller..."
pyinstaller --noconfirm --onedir --windowed --name "zenith" \
    --icon "build_scripts/icon.png" \
    --add-data "gui/style.qss:gui" \
    "zenith.py"

echo "Downloading appimagetool..."
wget -q -nc -O appimagetool-x86_64.AppImage https://github.com/AppImage/AppImageKit/releases/download/continuous/appimagetool-x86_64.AppImage || true
chmod +x appimagetool-x86_64.AppImage

APPDIR="AppDir"
echo "Creating AppDir structure..."
rm -rf "$APPDIR" && mkdir -p "$APPDIR/usr/bin"
cp -r dist/zenith/* "$APPDIR/usr/bin/"

cp build_scripts/icon.png "$APPDIR/zenith.png"

cat <<'EOF' > "$APPDIR/zenith.desktop"
[Desktop Entry]
Name=Zenith Auto Clicker
Exec=zenith
Icon=zenith
Type=Application
Categories=Utility;
Terminal=false
EOF

cat <<'EOF' > "$APPDIR/AppRun"
#!/bin/sh
HERE="$(dirname "$(readlink -f "${0}")")"
export PATH="${HERE}/usr/bin:${PATH}"
export LD_LIBRARY_PATH="${HERE}/usr/bin:${LD_LIBRARY_PATH}"
exec "${HERE}/usr/bin/zenith" "$@"
EOF
chmod +x "$APPDIR/AppRun"

echo "Packaging AppImage..."
export APPIMAGE_EXTRACT_AND_RUN=1
./appimagetool-x86_64.AppImage "$APPDIR" "ZenithAutoClicker-x86_64.AppImage"

echo "Done! The AppImage has been created."
