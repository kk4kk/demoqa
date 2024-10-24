from pages.base_page import BasePage # Импортируем класс BasePage
from components.components import WebElement # Импортируем класс WebElement

class Tables(BasePage): # Создаём класс Tables, наследуемый от класса BasePage

    def __init__(self, driver): # добавляем конструктор, принимающий аргумент driver
        self.base_url = 'https://demoqa.com/webtables' # создаём атрибут self.base_url и передаём в него URL
        super().__init__(driver, self.base_url) # используем конструкцию супер для прокидывания данных в верхний класс

        self.no_data = WebElement(driver, 'div.rt-noData')
        self.btn_delete_row = WebElement(driver, '//*[@title="Delete"]', 'xpath')
        self.btn_edit_row = WebElement(driver, '//*[@title="Edit"]', 'xpath')
        self.btn_add_record = WebElement(driver, '#addNewRecordButton')
        self.btn_regform_submit = WebElement(driver, '#submit')
        self.user_form = WebElement(driver, '#userForm')
        self.field_first_name = WebElement(driver, '#firstName')
        self.field_last_name = WebElement(driver, '#lastName')
        self.field_user_email = WebElement(driver, '#userEmail')
        self.field_age = WebElement(driver, '#age')
        self.field_salary = WebElement(driver, '#salary')
        self.field_department = WebElement(driver, '#department')
        self.cell_name_1row = WebElement(driver, 'div.rt-tr-group:nth-child(1) > div:nth-child(1) > div:nth-child(1)')
        self.field_search = WebElement(driver, '#searchBox')
        self.btn_search = WebElement(driver, '#basic-addon2')
        self.select_wrap = WebElement(driver, '//*[@aria-label="rows per page"]', 'xpath')
        self.btn_previous = WebElement(driver, 'div.-previous > button.-btn')
        self.btn_next = WebElement(driver, 'div.-next > button.-btn')
        self.total_pages = WebElement(driver, 'span.-totalPages')
        self.current_page = WebElement(driver, '//*[@aria-label="jump to page"]', 'xpath')