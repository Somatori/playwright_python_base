from pages.alerts_page import AlertsPage


def test_alert(page):
    alerts = AlertsPage(page)
    alerts.goto()
    
    alerts.click_alert_button_and_respond(accept_dialog=True) 
    assert alerts.get_alert_type() == "alert"
    assert alerts.get_alert_message() == "You clicked a button"


def test_confirm(page):
    alerts = AlertsPage(page)
    alerts.goto()
    
    alerts.click_confirm_button_and_respond(accept_dialog=True) 
    assert alerts.get_alert_type() == "confirm"
    assert alerts.get_alert_message() == "Do you confirm action?"
    assert alerts.confirm_message_has_text("You selected Ok")

    alerts.click_confirm_button_and_respond(accept_dialog=False) 
    assert alerts.confirm_message_has_text("You selected Cancel")