import pytest

from pages.demoqa import DemoQa
from pages.radio_button import RadioBtn


@pytest.mark.skip
def test_decor(browser):
    demo_qa_page = DemoQa(browser)

    demo_qa_page.visit()

    assert demo_qa_page.h5.check_count_elements(6)

    for element in demo_qa_page.h5.find_elements(): # цикл, где find_elements ищет все элементы по неуникальному локатору
        assert element.text != '' # проверяем, что текст каждого элемента не равен пустой строке


@pytest.mark.skipif(True, reason = 'Просто пропуск')
def test_decor_1(browser):
    radio = RadioBtn(browser)

    radio.visit()
    radio.btn_yes.click_force()
    assert radio.text.get_text() == 'You have selected Yes'

    radio.btn_impressive.click_force()
    assert radio.text.get_text() == 'You have selected Impressive'

    assert 'disabled' in radio.btn_no.get_dom_attribute('class')