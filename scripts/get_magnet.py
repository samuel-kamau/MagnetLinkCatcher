import requests
import os
import PySimpleGUI as sg
import urllib.parse
from bs4 import BeautifulSoup

class GetMagnet:
    def get_download_pages(self, movie_title):
        google_url = f"https://www.google.com/search?q={urllib.parse.quote_plus(movie_title)}+download+torrent"
        request = requests.get(google_url)
        result = BeautifulSoup(request.content, "lxml")

        download_pages_links = []
        
        for i in result.find_all("a"):
            if (i.attrs["href"].startswith("/url?q=")) and ("accounts.google.com" not in i.attrs["href"]):
                download_pages_links.append(i.attrs["href"][7:-88])

        return download_pages_links

    def get_download_links(self, download_pages_links):
        all_magnet_links = []
        magnet_links = {}

        for link in download_pages_links:
            sg.Print(f"Searching in: {link}\n", font=("Segoe UI", 10), no_button=True)
            # print(f"Searching in: {link}\n")
            request = requests.get(link)
            result = BeautifulSoup(request.content, "lxml")

            for i in result.find_all("a"):
                if "href" in i.attrs:
                    if "magnet:?xt=" in i.attrs["href"]:
                        all_magnet_links.append(i.attrs["href"])

        for magnet_link in all_magnet_links:
            if magnet_link not in magnet_links:
                magnet_links[self.get_torrent_name(magnet_link)] = magnet_link

        sg.PrintClose()
        return magnet_links

    def get_torrent_name(self, magnet_link):
        name = magnet_link.split("tr=")[0][64:-1]
        if name.startswith(";dn=") and name.endswith("&amp"):
            name = name[4:-4]

        return urllib.parse.unquote_plus(name)

    def magnets_to_file(self, magnet_links, filename):
        with open(f"{filename}.txt", "w", encoding="utf-8") as file:
            for name, magnet_link in magnet_links.items():
                file.write(f"{name}\n{magnet_link}\n\n")

# process = GetMagnet()
# pages = process.get_download_pages("Movie here")
# links = process.get_download_links(pages)
# for k, v in links.items():
#     print(f"\n{k}\n\n{v}\n\n")