from pages.text_box import TextBox
import time

def test_placeholder(browser):
    text_box_page = TextBox(browser)

    text_box_page.visit()
    assert text_box_page.name.get_dom_attribute('placeholder') == 'Full Name'