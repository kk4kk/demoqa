# БАЗОВЫЙ КЛАСС

class BasePage: # Создаём класс


    def __init__(self, driver, base_url): # инициализируем с атрибутом driver, а также добавляем base_url
        self.driver = driver
        self.base_url = base_url # теперь это не явный адрес, а принимаемый аргумент base_url


    def visit(self): # метод посещения страницы
        return self.driver.get(self.base_url) # возвращает переход на страницу по принятому URL


    def get_url(self): # метод получения текущего URL
        return self.driver.current_url


    def equal_url(self): # метод проверки URL на соответствие
        if self.get_url() == self.base_url: # условие соответствия заданного self.base_url и полученного self.get_url
            return True
        else:
            return False