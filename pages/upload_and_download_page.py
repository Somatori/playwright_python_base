from playwright.sync_api import Page, expect
from configs.config import BASE_URL


class UploadAndDownloadPage:
    def __init__(self, page: Page):
        self.page = page

    ### ========== LOCATORS ==========
    def _download_button(self):
        return self.page.get_by_role('link', name='Download')

    ### ========== ACTIONS =============
    def goto(self):
        self.page.goto(f"{BASE_URL}/upload-download")

    def download_file(self):
        # Start waiting for the download
        with self.page.expect_download() as download_info:
            # Perform the action that initiates download
            self._download_button().click()
        return download_info.value


    ### ========== ASSERTIONS =============
