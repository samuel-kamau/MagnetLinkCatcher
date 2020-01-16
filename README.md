<p align="center">
  <img src="https://i.imgur.com/ry6s1OO.png" alt="Logo"/>

## Get magnet links from internet without any effort! 🧲

## Getting started

### From a installer

Download the installer for Windows [here](https://sourceforge.net/projects/magnetlinkcatcher/files/latest/download).

### From source

In order to run this program from source, you'll need:

* Latest version of Python3
* Git (optional)
* Install dependencies

To install Python3, please visit [Python official website](https://www.python.org/downloads/), download and install the latest package available. If you are using GNU/Linux, you may already have Python3 installed in your system. Type ```python3 --version``` to check.

To install Git, please visit [Git official website](https://git-scm.com/downloads), download and install the latest package available. Setup Git with your name and email. Clone the repository to your machine using the following command:

```
git clone https://github.com/pedrolemoz/MagnetLinkCatcher.git
```

If you don't wanna install Git, just download the ```.zip``` from this repository (the green button above), and unzip it in your machine.

To install dependencies, type the following command in your command prompt or terminal (make sure to be in the project directory):

```
pip install -r requeriments.txt
```

### Building the application

If you forked this project and want to build your executable, there's a script to do it. I used ```cx_Freeze``` to build the program.

Install ```cx_Freeze``` using ```pip``` with the following command:

```
pip install cx-Freeze
```

To build the application:

```
python build_application.py build
```

It will create a folder called ```build``` with the executable inside.

> Note 1: I don't know why, but cx_Freeze doesn't work in Python 3.8. I'm currently using Python 3.7.6 to build this project.

> Note 2: If your executable fail to start, try rename the folder Tkinter in lib directory to tkinter.


### How to use

Type what content you wanna links for, in the search box, select one or more of sources and click in the search button.

By now, supported sources are:

* Google (Slow, but works fine for dubbed content)
* The Pirate Bay (Fast, and works for every content)
* 1337x (Fast, and works for every content)
* Nyaa (Fast, focused in anime RAW's)
* EZTV (Fast, focused in TV Shows)
* YTS (Fast, focused in lightweight movies)

After the search is finished, you can:

* Save all links to a text file
  > Links are saved to your Downloads folder by default
* Open the selected magnet link with your default torrent client
* Copy the magnet link to your clipboard

We plan to add new features, such:

* Save magnet links as a ```.torrent``` file
* Get info about seeders and leechers and use it to rate torrents
* Download torrents without a external client
