# БАЗОВЫЙ КЛАСС

from selenium.webdriver.common.by import By # Импортируем метод By

class BasePage: # Создаём класс

    # def __init__(self, driver): # инициализируем с атрибутом driver, принимающим аргументы
    #     self.driver = driver
    #     self.base_url = 'https://demoqa.com/' # аргумент выставлен по умолчанию

    def __init__(self, driver, base_url): # инициализируем с атрибутом driver, а также добавляем base_url, принимающие аргументы
        self.driver = driver
        self.base_url = base_url # теперь это не явный адрес, а принимаемый аргумент base_url

    def visit(self): # метод посещения страницы
        return self.driver.get(self.base_url) # возвращает переход на страницу по принятому URL

# Перенесли метод find_element в components.py
    # def find_element(self, locator): # Метод поиска элемента. Принимает локатор
    #     return self.driver.find_element(By.CSS_SELECTOR, locator) # Возвращает результат обращение к поиску локатора через драйвер.

    def get_url(self): # метод получения текущего URL
        return self.driver.current_url

    def equal_url(self): # метод проверки URL на соответствие
        if self.get_url() == self.base_url: # условие соответствия заданного self.base_url и полученного self.get_url
            return True
        else:
            return False