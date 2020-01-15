from cx_Freeze import setup, Executable
setup(
    name = "ML",
    version = "1.0.0",
    options = {"build_exe": {
        'packages': ["os","PySimpleGUI", "pyperclip", "requests", "urllib.parse", "bs4"],
        'include_msvcr': True,
    }},
    executables = [Executable("Magnet Link Catcher.py",base="Win32GUI")]
    )