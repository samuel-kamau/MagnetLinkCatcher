import PySimpleGUI as sg
import os
import pyperclip
from scripts.get_magnet import GetMagnet

sg.LOOK_AND_FEEL_TABLE["MagnetLinkCatcher"] = {
    'BACKGROUND': "white",
    'TEXT': "#323232",
    'INPUT': "#dfe2e8",
    'TEXT_INPUT': '#000000',
    'SCROLL': '#c7e78b',
    'BUTTON': ("white", "#5d2b90"),
    'PROGRESS': ("white", "black"),
    'BORDER': 0, 'SLIDER_DEPTH': 0, 'PROGRESS_DEPTH': 0,
}

sg.change_look_and_feel("MagnetLinkCatcher")

main_layout = [
    [sg.Text("\n", font=("Segoe UI Light", 5))],
    [sg.Text("  Magnet Link Catcher", font=("Segoe UI Light", 24), text_color="#5d2b90", justification="left")],
    [sg.Text("    Search for something", font=("Segoe UI Light", 14))],
    [sg.Text("\n", font=("Segoe UI Light", 1))],
    [sg.Text("  "), sg.InputText(size=(28, 6), font=("Segoe UI Light", 12)), sg.VerticalSeparator(pad=(4, (3, 4))), sg.Submit("Search", size=(12, 0), font=("Segoe UI Light", 10, "bold"))],
    [sg.Text("\n", font=("Segoe UI Light", 1))],
    [sg.Text("    Choose your search source for content", font=("Segoe UI Light", 14))],
    [sg.Text("\n", font=("Segoe UI Light", 1))],
    [sg.Text("  "), sg.Checkbox("Google", font=("Segoe UI Light", 12), size=(11, 1), default=True), sg.Checkbox("The Pirate Bay", font=("Segoe UI Light", 12), size=(16, 1)), sg.Checkbox("1337x", font=("Segoe UI Light", 12))],
    [sg.Text("  "), sg.Checkbox("Nyaa", font=("Segoe UI Light", 12), size=(11, 1)), sg.Checkbox("EZTV", font=("Segoe UI Light", 12), size=(16, 1)), sg.Checkbox("YTS", font=("Segoe UI Light", 12))],
    [sg.Text("\n", font=("Segoe UI Light", 1))],
    [sg.Text("  "), sg.Button("Support this project", size=(17, 0), font=("Segoe UI Light", 10, "bold")), sg.VerticalSeparator(pad=(6, 3)), sg.Button("About", size=(7, 0), font=("Segoe UI Light", 10, "bold")), sg.VerticalSeparator(pad=(6, 3)), sg.Button("Exit", size=(12, 0), font=("Segoe UI Light", 10, "bold"))],
    [sg.Text("\nDeveloped by Pedro Lemos (@pedrolemoz)", font=("Segoe UI Light", 12), size=(42, 0), justification="center")]
]

window = sg.Window("Magnet Link Catcher", main_layout, size=(430, 410))

process = GetMagnet()

while True:
    event, values = window.read()
    print(event, values)

    if event in (None, "Exit"):
        window.close()
        break

    if event == "About":

        about_layout = [
            [sg.Text("\n", font=("Segoe UI Light", 1))],
            [sg.Text("This project was born with an idea for automatize torrent downloading.\nI don't wanna search for torrent and see boring adverts. This program search on many sources and return all found magnet links and is able to start the default torrent application, copy links and save its to file.", font = ("Segoe UI", 12), size = (56, 0), justification="left")],
            [sg.Text("\n", font=("Segoe UI Light", 1))],
            [sg.Text(" " * 101), sg.Button("Close", size=(12, 0), font = ("Segoe UI Light", 10, "bold"))],
            [sg.Text("\n", font = ("Segoe UI Light", 1))]
        ]

        about_window = sg.Window("About project", about_layout)

        while True:
            about_event, about_values = about_window.read()
            if about_event in (None, "Close"):
                about_window.close()
                break

    if event == "Search":
        dict_download_links = process.get_magnet(values[0], google = values[1], tpb = values[2], l337x = values[3], nyaa = values[4], eztv = values[5], yts = values[6])

        download_links = []

        [download_links.append(i) for i in dict_download_links.keys()]

        results_layout = [
            [sg.Text("\n", font = ("Segoe UI Light", 5))],
            [sg.Text("Process finished sucessfully!", font = ("Segoe UI Light", 14), size = (30, 0), justification = "left")],
            [sg.Text("\n", font = ("Segoe UI Light", 1))],
            [sg.Listbox(values = download_links, size = (90, 15), font=("Segoe UI", 10), enable_events=True)],
            [sg.Text("\n", font=("Segoe UI Light", 1))],
            [sg.Text(" " * 16), sg.Button("Save all links to file", size=(22, 0), font=("Segoe UI Light", 10, "bold")), sg.Button("Open magnet link", size=(16, 0), font=("Segoe UI Light", 10, "bold")), sg.Button("Copy magnet link", size=(16, 0), font=("Segoe UI Light", 10, "bold")), sg.Button("Close", size=(12, 0), font=("Segoe UI Light", 10, "bold"))],
            [sg.Text("\n", font=("Segoe UI Light", 1))]
        ]

        results_window = sg.Window("Sucess!", results_layout)

        while True:
            results_event, results_values = results_window.read()

            if results_event in (None, "Close"):
                process.links = {}
                dict_download_links, download_links = {}, []
                results_window.close()
                break

            if results_event == "Save all links to file":
                process.magnets_to_file(dict_download_links, values[0])

                save_layout = [
                    [sg.Text("\n", font=("Segoe UI Light", 5))],
                    [sg.Text(f"Magnet links saved sucessfully!", size=(25, 0), font=("Segoe UI Light", 14), justification="left")],
                    [sg.Text("\n", font=("Segoe UI Light", 1))],
                    [sg.Text(" " * 6), sg.Button("Open file", size=(12, 0), font=("Segoe UI Light", 10, "bold")), sg.Button("Close", size=(12, 0), font=("Segoe UI Light", 10, "bold"))],
                    [sg.Text("\n", font=("Segoe UI Light", 1))]
                ]

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

                clipboard_layout = [
                    [sg.Text("\n", font=("Segoe UI Light", 5))],
                    [sg.Text("Copied to clipboard!", font=("Segoe UI Light", 14), size=(17, 0), justification="left")],
                    [sg.Text("\n", font=("Segoe UI Light", 1))]
                ]

                clipboard_window = sg.Window("Sucess!", clipboard_layout, auto_close=True)

                clipboard_event, clipboard_result = clipboard_window.read()
