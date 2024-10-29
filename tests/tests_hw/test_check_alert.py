import time
from pages.alerts import Alerts


def test_check_alert(browser):
    alert_page = Alerts(browser)

    alert_page.visit()
    assert not alert_page.alert()

    alert_page.timerAlertButton.click()
    time.sleep(6)

    assert alert_page.alert()
