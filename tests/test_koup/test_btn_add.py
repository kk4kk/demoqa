from pages.koup import Koup
from pages.koup_add import KoupAdd
import time


def test_koup_add(browser):
    koup_page = Koup(browser)
    koup_add = KoupAdd(browser)

    koup_page.visit()

    assert koup_page.link_add.get_text() == 'Add/Remove Elements'

    koup_page.link_add.click()

    assert koup_add.equal_url()

    assert koup_add.btn_add.get_text() == 'Add Element' # Проверяем наличие кнопки с текстом "Add Element"

    assert koup_add.btn_add.get_dom_attribute('onclick') == 'addElement()' # Проверяем, что атрибут onclick у кнопки равен "addElement()"

    """When Кликнуть на кнопку 4 раза"""
    for i in range(4): # Цикл для 4-х кликов по кнопке "Add Element"
        koup_add.btn_add.click()

    assert koup_add.btns_delete.check_count_elements(4) # Проверяем наличие 4-х появившихся кнопок "Delete".
    # Для этого обращаемся к странице koup_add -> кнопке btns_delete, и методом check_count_elements проверяем кол-во кнопок.

    # проверка для всех элементов
    for element in koup_add.btns_delete.find_elements(): # Обращаемся к странице, кнопкам
        assert element.text == 'Delete' # И находим их по тексту "Delete"

    # ! проверка только для первого элемента. Не подходит для множества одинаковых элементов с идентичным неуникальным локатором!
    assert koup_add.btns_delete.get_text() == 'Delete'

    """When Кликнуть на кнопку "Delete" """
    while koup_add.btns_delete.exist(): # Используем цикл while для кликов по кнопкам "Delete". Цикл работает, пока условие = истина.
        koup_add.btns_delete.click()

    assert not koup_add.btns_delete.exist() # Проводим проверку, что кнопки "Delete" более не существуют.
    time.sleep(7)