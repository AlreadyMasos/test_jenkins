from third_task.Base.Elements.Button import Button
from third_task.Base.BasePage import BaseForm
from third_task.resourses.browser_manager import Browser
from third_task.resourses.utils import data, compare_text
from third_task.resourses.logger import log
import logging


class HandlePage(BaseForm):
    logs = log(logging.DEBUG)
    _alerts_button = Button('//div[@class="card mt-4 top-card"][3]', 'xpath')
    _browser_win_button = Button('//span[contains(text(), "Browser Windows")]', 'xpath')
    _new_tab_button = Button('//button[@id="tabButton"]', 'xpath')
    _elements_button = Button("//div[@class='element-group'][1]", 'xpath')
    _links_button = Button("//span[@class='text' and text()='Links']", 'xpath')

    def __init__(self):
        super().__init__(self._browser_win_button)

    def browser_win_click(self):
        self._browser_win_button.element_click()

    def alerts_button_click(self):
        self._alerts_button.element_click()

    def click_new_tab_button(self):
        self._new_tab_button.element_click()

    def check_new_tab(self):
        return compare_text(Browser.get_tab_url(), data['links']['sample_page'])

    def links_button_click(self):
        self._elements_button.element_click()
        Browser.scroll_down()
        self._links_button.wait_until_loaded()
        self._links_button.element_click()
