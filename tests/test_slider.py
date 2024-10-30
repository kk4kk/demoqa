from pages.slider import Slider
from selenium.webdriver import Keys


def test_slider_v3(browser):
    slider = Slider(browser)

    slider.visit()
    assert slider.slider.exist()
    assert slider.field_input.exist()

    while not slider.field_input.get_dom_attribute('value') == '50': # Цикл для интерактивного эл-та slider.
        # Пока значение атрибута value слайдера НЕ 50,
        slider.slider.send_keys(Keys.ARROW_RIGHT) # Мы стрелкой вправо двигаем бегунок слайдера

    assert slider.field_input.get_dom_attribute('value') == '50' # После этого проверяем, что значение достигло 50