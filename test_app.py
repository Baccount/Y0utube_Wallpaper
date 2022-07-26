import os

from functions import (
    check_url,
    create_temp_folder,
    delete_temp_folder,
    download_video,
    move_video,
)
from y0utube_wallpaper import checkWallpaper

temp_path = os.path.expanduser("~") + "/Library/Caches/Y0utube"
final_path = (
    os.path.expanduser("~")
    + "/Library/Containers/whbalzac.Dongtaizhuomian/Data/Documents/Videos"
)


def test_create_temp_folder():
    """
    Test the create_temp_folder function
    """
    delete_temp_folder()
    create_temp_folder()
    assert os.path.exists(temp_path) is True
    # clean up
    delete_temp_folder()


def test_delete_temp_folder():
    """
    Test the delete_temp_folder function
    """
    create_temp_folder()
    delete_temp_folder()
    assert not os.path.exists(temp_path)


def test_check_url():
    """
    Test the check_url function
    """
    assert check_url("https://www.youtube.com/watch?v=Wch3gJG2GJ4")
    assert check_url("https://wwwyoutube.com/watch?v=Wch3gJG2GJ4") is False


def test_download_video():
    """
    Test the download_video function
    """
    delete_temp_folder()
    create_temp_folder()
    assert download_video("https://www.youtube.com/watch?v=Wch3gJG2GJ4") is True
    # clean up
    delete_temp_folder()


def test_move_video():
    """
    Test the move_video function
    """
    delete_temp_folder()
    create_temp_folder()
    download_video("https://www.youtube.com/watch?v=Wch3gJG2GJ4")
    assert move_video() is True
    # clean up
    delete_temp_folder()


def test_checkWallpaper():
    """
    Test the checkWallpaper function
    """
    assert checkWallpaper() is True
