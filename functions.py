import os
import re  # regex
from time import sleep

import youtube_dl
from pyfiglet import Figlet

temp_path = os.path.expanduser("~") + "/Library/Caches/Y0utube"
final_path = (
    os.path.expanduser("~")
    + "/Library/Containers/whbalzac.Dongtaizhuomian/Data/Documents/Videos"
)


def create_temp_folder():
    """
    Create a  temporary folder at the given path to save the videos
    """
    if not os.path.exists(temp_path):
        os.makedirs(temp_path)


def move_video() -> bool:
    """
    Move the video from the temporary folder to the final folder
    """
    # move the video from the temporary folder to the given path
    try:
        for file in os.listdir(temp_path):
            os.rename(temp_path + "/" + file, final_path + "/" + file)
        print(green("Video installed successfully"))
        # for testing purposes
        return True
    except Exception as e:
        # for testing purposes
        return False
        print(red("Error: " + str(e)))
        print(red("Video not installed"))


def delete_temp_folder():
    """
    Delete the temporary folder "Forcefully"
    """
    if os.path.exists(temp_path):
        os.system("rm -rf " + temp_path)


def show_splash():
    """
    Display splash screen
    """
    clear_screen()
    title = "Y0Utube \n Wallpaper"
    f = Figlet(font="standard")
    print(red(f.renderText(title)))


def clear_screen():
    """
    It prints 25 new lines
    """
    print("\n" * 25)


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
    elif match is None:
        # for testing purposes
        return False


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


def download_video(url: str, terminal: bool = False, playlist: bool = False) -> bool:
    """
    Download playlist from youtube using youtube-dl

    :param url: the url of the playlist
    :type url: str
    :param terminal: If the user is using the command lines Do Not show UI, just quit
    :type terminal: bool
    :param playlist: If the user is downloading a playlist = True
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
        "outtmpl": temp_path + "/" + "%(title)s",
        "yes-playlist": True if playlist else False,
    }
    try:
        youtube_dl.YoutubeDL(ydl_opts).extract_info(url)
        print(green("Playlist downloaded successfully"))
        move_video()
        sleep(1)
        if terminal is True:
            exit(0)
        # for testing purposes
        return True
    except Exception as e:
        print(red("Error: " + str(e)))
        print(red("Playlist not downloaded"))
        delete_temp_folder()
        if terminal is True:
            exit(0)
        # for testing purposes
        return False
