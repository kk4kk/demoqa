# ТЕСТ

from pages.demoqa import DemoQa # Импортируем класс
from pages.elements_page import ElementsPage

def test_go_to_page_elements(browser):

    demo_qa_page = DemoQa(browser) # Создаем объект класса DemoQa, передаём в него драйвер (browser)
    elements_page = ElementsPage(browser)

    demo_qa_page.visit() # посещаем страницу
    assert demo_qa_page.equal_url() # проверка URL на соответствие

    # demo_qa_page.click_on_the_btn_elements() # кликаем на кнопку
    # меняем после переноса метода click в components:
    demo_qa_page.btn_elements.click()
    assert elements_page.equal_url() # проверка URL на соответствие