from third_task.Base.Elements.Button import Button
from third_task.Base.BasePage import BaseForm
from third_task.resourses.logger import log
from third_task.page_objects.left_panel import LeftPanel
from third_task.resourses.browser_manager import Browser
import logging


class MainPage(BaseForm):
    logs = log(logging.DEBUG)
    _alert_button = Button('//div[@class="card mt-4 top-card"][3]', 'xpath')
    _elements_button = Button('//div[@class="card mt-4 top-card"][1]', 'xpath')
    _widgets_button = Button('//div[@class="card mt-4 top-card"][4]', 'xpath')
    _left_panel = LeftPanel()

    def __init__(self):
        super().__init__(self._elements_button)

    def click_alerts_button(self):
        self._alert_button.element_click()

    def click_elements_button(self):
        self._elements_button.wait_until_loaded()
        self._elements_button.element_click()

    def click_widgets_button(self):
        self._widgets_button.wait_until_loaded()
        self._widgets_button.element_click()

    def click_slider_button(self):
        Browser.scroll_down()
        self._left_panel.click_slider_button()
