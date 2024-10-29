from pages.demoqa import DemoQa
from pages.alerts import Alerts
from pages.accordion import Accordion
from pages.browser_tab import BrowserTab
import pytest # Импортируем pytest для использования декоратора
import time


@pytest.mark.parametrize('pages', [Accordion, Alerts, DemoQa, BrowserTab]) # позволяет избежать нам повторения кода, оптимизирует его.
def test_check_title_all_pages(browser, pages): # в функцию будут подставляться по очереди все страницы-аргументы,
    # перечисленные выше в декораторе. Функция циклично отработает с каждым из них.
    page = pages(browser)
    page.visit()
    time.sleep(2)

    assert page.viewport.exist() # проверяем наличие мета тега
    assert page.viewport.get_dom_attribute('name') == 'viewport'
    assert page.viewport.get_dom_attribute('content') == 'width=device-width,initial-scale=1'