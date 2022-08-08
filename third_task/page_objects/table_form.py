from third_task.Base.Elements.Button import Button
from third_task.Base.Elements.Input import Input
from third_task.Base.BasePage import BaseForm
from third_task.Base.BaseElement import BaseElement
from third_task.resourses.User import User


class TableForm(BaseForm):

    _first_name_input = Input("//input[@id='firstName']", 'xpath')
    _last_name_input = Input("//input[@id='lastName']", 'xpath')
    _mail_input = Input("//input[@id='userEmail']", 'xpath')
    _age_input = Input("//input[@id='age']", 'xpath')
    _salary_input = Input("//input[@id='salary']", 'xpath')
    _department_input = Input("//input[@id='department']", 'xpath')
    _submit_button = Button("//button[@id='submit']", 'xpath')
    _check_form = BaseElement('//div[@id="registration-form-modal"]', 'xpath')

    def __init__(self):
        super().__init__(self._submit_button)

    def insert_data(self, user_n):
        user = User(user_n)
        user_info = user.get_data()
        self._first_name_input.sendkeys(user_info[0])
        self._last_name_input.sendkeys(user_info[1])
        self._mail_input.sendkeys(user_info[2])
        self._age_input.sendkeys(user_info[3])
        self._salary_input.sendkeys(user_info[4])
        self._department_input.sendkeys(user_info[5])
        self._submit_button.element_click()
