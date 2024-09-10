# КЛАСС СТРАНИЦЫ

# from selenium.common.exceptions import NoSuchElementException # Импортируем исключение NoSuchElementException
from pages.base_page import BasePage # Импортируем класс BasePage
from components.components import WebElement # Импортируем класс WebElement

class DemoQa(BasePage): # Создаём класс DemoQa, наследуемый от класса BasePage

    def __init__(self, driver): # добавляем конструктор, принимающий аргумент driver
        self.base_url = 'https://demoqa.com/' # создаём атрибут self.base_url и передаём в него URL
        super().__init__(driver, self.base_url) # используем конструкцию супер для прокидывания данных в верхний класс

        self.icon = WebElement(driver, '#app > header > a')
        self.btn_elements = WebElement(driver, '#app > div > div > div.home-body > div > div:nth-child(1)')
        self.footer = WebElement(driver, '#app > footer > span')

# перенесли метод exist в components
    # def exist_icon(self): # вызываем метод find_element родительского класса и передает в него локатор
    #     try:
    #         # self.find_element(locator='#app > header > a')
    #         self.icon.find_element() # приводим строку к такому виду после переноса метода find_element в components.py
    #     except NoSuchElementException: # Исключение ошибки NoSuchElementException (когда элемент не найден)
    #         return False # Возвращаем False, в случае её появления
    #     return True # иначе возвращаем True

# перенесли метод click в components
    # def click_on_the_icon(self): # метод кликает на элемент
    #     self.find_element(locator='#app > header > a').click() # находим элемент по локатору
    #
    # def click_on_the_btn_elements(self): # метод для теста test_go_to_page_elements
    #     self.find_element(locator='#app > div > div > div.home-body > div > div:nth-child(1)').click()

# перенесли метод equal_url в базовый класс
    # def equal_url(self): # метод проверки URL на соответствие
    # #    if self.get_url() == 'https://demoqa.com/': # если текущий URL совпадает с ...
    #     if self.get_url() == self.base_url: # меняем предыдущий вариант явного указания адреса на self.base_url
    #         return True
    #     else:
    #         return False