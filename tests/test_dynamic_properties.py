from pages.dynamic_properties_page import DynamicPropertiesPage


def test_appearing_button(page):
    dynamic_properties = DynamicPropertiesPage(page)
    dynamic_properties.goto()
    dynamic_properties.wait_for_visible_after_5_seconds_btn()
    assert dynamic_properties.is_visible_after_5_seconds_btn_clickable()

