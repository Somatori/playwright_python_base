from playwright.sync_api import Page, expect, Dialog
from configs.config import BASE_URL


class AlertsPage:
    def __init__(self, page: Page):
        self.page = page

        # Attributes for dialog window
        self.alert_message = None
        self.alert_type = None
        self._should_accept = True 
        self._input_text_for_prompt = None

    ### ========== LOCATORS ==========
    def _alert_button(self):
        return self.page.locator('#alertButton')
    
    def _confirm_button(self):
        return self.page.locator('#confirmButton')
    
    def _confirm_message(self):
        return self.page.locator('#confirmResult')
    
    def _prompt_button(self):
        return self.page.locator('#promtButton')
    
    def _prompt_message(self):
        return self.page.locator('#promptResult')

    ### ========== ACTIONS =============
    def goto(self):
        self.page.goto(f"{BASE_URL}/alerts", wait_until="domcontentloaded")

   # The central dialog handler function
    def _handle_dialog_logic(self, dialog: Dialog):
        # Store dialog message/type
        self.alert_message = dialog.message
        self.alert_type = dialog.type

        # Check if it's a prompt and we have text to input
        if self.alert_type == "prompt" and self._input_text_for_prompt is not None:
            if self._should_accept:
                # Pass the input text when accepting the prompt
                dialog.accept(self._input_text_for_prompt)
            else:
                # Dismiss the prompt without entering text (or enters empty string)
                dialog.dismiss()
        
        # Handle regular alerts/confirms based on the class attribute
        if self._should_accept:
            dialog.accept()
        else:
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

    def click_prompt_button_and_respond(self, input_text: str = "", accept_dialog: bool = True):
        """
        Clicks the prompt button, enters text, and handles the dialog.
        :param input_text: The text to enter into the prompt field.
        :param accept_dialog: True to click 'OK' (accept), False to click 'Cancel' (dismiss).
        """
        # Set the flags before the event is triggered
        self._should_accept = accept_dialog
        self._input_text_for_prompt = input_text
        
        # Register the handler
        self.page.once("dialog", self._handle_dialog_logic)
        
        # Trigger the prompt
        self._prompt_button().click()


    ### ========== ASSERTIONS =============

    def confirm_message_has_text(self, text):
        expect(self._confirm_message()).to_have_text(text)
        return True
    
    def prompt_message_has_text(self, text):
        expect(self._prompt_message()).to_have_text(text)
        return True