from pages.text_box import TextBox
import time


def test_text_box(browser):
    text_box = TextBox(browser)
    name = 'Kim Jong-Un'
    address = '588841, North Korea, Pyongyang'

    text_box.visit()
    text_box.name.send_keys(name)
    time.sleep(2)
    text_box.address.send_keys(address)
    time.sleep(2)
    text_box.btn_submit.click_force()

    assert text_box.output_name.get_text() == f'Name:{name}'
    assert text_box.output_address.get_text() == f'Current Address :{address}'