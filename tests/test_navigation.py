from pages.demoqa import DemoQa # Импортируем класс DemoQa
from pages.elements_page import ElementsPage # Импортируем класс WebElement


def test_navigation(browser):
    demo_qa_page = DemoQa(browser)  # Создаем объект класса DemoQa, передаём в него драйвер (browser)
    elements_page = ElementsPage(browser)  # Создаем объект класса ElementsPage, передаём в него драйвер (browser)

    demo_qa_page.visit()
    demo_qa_page.btn_elements.click()
    demo_qa_page.refresh()
    browser.refresh()
    browser.back()
    browser.forward()

    assert elements_page.equal_url()