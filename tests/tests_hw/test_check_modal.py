from pages.modal_dialogs import ModalDialogs
import pytest # Импортируем pytest для использования декоратора
import time
import requests


response = requests.get('https://demoqa.com/modal-dialogs')
# response = requests.get('http://globalcom.spb.ru/en/') # Добавил адрес с 404 ошибкой для проверки пропуска
@pytest.mark.skipif(response.status_code != 200, reason="Пропуск теста из-за неверного кода ответа")
def test_modal_dialogs(browser):
    modal_dialogs = ModalDialogs(browser)
    modal_dialogs.visit()
    modal_dialogs.btnSmallModal.click()
    time.sleep(2)
    assert modal_dialogs.smallModal.exist()
    modal_dialogs.btnCloseSmallModal.click()
    time.sleep(2)
    modal_dialogs.btnLargeModal.click()
    time.sleep(2)
    assert modal_dialogs.largeModal.exist()
    modal_dialogs.btnCloseLargeModal.click()
    time.sleep(2)