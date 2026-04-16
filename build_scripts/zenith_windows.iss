[Setup]
AppName=Zenith Auto Clicker
AppVersion=1.0
DefaultDirName={autopf}\Zenith Auto Clicker
DefaultGroupName=Zenith Auto Clicker
UninstallDisplayIcon={app}\Zenith Auto Clicker.exe
Compression=lzma2
SolidCompression=yes
OutputDir=..\dist
OutputBaseFilename=Zenith_Setup
SetupIconFile=icon.ico

[Files]
Source: "..\dist\Zenith Auto Clicker\*"; DestDir: "{app}"; Flags: ignoreversion recursesubdirs createallsubdirs

[Icons]
Name: "{autoprograms}\Zenith Auto Clicker"; Filename: "{app}\Zenith Auto Clicker.exe"
Name: "{commondesktop}\Zenith Auto Clicker"; Filename: "{app}\Zenith Auto Clicker.exe"; Tasks: desktopicon

[Tasks]
Name: "desktopicon"; Description: "Create a &desktop shortcut"; GroupDescription: "Additional icons:"
