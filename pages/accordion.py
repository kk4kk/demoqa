# КЛАСС СТРАНИЦЫ

from pages.base_page import BasePage # Импортируем класс BasePage
from components.components import WebElement # Импортируем класс WebElement

class Accordion(BasePage): # Создаём класс Accordion, наследуемый от класса BasePage

    def __init__(self, driver): # добавляем конструктор, принимающий аргумент driver
        self.base_url = 'https://demoqa.com/accordian' # создаём атрибут self.base_url и передаём в него URL
        super().__init__(driver, self.base_url) # используем конструкцию супер для прокидывания данных в верхний класс

        self.what_lorem_ipsum = WebElement(driver, '#section1Content > p')
        self.where_lorem_ipsum1 = WebElement(driver, '#section2Content > p:nth-child(1)')
        self.where_lorem_ipsum2 = WebElement(driver, '#section2Content > p:nth-child(2)')
        self.why_lorem_ipsum = WebElement(driver, '#section3Content > p')
        self.head_what_lorem_ipsum = WebElement(driver, '#section1Heading')