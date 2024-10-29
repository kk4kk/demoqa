import time
from pages.links import Links


def test_window_tab(browser):
    links = Links(browser)

    links.visit()
    assert links.link_home.get_text() == 'Home'
    assert links.link_home.get_dom_attribute('href') == 'https://demoqa.com'
    assert links.link_home.get_dom_attribute('target') == '_blank'
    links.link_home.click()
    time.sleep(2)
    assert len(browser.window_handles) == 2