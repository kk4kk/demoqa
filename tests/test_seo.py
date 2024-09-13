from pages.demoqa import DemoQa # Импортируем класс DemoQa


def test_check_title_demo(browser):
    demo_qa_page = DemoQa(browser)  # Создаем объект класса DemoQa, передаём в него драйвер (browser)

    demo_qa_page.visit()
    assert browser.title == 'DEMOQA' # Сравниваем название title с заданным

