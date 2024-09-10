# КЛАСС СТРАНИЦЫ

from pages.base_page import BasePage # Импортируем класс BasePage
from components.components import WebElement # Импортируем класс WebElement

class ElementsPage(BasePage): # Создаём класс ElementsPage, наследуемый от класса BasePage

    def __init__(self, driver): # добавляем конструктор, принимающий аргумент driver
        self.base_url = 'https://demoqa.com/elements' # создаём атрибут self.base_url и передаём в него URL
        super().__init__(driver, self.base_url) # используем конструкцию супер для прокидывания данных в верхний класс

        self.clue_text = WebElement(driver, '#app > div > div > div > div.col-12.mt-4.col-md-6')