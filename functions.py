import os
import re  # regex
from random import randint
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


def move_video():
    """
    Move the video from the temporary folder to the final folder
    """
    # move the video from the temporary folder to the given path
    try:
        for file in os.listdir(temp_path):
            os.rename(temp_path + "/" + file, final_path + "/" + file)
        print(green("Video installed successfully"))
    except Exception as e:
        print(red("Error: " + str(e)))
        print(red("Video not installed"))


def delete_temp_folder():
    """
    Delete the temporary folder "Forcefully"
    """
    if os.path.exists(temp_path):
        os.system("rm -rf " + temp_path)


def get_random_number():
    return str(randint(0, 100000))


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
    save_path = final_path
    if save_path is None:
        return

    # download the video
    download_video(url)
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
    save_path = final_path
    if save_path is None:
        return

    # download playlist from youtube using youtube-dl
    download_playlist(url)
    print("Playlist downloaded successfully")


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


def download_video(url: str):
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
        # name of the video is the title
        "outtmpl": temp_path + "/" + '%(title)s',
    }
    try:
        youtube_dl.YoutubeDL(ydl_opts).extract_info(url)
        print(green("Video downloaded successfully"))
        move_video()
        sleep(1)
    except Exception as e:
        print(red("Error: " + str(e)))
        print(red("Video not downloaded"))
        delete_temp_folder()


def download_playlist(url: str):
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
        "outtmpl": temp_path + "/" + '%(title)s',
        "yes-playlist": True,
    }
    try:
        youtube_dl.YoutubeDL(ydl_opts).extract_info(url)
        print(green("Playlist downloaded successfully"))
        move_video()
        sleep(1)
    except Exception as e:
        print(red("Error: " + str(e)))
        print(red("Playlist not downloaded"))
        delete_temp_folder()
