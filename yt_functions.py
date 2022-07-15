import os
import re  # regex
from time import sleep

import youtube_dl
from pyfiglet import Figlet



def savePath() -> str:
    # Returning the path to save the video
    return os.path.expanduser("~") + '/Library/Containers/whbalzac.Dongtaizhuomian/Data/Documents/Videos'





def video(url: str = None):
    """
    Download the video from the given url
    
    :param url: the url of the video you want to download
    :type url: str
    """
    # check if the url is valid
    if check_url(url) is None:
        print("Invalid URL")
        return

    # get the path to save the video
    save_path = savePath()
    if save_path is None:
        return

    # download the video
    download_video(url, save_path)
    print("Video downloaded successfully")




def playlist(url: str = None):
    """
    Download playlist from youtube using youtube-dl
    
    :param url: the url of the playlist
    :type url: str
    """  
    # check if the url is valid
    if check_url(url) is None:
        print("Invalid URL")
        return
    
    # get the path to save the video
    save_path = savePath()
    if save_path is None:
        return

    # download playlist from youtube using youtube-dl
    download_playlist(url, save_path)
    print("Playlist downloaded successfully")




























def show_splash():
    """
    Display splash screen
    """
    clear_screen()
    title = "Y0utube Wallpaper"
    f = Figlet(font="standard")
    print(red(f.renderText(title)))


def clear_screen():
    """
    It prints 25 new lines
    """
    print("\n" * 25)


def check_url(url: str):
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
    elif match is None:
        return None


def green(text: str) -> str:
    """
    `green` takes a string and returns a string
    
    :param text: the text to be colored
    :type text: str
    :return: The text in green.
    """
    return "\033[32m" + text + "\033[0m"


def red(text: str) -> str:
    """
    `red` takes a string and returns a string
    
    :param text: The text to be colored
    :type text: str
    :return: The text is being returned with the color red.
    """
    return "\033[31m" + text + "\033[0m"


def blue(text: str) -> str:
    """
    `blue` takes a string and returns a string
    
    :param text: The text to be colored
    :type text: str
    :return: The text is being returned with the color blue.
    """
    return "\033[34m" + text + "\033[0m"


def download_video(url: str, save_path: str):
    """
    Download the video from the given url and save it to the given path
    
    :param url: the url of the video you want to download
    :type url: str
    :param save_path: The path where you want to save the video
    :type save_path: str
    """
    ydl_opts = {
        # hight quality video
        "format": "bestvideo[ext=mp4]+bestaudio[ext=m4a]/bestvideo+bestaudio",
        # save location of the video
        "outtmpl": save_path + "/%(title)s.%(ext)s",
    }
    youtube_dl.YoutubeDL(ydl_opts).extract_info(url)


def download_playlist(url: str, save_path: str):
    """
    Download playlist from youtube using youtube-dl
    
    :param url: the url of the playlist
    :type url: str
    :param save_path: The path where you want to save the downloaded videos
    :type save_path: str
    """
    # download playlist from youtube using youtube-dl
    ydl_opts = {
        # hight quality video
        "format": "bestvideo[ext=mp4]+bestaudio[ext=m4a]/bestvideo+bestaudio",
        # save location of the video
        "outtmpl": save_path + "/%(title)s.%(ext)s",
        "yes-playlist": True,
    }
    youtube_dl.YoutubeDL(ydl_opts).extract_info(url)
