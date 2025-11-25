from playwright.sync_api import Page, expect
from configs.config import BASE_URL


class UploadAndDownloadPage:
    def __init__(self, page: Page):
        self.page = page

    ### ========== LOCATORS ==========
    def _download_button(self):
        return self.page.get_by_role('link', name='Download')
    
    def _file_input(self):
        return self.page.get_by_label('Select a file')

    ### ========== ACTIONS =============
    def goto(self):
        self.page.goto(f"{BASE_URL}/upload-download")

    def download_file(self):
        # Start waiting for the download
        with self.page.expect_download() as download_info:
            # Perform the action that initiates download
            self._download_button().click()
        return download_info.value
    
    def select_input_file_for_upload(self, file_path):
        self._file_input().set_input_files(str(file_path))
        

    ### ========== ASSERTIONS =============

    def file_input_contains_filename(self, filename_regex):
        expect(self._file_input()).to_have_value(filename_regex)
        return True