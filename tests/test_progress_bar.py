from pages.progress_bar import ProgressBar
import time


def test_progress_bar(browser):
    pb = ProgressBar(browser)

    pb.visit()
    time.sleep(2)

    pb.startStopButton.click_force()

    while True: # бесконечный цикл пока True
        if pb.progressBar.get_dom_attribute('aria-valuenow') == '51': # Если значение достигло 51
            pb.startStopButton.click_force() # то нажимаем на кнопку
            break # выходим из цикла

    time.sleep(2)
    assert pb.progressBar.get_dom_attribute('aria-valuenow') == '51'

