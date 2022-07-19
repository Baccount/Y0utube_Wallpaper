from functions import create_temp_folder, delete_temp_folder, download_video
import os

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
    assert os.path.exists(temp_path)
    delete_temp_folder()


def test_delete_temp_folder():
    """
    Test the delete_temp_folder function
    """
    create_temp_folder()
    delete_temp_folder()
    assert not os.path.exists(temp_path)
    delete_temp_folder()

def test_download_video():
    """
    Test the download_video function
    """
    delete_temp_folder()
    create_temp_folder()
    assert download_video("https://www.youtube.com/watch?v=Wch3gJG2GJ4")
    delete_temp_folder()