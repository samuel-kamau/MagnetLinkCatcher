import requests
import os
import PySimpleGUI as sg
import urllib.parse
from pathlib import Path
from bs4 import BeautifulSoup, SoupStrainer

class GetMagnet:
	def __init__(self):
		self.links = {}
	
	def get_magnet(self, search_content, google = True, tpb = False, l337x = False, nyaa = False, eztv = False, yts = False, ettv = False, rutracker = False):
		search_content = urllib.parse.quote_plus(f"{search_content}")
		
		if google:
			pages = self.get_download_pages_from_google(search_content)
			link = self.get_download_links(pages)
			self.links.update(link)
		
		if tpb:
			pages = []
			
			for i in range(5):
				pages.append(f"https://tpb.party/search/{search_content}/{i + 1}/7/0")
			
			link = self.get_download_links(pages)
			self.links.update(link)
		
		if l337x:
			pages = self.get_download_pages_from_l337x(search_content)			
			link = self.get_download_links(pages)
			self.links.update(link)
		
		if nyaa:
			pages = []
			
			for i in range(5):
				pages.append(f"https://nyaa.si/?q={search_content}&f=0&c=0_0&s=seeders&o=desc&p={i + 1}")
			
			link = self.get_download_links(pages)
			self.links.update(link)
		
		if eztv:
			pages = [f"https://eztv.io/search/{search_content}"]
			
			link = self.get_download_links(pages)
			self.links.update(link)
		
		if yts:
			pages = self.get_download_pages_from_yts(search_content)
			link = self.get_download_links(pages)
			self.links.update(link)

		if ettv:
			pages = self.get_download_pages_from_ettv(search_content)
			link = self.get_download_links(pages)
			self.links.update(link)
		
		return self.links
	
	def get_download_pages_from_google(self, search_content):
		google_url = f"https://www.google.com/search?q={search_content}+download+torrent"

		request = requests.get(google_url)
		result = BeautifulSoup(request.content, "lxml", parse_only=SoupStrainer("a"))
		
		download_pages_links = []
		
		for i in result.find_all("a", href = True):
			if (i.get("href").startswith("/url?q=")) and ("accounts.google.com" not in i.get("href")) and (".org" not in i.get("href")) and ("youtube.com" not in i.get("href")) and ("facebook.com" not in i.get("href")):
				download_pages_links.append(i.get("href")[7:-88])

		for i in download_pages_links:
			print(i)
		
		return download_pages_links

	def get_download_pages_from_l337x(self, search_content):
		l337x_url = f"https://www.1377x.to/search/{search_content}/1/"
		request = requests.get(l337x_url)
		result = BeautifulSoup(request.content, "lxml", parse_only=SoupStrainer("a"))
		
		download_pages_links = []
		
		for i in result.find_all("a", href = True):
			if i.get("href").startswith("/torrent") and i.get("href") not in download_pages_links:
				download_pages_links.append(f'https://www.1377x.to{i.get("href")}')
		
		return download_pages_links

	def get_download_pages_from_ettv(self, search_content):
		ettv_url = f"https://www.ettv.to/torrents-search.php?search={search_content}"
		request = requests.get(ettv_url)
		result = BeautifulSoup(request.content, "lxml", parse_only=SoupStrainer("a"))
		
		download_pages_links = []
		
		for i in result.find_all("a", href = True):
			if i.get("href").startswith("/torrent/") and i.get("href") not in download_pages_links:
				download_pages_links.append(f'https://www.ettv.to{i.get("href")}')
		
		return download_pages_links

	
	def get_download_pages_from_l337x(self, search_content):
		l337x_url = f"https://www.1377x.to/search/{search_content}/1/"
		request = requests.get(l337x_url)
		result = BeautifulSoup(request.content, "lxml", parse_only=SoupStrainer("a"))
		
		download_pages_links = []
		
		for i in result.find_all("a", href = True):
			if i.get("href").startswith("/torrent") and i.get("href") not in download_pages_links:
				download_pages_links.append(f'https://www.1377x.to{i.get("href")}')
		
		return download_pages_links
	
	def get_download_pages_from_yts(self, search_content):
		yts_url = f"https://yts.lt/browse-movies/{search_content}/all/all/0/latest"
		request = requests.get(yts_url)
		result = BeautifulSoup(request.content, "lxml", parse_only=SoupStrainer("a"))
		
		download_pages_links = []
		
		for i in result.find_all("a", href = True):
			if i.get("href").startswith("https://yts.lt/movie/") and i.get("href") not in download_pages_links:
				download_pages_links.append(i.get("href"))
		
		return download_pages_links
	
	def get_download_links(self, download_pages_links):
		all_magnet_links = []
		magnet_links = {}
		
		for link in download_pages_links:
			sg.Print(f"Searching in: {link}\n", font=("Segoe UI", 10), no_button=True)
			print(f"Searching in: {link}\n")
			request = requests.get(link)
			result = BeautifulSoup(request.content, "lxml", parse_only=SoupStrainer("a"))
			
			for i in result.find_all("a", href = True):
				if i.get("href").startswith("magnet:?xt="):
					all_magnet_links.append(i.get("href"))
		
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
		if os.path.exists(os.path.join(Path.home(), "Downloads", "MagnetLinkCatcher")) == False:
			os.mkdir(os.path.join(Path.home(), "Downloads", "MagnetLinkCatcher"))
		
		path_to_file = os.path.join(Path.home(), "Downloads", "MagnetLinkCatcher")
		
		with open(os.path.join(path_to_file, f"{filename}.txt"), "w", encoding="utf-8") as file:
			for name, magnet_link in magnet_links.items():
				file.write(f"{name}\n{magnet_link}\n\n")

		return path_to_file

# k = GetMagnet()
# g = k.get_magnet("mr robot", google = False)
# print(g)