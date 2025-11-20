from pages.upload_and_download_page import UploadAndDownloadPage


def test_download(page):
    upload_and_download = UploadAndDownloadPage(page)
    upload_and_download.goto()

    download = upload_and_download.download_file()
    assert download.suggested_filename == "sampleFile.jpeg"
    

