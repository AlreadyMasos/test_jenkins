from third_task.Base.BasePage import BaseForm
from third_task.Base.Elements.TextField import TextField
from third_task.resourses.browser_manager import Browser
from third_task.resourses.logger import log
import logging


class LinksPage(BaseForm):
    logs = log(logging.DEBUG)
    _home_link = TextField("//a[@id='simpleLink' and text()='Home']", 'xpath')
    b = Browser()

    def __init__(self):
        super().__init__(self._home_link)

    def home_link_click(self):
        self._home_link.wait_until_loaded()
        self._home_link.element_click()
