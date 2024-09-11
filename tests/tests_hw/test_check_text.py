# ТЕСТ

from pages.demoqa import DemoQa # Импортируем класс
from pages.elements_page import ElementsPage # Импортируем класс
import time

def test_check_footer_text(browser):

    demo_qa_page = DemoQa(browser) # Создаем объект класса DemoQa, передаём в него драйвер (browser)

    demo_qa_page.visit() # посещаем страницу
    assert demo_qa_page.footer.get_text() # проверка текста футера на соответствие


def test_check_elements_text(browser):

    demo_qa_page = DemoQa(browser)  # Создаем объект класса DemoQa, передаём в него драйвер (browser)
    elements_page = ElementsPage(browser) # Создаем объект класса ElementsPage, передаём в него драйвер (browser)

    demo_qa_page.visit() # посещаем страницу
    demo_qa_page.btn_elements.click() # кликаем на кнопку элементов
    time.sleep(3) # сделал, чтобы убедиться в переходе по клику
    assert elements_page.clue_text.get_elem_text() # проверка текста в разделе элементы на соответствие


def test_page_elements(browser):
    elements_page = ElementsPage(browser)

    elements_page.visit()
    assert elements_page.icon.exist()
    assert elements_page.btn_sidebar_first.exist()
    assert elements_page.btn_sidebar_first_textbox.exist()





