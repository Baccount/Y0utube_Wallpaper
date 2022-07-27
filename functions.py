"""Created by: Baccount"""
import os
import re  # regex
from time import sleep

import youtube_dl
from pyfiglet import Figlet

from tools import blue, clear_screen, green, red

TEMP_PATH = os.path.expanduser("~") + "/Library/Caches/Y0utube"
FINAL_PATH = (
    os.path.expanduser("~")
    + "/Library/Containers/whbalzac.Dongtaizhuomian/Data/Documents/Videos"
)


def create_temp_folder():
    """
    Create a  temporary folder at the given path to save the videos
    """
    if not os.path.exists(TEMP_PATH):
        os.makedirs(TEMP_PATH)


def move_video() -> bool:
    """
    Move the video from the temporary folder to the final folder
    """
    try:
        for file in os.listdir(TEMP_PATH):
            os.rename(TEMP_PATH + "/" + file, FINAL_PATH + "/" + file)
        print(green("Video installed successfully"))
        # for testing purposes
        return True
    except Exception as e:
        print(red("Error: Video not installed\n" + str(e)))
        # for testing purposes
        return False


def delete_temp_folder():
    """
    Delete the temporary folder "Forcefully"
    """
    if os.path.exists(TEMP_PATH):
        os.system("rm -rf " + TEMP_PATH)


def show_splash():
    """
    Display splash screen
    """
    clear_screen()
    title = "Y0Utube \n Wallpaper"
    f = Figlet(font="standard")
    print(red(f.renderText(title)))


def check_url(url: str) -> bool:
    """
    It takes a string as an argument, checks if it's a valid youtube url, and returns the url if it is,
    or None if it isn't

    :param url: The URL of the video to be downloaded
    :type url: str
    :return: The match object or None
    """
    regex = r"^(https?\:\/\/)?(www\.youtube\.com|youtu\.be)\/.+$"

    match = re.match(regex, url)
    if match:
        return match.group()
    else:
        # for testing purposes
        return False


def download_video(url: str, terminal: bool = False, playlist: bool = False) -> bool:
    """
    Download playlist from youtube using youtube-dl

    :param url: the url of the playlist
    :type url: str
    :param terminal: If the user is using the command lines Do Not show UI, just quit
    :type terminal: bool
    :param playlist: If the user is downloading a playlist
    :type playlist: bool
    """
    if not check_url(url):
        print("Invalid URL")
        # for testing purposes
        return False
    # download playlist from youtube using youtube-dl
    ydl_opts = {
        # hight quality video
        "format": "bestvideo[ext=mp4]+bestaudio[ext=m4a]/bestvideo+bestaudio",
        # save location of the video
        "outtmpl": TEMP_PATH + "/" + "%(title)s",
        "yes-playlist": True if playlist else False,
    }
    try:
        print(blue("Press Ctrl+C to cancel"))
        youtube_dl.YoutubeDL(ydl_opts).extract_info(url)
        print(green("Playlist downloaded successfully"))
        move_video()
        sleep(1)
        # for testing purposes
        return True
    except Exception as e:
        print(red("Error: Playlist not downloaded\n" + str(e)))
        delete_temp_folder()
        if terminal is True:
            exit(0)
        # for testing purposes
        return False
    # close program if the user is using the command line
    if terminal is True:
        exit(0)


def keyboard_interrupt():
    """
    Catch keyboard interrupt control + c
    """
    clear_screen()
    print(red("Clearing temporary files"))
    delete_temp_folder()
    exit(0)
