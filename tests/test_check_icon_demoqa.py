# ТЕСТ

from pages.demoqa import DemoQa # Импортируем класс

def test_check_icon(browser):

    demo_qa_page = DemoQa(browser) # Создаем объект класса DemoQa, передаём в него драйвер (browser)
    demo_qa_page.visit() # посещаем страницу
    demo_qa_page.icon.click()
    assert demo_qa_page.equal_url() # проверка URL на соответствие
    assert demo_qa_page.icon.exist()