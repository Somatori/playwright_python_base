from pages.upload_and_download_page import UploadAndDownloadPage
from helpers.file_helper import get_test_data_path
import re


def test_download(page):
    upload_and_download = UploadAndDownloadPage(page)
    upload_and_download.goto()

    download = upload_and_download.download_file()
    assert download.suggested_filename == "sampleFile.jpeg"
    

def test_upload(page):
    file_path = get_test_data_path("uploads", "sample.txt")
    filename_regex = re.compile(r'sample\.txt$') # ends with 'sample.txt'

    upload_and_download = UploadAndDownloadPage(page)
    upload_and_download.goto()

    upload_and_download.select_input_file_for_upload(file_path)
    assert upload_and_download.file_input_contains_filename(filename_regex)