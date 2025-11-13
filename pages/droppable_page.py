from playwright.sync_api import Page, expect
from configs.config import BASE_URL


class DroppablePage:
    def __init__(self, page: Page):
        self.page = page

    ### ========== LOCATORS ==========
    def _droppable_area(self):
        return self.page.locator('div#droppableExample-tabpane-simple div#droppable')
    
    def _draggable_element(self):
        return self.page.locator('div#droppableExample-tabpane-simple div#draggable')
    

    ### ========== ACTIONS =============
    def goto(self):
        self.page.goto(f"{BASE_URL}/droppable")

    def get_droppable_area_text(self):
        return self._droppable_area().inner_text()
    
    def drag_element_to_droppable_area(self):
        self._draggable_element().drag_to(self._droppable_area())


    ### ========== ASSERTIONS =============
    def droppable_area_has_text(self, text):
        expect(self._droppable_area()).to_have_text(text)
        return True