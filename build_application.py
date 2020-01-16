import os
from cx_Freeze import setup, Executable

target = Executable (
    script = "Magnet Link Catcher.py",
    base = "Win32GUI",
    icon = "icon.ico"
    )

setup (
    name = "Magnet Link Catcher",
    version = "1.0",
    description = "Get magnet links from internet without any effort!",
    author = "Pedro Lemos",
    options = {
                "build_exe": {
                        "packages": ["os", "tkinter", "PySimpleGUI", "pyperclip", "requests", "urllib.parse", "bs4"],
                        "include_files": ["icon.ico", "icon.png"]
                    }
            },
    
    executables = [target]
    )