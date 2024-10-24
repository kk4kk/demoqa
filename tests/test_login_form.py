from selenium.webdriver import Keys
from pages.form_page import FormPage
import time

def test_login_form(browser):
    form_page = FormPage(browser)

    form_page.visit()
    assert not form_page.modal_dialog.exist()
    time.sleep(2)
    form_page.first_name.send_keys('tester')
    form_page.last_name.send_keys('testerovich')
    form_page.user_email.send_keys('test@ttt.tt')
    form_page.gender_radio_1.click_force()
    form_page.user_number.send_keys('11111111111')
    form_page.hobbies_1.click_force()
    form_page.hobbies_3.click_force()
    form_page.current_address.send_keys('588841, North Korea, Pyongyang')
    time.sleep(2)
    form_page.btn_submit.click_force()
    time.sleep(2)

    assert form_page.modal_dialog.exist() # Проверка на наличие modal_dialog
    form_page.btn_close_modal.click_force()


def test_login_form_1(browser):
    form_page = FormPage(browser)

    form_page.visit()
    form_page.select_state.scroll_to_element()
    form_page.select_state.click()
    time.sleep(2)
    form_page.input_state.send_keys('Haryana')
    time.sleep(2)
    form_page.input_state.send_keys(Keys.ENTER)
    form_page.select_city.click()
    time.sleep(2)
    form_page.input_city.send_keys('Panipat')
    time.sleep(2)
    form_page.input_city.send_keys(Keys.ENTER)
    time.sleep(2)


def test_login_form_2(browser):
    form_page = FormPage(browser)

    form_page.visit()
    form_page.select_state.scroll_to_element()
    form_page.select_state.click()
    form_page.btn_NCR.click()
    time.sleep(2)
    form_page.select_city.click()
    form_page.btn_Noida.click()


def test_login_form_3(browser):
    form_page = FormPage(browser)

    form_page.visit()
    form_page.select_state.scroll_to_element()
    form_page.select_state.click()
    form_page.input_state.send_keys(Keys.PAGE_DOWN)
    form_page.input_state.send_keys(Keys.ENTER)
    time.sleep(2)
    form_page.select_city.click()
    form_page.input_city.send_keys(Keys.DOWN)
    time.sleep(2)
    form_page.input_city.send_keys(Keys.ENTER)
    time.sleep(2)