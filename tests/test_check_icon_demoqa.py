# ТЕСТ

# from selenium.webdriver.common.by import By
from pages.demoqa import DemoQa # Импортируем класс
import time
def test_check_icon(browser):

    # browser.get('https://demoqa.com/')
    # icon = browser.find_element(By.CSS_SELECTOR, '#app > header > a')
    #
    # if icon is None:
    #     print('Элемент не найден')
    # else:
    #     print('Элемент найден')

    demo_qa_page = DemoQa(browser) # Создаем объект класса DemoQa, передаём в него драйвер (browser)
    demo_qa_page.visit() # посещаем страницу
    time.sleep(3)
    # demo_qa_page.click_on_the_icon() # кликаем по элементу
    # меняем после переноса метода click в components:
    demo_qa_page.icon.click()
    time.sleep(3) # благодаря этому мы увидим, что страничка перезагрузится
    assert demo_qa_page.equal_url() # проверка URL на соответствие
    # меняем после переноса метода exist в components:
    # assert demo_qa_page.exist_icon() # проверка наличия элемента на странице
    assert demo_qa_page.icon.exist()