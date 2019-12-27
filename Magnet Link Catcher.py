try:
    import PySimpleGUI as sg
except:
    print("Your system doesn't have python3-tk package installed.\nPlease install it using your package manager.\nAPT: sudo apt install python3-tk")
import os
import pyperclip
from scripts.get_magnet import GetMagnet
from gui.design import *


window = sg.Window("Magnet Link Catcher", main_layout, size=(430, 280))

process = GetMagnet()

while True:
    event, values = window.read()

    if event in (None, "Exit"):
        window.close()
        break

    if event == "Search":
        download_pages = process.get_download_pages(values[0])
        dict_download_links = process.get_download_links(download_pages)

        [download_links.append(i) for i in dict_download_links.keys()]

        results_window = sg.Window("Sucess!", results_layout)

        while True:
            results_event, results_values = results_window.read()

            if results_event in (None, "Close"):
                results_window.close()
                break

            if results_event == "Save all links to file":
                process.magnets_to_file(dict_download_links, values[0])

                save_window = sg.Window("Sucess!", save_layout)

                while True:
                    save_event, save_result = save_window.read()

                    if save_event in (None, "Close"):
                        save_window.close()
                        break

                    if save_event == "Open file":
                        os.startfile(f"{values[0]}.txt")

            if results_event == "Open magnet link":
                os.startfile(dict_download_links[results_values[0][0]])

            if results_event == "Copy magnet link":
                pyperclip.copy(dict_download_links[results_values[0][0]])

                clipboard_window = sg.Window("Sucess!", clipboard_layout, auto_close=True)

                clipboard_event, clipboard_result = clipboard_window.read()
