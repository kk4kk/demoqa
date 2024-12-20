from pages.demoqa import DemoQa
from pages.alerts import Alerts
from pages.accordion import Accordion
from pages.browser_tab import BrowserTab
import pytest # Импортируем pytest для использования декоратора
import time


def test_check_title_demo(browser):
    demo_qa_page = DemoQa(browser)  # Создаем объект класса DemoQa, передаём в него драйвер (browser)

    demo_qa_page.visit()
    assert browser.title == 'DEMOQA' # Сравниваем название title с заданным


@pytest.mark.parametrize('pages', [Accordion, Alerts, DemoQa, BrowserTab]) # позволяет избежать нам повторения кода, оптимизирует его.
def test_check_title_all_pages(browser, pages): # в функцию будут подставляться по очереди все страницы-аргументы,
    # перечисленные выше в декораторе. Функция циклично отработает с каждым из них.
    page = pages(browser)
    page.visit()
    time.sleep(2)

    assert page.get_title() == 'DEMOQA'