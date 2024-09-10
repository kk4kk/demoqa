# КЛАСС СТРАНИЦЫ

from pages.base_page import BasePage # Импортируем класс BasePage
from components.components import WebElement # Импортируем класс WebElement

class ElementsPage(BasePage): # Создаём класс ElementsPage, наследуемый от класса BasePage

    def __init__(self, driver): # добавляем конструктор, принимающий аргумент driver
        self.base_url = 'https://demoqa.com/elements' # создаём атрибут self.base_url и передаём в него URL
        super().__init__(driver, self.base_url) # используем конструкцию супер для прокидывания данных в верхний класс

        self.clue_text = WebElement(driver, '#app > div > div > div > div.col-12.mt-4.col-md-6')

# перенесли метод equal_url в базовый класс
    # def equal_url(self): # метод проверки URL на соответствие
    #     if self.get_url() == self.base_url: # условие соответствия заданного self.base_url и полученного self.get_url
    #         return True
    #     else:
    #         return False

