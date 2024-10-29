import time
from pages.browser_tab import BrowserTab


def test_browser_tab(browser):
    page_browser = BrowserTab(browser)

    page_browser.visit()

    assert len(browser.window_handles) == 1 # Делаем проверку сравнением количества открытых вкладок (длина),
    # используя метод для получения списка открытых вкладок.
    # Важно. Здесь мы обращаемся именно к браузеру (browser), а не к странице.

    page_browser.new_tab.click() # Добавляем новую вкладку
    time.sleep(2)

    assert len(browser.window_handles) == 2 # Снова делаем проверку сравнением количества открытых вкладок

    browser.switch_to.window(browser.window_handles[0]) # Метод принудительного перехода на указанную вкладку.
    # Т.к. вкладки хранятся в списке, то и с аргументом мы работаем как со списком: квадратные скобки, нумерация.
    time.sleep(2)
