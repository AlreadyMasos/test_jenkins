from third_task.Base.BaseElement import BaseElement
from selenium.webdriver.common.keys import Keys


class Slider(BaseElement):

    def get_current_value(self):
        elem = self.find_element()
        return elem.get_attribute('value')

    def change_value(self, value, default_value = 25):
        for i in range(default_value):
            self.find_element().send_keys(Keys.LEFT)
        for i in range(value):
            self.find_element().send_keys(Keys.RIGHT)
