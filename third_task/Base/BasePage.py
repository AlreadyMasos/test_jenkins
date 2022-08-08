from selenium.common.exceptions import TimeoutException
from third_task.Base.BaseElement import BaseElement
from third_task.resourses.logger import log
import logging


class BaseForm:
    logs = log(logging.DEBUG)

    def __init__(self, element):
        self.uniqElem = BaseElement(element.locator_name, element.locator_type)

    def check_load(self):
        try:
            self.uniqElem.wait_until_loaded()
            self.logs.info('Try to check page load')
            return True if len(self.uniqElem.find_elements()) > 0 else False
        except TimeoutException:
            self.logs.error('Page not loaded')
            return False
