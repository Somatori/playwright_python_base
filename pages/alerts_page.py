from playwright.sync_api import Page, expect, Dialog
from configs.config import BASE_URL


class AlertsPage:
    def __init__(self, page: Page):
        self.page = page

        # Attributes to store dialog info
        self.alert_message = None
        self.alert_type = None

    ### ========== LOCATORS ==========
    def _alert_button(self):
        return self.page.locator('#alertButton')

    ### ========== ACTIONS =============
    def goto(self):
        self.page.goto(f"{BASE_URL}/alerts", wait_until="domcontentloaded")

    def click_the_alert_button(self):
        # Define a function that handles the dialog and includes a pause
        def handle_dialog(dialog: Dialog):
            # # Add a pause to visually inspect the alert in degug-mode
            # self.page.wait_for_timeout(5000)

            # Store the values
            self.alert_message = dialog.message
            self.alert_type = dialog.type

            # Accept of dismiss the dialog
            dialog.accept() # Or dialog.dismiss()

        # Register the handler
        self.page.once("dialog", handle_dialog)
        
        # Trigger the alert
        self._alert_button().click()

    def get_alert_type(self):
        return self.alert_type

    def get_alert_message(self):
        # Optional check in case the dialog never appeared
        if self.alert_message is None:
             raise Exception("Alert message was never captured. The dialog might not have appeared.")
        
        return self.alert_message




    ### ========== ASSERTIONS =============
