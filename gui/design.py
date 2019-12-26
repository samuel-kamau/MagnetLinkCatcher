import PySimpleGUI as sg


# Magnet Links Catcher theme

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

#   Main screen layout

main_layout = [
    [sg.Text("\n", font=("Segoe UI Light", 5))],
    [sg.Text("  Magnet Link Catcher", font=("Segoe UI Light", 24), text_color="#5d2b90", justification="left")],
    [sg.Text("    Search for something", font=("Segoe UI Light", 14))],
    [sg.Text("\n", font=("Segoe UI Light", 1))],
    [sg.Text("  "), sg.InputText(size=(28, 6), font=("Segoe UI Light", 12)), sg.VerticalSeparator(pad=(4, (3, 4))),
        sg.Submit("Search", size=(12, 0), font=("Segoe UI Light", 10, "bold"))],
    [sg.Text("  "), sg.Button("Support this project", size=(17, 0), font=("Segoe UI Light", 10, "bold")), 
        sg.VerticalSeparator(pad=(6, 3)), sg.Button("About", size=(7, 0), font=("Segoe UI Light", 10, "bold")),
        sg.VerticalSeparator(pad=(6, 3)), sg.Button("Exit", size=(12, 0), font=("Segoe UI Light", 10, "bold"))],
    [sg.Text("\nDeveloped by Pedro Lemos (@pedrolemoz)", font=("Segoe UI Light", 12), size=(42, 0), justification="center")]
]


#   Window which results are shown

download_links = []

results_layout = [
    [sg.Text("\n", font=("Segoe UI Light", 5))],
    [sg.Text("Process finished sucessfully!", font=("Segoe UI Light", 14), size=(30, 0), justification="left")],
    [sg.Text("\n", font=("Segoe UI Light", 1))],
    [sg.Listbox(values=download_links, size=(90, 15), font=("Segoe UI", 10), enable_events=True)],
    [sg.Text("\n", font=("Segoe UI Light", 1))],
    [sg.Text(" " * 16), sg.Button("Save all links to file", size=(22, 0), font=("Segoe UI Light", 10, "bold")),
        sg.Button("Open magnet link", size=(16, 0), font=("Segoe UI Light", 10, "bold")),
        sg.Button("Copy magnet link", size=(16, 0), font=("Segoe UI Light", 10, "bold")),
        sg.Button("Close", size=(12, 0), font=("Segoe UI Light", 10, "bold"))],
    [sg.Text("\n", font=("Segoe UI Light", 1))]
]


#   Save to file oopup

save_layout = [
    [sg.Text("\n", font=("Segoe UI Light", 5))],
    [sg.Text(f"Magnet links saved sucessfully!", size=(25, 0), font=("Segoe UI Light", 14), justification="left")],
    [sg.Text("\n", font=("Segoe UI Light", 1))],
    [sg.Text(" " * 6), sg.Button("Open file", size=(12, 0), font=("Segoe UI Light", 10, "bold")),
        sg.Button("Close", size=(12, 0), font=("Segoe UI Light", 10, "bold"))],
    [sg.Text("\n", font=("Segoe UI Light", 1))]
]


#   Clipboard popup

clipboard_layout = [
    [sg.Text("\n", font=("Segoe UI Light", 5))],
    [sg.Text("Copied to clipboard!", font=(
        "Segoe UI Light", 14), size=(17, 0), justification="left")],
    [sg.Text("\n", font=("Segoe UI Light", 1))]
]
