# КЛАСС СТРАНИЦЫ

from pages.base_page import BasePage # Импортируем класс BasePage
from components.components import WebElement # Импортируем класс WebElement

class DemoQa(BasePage): # Создаём класс DemoQa, наследуемый от класса BasePage

    def __init__(self, driver): # добавляем конструктор, принимающий аргумент driver
        self.base_url = 'https://demoqa.com/' # создаём атрибут self.base_url и передаём в него URL
        super().__init__(driver, self.base_url) # используем конструкцию супер для прокидывания данных в верхний класс

        self.icon = WebElement(driver, '#app > header > a')
        self.btn_elements = WebElement(driver, '#app > div > div > div.home-body > div > div:nth-child(1)')
        self.footer = WebElement(driver, '#app > footer > span')
        self.h5 = WebElement(driver, 'div.card-body > h5')