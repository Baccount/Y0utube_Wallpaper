import argparse as ap
import os

from functions import (
    clear_screen,
    create_temp_folder,
    delete_temp_folder,
    download_video,
    keyboard_interrupt,
)
from tools import show_splash

# Youtube Offline Downloader


def main():
    if not checkWallpaper():
        # Wallpaper engine is not installed
        exit(1)
    delete_temp_folder()
    create_temp_folder()
    # catch arguments from user
    argument()
    while True:
        # if no arguments are passed, show the splash screen
        clear_screen()
        show_splash()
        print("1. Download video")
        print("2. Download Playlist")
        print("3. Exit")

        choice = input("Enter your choice: ")
        if choice == "1":
            url = input("Enter the URL of the video: ")
            download_video(url)
        elif choice == "2":
            url = input("Enter the URL of the playlist: ")
            download_video(url, playlist=True)
        elif choice == "3":
            print("Exiting...")
            exit(0)


def argument():
    """Parsing the arguments passed by the user.
    optional arguments:
    -h, --help            show this help message and exit
    -u URL, --url URL     URL of the video or playlist to download
    -pl PLAYLIST, --playlist PLAYLIST URL of the playlist to download
    """
    parser = ap.ArgumentParser(description="Youtube Offline Downloader")
    parser.add_argument(
        "-v", "--video", help="Video of the video to download", required=False
    )
    # playlist argument
    parser.add_argument(
        "-pl", "--playlist", help="URL of the playlist to download", required=False
    )

    # pass terminal=True if program will quit after downloading
    if parser.parse_args().video:
        download_video(parser.parse_args().video, terminal=True)

    # if the playlist arg is provided, then download the playlist
    if parser.parse_args().playlist:
        # pass terminal=True if program will quit after downloading
        download_video(parser.parse_args().playlist, terminal=True, playlist=True)


def checkWallpaper() -> bool:
    """
    Check if the wallpaper engine is installed.
    If not, install it.
    return: True if wallpaper engine is installed, False if not.
    """
    usr = os.path.expanduser("~") + "/Library/Containers/whbalzac.Dongtaizhuomian"

    if not os.path.exists(usr):
        print("Please install Dynamic Wallpaper")
        print(
            "https://apps.apple.com/us/app/dynamic-wallpaper-engine/id1453504509?mt=12"
        )
        input("Press Enter to exit...")
        return False
    return True


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        keyboard_interrupt()
