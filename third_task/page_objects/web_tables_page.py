from third_task.Base.BasePage import BaseForm
from third_task.page_objects.left_panel import LeftPanel
from third_task.Base.Elements.Button import Button
from third_task.page_objects.table_form import TableForm
from third_task.Base.Elements.TableRow import TableRow
from third_task.resourses.User import User


class TablesPage(BaseForm):
    panel = LeftPanel()
    _add_new_row_button = Button('//button[@id="addNewRecordButton"]', 'xpath')
    _delete_4_button = Button('//span[@id="delete-record-4"]', 'xpath')
    _table_form = TableForm()
    _row_xpath = TableRow('//div[@class="rt-td"]', 'xpath')

    def __init__(self):
        super().__init__(self._add_new_row_button)

    def add_click(self):
        self._add_new_row_button.element_click()

    def insert_user_data(self, user_n):
        self._table_form.insert_data(user_n)

    def table_click(self):
        self.panel.tables_button_click()

    def check_add(self):
        return True if self._delete_4_button.find_element() else False

    def click_delete(self):
        self._delete_4_button.element_click()

    def print_all(self):
        self._row_xpath.return_all()

    def check_if_user_data_in_table(self, user_n):
        user_data = User(user_n).get_data()
        table_data = self._row_xpath.return_all()
        return True if user_data[3] in table_data else False
