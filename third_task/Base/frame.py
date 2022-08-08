from third_task.Base.BaseElement import BaseElement
from third_task.resourses.singldriver import driver


class IFrame(BaseElement):

    def switch_to_frame(self):
        driver.switch_to.frame(self.find_element())

    @staticmethod
    def switch_to_def():
        driver.switch_to.default_content()
