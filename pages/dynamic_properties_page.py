from playwright.sync_api import Page, expect
from configs.config import BASE_URL


class DynamicPropertiesPage:
    def __init__(self, page: Page):
        self.page = page

    ### ========== LOCATORS ==========
    def _visible_after_5_seconds_btn(self):
        return self.page.locator("button#visibleAfter")

    ### ========== ACTIONS =============
    def goto(self):
        self.page.goto(f"{BASE_URL}/dynamic-properties")

    def wait_for_visible_after_5_seconds_btn(self):
        self.page.wait_for_timeout(5000)
        expect(self._visible_after_5_seconds_btn()).to_be_visible()

    ### ========== ASSERTIONS =============
    def is_visible_after_5_seconds_btn_clickable(self) -> bool:
        self._visible_after_5_seconds_btn().click()
        return True