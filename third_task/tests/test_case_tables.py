import pytest
from third_task.page_objects.web_tables_page import TablesPage
from third_task.page_objects.main_page import MainPage
from third_task.resourses.browser_manager import Browser
from third_task.resourses.utils import data
from third_task.resourses.conftest import pytest_sessiosstart, pytest_sessionfinish


@pytest.mark.parametrize('user_n', [1, 2], scope='session')
def test_case_tables(user_n, pytest_sessiosstart, pytest_sessionfinish):
    Browser.open_page(data['links']['main_page'])
    main = MainPage()
    assert main.check_load(), 'main page not loaded'
    main.click_elements_button()
    table = TablesPage()
    table.table_click()
    assert table.check_load(), 'table page not opened'
    table.add_click()
    table.insert_user_data(user_n)
    assert table.check_if_user_data_in_table(user_n), 'user not added'
    table.click_delete()
    assert not table.check_if_user_data_in_table(user_n), 'user not deleted'

