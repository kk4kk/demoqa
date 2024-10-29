import time
from pages.alerts import Alerts


def test_alert(browser):
    alert_page = Alerts(browser)

    alert_page.visit()
    assert not alert_page.alert() # Проверка отсутствия активного алерта на странице

    alert_page.alertButton.click()
    time.sleep(2)

    assert alert_page.alert()
    alert_page.alert().accept()


def test_alert_text(browser):
    alert_page = Alerts(browser)

    alert_page.visit()
    alert_page.alertButton.click()
    time.sleep(2)

    assert alert_page.alert().text == 'You clicked a button' # Проверка соответствия текста алерта

    alert_page.alert().accept() # Подтверждение алерта
    assert not alert_page.alert()


def test_confirm(browser):
    alert_page = Alerts(browser)

    alert_page.visit()
    alert_page.confirmButton.click()
    time.sleep(2)
    alert_page.alert().dismiss()    # Отмена алерта

    assert alert_page.confirmResult.get_text() == 'You selected Cancel'  # Проверка соответствия текста алерта


def test_prompt(browser):
    alert_page = Alerts(browser)
    name = 'Jackie Chan'
    alert_page.visit()
    alert_page.promptButton.click()
    time.sleep(2)

    alert_page.alert().send_keys(name) # Ввод текста в поле алерта
    alert_page.alert().accept()

    assert alert_page.promptResult.get_text() == f'You entered { name }' # Проверка соответствия текста алерта
    time.sleep(2)
