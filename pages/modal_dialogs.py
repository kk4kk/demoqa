from components.components import WebElement
from pages.base_page import BasePage

class ModalDialogs(BasePage):


    def __init__(self, driver):
        self.base_url = 'https://demoqa.com/modal-dialogs'
        super().__init__(driver, self.base_url)

        self.btns_third_menu = WebElement(driver, 'div:nth-child(3) > div > ul >li')
        self.icon = WebElement(driver, '#app > header > a > img')
        self.btnSmallModal = WebElement(driver, '#showSmallModal')
        self.btnLargeModal = WebElement(driver, '#showLargeModal')
        self.btnCloseSmallModal = WebElement(driver, '#closeSmallModal')
        self.btnCloseLargeModal = WebElement(driver, '#closeLargeModal')
        self.smallModal = WebElement(driver, '//*[@aria-labelledby="example-modal-sizes-title-sm"]', 'xpath')
        self.largeModal = WebElement(driver, '//*[@aria-labelledby="example-modal-sizes-title-lg"]', 'xpath')