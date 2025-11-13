from playwright.sync_api import Page, expect
from configs.config import BASE_URL


class TemplatePage:
    def __init__(self, page: Page):
        self.page = page

    ### ========== LOCATORS ==========
    # def _(self):
        # return self.page.

    ### ========== ACTIONS =============
    def goto(self):
        self.page.goto(f"{BASE_URL}/template")


    ### ========== ASSERTIONS =============
