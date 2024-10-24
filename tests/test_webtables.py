import time
from selenium.webdriver import Keys
from pages.tables import Tables



def test_tables(browser):
	"""Проверка блока No rows found"""
	page_tables = Tables(browser)

	page_tables.visit()
	assert not page_tables.no_data.exist()	# Проверяем, что у нас не пустая таблица (без статуса "No rows found")

	"""Удаляем все записи"""
	while page_tables.btn_delete_row.exist():	# Используем цикл для удаления записей.
		page_tables.btn_delete_row.click()	# Пока строки существуют, мы нажимаем на кнопку удалить

	time.sleep(2)
	assert page_tables.no_data.exist()	# Проверяем, что у нас таблица пуста ("No rows found")


def test_regform_n_table(browser):
	page_tables = Tables(browser)
	first_name = 'Masha'
	upd_first_name = 'Mariya'
	last_name = 'Rasteryasha'
	user_email = 'rasteryasha@ya.ru'
	user_age = '31'
	salary = '1000'
	department = 'Department of Lost Letters'

	page_tables.visit()
	page_tables.btn_add_record.click()
	page_tables.btn_regform_submit.click_force()

	assert page_tables.user_form.get_dom_attribute('class') == 'was-validated'
	time.sleep(2)

	page_tables.field_first_name.send_keys(first_name)
	page_tables.field_last_name.send_keys(last_name)
	page_tables.field_user_email.send_keys(user_email)
	page_tables.field_age.send_keys(user_age)
	page_tables.field_salary.send_keys(salary)
	page_tables.field_department.send_keys(department)
	time.sleep(2)
	page_tables.btn_regform_submit.click_force()
	time.sleep(3)

	# Страниц и строк в таблице может быть разное кол-во,
	# поэтому для поиска нужной записи удобнее использовать форму поиска по таблице.
	page_tables.field_search.send_keys(user_email)
	time.sleep(2)
	page_tables.btn_edit_row.click()
	page_tables.field_first_name.clear()
	page_tables.field_first_name.send_keys(upd_first_name)
	time.sleep(2)
	page_tables.btn_regform_submit.click_force()
	# Проверяю, обновились ли данные:
	assert page_tables.cell_name_1row.get_text() == upd_first_name
	time.sleep(3)

	page_tables.btn_delete_row.click()
	time.sleep(3)
	# Проверяю, удалились ли данные (по фильтру стоит нужная мне запись)
	assert page_tables.no_data.exist()


def test_tables_2(browser):
	page_tables = Tables(browser)
	page_tables.visit()

	assert page_tables.equal_url()

	page_tables.select_wrap.scroll_to_element()
	page_tables.select_wrap.click()
	page_tables.select_wrap.send_keys(Keys.PAGE_UP)
	page_tables.select_wrap.send_keys(Keys.ENTER)
	time.sleep(2)

	assert page_tables.btn_previous.get_dom_attribute('disabled')

	assert page_tables.btn_next.get_dom_attribute('disabled')

	page_tables.btn_add_record.click()
	page_tables.field_first_name.send_keys('Georgy')
	page_tables.field_last_name.send_keys('Vitsin')
	page_tables.field_user_email.send_keys('trus@operation-i.ru')
	page_tables.field_age.send_keys('47')
	page_tables.field_salary.send_keys('150')
	page_tables.field_department.send_keys('operation i')
	time.sleep(2)
	page_tables.btn_regform_submit.click_force()
	time.sleep(2)

	page_tables.btn_add_record.click()
	page_tables.field_first_name.send_keys('Yuriy')
	page_tables.field_last_name.send_keys('Nikulin')
	page_tables.field_user_email.send_keys('balbes@operation-i.ru')
	page_tables.field_age.send_keys('43')
	page_tables.field_salary.send_keys('150')
	page_tables.field_department.send_keys('operation i')
	time.sleep(2)
	page_tables.btn_regform_submit.click_force()
	time.sleep(2)

	page_tables.btn_add_record.click()
	page_tables.field_first_name.send_keys('Evgeny')
	page_tables.field_last_name.send_keys('Morgunov')
	page_tables.field_user_email.send_keys('byvalyy@operation-i.ru')
	page_tables.field_age.send_keys('37')
	page_tables.field_salary.send_keys('150')
	page_tables.field_department.send_keys('operation i')
	time.sleep(2)
	page_tables.btn_regform_submit.click_force()
	time.sleep(2)

	assert page_tables.total_pages.get_text() == '2'

	assert not page_tables.btn_next.get_dom_attribute('disabled')

	page_tables.btn_next.click()
	time.sleep(3)

	assert page_tables.current_page.get_dom_attribute('value') == '2'

	page_tables.btn_previous.click()
	time.sleep(3)

	assert page_tables.current_page.get_dom_attribute('value') == '1'