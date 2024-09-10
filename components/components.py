from selenium.webdriver.common.by import By # Импортируем метод By
from selenium.common.exceptions import NoSuchElementException # Импортируем исключение NoSuchElementException

class WebElement: # Создаём самостоятельный класс WebElement (не наследуется от какого-то другого класса)

    def __init__(self, driver, locator = ''): # аргумент у локатора по умолчанию - пустая строчка
        self.driver = driver
        self.locator = locator


    def click(self): # метод кликает на элемент
        self.find_element().click() # После добавления ниже метода find_element, приводим строку к такому виду


    def find_element(self):  # Метод поиска элемента. После переноса с BasePage убираем локатор из атрибутов.
        return self.driver.find_element(By.CSS_SELECTOR, self.locator)  # После переноса с BasePage обращаемся не просто к locator, а к self.locator


    def exist(self): # после переноса сюда убираем из названия icon. Вызывает метод find_element родительского класса и передает в него локатор
        try:
            self.find_element() # приводим строку к такому виду после переноса сюда метода exist
        except NoSuchElementException: # Исключение ошибки NoSuchElementException (когда элемент не найден)
            return False # Возвращаем False, в случае её появления
        return True # иначе возвращаем True

    def get_text(self):
        if str(self.find_element().text) == '© 2013-2020 TOOLSQA.COM | ALL RIGHTS RESERVED.':  # условие соответствия заданного текста и текста элемента
            return True
        else:
            return False

    def get_elem_text(self):
        if str(self.find_element().text) == 'Please select an item from left to start practice.':  # условие соответствия заданного текста и текста элемента
            return True
        else:
            return False