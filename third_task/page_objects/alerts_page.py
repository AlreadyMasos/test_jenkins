from third_task.Base.Elements.Button import Button
from third_task.Base.BasePage import BaseForm
from third_task.Base.Elements.Alert import Alert
from third_task.Base.Elements.TextField import TextField
from third_task.page_objects.left_panel import LeftPanel
from third_task.resourses.utils import compare_text, random_string
from third_task.resourses.logger import log
import logging


class AlertsPage(BaseForm):
    logs = log(logging.DEBUG)
    _to_see_alert_button = Button('//button[@id="alertButton"]', 'xpath')
    _confirm_box_button = Button('//button[@id="confirmButton"]', 'xpath')
    _prompt_box_button = Button('//button[@id="promtButton"]', 'xpath')
    _text_ok = TextField('//span[@class="text-success"]', 'xpath')
    _text_rand = TextField('//span[@id="promptResult"]', 'xpath')
    left_panel = LeftPanel()

    def __init__(self):
        super().__init__(self._to_see_alert_button)

    def click_alerts_button(self):
        self.left_panel.alerts_button_click()

    def click_nested_frames_button(self):
        self.left_panel.click_nested_frames_button()

    def click_frames_button(self):
        self.left_panel.click_frames_button()

    def click_to_see_alert_button(self):
        self._to_see_alert_button.element_click()

    def click_confirm_box_button(self):
        self._confirm_box_button.element_click()

    def click_promt_box_button(self):
        self._prompt_box_button.element_click()

    def get_rand_text(self):
        return self._text_rand.get_text()
