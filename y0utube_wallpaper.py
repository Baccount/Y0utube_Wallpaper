import argparse as ap

from functions import (
    clear_screen,
    create_temp_folder,
    delete_temp_folder,
    playlist,
    show_splash,
    video,
)

# Youtube Offline Downloader


def main():
    # delete the temp folder if it exists
    delete_temp_folder()
    # creates a temporary folder to store the downloaded videos
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
            video(url)
        elif choice == "2":
            url = input("Enter the URL of the playlist: ")
            playlist(url)
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
        "-u", "--url", help="URL of the video to download", required=False
    )
    # playlist argument
    parser.add_argument(
        "-pl", "--playlist", help="URL of the playlist to download", required=False
    )

    # if the url arg is provided, then download the video
    if parser.parse_args().url:
        video(parser.parse_args().url)

    # if the playlist arg is provided, then download the playlist
    if parser.parse_args().playlist:
        playlist(parser.parse_args().playlist)


if __name__ == "__main__":
    main()
