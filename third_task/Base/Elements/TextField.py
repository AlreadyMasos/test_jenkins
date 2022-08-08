from third_task.Base.BaseElement import BaseElement
from third_task.resourses.logger import log
import logging


class TextField(BaseElement):
    logs = log(logging.DEBUG)

    def get_text(self):
        try:
            self.logs.info('got text field text')
            return self.find_element().text
        except:
            self.logs.error('error when try to get text from textfield')