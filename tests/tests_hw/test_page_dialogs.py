from pages.modal_dialogs import ModalDialogs # Импортируем класс
from pages.demoqa import DemoQa
import time


def test_modal_elements(browser):
    modal_dialogs = ModalDialogs(browser) # Создаем объект класса ModalDialogs, передаём в него драйвер (browser)

    modal_dialogs.visit() # посещаем страницу
    assert modal_dialogs.btns_third_menu.check_count_elements(count=5) # проверяем количество элементов раздела меню на соответствие заданному значению


def test_navigation_modal(browser):
    modal_dialogs = ModalDialogs(browser) # Создаем объект класса ModalDialogs, передаём в него драйвер (browser)
    demo_qa_page = DemoQa(browser)  # Создаем объект класса DemoQa, передаём в него драйвер (browser)

    modal_dialogs.visit()  # посещаем страницу
    modal_dialogs.refresh() # обновляем страницу
    modal_dialogs.icon.click() # по клику на иконку переходим на главную страницу
    browser.back() # переходим назад стрелкой браузера
    browser.set_window_size(900, 400) # устанавливаем размер экрана 900х400
    time.sleep(2) # timeout 2 сек
    browser.forward() # переходим вперед стрелкой браузера

    assert demo_qa_page.equal_url()  # проверка URL главной страницы на соответствие
    assert browser.title == 'DEMOQA'  # Сравниваем название title с заданным

    browser.set_window_size(1000, 1000)  # устанавливаем размер экрана 1000х1000