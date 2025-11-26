from pages.alerts_page import AlertsPage


def test_alert(page):
    alerts = AlertsPage(page)
    alerts.goto()
    
    alerts.click_the_alert_button() 
    assert alerts.get_alert_type() == "alert"
    assert alerts.get_alert_message() == "You clicked a button"

