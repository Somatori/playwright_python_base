from playwright.sync_api import Page, expect, Dialog
from configs.config import BASE_URL


class AlertsPage:
    def __init__(self, page: Page):
        self.page = page

        # Attributes for dialog window
        self.alert_message = None
        self.alert_type = None
        self._should_accept = True 

    ### ========== LOCATORS ==========
    def _alert_button(self):
        return self.page.locator('#alertButton')
    
    def _confirm_button(self):
        return self.page.locator('#confirmButton')
    
    def _confirm_message(self):
        return self.page.locator('#confirmResult')

    ### ========== ACTIONS =============
    def goto(self):
        self.page.goto(f"{BASE_URL}/alerts", wait_until="domcontentloaded")

   # The central dialog handler function
    def _handle_dialog_logic(self, dialog: Dialog):
        # Store dialog message/type
        self.alert_message = dialog.message
        self.alert_type = dialog.type
        
        # Decide whether to accept or dismiss based on the class attribute
        if self._should_accept:
            dialog.accept()
        else:
            # Note: Dismissing an 'alert' type dialog often behaves like 'accept' in browsers
            # This is most useful for 'confirm' or 'prompt' dialogs.
            dialog.dismiss()

    def click_alert_button_and_respond(self, accept_dialog: bool = True):
        """
        Clicks the alert button and handles the ensuing dialog.
        :param accept_dialog: True to accept (OK/Yes), False to dismiss (Cancel/No).
        """
        # Set the decision flag before the event is triggered
        self._should_accept = accept_dialog
        
        # Register the handler (we use the instance method directly)
        self.page.once("dialog", self._handle_dialog_logic)
        
        # Trigger the alert
        self._alert_button().click()

    def get_alert_type(self):
        return self.alert_type

    def get_alert_message(self):
        # Optional check in case the dialog never appeared
        if self.alert_message is None:
             raise Exception("Alert message was never captured. The dialog might not have appeared.")
        
        return self.alert_message

    def click_confirm_button_and_respond(self, accept_dialog: bool = True):
        """
        Clicks the confirm button and handles the ensuing dialog.
        :param accept_dialog: True to accept (OK/Yes), False to dismiss (Cancel/No).
        """
        # Set the decision flag before the event is triggered
        self._should_accept = accept_dialog
        
        # Register the handler (we use the instance method directly)
        self.page.on("dialog", self._handle_dialog_logic)
        
        # Trigger the alert
        self._confirm_button().click()


    ### ========== ASSERTIONS =============

    def confirm_message_has_text(self, text):
        expect(self._confirm_message()).to_have_text(text)
        return True