import pytest
from selenium import webdriver
# from selenium.webdriver.chrome.options import Options

@pytest.fixture(scope='session')
def browser():
    # options = Options()
    # options.add_argument('--ignore-certificate-errors')
    # options.add_argument('--ignore-ssl-errors')
    # driver = webdriver.Chrome(options=options) # Добавил опции игнорирования ошибок SSL в этом проекте.
    driver = webdriver.Chrome()
    driver.set_window_size(width=1000, height=1000) # Устанавливаем размер окна для тестов
    yield driver
    driver.quit()