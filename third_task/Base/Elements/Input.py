from third_task.Base.BaseElement import BaseElement
from selenium.common.exceptions import TimeoutException
from third_task.resourses.logger import log
import logging


class Input(BaseElement):
    logs = log(logging.DEBUG)

    def sendkeys(self, text):
        try:
            self.logs.info('Keys sended to input')
            element = self.find_element()
            element.send_keys(text)
        except TimeoutException:
            self.logs.error('Timeout exception when try to send keys to input')
            return False

    def get_value(self):
        return self.find_element().get_attribute('value')
