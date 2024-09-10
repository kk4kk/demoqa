# ТЕСТ

# Импортируем классы:
from pages.demoqa import DemoQa
from pages.elements_page import ElementsPage

def test_go_to_page_elements(browser):

    demo_qa_page = DemoQa(browser) # Создаем объект класса DemoQa, передаём в него драйвер (browser)
    elements_page = ElementsPage(browser) # Создаем объект класса ElementsPage, передаём в него драйвер (browser)

    demo_qa_page.visit() # посещаем страницу
    assert demo_qa_page.equal_url() # проверка URL на соответствие

    demo_qa_page.btn_elements.click() # кликаем на кнопку Elements
    assert elements_page.equal_url() # проверка URL на соответствие