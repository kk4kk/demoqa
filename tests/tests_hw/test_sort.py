import time
from pages.tables import Tables


def test_sort_columns(browser):
    page_tables = Tables(browser)

    page_tables.visit()
    # можно реализовать через цикл или так (более громоздко, но будет нагляднее в случае ошибки конкретного столбца):
    assert not 'sort' in page_tables.column_first_name.get_dom_attribute('class')
    page_tables.column_first_name.click()
    time.sleep(2)
    assert '-sort-asc' in page_tables.column_first_name.get_dom_attribute('class')
    page_tables.column_first_name.click()
    time.sleep(2)
    assert '-sort-desc' in page_tables.column_first_name.get_dom_attribute('class')

    assert not 'sort' in page_tables.column_last_name.get_dom_attribute('class')
    page_tables.column_last_name.click()
    time.sleep(2)
    assert '-sort-asc' in page_tables.column_last_name.get_dom_attribute('class')
    page_tables.column_last_name.click()
    time.sleep(2)
    assert '-sort-desc' in page_tables.column_last_name.get_dom_attribute('class')

    assert not 'sort' in page_tables.column_age.get_dom_attribute('class')
    page_tables.column_age.click()
    time.sleep(2)
    assert '-sort-asc' in page_tables.column_age.get_dom_attribute('class')
    page_tables.column_age.click()
    time.sleep(2)
    assert '-sort-desc' in page_tables.column_age.get_dom_attribute('class')

    assert not 'sort' in page_tables.column_email.get_dom_attribute('class')
    page_tables.column_email.click()
    time.sleep(2)
    assert '-sort-asc' in page_tables.column_email.get_dom_attribute('class')
    page_tables.column_email.click()
    time.sleep(2)
    assert '-sort-desc' in page_tables.column_email.get_dom_attribute('class')

    assert not 'sort' in page_tables.column_salary.get_dom_attribute('class')
    page_tables.column_salary.click()
    time.sleep(2)
    assert '-sort-asc' in page_tables.column_salary.get_dom_attribute('class')
    page_tables.column_salary.click()
    time.sleep(2)
    assert '-sort-desc' in page_tables.column_salary.get_dom_attribute('class')

    assert not 'sort' in page_tables.column_department.get_dom_attribute('class')
    page_tables.column_department.click()
    time.sleep(2)
    assert '-sort-asc' in page_tables.column_department.get_dom_attribute('class')
    page_tables.column_department.click()
    time.sleep(2)
    assert '-sort-desc' in page_tables.column_department.get_dom_attribute('class')

    assert not 'sort' in page_tables.column_action.get_dom_attribute('class')
    page_tables.column_action.click()
    time.sleep(2)
    assert '-sort-asc' in page_tables.column_action.get_dom_attribute('class')
    page_tables.column_action.click()
    time.sleep(2)
    assert '-sort-desc' in page_tables.column_action.get_dom_attribute('class')