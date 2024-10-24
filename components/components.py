from selenium.webdriver.common.by import By # Импортируем метод By
from selenium.common.exceptions import NoSuchElementException # Импортируем исключение NoSuchElementException
from selenium.webdriver.common.keys import Keys

class WebElement: # Создаём самостоятельный класс WebElement (не наследуется от какого-то другого класса)

    def __init__(self, driver, locator = '', locator_type='css'): # аргумент у локатора по умолчанию - пустая строчка.
                                                                  # после добавления метода get_by_type, прописываем тип селектора по умолчанию
        self.driver = driver
        self.locator = locator
        self.locator_type = locator_type # указываем после добавления метода get_by_type

    def click(self): # метод кликает на элемент
        self.find_element().click() # После добавления ниже метода find_element, приводим строку к такому виду


    def click_force(self): # метод принудительно кликает на элемент, даже если он скрыт
        self.driver.execute_script('arguments[0].click();', self.find_element())


    def find_element(self):  # Метод поиска элемента. После переноса с BasePage убираем локатор из атрибутов.
        return self.driver.find_element(self.get_by_type(), self.locator)  # После переноса с BasePage обращаемся не просто к locator, а к self.locator
                                                                           # после добавления метода get_by_type, меняем и тип селектора на вызов метода get_by_type


    def find_elements(self):  # Метод поиска элементов.
        return self.driver.find_elements(self.get_by_type(), self.locator) # аналогично меняем тип селектора на вызов метода get_by_type


    def exist(self): # после переноса сюда убираем из названия icon. Вызывает метод find_element родительского класса и передает в него локатор
        try:
            self.find_element() # приводим строку к такому виду после переноса сюда метода exist
        except NoSuchElementException: # Исключение ошибки NoSuchElementException (когда элемент не найден)
            return False # Возвращаем False, в случае её появления
        return True # иначе возвращаем True


    def get_text(self):
        return str(self.find_element().text)


    def get_copyright_text(self):
        if str(self.find_element().text) == '© 2013-2020 TOOLSQA.COM | ALL RIGHTS RESERVED.':  # условие соответствия заданного текста и текста элемента
            return True
        else:
            return False

    def get_elem_text(self):
        if str(self.find_element().text) == 'Please select an item from left to start practice.':  # условие соответствия заданного текста и текста элемента
            return True
        else:
            return False


    def visible(self):
        return self.find_element().is_displayed()


    def check_count_elements(self, count: int) -> bool:
        if len(self.find_elements()) == count:
            return True
        return False


    def send_keys(self, text: str):
        self.find_element().send_keys(text)


    def clear(self):
        self.find_element().send_keys(Keys.CONTROL + 'a') # find_element указывать необязательно, т.к. выше в send_keys он вызывается
        self.find_element().send_keys(Keys.DELETE)


    def get_dom_attribute(self, name: str):
        value = self.find_element().get_dom_attribute(name)

        if value is None:
            return False
        if len(value) > 0:
            return value
        return True


    def check_css(self, style, value=''):
        return self.find_element().value_of_css_property(style) == value

    def get_by_type(self):
        if self.locator_type == 'id':
            return By.ID
        elif self.locator_type == 'name':
            return By.NAME
        elif self.locator_type == 'xpath':
            return By.XPATH
        elif self.locator_type == 'css':
            return By.CSS_SELECTOR
        elif self.locator_type == 'class':
            return By.CLASS_NAME
        elif self.locator_type == 'link':
            return By.LINK_TEXT
        else:
            print('Locator type ' + self.locator_type + ' is not correct')


    def scroll_to_element(self): # метод скроллинга страницы
        self.driver.execute_script('window.scrollTo(0, document.body.scrollHeight);', self.find_element())
