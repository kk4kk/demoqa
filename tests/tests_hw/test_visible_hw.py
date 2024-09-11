from pages.accordion import Accordion
import time

def test_visible_accordion(browser):
    accordion = Accordion(browser)                  # Создаем объект страницы

    accordion.visit()                               # Посещаем страницу accordion
    assert accordion.what_lorem_ipsum.visible()     # Проверяем на видимость элемента
    accordion.head_what_lorem_ipsum.click()         # Кликаем на элемент
    time.sleep(2)
    assert not accordion.what_lorem_ipsum.visible() # Проверяем на невидимость элемента


def test_visible_accordion_default(browser):
    accordion = Accordion(browser)                      # Создаем объект страницы

    accordion.visit()                                   # Посещаем страницу accordion
    assert not accordion.where_lorem_ipsum1.visible()   # Проверяем элементы на невидимость
    assert not accordion.where_lorem_ipsum2.visible()
    assert not accordion.why_lorem_ipsum.visible()